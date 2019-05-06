---
exclude_from_search: true
js:
  - /assets/js/aip/aip-index.js
permalink: /
---

# API Improvement Proposals

## What are AIPs?

AIP stands for **API Improvement Proposal**, which is a design document
providing high-level, concise documentation for API development. They are to
serve as the source of truth for API-related documentation at Google and the
means by which API teams discuss and come to consensus on API guidance.

Some product areas within Googles have guidance which may supplement (and
occasionally override) the standard rules. These PAs often use the AIP system
too. If so, we list their AIPs here, along with which parts of Google they
apply to. So the complete set of AIPs that apply to you are the General API
Guidance, possibly supplemented by your PA's guidance.

## AIP Listing

The following is a listing of all AIPs so far, broken down by type.

### Meta-AIPs (AIPs about AIPs)

<!-- prettier-ignore-start -->

| Number | Title | State |
| -----: | ----- | ----- |
{% for p in site.pages -%}
{% if p.aip and p.aip.id < 100 -%}
| {{ p.aip.id }} | [{{ p.title }}]({{ p.url }}) | {{ p.aip.state | capitalize }} |
{% endif -%}
{% endfor %}

<!-- prettier-ignore-end -->

### Process

<!-- prettier-ignore-start -->

| Number | Title | State |
| -----: | ----- | ----- |
{% for p in site.pages -%}
{% if p.aip and p.aip.id >= 100 and p.aip.id < 120 -%}
| {{ p.aip.id }} | [{{ p.title }}]({{ p.url }}) | {{ p.aip.state | capitalize }} |
{% endif -%}
{% endfor %}

<!-- prettier-ignore-end -->

### Guidance

<!-- prettier-ignore-start -->

| Number | Title | State |
| -----: | ----- | ----- |
{% for p in site.pages -%}
{% if p.aip and p.aip.id >= 120 and p.aip.id < 1000 -%}
| {{ p.aip.id }} | [{{ p.title }}]({{ p.url }}) | {{ p.aip.state | capitalize }} |
{% endif -%}
{% endfor %}

<!-- prettier-ignore-end -->

### PA / Team Guidance

Certain PAs or teams may provide specific guidance that only applies to APIs
within the purview of that group.

While it is uncommon, it may be the case that group-level guidance will
contradict general guidance. In this situation, the group-specific guidance
takes precedence (local consistency has higher precedence than global
consistency.)

| Block | Team                              |
| ----: | --------------------------------- |
|  2500 | [Cloud](./cloud/index.md)         |
|  2700 | [Apps (G Suite)](./apps/index.md) |
