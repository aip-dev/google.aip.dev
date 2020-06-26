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

import os

import jinja2

from generator import md


TEMPLATE_DIR = os.path.realpath(
    os.path.join(os.path.dirname(__file__), '..', 'templates'),
)


jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(searchpath=TEMPLATE_DIR),
    undefined=jinja2.StrictUndefined,
)
jinja_env.filters['markdown'] = lambda s: md.MarkdownDocument(s).html
