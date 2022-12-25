# Issue 4623: x^2 is wrong in RealIntervalField

archive/issues_004623.json:
```json
{
    "body": "Assignee: somebody\n\n```\nsage: R=RealIntervalField(53)\nsage: x=R(-1,2)\nsage: xx=x^2\nsage: xx.lower(), xx.upper()\n(-2.00000000000000, 4.00000000000000)\n```\nThe result should be (0, 4) instead, since for -1 <= x <= 2, we have 0 <= x^2 <= 4.\n(Of course (-2, 4) is a correct enclosure, but any specialist of interval arithmetic\nwill consider that as a real bug.)\n\nIssue created by migration from https://trac.sagemath.org/ticket/4623\n\n",
    "created_at": "2008-11-26T14:04:05Z",
    "labels": [
        "component: basic arithmetic",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "x^2 is wrong in RealIntervalField",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4623",
    "user": "https://github.com/zimmermann6"
}
```
Assignee: somebody

```
sage: R=RealIntervalField(53)
sage: x=R(-1,2)
sage: xx=x^2
sage: xx.lower(), xx.upper()
(-2.00000000000000, 4.00000000000000)
```
The result should be (0, 4) instead, since for -1 <= x <= 2, we have 0 <= x^2 <= 4.
(Of course (-2, 4) is a correct enclosure, but any specialist of interval arithmetic
will consider that as a real bug.)

Issue created by migration from https://trac.sagemath.org/ticket/4623





---

archive/issue_comments_034698.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2009-01-22T18:19:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4623",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4623#issuecomment-34698",
    "user": "https://github.com/aghitza"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_034699.json:
```json
{
    "body": "Attachment [11285.patch](tarball://root/attachments/some-uuid/ticket4623/11285.patch) by @zimmermann6 created at 2009-01-22 21:14:17\n\nThe attachment fixes that problem, and adds some doctest examples.\n\nFor the reviewer:\n* I'm not sure divmod is the best way to test if a number is even\n* I'm not sure .abs() is the best way to force the lower bound to 0\n\nNote also that x^0 returns 1, which is not an interval (but that was already the case before\nthat patch).",
    "created_at": "2009-01-22T21:14:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4623",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4623#issuecomment-34699",
    "user": "https://github.com/zimmermann6"
}
```

Attachment [11285.patch](tarball://root/attachments/some-uuid/ticket4623/11285.patch) by @zimmermann6 created at 2009-01-22 21:14:17

The attachment fixes that problem, and adds some doctest examples.

For the reviewer:
* I'm not sure divmod is the best way to test if a number is even
* I'm not sure .abs() is the best way to force the lower bound to 0

Note also that x^0 returns 1, which is not an interval (but that was already the case before
that patch).



---

archive/issue_comments_034700.json:
```json
{
    "body": "Attachment [trac_4623.patch](tarball://root/attachments/some-uuid/ticket4623/trac_4623.patch) by @aghitza created at 2009-01-24 07:05:15\n\napply on top of the previous patch",
    "created_at": "2009-01-24T07:05:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4623",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4623#issuecomment-34700",
    "user": "https://github.com/aghitza"
}
```

Attachment [trac_4623.patch](tarball://root/attachments/some-uuid/ticket4623/trac_4623.patch) by @aghitza created at 2009-01-24 07:05:15

apply on top of the previous patch



---

archive/issue_comments_034701.json:
```json
{
    "body": "Looks good to me.  I have tried a few other approaches to the two questions Paul asked above, but they turn out to be slower, so I think the patch is good to go as it is.\n\nI have made a tiny modification that makes the frequent special case exponent=2 almost three times faster.  Apply both patches to 3.3.alpha1.",
    "created_at": "2009-01-24T07:05:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4623",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4623#issuecomment-34701",
    "user": "https://github.com/aghitza"
}
```

Looks good to me.  I have tried a few other approaches to the two questions Paul asked above, but they turn out to be slower, so I think the patch is good to go as it is.

I have made a tiny modification that makes the frequent special case exponent=2 almost three times faster.  Apply both patches to 3.3.alpha1.



---

archive/issue_comments_034702.json:
```json
{
    "body": "thanks Alex for your review. I was not aware of x.square(). Then probably we should replace\nxq * xq by xq.square() in my patch:\n\n```\nsage: x=RealIntervalField(53)((-e,pi))\nsage: %timeit x.square()\n1000000 loops, best of 3: 769 ns per loop\nsage: %timeit (x * x)\n1000000 loops, best of 3: 948 ns per loop\n```",
    "created_at": "2009-01-24T10:18:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4623",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4623#issuecomment-34702",
    "user": "https://github.com/zimmermann6"
}
```

thanks Alex for your review. I was not aware of x.square(). Then probably we should replace
xq * xq by xq.square() in my patch:

```
sage: x=RealIntervalField(53)((-e,pi))
sage: %timeit x.square()
1000000 loops, best of 3: 769 ns per loop
sage: %timeit (x * x)
1000000 loops, best of 3: 948 ns per loop
```



---

archive/issue_comments_034703.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-24T17:14:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4623",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4623#issuecomment-34703",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_010540.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-01-24T17:14:10Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4623",
    "milestone": "sage-3.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4623#event-10540"
}
```



---

archive/issue_comments_034704.json:
```json
{
    "body": "Merged in Sage 3.3.alpha2",
    "created_at": "2009-01-24T17:14:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4623",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4623#issuecomment-34704",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.3.alpha2



---

archive/issue_events_010541.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-01-24T17:14:10Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4623",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4623#event-10541"
}
```



---

archive/issue_comments_034705.json:
```json
{
    "body": "Attachment [trac_4623_2.patch](tarball://root/attachments/some-uuid/ticket4623/trac_4623_2.patch) by @zimmermann6 created at 2009-01-24 19:34:33",
    "created_at": "2009-01-24T19:34:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4623",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4623#issuecomment-34705",
    "user": "https://github.com/zimmermann6"
}
```

Attachment [trac_4623_2.patch](tarball://root/attachments/some-uuid/ticket4623/trac_4623_2.patch) by @zimmermann6 created at 2009-01-24 19:34:33



---

archive/issue_comments_034706.json:
```json
{
    "body": "trac_4623_2.patch looks good and has been merged in Sage 3.3.alpha2.\n\nCheers,\n\nMichael",
    "created_at": "2009-01-24T20:05:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4623",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4623#issuecomment-34706",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

trac_4623_2.patch looks good and has been merged in Sage 3.3.alpha2.

Cheers,

Michael
