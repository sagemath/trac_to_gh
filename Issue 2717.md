# Issue 2717: maxima expect interface synchronization not sufficiently robust

archive/issues_002717.json:
```json
{
    "body": "Assignee: @williamstein\n\nIt is still possible to very occassionaly throw off the Maxima synchronization, maybe during parallel doctesting (?).  E.g.,\n\n```\nsage -t  devel/sage-main/sage/calculus/functional.py        **********************************************************************\nFile \"functional.py\", line 301:\n    sage: limit((tan(sin(x)) - sin(tan(x)))/x^7, taylor=True, x=0)\nExpected:\n    1/30\nGot:\n    1820214126\n**********************************************************************\n1 items had failures:\n   1 of   7 in __main__.example_4\n***Test Failed*** 1 failures.\nFor whitespace errors\n```\n\nThe above is particularly bad since you can't tell something went wrong -- you just\nget a wrong number out.  The point of this ticket isn't to fix the whole problem.\nInstead, change the synchronization marker in maxima.py from being a single number\nto a string such as \n\n    __SAGE_SYNCHRO_MARKER_1820214126\n\nso that instead of people being confused by a wrong answer, it will be\ncrystal clear that something went wrong. \n\nThis will likely be nearly trivial to implement. \n\nIssue created by migration from https://trac.sagemath.org/ticket/2717\n\n",
    "created_at": "2008-03-29T16:27:36Z",
    "labels": [
        "component: interfaces",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.11",
    "title": "maxima expect interface synchronization not sufficiently robust",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2717",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

It is still possible to very occassionaly throw off the Maxima synchronization, maybe during parallel doctesting (?).  E.g.,

```
sage -t  devel/sage-main/sage/calculus/functional.py        **********************************************************************
File "functional.py", line 301:
    sage: limit((tan(sin(x)) - sin(tan(x)))/x^7, taylor=True, x=0)
Expected:
    1/30
Got:
    1820214126
**********************************************************************
1 items had failures:
   1 of   7 in __main__.example_4
***Test Failed*** 1 failures.
For whitespace errors
```

The above is particularly bad since you can't tell something went wrong -- you just
get a wrong number out.  The point of this ticket isn't to fix the whole problem.
Instead, change the synchronization marker in maxima.py from being a single number
to a string such as 

    __SAGE_SYNCHRO_MARKER_1820214126

so that instead of people being confused by a wrong answer, it will be
crystal clear that something went wrong. 

This will likely be nearly trivial to implement. 

Issue created by migration from https://trac.sagemath.org/ticket/2717





---

archive/issue_comments_018696.json:
```json
{
    "body": "Attachment [trac2717-maxima-sync-fail-safer.patch](tarball://root/attachments/some-uuid/ticket2717/trac2717-maxima-sync-fail-safer.patch) by cwitty created at 2008-03-29 19:19:23",
    "created_at": "2008-03-29T19:19:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2717",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2717#issuecomment-18696",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Attachment [trac2717-maxima-sync-fail-safer.patch](tarball://root/attachments/some-uuid/ticket2717/trac2717-maxima-sync-fail-safer.patch) by cwitty created at 2008-03-29 19:19:23



---

archive/issue_comments_018697.json:
```json
{
    "body": "Looks good to me. Second review appreciated.\n\nCheers,\n\nMichael",
    "created_at": "2008-03-29T19:28:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2717",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2717#issuecomment-18697",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Looks good to me. Second review appreciated.

Cheers,

Michael



---

archive/issue_comments_018698.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2008-03-29T20:38:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2717",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2717#issuecomment-18698",
    "user": "https://github.com/mwhansen"
}
```

Looks good to me.



---

archive/issue_comments_018699.json:
```json
{
    "body": "Merged in Sage 2.11.rc0",
    "created_at": "2008-03-29T20:50:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2717",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2717#issuecomment-18699",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.11.rc0



---

archive/issue_events_006342.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-03-29T20:50:57Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2717",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2717#event-6342"
}
```



---

archive/issue_comments_018700.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-29T20:50:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2717",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2717#issuecomment-18700",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
