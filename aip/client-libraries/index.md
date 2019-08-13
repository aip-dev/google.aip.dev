---
aip_index:
  scope: client-libraries
exclude_from_search: true
js:
  - /assets/js/aip/aip-index.js
permalink: /client-libraries
---

# Client Libraries AIPs

The following AIPs apply to work on client libraries and generators for
mass-producing client libraries.

### Guidance

<!-- prettier-ignore-start -->

| Number | Title | State |
| -----: | ----- | ----- |
{% for p in site.pages -%}
{% if p.aip and p.aip.id >= 4200 and p.aip.id < 4300 -%}
| {{ p.aip.id }} | [{{ p.title }}]({{ p.url }}) | {{ p.aip.state | capitalize }} |
{% endif -%}
{% endfor %}

<!-- prettier-ignore-end -->
