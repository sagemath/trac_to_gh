# Issue 3849: notebook -- Internal Server Error given when input to File upload or Data attachment is invalid

archive/issues_003849.json:
```json
{
    "body": "Assignee: boothby\n\n(1) In Google Docs if one fills in both \"Browse your computer ...\" and \"Or enter the url of a ...\", the server just deals with the first input box. The Notebook instead deals with the second. Do what Google does.\n\n(2) Google uses JavaScript alert boxes to report errors. The Notebook just gives a \"Internal Server Error.\" The Notebook should do inline error reporting just as is done on the Registration page.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3849\n\n",
    "created_at": "2008-08-14T12:54:59Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "title": "notebook -- Internal Server Error given when input to File upload or Data attachment is invalid",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3849",
    "user": "TimothyClemans"
}
```
Assignee: boothby

(1) In Google Docs if one fills in both "Browse your computer ..." and "Or enter the url of a ...", the server just deals with the first input box. The Notebook instead deals with the second. Do what Google does.

(2) Google uses JavaScript alert boxes to report errors. The Notebook just gives a "Internal Server Error." The Notebook should do inline error reporting just as is done on the Registration page.

Issue created by migration from https://trac.sagemath.org/ticket/3849





---

archive/issue_comments_027373.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-08-14T12:55:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3849",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3849#issuecomment-27373",
    "user": "TimothyClemans"
}
```

Changing status from new to assigned.



---

archive/issue_comments_027374.json:
```json
{
    "body": "Changing assignee from boothby to TimothyClemans.",
    "created_at": "2008-08-14T12:55:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3849",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3849#issuecomment-27374",
    "user": "TimothyClemans"
}
```

Changing assignee from boothby to TimothyClemans.



---

archive/issue_comments_027375.json:
```json
{
    "body": "Error reporting does exist for file extension errors. However, it is not inline.",
    "created_at": "2008-08-14T12:59:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3849",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3849#issuecomment-27375",
    "user": "TimothyClemans"
}
```

Error reporting does exist for file extension errors. However, it is not inline.



---

archive/issue_comments_027376.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-08-14T13:30:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3849",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3849#issuecomment-27376",
    "user": "TimothyClemans"
}
```

Attachment



---

archive/issue_comments_027377.json:
```json
{
    "body": "Took care of (1) and also now clicking \"Upload Worksheet\" when form blank no longer displays \"Internal Server Error.\"",
    "created_at": "2008-08-14T13:32:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3849",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3849#issuecomment-27377",
    "user": "TimothyClemans"
}
```

Took care of (1) and also now clicking "Upload Worksheet" when form blank no longer displays "Internal Server Error."



---

archive/issue_comments_027378.json:
```json
{
    "body": "Attachment\n\nForget about this code.  This is an important error though.\n\nThe attached patch sagenb_3849-part1.patch I think completely fixes all such problems for uploading a *worksheet*, but doesn't do anything about Data-->Upload or attach file.\n\nI'm making Data -->Upload or attach a file a new ticket: #7495",
    "created_at": "2009-11-20T00:34:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3849",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3849#issuecomment-27378",
    "user": "was"
}
```

Attachment

Forget about this code.  This is an important error though.

The attached patch sagenb_3849-part1.patch I think completely fixes all such problems for uploading a *worksheet*, but doesn't do anything about Data-->Upload or attach file.

I'm making Data -->Upload or attach a file a new ticket: #7495



---

archive/issue_comments_027379.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-11-20T00:36:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3849",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3849#issuecomment-27379",
    "user": "was"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_027380.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-11-20T00:36:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3849",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3849#issuecomment-27380",
    "user": "was"
}
```

Attachment



---

archive/issue_comments_027381.json:
```json
{
    "body": "Attachment\n\nVersion 2.  Added backlink.  Apply only this patch to the sagenb repo.",
    "created_at": "2009-11-20T07:29:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3849",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3849#issuecomment-27381",
    "user": "mpatel"
}
```

Attachment

Version 2.  Added backlink.  Apply only this patch to the sagenb repo.



---

archive/issue_comments_027382.json:
```json
{
    "body": "Version 2:\n\n* Adds a link back to the upload page.\n* `sage-support` --> `sage-support group`.\n\nMy review, to the extent it counts, is positive.",
    "created_at": "2009-11-20T07:33:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3849",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3849#issuecomment-27382",
    "user": "mpatel"
}
```

Version 2:

* Adds a link back to the upload page.
* `sage-support` --> `sage-support group`.

My review, to the extent it counts, is positive.



---

archive/issue_comments_027383.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-12-06T07:48:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3849",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3849#issuecomment-27383",
    "user": "timdumol"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_027384.json:
```json
{
    "body": "Replying to [comment:7 mpatel]:\n> [...]\n> My review, to the extent it counts, is positive.\n\nI'm giving this a positive review. Everything works fine.",
    "created_at": "2009-12-06T07:48:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3849",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3849#issuecomment-27384",
    "user": "timdumol"
}
```

Replying to [comment:7 mpatel]:
> [...]
> My review, to the extent it counts, is positive.

I'm giving this a positive review. Everything works fine.



---

archive/issue_comments_027385.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-12-08T05:29:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3849",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3849#issuecomment-27385",
    "user": "was"
}
```

Resolution: fixed



---

archive/issue_comments_027386.json:
```json
{
    "body": "merged into sage-4.3",
    "created_at": "2009-12-08T05:29:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3849",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3849#issuecomment-27386",
    "user": "was"
}
```

merged into sage-4.3
