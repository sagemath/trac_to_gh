# Issue 2933: calculus -- substitution of a dict for SymbolicFunctionEvaluation is broken (but **kwds works)

archive/issues_002933.json:
```json
{
    "body": "Assignee: @williamstein\n\nSubstitution with a dictionary as input is broken.  Notice below in the\nthird input that the dictionary is ignored?!\n\n\n```\nsage: function('f',x)\nf(x)\nsage: (f(x)).substitute(f=log)\nlog(x)\nsage: (f(x)).substitute({f:log})\nf(x)\nsage: type(f(x))\n<class 'sage.calculus.calculus.SymbolicFunctionEvaluation'>\nsage: (x^3 + 1).substitute(x=5)\n126\nsage: (x^3 + 1).substitute({x:5})\n126\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2933\n\n",
    "created_at": "2008-04-15T15:02:46Z",
    "labels": [
        "calculus",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "calculus -- substitution of a dict for SymbolicFunctionEvaluation is broken (but **kwds works)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2933",
    "user": "@williamstein"
}
```
Assignee: @williamstein

Substitution with a dictionary as input is broken.  Notice below in the
third input that the dictionary is ignored?!


```
sage: function('f',x)
f(x)
sage: (f(x)).substitute(f=log)
log(x)
sage: (f(x)).substitute({f:log})
f(x)
sage: type(f(x))
<class 'sage.calculus.calculus.SymbolicFunctionEvaluation'>
sage: (x^3 + 1).substitute(x=5)
126
sage: (x^3 + 1).substitute({x:5})
126
```


Issue created by migration from https://trac.sagemath.org/ticket/2933





---

archive/issue_comments_020202.json:
```json
{
    "body": "Changing assignee from @williamstein to @mwhansen.",
    "created_at": "2008-04-15T17:40:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2933",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2933#issuecomment-20202",
    "user": "@mwhansen"
}
```

Changing assignee from @williamstein to @mwhansen.



---

archive/issue_comments_020203.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-04-15T17:40:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2933",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2933#issuecomment-20203",
    "user": "@mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_020204.json:
```json
{
    "body": "Attachment [2933.patch](tarball://root/attachments/some-uuid/ticket2933/2933.patch) by @mwhansen created at 2008-04-15 17:40:47",
    "created_at": "2008-04-15T17:40:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2933",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2933#issuecomment-20204",
    "user": "@mwhansen"
}
```

Attachment [2933.patch](tarball://root/attachments/some-uuid/ticket2933/2933.patch) by @mwhansen created at 2008-04-15 17:40:47



---

archive/issue_comments_020205.json:
```json
{
    "body": "I find the business with isinstance(str) strange, but it looks right and the doctests assert the correct behaviour.",
    "created_at": "2008-04-17T05:17:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2933",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2933#issuecomment-20205",
    "user": "@ncalexan"
}
```

I find the business with isinstance(str) strange, but it looks right and the doctests assert the correct behaviour.



---

archive/issue_comments_020206.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-17T06:11:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2933",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2933#issuecomment-20206",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_020207.json:
```json
{
    "body": "Merged in Sage 3.0.alpha6",
    "created_at": "2008-04-17T06:11:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2933",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2933#issuecomment-20207",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.alpha6
