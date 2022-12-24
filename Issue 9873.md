# Issue 9873: add a function for the derivative of ceil and floor

archive/issues_009873.json:
```json
{
    "body": "Assignee: @burcin\n\nCC:  ktkohl @rwst @kcrisman @pelegm\n\nWe should define a new symbolic function for the derivative of `ceil` or `floor`. \n\nIn Maple:\n\n\n```\n> diff(floor(x),x);\n                                  floor(1, x)\n> diff(floor(x),x,x);\n                                  floor(1, x)\n> diff(ceil(x),x,x); \n                                  floor(1, x)\n> eval(diff(ceil(x),x,x),x=1.5);\n                                       0\n> eval(diff(ceil(x),x,x),x=0);  \nError, (in floor) floor is not differentiable at integers\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9874\n\n",
    "created_at": "2010-09-08T11:41:23Z",
    "labels": [
        "symbolics",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.8",
    "title": "add a function for the derivative of ceil and floor",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9873",
    "user": "@burcin"
}
```
Assignee: @burcin

CC:  ktkohl @rwst @kcrisman @pelegm

We should define a new symbolic function for the derivative of `ceil` or `floor`. 

In Maple:


```
> diff(floor(x),x);
                                  floor(1, x)
> diff(floor(x),x,x);
                                  floor(1, x)
> diff(ceil(x),x,x); 
                                  floor(1, x)
> eval(diff(ceil(x),x,x),x=1.5);
                                       0
> eval(diff(ceil(x),x,x),x=0);  
Error, (in floor) floor is not differentiable at integers
```


Issue created by migration from https://trac.sagemath.org/ticket/9874





---

archive/issue_comments_097695.json:
```json
{
    "body": "Changing keywords from \"\" to \"sd35.5\".",
    "created_at": "2012-01-12T14:48:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9873",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9873#issuecomment-97695",
    "user": "ktkohl"
}
```

Changing keywords from "" to "sd35.5".



---

archive/issue_comments_097696.json:
```json
{
    "body": "These give the right answer but also a runtime error:\n\n```\nsage: floor(x).derivative().subs(x=1.5)\nException RuntimeError: 'maximum recursion depth exceeded while calling a Python object' in 'sage.structure.parent.good_as_coerce_domain' ignored\n0\nsage: ceil(x).derivative().subs(x=1.5)\nException RuntimeError: 'maximum recursion depth exceeded while calling a Python object' in 'sage.structure.parent.good_as_coerce_domain' ignored\n0\n```\n\n\n----\nNew commits:",
    "created_at": "2015-05-25T18:44:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9873",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9873#issuecomment-97696",
    "user": "ktkohl"
}
```

These give the right answer but also a runtime error:

```
sage: floor(x).derivative().subs(x=1.5)
Exception RuntimeError: 'maximum recursion depth exceeded while calling a Python object' in 'sage.structure.parent.good_as_coerce_domain' ignored
0
sage: ceil(x).derivative().subs(x=1.5)
Exception RuntimeError: 'maximum recursion depth exceeded while calling a Python object' in 'sage.structure.parent.good_as_coerce_domain' ignored
0
```


----
New commits:



---

archive/issue_comments_097697.json:
```json
{
    "body": "Just a quick note that there are empty examples and tests fields but you probably know that.",
    "created_at": "2015-05-26T06:11:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9873",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9873#issuecomment-97697",
    "user": "@rwst"
}
```

Just a quick note that there are empty examples and tests fields but you probably know that.
