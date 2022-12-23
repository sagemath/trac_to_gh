# Issue 2354: bug in matrix_real_double_dense  (trivial to fix)

archive/issues_002354.json:
```json
{
    "body": "Assignee: was\n\n\n```\n        _n.flags = _n.flags|(NPY_OWNDATA) # this sets the ownership bug\n```\n\n\nbut should be\n\n```\n        _n.flags = _n.flags|(NPY_OWNDATA) # this sets the ownership bit\n```\n\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2354\n\n",
    "created_at": "2008-02-29T17:41:14Z",
    "labels": [
        "linear algebra",
        "major",
        "bug"
    ],
    "title": "bug in matrix_real_double_dense  (trivial to fix)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2354",
    "user": "was"
}
```
Assignee: was


```
        _n.flags = _n.flags|(NPY_OWNDATA) # this sets the ownership bug
```


but should be

```
        _n.flags = _n.flags|(NPY_OWNDATA) # this sets the ownership bit
```




Issue created by migration from https://trac.sagemath.org/ticket/2354





---

archive/issue_comments_015828.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-03-03T17:57:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2354",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2354#issuecomment-15828",
    "user": "dfdeshom"
}
```

Attachment



---

archive/issue_comments_015829.json:
```json
{
    "body": "Changing priority from major to trivial.",
    "created_at": "2008-03-03T17:57:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2354",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2354#issuecomment-15829",
    "user": "dfdeshom"
}
```

Changing priority from major to trivial.



---

archive/issue_comments_015830.json:
```json
{
    "body": "Changing assignee from was to dfdeshom.",
    "created_at": "2008-03-03T17:57:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2354",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2354#issuecomment-15830",
    "user": "dfdeshom"
}
```

Changing assignee from was to dfdeshom.



---

archive/issue_comments_015831.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-03-03T17:57:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2354",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2354#issuecomment-15831",
    "user": "dfdeshom"
}
```

Changing status from new to assigned.



---

archive/issue_comments_015832.json:
```json
{
    "body": "Looks good.",
    "created_at": "2008-03-11T01:10:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2354",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2354#issuecomment-15832",
    "user": "AlexGhitza"
}
```

Looks good.



---

archive/issue_comments_015833.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-12T22:09:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2354",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2354#issuecomment-15833",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_015834.json:
```json
{
    "body": "Merged in Sage 2.10.4.alpha0",
    "created_at": "2008-03-12T22:09:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2354",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2354#issuecomment-15834",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.4.alpha0
