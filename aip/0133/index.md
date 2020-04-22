---
aip:
  id: 133
  state: approved
  created: 2019-01-23
  updated: 2019-06-10
permalink: /133
redirect_from:
  - /0133
---

# Standard methods: Create

In REST APIs, it is customary to make a `POST` request to a collection's URI
(for example, `/v1/publishers/{publisher}/books`) in order to create a new
resource within that collection.

Resource-oriented design ([AIP-121][]) honors this pattern through the `Create`
method. These RPCs accept the parent collection and the resource to create (and
potentially some other parameters), and return the created resource.

[aip-121]: ../0121.md
