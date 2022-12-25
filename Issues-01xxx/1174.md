# Issue 1174: [with patch, with positive review] very minor bug in calculs _complex_ coercion.

archive/issues_001174.json:
```json
{
    "body": "Assignee: @williamstein\n\nStill broken (or perhaps something deeper)\n\n```\nsage: complex(cos(3))\n------------------------------------------------------------\nTraceback (most recent call last):\n  File \"<ipython console>\", line 1, in <module>\n  File \"/Users/robert/sage/current/local/lib/python2.5/site-packages/sage/calculus/calculus.py\", line 3908, in __complex__\n    return complex(f._approx_(complex(g)))\n<type 'exceptions.TypeError'>: can't convert complex to float; use abs(z)\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/1174\n\n",
    "closed_at": "2007-12-02T22:07:56Z",
    "created_at": "2007-11-15T07:46:36Z",
    "labels": [
        "component: calculus",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.15",
    "title": "[with patch, with positive review] very minor bug in calculs _complex_ coercion.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1174",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

Still broken (or perhaps something deeper)

```
sage: complex(cos(3))
------------------------------------------------------------
Traceback (most recent call last):
  File "<ipython console>", line 1, in <module>
  File "/Users/robert/sage/current/local/lib/python2.5/site-packages/sage/calculus/calculus.py", line 3908, in __complex__
    return complex(f._approx_(complex(g)))
<type 'exceptions.TypeError'>: can't convert complex to float; use abs(z)
```

Issue created by migration from https://trac.sagemath.org/ticket/1174





---

archive/issue_comments_007234.json:
```json
{
    "body": "Attachment [7349.patch](tarball://root/attachments/some-uuid/ticket1174/7349.patch) by @williamstein created at 2007-11-15 07:47:21\n\nI noticed this very slight mistake recently...",
    "created_at": "2007-11-15T07:47:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1174",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1174#issuecomment-7234",
    "user": "https://github.com/williamstein"
}
```

Attachment [7349.patch](tarball://root/attachments/some-uuid/ticket1174/7349.patch) by @williamstein created at 2007-11-15 07:47:21

I noticed this very slight mistake recently...



---

archive/issue_comments_007235.json:
```json
{
    "body": "I approve.",
    "created_at": "2007-11-18T08:34:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1174",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1174#issuecomment-7235",
    "user": "https://github.com/robertwb"
}
```

I approve.



---

archive/issue_comments_007236.json:
```json
{
    "body": "But there should be a doctest.",
    "created_at": "2007-11-18T08:34:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1174",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1174#issuecomment-7236",
    "user": "https://github.com/robertwb"
}
```

But there should be a doctest.



---

archive/issue_comments_007237.json:
```json
{
    "body": "The patch is good, the problem is that none of the python functions (e.g. sqrt, sin) handle complex values.",
    "created_at": "2007-12-02T07:21:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1174",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1174#issuecomment-7237",
    "user": "https://github.com/robertwb"
}
```

The patch is good, the problem is that none of the python functions (e.g. sqrt, sin) handle complex values.



---

archive/issue_comments_007238.json:
```json
{
    "body": "apply this after applying the other patch",
    "created_at": "2007-12-02T20:25:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1174",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1174#issuecomment-7238",
    "user": "https://github.com/williamstein"
}
```

apply this after applying the other patch



---

archive/issue_comments_007239.json:
```json
{
    "body": "Attachment [trac-1174-part2.patch](tarball://root/attachments/some-uuid/ticket1174/trac-1174-part2.patch) by @williamstein created at 2007-12-02 20:25:48",
    "created_at": "2007-12-02T20:25:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1174",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1174#issuecomment-7239",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac-1174-part2.patch](tarball://root/attachments/some-uuid/ticket1174/trac-1174-part2.patch) by @williamstein created at 2007-12-02 20:25:48



---

archive/issue_comments_007240.json:
```json
{
    "body": "Attachment [trac-1174-part3.patch](tarball://root/attachments/some-uuid/ticket1174/trac-1174-part3.patch) by cwitty created at 2007-12-02 21:39:11\n\nLooks good to me; doctests pass in sage/calculus and sage/rings.  (Apply all three patches, in order.)",
    "created_at": "2007-12-02T21:39:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1174",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1174#issuecomment-7240",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Attachment [trac-1174-part3.patch](tarball://root/attachments/some-uuid/ticket1174/trac-1174-part3.patch) by cwitty created at 2007-12-02 21:39:11

Looks good to me; doctests pass in sage/calculus and sage/rings.  (Apply all three patches, in order.)



---

archive/issue_events_003154.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-12-02T22:07:56Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1174",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1174#event-3154"
}
```



---

archive/issue_comments_007241.json:
```json
{
    "body": "Merged in 2.8.15.rc0.",
    "created_at": "2007-12-02T22:07:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1174",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1174#issuecomment-7241",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in 2.8.15.rc0.



---

archive/issue_comments_007242.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-02T22:07:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1174",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1174#issuecomment-7242",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
