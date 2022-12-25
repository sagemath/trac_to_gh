# Issue 4521: Trivial permutation group enumeration bug

archive/issues_004521.json:
```json
{
    "body": "Assignee: joyner\n\nCC:  @saliola @mwhansen @KPanComputes\n\n1. This gives an error:\n\nsage: G = PermutationGroup([])\nsage: G.list()\n\n2. Permutation group should take an argument for the degree, e.g.:\n\nsage: G = PermutationGroup([],degree=4)\n\n3. Permutation group should set the degree correctly:\n\nsage: G = PermutationGroup([[]])\nsage: \nsage: G.list()\n[()]\nsage: G.degree()\n1\nsage: G = PermutationGroup([This is the Trac macro *1* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#1-macro))\nsage: G.degree()\n1\n\nThe first group should have degree 0. \n\n3. Degree 0 should really be supported or \nwe will have difficulties with automorphism \ngroups of boundary cases.  Currently this \ngives an error:\n\nsage: SymmetricGroup(0)\n\nCertainly these examples should go into the \ndocstrings.\nMost of these can be trivially fixed, but \nit would be good if someone could review \npermutation groups with a view to catching \nthese problems before they arise.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4521\n\n",
    "created_at": "2008-11-14T09:05:07Z",
    "labels": [
        "component: group theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-9.8",
    "title": "Trivial permutation group enumeration bug",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4521",
    "user": "https://trac.sagemath.org/admin/accounts/users/kohel"
}
```
Assignee: joyner

CC:  @saliola @mwhansen @KPanComputes

1. This gives an error:

sage: G = PermutationGroup([])
sage: G.list()

2. Permutation group should take an argument for the degree, e.g.:

sage: G = PermutationGroup([],degree=4)

3. Permutation group should set the degree correctly:

