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

import markdown
import pymdownx.highlight
import pymdownx.superfences


class MarkdownDocument(str):
    """A utility class representing Markdown content."""

    def __init__(self, content: str, *, toc_title: str = 'Contents'):
        self._content = content
        self._engine = markdown.Markdown(
            extensions=[_superfences, 'toc'],
            extension_configs={
                'toc': {
                    'title': toc_title,
                    'toc_depth': '2-3',
                },
            },
            tab_length=2,
        )

    def __str__(self) -> str:
        return self._content

    @property
    def html(self) -> str:
        """Return the HTML content for this Markdown document."""
        if not hasattr(self, '_html'):
            self._html = self._engine.convert(self._content)
        return self._html

    @property
    def title(self) -> str:
        """Return the document title."""
        return self._content.strip().splitlines()[0].strip('# \n')

    @property
    def toc(self) -> str:
        """Return a table of contents for the Markdown document."""
        # We need to fire the html property because conversion may not have
        # happened yet, and the toc extension requires conversion to occur
        # first.
        #
        # The `html` property caches, so this does not entail any additional
        # performance hit.
        self.html
        return self._engine.toc


def _fmt(src: str, lang: str, css_class: str, *args, **kwargs):
    """Custom Markdown formatter that retains language classes."""
    highlighter = pymdownx.highlight.Highlight(guess_lang=False)
    return highlighter.highlight(src, lang, f'{css_class} language-{lang}')


# Define the superfences extension.
# We need a custom fence to maintain useful language-specific CSS classes.
_superfences = pymdownx.superfences.SuperFencesCodeExtension(
    custom_fences=[{
        'name': '*',
        'class': 'highlight',
        'format': _fmt,
    }],
)
