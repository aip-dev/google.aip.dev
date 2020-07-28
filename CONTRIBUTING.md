# Contributing

We'd love to accept your patches and contributions to this project.

## Development Environment

If you are contributing AIP content (rather than code) and want to be able to
view it in your browser, the easiest way to do so is to run the provided
development server.

We use [GitHub Pages][1] to make this documentation available, and a specific
[site generator][2] to build the site.

If you have [Docker][3] installed, clone this repository and run the `serve.sh`
file at the root of the repository. This script does two things:

- It builds the provided Docker image (unless you already have it) and tags it
  as `aip-site`.
- It runs the `aip-site` image.

The development server uses port 4000; point your web browser to
`http://localhost:4000`, and you should see the site.

**Note:** After building the Docker image for the first time, you may
experience issues if Python dependencies change underneath you. If this
happens, remove your Docker image (`docker rmi aip-site`) and run `serve.sh`
again.

### Arguments

Any arguments provided to `serve.sh` (or `docker run`) are forwarded (however,
the current site generator does not honor any; this may change in the future).

### Hot reloading

The development server recognizes when files change (including static files)
and local changes will be automatically reflected in your browser upon reload.

### Local Installation

It is possible to run the development server locally also. The general gist of
how to do so correctly is:

- Install Python 3.8 if you do not already have it (direct install is fine, but
  [pyenv][5] is probably the best way if you have other Python projects).
- Create a Python 3.8 [venv][6]. Once it is created, activate it in your shell
  (`source path/to/venv/bin/activate`).
- `pip install git+https://github.com/aip-dev/site-generator.git`
- `aip-site-serve .`

## Contributor License Agreement

Contributions to this project must be accompanied by a Contributor License
Agreement. You (or your employer) retain the copyright to your contribution,
this simply gives us permission to use and redistribute your contributions as
part of the project. Head over to <https://cla.developers.google.com/> to see
your current agreements on file or to sign a new one.

You generally only need to submit a CLA once, so if you have already submitted
one (even if it was for a different project), you probably do not need to do it
again.

## Code reviews

All submissions, including submissions by project members, require review. We
use GitHub pull requests for this purpose. Consult
[GitHub Help](https://help.github.com/articles/about-pull-requests/) for more
information on using pull requests.

### Formatting

We use [prettier][4] to format Markdown, JavaScript, and (most) HTML, in order
to ensure a consistent style throughout our source. You can add prettier as a
plugin in most development environments.

[1]: https://pages.github.com/
[2]: https://github.com/aip-dev/site-generator
[3]: https://docker.com/
[4]: https://prettier.io/
[5]: https://github.com/pyenv/pyenv
[6]: https://docs.python.org/3/library/venv.html
