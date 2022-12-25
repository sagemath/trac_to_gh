# Issue 7768: PDF version of reference manual fails to build in Sage 4.3

archive/issues_007768.json:
```json
{
    "body": "Assignee: mvngu\n\nKeywords: reference manual\n\nWith Sage 4.3, building the PDF version of the reference manual hangs at the line:\n\n```\n! Missing $ inserted.\n<inserted text> \n                $\nl.164972 $\\mbox{min_bound} \n                           \\leq \\mbox{linear_function} \\leq \\mbox{max_bound}$\n```\n\nThis is due to the docstring of the method `constraints()` in `sage/numerical/mip.pyx`. The attached patch should fix the docstring formatting and allow the PDF version of the reference manual to build successfully.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7768\n\n",
    "created_at": "2009-12-26T13:33:58Z",
    "labels": [
        "component: documentation",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.1",
    "title": "PDF version of reference manual fails to build in Sage 4.3",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7768",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```
Assignee: mvngu

Keywords: reference manual

With Sage 4.3, building the PDF version of the reference manual hangs at the line:

```
! Missing $ inserted.
<inserted text> 
                $
l.164972 $\mbox{min_bound} 
                           \leq \mbox{linear_function} \leq \mbox{max_bound}$
```

This is due to the docstring of the method `constraints()` in `sage/numerical/mip.pyx`. The attached patch should fix the docstring formatting and allow the PDF version of the reference manual to build successfully.

Issue created by migration from https://trac.sagemath.org/ticket/7768





---

archive/issue_comments_066844.json:
```json
{
    "body": "Attachment [trac_7768-doc.patch](tarball://root/attachments/some-uuid/ticket7768/trac_7768-doc.patch) by mvngu created at 2009-12-26 13:38:23\n\nbased on Sage 4.3",
    "created_at": "2009-12-26T13:38:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7768",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7768#issuecomment-66844",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Attachment [trac_7768-doc.patch](tarball://root/attachments/some-uuid/ticket7768/trac_7768-doc.patch) by mvngu created at 2009-12-26 13:38:23

based on Sage 4.3



---

archive/issue_comments_066845.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-12-26T13:38:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7768",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7768#issuecomment-66845",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_066846.json:
```json
{
    "body": "Without the patch, the PDF build crashes.  With the patch it succeeds.  Both the PDF and html versions look good with the patch.",
    "created_at": "2009-12-26T16:17:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7768",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7768#issuecomment-66846",
    "user": "https://github.com/jhpalmieri"
}
```

Without the patch, the PDF build crashes.  With the patch it succeeds.  Both the PDF and html versions look good with the patch.



---

archive/issue_comments_066847.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-12-26T16:17:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7768",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7768#issuecomment-66847",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_007983.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2010-01-03T21:24:04Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7768",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7768#event-7983"
}
```



---

archive/issue_comments_066848.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-03T21:24:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7768",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7768#issuecomment-66848",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed
