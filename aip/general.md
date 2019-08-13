---
exclude_from_search: true
js:
  - /assets/js/aip/aip-index.js
permalink: /general
---

# General AIPs

The following AIPs apply to work across all APIs generally.

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
