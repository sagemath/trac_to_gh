# Issue 187: [Pyrex] c-code mis-interpretation

archive/issues_000187.json:
```json
{
    "body": "Assignee: @williamstein\n\nI found a small bit of code that gets compiled incorrectly to c.  A sample is:\n\n\n```\ndef unlist():\n        lst = [1,2]\n        lst,m = lst\n```\n\n\nThe translated c-code from this will produce an Unindexable exception.  This \nresults from the fact that the variable \"lst\" is bound to the first element \nof the list (the integer 1) before the second element is extracted \nfrom \"lst\".  Hence it tries to unpack from the integer rather than the list.\n\nIssue created by migration from https://trac.sagemath.org/ticket/187\n\n",
    "created_at": "2006-12-19T02:32:23Z",
    "labels": [
        "interfaces",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.1",
    "title": "[Pyrex] c-code mis-interpretation",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/187",
    "user": "joel"
}
```
Assignee: @williamstein

I found a small bit of code that gets compiled incorrectly to c.  A sample is:


```
def unlist():
        lst = [1,2]
        lst,m = lst
```


The translated c-code from this will produce an Unindexable exception.  This 
results from the fact that the variable "lst" is bound to the first element 
of the list (the integer 1) before the second element is extracted 
from "lst".  Hence it tries to unpack from the integer rather than the list.

Issue created by migration from https://trac.sagemath.org/ticket/187





---

archive/issue_comments_000850.json:
```json
{
    "body": "This is a rather old bug. We should verify that the problem still exists.\n\ntagged for 2.9, hopefully to be resolved during Sage Bug Day 2.\n\nCheers,\n\nMichael",
    "created_at": "2007-08-28T18:56:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/187",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/187#issuecomment-850",
    "user": "mabshoff"
}
```

This is a rather old bug. We should verify that the problem still exists.

tagged for 2.9, hopefully to be resolved during Sage Bug Day 2.

Cheers,

Michael



---

archive/issue_comments_000851.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-19T23:29:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/187",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/187#issuecomment-851",
    "user": "@williamstein"
}
```

Resolution: fixed



---

archive/issue_comments_000852.json:
```json
{
    "body": "works for me now.",
    "created_at": "2008-01-19T23:29:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/187",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/187#issuecomment-852",
    "user": "@williamstein"
}
```

works for me now.
