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

from typing import Optional
from unittest import mock
import uuid
import textwrap

from generator import models


def file(text: str):
    return mock.mock_open(read_data=textwrap.dedent(text).strip() + '\n')


class Site(models.Site):
    @classmethod
    def load(cls, path: Optional[str] = None) -> 'Site':
        return cls(
            base_url='https://aip.dev',
            data={'header': {'links': []}},
            path=path,
            revision=str(uuid.uuid4())[-8:],
            repo_url='https://github.com/aip-dev/aip'
        )

    @property
    def aips(self):
        return {}

    @property
    def news(self):
        return {}

    @property
    def pages(self):
        return {}

    @property
    def scopes(self):
        return {'general': Scope.load('general')}


class Scope(models.Scope):
    @classmethod
    def load(cls, directory: str) -> 'Scope':
        return cls(
            directory=directory,
            code=directory,
            order=0,
            title=directory.capitalize(),
            data={},
        )

    @property
    def aips(self):
        return {}
