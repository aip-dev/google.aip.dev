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
TODO: Should the effective policy message be the same as the policy message? If it's different, should properties of an effective policy reference the concrete policy which caused it?
-->

# Policy API Guidance

A policy is a set of guidelines which control some behavior of a
[resource](https://aip.dev/121) and its descendants. Some examples of
controllable behaviors are:  who can access a resource, what configurations are
allowed for a resource, and what billing account to charge for a resource’s
usage.

## Definitions

There are 2 types of policies, _dedicated_ and _shared_.

A _dedicated_ policy shares an identifier with the resource it is bound to. IAM
policies in GCP are an example of dedicated polices. Users "set" the policy
directly on the resource they intend it to apply to, and all children of the
resource inherit the policy.

A _shared_ policy is a first-class resource (with its own identifier) and can
even have policies applied to it (like an authorization policy). Unlike other
resources, a shared policy can be _bound_ to one or more resources, and applies
to those resources and any descendants. An example of a shared policy is
billing accounts, which are associated with resources that bill to them.

## Guidance

### Standard Methods

For most policy types, the policy name **should** be incorporated into the
method name. For example, `GetBillingPolicy` for a Billing policy. The
descriptions below omit the specific policy type for brevity.

### Dedicated Policies

If a resource can only have one of policy type bound to it, and there does not
need to be a separation of authorization privilege between the resource and the
policy, then services **may** use a dedicated policy.

Dedicated polices are the simpler of the two to implement, with a smaller API
scope. The authorization policy applied to the resource applies to the policy
as well. This can be problematic if users have permissions to modify
permissions on the resource, yet aren't intended to be able to modify the
policy.

- **SetPolicy** - Sets a dedicated policy for a resource
- **GetPolicy** - Retrieves the dedicated policy for a resource
- **DeletePolicy** - Deletes the dedicated policy for a resource
- **LookupEffectivePolicy** - Retrieves the effective policy for a resource,
  which is the combination of policies on the resource and any ancestors

### Shared policies

If a single policy is to be bound to multiple resources, or it should be
possible to apply a policy to the policy (eg., an authorization policy), then
services **should** use a shared policy.

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

Each policy method **should** have a separate permission in order to permit the
expression of fine-grained authorization policies.

Bindings are a bit special in that they connect two resources. Conceptually,
it's easiest to think of a binding as two half-bindings, one connected to the
policy and one connected to the resource. Each half-binding has its own
permission to create/delete. Therefore, creating a binding between a policy and
a resource requires two permissions; however breaking a binding only requires
permission on either the policy or the resource.

**Note:** No guidance is currently given for re-creating a binding. In theory,
only half of a binding could be deleted, thus requiring only a single
permission to re-establish the missing half of the binding.

### Effective Policies

An effective policy is the combination of policies applied to the ancestry of a
resource. For example, determining the effective policy for a VM would require
loading the policies attached to the VM, Project, Folder, and Organization.

There are multiple combination strategies, and which is chosen depends on the
policy system. Generally speaking, policies **should** be combined in an
additive fashion where leaf nodes take precedence for `ALLOW` semantics, and the
root nodes taking precedence for `DENY` semantics. This strategy works well for
large organizations where administrators need to delegate their responsibility
and/or want to set reasonable defaults at the top with overrides being set
where needed.

In some use cases, a policy lower in the hierarchy taking precedence is
unacceptable. In such cases, the override semantics **should** be a
configuration property of the policy itself (eg., an administrator could
explicitly configure the policy at the top to disallow overrides). This is
important for making it self-evident that the policy is not following the
standard patterns.

If no policies are bound the ancestry of a resource, the effective policy
**must** be equivalent to an empty policy.

## Changelog

- **2019-11-22**: Initial draft version
