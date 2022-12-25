# Issue 4521: Trivial permutation and permutation groups

archive/issues_004521.json:
```json
{
    "body": "Assignee: joyner\n\nCC:  @saliola @mwhansen @KPanComputes\n\nWhen constructing an empty permutation the degree should be zero (ie a permutation of the empty set). But\n\n```\nsage: PermutationGroupElement([]).parent().domain()\n{1}\n```\nIncidentally, it is also wrong for `PermutationGroup`\n\n```\nsage: G = PermutationGroup([])\nsage: G.degree()\n1\n```\n\nMaybe `PermutationGroupElement` and `PermutationGroup` should take an argument for the degree, e.g.:\n\n```\nsage: G = PermutationGroup([],degree=4)\n```\n\nNOTE: one (not compltely ideal) workaround is to use `SymmetricGroup(4).subgroup([])`\n\n---\n\nThe original report mentioned two other problems that now behave coherently (tested on 9.0.beta3)\n\n1. This gives an error:\n\n```\nsage: G = PermutationGroup([])\nsage: G.list()\n```\n\n4. Degree 0 should really be supported or \nwe will have difficulties with automorphism \ngroups of boundary cases.  Currently this \ngives an error:\n\n```\nsage: SymmetricGroup(0)\n```\nCertainly these examples should go into the  docstrings. Most of these can be trivially fixed, but it would be good if someone could review permutation groups with a view to catching these problems before they arise.\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4521\n\n",
    "created_at": "2008-11-14T09:05:07Z",
    "labels": [
        "component: group theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-9.8",
    "title": "Trivial permutation and permutation groups",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4521",
    "user": "https://trac.sagemath.org/admin/accounts/users/kohel"
}
```
Assignee: joyner

CC:  @saliola @mwhansen @KPanComputes

When constructing an empty permutation the degree should be zero (ie a permutation of the empty set). But

```
sage: PermutationGroupElement([]).parent().domain()
{1}
```
Incidentally, it is also wrong for `PermutationGroup`

```
sage: G = PermutationGroup([])
sage: G.degree()
1
```

Maybe `PermutationGroupElement` and `PermutationGroup` should take an argument for the degree, e.g.:

```
sage: G = PermutationGroup([],degree=4)
```

NOTE: one (not compltely ideal) workaround is to use `SymmetricGroup(4).subgroup([])`

---

The original report mentioned two other problems that now behave coherently (tested on 9.0.beta3)

1. This gives an error:

```
sage: G = PermutationGroup([])
sage: G.list()
```

4. Degree 0 should really be supported or 
we will have difficulties with automorphism 
groups of boundary cases.  Currently this 
gives an error:

```
sage: SymmetricGroup(0)
```
Certainly these examples should go into the  docstrings. Most of these can be trivially fixed, but it would be good if someone could review permutation groups with a view to catching these problems before they arise.



Issue created by migration from https://trac.sagemath.org/ticket/4521





---

archive/issue_comments_033488.json:
```json
{
    "body": "I took a quick look at the code today and I've come away with a bunch of questions.\n\n(1) Can you post the definition of degree? In the current code, degree it is set equal to largest_moved_point, which grabs the value from gap's LargestMovedPoint if it isn't properly set. But this doesn't seem to agree with some of the things mentioned above.\n\n(2) Which group should the following command return?\n\n```\nsage: G = PermutationGroup([],degree=4)\n```\n\n(3) The following two groups are isomorphic:\n\n```\nsage: G = PermutationGroup([[]]) \nsage: G = PermutationGroup([ [1] ])\n```\nThis is because\n\n```\nsage: PermutationGroupElement([]).list()\n[1]\nsage: PermutationGroupElement([1]).list()\n[1]\n```\nSo I'm not sure why one group should have degree 0 while the other does not.\n\n(4) What should the degrees of SymmetricGroup(0) and SymmetricGroup(1) be? Should SymmetricGroup(0) == SymmetricGroup(1)?\n\nI think these are all my questions for now.",
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

archive/issue_events_010258.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-01-09T23:27:08Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4521",
    "milestone": "sage-3.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4521#event-10258"
}
```



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

archive/issue_events_010259.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4521",
    "milestone": "sage-3.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4521#event-10259"
}
```



---

archive/issue_events_010260.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4521",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4521#event-10260"
}
```



---

archive/issue_events_010261.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4521",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4521#event-10261"
}
```



---

archive/issue_events_010262.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4521",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4521#event-10262"
}
```



---

archive/issue_events_010263.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4521",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4521#event-10263"
}
```



---

archive/issue_events_010264.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4521",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4521#event-10264"
}
```



