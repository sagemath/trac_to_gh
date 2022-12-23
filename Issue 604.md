# Issue 604: Number field element memory leak

archive/issues_000604.json:
```json
{
    "body": "Assignee: was\n\nThe NTL structures in the number field are leaking.\n\nThe attached patch fixes this and some other matters with multiplication and division -- actually making them use NTL.\n\nIssue created by migration from https://trac.sagemath.org/ticket/604\n\n",
    "created_at": "2007-09-06T21:44:29Z",
    "labels": [
        "number theory",
        "major",
        "bug"
    ],
    "title": "Number field element memory leak",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/604",
    "user": "jbmohler"
}
```
Assignee: was

The NTL structures in the number field are leaking.

The attached patch fixes this and some other matters with multiplication and division -- actually making them use NTL.

Issue created by migration from https://trac.sagemath.org/ticket/604





---

archive/issue_comments_003110.json:
```json
{
    "body": "Attachment",
    "created_at": "2007-09-06T21:45:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/604",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/604#issuecomment-3110",
    "user": "jbmohler"
}
```

Attachment



---

archive/issue_comments_003111.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-09-07T04:43:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/604",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/604#issuecomment-3111",
    "user": "was"
}
```

Resolution: fixed
