# Issue 3941: threading diff over lists to give the jacobian

archive/issues_003941.json:
```json
{
    "body": "Assignee: @garyfurnish\n\nIn MMA, you can thread the derivative over lists of variables and functions to compute the Jacobian.  Here's a routine that wraps the sage diff function to do it.  \n\n\n```\ndef diff(f,*args):\n    if isinstance(f, (list, tuple)):\n        return [diff(component,*args) for component in f]\n    else:\n        if isinstance(args[0], (list, tuple)):\n            return [diff(f,variable) for variable in args[0]]\n        else:\n            return sage.all.diff(f,*args)\n```\n\n\nand the results:\n\n\n```\nsage: var('a,b,c,d,x,y')\nsage: diff((a*x+b*y,c*x+d*y),(x,y))\n[[a, b], [c, d]]\n```\n\n\nwell, so the result is not really a matrix, but rather a nested list that could be indexed like a matrix or turned into a matrix in the above case.\n\n\nWe could write the above even more simply if we had an outer product operator: \n\nouter_product(diff,f,vars), where f and vars were lists.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3941\n\n",
    "created_at": "2008-08-24T05:13:27Z",
    "labels": [
        "component: calculus",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "threading diff over lists to give the jacobian",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3941",
    "user": "https://github.com/jasongrout"
}
```
Assignee: @garyfurnish

In MMA, you can thread the derivative over lists of variables and functions to compute the Jacobian.  Here's a routine that wraps the sage diff function to do it.  


```
def diff(f,*args):
    if isinstance(f, (list, tuple)):
        return [diff(component,*args) for component in f]
    else:
        if isinstance(args[0], (list, tuple)):
            return [diff(f,variable) for variable in args[0]]
        else:
            return sage.all.diff(f,*args)
```


and the results:


```
sage: var('a,b,c,d,x,y')
sage: diff((a*x+b*y,c*x+d*y),(x,y))
[[a, b], [c, d]]
```


well, so the result is not really a matrix, but rather a nested list that could be indexed like a matrix or turned into a matrix in the above case.


We could write the above even more simply if we had an outer product operator: 

outer_product(diff,f,vars), where f and vars were lists.

Issue created by migration from https://trac.sagemath.org/ticket/3941





---

archive/issue_comments_028198.json:
```json
{
    "body": "See also #2547, asking for a symbolic gradient and hessian.",
    "created_at": "2008-08-31T15:06:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3941",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3941#issuecomment-28198",
    "user": "https://github.com/jicama"
}
```

See also #2547, asking for a symbolic gradient and hessian.



---

archive/issue_comments_028199.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-11-14T06:24:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3941",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3941#issuecomment-28199",
    "user": "https://github.com/jasongrout"
}
```

Changing status from new to assigned.



---

archive/issue_comments_028200.json:
```json
{
    "body": "Changing assignee from @garyfurnish to @jasongrout.",
    "created_at": "2008-11-14T06:24:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3941",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3941#issuecomment-28200",
    "user": "https://github.com/jasongrout"
}
```

Changing assignee from @garyfurnish to @jasongrout.



---

archive/issue_comments_028201.json:
```json
{
    "body": "See http://groups.google.com/group/sage-devel/browse_thread/thread/666b18d9ea182f13 for an updated mydiff function and discussion.",
    "created_at": "2009-01-14T07:37:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3941",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3941#issuecomment-28201",
    "user": "https://github.com/jasongrout"
}
```

See http://groups.google.com/group/sage-devel/browse_thread/thread/666b18d9ea182f13 for an updated mydiff function and discussion.



---

archive/issue_comments_028202.json:
```json
{
    "body": "Why not have a function .jacobian to give the jacobian?",
    "created_at": "2009-01-14T16:47:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3941",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3941#issuecomment-28202",
    "user": "https://github.com/williamstein"
}
```

Why not have a function .jacobian to give the jacobian?



---

archive/issue_comments_028203.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2009-01-22T18:22:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3941",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3941#issuecomment-28203",
    "user": "https://github.com/aghitza"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_028204.json:
```json
{
    "body": "What about functions with codomain R<sup>n</sup> where n>1?  If these are represented via a list, tuple, or vector, the code works from above (well, let's add handling of vectors with the following:\n\n\n```\ndef diff(f, *args):\n    if isinstance(f, (list, tuple)) or sage.structure.element.is_Vector(f):\n        return [diff(component, *args) for component in f]\n    else:\n        if isinstance(args[0], (list, tuple)) or is_Vector(args[0]):\n            return [diff(f, variable) for variable in args[0]]\n        else:\n            return sage.all.diff(f, *args)\n```\n\n\nThis wouldn't work with a `.jacobian` method---where would we put the method?",
    "created_at": "2009-02-12T22:44:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3941",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3941#issuecomment-28204",
    "user": "https://github.com/jasongrout"
}
```

What about functions with codomain R<sup>n</sup> where n>1?  If these are represented via a list, tuple, or vector, the code works from above (well, let's add handling of vectors with the following:


```
def diff(f, *args):
    if isinstance(f, (list, tuple)) or sage.structure.element.is_Vector(f):
        return [diff(component, *args) for component in f]
    else:
        if isinstance(args[0], (list, tuple)) or is_Vector(args[0]):
            return [diff(f, variable) for variable in args[0]]
        else:
            return sage.all.diff(f, *args)
```


This wouldn't work with a `.jacobian` method---where would we put the method?



---

archive/issue_comments_028205.json:
```json
{
    "body": "#5253 makes this less needed, but I still think it would be nice to have good syntax for this sort of thing using the diff function.",
    "created_at": "2009-02-13T05:50:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3941",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3941#issuecomment-28205",
    "user": "https://github.com/jasongrout"
}
```

#5253 makes this less needed, but I still think it would be nice to have good syntax for this sort of thing using the diff function.



---

archive/issue_comments_028206.json:
```json
{
    "body": "Does the new functionality that\n\n```\nf(x,y)=3*sin(x)-2*cos(y)-x*y\nf.diff(2)\n```\n\nworks change anything on this ticket?  Just throwing it out there, it may be irrelevant.",
    "created_at": "2010-05-26T20:09:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3941",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3941#issuecomment-28206",
    "user": "https://github.com/kcrisman"
}
```

Does the new functionality that

```
f(x,y)=3*sin(x)-2*cos(y)-x*y
f.diff(2)
```

works change anything on this ticket?  Just throwing it out there, it may be irrelevant.
