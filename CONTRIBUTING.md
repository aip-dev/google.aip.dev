# Contributing

We'd love to accept your patches and contributions to this project.

## Development Environment

If you are contributing documentation (rather than samples) and want to be able
to view it in your browser, the easiest way to do so is to run the provided
development server.

We use [GitHub Pages][1] to make this documentation available, which uses
[Jekyll][2] under the hood.

If you have [Docker][3] installed, clone this repository and run the `serve.sh`
file at the root of the repository. This script does two things:

- It builds the provided Docker image (unless you already have it) and tags it
  as `googleapis-site`.
- It runs the `googleapis-site` image.

The Jekyll development server uses port 4000 by default; point your web browser
to `http://localhost:4000`, and you should see the site.

### Arguments

Any arguments provided to `serve.sh` (or `docker run`) are forwarded to Jekyll.
Note that the Docker entrypoint automatically provides `--destination` and
`--host` arguments, and you should not change these. Additionally, changing
ports is not advised (call `docker run` yourself with a customized `-p` switch
if you need to use custom ports).

### Hot reloading

The Jekyll development server supports "hot reloading" (where local changes
will be automatically reflected in your browser without having to manually
reload). You can activate this by sending the `--livereload` flag (`-l` for
short) to `serve.sh`.

### Local Installation

It is possible to run the development server locally also. The general gist of
how to do so correctly is:

- Install [rbenv](https://github.com/rbenv/rbenv).
- Use rbenv to install an appropriate version of Ruby.
- `gem install bundler`
- `bundle install`

Once this is done, you can run `bundle exec jekyll serve` to run the
development server (as above, include `--livereload` to get automatic
reloading).

**Note:** The Jekyll default setup will write the static site in-place to the
`_site` subdirectory. (The Docker image redirects this to an arbitrary spot in
the image so as not to pollute the local disk.)

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

[1]: https://pages.github.com/
[2]: https://jekyllrb.com/
[3]: https://docker.com/
