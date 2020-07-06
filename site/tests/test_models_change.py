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

from generator.models import Change


def test_ordering():
    a = Change(date=date(2012, 4, 21), message='foo')
    b = Change(date=date(2020, 4, 21), message='bar')
    assert a > b


def test_set():
    a = Change(date=date(2012, 4, 21), message='foo')
    b = Change(date=date(2020, 4, 21), message='bar')
    assert len({a, a, b, b}) == 2
