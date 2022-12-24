# Issue 7768: PDF version of reference manual fails to build in Sage 4.3

archive/issues_007768.json:
```json
{
    "body": "Assignee: mvngu\n\nKeywords: reference manual\n\nWith Sage 4.3, building the PDF version of the reference manual hangs at the line:\n\n```\n! Missing $ inserted.\n<inserted text> \n                $\nl.164972 $\\mbox{min_bound} \n                           \\leq \\mbox{linear_function} \\leq \\mbox{max_bound}$\n```\n\nThis is due to the docstring of the method `constraints()` in `sage/numerical/mip.pyx`. The attached patch should fix the docstring formatting and allow the PDF version of the reference manual to build successfully.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7768\n\n",
    "created_at": "2009-12-26T13:33:58Z",
    "labels": [
        "documentation",
        "major",
        "bug"
    ],
    "title": "PDF version of reference manual fails to build in Sage 4.3",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7768",
    "user": "mvngu"
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

archive/issue_comments_066960.json:
```json
{
    "body": "Attachment [trac_7768-doc.patch](tarball://root/attachments/some-uuid/ticket7768/trac_7768-doc.patch) by mvngu created at 2009-12-26 13:38:23\n\nbased on Sage 4.3",
    "created_at": "2009-12-26T13:38:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7768",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7768#issuecomment-66960",
    "user": "mvngu"
}
```

Attachment [trac_7768-doc.patch](tarball://root/attachments/some-uuid/ticket7768/trac_7768-doc.patch) by mvngu created at 2009-12-26 13:38:23

based on Sage 4.3



---

archive/issue_comments_066961.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-12-26T13:38:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7768",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7768#issuecomment-66961",
    "user": "mvngu"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_066962.json:
```json
{
    "body": "Without the patch, the PDF build crashes.  With the patch it succeeds.  Both the PDF and html versions look good with the patch.",
    "created_at": "2009-12-26T16:17:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7768",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7768#issuecomment-66962",
    "user": "jhpalmieri"
}
```

Without the patch, the PDF build crashes.  With the patch it succeeds.  Both the PDF and html versions look good with the patch.



---

archive/issue_comments_066963.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-12-26T16:17:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7768",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7768#issuecomment-66963",
    "user": "jhpalmieri"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_066964.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-03T21:24:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7768",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7768#issuecomment-66964",
    "user": "mhansen"
}
```

Resolution: fixed
