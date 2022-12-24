# Issue 4568: Dangerous doc test of save_session

archive/issues_004568.json:
```json
{
    "body": "Assignee: mabshoff\n\nThe doc test of `save_session` does the following:\n\n```\n        EXAMPLES:\n            sage: a = 5\n            sage: save_session('session')\n        \n        ...\n        Clean up the session file we just wrote to disk.\n            sage: os.unlink('session.sobj')\n```\n\n\nHence, if the user happens to have a file `session.sobj` in the current directory then running the doc test would destroy it.\n\nAccording to a suggestion of Robert Bradshow, using the `tempfile` Python module might help.\n\nUnfortunately I have no idea in what file `save_session` is defined - so, no patch at that point...\n\nIssue created by migration from https://trac.sagemath.org/ticket/4568\n\n",
    "created_at": "2008-11-20T20:21:21Z",
    "labels": [
        "doctest coverage",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.1",
    "title": "Dangerous doc test of save_session",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4568",
    "user": "SimonKing"
}
```
Assignee: mabshoff

The doc test of `save_session` does the following:

```
        EXAMPLES:
            sage: a = 5
            sage: save_session('session')
        
        ...
        Clean up the session file we just wrote to disk.
            sage: os.unlink('session.sobj')
```


Hence, if the user happens to have a file `session.sobj` in the current directory then running the doc test would destroy it.

According to a suggestion of Robert Bradshow, using the `tempfile` Python module might help.

Unfortunately I have no idea in what file `save_session` is defined - so, no patch at that point...

Issue created by migration from https://trac.sagemath.org/ticket/4568





---

archive/issue_comments_034221.json:
```json
{
    "body": "Meanwhile I found out that `save_session` is in `sage/misc/session.pyx`. Hence, I produced a patch that modifies three doc tests that had the above dangerous behaviour.",
    "created_at": "2008-11-21T11:14:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4568",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4568#issuecomment-34221",
    "user": "SimonKing"
}
```

Meanwhile I found out that `save_session` is in `sage/misc/session.pyx`. Hence, I produced a patch that modifies three doc tests that had the above dangerous behaviour.



---

archive/issue_comments_034222.json:
```json
{
    "body": "Changing keywords from \"\" to \"save_session temporary file\".",
    "created_at": "2008-11-21T11:14:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4568",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4568#issuecomment-34222",
    "user": "SimonKing"
}
```

Changing keywords from "" to "save_session temporary file".



---

archive/issue_comments_034223.json:
```json
{
    "body": "Simon,\n\nmake sure to assign a milestone when you open a ticket.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-21T11:16:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4568",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4568#issuecomment-34223",
    "user": "mabshoff"
}
```

Simon,

make sure to assign a milestone when you open a ticket.

Cheers,

Michael



---

archive/issue_comments_034224.json:
```json
{
    "body": "Hi Simon,\n\nMy concern with the current wording is that it's not entirely clear that the user should NOT save the session to a file in SAGE_TMP.  We only do that for doctesting purposes.\n\n--Mike",
    "created_at": "2008-11-21T17:20:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4568",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4568#issuecomment-34224",
    "user": "mhansen"
}
```

Hi Simon,

My concern with the current wording is that it's not entirely clear that the user should NOT save the session to a file in SAGE_TMP.  We only do that for doctesting purposes.

--Mike



---

archive/issue_comments_034225.json:
```json
{
    "body": "Fixing dangerous doc test behaviour in session.pyx (2nd version)",
    "created_at": "2008-11-22T11:13:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4568",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4568#issuecomment-34225",
    "user": "SimonKing"
}
```

Fixing dangerous doc test behaviour in session.pyx (2nd version)



---

archive/issue_comments_034226.json:
```json
{
    "body": "Attachment [save_session.patch](tarball://root/attachments/some-uuid/ticket4568/save_session.patch) by SimonKing created at 2008-11-22 11:15:41\n\nReplying to [comment:3 mhansen]:\n> My concern with the current wording is that it's not entirely clear that the user should NOT save the session to a file in SAGE_TMP.  We only do that for doctesting purposes.\n\nHi Mike, \n\nGood point! I changed my patch accordingly - in the new patch I clearly say that for permanent saving SAGE_TMP would be a bad idea.\n\nCheers\n    Simon",
    "created_at": "2008-11-22T11:15:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4568",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4568#issuecomment-34226",
    "user": "SimonKing"
}
```

Attachment [save_session.patch](tarball://root/attachments/some-uuid/ticket4568/save_session.patch) by SimonKing created at 2008-11-22 11:15:41

Replying to [comment:3 mhansen]:
> My concern with the current wording is that it's not entirely clear that the user should NOT save the session to a file in SAGE_TMP.  We only do that for doctesting purposes.

Hi Mike, 

Good point! I changed my patch accordingly - in the new patch I clearly say that for permanent saving SAGE_TMP would be a bad idea.

Cheers
    Simon



---

archive/issue_comments_034227.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-11-28T20:51:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4568",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4568#issuecomment-34227",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_034228.json:
```json
{
    "body": "Merged in Sage 3.2.1.rc0",
    "created_at": "2008-11-28T20:51:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4568",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4568#issuecomment-34228",
    "user": "mabshoff"
}
```

Merged in Sage 3.2.1.rc0
