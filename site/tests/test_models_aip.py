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

from datetime import date
from unittest import mock
import dataclasses
import io
import textwrap

import pytest

from generator import models
from tests import mocks


def test_load():
    aip_file = mock.mock_open(read_data=textwrap.dedent("""
        ---
        aip:
            id: 42
            state: reviewing
            created: 2012-04-21
        ---
        # The Answer

        To life, the universe, and everything.
    """).strip())
    with mock.patch.object(io, 'open', aip_file) as m:
        aip = models.AIP.load_legacy('general', 42)
        m.assert_called_once_with(f'{models.AIP_DIR}/general/0042.md', 'r')
    assert aip.id == 42
    assert aip.state == 'reviewing'
    assert aip.created == date(2012, 4, 21)
    assert aip.title == 'The Answer'


@pytest.fixture
def aip():
    return models.AIP(
        id=421,
        state='approved',
        created=date(2012, 4, 21),
        scope='general',
        fragments=[
            '# Design\n\nWhen designing an API, you need a good design.',
            '## Guidance\n\nDesign well.',
        ],
        changelog={
            models.Change(date=date(2020, 4, 21), message='Lorem ipsum.')
        },
        data={'foo': 'bar'},
    )


def test_content(aip):
    assert aip.content.strip() == textwrap.dedent("""
        # Design

        When designing an API, you need a good design.

        ## Guidance

        Design well.

        ## Changelog

        - **2020-04-21:** Lorem ipsum.
    """).strip()


def test_placement_default(aip):
    assert aip.placement == {
        'category': 'misc',
        'order': float('inf'),
    }


def test_redirects(aip):
    assert aip.redirects == {'/0421'}
    aip.data['redirect_from'] = '/special-entrypoint'
    assert aip.redirects == {'/0421', '/special-entrypoint'}


def test_relative_uri(aip):
    other = dataclasses.replace(aip, scope='other')
    assert aip.relative_uri == '/421'
    assert other.relative_uri == '/other/421'


def test_render(aip):
    with mock.patch.object(models, 'Site', mocks.Site):
        rendered = aip.render()
        print(rendered)
        assert '<h1>Design</h1>' in rendered
        assert '<h2 id="guidance">Guidance</h2>' in rendered
        assert '<h2 id="changelog">Changelog</h2>' in rendered


def test_repo_path(aip):
    assert aip.repo_path == '/aip/general/0421.md'


def test_title(aip):
    assert aip.title == 'Design'


def test_updated(aip):
    never_updated = dataclasses.replace(aip, changelog=set())
    assert aip.updated == date(2020, 4, 21)
    assert never_updated.updated == date(2012, 4, 21)
