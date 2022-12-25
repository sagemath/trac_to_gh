# Issue 7010: sanity check key value of the shift cryptosystem

archive/issues_007010.json:
```json
{
    "body": "Assignee: somebody\n\nCC:  @rbeezer\n\nThis is a follow up to ticket #6841.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7010\n\n",
    "created_at": "2009-09-25T07:13:23Z",
    "labels": [
        "component: cryptography"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.2",
    "title": "sanity check key value of the shift cryptosystem",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7010",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```
Assignee: somebody

CC:  @rbeezer

This is a follow up to ticket #6841.

Issue created by migration from https://trac.sagemath.org/ticket/7010





---

archive/issue_comments_057854.json:
```json
{
    "body": "clean up sage/crypto/classical.py so it conforms to coding conventions",
    "created_at": "2009-10-04T16:00:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7010",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7010#issuecomment-57854",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

clean up sage/crypto/classical.py so it conforms to coding conventions



---

archive/issue_comments_057855.json:
```json
{
    "body": "Attachment [trac_7010-code-clean-up.patch](tarball://root/attachments/some-uuid/ticket7010/trac_7010-code-clean-up.patch) by mvngu created at 2009-10-04 16:03:13\n\nThe patch `trac_7010-code-clean-up.patch` mainly cleans up the file `sage/crypto/classical.py` so it conforms to coding conventions. The clean up also removes the deprecated way of raising exceptions, and instead uses the way that is more compatible with Python 3.x.",
    "created_at": "2009-10-04T16:03:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7010",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7010#issuecomment-57855",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Attachment [trac_7010-code-clean-up.patch](tarball://root/attachments/some-uuid/ticket7010/trac_7010-code-clean-up.patch) by mvngu created at 2009-10-04 16:03:13

The patch `trac_7010-code-clean-up.patch` mainly cleans up the file `sage/crypto/classical.py` so it conforms to coding conventions. The clean up also removes the deprecated way of raising exceptions, and instead uses the way that is more compatible with Python 3.x.



---

archive/issue_comments_057856.json:
```json
{
    "body": "Attachment [trac_7010-key-check.patch](tarball://root/attachments/some-uuid/ticket7010/trac_7010-key-check.patch) by mvngu created at 2009-10-04 16:50:00\n\napply on top of previous patch",
    "created_at": "2009-10-04T16:50:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7010",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7010#issuecomment-57856",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Attachment [trac_7010-key-check.patch](tarball://root/attachments/some-uuid/ticket7010/trac_7010-key-check.patch) by mvngu created at 2009-10-04 16:50:00

apply on top of previous patch



---

archive/issue_comments_057857.json:
```json
{
    "body": "Applies, builds, functions, docs build, passes long tests.\n\nNo substantial code changes in the clean-up, sanity-check completes making the shift-cipher (#6841) complete with regard to poor input.\n\nPositive review.",
    "created_at": "2009-10-05T05:02:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7010",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7010#issuecomment-57857",
    "user": "https://github.com/rbeezer"
}
```

Applies, builds, functions, docs build, passes long tests.

No substantial code changes in the clean-up, sanity-check completes making the shift-cipher (#6841) complete with regard to poor input.

Positive review.



---

archive/issue_events_007233.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-10-15T10:04:52Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7010",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7010#event-7233"
}
```



---

archive/issue_comments_057858.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-10-15T10:04:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7010",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7010#issuecomment-57858",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed
