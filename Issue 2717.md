# Issue 2717: maxima expect interface synchronization not sufficiently robust

archive/issues_002717.json:
```json
{
    "body": "Assignee: was\n\nIt is still possible to very occassionaly throw off the Maxima synchronization, maybe during parallel doctesting (?).  E.g.,\n\n```\nsage -t  devel/sage-main/sage/calculus/functional.py        **********************************************************************\nFile \"functional.py\", line 301:\n    sage: limit((tan(sin(x)) - sin(tan(x)))/x^7, taylor=True, x=0)\nExpected:\n    1/30\nGot:\n    1820214126\n**********************************************************************\n1 items had failures:\n   1 of   7 in __main__.example_4\n***Test Failed*** 1 failures.\nFor whitespace errors\n```\n\n\nThe above is particularly bad since you can't tell something went wrong -- you just\nget a wrong number out.  The point of this ticket isn't to fix the whole problem.\nInstead, change the synchronization marker in maxima.py from being a single number\nto a string such as \n\n    __SAGE_SYNCHRO_MARKER_1820214126\n\nso that instead of people being confused by a wrong answer, it will be\ncrystal clear that something went wrong. \n\nThis will likely be nearly trivial to implement. \n\nIssue created by migration from https://trac.sagemath.org/ticket/2717\n\n",
    "created_at": "2008-03-29T16:27:36Z",
    "labels": [
        "interfaces",
        "blocker",
        "bug"
    ],
    "title": "maxima expect interface synchronization not sufficiently robust",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2717",
    "user": "was"
}
```
Assignee: was

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

archive/issue_comments_018735.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-03-29T19:19:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2717",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2717#issuecomment-18735",
    "user": "cwitty"
}
```

Attachment



---

archive/issue_comments_018736.json:
```json
{
    "body": "Looks good to me. Second review appreciated.\n\nCheers,\n\nMichael",
    "created_at": "2008-03-29T19:28:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2717",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2717#issuecomment-18736",
    "user": "mabshoff"
}
```

Looks good to me. Second review appreciated.

Cheers,

Michael



---

archive/issue_comments_018737.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2008-03-29T20:38:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2717",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2717#issuecomment-18737",
    "user": "mhansen"
}
```

Looks good to me.



---

archive/issue_comments_018738.json:
```json
{
    "body": "Merged in Sage 2.11.rc0",
    "created_at": "2008-03-29T20:50:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2717",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2717#issuecomment-18738",
    "user": "mabshoff"
}
```

Merged in Sage 2.11.rc0



---

archive/issue_comments_018739.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-29T20:50:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2717",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2717#issuecomment-18739",
    "user": "mabshoff"
}
```

Resolution: fixed
