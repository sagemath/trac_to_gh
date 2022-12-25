# Issue 1148: valuation doesn't work for rational numbers

archive/issues_001148.json:
```json
{
    "body": "Assignee: somebody\n\nIt would be nice if `valuation(3/5, 5)` returned -1, but it does this:\n\n```\nsage: valuation(3/5, 5)\n---------------------------------------------------------------------------\n<type 'exceptions.ZeroDivisionError'>     Traceback (most recent call last)\n\n/Users/david/series/<ipython console> in <module>()\n\n/Users/david/sage-2.8.12/local/lib/python2.5/site-packages/sage/rings/arith.py in valuation(m, p)\n    425     r=0\n    426     power=p\n--> 427     while m%power==0:\n    428         r += 1\n    429         power *= p\n\n/Users/david/series/rational.pyx in sage.rings.rational.Rational.__mod__()\n\n/Users/david/series/integer.pyx in sage.rings.integer.Integer.inverse_mod()\n\n<type 'exceptions.ZeroDivisionError'>: Inverse does not exist.\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1148\n\n",
    "created_at": "2007-11-11T16:50:33Z",
    "labels": [
        "component: basic arithmetic",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.15",
    "title": "valuation doesn't work for rational numbers",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1148",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```
Assignee: somebody

It would be nice if `valuation(3/5, 5)` returned -1, but it does this:

```
sage: valuation(3/5, 5)
---------------------------------------------------------------------------
<type 'exceptions.ZeroDivisionError'>     Traceback (most recent call last)

/Users/david/series/<ipython console> in <module>()

/Users/david/sage-2.8.12/local/lib/python2.5/site-packages/sage/rings/arith.py in valuation(m, p)
    425     r=0
    426     power=p
--> 427     while m%power==0:
    428         r += 1
    429         power *= p

/Users/david/series/rational.pyx in sage.rings.rational.Rational.__mod__()

/Users/david/series/integer.pyx in sage.rings.integer.Integer.inverse_mod()

<type 'exceptions.ZeroDivisionError'>: Inverse does not exist.
```


Issue created by migration from https://trac.sagemath.org/ticket/1148





---

archive/issue_events_003089.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-11-15T02:23:33Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1148",
    "milestone": "sage-2.8.13",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1148#event-3089"
}
```



---

archive/issue_comments_006985.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-11-16T01:13:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1148",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1148#issuecomment-6985",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```

Changing status from new to assigned.



---

archive/issue_comments_006986.json:
```json
{
    "body": "Changing assignee from somebody to dmharvey.",
    "created_at": "2007-11-16T01:13:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1148",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1148#issuecomment-6986",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```

Changing assignee from somebody to dmharvey.



---

archive/issue_comments_006987.json:
```json
{
    "body": "Attachment [1148.hg](tarball://root/attachments/some-uuid/ticket1148/1148.hg) by dmharvey created at 2007-11-16 02:15:37\n\nfixed it",
    "created_at": "2007-11-16T02:15:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1148",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1148#issuecomment-6987",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```

Attachment [1148.hg](tarball://root/attachments/some-uuid/ticket1148/1148.hg) by dmharvey created at 2007-11-16 02:15:37

fixed it



---

archive/issue_comments_006988.json:
```json
{
    "body": "Attachment [1148-more.patch](tarball://root/attachments/some-uuid/ticket1148/1148-more.patch) by @robertwb created at 2007-11-18 08:52:58",
    "created_at": "2007-11-18T08:52:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1148",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1148#issuecomment-6988",
    "user": "https://github.com/robertwb"
}
```

Attachment [1148-more.patch](tarball://root/attachments/some-uuid/ticket1148/1148-more.patch) by @robertwb created at 2007-11-18 08:52:58



---

archive/issue_comments_006989.json:
```json
{
    "body": "I tried the combination of 1148.hg and 1148-more.patch patch against 2.8.14.  The source code looks reasonable, and doctesting arith.py and rational.pyx (the two files touched by the change) both succeed.  (I did not try testall.)\n\nIn other words, looks good to me.",
    "created_at": "2007-11-27T04:51:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1148",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1148#issuecomment-6989",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

I tried the combination of 1148.hg and 1148-more.patch patch against 2.8.14.  The source code looks reasonable, and doctesting arith.py and rational.pyx (the two files touched by the change) both succeed.  (I did not try testall.)

In other words, looks good to me.



---

archive/issue_events_003090.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-12-01T18:51:29Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1148",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1148#event-3090"
}
```



---

archive/issue_comments_006990.json:
```json
{
    "body": "Merged in 2.8.15.alpha1.",
    "created_at": "2007-12-01T18:51:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1148",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1148#issuecomment-6990",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in 2.8.15.alpha1.



---

archive/issue_comments_006991.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-01T18:51:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1148",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1148#issuecomment-6991",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
