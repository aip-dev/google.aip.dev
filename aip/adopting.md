---
permalink: /adopting
---

# Adopting AIPs in your company

**Note:** We're working on some tooling to make this better. Keep an eye on
[this GitHub issue][] for progress.

While AIPs originated at Google and were aimed for Googlers writing Google
APIs, much of the guidance documented is useful outside of Google. This
document describes how you might adopt AIPs as the way you document your own
APIs even if you don't work at Google.

## The problem

Sometimes private organizations might have API guidance that they don't want or
care to share with the rest of the world. For example, maybe in your company
(let's say, Acme, Inc), you identify your resources with a special field called
`string acme_id`.

This rule could be written as an AIP, but there's no reason to share this rule
with everyone -- it's only for you and your development team. However, you
don't want this to conflict with a future AIP (e.g., if you make this AIP-1234,
maybe that AIP will get written in the future and then you'll have a conflict).
So what do you do?

## Custom AIP domains

We're working on a separate fork-able repository that you can copy and use as
your 9000 block AIP repository. The page rendered by GitHub Pages will serve
only the AIPs in that block and redirect all other pages to [aip.dev][].

In short, this means that you can create your own AIP domain (e.g.,
`aip.example.com`) and point that to the forked GitHub repository which will
redirect for all well-known AIPs and serve all internal AIPs from your own
repository. Once you've done that, you can cite all AIPs specifically using
that domain name (e.g., `aip.example.com/1234`) and you'll always get sent to
the right place.

While it's possible to create your own AIP IDs, it is recommended that you
maintain the same AIP IDs that are used in aip.dev. This will allow your AIPs
to be comparable across multiple AIP implementations.

## Forking AIP

You can fork the AIP project and run it in your own domain if necessary. This
will allow you to customize the AIPs to your organization's needs. Or you could
use the infrastructure to create your own set of AIPs.

### Updating the URL

To run the AIP infrastructure as a GitHub Page in a another repository, the
`_config.yaml` file must be updated to work correctly in the new repo.

If a new custom domain and CNAME have been created for your AIP, only the `url`
property will need to be updated to the new domain.

```
url: https://aip.dev
```

If you are not creating a new domain, it will be necessary to add the `baseurl`
property to the `_config.yaml`. This property should contain any additional
path information that may be appended to the domain in the `url`.

For example, assume GitHub user jdoe123 forked the aip project into a
repository named my-aips. If this user served the content from their master
branch, the url to the GitHub pages would be
`https://jdoe123.github.io/my-aips/`. The accompanying `_config.yaml` would be
configured as follows:

```
url: https://jdoe123.github.io
baseurl: /my-aips
```

For more information about about how these values are used by GitHub Pages, see
the [release notes][] that standardized these configurations in Jekyll.

### Configuring Navigation

The navigation headers and bar are generated dynamically based on the
`_data/header.yaml` and `_data/nav.yaml` files respectively.

The schema for the navigation bar can be viewed under
`assets/schemas/nav-schema.yaml`. It supports two types of navigation
components; `static_group` and `matter_group`. A `static_group` menu component
will always show the same navigation elements, regardless of the content of the
page and the repository. A `matter_group` component is generated dynamically
based on the AIPs in the domain, or the current page in the site. The
configurations for a `matter_group` can be viewed in the
`assets/schemas/nav-components.yaml#defintions/matter_group` schema.

The header is just a specially rendered `static_group` component. The schema
can be viewed at `assets/schemas/static_group.yaml`.

### Testing Configuration

The `tests` folder contains an npm test module that will validate your data
files. Running these tests requires npm and mocha. Once these are installed
that tests can be ran with the `npm test` command.

## AIP Extensions

Sometimes an organization within a domain may want to adopt most or all of the
AIPs in a domain, and also need the ability to make some adjustments. This is
considered an extension of an AIP domain, and is expected to reside within the
domain.

AIP extensions alter an AIP by providing a new file that should be displayed
when viewing that AIP ID within the organization's context.

AIP extensions are expected to follow the same rules regarding AIP numbering
when creating custom AIPs that are specific to their context.

When extending an AIP domain, an organization context **must** create a new
folder in the `aip` directory containing all of their altered or custom AIP
files. Additionally they must create an `index.md` file with the following
front-matter:

```
aip_index:
  scope: <unique scope for domain>
  order: <number that determines order in nav>
exclude_from_search: true
js: /assets/js/aip/aip-index.js
permalink: /<unique scope for domain>
```

Note that the value of `scope` will be used to identify the context under which
AIPs are being viewed and will determine the content of the nav menu and how
references to other AIPs are resolved.

<!-- prettier-ignore-start -->
[this github issue]: https://github.com/googleapis/aip/issues/98
[npm]: https://www.npmjs.com/get-npm
[mocha]: https://www.npmjs.com/package/mocha
[release notes]: https://jekyllrb.com/news/2016/10/06/jekyll-3-3-is-here/#2-relative_url-and-absolute_url-filters
<!-- prettier-ignore-end -->
