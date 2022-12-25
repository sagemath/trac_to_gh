# Issue 5266: plot_vector_field does not plot the end of the range when given plot_points argument

archive/issues_005266.json:
```json
{
    "body": "Assignee: @williamstein\n\n\n```\nvar('x,y')\nplot_vector_field( (-1,y), (x, -1, 1), (y, -1, 1), plot_points=4)\n```\n\n\npicks the 4 points at x=-1, -0.5,0, and 0.5, but doesn't get x=1!  The points it should pick are x=-1, -1/3, 1/3, and 1 (so we hit the end of the x-range).  The same applies to y.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5266\n\n",
    "created_at": "2009-02-14T10:22:25Z",
    "labels": [
        "component: graphics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "plot_vector_field does not plot the end of the range when given plot_points argument",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5266",
    "user": "https://github.com/jasongrout"
}
```
Assignee: @williamstein


```
var('x,y')
plot_vector_field( (-1,y), (x, -1, 1), (y, -1, 1), plot_points=4)
```


picks the 4 points at x=-1, -0.5,0, and 0.5, but doesn't get x=1!  The points it should pick are x=-1, -1/3, 1/3, and 1 (so we hit the end of the x-range).  The same applies to y.


Issue created by migration from https://trac.sagemath.org/ticket/5266





---

archive/issue_comments_040346.json:
```json
{
    "body": "Changing assignee from @williamstein to @jasongrout.",
    "created_at": "2009-02-14T11:00:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5266",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5266#issuecomment-40346",
    "user": "https://github.com/jasongrout"
}
```

Changing assignee from @williamstein to @jasongrout.



---

archive/issue_comments_040347.json:
```json
{
    "body": "Attachment [trac_5266-plotting-fencepost-error.patch](tarball://root/attachments/some-uuid/ticket5266/trac_5266-plotting-fencepost-error.patch) by @jasongrout created at 2009-02-14 11:00:09",
    "created_at": "2009-02-14T11:00:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5266",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5266#issuecomment-40347",
    "user": "https://github.com/jasongrout"
}
```

Attachment [trac_5266-plotting-fencepost-error.patch](tarball://root/attachments/some-uuid/ticket5266/trac_5266-plotting-fencepost-error.patch) by @jasongrout created at 2009-02-14 11:00:09



---

archive/issue_comments_040348.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-02-14T11:00:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5266",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5266#issuecomment-40348",
    "user": "https://github.com/jasongrout"
}
```

Changing status from new to assigned.



---

archive/issue_comments_040349.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2009-02-14T11:00:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5266",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5266#issuecomment-40349",
    "user": "https://github.com/jasongrout"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_040350.json:
```json
{
    "body": "mabshoff said to make this a blocker...",
    "created_at": "2009-02-14T11:00:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5266",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5266#issuecomment-40350",
    "user": "https://github.com/jasongrout"
}
```

mabshoff said to make this a blocker...



---

archive/issue_comments_040351.json:
```json
{
    "body": "All doctests pass with the patch applied, so now we need a formal review for this one.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-14T13:46:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5266",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5266#issuecomment-40351",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

All doctests pass with the patch applied, so now we need a formal review for this one.

Cheers,

Michael



---

archive/issue_comments_040352.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2009-02-14T14:13:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5266",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5266#issuecomment-40352",
    "user": "https://github.com/mwhansen"
}
```

Looks good to me.



---

archive/issue_comments_040353.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-14T16:09:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5266",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5266#issuecomment-40353",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_040354.json:
```json
{
    "body": "Merged in Sage 3.3.rc1.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-14T16:09:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5266",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5266#issuecomment-40354",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.3.rc1.

Cheers,

Michael



---

archive/issue_events_005522.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-02-14T16:09:22Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5266",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5266#event-5522"
}
```
