# Issue 3880: Bad behavior of arrows

archive/issues_003880.json:
```json
{
    "body": "Assignee: @williamstein\n\nAccording to the arrow documentation,\n\n```\nAn arrow from (xmin, ymin) to (xmax, ymax).\n```\n\n\nHowever, the current behavior is an arrow from (xmin, ymin) to (xmin + xmax, ymin + ymax).\n\nFor example:\n\n```\nsage: arrow((1, 1), (-1,-1))\n```\n\nwill draw an arrow from (1,1) to (0,0).\n\nIssue created by migration from https://trac.sagemath.org/ticket/3880\n\n",
    "created_at": "2008-08-16T19:22:55Z",
    "labels": [
        "graphics",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.2",
    "title": "Bad behavior of arrows",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3880",
    "user": "@itolkov"
}
```
Assignee: @williamstein

According to the arrow documentation,

```
An arrow from (xmin, ymin) to (xmax, ymax).
```


However, the current behavior is an arrow from (xmin, ymin) to (xmin + xmax, ymin + ymax).

For example:

```
sage: arrow((1, 1), (-1,-1))
```

will draw an arrow from (1,1) to (0,0).

Issue created by migration from https://trac.sagemath.org/ticket/3880





---

archive/issue_comments_027680.json:
```json
{
    "body": "According to the docs on matplotlib:\n\n> patches.FancyArrow(x, y, dx, dy, ...\n\nFixing the line where this constructor is called should solve the problem.",
    "created_at": "2008-08-16T19:25:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3880",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3880#issuecomment-27680",
    "user": "@itolkov"
}
```

According to the docs on matplotlib:

> patches.FancyArrow(x, y, dx, dy, ...

Fixing the line where this constructor is called should solve the problem.



---

archive/issue_comments_027681.json:
```json
{
    "body": "This should be taken care of at the same time as #3877.",
    "created_at": "2008-08-18T23:47:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3880",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3880#issuecomment-27681",
    "user": "@rlmill"
}
```

This should be taken care of at the same time as #3877.



---

archive/issue_comments_027682.json:
```json
{
    "body": "Jason is right, this is orthogonal to #3877. Shame on Alex for using such a stupid syntax as (xmin, ymin) to denote the tail coordinates of an arrow.",
    "created_at": "2008-08-19T01:22:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3880",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3880#issuecomment-27682",
    "user": "@rlmill"
}
```

Jason is right, this is orthogonal to #3877. Shame on Alex for using such a stupid syntax as (xmin, ymin) to denote the tail coordinates of an arrow.



---

archive/issue_comments_027683.json:
```json
{
    "body": "Attachment [trac_3880-arrows.patch](tarball://root/attachments/some-uuid/ticket3880/trac_3880-arrows.patch) by @rlmill created at 2008-08-19 01:28:41",
    "created_at": "2008-08-19T01:28:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3880",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3880#issuecomment-27683",
    "user": "@rlmill"
}
```

Attachment [trac_3880-arrows.patch](tarball://root/attachments/some-uuid/ticket3880/trac_3880-arrows.patch) by @rlmill created at 2008-08-19 01:28:41



---

archive/issue_comments_027684.json:
```json
{
    "body": "Patch looks good to me. Rlm explained to me what needed fixing.\n\nCheers,\n\nMichael",
    "created_at": "2008-08-19T01:39:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3880",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3880#issuecomment-27684",
    "user": "mabshoff"
}
```

Patch looks good to me. Rlm explained to me what needed fixing.

Cheers,

Michael



---

archive/issue_comments_027685.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-19T02:03:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3880",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3880#issuecomment-27685",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_027686.json:
```json
{
    "body": "Merged in Sage 3.1.2.alpha0",
    "created_at": "2008-08-19T02:03:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3880",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3880#issuecomment-27686",
    "user": "mabshoff"
}
```

Merged in Sage 3.1.2.alpha0



---

archive/issue_comments_027687.json:
```json
{
    "body": "Attachment [trac_3880_referee.patch](tarball://root/attachments/some-uuid/ticket3880/trac_3880_referee.patch) by mabshoff created at 2008-08-19 02:32:21",
    "created_at": "2008-08-19T02:32:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3880",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3880#issuecomment-27687",
    "user": "mabshoff"
}
```

Attachment [trac_3880_referee.patch](tarball://root/attachments/some-uuid/ticket3880/trac_3880_referee.patch) by mabshoff created at 2008-08-19 02:32:21
