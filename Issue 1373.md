# Issue 1373: 2.8.15.alpha2: quotient_module.py doctest failure

archive/issues_001373.json:
```json
{
    "body": "Assignee: was\n\nOn my laptop (32-bit x86 Linux, Debian testing) I get the following doctest failure in 2.8.15.alpha2:\n\n```\nsage -t  devel/sage-main/sage/modules/quotient_module.py    **********************************************************************\nFile \"quotient_module.py\", line 161:\n    sage: cmp(Q1, 5)\nExpected:\n    1                  \nGot:\n    -1\n**********************************************************************\n```\n\n\nThe code compares type(Q1) and type(5); since type objects have no useful pre-defined comparison operation, this just compares the memory addresses of the type objects.\n\nI think the doctest should just be removed.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1373\n\n",
    "created_at": "2007-12-02T17:27:05Z",
    "labels": [
        "algebraic geometry",
        "major",
        "bug"
    ],
    "title": "2.8.15.alpha2: quotient_module.py doctest failure",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1373",
    "user": "cwitty"
}
```
Assignee: was

On my laptop (32-bit x86 Linux, Debian testing) I get the following doctest failure in 2.8.15.alpha2:

```
sage -t  devel/sage-main/sage/modules/quotient_module.py    **********************************************************************
File "quotient_module.py", line 161:
    sage: cmp(Q1, 5)
Expected:
    1                  
Got:
    -1
**********************************************************************
```


The code compares type(Q1) and type(5); since type objects have no useful pre-defined comparison operation, this just compares the memory addresses of the type objects.

I think the doctest should just be removed.

Issue created by migration from https://trac.sagemath.org/ticket/1373





---

archive/issue_comments_008808.json:
```json
{
    "body": "\n```\nsage: cmp(Q1, 5) != 0\nTrue\n```\n",
    "created_at": "2007-12-03T01:37:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1373",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1373#issuecomment-8808",
    "user": "was"
}
```


```
sage: cmp(Q1, 5) != 0
True
```




---

archive/issue_comments_008809.json:
```json
{
    "body": "Merged in 2.8.15.rc0.",
    "created_at": "2007-12-03T01:52:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1373",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1373#issuecomment-8809",
    "user": "mabshoff"
}
```

Merged in 2.8.15.rc0.



---

archive/issue_comments_008810.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-03T01:52:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1373",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1373#issuecomment-8810",
    "user": "mabshoff"
}
```

Resolution: fixed
