# Standard methods: Get

In REST APIs, it is customary to make a `GET` request to a resource's URI (for
example, `/v1/publishers/{publisher}/books/{book}`) in order to retrieve that
resource.

Resource-oriented design ([AIP-121](/121)) honors this pattern through the
`Get` method. These RPCs accept the URI representing that resource and return
the resource.
