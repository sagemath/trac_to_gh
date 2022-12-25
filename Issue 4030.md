# Issue 4030: Vectors of callable things should be callable

archive/issues_004030.json:
```json
{
    "body": "Assignee: tbd\n\nThe motivation here is being able to evaluate the gradient of a function at a point.\n\n\n```\nThe desired behavior is\n    sage: x, y = var('x, y')\n    sage: f = x^2 + y^2\n    sage: g = f.gradient()\n    sage: g(x=3,y=2)\n    (6,4)\n\nCurrently, however\n    sage: g(x=3,y=2)\n    Traceback (most recent call last):\n    ...\n    TypeError:\n    'sage.modules.free_module_element.FreeModuleElement_generic_dense'\n    object is not callable\n\nCalls should also work for a vector of callable symbolic expressions.\nNote that the gradient part will only work once #2547 is applied.\n    sage: f(x,y) = x^2 + y^2\n    sage: g = f.gradient()\n    sage: g(3,2)\n    (6,4)\n    sage: g(y=2,x=3)\n    (6,4)\n}}\n\nIssue created by migration from https://trac.sagemath.org/ticket/4030\n\n",
    "created_at": "2008-09-01T05:13:17Z",
    "labels": [
        "component: algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.2",
    "title": "Vectors of callable things should be callable",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4030",
    "user": "https://github.com/jicama"
}
```
Assignee: tbd

The motivation here is being able to evaluate the gradient of a function at a point.


```
The desired behavior is
    sage: x, y = var('x, y')
    sage: f = x^2 + y^2
    sage: g = f.gradient()
    sage: g(x=3,y=2)
    (6,4)

Currently, however
    sage: g(x=3,y=2)
    Traceback (most recent call last):
    ...
    TypeError:
    'sage.modules.free_module_element.FreeModuleElement_generic_dense'
    object is not callable

Calls should also work for a vector of callable symbolic expressions.
Note that the gradient part will only work once #2547 is applied.
    sage: f(x,y) = x^2 + y^2
    sage: g = f.gradient()
    sage: g(3,2)
    (6,4)
    sage: g(y=2,x=3)
    (6,4)
}}

Issue created by migration from https://trac.sagemath.org/ticket/4030





---

archive/issue_comments_029014.json:
```json
{
    "body": "Changing component from algebra to calculus.",
    "created_at": "2008-09-01T05:23:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4030",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4030#issuecomment-29014",
    "user": "https://github.com/jicama"
}
```

Changing component from algebra to calculus.



---

archive/issue_comments_029015.json:
```json
{
    "body": "Attachment [callable_vectors.patch](tarball://root/attachments/some-uuid/ticket4030/callable_vectors.patch) by @jicama created at 2008-09-01 05:23:47\n\nThe attached patch solves all the cases above except the last, which returns\n\n\n```\nsage: g(y=2,x=3)\nTraceback (most recent call last):\n...\nTypeError: __call__() got an unexpected keyword argument 'y'\n```\n\n\nNot sure what the deal is with that.\n\nThis patch should only be applied after #2547.",
    "created_at": "2008-09-01T05:23:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4030",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4030#issuecomment-29015",
    "user": "https://github.com/jicama"
}
```

Attachment [callable_vectors.patch](tarball://root/attachments/some-uuid/ticket4030/callable_vectors.patch) by @jicama created at 2008-09-01 05:23:47

The attached patch solves all the cases above except the last, which returns


```
sage: g(y=2,x=3)
Traceback (most recent call last):
...
TypeError: __call__() got an unexpected keyword argument 'y'
```


Not sure what the deal is with that.

This patch should only be applied after #2547.



---

archive/issue_comments_029016.json:
```json
{
    "body": "Changing assignee from tbd to @jicama.",
    "created_at": "2008-09-01T05:23:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4030",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4030#issuecomment-29016",
    "user": "https://github.com/jicama"
}
```

Changing assignee from tbd to @jicama.



---

archive/issue_comments_029017.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2008-09-01T06:30:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4030",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4030#issuecomment-29017",
    "user": "https://github.com/jicama"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_029018.json:
```json
{
    "body": "After applying #4031, the patch here gives the desired behavior.",
    "created_at": "2008-09-01T06:30:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4030",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4030#issuecomment-29018",
    "user": "https://github.com/jicama"
}
```

After applying #4031, the patch here gives the desired behavior.



---

archive/issue_comments_029019.json:
```json
{
    "body": "Jason,\n\nplease assign a milestone to new tickets. The next release is usually the right choice.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-01T12:25:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4030",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4030#issuecomment-29019",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Jason,

please assign a milestone to new tickets. The next release is usually the right choice.

Cheers,

Michael



---

archive/issue_comments_029020.json:
```json
{
    "body": "Looks good to me. Apply only after #4031.",
    "created_at": "2008-09-01T22:50:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4030",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4030#issuecomment-29020",
    "user": "https://github.com/mwhansen"
}
```

Looks good to me. Apply only after #4031.



---

archive/issue_comments_029021.json:
```json
{
    "body": "Just to be clear, both #2547 and #4031 should be applied before this patch.  The functionality doesn't depend on #2547, but the doctests do.",
    "created_at": "2008-09-01T23:19:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4030",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4030#issuecomment-29021",
    "user": "https://github.com/jicama"
}
```

Just to be clear, both #2547 and #4031 should be applied before this patch.  The functionality doesn't depend on #2547, but the doctests do.



---

archive/issue_comments_029022.json:
```json
{
    "body": "Merged in Sage 3.1.2.alpha4",
    "created_at": "2008-09-02T10:14:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4030",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4030#issuecomment-29022",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.1.2.alpha4



---

archive/issue_comments_029023.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-02T10:14:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4030",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4030#issuecomment-29023",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
