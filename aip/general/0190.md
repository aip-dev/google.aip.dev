---
id: 190
state: approved
created: 2025-06-10
placement:
  category: polish
  order: 0
---

# Naming conventions

This topic describes the naming conventions used in Google APIs. In
general, these conventions apply to all Google-managed services.

## Guidance

In order to provide consistent developer experience across many APIs and
over a long period of time, all names used by an API **should** be:

-   straightforward
-   intuitive
-   consistent

This includes names of interfaces, resources, collections, methods, and
messages.

Since English is a second language for many developers, one goal of these
naming conventions is to make every API name understandable to the majority of
developers. It does this by encouraging the use of a simple, consistent, and
small vocabulary when naming methods and resources.

-   Names used in APIs **should** be in correct American English. For
    example, license (instead of licence), color (instead of colour).
-   Commonly accepted short forms or abbreviations of long words **may**
    be used for brevity. For example, API is preferred over Application
    Programming Interface.
-   Unless otherwise specified, definitions **must** use UpperCamelCase names,
    as defined by
    [Google Java Style](https://google.github.io/styleguide/javaguide.html#s5.3-camel-case).
-   Use intuitive, familiar terminology where possible. For example,
    when describing removing (and destroying) a resource, delete is
    preferred over erase.
-   Use the same name or term for the same concept, including for
    concepts shared across APIs.
-   Avoid name overloading. Use different names for different concepts.
-   Avoid overly general names that are ambiguous within the context of
    the API and the larger ecosystem of Google APIs. They can lead to
    misunderstanding of API concepts. Rather, choose specific names that
    accurately describe the API concept. This is particularly important
    for names that define first-order API elements, such as resources.
    There is no definitive list of names to avoid, as every name must be
    evaluated in the context of other names. Instance, info, and service
    are examples of names that have been problematic in the past. Names
    chosen should describe the API concept clearly (for example:
    instance of what?) and distinguish it from other relevant concepts
    (for example: does "alert" mean the rule, the signal, or the
    notification?).
-   Carefully consider use of names that may conflict with keywords in
    common programming languages. Such names **may** be used but will
    likely trigger additional scrutiny during API review. Use them
    judiciously and sparingly.

### Interface names

To avoid confusion with [Service Names](./0009.md#api-service-name) such as
`pubsub.googleapis.com`, the term *interface name* refers to the name
used when defining a `service` in a .proto file:

```proto
// Library is the interface name.
service Library {
  rpc ListBooks(...) returns (...);
  rpc ...
}
```

You can think of the *service name* as a reference to the actual
implementation of a set of APIs, while the *interface name* refers to
the abstract definition of an API.

An interface name **should** use an intuitive noun such as Calendar or
BlobStore. The name **should not** conflict with any well-established
concepts in programming languages and their runtime libraries (for
example, File).

In the rare case where an *interface name* would conflict with another
name within the API, a suffix (for example `Api` or `Service`)
**should** be used to disambiguate.

### Method names

A service **may**, in its IDL specification, define one or more API
methods that correspond to methods on collections and resources. The
method names **should** follow the naming convention of `VerbNoun` in
UpperCamelCase, where the noun is typically the resource type.

Standard methods, and their Batch variants, define their naming guidance in
the following documents:

Method | Standard | Batch
------ | -------- | -----
`Get`  | [AIP-131][] | [AIP-231][]
`List` | [AIP-132][] | N/A
`Create` | [AIP-133][] | [AIP-233][]
`Update` | [AIP-134][] | [AIP-234][]
`Delete` | [AIP-135][] | [AIP-235][]

All other methods are considered Custom Methods and adhere to AIP-136 naming
guidance.

### Message names

Message names **should** be short and concise. Avoid unnecessary or redundant
words. Adjectives can often be omitted if there is no corresponding message
without the adjective. For example, the `Shared` in `SharedProxySettings` is
unnecessary if there are no _unshared_ proxy settings.

Message names **should not** include prepositions (e.g. "With", "For").
Generally, message names with prepositions are better represented with
optional fields on the message.

#### Request and response messages

For request and response message names, see AIP-136 for custom methods and the 
appropriate AIP for
[standard methods](https://google.aip.dev/general#operations).

## Further reading

-   For proto and language package naming, see AIP-191.
-   For collection ID naming conventions, see
    [AIP-122](./0122.md#collection-identifiers).
-   For Enum names, see AIP-126.
-   For field names, see AIP-140.
-   For repeated field names, see [AIP-140](./0140#repeated-fields).
-   For fields representing times and durations, see AIP-142.
-   For fields representing dates and times of day, see
    [AIP-142](./0142#civil-dates-and-times).
-   For fields representing a quantity, see AIP-141.
-   For the canonical `List` method `filter` field, see
    [AIP-132](./0132#filtering).
-   For the canonical `List` response message, see
    [AIP-132](./0132#response-message).
-   For well known abbreviations, see [AIP-140](./0140#abbreviations).

<!-- Need these link values for the table entries which won't be hot-linked by
the site-generator like plain text would be -->
[AIP-131]: ./0131.md
[AIP-132]: ./0132.md
[AIP-133]: ./0133.md
[AIP-134]: ./0134.md
[AIP-135]: ./0135.md
[AIP-231]: ./0231.md
[AIP-233]: ./0233.md
[AIP-234]: ./0234.md
[AIP-235]: ./0235.md
