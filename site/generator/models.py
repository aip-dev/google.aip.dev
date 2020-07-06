# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from typing import Any, Dict, List, Optional, Set, Tuple, Union
import collections
import dataclasses
import datetime
import io
import os
import uuid

import jinja2
import yaml

from generator import md
from generator.env import jinja_env

BASEDIR = os.path.realpath(os.path.join(os.path.dirname(__file__), '..', '..'))
AIP_DIR = os.path.join(BASEDIR, 'aip')
SITE_DIR = os.path.join(BASEDIR, 'site')
DATA_DIR = os.path.join(SITE_DIR, 'data')


@dataclasses.dataclass
class Change:
    date: datetime.date
    message: str

    def __hash__(self):
        return hash(str(self))

    def __lt__(self, other: 'Change'):
        # We sort changes in reverse-cron, so a later date is "less" here.
        return self.date > other.date

    def __str__(self):
        return f'{self.date.isoformat()}: {self.message}'


@dataclasses.dataclass
class AIP:
    id: int
    state: str
    created: datetime.date
    scope: str
    legacy: bool = False
    fragments: List[str] = dataclasses.field(default_factory=list)
    changelog: Set[Change] = dataclasses.field(default_factory=set)
    data: Dict[str, Any] = dataclasses.field(default_factory=dict)

    @classmethod
    def load(cls, scope: str, id: int) -> 'AIP':
        """Load an AIP object from the given directory and return it."""
        # First, get the meta file and create the AIP object based on it.
        abs_dir = os.path.join(AIP_DIR, scope, f'{id:04d}')
        meta = yaml.safe_load(io.open(os.path.join(abs_dir, 'meta.yaml'), 'r'))
        aip = cls(
            id=meta.pop('id'),
            state=meta.pop('state'),
            created=meta.pop('created'),
            scope=meta.pop('scope', 'general'),
            data=meta,
        )

        # Next, iterate over the Markdown contents and injest them.
        for f in sorted([os.path.join(abs_dir, i) for i
                         in os.listdir(abs_dir) if i.endswith('.md')]):
            aip._injest_fragment(f)

            # Check for an equivalent YAML file and load it if there is one.
            if os.path.exists(y := f.replace('.md', '.yaml')):
                aip._injest_changelog(y)

        # Done; return the AIP object.
        return aip

    @classmethod
    def load_legacy(cls, scope: str, id: int) -> 'AIP':
        """Load an AIP object from the original location and parse it."""
        # Load the AIP Markdown file.
        path = os.path.join(AIP_DIR, scope, f'{id:04d}.md')
        with io.open(path, 'r') as f:
            jekyll_content = f.read()

        # Parse and coerce the front matter at the top of the file to
        # match the new format.
        fm, content = jekyll_content.lstrip('-\n').split('---\n', maxsplit=1)
        meta = yaml.safe_load(fm)['aip']

        # Return the AIP.
        return cls(
            id=meta.pop('id'),
            state=meta.pop('state'),
            created=meta.pop('created'),
            scope=meta.pop('scope', scope),
            data=meta,
            fragments=[content],
            legacy=True,
        )

    def __getattr__(self, name: str):
        try:
            return self.data[name]
        except KeyError as ex:
            raise AttributeError(str(ex))

    @property
    def content(self) -> md.MarkdownDocument:
        if not hasattr(self, '_md_content'):
            answer = '\n\n'.join(self.fragments)
            if self.changelog:
                answer += '\n\n## Changelog\n\n'
                for cl in sorted(self.changelog):
                    answer += f'- **{cl.date}:** {cl.message}\n'
            self._md_content = md.MarkdownDocument(answer)
        return self._md_content

    @property
    def placement(self) -> Dict[str, Any]:
        """Return the placement data for this AIP, or sensible defaults."""
        return self.data.get('placement', {
            'category': 'misc',
            'order': float('inf'),
        })

    @property
    def redirects(self) -> Set[str]:
        uris = {f'/{self.id:04d}', f'/{self.id:03d}', f'/{self.id:02d}'}
        uris = uris.difference({self.relative_uri})
        if 'redirect_from' in self.data:
            uris.add(self.data['redirect_from'])
        return uris

    @property
    def relative_uri(self) -> str:
        """Return the relative URI for this AIP."""
        if self.scope != 'general':
            return f'/{self.scope}/{self.id}'
        return f'/{self.id}'

    @property
    def repo_path(self) -> str:
        """Return the relative path in the GitHub repository."""
        return f'/aip/{self.scope}/{self.id:04d}.md'

    @property
    def title(self) -> str:
        """Return the AIP title."""
        return self.content.title

    @property
    def updated(self):
        """Return the most recent date on the changelog.

        If there is no changelog, return the created date instead.
        """
        if self.changelog:
            return sorted(self.changelog)[0].date
        return self.created

    def render(self):
        """Return the fully-rendered page for this AIP."""
        return jinja_env.get_template('aip.html.j2').render(
            aip=self,
            site=dataclasses.replace(Site.load(path=self.relative_uri))
        )

    def _injest_fragment(self, filename: str):
        """Injest a fragment of an AIP into the object.

        This both appends the content and adds the appropriate header to
        the table of contents.
        """
        with io.open(filename, 'r') as f:
            snippet: str = f.read()
        self.fragments.append(snippet.lstrip())

    def _injest_changelog(self, filename: str):
        """Injest a fragment of an AIP changelog into the object."""
        with io.open(filename, 'r') as f:
            conf = yaml.safe_load(f)
        for cl in conf.get('changelog', ()):
            self.changelog.add(Change(**cl))