sage: G = PermutationGroup([[]])
sage: 
sage: G.list()
[()]
sage: G.degree()
1
sage: G = PermutationGroup([This is the Trac macro *1* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#1-macro))
sage: G.degree()
1

The first group should have degree 0. 

3. Degree 0 should really be supported or 
we will have difficulties with automorphism 
groups of boundary cases.  Currently this 
gives an error:

sage: SymmetricGroup(0)

Certainly these examples should go into the 
docstrings.
Most of these can be trivially fixed, but 
it would be good if someone could review 
permutation groups with a view to catching 
these problems before they arise.

Issue created by migration from https://trac.sagemath.org/ticket/4521





---

archive/issue_comments_033488.json:
```json
{
    "body": "I took a quick look at the code today and I've come away with a bunch of questions.\n\n(1) Can you post the definition of degree? In the current code, degree it is set equal to largest_moved_point, which grabs the value from gap's LargestMovedPoint if it isn't properly set. But this doesn't seem to agree with some of the things mentioned above.\n\n(2) Which group should the following command return?\n\n```\nsage: G = PermutationGroup([],degree=4)\n```\n\n\n(3) The following two groups are isomorphic:\n\n```\nsage: G = PermutationGroup([[]]) \nsage: G = PermutationGroup([ [1] ])\n```\n\nThis is because\n\n```\nsage: PermutationGroupElement([]).list()\n[1]\nsage: PermutationGroupElement([1]).list()\n[1]\n```\n\nSo I'm not sure why one group should have degree 0 while the other does not.\n\n(4) What should the degrees of SymmetricGroup(0) and SymmetricGroup(1) be? Should SymmetricGroup(0) == SymmetricGroup(1)?\n\nI think these are all my questions for now.",
    "created_at": "2008-11-20T23:49:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4521",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4521#issuecomment-33488",
    "user": "https://github.com/saliola"
}
```

I took a quick look at the code today and I've come away with a bunch of questions.

(1) Can you post the definition of degree? In the current code, degree it is set equal to largest_moved_point, which grabs the value from gap's LargestMovedPoint if it isn't properly set. But this doesn't seem to agree with some of the things mentioned above.

(2) Which group should the following command return?

```
sage: G = PermutationGroup([],degree=4)
```


(3) The following two groups are isomorphic:

```
sage: G = PermutationGroup([[]]) 
sage: G = PermutationGroup([ [1] ])
```

This is because

```
sage: PermutationGroupElement([]).list()
[1]
sage: PermutationGroupElement([1]).list()
[1]
```

So I'm not sure why one group should have degree 0 while the other does not.

(4) What should the degrees of SymmetricGroup(0) and SymmetricGroup(1) be? Should SymmetricGroup(0) == SymmetricGroup(1)?

I think these are all my questions for now.



---

archive/issue_comments_033489.json:
```json
{
    "body": "Changing status from new to needs_info.",
    "created_at": "2013-02-19T16:49:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4521",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4521#issuecomment-33489",
    "user": "https://github.com/KPanComputes"
}
```

Changing status from new to needs_info.



---

archive/issue_comments_033490.json:
```json
{
    "body": "I have not looked into any standard references on the permutation groups, but, I'd think that degree of a permutation group should be the cardinality of the maximal set on which the group acts transitively. I'll try to look into the references tomorrow in the library. \n\nThis seems to resolve a couple of things, about the degree. I really don't know what should (2) return, perhaps an error? :)",
    "created_at": "2013-02-19T17:09:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4521",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4521#issuecomment-33490",
    "user": "https://github.com/KPanComputes"
}
```

I have not looked into any standard references on the permutation groups, but, I'd think that degree of a permutation group should be the cardinality of the maximal set on which the group acts transitively. I'll try to look into the references tomorrow in the library. 

This seems to resolve a couple of things, about the degree. I really don't know what should (2) return, perhaps an error? :)



---

archive/issue_comments_033491.json:
```json
{
    "body": "This is a bug\n\n```\nsage: PermutationGroupElement([]).list()\n[1]\n```\n\n`PermutationGroupElement([])` should really be the unique permutation of the empty set.",
    "created_at": "2019-10-28T14:44:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4521",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4521#issuecomment-33491",
    "user": "https://github.com/videlec"
}
```

This is a bug

```
sage: PermutationGroupElement([]).list()
[1]
```

`PermutationGroupElement([])` should really be the unique permutation of the empty set.



---

archive/issue_comments_033492.json:
```json
{
    "body": "Changing status from needs_info to needs_work.",
    "created_at": "2019-10-28T14:48:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4521",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4521#issuecomment-33492",
    "user": "https://github.com/videlec"
}
```

Changing status from needs_info to needs_work.



---

archive/issue_comments_033493.json:
```json
{
    "body": "Ticket retargeted after milestone closed",
    "created_at": "2020-01-06T14:10:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4521",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4521#issuecomment-33493",
    "user": "https://github.com/embray"
}
```

Ticket retargeted after milestone closed



---

archive/issue_comments_033494.json:
```json
{
    "body": "Batch modifying tickets that will likely not be ready for 9.1, based on a review of the ticket title, branch/review status, and last modification date.",
    "created_at": "2020-04-14T19:41:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4521",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4521#issuecomment-33494",
    "user": "https://github.com/mkoeppe"
}
```

Batch modifying tickets that will likely not be ready for 9.1, based on a review of the ticket title, branch/review status, and last modification date.



---

archive/issue_comments_033495.json:
```json
{
    "body": "Setting new milestone based on a cursory review of ticket status, priority, and last modification date.",
    "created_at": "2021-02-13T20:51:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4521",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4521#issuecomment-33495",
    "user": "https://github.com/mkoeppe"
}
```

Setting new milestone based on a cursory review of ticket status, priority, and last modification date.



---

archive/issue_comments_033496.json:
```json
{
    "body": "Setting a new milestone for this ticket based on a cursory review.",
    "created_at": "2021-07-19T00:44:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4521",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4521#issuecomment-33496",
    "user": "https://github.com/mkoeppe"
}
```

Setting a new milestone for this ticket based on a cursory review.
