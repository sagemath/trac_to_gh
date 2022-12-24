# Issue 7315: Can only forget one GenericDeclaration at a time for some reason

archive/issues_007315.json:
```json
{
    "body": "Assignee: burcin\n\nFrom [ this thread]: \n\n```\nsage: var('m')\nm\nsage: var('n')\nn\nsage: assume(n, 'integer'); assume(m, 'integer')\nsage: sin(n*pi).simplify()\n0\nsage: sin(m*pi).simplify()\n0\nsage: forget()\nsage: sin(m*pi).simplify()\n0\nsage: sin(n*pi).simplify()\nsin(pi*n)\n```\n\nThe problem seems to lie in the last few lines of _forget_all in sage.symbolic.assumptions.py, where for some reason the loop isn't doing what it should.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7315\n\n",
    "created_at": "2009-10-26T19:56:08Z",
    "labels": [
        "calculus",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.2.1",
    "title": "Can only forget one GenericDeclaration at a time for some reason",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7315",
    "user": "kcrisman"
}
```
Assignee: burcin

From [ this thread]: 

```
sage: var('m')
m
sage: var('n')
n
sage: assume(n, 'integer'); assume(m, 'integer')
sage: sin(n*pi).simplify()
0
sage: sin(m*pi).simplify()
0
sage: forget()
sage: sin(m*pi).simplify()
0
sage: sin(n*pi).simplify()
sin(pi*n)
```

The problem seems to lie in the last few lines of _forget_all in sage.symbolic.assumptions.py, where for some reason the loop isn't doing what it should.

Issue created by migration from https://trac.sagemath.org/ticket/7315





---

archive/issue_comments_061125.json:
```json
{
    "body": "Unfortunately, #1163 doesn't fix this either.",
    "created_at": "2009-10-26T20:04:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7315",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7315#issuecomment-61125",
    "user": "kcrisman"
}
```

Unfortunately, #1163 doesn't fix this either.



---

archive/issue_comments_061126.json:
```json
{
    "body": "The problem is actually because list removal is called in GenericDeclaration.forget(), so this is about behavior of list iteration in Python when you remove elements:\n\n```\n>>> L=[1,2,3,4]\n>>> for x in L:\n...     L.remove(x)\n...     x\n...     L\n... \n1\n[2, 3, 4]\n3\n[2, 4]\n```\n\nSo this piece of code is apparently using the wrong/un-Pythonic way of removing items from a list.",
    "created_at": "2009-10-26T20:29:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7315",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7315#issuecomment-61126",
    "user": "kcrisman"
}
```

The problem is actually because list removal is called in GenericDeclaration.forget(), so this is about behavior of list iteration in Python when you remove elements:

```
>>> L=[1,2,3,4]
>>> for x in L:
...     L.remove(x)
...     x
...     L
... 
1
[2, 3, 4]
3
[2, 4]
```

So this piece of code is apparently using the wrong/un-Pythonic way of removing items from a list.



---

archive/issue_comments_061127.json:
```json
{
    "body": "Attachment [trac_7315-forget-all.patch](tarball://root/attachments/some-uuid/ticket7315/trac_7315-forget-all.patch) by kcrisman created at 2009-10-27 13:37:06\n\nBased on 4.2",
    "created_at": "2009-10-27T13:37:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7315",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7315#issuecomment-61127",
    "user": "kcrisman"
}
```

Attachment [trac_7315-forget-all.patch](tarball://root/attachments/some-uuid/ticket7315/trac_7315-forget-all.patch) by kcrisman created at 2009-10-27 13:37:06

Based on 4.2



---

archive/issue_comments_061128.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-10-27T13:43:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7315",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7315#issuecomment-61128",
    "user": "kcrisman"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_061129.json:
```json
{
    "body": "This patch should fix the issue.  In fact, it's only because #7084 finally allows more than one such declaration that this bug ever showed up!",
    "created_at": "2009-10-27T13:43:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7315",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7315#issuecomment-61129",
    "user": "kcrisman"
}
```

This patch should fix the issue.  In fact, it's only because #7084 finally allows more than one such declaration that this bug ever showed up!



---

archive/issue_comments_061130.json:
```json
{
    "body": "Great catch.  Doctests and documentation passes.  Good work.",
    "created_at": "2009-10-29T19:36:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7315",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7315#issuecomment-61130",
    "user": "jason"
}
```

Great catch.  Doctests and documentation passes.  Good work.



---

archive/issue_comments_061131.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-10-29T19:36:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7315",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7315#issuecomment-61131",
    "user": "jason"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_061132.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-10-31T16:46:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7315",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7315#issuecomment-61132",
    "user": "mhansen"
}
```

Resolution: fixed
