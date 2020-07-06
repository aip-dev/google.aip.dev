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

import textwrap

import pytest

from generator import md


@pytest.fixture
def markdown_doc():
    return md.MarkdownDocument(textwrap.dedent("""
        # Title

        This is an intro paragraph.

        ## Sub 1

        Stuff and things, things and stuff.

        ### Drilling down

        This had a deeper item.

        ```python
        # This is a code example.
        ```

        ### Still drilling

        Drill drill drill

        ## Sub 2

        Weeeee
    """).strip())


def test_coerce(markdown_doc):
    assert '# Title' in markdown_doc
    assert '# Title' in str(markdown_doc)


def test_html(markdown_doc):
    assert '<h1>Title</h1>' in markdown_doc.html
    assert '<h2 id="sub-1">Sub 1</h2>' in markdown_doc.html
    assert '<h3 id="still-drilling">Still drilling</h3>' in markdown_doc.html
    assert '<p>Stuff and things, things and stuff.</p>' in markdown_doc.html
    assert '<div class="highlight language-python">' in markdown_doc.html
    assert markdown_doc.html is markdown_doc.html


def test_title(markdown_doc):
    assert markdown_doc.title == 'Title'


def toc(markdown_doc):
    assert 'Sub 1' in markdown_doc.toc
    assert 'Drilling down' in markdown_doc.toc
    assert 'Still drilling' in markdown_doc.toc
    assert 'Sub 2' in markdown_doc.toc
    assert 'Title' not in markdown_doc.toc  # Note: not in.
    assert 'Stuff and things' not in markdown_doc.toc