@dataclasses.dataclass
class Site:
    base_url: str
    repo_url: str
    revision: str
    path: Optional[str] = None
    data: Dict[str, Any] = dataclasses.field(default_factory=dict)

    @classmethod
    def load(cls, path: Optional[str] = None) -> 'Site':
        # Load the configuration.
        with io.open(os.path.join(SITE_DIR, 'config.yaml'), 'r') as f:
            config = yaml.safe_load(f)

        # Load all site data.
        data: Dict[str, Any] = {}
        for filename in os.listdir(DATA_DIR):
            with io.open(os.path.join(DATA_DIR, filename), 'r') as f:
                data[filename[:-5]] = yaml.safe_load(f)

        # Return a new Site object.
        return cls(
            base_url=config.get('base_url', ''),
            data=data,
            path=path,
            revision=str(uuid.uuid4())[-8:],
            repo_url=config.get('repo_url', jinja2.Undefined()),
        )

    @property
    def aips(self) -> Dict[Union[str, int], AIP]:
        """Return all the AIPs in the site."""
        if not hasattr(self, '_aips'):
            answer = collections.OrderedDict()
            for scope in self.scopes.values():
                for id, aip in scope.aips.items():
                    answer[id] = aip
            self._aips = answer
        return self._aips

    @property
    def news(self) -> Dict[str, 'Page']:
        """Return all the news pages in the site."""
        if not hasattr(self, '_news'):
            answer = collections.OrderedDict()
            news_dir = os.path.join(BASEDIR, 'news')
            for filename in sorted(os.listdir(news_dir), reverse=True):
                if not filename.endswith('.md'):
                    continue
                year, month = (int(i) for i in filename[:-3].split('-'))
                answer[f'{year}-{month:02d}'] = Page.load_news(year, month)
            self._news = answer
        return self._news

    @property
    def pages(self) -> Dict[str, 'Page']:
        """Return all of the static pages in the site."""
        if not hasattr(self, '_pages'):
            answer = {'contributing': Page.load('contributing')}
            page_dir = os.path.join(SITE_DIR, 'pages')
            for filename in os.listdir(page_dir):
                if not filename.endswith(('.md', '.md.j2')):
                    continue
                code = filename.split('.')[0]
                answer[code] = Page.load(code)
            self._pages = answer
        return self._pages

    @property
    def relative_uri(self) -> str:
        return '/{}'.format('/'.join(self.base_url.split('/')[3:])).rstrip('/')

    @property
    def scopes(self) -> Dict[str, 'Scope']:
        """Return all of the AIP scopes present in the site."""
        if not hasattr(self, '_scopes'):
            answer_list = []
            for filename in os.listdir(AIP_DIR):
                # If there is a meta.yaml file, then this is a scope directory
                # and we add it to our list.
                scope_file = os.path.join(AIP_DIR, filename, 'meta.yaml')
                if not os.path.exists(scope_file):
                    continue
                scope = Scope.load(os.path.join(AIP_DIR, filename))

                # Append the scope to our list.
                answer_list.append(scope)

            # Create an ordered dictionary of scopes.
            answer = collections.OrderedDict()
            for scope in sorted(answer_list, key=lambda i: i.order):
                answer[scope.code] = scope
            self._scopes = answer
        return self._scopes


