# Issue 3849: notebook -- Internal Server Error given when input to File upload or Data attachment is invalid

archive/issues_003849.json:
```json
{
    "body": "Assignee: boothby\n\n(1) In Google Docs if one fills in both \"Browse your computer ...\" and \"Or enter the url of a ...\", the server just deals with the first input box. The Notebook instead deals with the second. Do what Google does.\n\n(2) Google uses JavaScript alert boxes to report errors. The Notebook just gives a \"Internal Server Error.\" The Notebook should do inline error reporting just as is done on the Registration page.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3849\n\n",
    "created_at": "2008-08-14T12:54:59Z",
    "labels": [
        "component: notebook",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3",
    "title": "notebook -- Internal Server Error given when input to File upload or Data attachment is invalid",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3849",
    "user": "https://trac.sagemath.org/admin/accounts/users/TimothyClemans"
}
```
Assignee: boothby

(1) In Google Docs if one fills in both "Browse your computer ..." and "Or enter the url of a ...", the server just deals with the first input box. The Notebook instead deals with the second. Do what Google does.

(2) Google uses JavaScript alert boxes to report errors. The Notebook just gives a "Internal Server Error." The Notebook should do inline error reporting just as is done on the Registration page.

Issue created by migration from https://trac.sagemath.org/ticket/3849





---

archive/issue_comments_027315.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-08-14T12:55:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3849",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3849#issuecomment-27315",
    "user": "https://trac.sagemath.org/admin/accounts/users/TimothyClemans"
}
```

Changing status from new to assigned.



---

archive/issue_comments_027316.json:
```json
{
    "body": "Changing assignee from boothby to TimothyClemans.",
    "created_at": "2008-08-14T12:55:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3849",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3849#issuecomment-27316",
    "user": "https://trac.sagemath.org/admin/accounts/users/TimothyClemans"
}
```

Changing assignee from boothby to TimothyClemans.



---

archive/issue_comments_027317.json:
```json
{
    "body": "Error reporting does exist for file extension errors. However, it is not inline.",
    "created_at": "2008-08-14T12:59:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3849",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3849#issuecomment-27317",
    "user": "https://trac.sagemath.org/admin/accounts/users/TimothyClemans"
}
```

Error reporting does exist for file extension errors. However, it is not inline.



---

archive/issue_comments_027318.json:
```json
{
    "body": "Attachment [sage-3844_1.patch](tarball://root/attachments/some-uuid/ticket3849/sage-3844_1.patch) by TimothyClemans created at 2008-08-14 13:30:09",
    "created_at": "2008-08-14T13:30:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3849",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3849#issuecomment-27318",
    "user": "https://trac.sagemath.org/admin/accounts/users/TimothyClemans"
}
```

Attachment [sage-3844_1.patch](tarball://root/attachments/some-uuid/ticket3849/sage-3844_1.patch) by TimothyClemans created at 2008-08-14 13:30:09



---

archive/issue_comments_027319.json:
```json
{
    "body": "Took care of (1) and also now clicking \"Upload Worksheet\" when form blank no longer displays \"Internal Server Error.\"",
    "created_at": "2008-08-14T13:32:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3849",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3849#issuecomment-27319",
    "user": "https://trac.sagemath.org/admin/accounts/users/TimothyClemans"
}
```

Took care of (1) and also now clicking "Upload Worksheet" when form blank no longer displays "Internal Server Error."



---

archive/issue_comments_027320.json:
```json
{
    "body": "Attachment [sage-3849_1.patch](tarball://root/attachments/some-uuid/ticket3849/sage-3849_1.patch) by @williamstein created at 2009-11-20 00:34:53\n\nForget about this code.  This is an important error though.\n\nThe attached patch sagenb_3849-part1.patch I think completely fixes all such problems for uploading a *worksheet*, but doesn't do anything about Data-->Upload or attach file.\n\nI'm making Data -->Upload or attach a file a new ticket: #7495",
    "created_at": "2009-11-20T00:34:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3849",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3849#issuecomment-27320",
    "user": "https://github.com/williamstein"
}
```

Attachment [sage-3849_1.patch](tarball://root/attachments/some-uuid/ticket3849/sage-3849_1.patch) by @williamstein created at 2009-11-20 00:34:53

Forget about this code.  This is an important error though.

The attached patch sagenb_3849-part1.patch I think completely fixes all such problems for uploading a *worksheet*, but doesn't do anything about Data-->Upload or attach file.

I'm making Data -->Upload or attach a file a new ticket: #7495



---

archive/issue_comments_027321.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-11-20T00:36:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3849",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3849#issuecomment-27321",
    "user": "https://github.com/williamstein"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_027322.json:
```json
{
    "body": "Attachment [sagenb_3849.patch](tarball://root/attachments/some-uuid/ticket3849/sagenb_3849.patch) by @williamstein created at 2009-11-20 00:36:56",
    "created_at": "2009-11-20T00:36:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3849",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3849#issuecomment-27322",
    "user": "https://github.com/williamstein"
}
```

Attachment [sagenb_3849.patch](tarball://root/attachments/some-uuid/ticket3849/sagenb_3849.patch) by @williamstein created at 2009-11-20 00:36:56



---

archive/issue_comments_027323.json:
```json
{
    "body": "Attachment [sagenb_3849.2.patch](tarball://root/attachments/some-uuid/ticket3849/sagenb_3849.2.patch) by @qed777 created at 2009-11-20 07:29:36\n\nVersion 2.  Added backlink.  Apply only this patch to the sagenb repo.",
    "created_at": "2009-11-20T07:29:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3849",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3849#issuecomment-27323",
    "user": "https://github.com/qed777"
}
```

Attachment [sagenb_3849.2.patch](tarball://root/attachments/some-uuid/ticket3849/sagenb_3849.2.patch) by @qed777 created at 2009-11-20 07:29:36

Version 2.  Added backlink.  Apply only this patch to the sagenb repo.



---

archive/issue_comments_027324.json:
```json
{
    "body": "Version 2:\n\n* Adds a link back to the upload page.\n* `sage-support` --> `sage-support group`.\n\nMy review, to the extent it counts, is positive.",
    "created_at": "2009-11-20T07:33:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3849",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3849#issuecomment-27324",
    "user": "https://github.com/qed777"
}
```

Version 2:

* Adds a link back to the upload page.
* `sage-support` --> `sage-support group`.

My review, to the extent it counts, is positive.



---

archive/issue_comments_027325.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-12-06T07:48:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3849",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3849#issuecomment-27325",
    "user": "https://github.com/TimDumol"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_027326.json:
```json
{
    "body": "Replying to [comment:7 mpatel]:\n> [...]\n> My review, to the extent it counts, is positive.\n\nI'm giving this a positive review. Everything works fine.",
    "created_at": "2009-12-06T07:48:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3849",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3849#issuecomment-27326",
    "user": "https://github.com/TimDumol"
}
```

Replying to [comment:7 mpatel]:
> [...]
> My review, to the extent it counts, is positive.

I'm giving this a positive review. Everything works fine.



---

archive/issue_comments_027327.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-12-08T05:29:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3849",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3849#issuecomment-27327",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_comments_027328.json:
```json
{
    "body": "merged into sage-4.3",
    "created_at": "2009-12-08T05:29:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3849",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3849#issuecomment-27328",
    "user": "https://github.com/williamstein"
}
```

merged into sage-4.3



---

archive/issue_events_008811.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2009-12-08T05:29:34Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3849",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3849#event-8811"
}
```