---

archive/issue_events_010265.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4521",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4521#event-10265"
}
```



---

archive/issue_events_010266.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4521",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4521#event-10266"
}
```



---

archive/issue_comments_033491.json:
```json
{
    "body": "This is a bug\n\n```\nsage: PermutationGroupElement([]).list()\n[1]\n```\n`PermutationGroupElement([])` should really be the unique permutation of the empty set.",
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

archive/issue_events_010267.json:
```json
{
    "actor": "https://github.com/videlec",
    "created_at": "2019-10-28T14:48:59Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4521",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4521#event-10267"
}
```



---

archive/issue_events_010268.json:
```json
{
    "actor": "https://github.com/videlec",
    "created_at": "2019-10-28T14:48:59Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4521",
    "milestone": "sage-9.0",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4521#event-10268"
}
```



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

archive/issue_events_010269.json:
```json
{
    "actor": "https://github.com/embray",
    "created_at": "2020-01-06T14:10:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4521",
    "milestone": "sage-9.0",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4521#event-10269"
}
```



---

archive/issue_events_010270.json:
```json
{
    "actor": "https://github.com/embray",
    "created_at": "2020-01-06T14:10:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4521",
    "milestone": "sage-9.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4521#event-10270"
}
```



---

archive/issue_events_010271.json:
```json
{
    "actor": "https://github.com/mkoeppe",
    "created_at": "2020-04-14T19:41:51Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4521",
    "milestone": "sage-9.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4521#event-10271"
}
```



---

archive/issue_events_010272.json:
```json
{
    "actor": "https://github.com/mkoeppe",
    "created_at": "2020-04-14T19:41:51Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4521",
    "milestone": "sage-9.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4521#event-10272"
}
```



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

archive/issue_events_010273.json:
```json
{
    "actor": "https://github.com/mkoeppe",
    "created_at": "2020-09-05T19:21:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4521",
    "milestone": "sage-9.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4521#event-10273"
}
```



---

archive/issue_events_010274.json:
```json
{
    "actor": "https://github.com/mkoeppe",
    "created_at": "2020-09-05T19:21:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4521",
    "milestone": "sage-9.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4521#event-10274"
}
```



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

archive/issue_events_010275.json:
```json
{
    "actor": "https://github.com/mkoeppe",
    "created_at": "2021-02-13T20:51:01Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4521",
    "milestone": "sage-9.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4521#event-10275"
}
```



---

archive/issue_events_010276.json:
```json
{
    "actor": "https://github.com/mkoeppe",
    "created_at": "2021-02-13T20:51:01Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4521",
    "milestone": "sage-9.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4521#event-10276"
}
```



---

archive/issue_events_010277.json:
```json
{
    "actor": "https://github.com/mkoeppe",
    "created_at": "2021-07-19T00:44:56Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4521",
    "milestone": "sage-9.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4521#event-10277"
}
```



---

archive/issue_events_010278.json:
```json
{
    "actor": "https://github.com/mkoeppe",
    "created_at": "2021-07-19T00:44:56Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4521",
    "milestone": "sage-9.5",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4521#event-10278"
}
```



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



---

archive/issue_events_010279.json:
```json
{
    "actor": "https://github.com/mkoeppe",
    "created_at": "2021-12-18T19:24:17Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4521",
    "milestone": "sage-9.5",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4521#event-10279"
}
```



---

archive/issue_events_010280.json:
```json
{
    "actor": "https://github.com/mkoeppe",
    "created_at": "2021-12-18T19:24:17Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4521",
    "milestone": "sage-9.6",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4521#event-10280"
}
```



---

archive/issue_events_010281.json:
```json
{
    "actor": "https://github.com/mkoeppe",
    "created_at": "2022-04-07T00:07:21Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4521",
    "milestone": "sage-9.6",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4521#event-10281"
}
```



---

archive/issue_events_010282.json:
```json
{
    "actor": "https://github.com/mkoeppe",
    "created_at": "2022-04-07T00:07:21Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4521",
    "milestone": "sage-9.7",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4521#event-10282"
}
```



---

archive/issue_events_010283.json:
```json
{
    "actor": "https://github.com/mkoeppe",
    "created_at": "2022-09-19T18:58:47Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4521",
    "milestone": "sage-9.7",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4521#event-10283"
}
```



---

archive/issue_events_010284.json:
```json
{
    "actor": "https://github.com/mkoeppe",
    "created_at": "2022-09-19T18:58:47Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4521",
    "milestone": "sage-9.8",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4521#event-10284"
}
```
