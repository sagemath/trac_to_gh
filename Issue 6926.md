# Issue 6926: multiple bugs in plotting symbolic expressions

archive/issues_006926.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @rlmill\n\nThis is a bug:\n\n```\nsage: plot(abs(exp(i*x)), xmin=1,xmax=2)\nTraceback (most recent call last):\n...\nTypeError: float() argument must be a string or a number\n```\n\nThe above should never happen, since the outputs of the function should be floats.   \n\nDoing the obvious workaround yields another totally different bug!\n\n```\nsage: plot(lambda x: float(abs(exp(i*x))), xmin=1,xmax=2)\nTraceback (most recent call last):\n...\nZeroDivisionError: float division\n```\n\n\nThe above ZeroDivisionError comes from trying incorrectly to scale the y-axis!\n\nThe following works, where we do two things explicitly, both of which should be completely automatic. \n\n```\nsage: plot(lambda x: float(abs(exp(i*x))), xmin=1,xmax=2, ymin=0,ymax=1)\n```\n\n\nThis was reported by Andi Walz on sage-support.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6926\n\n",
    "created_at": "2009-09-12T19:27:44Z",
    "labels": [
        "graphics",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "multiple bugs in plotting symbolic expressions",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6926",
    "user": "@williamstein"
}
```
Assignee: @williamstein

CC:  @rlmill

This is a bug:

```
sage: plot(abs(exp(i*x)), xmin=1,xmax=2)
Traceback (most recent call last):
...
TypeError: float() argument must be a string or a number
```

The above should never happen, since the outputs of the function should be floats.   

Doing the obvious workaround yields another totally different bug!

```
sage: plot(lambda x: float(abs(exp(i*x))), xmin=1,xmax=2)
Traceback (most recent call last):
...
ZeroDivisionError: float division
```


The above ZeroDivisionError comes from trying incorrectly to scale the y-axis!

The following works, where we do two things explicitly, both of which should be completely automatic. 

```
sage: plot(lambda x: float(abs(exp(i*x))), xmin=1,xmax=2, ymin=0,ymax=1)
```


This was reported by Andi Walz on sage-support.

Issue created by migration from https://trac.sagemath.org/ticket/6926





---

archive/issue_comments_057234.json:
```json
{
    "body": "The second bug is fixed in the latest alpha of Sage.  It was fixed by moving the axes drawing to matplotlib by #5448.",
    "created_at": "2009-09-12T19:49:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6926",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6926#issuecomment-57234",
    "user": "@jasongrout"
}
```

The second bug is fixed in the latest alpha of Sage.  It was fixed by moving the axes drawing to matplotlib by #5448.



---

archive/issue_comments_057235.json:
```json
{
    "body": "The first bug is now fixed, I believe by #7614.  This ticket can be closed as fixed now.",
    "created_at": "2010-01-17T10:32:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6926",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6926#issuecomment-57235",
    "user": "@jasongrout"
}
```

The first bug is now fixed, I believe by #7614.  This ticket can be closed as fixed now.



---

archive/issue_comments_057236.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-17T10:32:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6926",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6926#issuecomment-57236",
    "user": "@jasongrout"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_057237.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-17T11:00:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6926",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6926#issuecomment-57237",
    "user": "@jasongrout"
}
```

Resolution: fixed
