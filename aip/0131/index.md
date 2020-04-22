---
aip:
  id: 131
  state: approved
  created: 2019-01-22
permalink: /131
redirect_from:
  - /0131
---

# Standard methods: Get

In REST APIs, it is customary to make a `GET` request to a resource's URI (for
example, `/v1/publishers/{publisher}/books/{book}`) in order to retrieve that
resource.

Resource-oriented design ([AIP-121][]) honors this pattern through the `Get`
method. These RPCs accept the URI representing that resource and return the
resource.

[aip-121]: ../0121.md
