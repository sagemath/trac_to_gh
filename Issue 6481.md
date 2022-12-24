# Issue 6481: g.subs({x:1,y:2}) should walk through x,y sorted

archive/issues_006481.json:
```json
{
    "body": "Assignee: malb\n\nreported by Kwankyu on [sage-support]:\n\n\n```\nI mean the substitution y:x*y is applied first in the following\n\nsage: R.<x,y>=QQ[]\nsage: g=x+y\nsage: g.subs({x:x+1,y:x*y})\nx*y + x + y + 1\n\nwhere I think applying x:x+1 first seems intuitive if order ever\nshould be significant.\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6481\n\n",
    "created_at": "2009-07-08T12:58:14Z",
    "labels": [
        "commutative algebra",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "g.subs({x:1,y:2}) should walk through x,y sorted",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6481",
    "user": "malb"
}
```
Assignee: malb

reported by Kwankyu on [sage-support]:


```
I mean the substitution y:x*y is applied first in the following

sage: R.<x,y>=QQ[]
sage: g=x+y
sage: g.subs({x:x+1,y:x*y})
x*y + x + y + 1

where I think applying x:x+1 first seems intuitive if order ever
should be significant.
```



Issue created by migration from https://trac.sagemath.org/ticket/6481





---

archive/issue_comments_052399.json:
```json
{
    "body": "For the record, I think the entire design of subs for multivariate polynomial rings is wrong.  I've thus opened #6482 and explained my reasoning for this.\n\nNote that in any case, if the current subs behavior is super fast or useful to people (is it?) then we can keep it as a nondefault option, in which case this ticket #6481 also makes sense to keep, since at least we should do the order of substitution in an easy-to-understand way.",
    "created_at": "2009-07-08T13:11:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6481",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6481#issuecomment-52399",
    "user": "was"
}
```

For the record, I think the entire design of subs for multivariate polynomial rings is wrong.  I've thus opened #6482 and explained my reasoning for this.

Note that in any case, if the current subs behavior is super fast or useful to people (is it?) then we can keep it as a nondefault option, in which case this ticket #6481 also makes sense to keep, since at least we should do the order of substitution in an easy-to-understand way.



---

archive/issue_comments_052400.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2009-09-09T20:13:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6481",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6481#issuecomment-52400",
    "user": "malb"
}
```

Resolution: duplicate



---

archive/issue_comments_052401.json:
```json
{
    "body": "Dupe of #6482",
    "created_at": "2009-09-09T20:13:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6481",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6481#issuecomment-52401",
    "user": "malb"
}
```

Dupe of #6482
