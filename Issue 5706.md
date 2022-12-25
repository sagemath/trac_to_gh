# Issue 5706: implicit_plot totally sucks when input an equation

archive/issues_005706.json:
```json
{
    "body": "Assignee: @williamstein\n\nMake Sage hurt:\n\n```\nvar('x,y')\nimplicit_plot(x^2+y^2 == 1, (x,-2,2), (y,-2,2))\n```\n\n\nThe problem is that implicit_plot takes a function, not a symbolic equation, so it views \"x<sup>2+y</sup>2 == 1\" as a function --- and that is very painful.  \n\nSOLUTION: Check if the input is an equation, and if so, make RHS zero, and plot corresponding function equal to 0.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5706\n\n",
    "created_at": "2009-04-07T17:36:29Z",
    "labels": [
        "component: graphics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.1",
    "title": "implicit_plot totally sucks when input an equation",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5706",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

Make Sage hurt:

```
var('x,y')
implicit_plot(x^2+y^2 == 1, (x,-2,2), (y,-2,2))
```


The problem is that implicit_plot takes a function, not a symbolic equation, so it views "x<sup>2+y</sup>2 == 1" as a function --- and that is very painful.  

SOLUTION: Check if the input is an equation, and if so, make RHS zero, and plot corresponding function equal to 0.


Issue created by migration from https://trac.sagemath.org/ticket/5706





---

archive/issue_comments_044504.json:
```json
{
    "body": "Attachment [trac_5706.patch](tarball://root/attachments/some-uuid/ticket5706/trac_5706.patch) by @williamstein created at 2009-04-09 06:11:45",
    "created_at": "2009-04-09T06:11:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5706",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5706#issuecomment-44504",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac_5706.patch](tarball://root/attachments/some-uuid/ticket5706/trac_5706.patch) by @williamstein created at 2009-04-09 06:11:45



---

archive/issue_comments_044505.json:
```json
{
    "body": "There is one doctest failure in here:\n\n```\nsage -t -long \"devel/sage/sage/plot/contour_plot.py\"\n**********************************************************************\nFile \"/scratch/mabshoff/sage-3.4.1.rc2/devel/sage/sage/plot/contour_plot.py\", line 195:\n    sage: implicit_plot(x^2+y^2 == 2, (-3,3), (-3,3)).show(aspect_ratio=1)\nExpected nothing\nGot:\n    doctest:2846: DeprecationWarning: Substitution using function-call syntax and \nunnamed arguments is deprecated and will be removed from a future release of Sage; you \ncan use named arguments instead, like EXPR(x=..., y=...)\n**********************************************************************\n1 items had failures:\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2009-04-09T06:23:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5706",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5706#issuecomment-44505",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

There is one doctest failure in here:

```
sage -t -long "devel/sage/sage/plot/contour_plot.py"
**********************************************************************
File "/scratch/mabshoff/sage-3.4.1.rc2/devel/sage/sage/plot/contour_plot.py", line 195:
    sage: implicit_plot(x^2+y^2 == 2, (-3,3), (-3,3)).show(aspect_ratio=1)
Expected nothing
Got:
    doctest:2846: DeprecationWarning: Substitution using function-call syntax and 
unnamed arguments is deprecated and will be removed from a future release of Sage; you 
can use named arguments instead, like EXPR(x=..., y=...)
**********************************************************************
1 items had failures:
```


Cheers,

Michael



---

archive/issue_comments_044506.json:
```json
{
    "body": "Attachment [trac_5706.2.patch](tarball://root/attachments/some-uuid/ticket5706/trac_5706.2.patch) by mabshoff created at 2009-04-09 06:40:29\n\nSlightly fixed up version of William's patch due to deprecation of substitution (see #5413)",
    "created_at": "2009-04-09T06:40:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5706",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5706#issuecomment-44506",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [trac_5706.2.patch](tarball://root/attachments/some-uuid/ticket5706/trac_5706.2.patch) by mabshoff created at 2009-04-09 06:40:29

Slightly fixed up version of William's patch due to deprecation of substitution (see #5413)



---

archive/issue_comments_044507.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-09T06:40:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5706",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5706#issuecomment-44507",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_044508.json:
```json
{
    "body": "Merged trac_5706.2.patch in Sage 3.4.1.rc2.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-09T06:40:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5706",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5706#issuecomment-44508",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged trac_5706.2.patch in Sage 3.4.1.rc2.

Cheers,

Michael



---

archive/issue_events_005948.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2009-04-09T06:40:59Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5706",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5706#event-5948"
}
```



---

archive/issue_comments_044509.json:
```json
{
    "body": "Ooops, didn't change the review status.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-09T06:49:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5706",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5706#issuecomment-44509",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Ooops, didn't change the review status.

Cheers,

Michael
