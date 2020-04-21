---
aip_fragment:
  id: 131
  changelog:
    - date: 2019-10-18
      message: Added guidance on annotations.
    - date: 2019-08-01
      message: |
        Changed the examples from "shelves" to "publishers", to present a
        better example of resource ownership.
---

## Guidance

APIs **should** generally provide a get method for resources unless it is not
valuable for users to do so. The purpose of the get method is to return data
from a single resource.

Get methods are specified using the following pattern:

```proto
rpc GetBook(GetBookRequest) returns (Book) {
  option (google.api.http) = {
    get: "/v1/{name=publishers/*/books/*}"
  };
  option (google.api.method_signature) = "name";
}
```

- The RPC's name **must** begin with the word `Get`. The remainder of the RPC
  name **should** be the singular form of the resource's message name.
- The request message **must** match the RPC name, with a `-Request` suffix.
- The response message **must** be the resource itself. (There is no
  `GetBookResponse`.)
- The HTTP verb **must** be `GET`.
- The URI **should** contain a single variable field corresponding to the
  resource name.
  - This field **should** be called `name`.
  - The URI **should** have a variable corresponding to this field.
  - The `name` field **should** be the only variable in the URI path. All
    remaining parameters **should** map to URI query parameters.
- There **must not** be a `body` key in the `google.api.http` annotation.
- There **should** be exactly one `google.api.method_signature` annotation,
  with a value of `"name"`.
