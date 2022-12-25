# Issue 6802: define a real variable with var()

archive/issues_006802.json:
```json
{
    "body": "Keywords: var(), real variable\n\nAt this [sage-support](http://groups.google.com/group/sage-support/browse_thread/thread/7bf451cf8202e085) thread, there is a request for `var()` to be able to define a \"real\" variable. Then one can do this\n\n```\nsage: a = var(\"a\")\nsage: conjugate(a)\na\n```\n\nAs of Sage 4.1.1, we have this:\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: a = var(\"a\")\nsage: conjugate(a)\nconjugate(a)\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6802\n\n",
    "created_at": "2009-08-22T10:49:16Z",
    "labels": [
        "component: symbolics"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "define a real variable with var()",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6802",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```
Keywords: var(), real variable

At this [sage-support](http://groups.google.com/group/sage-support/browse_thread/thread/7bf451cf8202e085) thread, there is a request for `var()` to be able to define a "real" variable. Then one can do this

```
sage: a = var("a")
sage: conjugate(a)
a
```

As of Sage 4.1.1, we have this:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: a = var("a")
sage: conjugate(a)
conjugate(a)
```


Issue created by migration from https://trac.sagemath.org/ticket/6802





---

archive/issue_comments_055909.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2009-08-22T14:18:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6802",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6802#issuecomment-55909",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: duplicate



---

archive/issue_comments_055910.json:
```json
{
    "body": "Closing this as a duplicate of #6559.",
    "created_at": "2009-08-22T14:18:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6802",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6802#issuecomment-55910",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Closing this as a duplicate of #6559.
