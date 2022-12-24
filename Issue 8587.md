# Issue 8587: get rid of annoying warning in vector_space_dimension()

archive/issues_008587.json:
```json
{
    "body": "Assignee: malb\n\nCC:  burcin polybori\n\nWe pass a Groebner basis to `vdim()` of Singular but forgot to mention it to Singular.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8587\n\n",
    "created_at": "2010-03-23T13:46:54Z",
    "labels": [
        "commutative algebra",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.2",
    "title": "get rid of annoying warning in vector_space_dimension()",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8587",
    "user": "malb"
}
```
Assignee: malb

CC:  burcin polybori

We pass a Groebner basis to `vdim()` of Singular but forgot to mention it to Singular.

Issue created by migration from https://trac.sagemath.org/ticket/8587





---

archive/issue_comments_077767.json:
```json
{
    "body": "Attachment [vdim_warning.patch](tarball://root/attachments/some-uuid/ticket8587/vdim_warning.patch) by malb created at 2010-03-23 13:47:28",
    "created_at": "2010-03-23T13:47:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8587",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8587#issuecomment-77767",
    "user": "malb"
}
```

Attachment [vdim_warning.patch](tarball://root/attachments/some-uuid/ticket8587/vdim_warning.patch) by malb created at 2010-03-23 13:47:28



---

archive/issue_comments_077768.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-03-23T13:47:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8587",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8587#issuecomment-77768",
    "user": "malb"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_077769.json:
```json
{
    "body": "Looks good to me.\n\nAFAICT, the message is printed to stderr, so there is no easy way to test this.",
    "created_at": "2010-05-04T21:30:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8587",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8587#issuecomment-77769",
    "user": "burcin"
}
```

Looks good to me.

AFAICT, the message is printed to stderr, so there is no easy way to test this.



---

archive/issue_comments_077770.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-05-04T21:30:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8587",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8587#issuecomment-77770",
    "user": "burcin"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_077771.json:
```json
{
    "body": "apply only this patch",
    "created_at": "2010-05-04T21:32:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8587",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8587#issuecomment-77771",
    "user": "burcin"
}
```

apply only this patch



---

archive/issue_comments_077772.json:
```json
{
    "body": "Attachment [trac_8587-vdim_warning.patch](tarball://root/attachments/some-uuid/ticket8587/trac_8587-vdim_warning.patch) by burcin created at 2010-05-04 21:33:26\n\nattachment:trac_8587-vdim_warning.patch adds the ticket number in the log message.",
    "created_at": "2010-05-04T21:33:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8587",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8587#issuecomment-77772",
    "user": "burcin"
}
```

Attachment [trac_8587-vdim_warning.patch](tarball://root/attachments/some-uuid/ticket8587/trac_8587-vdim_warning.patch) by burcin created at 2010-05-04 21:33:26

attachment:trac_8587-vdim_warning.patch adds the ticket number in the log message.



---

archive/issue_comments_077773.json:
```json
{
    "body": "Merged [trac_8587-vdim_warning.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8587/trac_8587-vdim_warning.patch).",
    "created_at": "2010-05-08T21:46:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8587",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8587#issuecomment-77773",
    "user": "mvngu"
}
```

Merged [trac_8587-vdim_warning.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8587/trac_8587-vdim_warning.patch).



---

archive/issue_comments_077774.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-05-08T21:46:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8587",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8587#issuecomment-77774",
    "user": "mvngu"
}
```

Resolution: fixed
