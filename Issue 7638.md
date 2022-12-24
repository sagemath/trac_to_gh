# Issue 7638: [with patch, needs review] Cannot create big matrix on 64-bit system

archive/issues_007638.json:
```json
{
    "body": "Assignee: was\n\n*64-bit only*\n\nDue to unfortunate parenthesis, it is possible to create 2^31 by 10-matrices, but not 10 by 2^31. See patch\n\nIssue created by migration from https://trac.sagemath.org/ticket/7638\n\n",
    "created_at": "2009-12-09T14:02:41Z",
    "labels": [
        "linear algebra",
        "major",
        "bug"
    ],
    "title": "[with patch, needs review] Cannot create big matrix on 64-bit system",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7638",
    "user": "dagss"
}
```
Assignee: was

*64-bit only*

Due to unfortunate parenthesis, it is possible to create 2^31 by 10-matrices, but not 10 by 2^31. See patch

Issue created by migration from https://trac.sagemath.org/ticket/7638





---

archive/issue_comments_065279.json:
```json
{
    "body": "Attachment [7638-bigmatrix-fix.patch](tarball://root/attachments/some-uuid/ticket7638/7638-bigmatrix-fix.patch) by dagss created at 2009-12-09 14:04:03",
    "created_at": "2009-12-09T14:04:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7638",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7638#issuecomment-65279",
    "user": "dagss"
}
```

Attachment [7638-bigmatrix-fix.patch](tarball://root/attachments/some-uuid/ticket7638/7638-bigmatrix-fix.patch) by dagss created at 2009-12-09 14:04:03



---

archive/issue_comments_065280.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-12-09T14:06:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7638",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7638#issuecomment-65280",
    "user": "dagss"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_065281.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-12-09T14:38:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7638",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7638#issuecomment-65281",
    "user": "was"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_065282.json:
```json
{
    "body": "Thanks for finding this.  Positive review. \n\nI had to rebase the patch for sage-4.3.alpha1; rebased patch attached.",
    "created_at": "2009-12-09T14:38:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7638",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7638#issuecomment-65282",
    "user": "was"
}
```

Thanks for finding this.  Positive review. 

I had to rebase the patch for sage-4.3.alpha1; rebased patch attached.



---

archive/issue_comments_065283.json:
```json
{
    "body": "Attachment [trac_7638-rebase.patch](tarball://root/attachments/some-uuid/ticket7638/trac_7638-rebase.patch) by mhansen created at 2009-12-10 14:24:23",
    "created_at": "2009-12-10T14:24:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7638",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7638#issuecomment-65283",
    "user": "mhansen"
}
```

Attachment [trac_7638-rebase.patch](tarball://root/attachments/some-uuid/ticket7638/trac_7638-rebase.patch) by mhansen created at 2009-12-10 14:24:23



---

archive/issue_comments_065284.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-12-10T14:24:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7638",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7638#issuecomment-65284",
    "user": "mhansen"
}
```

Resolution: fixed
