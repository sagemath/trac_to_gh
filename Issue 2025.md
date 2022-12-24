# Issue 2025: bug in applying functions to a symbolic matrix

archive/issues_002025.json:
```json
{
    "body": "Assignee: was\n\nNote below that the stupid constant term of the taylor expansion\ninside the matrix keeps getting pushed off to the far right!\n\n\n```\nsage: m = matrix(1,[-x/(2*x-4)])\nsage: m.apply_map(lambda e: taylor(e,x,0,4))\n[x^4/32 + x^3/16 + x^2/8 + x/4]\nsage: m.apply_map(lambda e: taylor(e,x,0,4))\n[x^4/32 + x^3/16 + x^2/8 + x/4]\nsage: m.apply_map(lambda e: taylor(e,x,1,4))\n[x + (x - 1)^4 + (x - 1)^3 + (x - 1)^2 - 1/2]\nsage: m.apply_map(lambda e: taylor(e,x,2,4))\n[-1/(x - 2) - 1/2]\nsage: m.apply_map(lambda e: taylor(e,x,3,4))\n[x - (x - 3)^4 + (x - 3)^3 - (x - 3)^2 - 9/2]\nsage: m[0,0].taylor(x,3,4)\n-3/2 + x - 3 - (x - 3)^2 + (x - 3)^3 - (x - 3)^4\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2025\n\n",
    "created_at": "2008-02-01T14:02:18Z",
    "labels": [
        "calculus",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "bug in applying functions to a symbolic matrix",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2025",
    "user": "was"
}
```
Assignee: was

Note below that the stupid constant term of the taylor expansion
inside the matrix keeps getting pushed off to the far right!


```
sage: m = matrix(1,[-x/(2*x-4)])
sage: m.apply_map(lambda e: taylor(e,x,0,4))
[x^4/32 + x^3/16 + x^2/8 + x/4]
sage: m.apply_map(lambda e: taylor(e,x,0,4))
[x^4/32 + x^3/16 + x^2/8 + x/4]
sage: m.apply_map(lambda e: taylor(e,x,1,4))
[x + (x - 1)^4 + (x - 1)^3 + (x - 1)^2 - 1/2]
sage: m.apply_map(lambda e: taylor(e,x,2,4))
[-1/(x - 2) - 1/2]
sage: m.apply_map(lambda e: taylor(e,x,3,4))
[x - (x - 3)^4 + (x - 3)^3 - (x - 3)^2 - 9/2]
sage: m[0,0].taylor(x,3,4)
-3/2 + x - 3 - (x - 3)^2 + (x - 3)^3 - (x - 3)^4
```


Issue created by migration from https://trac.sagemath.org/ticket/2025





---

archive/issue_comments_013098.json:
```json
{
    "body": "This is caused by the following.\n\n\n\n```\nsage: a = -x/(2*x-4)\nsage: e = lambda e: taylor(e,x,3,4)\nsage: b = e(a)._maxima_(); b\nx-(x-3)^4+(x-3)^3-(x-3)^2-9/2\n```\n\n\n\nI don't know a good/easy way to prevent this from happening.",
    "created_at": "2008-02-02T02:30:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2025",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2025#issuecomment-13098",
    "user": "mhansen"
}
```

This is caused by the following.



```
sage: a = -x/(2*x-4)
sage: e = lambda e: taylor(e,x,3,4)
sage: b = e(a)._maxima_(); b
x-(x-3)^4+(x-3)^3-(x-3)^2-9/2
```



I don't know a good/easy way to prevent this from happening.



---

archive/issue_comments_013099.json:
```json
{
    "body": "Note that this issue arises from using Maxima internally for symbolic matrices.  If we use Sage's generic matrices over SR, then this isn't an issue.\n\n\nOne possible fix would be to add a simplify=False option to tell maxima not to use any simplification rules when constructing the object.",
    "created_at": "2008-02-02T02:41:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2025",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2025#issuecomment-13099",
    "user": "mhansen"
}
```

Note that this issue arises from using Maxima internally for symbolic matrices.  If we use Sage's generic matrices over SR, then this isn't an issue.


One possible fix would be to add a simplify=False option to tell maxima not to use any simplification rules when constructing the object.



---

archive/issue_comments_013100.json:
```json
{
    "body": "Changing assignee from was to gfurnish.",
    "created_at": "2008-03-16T20:10:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2025",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2025#issuecomment-13100",
    "user": "gfurnish"
}
```

Changing assignee from was to gfurnish.



---

archive/issue_comments_013101.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-03-16T20:10:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2025",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2025#issuecomment-13101",
    "user": "gfurnish"
}
```

Changing status from new to assigned.



---

archive/issue_comments_013102.json:
```json
{
    "body": "Note that this will be fixed when we switch over to Pynac as symbolic arithmetic won't have a huge overhead.",
    "created_at": "2009-01-22T22:49:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2025",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2025#issuecomment-13102",
    "user": "mhansen"
}
```

Note that this will be fixed when we switch over to Pynac as symbolic arithmetic won't have a huge overhead.



---

archive/issue_comments_013103.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2009-06-04T21:15:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2025",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2025#issuecomment-13103",
    "user": "mhansen"
}
```

Resolution: invalid



---

archive/issue_comments_013104.json:
```json
{
    "body": "This is now fixed due to the changes in 4.0\n\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: sage: m = matrix(1,[-x/(2*x-4)])\nsage: sage: m.apply_map(lambda e: taylor(e,x,0,4))\n[1/32*x^4 + 1/16*x^3 + 1/8*x^2 + 1/4*x]\nsage: sage: m.apply_map(lambda e: taylor(e,x,0,4))\n[1/32*x^4 + 1/16*x^3 + 1/8*x^2 + 1/4*x]\nsage: sage: m.apply_map(lambda e: taylor(e,x,1,4))\n[(x - 1)^4 + (x - 1)^3 + (x - 1)^2 + x - 1/2]\nsage: sage: m.apply_map(lambda e: taylor(e,x,2,4))\n[-1/(x - 2) - 1/2]\nsage: sage: m.apply_map(lambda e: taylor(e,x,3,4))\n[-(x - 3)^4 + (x - 3)^3 - (x - 3)^2 + x - 9/2]\nsage: sage: m[0,0].taylor(x,3,4)\n-(x - 3)^4 + (x - 3)^3 - (x - 3)^2 + x - 9/2\n```\n",
    "created_at": "2009-06-04T21:15:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2025",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2025#issuecomment-13104",
    "user": "mhansen"
}
```

This is now fixed due to the changes in 4.0


```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: sage: m = matrix(1,[-x/(2*x-4)])
sage: sage: m.apply_map(lambda e: taylor(e,x,0,4))
[1/32*x^4 + 1/16*x^3 + 1/8*x^2 + 1/4*x]
sage: sage: m.apply_map(lambda e: taylor(e,x,0,4))
[1/32*x^4 + 1/16*x^3 + 1/8*x^2 + 1/4*x]
sage: sage: m.apply_map(lambda e: taylor(e,x,1,4))
[(x - 1)^4 + (x - 1)^3 + (x - 1)^2 + x - 1/2]
sage: sage: m.apply_map(lambda e: taylor(e,x,2,4))
[-1/(x - 2) - 1/2]
sage: sage: m.apply_map(lambda e: taylor(e,x,3,4))
[-(x - 3)^4 + (x - 3)^3 - (x - 3)^2 + x - 9/2]
sage: sage: m[0,0].taylor(x,3,4)
-(x - 3)^4 + (x - 3)^3 - (x - 3)^2 + x - 9/2
```

