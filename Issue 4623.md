# Issue 4623: x^2 is wrong in RealIntervalField

archive/issues_004623.json:
```json
{
    "body": "Assignee: somebody\n\n\n```\nsage: R=RealIntervalField(53)\nsage: x=R(-1,2)\nsage: xx=x^2\nsage: xx.lower(), xx.upper()\n(-2.00000000000000, 4.00000000000000)\n```\n\nThe result should be (0, 4) instead, since for -1 <= x <= 2, we have 0 <= x^2 <= 4.\n(Of course (-2, 4) is a correct enclosure, but any specialist of interval arithmetic\nwill consider that as a real bug.)\n\nIssue created by migration from https://trac.sagemath.org/ticket/4623\n\n",
    "created_at": "2008-11-26T14:04:05Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "title": "x^2 is wrong in RealIntervalField",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4623",
    "user": "zimmerma"
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

archive/issue_comments_034765.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2009-01-22T18:19:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4623",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4623#issuecomment-34765",
    "user": "AlexGhitza"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_034766.json:
```json
{
    "body": "Attachment\n\nThe attachment fixes that problem, and adds some doctest examples.\n\nFor the reviewer:\n* I'm not sure divmod is the best way to test if a number is even\n* I'm not sure .abs() is the best way to force the lower bound to 0\n\nNote also that x^0 returns 1, which is not an interval (but that was already the case before\nthat patch).",
    "created_at": "2009-01-22T21:14:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4623",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4623#issuecomment-34766",
    "user": "zimmerma"
}
```

Attachment

The attachment fixes that problem, and adds some doctest examples.

For the reviewer:
* I'm not sure divmod is the best way to test if a number is even
* I'm not sure .abs() is the best way to force the lower bound to 0

Note also that x^0 returns 1, which is not an interval (but that was already the case before
that patch).



---

archive/issue_comments_034767.json:
```json
{
    "body": "Attachment\n\napply on top of the previous patch",
    "created_at": "2009-01-24T07:05:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4623",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4623#issuecomment-34767",
    "user": "AlexGhitza"
}
```

Attachment

apply on top of the previous patch



---

archive/issue_comments_034768.json:
```json
{
    "body": "Looks good to me.  I have tried a few other approaches to the two questions Paul asked above, but they turn out to be slower, so I think the patch is good to go as it is.\n\nI have made a tiny modification that makes the frequent special case exponent=2 almost three times faster.  Apply both patches to 3.3.alpha1.",
    "created_at": "2009-01-24T07:05:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4623",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4623#issuecomment-34768",
    "user": "AlexGhitza"
}
```

Looks good to me.  I have tried a few other approaches to the two questions Paul asked above, but they turn out to be slower, so I think the patch is good to go as it is.

I have made a tiny modification that makes the frequent special case exponent=2 almost three times faster.  Apply both patches to 3.3.alpha1.



---

archive/issue_comments_034769.json:
```json
{
    "body": "thanks Alex for your review. I was not aware of x.square(). Then probably we should replace\nxq * xq by xq.square() in my patch:\n\n```\nsage: x=RealIntervalField(53)((-e,pi))\nsage: %timeit x.square()\n1000000 loops, best of 3: 769 ns per loop\nsage: %timeit (x * x)\n1000000 loops, best of 3: 948 ns per loop\n```\n",
    "created_at": "2009-01-24T10:18:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4623",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4623#issuecomment-34769",
    "user": "zimmerma"
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

archive/issue_comments_034770.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-24T17:14:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4623",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4623#issuecomment-34770",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_034771.json:
```json
{
    "body": "Merged in Sage 3.3.alpha2",
    "created_at": "2009-01-24T17:14:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4623",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4623#issuecomment-34771",
    "user": "mabshoff"
}
```

Merged in Sage 3.3.alpha2



---

archive/issue_comments_034772.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-01-24T19:34:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4623",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4623#issuecomment-34772",
    "user": "zimmerma"
}
```

Attachment



---

archive/issue_comments_034773.json:
```json
{
    "body": "trac_4623_2.patch looks good and has been merged in Sage 3.3.alpha2.\n\nCheers,\n\nMichael",
    "created_at": "2009-01-24T20:05:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4623",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4623#issuecomment-34773",
    "user": "mabshoff"
}
```

trac_4623_2.patch looks good and has been merged in Sage 3.3.alpha2.

Cheers,

Michael
