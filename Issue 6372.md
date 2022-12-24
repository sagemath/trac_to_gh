# Issue 6372: Move a few 3d plot files into plot3d

archive/issues_006372.json:
```json
{
    "body": "Assignee: was\n\ntachyon.py and tri_plot.py really belong in plot/plot3d, and there is an extra texture.py which is unused to remove.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6372\n\n",
    "created_at": "2009-06-20T19:07:49Z",
    "labels": [
        "graphics",
        "minor",
        "enhancement"
    ],
    "title": "Move a few 3d plot files into plot3d",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6372",
    "user": "kcrisman"
}
```
Assignee: was

tachyon.py and tri_plot.py really belong in plot/plot3d, and there is an extra texture.py which is unused to remove.

Issue created by migration from https://trac.sagemath.org/ticket/6372





---

archive/issue_comments_051004.json:
```json
{
    "body": "Depends on #6269",
    "created_at": "2009-06-20T19:12:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6372",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6372#issuecomment-51004",
    "user": "kcrisman"
}
```

Depends on #6269



---

archive/issue_comments_051005.json:
```json
{
    "body": "Attachment [trac_6372.patch](tarball://root/attachments/some-uuid/ticket6372/trac_6372.patch) by kcrisman created at 2009-06-20 19:16:26\n\nThis patch also makes necessary changes in a few other files to allow this, including in the plot3d rest documentation.",
    "created_at": "2009-06-20T19:16:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6372",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6372#issuecomment-51005",
    "user": "kcrisman"
}
```

Attachment [trac_6372.patch](tarball://root/attachments/some-uuid/ticket6372/trac_6372.patch) by kcrisman created at 2009-06-20 19:16:26

This patch also makes necessary changes in a few other files to allow this, including in the plot3d rest documentation.



---

archive/issue_comments_051006.json:
```json
{
    "body": "This also needs a rebase, since #6269 requires a rebase.",
    "created_at": "2009-06-24T22:24:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6372",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6372#issuecomment-51006",
    "user": "mvngu"
}
```

This also needs a rebase, since #6269 requires a rebase.



---

archive/issue_comments_051007.json:
```json
{
    "body": "kcrisman: Can you rebase the patch?",
    "created_at": "2009-06-25T00:16:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6372",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6372#issuecomment-51007",
    "user": "mvngu"
}
```

kcrisman: Can you rebase the patch?



---

archive/issue_comments_051008.json:
```json
{
    "body": "Attachment [trac_6372-rebased.patch](tarball://root/attachments/some-uuid/ticket6372/trac_6372-rebased.patch) by mvngu created at 2009-06-26 01:48:23\n\nrebased against Sage 4.1.alpha1",
    "created_at": "2009-06-26T01:48:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6372",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6372#issuecomment-51008",
    "user": "mvngu"
}
```

Attachment [trac_6372-rebased.patch](tarball://root/attachments/some-uuid/ticket6372/trac_6372-rebased.patch) by mvngu created at 2009-06-26 01:48:23

rebased against Sage 4.1.alpha1



---

archive/issue_comments_051009.json:
```json
{
    "body": "The patch `trac_6372-rebased.patch` is rebased against Sage 4.1.alpha1. It depends on #6269 and likely to also depends on #5640. So patches should be applied in the following order:\n1. the rebased patch at #6269\n2. the rebased patch at #5640\n3. the rebased patch on this ticket",
    "created_at": "2009-06-26T01:53:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6372",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6372#issuecomment-51009",
    "user": "mvngu"
}
```

The patch `trac_6372-rebased.patch` is rebased against Sage 4.1.alpha1. It depends on #6269 and likely to also depends on #5640. So patches should be applied in the following order:
1. the rebased patch at #6269
2. the rebased patch at #5640
3. the rebased patch on this ticket



---

archive/issue_comments_051010.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-26T17:41:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6372",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6372#issuecomment-51010",
    "user": "boothby"
}
```

Resolution: fixed