@dataclasses.dataclass
class Page:
    code: str
    content: md.MarkdownDocument
    config: Dict[str, Any] = dataclasses.field(default_factory=dict)

    @classmethod
    def load(cls, code: str) -> 'Page':
        """Load a support page and return a new Page object."""
        # Get the path of the Markdown file.
        #
        # Note: CONTRIBUTING.md is a special case because it is really
        # important to store it at the root where people can find it on GitHub.
        path = os.path.join(SITE_DIR, 'pages', f'{code}.md')
        if code == 'contributing':
            path = os.path.join(BASEDIR, 'CONTRIBUTING.md')
        if os.path.exists(path + '.j2'):
            path += '.j2'

        # Load the file and read the content.
        with io.open(path, 'r') as f:
            content = f.read()

        # If the path is a Jinja template, resolve the content.
        # Only the site is sent as context in this case.
        if path.endswith('.j2'):
            content = jinja_env.from_string(content).render(site=Site.load())

        # Check for a config file. If one exists, load it too.
        config_file = os.path.join(SITE_DIR, 'pages', f'{code}.yaml')
        config = {}
        if os.path.exists(config_file):
            with io.open(config_file, 'r') as f:
                config = yaml.safe_load(f)

        # Return the page.
        return cls(
            code=code,
            config=config,
            content=md.MarkdownDocument(content),
        )

    @classmethod
    def load_news(cls, year: int, month: int) -> 'Page':
        """Load a newsletter page and return a new Page object."""
        # Load the Markdown file and read the content.
        path = os.path.join(BASEDIR, 'news', f'{year}-{month:02d}.md')
        with io.open(path, 'r') as f:
            content = f.read()

        # Check for a config file. If one exists, load it too.
        config_file = path.replace('.md', '.yaml')
        config = {}
        if os.path.exists(config_file):
            with io.open(config_file, 'r') as f:
                config = yaml.safe_load(f)

        # Return the page.
        return cls(
            code=f'news/{year}-{month:02d}',
            config=config,
            content=md.MarkdownDocument(content),
        )

    @property
    def relative_uri(self) -> str:
        return f'/{self.code}'

    @property
    def repo_path(self) -> str:
        if self.code == 'contributing':
            return '/CONTRIBUTING.md'
        return f'/site/pages/{self.code}.md'

    @property
    def title(self) -> str:
        """Return the page title."""
        return self.content.title

    def render(self) -> str:
        return jinja_env.get_template('page.html.j2').render(
            page=self,
            site=dataclasses.replace(Site.load(path=self.relative_uri))
        )


@dataclasses.dataclass
class Category:
    code: str
    title: str
    order: int
    aips: Tuple[AIP]


@dataclasses.dataclass
class Scope:
    directory: str
    code: str
    title: str
    order: int
    data: Dict[str, Any] = dataclasses.field(default_factory=dict)

    @classmethod
    def load(cls, directory: str) -> 'Scope':
        with io.open(os.path.join(directory, 'meta.yaml'), 'r') as f:
            conf = yaml.safe_load(f)
        code = conf.pop('code', directory.rstrip('/').split('/')[-1])
        return cls(
            directory=directory,
            code=code,
            title=conf.pop('title', code.capitalize()),
            order=conf.pop('order', float('inf')),
            data=conf,
        )

    def __getattr__(self, name):
        try:
            return self.data[name]
        except KeyError as ex:
            raise AttributeError(str(ex))

    @property
    def aips(self) -> Dict[int, AIP]:
        """Return a dict of AIPs, sorted by number."""
        if not hasattr(self, '_aips'):
            answer = []
            for filename in os.listdir(self.directory):
                aip_dir = os.path.join(self.directory, filename)

                # Load new-style AIPs.
                if os.path.exists(os.path.join(aip_dir, 'meta.yaml')):
                    answer.append(AIP.load(self.code, int(filename)))

                # Load legacy AIPs.
                if filename.endswith('.md') and filename != 'index.md':
                    aip_id = int(filename[:-3])
                    answer.append(AIP.load_legacy(self.code, aip_id))

            answer = sorted(answer, key=lambda i: i.id)
            self._aips = collections.OrderedDict([(i.id, i) for i in answer])
        return self._aips

    @property
    def categories(self) -> Dict[str, 'Category']:
        if not hasattr(self, '_categories'):
            # There may be no categories. This is fine; just "fake" a single
            # category based on the scope.
            #
            # This is guaranteed to have all AIPs, so just return immediately
            # and skip remaining processing.
            if not self.data.get('categories', None):
                self._categories = {self.code: Category(
                    code=self.code,
                    title=self.title,
                    order=0,
                    aips=tuple(self.aips.values()),
                )}
                return self._categories

            # Iterate over each category and piece together the AIPs in order.
            cats = collections.OrderedDict()
            for ix, cat in enumerate(self.data['categories']):
                # Determine what AIPs are in this category.
                aips = []
                for aip in self.aips.values():
                    if aip.placement.get('category', 'misc') != cat['code']:
                        continue
                    aips.append(aip)
                aips = tuple(sorted(aips,
                    key=lambda i: i.placement.get('order', float('inf')),
                ))

                # Create the category object and add it.
                cats[cat['code']] = Category(
                    code=cat['code'],
                    title=cat.get('title', cat['code'].capitalize()),
                    order=ix,
                    aips=aips,
                )
            self._categories = cats
        return self._categories

    @property
    def relative_uri(self) -> str:
        return f'/{self.code}'

    def render(self):
        """Render the page for this scope."""
        return jinja_env.get_template('aip-listing.html.j2').render(
            scope=self,
            site=dataclasses.replace(Site.load(path=self.relative_uri))
        )
