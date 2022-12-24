# Issue 2163: .show?? pops up the graphics item as well as the help page

archive/issues_002163.json:
```json
{
    "body": "Assignee: was\n\nAt the command line:\n\n\n```\nsage: a=plot(x^2,(x,-1,1))\nsage: a.show??\nsage: a.show?\n```\n\n\nIn either of the last two commands, the plot pops up on my Ubuntu 7.10 box (as well as the help).\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2163\n\n",
    "created_at": "2008-02-14T23:00:03Z",
    "labels": [
        "algebraic geometry",
        "major",
        "bug"
    ],
    "title": ".show?? pops up the graphics item as well as the help page",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2163",
    "user": "jason"
}
```
Assignee: was

At the command line:


```
sage: a=plot(x^2,(x,-1,1))
sage: a.show??
sage: a.show?
```


In either of the last two commands, the plot pops up on my Ubuntu 7.10 box (as well as the help).


Issue created by migration from https://trac.sagemath.org/ticket/2163





---

archive/issue_comments_014200.json:
```json
{
    "body": "Changing component from algebraic geometry to graphics.",
    "created_at": "2008-02-14T23:03:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2163",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2163#issuecomment-14200",
    "user": "mabshoff"
}
```

Changing component from algebraic geometry to graphics.



---

archive/issue_comments_014201.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-02-15T01:51:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2163",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2163#issuecomment-14201",
    "user": "mhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_014202.json:
```json
{
    "body": "Changing assignee from was to mhansen.",
    "created_at": "2008-02-15T01:51:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2163",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2163#issuecomment-14202",
    "user": "mhansen"
}
```

Changing assignee from was to mhansen.



---

archive/issue_comments_014203.json:
```json
{
    "body": "This is due to the following:\n\n\n```\nString Form:    <bound method Graphics.show of >\n```\n\n\nwhereas after show_default(False), we get:\n\n\n```\nString Form:    <bound method Graphics.show of Graphics object consisting of 1 graphics primitive>\n```\n",
    "created_at": "2008-02-15T01:51:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2163",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2163#issuecomment-14203",
    "user": "mhansen"
}
```

This is due to the following:


```
String Form:    <bound method Graphics.show of >
```


whereas after show_default(False), we get:


```
String Form:    <bound method Graphics.show of Graphics object consisting of 1 graphics primitive>
```




---

archive/issue_comments_014204.json:
```json
{
    "body": "This can be fixed if we can tell IPython to set show_default(False) when doing things like repr(a.show)",
    "created_at": "2008-02-15T02:11:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2163",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2163#issuecomment-14204",
    "user": "mhansen"
}
```

This can be fixed if we can tell IPython to set show_default(False) when doing things like repr(a.show)



---

archive/issue_comments_014205.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-03T00:54:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2163",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2163#issuecomment-14205",
    "user": "mhansen"
}
```

Resolution: fixed



---

archive/issue_comments_014206.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2008-09-03T00:54:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2163",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2163#issuecomment-14206",
    "user": "mhansen"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_014207.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2008-09-03T00:54:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2163",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2163#issuecomment-14207",
    "user": "mhansen"
}
```

Changing status from closed to reopened.



---

archive/issue_comments_014208.json:
```json
{
    "body": "Attachment [trac_2163.patch](tarball://root/attachments/some-uuid/ticket2163/trac_2163.patch) by mhansen created at 2008-12-02 08:44:34\n\nI had already fixed some problems caused by removing the 'nodoctest' at the top before realizing there's no good way to test the function which I added.\n\nThe thing which addresses this ticket is the last hunk at the bottom of the patch.",
    "created_at": "2008-12-02T08:44:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2163",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2163#issuecomment-14208",
    "user": "mhansen"
}
```

Attachment [trac_2163.patch](tarball://root/attachments/some-uuid/ticket2163/trac_2163.patch) by mhansen created at 2008-12-02 08:44:34

I had already fixed some problems caused by removing the 'nodoctest' at the top before realizing there's no good way to test the function which I added.

The thing which addresses this ticket is the last hunk at the bottom of the patch.



---

archive/issue_comments_014209.json:
```json
{
    "body": "This fixes the problem.  Tests pass in interpreter.py as well (thanks for fixing all those too!)\n\nPositive review.",
    "created_at": "2008-12-05T08:49:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2163",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2163#issuecomment-14209",
    "user": "jason"
}
```

This fixes the problem.  Tests pass in interpreter.py as well (thanks for fixing all those too!)

Positive review.



---

archive/issue_comments_014210.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-12-05T09:37:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2163",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2163#issuecomment-14210",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_014211.json:
```json
{
    "body": "Merged in Sage 3.2.2.alpha0",
    "created_at": "2008-12-05T09:37:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2163",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2163#issuecomment-14211",
    "user": "mabshoff"
}
```

Merged in Sage 3.2.2.alpha0
