# Issue 5121: major bug in plot command

archive/issues_005121.json:
```json
{
    "body": "Assignee: @williamstein\n\n\n```\nsage: E = EllipticCurve('37a')\nsage: plot(E)\nsage: plot(E, xmin=25,xmax=25)\nTraceback (most recent call last):\n...\nAttributeError: 'SymbolicEquation' object has no attribute '_fast_float_'\n```\n\n\nThis broke David Hansen's thesis.  It also caused me a lot of embarasement during my talk at Sage Days 12!!!\n\nIt is a new bug introduced by some plot refactoring recently. \n\nIssue created by migration from https://trac.sagemath.org/ticket/5121\n\n",
    "created_at": "2009-01-28T20:07:18Z",
    "labels": [
        "component: graphics",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "major bug in plot command",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5121",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein


```
sage: E = EllipticCurve('37a')
sage: plot(E)
sage: plot(E, xmin=25,xmax=25)
Traceback (most recent call last):
...
AttributeError: 'SymbolicEquation' object has no attribute '_fast_float_'
```


This broke David Hansen's thesis.  It also caused me a lot of embarasement during my talk at Sage Days 12!!!

It is a new bug introduced by some plot refactoring recently. 

Issue created by migration from https://trac.sagemath.org/ticket/5121





---

archive/issue_comments_039078.json:
```json
{
    "body": "Apparently a block of code was not indented correctly.  I'll post up a patch momentarily.",
    "created_at": "2009-01-28T21:19:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5121",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5121#issuecomment-39078",
    "user": "https://github.com/jasongrout"
}
```

Apparently a block of code was not indented correctly.  I'll post up a patch momentarily.



---

archive/issue_comments_039079.json:
```json
{
    "body": "This broke in the commit http://www.sagemath.org/hg/sage-main/diff/ed11b267ec9f/sage/plot/plot.py",
    "created_at": "2009-01-28T21:56:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5121",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5121#issuecomment-39079",
    "user": "https://github.com/jasongrout"
}
```

This broke in the commit http://www.sagemath.org/hg/sage-main/diff/ed11b267ec9f/sage/plot/plot.py



---

archive/issue_comments_039080.json:
```json
{
    "body": "Attachment [trac_5121.patch](tarball://root/attachments/some-uuid/ticket5121/trac_5121.patch) by @williamstein created at 2009-01-28 23:14:17",
    "created_at": "2009-01-28T23:14:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5121",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5121#issuecomment-39080",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac_5121.patch](tarball://root/attachments/some-uuid/ticket5121/trac_5121.patch) by @williamstein created at 2009-01-28 23:14:17



---

archive/issue_events_011847.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-01-29T00:27:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5121",
    "milestone": "sage-3.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5121#event-11847"
}
```



---

archive/issue_comments_039081.json:
```json
{
    "body": "Merged in Sage 3.3.alpha3.\n\nCheers,\n\nMichael",
    "created_at": "2009-01-29T00:27:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5121",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5121#issuecomment-39081",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.3.alpha3.

Cheers,

Michael



---

archive/issue_comments_039082.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-29T00:27:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5121",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5121#issuecomment-39082",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_011848.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-01-29T00:27:53Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5121",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5121#event-11848"
}
```
