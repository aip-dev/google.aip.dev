## What are AIPs?

AIP stands for **API Improvement Proposal**, which is a design document
providing high-level, concise documentation for API development. They are to
serve as the source of truth for API-related documentation at Google and the
means by which API teams discuss and come to consensus on API guidance.

Some product areas within Googles have guidance which may supplement (and
occasionally override) the standard rules. These PAs often use the AIP system
too. If so, we list their AIPs here, along with which parts of Google they
apply to. So the complete set of AIPs that apply to you are the General API
Guidance, possibly supplemented by your PA's guidance.

---

## AIP Listing

The following is a listing of all AIPs so far, broken down by type.

### Meta-AIPs (AIPs about AIPs)

| Number | Title                                   | State    |
| -----: | --------------------------------------- | -------- |
|      1 | [AIP Purpose and Guidelines](./0001.md) | Approved |
|      2 | [AIP Numbering](./0002.md)              | Approved |

### Process

| Number | Title                              | State    |
| -----: | ---------------------------------- | -------- |
|    100 | [API Design Review FAQ](./0100.md) | Approved |

### General API guidance

| Number | Title                                            | State     |
| -----: | ------------------------------------------------ | --------- |
|    121 | [Resource-oriented design](./aip/0121)           | Approved  |
|    122 | [Resource names](./0122.md)                      | Reviewing |
|    131 | [Standard methods: Get](./0131.md)               | Reviewing |
|    132 | [Standard methods: List](./0132.md)              | Reviewing |
|    133 | [Standard methods: Create](./0133.md)            | Reviewing |
|    134 | [Standard methods: Update](./0134.md)            | Reviewing |
|    135 | [Standard methods: Delete](./0135.md)            | Reviewing |
|    136 | [Custom methods](./0136.md)                      | Reviewing |
|    157 | [Partial responses](./0157.md)                   | Reviewing |
|    200 | [Avoiding setting bad API precedents](./0200.md) | Approved  |
|    203 | [Documenting field behavior](./0203.md)          | Approved  |
|    205 | [Annotate beta-blocking API changes](./0205.md)  | Reviewing |
|    210 | [Unicode usage in APIs](./0210.md)               | Approved  |
|    213 | [Common proto messages](./0213.md)               | Approved  |
|    214 | [Resource expiration](./0214.md)                 | Approved  |
|    215 | [Always version all protos](./0215.md)           | Approved  |
|    216 | [States](./0216.md)                              | Approved  |

### PA / Team Guidance

Certain PAs or teams may provide specific guidance that only applies to APIs
within the purview of that group.

While it is uncommon, it may be the case that group-level guidance will
contradict general guidance. In this situation, the group-specific guidance
takes precedence (local consistency has higher precedence than global
consistency.)

| Block | Team                     |
| ----: | ------------------------ |
|  2500 | [Cloud](./cloud)         |
|  2700 | [Apps (G Suite)](./apps) |
|  4600 | [Geo](./geo)             |

<style>
th:first-child { width: 100px; }
td:first-child { width: 100px; }
th:nth-child(3) { width: 125px; }
td:nth-child(3) { width: 125px; }
</style>
