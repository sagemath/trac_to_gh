# Issue 1863: implement f.change_ring(R) for f a multivariate polynomial

archive/issues_001863.json:
```json
{
    "body": "Assignee: @malb\n\nThis works:\n\n```\nsage: R.<x> = QQ[]\nsage: f = x^3 + 3/5\nsage: f.change_ring(GF(7))\nx^3 + 2\n```\n\nThis should work:\n\n```\nsage: R.<x,y> = QQ[]\nsage: f = x^3 + 3/5*y + 1\nsage: f.change_ring(GF(7))\nTraceback (most recent call last):\n...\nAttributeError: 'sage.rings.polynomial.multi_polynomial_libsingular' object has no attribute 'change_ring'\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1863\n\n",
    "created_at": "2008-01-20T16:36:56Z",
    "labels": [
        "component: commutative algebra"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "implement f.change_ring(R) for f a multivariate polynomial",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1863",
    "user": "https://github.com/williamstein"
}
```
Assignee: @malb

This works:

```
sage: R.<x> = QQ[]
sage: f = x^3 + 3/5
sage: f.change_ring(GF(7))
x^3 + 2
```

This should work:

```
sage: R.<x,y> = QQ[]
sage: f = x^3 + 3/5*y + 1
sage: f.change_ring(GF(7))
Traceback (most recent call last):
...
AttributeError: 'sage.rings.polynomial.multi_polynomial_libsingular' object has no attribute 'change_ring'
```


Issue created by migration from https://trac.sagemath.org/ticket/1863





---

archive/issue_comments_011768.json:
```json
{
    "body": "Attachment [trac_1863_change_ring.patch](tarball://root/attachments/some-uuid/ticket1863/trac_1863_change_ring.patch) by @malb created at 2008-03-28 12:11:21",
    "created_at": "2008-03-28T12:11:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1863",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1863#issuecomment-11768",
    "user": "https://github.com/malb"
}
```

Attachment [trac_1863_change_ring.patch](tarball://root/attachments/some-uuid/ticket1863/trac_1863_change_ring.patch) by @malb created at 2008-03-28 12:11:21



---

archive/issue_comments_011769.json:
```json
{
    "body": "The attached patch implements `change_ring`.",
    "created_at": "2008-03-28T12:11:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1863",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1863#issuecomment-11769",
    "user": "https://github.com/malb"
}
```

The attached patch implements `change_ring`.



---

archive/issue_comments_011770.json:
```json
{
    "body": "Attachment [1863.patch](tarball://root/attachments/some-uuid/ticket1863/1863.patch) by @mwhansen created at 2008-03-31 14:46:26",
    "created_at": "2008-03-31T14:46:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1863",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1863#issuecomment-11770",
    "user": "https://github.com/mwhansen"
}
```

Attachment [1863.patch](tarball://root/attachments/some-uuid/ticket1863/1863.patch) by @mwhansen created at 2008-03-31 14:46:26



---

archive/issue_comments_011771.json:
```json
{
    "body": "Looks good to me.  1863.patch is rebased and the one to apply.",
    "created_at": "2008-03-31T14:46:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1863",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1863#issuecomment-11771",
    "user": "https://github.com/mwhansen"
}
```

Looks good to me.  1863.patch is rebased and the one to apply.



---

archive/issue_events_002021.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-03-31T15:01:53Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1863",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1863#event-2021"
}
```



---

archive/issue_comments_011772.json:
```json
{
    "body": "Merged trac_1863_change_ring.patch in Sage 3.0.alpha0",
    "created_at": "2008-03-31T15:01:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1863",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1863#issuecomment-11772",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged trac_1863_change_ring.patch in Sage 3.0.alpha0



---

archive/issue_comments_011773.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-31T15:01:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1863",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1863#issuecomment-11773",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
