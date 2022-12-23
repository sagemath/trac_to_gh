# Issue 3427: [with patch; needs review] remove ntl library from sage_object build dependency in setup.py

archive/issues_003427.json:
```json
{
    "body": "Assignee: mabshoff\n\nI can think of no good reason that the ntl library is linked into sage_object.pyx!  It absolutely shouldn't be needed.   Not having it there is needed for making sagelite. \n\nIssue created by migration from https://trac.sagemath.org/ticket/3427\n\n",
    "created_at": "2008-06-14T22:15:34Z",
    "labels": [
        "build",
        "major",
        "bug"
    ],
    "title": "[with patch; needs review] remove ntl library from sage_object build dependency in setup.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3427",
    "user": "was"
}
```
Assignee: mabshoff

I can think of no good reason that the ntl library is linked into sage_object.pyx!  It absolutely shouldn't be needed.   Not having it there is needed for making sagelite. 

Issue created by migration from https://trac.sagemath.org/ticket/3427





---

archive/issue_comments_024149.json:
```json
{
    "body": "Attachment\n\nPositive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-06-15T19:05:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3427",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3427#issuecomment-24149",
    "user": "mabshoff"
}
```

Attachment

Positive review.

Cheers,

Michael



---

archive/issue_comments_024150.json:
```json
{
    "body": "Merged in Sage 3.0.3.rc0",
    "created_at": "2008-06-15T19:15:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3427",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3427#issuecomment-24150",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.3.rc0



---

archive/issue_comments_024151.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-06-15T19:15:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3427",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3427#issuecomment-24151",
    "user": "mabshoff"
}
```

Resolution: fixed
