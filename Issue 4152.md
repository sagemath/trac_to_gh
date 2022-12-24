# Issue 4152: parametric_plot should take the variable range as (var, min, max) like plot

archive/issues_004152.json:
```json
{
    "body": "Assignee: was\n\nThis should work to be consistent with plot:\n\n\n```\nsage: parametric_plot((2*x, x^2+1), (x,0,1))\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n\n/home/grout/<ipython console> in <module>()\n\nTypeError: parametric_plot() takes exactly 3 arguments (2 given)\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4152\n\n",
    "created_at": "2008-09-19T16:35:56Z",
    "labels": [
        "graphics",
        "major",
        "bug"
    ],
    "title": "parametric_plot should take the variable range as (var, min, max) like plot",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4152",
    "user": "jason"
}
```
Assignee: was

This should work to be consistent with plot:


```
sage: parametric_plot((2*x, x^2+1), (x,0,1))
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/grout/<ipython console> in <module>()

TypeError: parametric_plot() takes exactly 3 arguments (2 given)
```



Issue created by migration from https://trac.sagemath.org/ticket/4152





---

archive/issue_comments_030149.json:
```json
{
    "body": "This was also mentioned in #2410, but was not a fundamental part of that ticket.",
    "created_at": "2008-09-19T19:20:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4152",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4152#issuecomment-30149",
    "user": "jason"
}
```

This was also mentioned in #2410, but was not a fundamental part of that ticket.



---

archive/issue_comments_030150.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-01-22T08:27:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4152",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4152#issuecomment-30150",
    "user": "mhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_030151.json:
```json
{
    "body": "Attachment [trac_4152.patch](tarball://root/attachments/some-uuid/ticket4152/trac_4152.patch) by mhansen created at 2009-01-22 08:27:42",
    "created_at": "2009-01-22T08:27:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4152",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4152#issuecomment-30151",
    "user": "mhansen"
}
```

Attachment [trac_4152.patch](tarball://root/attachments/some-uuid/ticket4152/trac_4152.patch) by mhansen created at 2009-01-22 08:27:42



---

archive/issue_comments_030152.json:
```json
{
    "body": "Changing assignee from was to mhansen.",
    "created_at": "2009-01-22T08:27:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4152",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4152#issuecomment-30152",
    "user": "mhansen"
}
```

Changing assignee from was to mhansen.



---

archive/issue_comments_030153.json:
```json
{
    "body": "apply on top of previous patch",
    "created_at": "2009-01-22T14:20:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4152",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4152#issuecomment-30153",
    "user": "jason"
}
```

apply on top of previous patch



---

archive/issue_comments_030154.json:
```json
{
    "body": "Attachment [trac_4152-docs-dispatch.patch](tarball://root/attachments/some-uuid/ticket4152/trac_4152-docs-dispatch.patch) by jason created at 2009-01-22 14:20:59\n\npositive review for mhansen's patch.  My patch further adds to the documentation and makes the parametric plot function dispatch the 3d version when needed.  My patch needs to be reviewed.",
    "created_at": "2009-01-22T14:20:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4152",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4152#issuecomment-30154",
    "user": "jason"
}
```

Attachment [trac_4152-docs-dispatch.patch](tarball://root/attachments/some-uuid/ticket4152/trac_4152-docs-dispatch.patch) by jason created at 2009-01-22 14:20:59

positive review for mhansen's patch.  My patch further adds to the documentation and makes the parametric plot function dispatch the 3d version when needed.  My patch needs to be reviewed.



---

archive/issue_comments_030155.json:
```json
{
    "body": "Positive review for Jason's part.",
    "created_at": "2009-01-22T14:31:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4152",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4152#issuecomment-30155",
    "user": "mhansen"
}
```

Positive review for Jason's part.



---

archive/issue_comments_030156.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-23T10:02:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4152",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4152#issuecomment-30156",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_030157.json:
```json
{
    "body": "Merged both patches in Sage 3.3.alpha0\n\nCheers,\n\nMichael",
    "created_at": "2009-01-23T10:02:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4152",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4152#issuecomment-30157",
    "user": "mabshoff"
}
```

Merged both patches in Sage 3.3.alpha0

Cheers,

Michael
