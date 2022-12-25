# Issue 1897: %latex -- bug in passing in predefined sage variables (serious but probably very easy to fix)

archive/issues_001897.json:
```json
{
    "body": "Assignee: boothby\n\n```\n12:46 < ianxek> hi there\n12:47 < ianxek> A Latex question in sage : if I define a variable say x=3 and later on use the\n                %latex environment and use $\\sage{x}$ then it says x is unknown\n12:48 < ianxek> How do I tell sage to access the previously defined x ?\n13:03 < sage> This is a bug in Sage!\n13:03 < sage> However, here is a workaround until it gets fixed.\n13:03 < sage> ianxek.\n13:03 < sage> latex.eval('$2+\\sage{a}$', locals=globals())\n13:03 < sage> I.e., instead of typing %latex in the cell, do \n13:04 < sage> latex.eval(\"A latex string\", locals=globals())\n13:04 < sage> And you'll see the variables properly.\n13:04 < sage> Thanks for asking this question.\n```\n\nI think the problem involves system.eval not getting passed the\nglobals() dictionary correctly...\n\nIssue created by migration from https://trac.sagemath.org/ticket/1897\n\n",
    "created_at": "2008-01-23T21:05:16Z",
    "labels": [
        "component: notebook",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "%latex -- bug in passing in predefined sage variables (serious but probably very easy to fix)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1897",
    "user": "https://github.com/williamstein"
}
```
Assignee: boothby

```
12:46 < ianxek> hi there
12:47 < ianxek> A Latex question in sage : if I define a variable say x=3 and later on use the
                %latex environment and use $\sage{x}$ then it says x is unknown
12:48 < ianxek> How do I tell sage to access the previously defined x ?
13:03 < sage> This is a bug in Sage!
13:03 < sage> However, here is a workaround until it gets fixed.
13:03 < sage> ianxek.
13:03 < sage> latex.eval('$2+\sage{a}$', locals=globals())
13:03 < sage> I.e., instead of typing %latex in the cell, do 
13:04 < sage> latex.eval("A latex string", locals=globals())
13:04 < sage> And you'll see the variables properly.
13:04 < sage> Thanks for asking this question.
```

I think the problem involves system.eval not getting passed the
globals() dictionary correctly...

Issue created by migration from https://trac.sagemath.org/ticket/1897





---

archive/issue_comments_011976.json:
```json
{
    "body": "Changing assignee from boothby to @mwhansen.",
    "created_at": "2009-01-19T13:50:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1897",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1897#issuecomment-11976",
    "user": "https://github.com/mwhansen"
}
```

Changing assignee from boothby to @mwhansen.



---

archive/issue_comments_011977.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-01-19T13:50:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1897",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1897#issuecomment-11977",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_011978.json:
```json
{
    "body": "Attachment [trac_1897.patch](tarball://root/attachments/some-uuid/ticket1897/trac_1897.patch) by @mwhansen created at 2009-01-19 13:50:11\n\nThe problem was caused by syseval in sage.server.support needing the second positional argument to be an argument for global variables.",
    "created_at": "2009-01-19T13:50:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1897",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1897#issuecomment-11978",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac_1897.patch](tarball://root/attachments/some-uuid/ticket1897/trac_1897.patch) by @mwhansen created at 2009-01-19 13:50:11

The problem was caused by syseval in sage.server.support needing the second positional argument to be an argument for global variables.



---

archive/issue_comments_011979.json:
```json
{
    "body": "With %latex in notebook I'm getting \n\n```\nAn error occured.\nError latexing slide.\n```",
    "created_at": "2009-01-21T07:00:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1897",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1897#issuecomment-11979",
    "user": "https://trac.sagemath.org/admin/accounts/users/TimothyClemans"
}
```

With %latex in notebook I'm getting 

```
An error occured.
Error latexing slide.
```



---

archive/issue_comments_011980.json:
```json
{
    "body": "This fixes the problem for me.  TimothyClemans, you need a bunch of things for this to work, like dvipng, etc.  Can you latex any slides at all?",
    "created_at": "2009-01-22T14:44:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1897",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1897#issuecomment-11980",
    "user": "https://github.com/jasongrout"
}
```

This fixes the problem for me.  TimothyClemans, you need a bunch of things for this to work, like dvipng, etc.  Can you latex any slides at all?



---

archive/issue_events_004576.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-01-23T09:39:30Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1897",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1897#event-4576"
}
```



---

archive/issue_comments_011981.json:
```json
{
    "body": "Merged in Sage 3.3.alpha1\n\nCheers,\n\nMichael",
    "created_at": "2009-01-23T09:39:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1897",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1897#issuecomment-11981",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.3.alpha1

Cheers,

Michael



---

archive/issue_comments_011982.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-23T09:39:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1897",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1897#issuecomment-11982",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_004577.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-01-23T10:54:28Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1897",
    "milestone": "sage-3.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1897#event-4577"
}
```
