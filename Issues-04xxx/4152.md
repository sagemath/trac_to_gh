# Issue 4152: [with patch, positive review] parametric_plot should take the variable range as (var, min, max) like plot

archive/issues_004152.json:
```json
{
    "body": "Assignee: @mwhansen\n\nThis should work to be consistent with plot:\n\n```\nsage: parametric_plot((2*x, x^2+1), (x,0,1))\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n\n/home/grout/<ipython console> in <module>()\n\nTypeError: parametric_plot() takes exactly 3 arguments (2 given)\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4152\n\n",
    "closed_at": "2009-01-23T10:02:01Z",
    "created_at": "2008-09-19T16:35:56Z",
    "labels": [
        "component: graphics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "[with patch, positive review] parametric_plot should take the variable range as (var, min, max) like plot",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4152",
    "user": "https://github.com/jasongrout"
}
```
Assignee: @mwhansen

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

archive/issue_comments_030088.json:
```json
{
    "body": "This was also mentioned in #2410, but was not a fundamental part of that ticket.",
    "created_at": "2008-09-19T19:20:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4152",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4152#issuecomment-30088",
    "user": "https://github.com/jasongrout"
}
```

This was also mentioned in #2410, but was not a fundamental part of that ticket.



---

archive/issue_comments_030089.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-01-22T08:27:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4152",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4152#issuecomment-30089",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_030090.json:
```json
{
    "body": "Attachment [trac_4152.patch](tarball://root/attachments/some-uuid/ticket4152/trac_4152.patch) by @mwhansen created at 2009-01-22 08:27:42",
    "created_at": "2009-01-22T08:27:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4152",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4152#issuecomment-30090",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac_4152.patch](tarball://root/attachments/some-uuid/ticket4152/trac_4152.patch) by @mwhansen created at 2009-01-22 08:27:42



---

archive/issue_comments_030091.json:
```json
{
    "body": "Changing assignee from @williamstein to @mwhansen.",
    "created_at": "2009-01-22T08:27:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4152",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4152#issuecomment-30091",
    "user": "https://github.com/mwhansen"
}
```

Changing assignee from @williamstein to @mwhansen.



---

archive/issue_comments_030092.json:
```json
{
    "body": "apply on top of previous patch",
    "created_at": "2009-01-22T14:20:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4152",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4152#issuecomment-30092",
    "user": "https://github.com/jasongrout"
}
```

apply on top of previous patch



---

archive/issue_comments_030093.json:
```json
{
    "body": "Attachment [trac_4152-docs-dispatch.patch](tarball://root/attachments/some-uuid/ticket4152/trac_4152-docs-dispatch.patch) by @jasongrout created at 2009-01-22 14:20:59\n\npositive review for mhansen's patch.  My patch further adds to the documentation and makes the parametric plot function dispatch the 3d version when needed.  My patch needs to be reviewed.",
    "created_at": "2009-01-22T14:20:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4152",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4152#issuecomment-30093",
    "user": "https://github.com/jasongrout"
}
```

Attachment [trac_4152-docs-dispatch.patch](tarball://root/attachments/some-uuid/ticket4152/trac_4152-docs-dispatch.patch) by @jasongrout created at 2009-01-22 14:20:59

positive review for mhansen's patch.  My patch further adds to the documentation and makes the parametric plot function dispatch the 3d version when needed.  My patch needs to be reviewed.



---

archive/issue_comments_030094.json:
```json
{
    "body": "Positive review for Jason's part.",
    "created_at": "2009-01-22T14:31:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4152",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4152#issuecomment-30094",
    "user": "https://github.com/mwhansen"
}
```

Positive review for Jason's part.



---

archive/issue_comments_030095.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-23T10:02:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4152",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4152#issuecomment-30095",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_030096.json:
```json
{
    "body": "Merged both patches in Sage 3.3.alpha0\n\nCheers,\n\nMichael",
    "created_at": "2009-01-23T10:02:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4152",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4152#issuecomment-30096",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged both patches in Sage 3.3.alpha0

Cheers,

Michael



---

archive/issue_events_009443.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-01-23T10:02:01Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4152",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4152#event-9443"
}
```



---

archive/issue_events_009444.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-01-23T10:02:01Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4152",
    "milestone": "sage-3.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4152#event-9444"
}
```
