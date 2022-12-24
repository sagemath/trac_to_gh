# Issue 7755: Auto-detect SageNB install path when building documentation

archive/issues_007755.json:
```json
{
    "body": "Assignee: mvngu\n\nCC:  @jhpalmieri\n\nWe should update the \"docbuild\" configuration so that Sphinx can locate jsMath.\n\nSee [sage-notebook](http://groups.google.com/group/sage-notebook/browse_thread/thread/9db6f5df45bc05cc), #7467.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7755\n\n",
    "created_at": "2009-12-24T05:15:55Z",
    "labels": [
        "documentation",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3",
    "title": "Auto-detect SageNB install path when building documentation",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7755",
    "user": "@qed777"
}
```
Assignee: mvngu

CC:  @jhpalmieri

We should update the "docbuild" configuration so that Sphinx can locate jsMath.

See [sage-notebook](http://groups.google.com/group/sage-notebook/browse_thread/thread/9db6f5df45bc05cc), #7467.

Issue created by migration from https://trac.sagemath.org/ticket/7755





---

archive/issue_comments_066787.json:
```json
{
    "body": "Auto-detect jsMath path.  Based on timdumol's comment at #7467.  sage repo.",
    "created_at": "2009-12-24T05:24:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7755",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7755#issuecomment-66787",
    "user": "@qed777"
}
```

Auto-detect jsMath path.  Based on timdumol's comment at #7467.  sage repo.



---

archive/issue_comments_066788.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-12-24T06:24:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7755",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7755#issuecomment-66788",
    "user": "@jhpalmieri"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_066789.json:
```json
{
    "body": "Attachment [trac_7755-docbuild_jsmath_path.patch](tarball://root/attachments/some-uuid/ticket7755/trac_7755-docbuild_jsmath_path.patch) by @jhpalmieri created at 2009-12-24 06:24:13\n\nLooks good.  Here's a slightly different patch to do the same thing, just making os.path.join do more of the work.  I'm committing it in your name (I just edited the patch file) and I'm giving it a positive review.",
    "created_at": "2009-12-24T06:24:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7755",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7755#issuecomment-66789",
    "user": "@jhpalmieri"
}
```

Attachment [trac_7755-docbuild_jsmath_path.patch](tarball://root/attachments/some-uuid/ticket7755/trac_7755-docbuild_jsmath_path.patch) by @jhpalmieri created at 2009-12-24 06:24:13

Looks good.  Here's a slightly different patch to do the same thing, just making os.path.join do more of the work.  I'm committing it in your name (I just edited the patch file) and I'm giving it a positive review.



---

archive/issue_comments_066790.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-12-24T06:24:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7755",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7755#issuecomment-66790",
    "user": "@jhpalmieri"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_066791.json:
```json
{
    "body": "use this one instead",
    "created_at": "2009-12-24T06:24:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7755",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7755#issuecomment-66791",
    "user": "@jhpalmieri"
}
```

use this one instead



---

archive/issue_comments_066792.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-12-24T07:11:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7755",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7755#issuecomment-66792",
    "user": "@williamstein"
}
```

Resolution: fixed



---

archive/issue_comments_066793.json:
```json
{
    "body": "Attachment [trac_7755-docbuild_jsmath_path-v2.patch](tarball://root/attachments/some-uuid/ticket7755/trac_7755-docbuild_jsmath_path-v2.patch) by @williamstein created at 2009-12-24 07:11:50\n\nMerged into sage-4.3.rc2.",
    "created_at": "2009-12-24T07:11:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7755",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7755#issuecomment-66793",
    "user": "@williamstein"
}
```

Attachment [trac_7755-docbuild_jsmath_path-v2.patch](tarball://root/attachments/some-uuid/ticket7755/trac_7755-docbuild_jsmath_path-v2.patch) by @williamstein created at 2009-12-24 07:11:50

Merged into sage-4.3.rc2.
