---
aip:
  id: 2511
  scope: cloud
  state: draft
  created: 2019-11-22
permlink: /cloud/2511
redirect_from:
  - /2511
---

<!--
TODO: discuss policy lifecycle? binding lifecycle?
TODO: discuss policy conditions.
-->

# Policy API Guidance

A policy is a document-based resource that, when set on a resource, controls
some behavior for that resource and its descendants. Some examples of
controllable behaviors are:  who can access a resource, what configurations are
allowed for a resource and what billing account to charge for a resource’s
usage.

There are 2 types of policies, _dedicated_ and _shared_.

A _dedicated_ policy shares an identifier with the resource it is bound to. IAM
policies in GCP are an example of dedicated polices. Users "set" the policy on
directly on the resource they intend it to apply to, and all children of the
resource inherit the policy.

A _shared_ policy is a first-class resource (with its own identifier) and can
even have policies applied to it (like an authorization policy). Unlike other
resources, a shared policy can be _bound_ to one or more resources, and applies
to those resources and any descendents. An example of a shared policy is
billing accounts, which are associated with resources that bill to them.

## Standard Methods

For most policy types, it makes sense to incorporate the policy name in to the
method name, for example `GetBillingPolicy` for a Billing policy. The
descriptions below omit the specific policy type for brevity.

### Dedicated Policies

Dedicated polices are the simpler of the two to implement, with a smaller API
scope. A common issue is that since they are bound to a single resource, the
permissions to modify the policy get conflated with permissions to modify the
resource.

- **SetPolicy** - Sets a dedicated policy for a resource
- **GetPolicy** - Retrieves the dedicated policy for a resource
- **DeletePolicy** - Deletes the dedicated policy for a resource
- **LookupEffectivePolicy** - Retrieves the effective policy for a resource,
  which is the combination of policies on the resource and any ancestors

### Shared Policies

Shared policies have a more complex API scope, but are also substantially more
powerful. They permit users to have very fine-grained permissions and delegated
policy roles. They also allow a common policy definition (which might be quite
complex) to be bound to numerous resoures.

- **CreatePolicy** - Creates a shared policy resource
- **GetPolicy** - Retrieves a shared policy resource
- **UpdatePolicy** - Updates a shared policy resource
- **DeletePolicy** - Deletes a shared policy resource
- **ListPolicies** - Lists shared policy resources (typically for a given
  `parent`)
- **LookupEffectivePolicy** - Retrieves the effective policy for a given
  `resource`, which is the combination of the polices bound to the resource and
  any ancestors
- **CreateBinding** - Creates a binding between a shared policy resource and a
  specified resource
- **GetBinding** - Retrieves a binding between a shared policy resource and a
  resource
- **DeleteBinding** - Deletes a binding between a shared policy resource and a
  resource
- **ListBindings** - Lists bindings between shared policy resources and other
  resources. This method **must** accept either a reference to the shared
  policy resource or the target resource (typically via the `filter` field),
  and list all appropriate bindings.

### Permissions

There **should** be a separate permission for each policy method, per standard
practice.

Bindings are a bit special in that they connect two resources. Conceptually,
it's easiest to think of a binding as two half-bindings, one connected to the
Policy and one connected to the Resource. Each half-binding has it's own
permission to create/delete. So to create a binding between a Policy and a
Resource requires 2 permissions, but to break a binding only requires
permission on either the Policy or the Resource.

NOTE: At this point in time, no guidance is given for recreating a binding. In
theory only half of a binding could be deleted, thus allowing only a
single-permission to re-establish the missing half of the binding.

## Effictive Policies

An effective policy is the combination of policies applied to the ancestry of a
resource. For example, to determine the effective policy for a VM would require
loading the policies attacted to the VM, Project, Folder, and Organization.

There are multiple combination stragies, and which one chosen depends on the
Policy system. Generally speaking, policies **should** be combined in an
additive fashion where leaf nodes take precedence for ALLOW semantics, and the
root nodes taking precendence for DENY semantics. This strategy works well for
large organizations where administrators need to delegate their responsibility
and/or want to set reasonable defaults at the top with overrides being set
where needed.

In some use cases, a policy lower in the hierarchy taking precedency may be
unacceptable. We strongly encourage such cases to permit configuration of
override policies instead of forcing the choice.

If no policies are bound the ancsestry of a resource, the effective resource is
to be empty.

## Changelog

- **2019-11-22**: Initial draft version
