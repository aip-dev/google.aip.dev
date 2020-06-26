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

from typing import Union
import dataclasses
import io
import os
import re
import shutil
import sys

from scss.compiler import compile_file
import click

from generator import models
from generator import env


class Publisher:
    """Class for writing the AIP site out to disk."""

    def __init__(self, output_dir, *, log_to_stdout=False):
        self.output_dir = output_dir.rstrip(os.path.sep)
        self.log_to_stdout = log_to_stdout
        self.site = models.Site.load()

    def log(self, message: str, *, err: bool = False):
        """Conditionally log a message."""
        dest = sys.stderr if err else sys.stdout
        if self.log_to_stdout:
            print(f'{message}', file=dest)

    def publish_site(self):
        """Publish the full site."""
        for page in self.site.pages.values():
            self.publish_doc(page)
        for news in self.site.news.values():
            self.publish_doc(news)
        for scope in self.site.scopes.values():
            self.publish_doc(scope)
        for aip in self.site.aips.values():
            self.publish_doc(aip)
        self.publish_template('index.html.j2', 'index.html')
        self.publish_template('search.html.j2', 'search.html')
        self.publish_static()
        self.publish_template(
            'search.js.j2',
            'static/js/search/tipuesearch_content.js',
        )
        self.publish_css()

    def publish_doc(self, doc: Union[models.AIP, models.Scope, models.Page]):
        """Publish a single AIP document to disk."""
        # Determine the path and make sure the directory exists.
        path = f'{self.output_dir}{doc.relative_uri}.html'
        os.makedirs(os.path.dirname(path), exist_ok=True)

        # Write the document's file to disk.
        with io.open(path, 'w') as f:
            f.write(doc.render())
        self.log(f'Successfully wrote {path}.')

        # If this document has any redirects (only AIPs do as of this writing),
        # write out the redirect files to disk also.
        for redirect in getattr(doc, 'redirects', set()):
            rpath = f'{self.output_dir}{redirect}.html'
            with io.open(rpath, 'w') as f:
                f.write(env.jinja_env.get_template('redirect.html.j2').render(
                    site=self.site,
                    target=doc,
                ))
            self.log(f'Successfully wrote {rpath} (redirect).')

    def publish_template(self, tmpl: str, path: str):
        """Publish a site-wide template to a particular path."""
        path = f'{self.output_dir}{os.path.sep}{path}'
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with io.open(path, 'w') as f:
            f.write(env.jinja_env.get_template(tmpl).render(
                site=dataclasses.replace(self.site, path=path.split('.')[0]),
            ))
        self.log(f'Successfully wrote {path}.')

    def publish_static(self):
        """Copy the static directory."""
        shutil.copytree(
            src=os.path.join(models.SITE_DIR, 'static'),
            dst=os.path.join(self.output_dir, 'static'),
            dirs_exist_ok=True,
        )
        self.log('Successfully wrote static files.')

    def publish_css(self):
        """Compile and publish all SCSS files in the root SCSS directory."""
        scss_path = os.path.join(models.SITE_DIR, 'scss')
        css_path = os.path.join(self.output_dir, 'static', 'css')
        os.makedirs(css_path, exist_ok=True)
        for scss_file in os.listdir(scss_path):
            if not scss_file.endswith('.scss'):
                continue
            css_file = os.path.join(
                css_path,
                re.sub(r'\.scss$', '.css', scss_file),
            )
            with io.open(css_file, 'w') as f:
                f.write(compile_file(os.path.join(scss_path, scss_file)))
            self.log(f'Successfully wrote {css_file}.')


@click.command()
@click.argument('output_dir', type=click.Path(
    allow_dash=False,
    dir_okay=True,
    exists=False,
    file_okay=False,
    writable=True))
def publish(output_dir: str):
    """Publish static HTML pages into the specified location."""
    publisher = Publisher(output_dir, log_to_stdout=True)
    publisher.publish_site()


if __name__ == '__main__':
    publish()
