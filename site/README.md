# aip.dev static site generator

Welcome to our NIH static site generator.

**Note:** If you do not care about this and just want to write or modify AIPs,
see `CONTRIBUTING.md`.

## Why?

GitHub Pages normally automatically builds documentation with [Jekyll][], but
as the AIP system has grown, we are beginning to reach the limits of what
Jekyll can handle:

- AIP adoption is handled through fork-and-merge and top-down configuration
  files will lead to repetitive merge conflicts.
- Our grouping and listing logic has grown complicated, and had to be
  maintained using complex and error-prone Liquid templates.
- Jekyll is extensible but GitHub requires specific Jekyll plugins, meaning we
  can not use off-the-shelf solutions for planned features (e.g. tabbed code
  examples).
- Lack of meaningful build CI caused failures.
- Working with the development environment was (really) slow.

## Grumble. Fine. How does it work?

The app is essentially split up into models (`generator/models.py`) and
templates (`templates/`). The models file provides data classes that are sent
to the templates and which have convenient accessors for template needs (title,
relative URI, etc.)

There are three models that matter:

- **Site:** A singleton (ish) that provides access to all scopes, AIPs, and
  static pages. This is sent to every template as the `site` variable.
- **AIP:** A representation of a single AIP, including both content and
  metadata. This is sent to the AIP rendering template as the `aip` variable.
- **Scope:** A group of AIPs that apply to a particular scope. The "general"
  scope is special, and is the "root" group. This is sent to the AIP _listing_
  template as the `scope` variable.

Templates are [jinja2][] files in the `templates/` directory.

**Note:** We run Jinja in with "strict undefined", so referencing an undefined
variable in a template is a hard error rather than an empty string.

### Entry points

There are two entry points for the app. The _publisher_
(`generator/publisher.py`) is the program that iterates over the relevant
directories, renders HTML files, and writes them out to disk. The _app_
(`app.py`) is a lightweight Flask app that provides a development server.

[jekyll]: https://jekyllrb.com/
[jinja2]: https://jinja.palletsprojects.com/en/2.11.x/
