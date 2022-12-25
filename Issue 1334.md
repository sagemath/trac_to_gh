# Issue 1334: Constant polynomial can't be converted to rational

archive/issues_001334.json:
```json
{
    "body": "Assignee: somebody\n\n\n```\nsage: R.<x> = QQ['x']\nsage: QQ(R(1/2))\nTraceback (most recent call last):\n...\nTypeError: Unable to coerce 1/2 (<type 'sage.rings.polynomial.polynomial_element.Polynomial_generic_dense'>) to Rational\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1334\n\n",
    "created_at": "2007-11-29T09:31:42Z",
    "labels": [
        "component: basic arithmetic",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.15",
    "title": "Constant polynomial can't be converted to rational",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1334",
    "user": "https://github.com/robertwb"
}
```
Assignee: somebody


```
sage: R.<x> = QQ['x']
sage: QQ(R(1/2))
Traceback (most recent call last):
...
TypeError: Unable to coerce 1/2 (<type 'sage.rings.polynomial.polynomial_element.Polynomial_generic_dense'>) to Rational
```


Issue created by migration from https://trac.sagemath.org/ticket/1334





---

archive/issue_comments_008507.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-12-01T17:20:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1334",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1334#issuecomment-8507",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```

Changing status from new to assigned.



---

archive/issue_comments_008508.json:
```json
{
    "body": "Changing assignee from somebody to dmharvey.",
    "created_at": "2007-12-01T17:20:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1334",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1334#issuecomment-8508",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```

Changing assignee from somebody to dmharvey.



---

archive/issue_comments_008509.json:
```json
{
    "body": "Fixed it:\n\n\n```\nsage: R.<x> = QQ['x']\nsage: QQ(R(1/2))\n1/2\n```\n\n\nMore generally this patch allows coercion of any polynomial to QQ, as long as it's a constant polynomial whose constant term can be coerced into QQ.",
    "created_at": "2007-12-01T17:45:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1334",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1334#issuecomment-8509",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```

Fixed it:


```
sage: R.<x> = QQ['x']
sage: QQ(R(1/2))
1/2
```


More generally this patch allows coercion of any polynomial to QQ, as long as it's a constant polynomial whose constant term can be coerced into QQ.



---

archive/issue_comments_008510.json:
```json
{
    "body": "Attachment [1334.hg](tarball://root/attachments/some-uuid/ticket1334/1334.hg) by dmharvey created at 2007-12-01 17:46:46",
    "created_at": "2007-12-01T17:46:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1334",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1334#issuecomment-8510",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```

Attachment [1334.hg](tarball://root/attachments/some-uuid/ticket1334/1334.hg) by dmharvey created at 2007-12-01 17:46:46



---

archive/issue_comments_008511.json:
```json
{
    "body": "Looks good to me.  (doctests pass, code looks good)",
    "created_at": "2007-12-01T18:03:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1334",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1334#issuecomment-8511",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Looks good to me.  (doctests pass, code looks good)



---

archive/issue_comments_008512.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-01T18:08:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1334",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1334#issuecomment-8512",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_001474.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2007-12-01T18:08:34Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1334",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1334#event-1474"
}
```



---

archive/issue_comments_008513.json:
```json
{
    "body": "Merged in 2.8.15.alpha1.",
    "created_at": "2007-12-01T18:08:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1334",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1334#issuecomment-8513",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in 2.8.15.alpha1.
