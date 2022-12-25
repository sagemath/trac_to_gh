# Issue 1671: doctest: fix shapes.pyx fallout from #1666

archive/issues_001671.json:
```json
{
    "body": "Assignee: mabshoff\n\nDue to Robert's work (#1666) I get a bunch of doctest failures like the following:\n\n```\nsage -t  devel/sage-main/sage/groups/perm_gps/cubegroup.py  \n**********************************************************************\nFile \"cubegroup.py\", line 901:\n    sage: C.show3d()\nExpected nothing\nGot:\n    0.00166666666667\n    0.00166666666667\n    0.00166666666667\n    0.00166666666667\n    0.00166666666667\n    0.00166666666667\n    0.00166666666667\n    0.00166666666667\n    0.00166666666667\n    0.00166666666667\n    0.00166666666667\n    0.00166666666667\n**********************************************************************\n```\n\nI tracked this down to a print statement in `shapes.pyx`. I uncommented that line which fixes this issue.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/1671\n\n",
    "created_at": "2008-01-03T17:26:58Z",
    "labels": [
        "component: doctest coverage",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.9.2",
    "title": "doctest: fix shapes.pyx fallout from #1666",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1671",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

Due to Robert's work (#1666) I get a bunch of doctest failures like the following:

```
sage -t  devel/sage-main/sage/groups/perm_gps/cubegroup.py  
**********************************************************************
File "cubegroup.py", line 901:
    sage: C.show3d()
Expected nothing
Got:
    0.00166666666667
    0.00166666666667
    0.00166666666667
    0.00166666666667
    0.00166666666667
    0.00166666666667
    0.00166666666667
    0.00166666666667
    0.00166666666667
    0.00166666666667
    0.00166666666667
    0.00166666666667
**********************************************************************
```

I tracked this down to a print statement in `shapes.pyx`. I uncommented that line which fixes this issue.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/1671





---

archive/issue_comments_010583.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-03T17:27:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1671",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1671#issuecomment-10583",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_001830.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-01-03T17:27:58Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1671",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1671#event-1830"
}
```



---

archive/issue_comments_010584.json:
```json
{
    "body": "Attachment [Sage-2.9.2-remove-debug-output.patch](tarball://root/attachments/some-uuid/ticket1671/Sage-2.9.2-remove-debug-output.patch) by mabshoff created at 2008-01-03 17:27:58\n\nApplied to 2.9.2.alpha0.",
    "created_at": "2008-01-03T17:27:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1671",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1671#issuecomment-10584",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [Sage-2.9.2-remove-debug-output.patch](tarball://root/attachments/some-uuid/ticket1671/Sage-2.9.2-remove-debug-output.patch) by mabshoff created at 2008-01-03 17:27:58

Applied to 2.9.2.alpha0.
