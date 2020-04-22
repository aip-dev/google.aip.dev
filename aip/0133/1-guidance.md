---
aip_fragment:
  id: 133
  changelog:
    - date: 2019-10-18
      message: Added guidance on annotations.
    - date: 2019-08-01
      message: |
        Changed the examples from "shelves" to "publishers", to present a
        better example of resource ownership.
---

## Guidance

APIs **should** generally provide a create method for resources unless it is
not valuable for users to do so. The purpose of the create method is to create
a new resource in an already-existing collection.

Create methods are specified using the following pattern:

```proto
rpc CreateBook(CreateBookRequest) returns (Book) {
  option (google.api.http) = {
    post: "/v1/{parent=publishers/*}/books"
    body: "book"
  };
  option (google.api.method_signature) = "parent,book";
}
```

- The RPC's name **must** begin with the word `Create`. The remainder of the
  RPC name **should** be the singular form of the resource being created.
- The request message **must** match the RPC name, with a `-Request` suffix.
- The response message **must** be the resource itself. There is no
  `CreateBookResponse`.
  - If the create RPC is [long-running](#long-running-create), the response
    message **must** be a `google.longrunning.Operation` which resolves to the
    resource itself.
- The HTTP verb **must** be `POST`.
- The collection where the resource is being added **should** map to the URL
  path.
  - The collection's parent resource **should** be called `parent`, and
    **should** be the only variable in the URI path.
  - The collection identifier (`books` in the above example) **must** be
    literal.
- There **must** be a `body` key in the `google.api.http` annotation, and it
  **must** map to the resource field in the request message.
  - All remaining fields **should** map to URI query parameters.
- There **should** be exactly one `google.api.method_signature` annotation,
  with a value of `"parent,{resource}"` (unless the method supports
  [user-specified IDs](#user-specified-ids)).
