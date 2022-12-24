# Issue 645: multi-argument call for symbolic expressions

archive/issues_000645.json:
```json
{
    "body": "Assignee: was\n\n\n```\nsage: x,y = var('x y')\nsage: f(3)\ny + 3\nsage: f(3)(4)\n7\nsage: f(3,4)\n---------------------------------------------------------------------------\n<type 'exceptions.TypeError'>             Traceback (most recent call last)\n\n/Users/robert/sage/sage-2.5/devel/sage-working/<ipython console> in <module>()\n\n<type 'exceptions.TypeError'>: __call__() takes at most 2 arguments (3 given)\nsage: \n\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/645\n\n",
    "created_at": "2007-09-12T21:32:07Z",
    "labels": [
        "calculus",
        "major",
        "enhancement"
    ],
    "title": "multi-argument call for symbolic expressions",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/645",
    "user": "robertwb"
}
```
Assignee: was


```
sage: x,y = var('x y')
sage: f(3)
y + 3
sage: f(3)(4)
7
sage: f(3,4)
---------------------------------------------------------------------------
<type 'exceptions.TypeError'>             Traceback (most recent call last)

/Users/robert/sage/sage-2.5/devel/sage-working/<ipython console> in <module>()

<type 'exceptions.TypeError'>: __call__() takes at most 2 arguments (3 given)
sage: 

```


Issue created by migration from https://trac.sagemath.org/ticket/645





---

archive/issue_comments_003346.json:
```json
{
    "body": "Changing assignee from was to mhansen.",
    "created_at": "2007-11-30T23:24:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/645",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/645#issuecomment-3346",
    "user": "mhansen"
}
```

Changing assignee from was to mhansen.



---

archive/issue_comments_003347.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-11-30T23:24:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/645",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/645#issuecomment-3347",
    "user": "mhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_003348.json:
```json
{
    "body": "Attachment [645.patch](tarball://root/attachments/some-uuid/ticket645/645.patch) by mhansen created at 2007-11-30 23:25:01\n\nThis should be applied after #1345.",
    "created_at": "2007-11-30T23:25:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/645",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/645#issuecomment-3348",
    "user": "mhansen"
}
```

Attachment [645.patch](tarball://root/attachments/some-uuid/ticket645/645.patch) by mhansen created at 2007-11-30 23:25:01

This should be applied after #1345.



---

archive/issue_comments_003349.json:
```json
{
    "body": "Looks good to me, and doctests still pass in sage/calculus/*.",
    "created_at": "2007-12-01T02:57:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/645",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/645#issuecomment-3349",
    "user": "cwitty"
}
```

Looks good to me, and doctests still pass in sage/calculus/*.



---

archive/issue_comments_003350.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-01T11:16:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/645",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/645#issuecomment-3350",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_003351.json:
```json
{
    "body": "Merged in 2.8.15.alpha0.",
    "created_at": "2007-12-01T11:16:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/645",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/645#issuecomment-3351",
    "user": "mabshoff"
}
```

Merged in 2.8.15.alpha0.
