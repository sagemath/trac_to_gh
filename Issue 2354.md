# Issue 2354: bug in matrix_real_double_dense  (trivial to fix)

archive/issues_002354.json:
```json
{
    "body": "Assignee: @williamstein\n\n\n```\n        _n.flags = _n.flags|(NPY_OWNDATA) # this sets the ownership bug\n```\n\n\nbut should be\n\n```\n        _n.flags = _n.flags|(NPY_OWNDATA) # this sets the ownership bit\n```\n\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2354\n\n",
    "created_at": "2008-02-29T17:41:14Z",
    "labels": [
        "component: linear algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.4",
    "title": "bug in matrix_real_double_dense  (trivial to fix)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2354",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein


```
        _n.flags = _n.flags|(NPY_OWNDATA) # this sets the ownership bug
```


but should be

```
        _n.flags = _n.flags|(NPY_OWNDATA) # this sets the ownership bit
```




Issue created by migration from https://trac.sagemath.org/ticket/2354





---

archive/issue_comments_015793.json:
```json
{
    "body": "Attachment [2354.patch](tarball://root/attachments/some-uuid/ticket2354/2354.patch) by @dfdeshom created at 2008-03-03 17:57:00",
    "created_at": "2008-03-03T17:57:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2354",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2354#issuecomment-15793",
    "user": "https://github.com/dfdeshom"
}
```

Attachment [2354.patch](tarball://root/attachments/some-uuid/ticket2354/2354.patch) by @dfdeshom created at 2008-03-03 17:57:00



---

archive/issue_comments_015794.json:
```json
{
    "body": "Changing priority from major to trivial.",
    "created_at": "2008-03-03T17:57:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2354",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2354#issuecomment-15794",
    "user": "https://github.com/dfdeshom"
}
```

Changing priority from major to trivial.



---

archive/issue_comments_015795.json:
```json
{
    "body": "Changing assignee from @williamstein to @dfdeshom.",
    "created_at": "2008-03-03T17:57:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2354",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2354#issuecomment-15795",
    "user": "https://github.com/dfdeshom"
}
```

Changing assignee from @williamstein to @dfdeshom.



---

archive/issue_comments_015796.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-03-03T17:57:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2354",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2354#issuecomment-15796",
    "user": "https://github.com/dfdeshom"
}
```

Changing status from new to assigned.



---

archive/issue_comments_015797.json:
```json
{
    "body": "Looks good.",
    "created_at": "2008-03-11T01:10:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2354",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2354#issuecomment-15797",
    "user": "https://github.com/aghitza"
}
```

Looks good.



---

archive/issue_comments_015798.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-12T22:09:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2354",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2354#issuecomment-15798",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_015799.json:
```json
{
    "body": "Merged in Sage 2.10.4.alpha0",
    "created_at": "2008-03-12T22:09:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2354",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2354#issuecomment-15799",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.4.alpha0
