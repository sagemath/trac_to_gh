# Issue 8587: get rid of annoying warning in vector_space_dimension()

archive/issues_008587.json:
```json
{
    "body": "Assignee: @malb\n\nCC:  @burcin polybori\n\nWe pass a Groebner basis to `vdim()` of Singular but forgot to mention it to Singular.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8587\n\n",
    "closed_at": "2010-05-08T21:46:13Z",
    "created_at": "2010-03-23T13:46:54Z",
    "labels": [
        "component: commutative algebra",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.2",
    "title": "get rid of annoying warning in vector_space_dimension()",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8587",
    "user": "https://github.com/malb"
}
```
Assignee: @malb

CC:  @burcin polybori

We pass a Groebner basis to `vdim()` of Singular but forgot to mention it to Singular.

Issue created by migration from https://trac.sagemath.org/ticket/8587





---

archive/issue_comments_077639.json:
```json
{
    "body": "Attachment [vdim_warning.patch](tarball://root/attachments/some-uuid/ticket8587/vdim_warning.patch) by @malb created at 2010-03-23 13:47:28",
    "created_at": "2010-03-23T13:47:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8587",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8587#issuecomment-77639",
    "user": "https://github.com/malb"
}
```

Attachment [vdim_warning.patch](tarball://root/attachments/some-uuid/ticket8587/vdim_warning.patch) by @malb created at 2010-03-23 13:47:28



---

archive/issue_comments_077640.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-03-23T13:47:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8587",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8587#issuecomment-77640",
    "user": "https://github.com/malb"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_077641.json:
```json
{
    "body": "Looks good to me.\n\nAFAICT, the message is printed to stderr, so there is no easy way to test this.",
    "created_at": "2010-05-04T21:30:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8587",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8587#issuecomment-77641",
    "user": "https://github.com/burcin"
}
```

Looks good to me.

AFAICT, the message is printed to stderr, so there is no easy way to test this.



---

archive/issue_comments_077642.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-05-04T21:30:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8587",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8587#issuecomment-77642",
    "user": "https://github.com/burcin"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_077643.json:
```json
{
    "body": "apply only this patch",
    "created_at": "2010-05-04T21:32:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8587",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8587#issuecomment-77643",
    "user": "https://github.com/burcin"
}
```

apply only this patch



---

archive/issue_comments_077644.json:
```json
{
    "body": "Attachment [trac_8587-vdim_warning.patch](tarball://root/attachments/some-uuid/ticket8587/trac_8587-vdim_warning.patch) by @burcin created at 2010-05-04 21:33:26\n\nattachment:trac_8587-vdim_warning.patch adds the ticket number in the log message.",
    "created_at": "2010-05-04T21:33:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8587",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8587#issuecomment-77644",
    "user": "https://github.com/burcin"
}
```

Attachment [trac_8587-vdim_warning.patch](tarball://root/attachments/some-uuid/ticket8587/trac_8587-vdim_warning.patch) by @burcin created at 2010-05-04 21:33:26

attachment:trac_8587-vdim_warning.patch adds the ticket number in the log message.



---

archive/issue_comments_077645.json:
```json
{
    "body": "Merged [trac_8587-vdim_warning.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8587/trac_8587-vdim_warning.patch).",
    "created_at": "2010-05-08T21:46:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8587",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8587#issuecomment-77645",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Merged [trac_8587-vdim_warning.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8587/trac_8587-vdim_warning.patch).



---

archive/issue_comments_077646.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-05-08T21:46:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8587",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8587#issuecomment-77646",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_events_020746.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2010-05-08T21:46:13Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8587",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8587#event-20746"
}
```
