---
aip_index:
  scope: cloud
exclude_from_search: true
js:
  - /assets/js/aip/aip-index.js
permalink: /cloud
---

# Google Cloud Platform AIPs

The following AIPs apply to work on APIs on Google Cloud Platform.

### Google Cloud Platform APIs

<!-- prettier-ignore-start -->

| Number | Title | State |
| -----: | ----- | ----- |
{% for p in site.pages -%}
{% if p.aip and p.aip.id >= 2500 and p.aip.id < 2600 -%}
| {{ p.aip.id }} | [{{ p.title }}]({{ p.url }}) | {{ p.aip.state | capitalize }} |
{% endif -%}
{% endfor %}

<!-- prettier-ignore-end -->

### Cloud SDK

The following AIPs apply to work on the command-line interface for the Cloud
SDK.

<!-- prettier-ignore-start -->

| Number | Title | State |
| -----: | ----- | ----- |
{% for p in site.pages -%}
{% if p.aip and p.aip.id >= 2600 and p.aip.id < 2700 -%}
| {{ p.aip.id }} | [{{ p.title }}]({{ p.url }}) | {{ p.aip.state | capitalize }} |
{% endif -%}
{% endfor %}

<!-- prettier-ignore-end -->
