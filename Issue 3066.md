# Issue 3066: empty matrices: gram_schmidt() throws a NameError

archive/issues_003066.json:
```json
{
    "body": "Assignee: was\n\nLooks like an explicit import is the only thing missing on this one:\n\n\n```\nsage: a = matrix([])\nsage: m.gram_schmidt()\n<type 'exceptions.NameError'>: global name 'ZZ' is not defined\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3066\n\n",
    "created_at": "2008-04-30T15:20:39Z",
    "labels": [
        "linear algebra",
        "major",
        "bug"
    ],
    "title": "empty matrices: gram_schmidt() throws a NameError",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3066",
    "user": "dfdeshom"
}
```
Assignee: was

Looks like an explicit import is the only thing missing on this one:


```
sage: a = matrix([])
sage: m.gram_schmidt()
<type 'exceptions.NameError'>: global name 'ZZ' is not defined
```


Issue created by migration from https://trac.sagemath.org/ticket/3066





---

archive/issue_comments_021164.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-04-30T17:35:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3066",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3066#issuecomment-21164",
    "user": "dfdeshom"
}
```

Attachment



---

archive/issue_comments_021165.json:
```json
{
    "body": "Patch attached.",
    "created_at": "2008-04-30T17:35:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3066",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3066#issuecomment-21165",
    "user": "dfdeshom"
}
```

Patch attached.



---

archive/issue_comments_021166.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-05-01T05:47:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3066",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3066#issuecomment-21166",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_021167.json:
```json
{
    "body": "Merged in Sage 3.0.1.alpha1",
    "created_at": "2008-05-01T05:47:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3066",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3066#issuecomment-21167",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.1.alpha1
