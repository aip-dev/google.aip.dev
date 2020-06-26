## Guidance

APIs **should** generally provide a `List` method for resources unless it is
not valuable for users to do so. The purpose of the `List` method is to return
data from a single, finite collection.

List methods are specified using the following pattern:

```proto
rpc ListBooks(ListBooksRequest) returns (ListBooksResponse) {
  option (google.api.http) = {
    get: "/v1/{parent=publishers/*}/books"
  };
  option (google.api.method_signature) = "parent";
}
```

- The RPC's name **must** begin with the word `List`. The remainder of the RPC
  name **should** be the plural form of the resource being listed.
- The request and response messages **must** match the RPC name, with
  `-Request` and `-Response` suffixes.
- The HTTP verb **must** be `GET`.
- The collection whose resources are being listed **should** map to the URL
  path.
  - The collection's parent resource **should** be called `parent`, and
    **should** be the only variable in the URI path. All remaining parameters
    **should** map to URI query parameters.
  - The collection identifier (`books` in the above example) **must** be a
    literal string.
- The `body` key in the `google.api.http` annotation **must** be omitted.
- There **should** be exactly one `google.api.method_signature` annotation,
  with a value of `"parent"`.
