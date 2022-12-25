# Issue 9800: Linear programming construction doc fixes

archive/issues_009800.json:
```json
{
    "body": "Assignee: @nathanncohen\n\nKeywords: linear programming, constructions, doc\n\nThe linear programming page in the Sage Constructions document has a few errors. \n\n1.  In the vertex cover example, the objective should be to minimize, not maximize the sum.  Also, the example code is missing the objective function.\n\n2.  The maximal matching example code is also missing the objective function.\n\n3.  I couldn't run the examples even after having installed glpk according to the instructions.  Sage complained that no solver was installed.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9801\n\n",
    "created_at": "2010-08-25T13:48:21Z",
    "labels": [
        "component: documentation",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Linear programming construction doc fixes",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9800",
    "user": "https://github.com/rhinton"
}
```
Assignee: @nathanncohen

Keywords: linear programming, constructions, doc

The linear programming page in the Sage Constructions document has a few errors. 

1.  In the vertex cover example, the objective should be to minimize, not maximize the sum.  Also, the example code is missing the objective function.

2.  The maximal matching example code is also missing the objective function.

3.  I couldn't run the examples even after having installed glpk according to the instructions.  Sage complained that no solver was installed.


Issue created by migration from https://trac.sagemath.org/ticket/9801





---

archive/issue_comments_096133.json:
```json
{
    "body": "Attachment [trac-9801-linear-programming-constructions-doc.patch](tarball://root/attachments/some-uuid/ticket9801/trac-9801-linear-programming-constructions-doc.patch) by @rhinton created at 2010-08-25 14:01:24",
    "created_at": "2010-08-25T14:01:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9800#issuecomment-96133",
    "user": "https://github.com/rhinton"
}
```

Attachment [trac-9801-linear-programming-constructions-doc.patch](tarball://root/attachments/some-uuid/ticket9801/trac-9801-linear-programming-constructions-doc.patch) by @rhinton created at 2010-08-25 14:01:24



---

archive/issue_comments_096134.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2010-08-25T14:03:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9800#issuecomment-96134",
    "user": "https://github.com/rhinton"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_096135.json:
```json
{
    "body": "Attached patch apparently fixes problem (1).  \n\nIt attempts to fix problem (2), but I get an exception\n\n```\nMIPSolverException: 'GLPK : Solution is undefined'\n```\n\nRegarding (3), glpk apparently installed just fine on another machine, so I will bring up the problem on sage-devel to get help on the failed install.",
    "created_at": "2010-08-25T14:03:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9800#issuecomment-96135",
    "user": "https://github.com/rhinton"
}
```

Attached patch apparently fixes problem (1).  

It attempts to fix problem (2), but I get an exception

```
MIPSolverException: 'GLPK : Solution is undefined'
```

Regarding (3), glpk apparently installed just fine on another machine, so I will bring up the problem on sage-devel to get help on the failed install.



---

archive/issue_comments_096136.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2010-08-27T16:37:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9800#issuecomment-96136",
    "user": "https://github.com/rhinton"
}
```

Resolution: wontfix



---

archive/issue_events_024604.json:
```json
{
    "actor": "https://github.com/rhinton",
    "created_at": "2010-08-27T16:37:52Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9800",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9800#event-24604"
}
```



---

archive/issue_comments_096137.json:
```json
{
    "body": "Nathann Cohen promised a rewrite of this documentation soon.  See \n\nhttp://groups.google.com/group/sage-devel/browse_thread/thread/330baaf798e51a01\n\nfor details.",
    "created_at": "2010-08-27T16:37:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9800#issuecomment-96137",
    "user": "https://github.com/rhinton"
}
```

Nathann Cohen promised a rewrite of this documentation soon.  See 

http://groups.google.com/group/sage-devel/browse_thread/thread/330baaf798e51a01

for details.



---

archive/issue_events_024605.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2010-08-28T18:11:55Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9800",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9800#event-24605"
}
```
