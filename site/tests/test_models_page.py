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
import os
import textwrap

import pytest

from generator import md
from generator import models
from tests import mocks


@mock.patch.object(os.path, 'exists', mock.Mock(return_value=False))
def test_load():
    mock_open = mock.mock_open(read_data=textwrap.dedent("""
        # About

        We are awesome! Woohoo!
    """).strip())
    with mock.patch.object(io, 'open', mock_open):
        page = models.Page.load('about')
    assert page.code == 'about'
    assert page.title == 'About'
    assert 'Woohoo!' in page.content


@mock.patch.object(os.path, 'exists', mock.Mock(side_effect=(True, False)))
def test_load_template():
    mock_open = mock.mock_open(read_data=textwrap.dedent("""
        # Template

        The path value is {{ site.path }}.
    """).strip())
    mock_site = mocks.Site.load(path='/foo')
    with mock.patch.object(models.Site, 'load', return_value=mock_site):
        with mock.patch.object(io, 'open', mock_open):
            page = models.Page.load('about')
    assert page.code == 'about'
    assert page.title == 'Template'
    assert 'value is /foo.' in page.content


@mock.patch.object(os.path, 'exists', mock.Mock(return_value=False))
def test_load_contributing():
    mock_open = mock.mock_open(read_data=textwrap.dedent("""
        # Contributing

        We welcome your contributions, yo!
    """).strip())
    with mock.patch.object(io, 'open', mock_open):
        page = models.Page.load('contributing')
        assert mock_open.mock_calls[0][1][0].endswith('CONTRIBUTING.md')
    assert page.code == 'contributing'
    assert page.title == 'Contributing'
    assert 'your contributions' in page.content


@mock.patch.object(os.path, 'exists', mock.Mock(side_effect=(False, True)))
def test_load_with_config():
    content = textwrap.dedent("""
        # Static page

        With static stuff.
    """).strip()
    config = textwrap.dedent("""
        ---
        foo: bar
        baz: 2012-04-21
    """).strip()
    with mock.patch.object(io, 'open', mock.mock_open()) as m:
        m().read.side_effect = (content, config)
        page = models.Page.load('static-page')
    assert page.code == 'static-page'
    assert page.title == 'Static page'
    assert page.config['foo'] == 'bar'
    assert page.config['baz'] == date(2012, 4, 21)


@mock.patch.object(os.path, 'exists', mock.Mock(return_value=False))
def test_load_news():
    content = mock.mock_open(read_data=textwrap.dedent("""
        # Breaking news!

        All the news that is fit to print.
    """).strip())
    with mock.patch.object(io, 'open', content):
        page = models.Page.load_news(2012, 4)
    assert page.code == 'news/2012-04'
    assert page.relative_uri == '/news/2012-04'
    assert page.title == 'Breaking news!'


@mock.patch.object(os.path, 'exists', mock.Mock(return_value=True))
def test_load_news_with_config():
    content = textwrap.dedent("""
        # Static page

        With static stuff.
    """).strip()
    config = textwrap.dedent("""
        ---
        foo: bar
        baz: 2012-04-21
    """).strip()
    with mock.patch.object(io, 'open', mock.mock_open()) as m:
        m().read.side_effect = (content, config)
        page = models.Page.load_news(2012, 4)
    assert page.code == 'news/2012-04'
    assert page.title == 'Static page'
    assert page.config['foo'] == 'bar'
    assert page.config['baz'] == date(2012, 4, 21)


@pytest.fixture
def page():
    return models.Page(
        code='about',
        content=md.MarkdownDocument('# About\n\nWe are awesome!'),
    )


def test_relative_uri(page):
    assert page.relative_uri == '/about'


def test_repo_path(page):
    contrib = dataclasses.replace(page, code='contributing')
    assert page.repo_path == '/site/pages/about.md'
    assert contrib.repo_path == '/CONTRIBUTING.md'


def test_render(page):
    with mock.patch.object(models, 'Site', mocks.Site):
        rendered = page.render()
    assert '<h1>About</h1>' in rendered
    assert '<p>We are awesome!</p>' in rendered


def test_title(page):
    assert page.title == 'About'
