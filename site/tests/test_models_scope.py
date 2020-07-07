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

from unittest import mock
import io

import pytest

from generator import models
from tests import mocks


def test_load():
    config = mocks.file("""
        ---
        title: My Scope
        order: 85
    """)
    with mock.patch.object(io, 'open', config) as o:
        scope = models.Scope.load('my-scope')
        o.assert_called_once_with('my-scope/meta.yaml', 'r')
    assert scope.code == 'my-scope'
    assert scope.title == 'My Scope'
    assert scope.order == 85


@pytest.fixture
def scope():
    return models.Scope(
        directory='general',
        code='general',
        title='General',
        order=0,
        data={},
    )


def test_relative_uri(scope):
    assert scope.relative_uri == '/general'


def test_render(scope):
    with mock.patch.object(models, 'Site', mocks.Site):
        scope._aips = {}
        rendered = scope.render()
    assert '<title>General AIPs</title>' in rendered
