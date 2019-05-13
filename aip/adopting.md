---
permalink: /adopting
---

# Adopting AIPs in your company

**Note:** We're working on some tooling to make this better. Keep an eye on
[this GitHub issue](https://github.com/googleapis/aip/issues/98) for progress.

While AIPs originated at Google and were aimed for Googlers writing Google APIs,
much of the guidance documented is useful outside of Google. This document
describes how you might adopt AIPs as the way you document your own APIs even if
you don't work at Google.

## The problem

Sometimes private organizations might have API guidance that they don't want or
care to share with the rest of the world. For example, maybe in your company
(let's say, Acme, Inc), you identify your resources with a special field called
`string acme_id`.

This rule could be written as an AIP, but there's no reason to share this rule
with everyone -- it's only for you and your development team. However, you don't
want this to conflict with a future AIP (e.g., if you make this AIP-1234, maybe
that AIP will get written in the future and then you'll have a conflict). So
what do you do?

## The 9000 block

Much like the Unicode specification, we've reserved the 9000 block of AIP
numbers (that is, AIP-9000 through AIP-9999) to be for "internal use". This
means that these AIPs will never have public documentation and are free for
private companies to use for their own API guidance. As a result, all you have
to do is write your AIPs as usuall and give them a number in the 9000 block.

## Custom AIP domains

We're working on a separate fork-able repository that you can copy and use as
your 9000 block AIP repository. The page rendered by GitHub Pages will serve
only the AIPs in that block and redirect all other pages to [aip.dev][].

In sort, this means that you can create your own AIP domain (e.g.,
`aip.example.com`) and point that to the forked GitHub repository which will
redirect for all well-known AIPs and serve all internal AIPs from your own
repository. Once you've done that, you can cite all AIPs specifically using that
domain name (e.g., `aip.example.com/1234`) and you'll always get sent to the
right place.

[aip.dev]: https://aip.dev/