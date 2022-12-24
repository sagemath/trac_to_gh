# Issue 2081: Add .coefficients() and .exponents() to univariate polynomials and power series

archive/issues_002081.json:
```json
{
    "body": "Assignee: somebody\n\nThis should work:\n\n\n```\nsage: R.<x> = QQ[]\nsage: f = x^2+2*x\nsage: f.exponents()\n[1, 2]\nsage: f.coefficients()\n[2, 1]\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2081\n\n",
    "created_at": "2008-02-07T07:39:15Z",
    "labels": [
        "basic arithmetic",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.2",
    "title": "Add .coefficients() and .exponents() to univariate polynomials and power series",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2081",
    "user": "@jbandlow"
}
```
Assignee: somebody

This should work:


```
sage: R.<x> = QQ[]
sage: f = x^2+2*x
sage: f.exponents()
[1, 2]
sage: f.coefficients()
[2, 1]
```


Issue created by migration from https://trac.sagemath.org/ticket/2081





---

archive/issue_comments_013472.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-02-07T07:47:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2081",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2081#issuecomment-13472",
    "user": "@mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_013473.json:
```json
{
    "body": "Changing assignee from somebody to @mwhansen.",
    "created_at": "2008-02-07T07:47:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2081",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2081#issuecomment-13473",
    "user": "@mwhansen"
}
```

Changing assignee from somebody to @mwhansen.



---

archive/issue_comments_013474.json:
```json
{
    "body": "The patch looks good, one thing though: every parent is supposed to provide a `zero_element()` method, this could be used (but that isn't really important)",
    "created_at": "2008-02-14T23:43:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2081",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2081#issuecomment-13474",
    "user": "@malb"
}
```

The patch looks good, one thing though: every parent is supposed to provide a `zero_element()` method, this could be used (but that isn't really important)



---

archive/issue_comments_013475.json:
```json
{
    "body": "Attachment [2081.patch](tarball://root/attachments/some-uuid/ticket2081/2081.patch) by @mwhansen created at 2008-02-14 23:56:03\n\nUpdated patch to use .zero_element()",
    "created_at": "2008-02-14T23:56:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2081",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2081#issuecomment-13475",
    "user": "@mwhansen"
}
```

Attachment [2081.patch](tarball://root/attachments/some-uuid/ticket2081/2081.patch) by @mwhansen created at 2008-02-14 23:56:03

Updated patch to use .zero_element()



---

archive/issue_comments_013476.json:
```json
{
    "body": "`make test` passes, patch looks good, apply!",
    "created_at": "2008-02-15T00:37:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2081",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2081#issuecomment-13476",
    "user": "@malb"
}
```

`make test` passes, patch looks good, apply!



---

archive/issue_comments_013477.json:
```json
{
    "body": "Merged in Sage 2.10.2.alpha0",
    "created_at": "2008-02-15T02:16:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2081",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2081#issuecomment-13477",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.2.alpha0



---

archive/issue_comments_013478.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-15T02:16:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2081",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2081#issuecomment-13478",
    "user": "mabshoff"
}
```

Resolution: fixed
