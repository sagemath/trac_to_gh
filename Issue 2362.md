# Issue 2362: Integer digits method

archive/issues_002362.json:
```json
{
    "body": "Assignee: somebody\n\nThe digits method should take large bases.\n\n```\nsage: n=982352935629356293856239856239852352352\nsage: n.digits(928365923856928)\n...\n<type 'exceptions.OverflowError'>: long int too large to convert to int\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2362\n\n",
    "created_at": "2008-03-01T20:09:20Z",
    "labels": [
        "component: basic arithmetic",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.4",
    "title": "Integer digits method",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2362",
    "user": "https://trac.sagemath.org/admin/accounts/users/jbmohler"
}
```
Assignee: somebody

The digits method should take large bases.

```
sage: n=982352935629356293856239856239852352352
sage: n.digits(928365923856928)
...
<type 'exceptions.OverflowError'>: long int too large to convert to int
```


Issue created by migration from https://trac.sagemath.org/ticket/2362





---

archive/issue_events_005573.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/jbmohler",
    "created_at": "2008-03-02T05:51:15Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2362",
    "milestone": "sage-2.10.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2362#event-5573"
}
```



---

archive/issue_comments_015890.json:
```json
{
    "body": "I've added a patch which fixes this bug and 2170.\n\n```\nsage: n=3^100000\nsage: time _=n.digits(10)  # evidence of fixing 2170\nCPU times: user 0.07 s, sys: 0.00 s, total: 0.07 s\nWall time: 0.07\nsage: time _=n.str(10)\nCPU times: user 0.02 s, sys: 0.00 s, total: 0.02 s\nWall time: 0.02\nsage: time _=n.digits(10^40)  # evidence of fixing this bug\nCPU times: user 0.03 s, sys: 0.00 s, total: 0.03 s\nWall time: 0.03\n```",
    "created_at": "2008-03-02T05:51:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2362",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2362#issuecomment-15890",
    "user": "https://trac.sagemath.org/admin/accounts/users/jbmohler"
}
```

I've added a patch which fixes this bug and 2170.

```
sage: n=3^100000
sage: time _=n.digits(10)  # evidence of fixing 2170
CPU times: user 0.07 s, sys: 0.00 s, total: 0.07 s
Wall time: 0.07
sage: time _=n.str(10)
CPU times: user 0.02 s, sys: 0.00 s, total: 0.02 s
Wall time: 0.02
sage: time _=n.digits(10^40)  # evidence of fixing this bug
CPU times: user 0.03 s, sys: 0.00 s, total: 0.03 s
Wall time: 0.03
```



---

archive/issue_comments_015891.json:
```json
{
    "body": "Could you add the extremely impressive times in your comment above to the docstring. \n\nBy the way, EXCELLENT WORK on this  -- it's fast.  Excellent!",
    "created_at": "2008-03-02T08:14:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2362",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2362#issuecomment-15891",
    "user": "https://github.com/williamstein"
}
```

Could you add the extremely impressive times in your comment above to the docstring. 

By the way, EXCELLENT WORK on this  -- it's fast.  Excellent!



---

archive/issue_comments_015892.json:
```json
{
    "body": "Attachment [digits.2.patch](tarball://root/attachments/some-uuid/ticket2362/digits.2.patch) by jbmohler created at 2008-03-03 20:20:53",
    "created_at": "2008-03-03T20:20:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2362",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2362#issuecomment-15892",
    "user": "https://trac.sagemath.org/admin/accounts/users/jbmohler"
}
```

Attachment [digits.2.patch](tarball://root/attachments/some-uuid/ticket2362/digits.2.patch) by jbmohler created at 2008-03-03 20:20:53



---

archive/issue_comments_015893.json:
```json
{
    "body": "Use digits.2.patch.\n\nThis new patch fixes up some speed regressions compared to unpatched 2.10.2.  It seems that small cases are much better off using the naive base-conversion algorithm.  It also fixes some things so that we are just a bit faster for large input.\n\nNote that I also tweaked the ndigits method just a bit so that it works for arbitrary large input.",
    "created_at": "2008-03-03T20:24:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2362",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2362#issuecomment-15893",
    "user": "https://trac.sagemath.org/admin/accounts/users/jbmohler"
}
```

Use digits.2.patch.

This new patch fixes up some speed regressions compared to unpatched 2.10.2.  It seems that small cases are much better off using the naive base-conversion algorithm.  It also fixes some things so that we are just a bit faster for large input.

Note that I also tweaked the ndigits method just a bit so that it works for arbitrary large input.



---

archive/issue_events_005574.json:
```json
{
    "actor": "https://github.com/rlmill",
    "created_at": "2008-03-12T05:17:04Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2362",
    "milestone": "sage-2.10.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2362#event-5574"
}
```



---

archive/issue_events_005575.json:
```json
{
    "actor": "https://github.com/rlmill",
    "created_at": "2008-03-12T05:17:04Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2362",
    "milestone": "sage-2.10.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2362#event-5575"
}
```



---

archive/issue_comments_015894.json:
```json
{
    "body": "Attachment [digits.patch](tarball://root/attachments/some-uuid/ticket2362/digits.patch) by jbmohler created at 2008-03-13 14:39:40\n\nNow, you should use digits.patch\n\nThis latest patch has been rebased on 2.10.3",
    "created_at": "2008-03-13T14:39:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2362",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2362#issuecomment-15894",
    "user": "https://trac.sagemath.org/admin/accounts/users/jbmohler"
}
```

Attachment [digits.patch](tarball://root/attachments/some-uuid/ticket2362/digits.patch) by jbmohler created at 2008-03-13 14:39:40

Now, you should use digits.patch

This latest patch has been rebased on 2.10.3



---

archive/issue_comments_015895.json:
```json
{
    "body": "Looks good to me.  Note that this basically forces a -ba due to a change in integer.pxd.",
    "created_at": "2008-03-15T22:16:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2362",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2362#issuecomment-15895",
    "user": "https://github.com/mwhansen"
}
```

Looks good to me.  Note that this basically forces a -ba due to a change in integer.pxd.



---

archive/issue_comments_015896.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-16T00:07:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2362",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2362#issuecomment-15896",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_005576.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-03-16T00:07:23Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2362",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2362#event-5576"
}
```



---

archive/issue_comments_015897.json:
```json
{
    "body": "Merged digits.patch in Sage 2.10.4.rc0",
    "created_at": "2008-03-16T00:07:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2362",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2362#issuecomment-15897",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged digits.patch in Sage 2.10.4.rc0
