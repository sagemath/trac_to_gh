# Issue 4581: Permutation constructor fails with PermutationGroupElement

archive/issues_004581.json:
```json
{
    "body": "Assignee: @mwhansen\n\nCC:  @rlmill sage-combinat\n\nSince PermutationGroupElement accepts Permutations:\n\n```\nsage: PermutationGroupElement(Permutation([2,1,3]))\n(1,2)\n```\n\nit would be good if the other direction worked as well:\n\n```\nsage: g = PermutationGroupElement([2,1,3])\nsage: g\n(1,2)\nsage: Permutation(g)\n...\nValueError: l must be a list\n```\n\nThe following works:\n\n```\nsage: Permutation(g.list())\n[2, 1, 3]\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4581\n\n",
    "created_at": "2008-11-22T01:45:10Z",
    "labels": [
        "component: combinatorics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.2",
    "title": "Permutation constructor fails with PermutationGroupElement",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4581",
    "user": "https://github.com/saliola"
}
```
Assignee: @mwhansen

CC:  @rlmill sage-combinat

Since PermutationGroupElement accepts Permutations:

```
sage: PermutationGroupElement(Permutation([2,1,3]))
(1,2)
```

it would be good if the other direction worked as well:

```
sage: g = PermutationGroupElement([2,1,3])
sage: g
(1,2)
sage: Permutation(g)
...
ValueError: l must be a list
```

The following works:

```
sage: Permutation(g.list())
[2, 1, 3]
```


Issue created by migration from https://trac.sagemath.org/ticket/4581





---

archive/issue_comments_034283.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-12-02T08:51:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4581",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4581#issuecomment-34283",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_034284.json:
```json
{
    "body": "Attachment [trac_4581.patch](tarball://root/attachments/some-uuid/ticket4581/trac_4581.patch) by @mwhansen created at 2008-12-02 08:51:03",
    "created_at": "2008-12-02T08:51:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4581",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4581#issuecomment-34284",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac_4581.patch](tarball://root/attachments/some-uuid/ticket4581/trac_4581.patch) by @mwhansen created at 2008-12-02 08:51:03



---

archive/issue_comments_034285.json:
```json
{
    "body": "rlm, \n\nI know you are busy, but can you give this a review? :)\n\nCheers,\n\nMichael",
    "created_at": "2008-12-02T15:55:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4581",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4581#issuecomment-34285",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

rlm, 

I know you are busy, but can you give this a review? :)

Cheers,

Michael



---

archive/issue_comments_034286.json:
```json
{
    "body": "The patch applies successfully and doctests pass here.",
    "created_at": "2008-12-02T16:18:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4581",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4581#issuecomment-34286",
    "user": "https://github.com/saliola"
}
```

The patch applies successfully and doctests pass here.



---

archive/issue_comments_034287.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-12-04T13:35:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4581",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4581#issuecomment-34287",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_034288.json:
```json
{
    "body": "Merged in Sage 3.2.2.alpha0",
    "created_at": "2008-12-04T13:35:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4581",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4581#issuecomment-34288",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.2.2.alpha0



---

archive/issue_events_004828.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-12-04T13:35:02Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4581",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4581#event-4828"
}
```
