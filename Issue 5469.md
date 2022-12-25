# Issue 5469: sage -clone ...  should copy the sage/doc/output directory

archive/issues_005469.json:
```json
{
    "body": "Assignee: tba\n\nRunning \"sage -clone blah\" should copy $SAGE_ROOT/devel/sage/doc/output/...: for one thing, if you clone the repository, you should still have access to all of the local Sage documentation (via the \"Help\" button in the notebook), and for another, if you want to modify library code, you shouldn't have to wait 20 minutes to see how your changes affect the reference manual.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5469\n\n",
    "created_at": "2009-03-10T19:00:18Z",
    "labels": [
        "component: documentation",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4",
    "title": "sage -clone ...  should copy the sage/doc/output directory",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5469",
    "user": "https://github.com/jhpalmieri"
}
```
Assignee: tba

Running "sage -clone blah" should copy $SAGE_ROOT/devel/sage/doc/output/...: for one thing, if you clone the repository, you should still have access to all of the local Sage documentation (via the "Help" button in the notebook), and for another, if you want to modify library code, you shouldn't have to wait 20 minutes to see how your changes affect the reference manual.


Issue created by migration from https://trac.sagemath.org/ticket/5469





---

archive/issue_comments_042364.json:
```json
{
    "body": "Just a note, it would be nice if the files could be hard linked rather than actually copied.",
    "created_at": "2009-03-11T01:09:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5469",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5469#issuecomment-42364",
    "user": "https://github.com/robertwb"
}
```

Just a note, it would be nice if the files could be hard linked rather than actually copied.



---

archive/issue_events_005723.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2009-03-11T06:27:26Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5469",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5469#event-5723"
}
```



---

archive/issue_comments_042365.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-03-11T06:27:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5469",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5469#issuecomment-42365",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_042366.json:
```json
{
    "body": "Fixed via #5414.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-11T06:27:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5469",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5469#issuecomment-42366",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Fixed via #5414.

Cheers,

Michael
