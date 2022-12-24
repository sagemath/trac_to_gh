# Issue 2703: make _fast_float_ work on inequality testing

archive/issues_002703.json:
```json
{
    "body": "Assignee: mabshoff\n\nIt would be really nice if this worked:\n\n\n```\nsage: var('x y')\nsage: f=x^2+y^2<=1\nsage: g=f._fast_float_('x','y')\nsage: g(1,2)\nFalse\nsage: g(0.5,0.5)\nTrue\n```\n\n\nHere is a toy implementation:\n\n\n```\ndef ff(func,*args):\n    g1 = func.left()._fast_float_(*args)\n    g2 = func.right()._fast_float_(*args)\n    oper = func.operator()\n    def ret(*sub_args):\n        return oper(g1(*sub_args), g2(*sub_args))\n    return ret\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2703\n\n",
    "created_at": "2008-03-28T17:29:54Z",
    "labels": [
        "Cygwin",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "make _fast_float_ work on inequality testing",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2703",
    "user": "@jasongrout"
}
```
Assignee: mabshoff

It would be really nice if this worked:


```
sage: var('x y')
sage: f=x^2+y^2<=1
sage: g=f._fast_float_('x','y')
sage: g(1,2)
False
sage: g(0.5,0.5)
True
```


Here is a toy implementation:


```
def ff(func,*args):
    g1 = func.left()._fast_float_(*args)
    g2 = func.right()._fast_float_(*args)
    oper = func.operator()
    def ret(*sub_args):
        return oper(g1(*sub_args), g2(*sub_args))
    return ret
```



Issue created by migration from https://trac.sagemath.org/ticket/2703





---

archive/issue_comments_018643.json:
```json
{
    "body": "Changing assignee from mabshoff to @williamstein.",
    "created_at": "2008-03-28T18:06:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2703",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2703#issuecomment-18643",
    "user": "mabshoff"
}
```

Changing assignee from mabshoff to @williamstein.



---

archive/issue_comments_018644.json:
```json
{
    "body": "Changing component from Cygwin to calculus.",
    "created_at": "2008-03-28T18:06:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2703",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2703#issuecomment-18644",
    "user": "mabshoff"
}
```

Changing component from Cygwin to calculus.



---

archive/issue_comments_018645.json:
```json
{
    "body": "This looks like a near duplicate of #2768, where it was decided that this functionality was a bad idea.  See comment by robertwb.",
    "created_at": "2008-09-01T15:22:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2703",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2703#issuecomment-18645",
    "user": "@jicama"
}
```

This looks like a near duplicate of #2768, where it was decided that this functionality was a bad idea.  See comment by robertwb.



---

archive/issue_comments_018646.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2008-09-02T10:18:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2703",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2703#issuecomment-18646",
    "user": "mabshoff"
}
```

Resolution: invalid



---

archive/issue_comments_018647.json:
```json
{
    "body": "Thanks Jason,\n\nthis is invalid - another ticket gone :)\n\nCheers,\n\nMichael",
    "created_at": "2008-09-02T10:18:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2703",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2703#issuecomment-18647",
    "user": "mabshoff"
}
```

Thanks Jason,

this is invalid - another ticket gone :)

Cheers,

Michael
