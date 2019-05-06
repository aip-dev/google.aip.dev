---
aip_index:
  scope: apps
exclude_from_search: true
js:
  - /assets/js/aip/aip-index.js
permalink: /apps
---

# Apps AIPs

The following AIPs apply to work on APIs in the Google Apps (G Suite) PA. For
questions, contact apps-api-team@google.com.

### Guidance

<!-- prettier-ignore-start -->

| Number | Title | State |
| -----: | ----- | ----- |
{% for p in site.pages -%}
{% if p.aip and p.aip.id >= 2700 and p.aip.id < 2800 -%}
| {{ p.aip.id }} | [{{ p.title }}]({{ p.url }}) | {{ p.aip.state | capitalize }} |
{% endif -%}
{% endfor %}

<!-- prettier-ignore-end -->
