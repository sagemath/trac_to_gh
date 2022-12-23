# Issue 1968: notebook -- remove capability of using live tutorial for users not signed in to the notebook server

archive/issues_001968.json:
```json
{
    "body": "Assignee: boothby\n\nTimothy Clemans points out to me in chat a *major* security issue with the notebook.  If a user visits the live tutorial, e.g., \n\n    https://your_computer:port/doc/live/tut/node5.html\n\nthen they can execute code even if they aren't logged in!\n\nThis is a major security hole if somebody is running their own notebook server.\n\nSolution: by changing about 2 lines in server/notebook/twist.py, one can change it\nso the entire live tutorial is inaccessible accept to users that are logged in.  This should be done. \n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1968\n\n",
    "created_at": "2008-01-29T10:20:17Z",
    "labels": [
        "notebook",
        "blocker",
        "bug"
    ],
    "title": "notebook -- remove capability of using live tutorial for users not signed in to the notebook server",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1968",
    "user": "was"
}
```
Assignee: boothby

Timothy Clemans points out to me in chat a *major* security issue with the notebook.  If a user visits the live tutorial, e.g., 

    https://your_computer:port/doc/live/tut/node5.html

then they can execute code even if they aren't logged in!

This is a major security hole if somebody is running their own notebook server.

Solution: by changing about 2 lines in server/notebook/twist.py, one can change it
so the entire live tutorial is inaccessible accept to users that are logged in.  This should be done. 



Issue created by migration from https://trac.sagemath.org/ticket/1968





---

archive/issue_comments_012741.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-01-29T11:32:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1968",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1968#issuecomment-12741",
    "user": "was"
}
```

Attachment



---

archive/issue_comments_012742.json:
```json
{
    "body": "This seems to work.\nDirectly visiting the tutorial as above works when logged in but not when logged out\n(you get a not found error in the browser).\n\n\nwas: can you clarify that this is the intended effect.",
    "created_at": "2008-02-01T04:56:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1968",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1968#issuecomment-12742",
    "user": "jkantor"
}
```

This seems to work.
Directly visiting the tutorial as above works when logged in but not when logged out
(you get a not found error in the browser).


was: can you clarify that this is the intended effect.



---

archive/issue_comments_012743.json:
```json
{
    "body": "> was: can you clarify that this is the intended effect.\n\nYes, that is exactly the intended effect.  Excellent.",
    "created_at": "2008-02-01T05:12:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1968",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1968#issuecomment-12743",
    "user": "was"
}
```

> was: can you clarify that this is the intended effect.

Yes, that is exactly the intended effect.  Excellent.



---

archive/issue_comments_012744.json:
```json
{
    "body": "Ok, then the review is positive.\n\nCheers,\n\nMichael",
    "created_at": "2008-02-01T05:15:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1968",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1968#issuecomment-12744",
    "user": "mabshoff"
}
```

Ok, then the review is positive.

Cheers,

Michael



---

archive/issue_comments_012745.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-01T05:17:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1968",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1968#issuecomment-12745",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_012746.json:
```json
{
    "body": "Merged in Sage 2.10.1.rc4",
    "created_at": "2008-02-01T05:17:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1968",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1968#issuecomment-12746",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.1.rc4
