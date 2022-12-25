# Issue 2933: calculus -- substitution of a dict for SymbolicFunctionEvaluation is broken (but **kwds works)

archive/issues_002933.json:
```json
{
    "body": "Assignee: @williamstein\n\nSubstitution with a dictionary as input is broken.  Notice below in the\nthird input that the dictionary is ignored?!\n\n\n```\nsage: function('f',x)\nf(x)\nsage: (f(x)).substitute(f=log)\nlog(x)\nsage: (f(x)).substitute({f:log})\nf(x)\nsage: type(f(x))\n<class 'sage.calculus.calculus.SymbolicFunctionEvaluation'>\nsage: (x^3 + 1).substitute(x=5)\n126\nsage: (x^3 + 1).substitute({x:5})\n126\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2933\n\n",
    "created_at": "2008-04-15T15:02:46Z",
    "labels": [
        "component: calculus",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "calculus -- substitution of a dict for SymbolicFunctionEvaluation is broken (but **kwds works)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2933",
    "user": "https://github.com/williamstein"
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

archive/issue_comments_020160.json:
```json
{
    "body": "Changing assignee from @williamstein to @mwhansen.",
    "created_at": "2008-04-15T17:40:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2933",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2933#issuecomment-20160",
    "user": "https://github.com/mwhansen"
}
```

Changing assignee from @williamstein to @mwhansen.



---

archive/issue_comments_020161.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-04-15T17:40:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2933",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2933#issuecomment-20161",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_020162.json:
```json
{
    "body": "Attachment [2933.patch](tarball://root/attachments/some-uuid/ticket2933/2933.patch) by @mwhansen created at 2008-04-15 17:40:47",
    "created_at": "2008-04-15T17:40:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2933",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2933#issuecomment-20162",
    "user": "https://github.com/mwhansen"
}
```

Attachment [2933.patch](tarball://root/attachments/some-uuid/ticket2933/2933.patch) by @mwhansen created at 2008-04-15 17:40:47



---

archive/issue_comments_020163.json:
```json
{
    "body": "I find the business with isinstance(str) strange, but it looks right and the doctests assert the correct behaviour.",
    "created_at": "2008-04-17T05:17:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2933",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2933#issuecomment-20163",
    "user": "https://github.com/ncalexan"
}
```

I find the business with isinstance(str) strange, but it looks right and the doctests assert the correct behaviour.



---

archive/issue_comments_020164.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-17T06:11:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2933",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2933#issuecomment-20164",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_020165.json:
```json
{
    "body": "Merged in Sage 3.0.alpha6",
    "created_at": "2008-04-17T06:11:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2933",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2933#issuecomment-20165",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.alpha6
