# Standard methods: List

In many APIs, it is customary to make a `GET` request to a collection's URI
(for example, `/v1/publishers/1/books`) in order to retrieve a list of
resources, each of which lives within that collection.

Resource-oriented design ([AIP-121](/121)) honors this pattern through the
`List` method. These RPCs accept the parent collection (and potentially some
other parameters), and return a list of responses matching that input.
