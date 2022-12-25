# Issue 4573: Permutation not callable, but PermutationGroupElement is.

archive/issues_004573.json:
```json
{
    "body": "Assignee: @saliola\n\nCC:  sage-combinat\n\n\n```\nsage: p = PermutationGroupElement([2, 1, 4, 5, 3])\nsage: p(1)\n2\nsage: q = Permutation([2, 1, 4, 5, 3])\nsage: q(1)\n...\nTypeError: 'Permutation_class' object is not callable\n```\n\n\nThis causes me some confusion.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4573\n\n",
    "created_at": "2008-11-20T22:15:08Z",
    "labels": [
        "component: combinatorics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.1",
    "title": "Permutation not callable, but PermutationGroupElement is.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4573",
    "user": "https://github.com/saliola"
}
```
Assignee: @saliola

CC:  sage-combinat


```
sage: p = PermutationGroupElement([2, 1, 4, 5, 3])
sage: p(1)
2
sage: q = Permutation([2, 1, 4, 5, 3])
sage: q(1)
...
TypeError: 'Permutation_class' object is not callable
```


This causes me some confusion.

Issue created by migration from https://trac.sagemath.org/ticket/4573





---

archive/issue_comments_034200.json:
```json
{
    "body": "Attachment [trac_4573.patch](tarball://root/attachments/some-uuid/ticket4573/trac_4573.patch) by @saliola created at 2008-11-20 22:16:32\n\n(against 3.2.rc2)",
    "created_at": "2008-11-20T22:16:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4573",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4573#issuecomment-34200",
    "user": "https://github.com/saliola"
}
```

Attachment [trac_4573.patch](tarball://root/attachments/some-uuid/ticket4573/trac_4573.patch) by @saliola created at 2008-11-20 22:16:32

(against 3.2.rc2)



---

archive/issue_comments_034201.json:
```json
{
    "body": "Looks good.",
    "created_at": "2008-11-21T14:47:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4573",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4573#issuecomment-34201",
    "user": "https://github.com/mwhansen"
}
```

Looks good.



---

archive/issue_events_004818.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-11-21T20:23:17Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4573",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4573#event-4818"
}
```



---

archive/issue_comments_034202.json:
```json
{
    "body": "Merged in Sage 3.2.1.alpha0",
    "created_at": "2008-11-21T20:23:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4573",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4573#issuecomment-34202",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.2.1.alpha0



---

archive/issue_comments_034203.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-11-21T20:23:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4573",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4573#issuecomment-34203",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
