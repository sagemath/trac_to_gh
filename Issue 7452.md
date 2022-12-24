# Issue 7452: Make it easier to diagnose build problems by allowing copy-paste

archive/issues_007452.json:
```json
{
    "body": "Assignee: tbd\n\nIn case of build problems the message telling you what to do cannot be easily copied as one command to run.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7452\n\n",
    "created_at": "2009-11-13T17:27:07Z",
    "labels": [
        "build",
        "trivial",
        "enhancement"
    ],
    "title": "Make it easier to diagnose build problems by allowing copy-paste",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7452",
    "user": "iandrus"
}
```
Assignee: tbd

In case of build problems the message telling you what to do cannot be easily copied as one command to run.

Issue created by migration from https://trac.sagemath.org/ticket/7452





---

archive/issue_comments_062760.json:
```json
{
    "body": "Attachment [trac7452.patch](tarball://root/attachments/some-uuid/ticket7452/trac7452.patch) by iandrus created at 2009-11-13 17:28:36\n\nMake debugging instructions copy/pastable",
    "created_at": "2009-11-13T17:28:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7452",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7452#issuecomment-62760",
    "user": "iandrus"
}
```

Attachment [trac7452.patch](tarball://root/attachments/some-uuid/ticket7452/trac7452.patch) by iandrus created at 2009-11-13 17:28:36

Make debugging instructions copy/pastable



---

archive/issue_comments_062761.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-11-13T17:29:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7452",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7452#issuecomment-62761",
    "user": "iandrus"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_062762.json:
```json
{
    "body": "I couldn't successfully apply the patch `trac7452.patch` to Sage 4.3.alpha1. So I have attached the reviewer patch `trac_7452-rebased.patch` which is a rebase of iandrus' patch. This newer patch is based on Sage 4.3.alpha1 and contains some rewording, but the essential ideas are those of iandrus' so I kept his name on the newer patch. I'm OK with iandrus' original patch; only my rebased patch needs to be reviewed and applied. Essentially, anyone besides me are welcome to review `trac_7452-rebased.patch`.",
    "created_at": "2009-12-08T17:43:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7452",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7452#issuecomment-62762",
    "user": "mvngu"
}
```

I couldn't successfully apply the patch `trac7452.patch` to Sage 4.3.alpha1. So I have attached the reviewer patch `trac_7452-rebased.patch` which is a rebase of iandrus' patch. This newer patch is based on Sage 4.3.alpha1 and contains some rewording, but the essential ideas are those of iandrus' so I kept his name on the newer patch. I'm OK with iandrus' original patch; only my rebased patch needs to be reviewed and applied. Essentially, anyone besides me are welcome to review `trac_7452-rebased.patch`.



---

archive/issue_comments_062763.json:
```json
{
    "body": "If I am allowed to review the rebased patch, I give it a positive review.  The only nit that I have it is uses tabs, but there are other tabs in this file as well.",
    "created_at": "2009-12-08T21:19:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7452",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7452#issuecomment-62763",
    "user": "iandrus"
}
```

If I am allowed to review the rebased patch, I give it a positive review.  The only nit that I have it is uses tabs, but there are other tabs in this file as well.



---

archive/issue_comments_062764.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-12-08T21:19:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7452",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7452#issuecomment-62764",
    "user": "iandrus"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_062765.json:
```json
{
    "body": "Attachment [trac_7452-rebased.patch](tarball://root/attachments/some-uuid/ticket7452/trac_7452-rebased.patch) by mvngu created at 2009-12-08 22:08:26\n\nbased on Sage 4.3.alpha1",
    "created_at": "2009-12-08T22:08:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7452",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7452#issuecomment-62765",
    "user": "mvngu"
}
```

Attachment [trac_7452-rebased.patch](tarball://root/attachments/some-uuid/ticket7452/trac_7452-rebased.patch) by mvngu created at 2009-12-08 22:08:26

based on Sage 4.3.alpha1



---

archive/issue_comments_062766.json:
```json
{
    "body": "Replying to [comment:4 iandrus]:\n> If I am allowed to review the rebased patch, I give it a positive review. \n\nYes, I think you are allowed to review my rebased patch. Essentially, I'm happy with your original patch and I would give it a positive review. But I can't successfully apply your patch to Sage 4.3.alpha1 so I had to rebase your patch. What you are doing is reviewing the modification I made to your patch.\n\n\n\n\n\n> The only nit that I have it is uses tabs, but there are other tabs in this file as well.\n\nMy apology about introducing the tabs. I have attached a new patch which shouldn't have any tabs in it. Only that newer patch needs reviewing.",
    "created_at": "2009-12-08T22:13:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7452",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7452#issuecomment-62766",
    "user": "mvngu"
}
```

Replying to [comment:4 iandrus]:
> If I am allowed to review the rebased patch, I give it a positive review. 

Yes, I think you are allowed to review my rebased patch. Essentially, I'm happy with your original patch and I would give it a positive review. But I can't successfully apply your patch to Sage 4.3.alpha1 so I had to rebase your patch. What you are doing is reviewing the modification I made to your patch.





> The only nit that I have it is uses tabs, but there are other tabs in this file as well.

My apology about introducing the tabs. I have attached a new patch which shouldn't have any tabs in it. Only that newer patch needs reviewing.



---

archive/issue_comments_062767.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2009-12-08T22:13:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7452",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7452#issuecomment-62767",
    "user": "mvngu"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_062768.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-12-08T22:13:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7452",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7452#issuecomment-62768",
    "user": "mvngu"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_062769.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-12-09T08:28:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7452",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7452#issuecomment-62769",
    "user": "mhansen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_062770.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-12-14T15:53:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7452",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7452#issuecomment-62770",
    "user": "mhansen"
}
```

Resolution: fixed
