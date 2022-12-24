# Issue 2472: what parent should floor return?

archive/issues_002472.json:
```json
{
    "body": "Assignee: somebody\n\nCC:  @ncalexan\n\nKeywords: floor truncate ceil ceiling parent integer\n\nI think `floor` and `ceil` and `truncate` should return integers.\n\n\n```\nsage: floor(2).parent()\nInteger Ring\nsage: floor(2.0).parent()\nInteger Ring\nsage: floor(RIF(2.0)).parent()\nReal Interval Field with 53 bits of precision\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2472\n\n",
    "created_at": "2008-03-11T20:58:33Z",
    "labels": [
        "basic arithmetic",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "what parent should floor return?",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2472",
    "user": "@ncalexan"
}
```
Assignee: somebody

CC:  @ncalexan

Keywords: floor truncate ceil ceiling parent integer

I think `floor` and `ceil` and `truncate` should return integers.


```
sage: floor(2).parent()
Integer Ring
sage: floor(2.0).parent()
Integer Ring
sage: floor(RIF(2.0)).parent()
Real Interval Field with 53 bits of precision
```


Issue created by migration from https://trac.sagemath.org/ticket/2472





---

archive/issue_comments_016738.json:
```json
{
    "body": "> I think floor and ceil and truncate should return integers.\n\nI agree, though this goes against what Python does:\n\n\n```\nsage: math.floor(float(2.3))\n2.0    \n```\n\n\nI don't like Python's math.floor behavior, but I bet it agrees with the C library.\nYep:\n\n```\n     double\n     floor(double x);\n\n     long double\n     floorl(long double x);\n```\n\n\nI still vote for making floor always return Integer.",
    "created_at": "2008-03-11T21:03:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2472",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2472#issuecomment-16738",
    "user": "@williamstein"
}
```

> I think floor and ceil and truncate should return integers.

I agree, though this goes against what Python does:


```
sage: math.floor(float(2.3))
2.0    
```


I don't like Python's math.floor behavior, but I bet it agrees with the C library.
Yep:

```
     double
     floor(double x);

     long double
     floorl(long double x);
```


I still vote for making floor always return Integer.



---

archive/issue_comments_016739.json:
```json
{
    "body": "But what integer should it return?  In particular, what do you want floor(RIF(1.5, 12345.678)) to return, and why?  \n\nMy vote would be that floor and ceiling should not be implemented for RIF at all, because I don't think they have a sensible meaning.\n\nNote that when William first implemented floor and ceiling for RIF, he had them return integers; but he immediately (38 minutes later, according to Mercurial) changed them to return intervals, calling this a '\"moral\" improvement'.",
    "created_at": "2008-03-12T01:26:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2472",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2472#issuecomment-16739",
    "user": "cwitty"
}
```

But what integer should it return?  In particular, what do you want floor(RIF(1.5, 12345.678)) to return, and why?  

My vote would be that floor and ceiling should not be implemented for RIF at all, because I don't think they have a sensible meaning.

Note that when William first implemented floor and ceiling for RIF, he had them return integers; but he immediately (38 minutes later, according to Mercurial) changed them to return intervals, calling this a '"moral" improvement'.



---

archive/issue_comments_016740.json:
```json
{
    "body": "Perhaps what we need is an `IntegerInterval` class which represents an interval in ZZ.\n\nI think this might even have come up in the context of valuations of p-adic numbers, and I might have even discussed it with David Roe, but I can't remember if anything came out of it.",
    "created_at": "2008-03-13T18:50:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2472",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2472#issuecomment-16740",
    "user": "dmharvey"
}
```

Perhaps what we need is an `IntegerInterval` class which represents an interval in ZZ.

I think this might even have come up in the context of valuations of p-adic numbers, and I might have even discussed it with David Roe, but I can't remember if anything came out of it.



---

archive/issue_comments_016741.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2014-09-02T08:57:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2472",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2472#issuecomment-16741",
    "user": "@jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_016742.json:
```json
{
    "body": "We now have `unique_floor()` for `RIF` returning an integer, which solves the problem I guess.",
    "created_at": "2014-09-02T08:57:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2472",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2472#issuecomment-16742",
    "user": "@jdemeyer"
}
```

We now have `unique_floor()` for `RIF` returning an integer, which solves the problem I guess.



---

archive/issue_comments_016743.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2014-09-02T08:57:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2472",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2472#issuecomment-16743",
    "user": "@jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_016744.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2014-09-09T14:53:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2472",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2472#issuecomment-16744",
    "user": "@vbraun"
}
```

Resolution: fixed
