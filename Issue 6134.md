# Issue 6134: [with patch, needs review] Fix SR coercion issue with numpy.float128

archive/issues_006134.json:
```json
{
    "body": "On 32-bit boxes, numpy does not build a float128.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6134\n\n",
    "created_at": "2009-05-26T20:07:41Z",
    "labels": [
        "symbolics",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0",
    "title": "[with patch, needs review] Fix SR coercion issue with numpy.float128",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6134",
    "user": "@mwhansen"
}
```
On 32-bit boxes, numpy does not build a float128.

Issue created by migration from https://trac.sagemath.org/ticket/6134





---

archive/issue_comments_048994.json:
```json
{
    "body": "Attachment [trac_6134.patch](tarball://root/attachments/some-uuid/ticket6134/trac_6134.patch) by @jasongrout created at 2009-05-26 20:11:05\n\nThis applied to my 32-bit rc0 build and fixed the issue for me.  Positive review.",
    "created_at": "2009-05-26T20:11:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6134",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6134#issuecomment-48994",
    "user": "@jasongrout"
}
```

Attachment [trac_6134.patch](tarball://root/attachments/some-uuid/ticket6134/trac_6134.patch) by @jasongrout created at 2009-05-26 20:11:05

This applied to my 32-bit rc0 build and fixed the issue for me.  Positive review.



---

archive/issue_comments_048995.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-05-26T20:51:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6134",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6134#issuecomment-48995",
    "user": "@mwhansen"
}
```

Resolution: fixed



---

archive/issue_comments_048996.json:
```json
{
    "body": "Merged in 4.0.rc1.",
    "created_at": "2009-05-26T20:51:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6134",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6134#issuecomment-48996",
    "user": "@mwhansen"
}
```

Merged in 4.0.rc1.
