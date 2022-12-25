# Issue 3033: equations.py segfaults without --incref-local-binop cython flag

archive/issues_003033.json:
```json
{
    "body": "Assignee: @williamstein\n\nIf sage is compiled without the --incref-local-binop for Cython, calculus/equations.py segfaults.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3033\n\n",
    "closed_at": "2008-04-26T22:24:23Z",
    "created_at": "2008-04-26T22:15:19Z",
    "labels": [
        "component: calculus",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "equations.py segfaults without --incref-local-binop cython flag",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3033",
    "user": "https://github.com/garyfurnish"
}
```
Assignee: @williamstein

If sage is compiled without the --incref-local-binop for Cython, calculus/equations.py segfaults.

Issue created by migration from https://trac.sagemath.org/ticket/3033





---

archive/issue_comments_020834.json:
```json
{
    "body": "This uses a) Pbuild B) Upstream, patched, Cython.  Furthermore it is a heisenbug (although one that happens most of the time)",
    "created_at": "2008-04-26T22:21:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3033",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3033#issuecomment-20834",
    "user": "https://github.com/garyfurnish"
}
```

This uses a) Pbuild B) Upstream, patched, Cython.  Furthermore it is a heisenbug (although one that happens most of the time)



---

archive/issue_comments_020835.json:
```json
{
    "body": "No dice. Invalid for now since:\n\n```\n[23:37] <mabshoff> I am not sure if #3033 is valid.\n[23:37] <mabshoff> At least not in its current form.\n[23:37] <gfurnish> Yeah lets invalid that\n[23:37] <mabshoff> Wait.\n[23:37] <mabshoff> You need to add the fact that \n[23:37] <mabshoff> a) you use pbuild\n[23:37] <mabshoff> b) you use an *upstream* *patched* Cython\n[23:37] <mabshoff> So it isn't something that we can debug\n[23:38] <mabshoff> It might still be valid, so let's keep it open.\n[23:38] <mabshoff> I.e. once the updated cython is in-tree is in it might  come up again.\n[23:38] <mabshoff> But then we use --incref-local-binop per default anyway?\n[23:39] <gfurnish> yeah..\n[23:39] <mabshoff> So, in the end?\n[23:39] <mabshoff> Let's go with invalid for now. I am closing it with this conversation pasted in the comment.\n[23:39] <mabshoff> Alright?\n[23:40] <mabshoff> And you never know what happens if you do a complete rebuild of Sage.\n[23:40] <mabshoff> That tends to cause fixes for Heisenbugs.\n[23:40] <gfurnish> ok\n[23:40] <gfurnish> this is with multiple full rebuilds\n[23:40] <mabshoff> ok\n[23:41] <mabshoff> Well, if we hit it again we can reopen.\n```\n\nCheers,\n\nMichael",
    "created_at": "2008-04-26T22:24:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3033",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3033#issuecomment-20835",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

No dice. Invalid for now since:

```
[23:37] <mabshoff> I am not sure if #3033 is valid.
[23:37] <mabshoff> At least not in its current form.
[23:37] <gfurnish> Yeah lets invalid that
[23:37] <mabshoff> Wait.
[23:37] <mabshoff> You need to add the fact that 
[23:37] <mabshoff> a) you use pbuild
[23:37] <mabshoff> b) you use an *upstream* *patched* Cython
[23:37] <mabshoff> So it isn't something that we can debug
[23:38] <mabshoff> It might still be valid, so let's keep it open.
[23:38] <mabshoff> I.e. once the updated cython is in-tree is in it might  come up again.
[23:38] <mabshoff> But then we use --incref-local-binop per default anyway?
[23:39] <gfurnish> yeah..
[23:39] <mabshoff> So, in the end?
[23:39] <mabshoff> Let's go with invalid for now. I am closing it with this conversation pasted in the comment.
[23:39] <mabshoff> Alright?
[23:40] <mabshoff> And you never know what happens if you do a complete rebuild of Sage.
[23:40] <mabshoff> That tends to cause fixes for Heisenbugs.
[23:40] <gfurnish> ok
[23:40] <gfurnish> this is with multiple full rebuilds
[23:40] <mabshoff> ok
[23:41] <mabshoff> Well, if we hit it again we can reopen.
```

Cheers,

Michael



---

archive/issue_comments_020836.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2008-04-26T22:24:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3033",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3033#issuecomment-20836",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: invalid



---

archive/issue_events_006882.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-04-26T22:24:23Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3033",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3033#event-6882"
}
```
