---
permalink: /adopting
---

# Adopting AIPs in your company

**Note:** We're working on some tooling to make this better. Keep an eye on
[this GitHub issue](https://github.com/googleapis/aip/issues/98) for progress.

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

## The 9000 block

Much like the Unicode specification, we've reserved the 9000 block of AIP
numbers (that is, AIP-9000 through AIP-9999) to be for "internal use". This
means that these AIPs will never have public documentation and are free for
private companies to use for their own API guidance. As a result, all you have
to do is write your AIPs as usual and give them a number in the 9000 block.

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

## Forking AIP

You can fork the AIP project and run it in your own domain if necessary. This will allow you to customize the AIPs to your organizations needs, or even create your own set of AIPs.

### Updating the URL

When running the AIP infrastructure as a Github Page in a another repo, you will need to update the `_config.yaml` file so that Github Pages will build the relative urls of the AIP project correctly.

If you have created a new custom domain for your AIPs, you only need to change the `url` propery in `_config.yaml` to point to your new domain:

```
url: https://aip.dev
```

If you are not creating a new domain, it may be necessary to add the `baseurl` property to the `_config.yaml`. This property should contain any additional path information that may be appended to the domain in the `url`.

For example, assume Github user jdoe123 forked the aip project into a repository named my-aips. If this user served the content from their master branch, the url to the Github pages would be `https://jdoe123.github.io/my-aips/`. The `_config.yaml` would need to be updated as follows:

```
url: https://jdoe123.github.io
baseurl: /my-aips
```

For more information about about how these values are used by Github Pages, see the [release notes](https://jekyllrb.com/news/2016/10/06/jekyll-3-3-is-here/#2-relative_url-and-absolute_url-filters) that standardized these configurations in Jekyll.

### Configuring Navigation

The nav menu and the nav drawer are generated dynamically based on the `_data/nav.yaml` file. The nav.yaml file supports the creation of static and dynamic navigation menus that can be included or excluded from either the desktop or mobile views.

The schema can be viewed in `assets/schema/nav-schema.yaml`.

The `bar` and `drawer` properties in the file define the menu components to use when creating the desktop nav-bar and the mobile nav-drawer respectively. The other properties in the file are the definitions of the menu elements that are referred to in the `bar` and `drawer`.

There are two types of navigation elements that can be added to the menu: `static` and `matterGroup`. A `static` menu element will always show the same navigation elements, regardless of the content. A `matterGroup` element is generated dynamically based on the AIPs in the domain, or the current page in the site.
