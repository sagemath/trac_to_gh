# Issue 4806: broken real number exponent preparsing

archive/issues_004806.json:
```json
{
    "body": "Assignee: @williamstein\n\nIn sage 3.2:\n\n\n```\nsage: 1.656e02\n165.600000000000      # ok\nsage: 1.656e-02\n0.0165600000000000     # ok\nsage: 1.656e+02\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n\n/Users/david/<ipython console> in <module>()\n\n/Users/david/sage-3.2/local/lib/python2.5/site-packages/sage/rings/real_mpfr.so in sage.rings.real_mpfr.create_RealNumber (sage/rings/real_mpfr.c:21490)()\n\n/Users/david/sage-3.2/local/lib/python2.5/site-packages/sage/rings/real_mpfr.so in sage.rings.real_mpfr.RealLiteral.__init__ (sage/rings/real_mpfr.c:20706)()\n\n/Users/david/sage-3.2/local/lib/python2.5/site-packages/sage/rings/real_mpfr.so in sage.rings.real_mpfr.RealNumber.__init__ (sage/rings/real_mpfr.c:7305)()\n\n/Users/david/sage-3.2/local/lib/python2.5/site-packages/sage/rings/real_mpfr.so in sage.rings.real_mpfr.RealNumber._set (sage/rings/real_mpfr.c:7782)()\n\nTypeError: Unable to convert x (='1.656e') to real number.\n```\n\n\nIn plain python 2.5.2:\n\n```\n>>> 1.656e+02\n165.59999999999999\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4806\n\n",
    "created_at": "2008-12-15T17:04:37Z",
    "labels": [
        "user interface",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "broken real number exponent preparsing",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4806",
    "user": "dmharvey"
}
```
Assignee: @williamstein

In sage 3.2:


```
sage: 1.656e02
165.600000000000      # ok
sage: 1.656e-02
0.0165600000000000     # ok
sage: 1.656e+02
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/Users/david/<ipython console> in <module>()

/Users/david/sage-3.2/local/lib/python2.5/site-packages/sage/rings/real_mpfr.so in sage.rings.real_mpfr.create_RealNumber (sage/rings/real_mpfr.c:21490)()

/Users/david/sage-3.2/local/lib/python2.5/site-packages/sage/rings/real_mpfr.so in sage.rings.real_mpfr.RealLiteral.__init__ (sage/rings/real_mpfr.c:20706)()

/Users/david/sage-3.2/local/lib/python2.5/site-packages/sage/rings/real_mpfr.so in sage.rings.real_mpfr.RealNumber.__init__ (sage/rings/real_mpfr.c:7305)()

/Users/david/sage-3.2/local/lib/python2.5/site-packages/sage/rings/real_mpfr.so in sage.rings.real_mpfr.RealNumber._set (sage/rings/real_mpfr.c:7782)()

TypeError: Unable to convert x (='1.656e') to real number.
```


In plain python 2.5.2:

```
>>> 1.656e+02
165.59999999999999
```



Issue created by migration from https://trac.sagemath.org/ticket/4806





---

archive/issue_comments_036437.json:
```json
{
    "body": "Rolled into #5079",
    "created_at": "2009-01-23T22:30:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4806",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4806#issuecomment-36437",
    "user": "boothby"
}
```

Rolled into #5079



---

archive/issue_comments_036438.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2009-01-23T22:30:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4806",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4806#issuecomment-36438",
    "user": "boothby"
}
```

Resolution: duplicate
