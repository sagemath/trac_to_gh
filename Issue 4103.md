# Issue 4103: Delete the cmap option for vector field plots

archive/issues_004103.json:
```json
{
    "body": "Assignee: @williamstein\n\nThe cmap argument for vector field plots is not used.  Does anyone know why it's there?  I don't think it's even valid matplotlib code.\n\nThis patch deletes the option.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4103\n\n",
    "created_at": "2008-09-12T04:03:03Z",
    "labels": [
        "component: graphics",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.3",
    "title": "Delete the cmap option for vector field plots",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4103",
    "user": "https://github.com/jasongrout"
}
```
Assignee: @williamstein

The cmap argument for vector field plots is not used.  Does anyone know why it's there?  I don't think it's even valid matplotlib code.

This patch deletes the option.

Issue created by migration from https://trac.sagemath.org/ticket/4103





---

archive/issue_comments_029654.json:
```json
{
    "body": "Attachment [plot_vector_field_cmap.patch](tarball://root/attachments/some-uuid/ticket4103/plot_vector_field_cmap.patch) by @jasongrout created at 2008-09-12 04:14:00",
    "created_at": "2008-09-12T04:14:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4103",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4103#issuecomment-29654",
    "user": "https://github.com/jasongrout"
}
```

Attachment [plot_vector_field_cmap.patch](tarball://root/attachments/some-uuid/ticket4103/plot_vector_field_cmap.patch) by @jasongrout created at 2008-09-12 04:14:00



---

archive/issue_comments_029655.json:
```json
{
    "body": "Patch looks good to me. Assuming it passes doctests (which are running now) this is a positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-19T02:22:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4103",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4103#issuecomment-29655",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Patch looks good to me. Assuming it passes doctests (which are running now) this is a positive review.

Cheers,

Michael



---

archive/issue_comments_029656.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-19T03:13:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4103",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4103#issuecomment-29656",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_029657.json:
```json
{
    "body": "Merged in Sage 3.1.3.alpha0",
    "created_at": "2008-09-19T03:13:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4103",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4103#issuecomment-29657",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.1.3.alpha0
