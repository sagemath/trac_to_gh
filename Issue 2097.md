# Issue 2097: aspect_ratio option to show() for function plots does not work correctly

archive/issues_002097.json:
```json
{
    "body": "Assignee: moretti\n\n\n```\nplot(x^2, (x, -10, 10)).show(aspect_ratio=1)\n```\n\n\noutputs a figure which is wide and short. It should be skinny and tall.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2097\n\n",
    "created_at": "2008-02-08T02:04:14Z",
    "labels": [
        "graphics",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.2",
    "title": "aspect_ratio option to show() for function plots does not work correctly",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2097",
    "user": "moretti"
}
```
Assignee: moretti


```
plot(x^2, (x, -10, 10)).show(aspect_ratio=1)
```


outputs a figure which is wide and short. It should be skinny and tall.

Issue created by migration from https://trac.sagemath.org/ticket/2097





---

archive/issue_comments_013564.json:
```json
{
    "body": "Fixed in the attached patch.",
    "created_at": "2008-02-08T02:09:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2097",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2097#issuecomment-13564",
    "user": "moretti"
}
```

Fixed in the attached patch.



---

archive/issue_comments_013565.json:
```json
{
    "body": "Attachment [aspect.patch](tarball://root/attachments/some-uuid/ticket2097/aspect.patch) by moretti created at 2008-02-08 02:10:00",
    "created_at": "2008-02-08T02:10:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2097",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2097#issuecomment-13565",
    "user": "moretti"
}
```

Attachment [aspect.patch](tarball://root/attachments/some-uuid/ticket2097/aspect.patch) by moretti created at 2008-02-08 02:10:00



---

archive/issue_comments_013566.json:
```json
{
    "body": "This patch makes a doctest fail; my attached patch fixes the doctest.\n\nOther than that, it looks good.  (The code looks good, it fixes the problem, and (after my patch) doctests still pass in sage/plots/.)\n\nApply both patches.",
    "created_at": "2008-02-09T21:23:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2097",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2097#issuecomment-13566",
    "user": "cwitty"
}
```

This patch makes a doctest fail; my attached patch fixes the doctest.

Other than that, it looks good.  (The code looks good, it fixes the problem, and (after my patch) doctests still pass in sage/plots/.)

Apply both patches.



---

archive/issue_comments_013567.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-12T18:29:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2097",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2097#issuecomment-13567",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_013568.json:
```json
{
    "body": "Attachment [aspect_fixtest.patch](tarball://root/attachments/some-uuid/ticket2097/aspect_fixtest.patch) by mabshoff created at 2008-02-12 18:29:06\n\nMerged both patches in Sage 2.10.2.alpha0",
    "created_at": "2008-02-12T18:29:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2097",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2097#issuecomment-13568",
    "user": "mabshoff"
}
```

Attachment [aspect_fixtest.patch](tarball://root/attachments/some-uuid/ticket2097/aspect_fixtest.patch) by mabshoff created at 2008-02-12 18:29:06

Merged both patches in Sage 2.10.2.alpha0
