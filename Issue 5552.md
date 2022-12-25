# Issue 5552: plot_slope_field typo

archive/issues_005552.json:
```json
{
    "body": "Assignee: @williamstein\n\n\n```\nplot_slope_field((f, g), (xvar, xmin, xmax), (yvar, ymin, ymax)) \n```\n\nshould only have one function, not the two functions left over from plot_vector_field\n\nIssue created by migration from https://trac.sagemath.org/ticket/5552\n\n",
    "created_at": "2009-03-17T20:45:26Z",
    "labels": [
        "component: graphics",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.1",
    "title": "plot_slope_field typo",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5552",
    "user": "https://github.com/kcrisman"
}
```
Assignee: @williamstein


```
plot_slope_field((f, g), (xvar, xmin, xmax), (yvar, ymin, ymax)) 
```

should only have one function, not the two functions left over from plot_vector_field

Issue created by migration from https://trac.sagemath.org/ticket/5552





---

archive/issue_comments_043104.json:
```json
{
    "body": "This is in the docs, not in the def, of course.",
    "created_at": "2009-03-17T20:51:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5552",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5552#issuecomment-43104",
    "user": "https://github.com/kcrisman"
}
```

This is in the docs, not in the def, of course.



---

archive/issue_comments_043105.json:
```json
{
    "body": "Attachment [slope_field_typo.patch](tarball://root/attachments/some-uuid/ticket5552/slope_field_typo.patch) by @kcrisman created at 2009-03-18 00:40:52",
    "created_at": "2009-03-18T00:40:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5552",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5552#issuecomment-43105",
    "user": "https://github.com/kcrisman"
}
```

Attachment [slope_field_typo.patch](tarball://root/attachments/some-uuid/ticket5552/slope_field_typo.patch) by @kcrisman created at 2009-03-18 00:40:52



---

archive/issue_comments_043106.json:
```json
{
    "body": "This looks correct.  Positive review.",
    "created_at": "2009-03-18T17:11:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5552",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5552#issuecomment-43106",
    "user": "https://github.com/jasongrout"
}
```

This looks correct.  Positive review.



---

archive/issue_comments_043107.json:
```json
{
    "body": "The patch cleanly applies as well.",
    "created_at": "2009-03-18T17:13:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5552",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5552#issuecomment-43107",
    "user": "https://github.com/jasongrout"
}
```

The patch cleanly applies as well.



---

archive/issue_comments_043108.json:
```json
{
    "body": "Merged in Sage 3.4.1.alpha0.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-23T21:26:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5552",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5552#issuecomment-43108",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.4.1.alpha0.

Cheers,

Michael



---

archive/issue_comments_043109.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-03-23T21:26:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5552",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5552#issuecomment-43109",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
