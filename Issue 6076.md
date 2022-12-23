# Issue 6076: Allow to redefine the python symbol in the Notebook

archive/issues_006076.json:
```json
{
    "body": "Assignee: boothby\n\nCC:  was mhansen\n\nThe problem is that Sage notebook doesn't allow the user to redefine the \"python\" symbol. \n\nAs a consequence,\n\n\n```\nfrom sympy import *\n```\n\n\nfails. We can of course fix this particular problem in sympy, but I think this is a bug that should be fixed in the notebook. See this thread for more info:\n\nhttp://groups.google.com/group/sage-devel/browse_thread/thread/ed5db1f344ed6371/\n\nIssue created by migration from https://trac.sagemath.org/ticket/6076\n\n",
    "created_at": "2009-05-18T21:20:07Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "title": "Allow to redefine the python symbol in the Notebook",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6076",
    "user": "certik"
}
```
Assignee: boothby

CC:  was mhansen

The problem is that Sage notebook doesn't allow the user to redefine the "python" symbol. 

As a consequence,


```
from sympy import *
```


fails. We can of course fix this particular problem in sympy, but I think this is a bug that should be fixed in the notebook. See this thread for more info:

http://groups.google.com/group/sage-devel/browse_thread/thread/ed5db1f344ed6371/

Issue created by migration from https://trac.sagemath.org/ticket/6076





---

archive/issue_comments_048364.json:
```json
{
    "body": "Works for me now. Anyone mind checking if it's a problem, and close otherwise?",
    "created_at": "2009-11-30T08:49:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6076",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6076#issuecomment-48364",
    "user": "timdumol"
}
```

Works for me now. Anyone mind checking if it's a problem, and close otherwise?



---

archive/issue_comments_048365.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-11-30T08:59:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6076",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6076#issuecomment-48365",
    "user": "certik"
}
```

Resolution: fixed



---

archive/issue_comments_048366.json:
```json
{
    "body": "I can confirm that this is now fixed on sagenb.org, so this ticket can be closed. Thanks for fixing it!\n\nOndrej",
    "created_at": "2009-11-30T08:59:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6076",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6076#issuecomment-48366",
    "user": "certik"
}
```

I can confirm that this is now fixed on sagenb.org, so this ticket can be closed. Thanks for fixing it!

Ondrej
