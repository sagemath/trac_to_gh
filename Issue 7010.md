# Issue 7010: sanity check key value of the shift cryptosystem

archive/issues_007010.json:
```json
{
    "body": "Assignee: somebody\n\nCC:  @rbeezer\n\nThis is a follow up to ticket #6841.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7010\n\n",
    "created_at": "2009-09-25T07:13:23Z",
    "labels": [
        "cryptography",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.2",
    "title": "sanity check key value of the shift cryptosystem",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7010",
    "user": "mvngu"
}
```
Assignee: somebody

CC:  @rbeezer

This is a follow up to ticket #6841.

Issue created by migration from https://trac.sagemath.org/ticket/7010





---

archive/issue_comments_057962.json:
```json
{
    "body": "clean up sage/crypto/classical.py so it conforms to coding conventions",
    "created_at": "2009-10-04T16:00:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7010",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7010#issuecomment-57962",
    "user": "mvngu"
}
```

clean up sage/crypto/classical.py so it conforms to coding conventions



---

archive/issue_comments_057963.json:
```json
{
    "body": "Attachment [trac_7010-code-clean-up.patch](tarball://root/attachments/some-uuid/ticket7010/trac_7010-code-clean-up.patch) by mvngu created at 2009-10-04 16:03:13\n\nThe patch `trac_7010-code-clean-up.patch` mainly cleans up the file `sage/crypto/classical.py` so it conforms to coding conventions. The clean up also removes the deprecated way of raising exceptions, and instead uses the way that is more compatible with Python 3.x.",
    "created_at": "2009-10-04T16:03:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7010",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7010#issuecomment-57963",
    "user": "mvngu"
}
```

Attachment [trac_7010-code-clean-up.patch](tarball://root/attachments/some-uuid/ticket7010/trac_7010-code-clean-up.patch) by mvngu created at 2009-10-04 16:03:13

The patch `trac_7010-code-clean-up.patch` mainly cleans up the file `sage/crypto/classical.py` so it conforms to coding conventions. The clean up also removes the deprecated way of raising exceptions, and instead uses the way that is more compatible with Python 3.x.



---

archive/issue_comments_057964.json:
```json
{
    "body": "Attachment [trac_7010-key-check.patch](tarball://root/attachments/some-uuid/ticket7010/trac_7010-key-check.patch) by mvngu created at 2009-10-04 16:50:00\n\napply on top of previous patch",
    "created_at": "2009-10-04T16:50:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7010",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7010#issuecomment-57964",
    "user": "mvngu"
}
```

Attachment [trac_7010-key-check.patch](tarball://root/attachments/some-uuid/ticket7010/trac_7010-key-check.patch) by mvngu created at 2009-10-04 16:50:00

apply on top of previous patch



---

archive/issue_comments_057965.json:
```json
{
    "body": "Applies, builds, functions, docs build, passes long tests.\n\nNo substantial code changes in the clean-up, sanity-check completes making the shift-cipher (#6841) complete with regard to poor input.\n\nPositive review.",
    "created_at": "2009-10-05T05:02:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7010",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7010#issuecomment-57965",
    "user": "@rbeezer"
}
```

Applies, builds, functions, docs build, passes long tests.

No substantial code changes in the clean-up, sanity-check completes making the shift-cipher (#6841) complete with regard to poor input.

Positive review.



---

archive/issue_comments_057966.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-10-15T10:04:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7010",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7010#issuecomment-57966",
    "user": "@mwhansen"
}
```

Resolution: fixed
