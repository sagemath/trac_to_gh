# Issue 5266: plot_vector_field does not plot the end of the range when given plot_points argument

archive/issues_005266.json:
```json
{
    "body": "Assignee: @williamstein\n\n\n```\nvar('x,y')\nplot_vector_field( (-1,y), (x, -1, 1), (y, -1, 1), plot_points=4)\n```\n\n\npicks the 4 points at x=-1, -0.5,0, and 0.5, but doesn't get x=1!  The points it should pick are x=-1, -1/3, 1/3, and 1 (so we hit the end of the x-range).  The same applies to y.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5266\n\n",
    "created_at": "2009-02-14T10:22:25Z",
    "labels": [
        "graphics",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "plot_vector_field does not plot the end of the range when given plot_points argument",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5266",
    "user": "@jasongrout"
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

archive/issue_comments_040425.json:
```json
{
    "body": "Changing assignee from @williamstein to @jasongrout.",
    "created_at": "2009-02-14T11:00:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5266",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5266#issuecomment-40425",
    "user": "@jasongrout"
}
```

Changing assignee from @williamstein to @jasongrout.



---

archive/issue_comments_040426.json:
```json
{
    "body": "Attachment [trac_5266-plotting-fencepost-error.patch](tarball://root/attachments/some-uuid/ticket5266/trac_5266-plotting-fencepost-error.patch) by @jasongrout created at 2009-02-14 11:00:09",
    "created_at": "2009-02-14T11:00:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5266",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5266#issuecomment-40426",
    "user": "@jasongrout"
}
```

Attachment [trac_5266-plotting-fencepost-error.patch](tarball://root/attachments/some-uuid/ticket5266/trac_5266-plotting-fencepost-error.patch) by @jasongrout created at 2009-02-14 11:00:09



---

archive/issue_comments_040427.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-02-14T11:00:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5266",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5266#issuecomment-40427",
    "user": "@jasongrout"
}
```

Changing status from new to assigned.



---

archive/issue_comments_040428.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2009-02-14T11:00:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5266",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5266#issuecomment-40428",
    "user": "@jasongrout"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_040429.json:
```json
{
    "body": "mabshoff said to make this a blocker...",
    "created_at": "2009-02-14T11:00:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5266",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5266#issuecomment-40429",
    "user": "@jasongrout"
}
```

mabshoff said to make this a blocker...



---

archive/issue_comments_040430.json:
```json
{
    "body": "All doctests pass with the patch applied, so now we need a formal review for this one.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-14T13:46:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5266",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5266#issuecomment-40430",
    "user": "mabshoff"
}
```

All doctests pass with the patch applied, so now we need a formal review for this one.

Cheers,

Michael



---

archive/issue_comments_040431.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2009-02-14T14:13:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5266",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5266#issuecomment-40431",
    "user": "@mwhansen"
}
```

Looks good to me.



---

archive/issue_comments_040432.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-14T16:09:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5266",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5266#issuecomment-40432",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_040433.json:
```json
{
    "body": "Merged in Sage 3.3.rc1.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-14T16:09:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5266",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5266#issuecomment-40433",
    "user": "mabshoff"
}
```

Merged in Sage 3.3.rc1.

Cheers,

Michael
