# Issue 762: Elliptic curve L-series bug

archive/issues_000762.json:
```json
{
    "body": "Assignee: @williamstein\n\nThere is a bug in computing the values along a line of the L-series:\n\n\n```\nsage: E = EllipticCurve('389a')\nsage: L = E.Lseries_dokchitser()\nsage: E.Lseries_values_along_line(0.5, 3, 5)\nTraceback (most recent call last):\n...\nValueError: too many values to unpack\n```\n\n\nThis is just a light wrapper around Rubinstein's lcalc, so should be very easy to fix.\n\nIssue created by migration from https://trac.sagemath.org/ticket/762\n\n",
    "created_at": "2007-09-30T04:34:43Z",
    "labels": [
        "component: number theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.11",
    "title": "Elliptic curve L-series bug",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/762",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

There is a bug in computing the values along a line of the L-series:


```
sage: E = EllipticCurve('389a')
sage: L = E.Lseries_dokchitser()
sage: E.Lseries_values_along_line(0.5, 3, 5)
Traceback (most recent call last):
...
ValueError: too many values to unpack
```


This is just a light wrapper around Rubinstein's lcalc, so should be very easy to fix.

Issue created by migration from https://trac.sagemath.org/ticket/762





---

archive/issue_comments_004498.json:
```json
{
    "body": "With 2.8.10.alpha1 we are getting a different error:\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n| SAGE Version 2.8.10.alpha1, Release Date: 2007-10-27               |\n| Type notebook() for the GUI, and license() for information.        |\nsage: sage: E = EllipticCurve('389a')\nsage: sage: L = E.Lseries_dokchitser()\n---------------------------------------------------------------------------\n<type 'exceptions.AttributeError'>        Traceback (most recent call last)\n\n/tmp/Work-mabshoff/sage-2.8.10.alpha1/<ipython console> in <module>()\n\n<type 'exceptions.AttributeError'>: 'EllipticCurve_rational_field' object has no attribute 'Lseries_dokchitser'\nsage: sage: E.Lseries_values_along_line(0.5, 3, 5)\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2007-10-28T23:27:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/762",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/762#issuecomment-4498",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

With 2.8.10.alpha1 we are getting a different error:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 2.8.10.alpha1, Release Date: 2007-10-27               |
| Type notebook() for the GUI, and license() for information.        |
sage: sage: E = EllipticCurve('389a')
sage: sage: L = E.Lseries_dokchitser()
---------------------------------------------------------------------------
<type 'exceptions.AttributeError'>        Traceback (most recent call last)

/tmp/Work-mabshoff/sage-2.8.10.alpha1/<ipython console> in <module>()

<type 'exceptions.AttributeError'>: 'EllipticCurve_rational_field' object has no attribute 'Lseries_dokchitser'
sage: sage: E.Lseries_values_along_line(0.5, 3, 5)
```


Cheers,

Michael



---

archive/issue_comments_004499.json:
```json
{
    "body": "this fixes the bug.",
    "created_at": "2007-10-28T23:58:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/762",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/762#issuecomment-4499",
    "user": "https://github.com/williamstein"
}
```

this fixes the bug.



---

archive/issue_comments_004500.json:
```json
{
    "body": "Attachment [trac762.patch](tarball://root/attachments/some-uuid/ticket762/trac762.patch) by @williamstein created at 2007-10-28 23:58:57",
    "created_at": "2007-10-28T23:58:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/762",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/762#issuecomment-4500",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac762.patch](tarball://root/attachments/some-uuid/ticket762/trac762.patch) by @williamstein created at 2007-10-28 23:58:57



---

archive/issue_events_002083.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-10-29T06:00:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/762",
    "milestone": "sage-2.8.11",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/762#event-2083"
}
```



---

archive/issue_comments_004501.json:
```json
{
    "body": "applied to 2.8.11.alpha0",
    "created_at": "2007-11-01T09:43:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/762",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/762#issuecomment-4501",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

applied to 2.8.11.alpha0



---

archive/issue_events_002084.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-11-01T09:43:21Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/762",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/762#event-2084"
}
```



---

archive/issue_comments_004502.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-11-01T09:43:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/762",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/762#issuecomment-4502",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
