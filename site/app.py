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

import dataclasses
import re

from flask import Flask, render_template, request, Response
from scss.compiler import compile_file

from generator import env
from generator import models


app = Flask(__name__)
app.jinja_env = env.jinja_env


@app.route('/')
def hello():
    return render_template('index.html.j2', site=models.Site.load())


@app.route('/<int:aip_id>')
def aip(aip_id: int):
    """Display a single AIP document."""
    return models.Site.load().aips[aip_id].render()


@app.route('/news/<int:year>-<int:month>')
def news(year: int, month: int):
    """Display a single news document."""
    return models.Site.load().news[f'{year:04d}-{month:02d}'].render()


@app.route('/search')
def search():
    """Display the search page."""
    return render_template('search.html.j2',
        site=dataclasses.replace(models.Site.load(), path=request.path),
    )


@app.route('/<page>')
def page(page: str):
    """Display a static page or listing of AIPs in a given scope."""
    site = models.Site.load()
    if page in site.scopes:
        return site.scopes[page].render()
    return site.pages[page].render()


@app.route('/static/css/<path:css_file>')
def scss(css_file: str):
    """Compile the given SCSS file and return it."""
    scss_file = re.sub(r'\.css$', '.scss', css_file)
    return Response(compile_file(f'scss/{scss_file}'), mimetype='text/css')


@app.route('/static/js/search/tipuesearch_content.js')
def search_content():
    """Compile the search content JavaScript and return it."""
    return Response(
        render_template('search.js.j2', site=models.Site.load()),
        mimetype='text/javascript',
    )
