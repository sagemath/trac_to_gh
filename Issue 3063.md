# Issue 3063: empty matrices: norm() returns a ValueError

archive/issues_003063.json:
```json
{
    "body": "Assignee: was\n\n\n```\nsage: a = matrix([])\n\nsage: a.norm()\n---------------------------------------------------------------------------\n\n<type 'exceptions.ValueError'>: max() arg is an empty sequence\n```\n\n\nI think the answer in this case should be 0.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3063\n\n",
    "created_at": "2008-04-30T15:10:44Z",
    "labels": [
        "linear algebra",
        "major",
        "bug"
    ],
    "title": "empty matrices: norm() returns a ValueError",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3063",
    "user": "dfdeshom"
}
```
Assignee: was


```
sage: a = matrix([])

sage: a.norm()
---------------------------------------------------------------------------

<type 'exceptions.ValueError'>: max() arg is an empty sequence
```


I think the answer in this case should be 0.

Issue created by migration from https://trac.sagemath.org/ticket/3063





---

archive/issue_comments_021148.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-04-30T17:54:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3063",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3063#issuecomment-21148",
    "user": "dfdeshom"
}
```

Attachment



---

archive/issue_comments_021149.json:
```json
{
    "body": "Patch attached.",
    "created_at": "2008-04-30T17:54:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3063",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3063#issuecomment-21149",
    "user": "dfdeshom"
}
```

Patch attached.



---

archive/issue_comments_021150.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-05-01T05:46:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3063",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3063#issuecomment-21150",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_021151.json:
```json
{
    "body": "Merged in Sage 3.0.1.alpha1",
    "created_at": "2008-05-01T05:46:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3063",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3063#issuecomment-21151",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.1.alpha1
