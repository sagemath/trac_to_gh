# Issue 6686: [with patch, needs review] Missing closing </center> tag in notebook help page

archive/issues_006686.json:
```json
{
    "body": "Assignee: boothby\n\nThe notebook help page `http://localhost:8000/help` is not properly centered, because a closing `</center>` tag was omitted at #6225.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6686\n\n",
    "created_at": "2009-08-08T09:56:15Z",
    "labels": [
        "component: notebook",
        "trivial",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.2",
    "title": "[with patch, needs review] Missing closing </center> tag in notebook help page",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6686",
    "user": "https://github.com/qed777"
}
```
Assignee: boothby

The notebook help page `http://localhost:8000/help` is not properly centered, because a closing `</center>` tag was omitted at #6225.

Issue created by migration from https://trac.sagemath.org/ticket/6686





---

archive/issue_comments_054878.json:
```json
{
    "body": "Attachment [trac_6686-help_center_tag.patch](tarball://root/attachments/some-uuid/ticket6686/trac_6686-help_center_tag.patch) by @qed777 created at 2009-08-08 09:58:44",
    "created_at": "2009-08-08T09:58:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6686",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6686#issuecomment-54878",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_6686-help_center_tag.patch](tarball://root/attachments/some-uuid/ticket6686/trac_6686-help_center_tag.patch) by @qed777 created at 2009-08-08 09:58:44



---

archive/issue_comments_054879.json:
```json
{
    "body": "Alternative way to balance <center> tags.  Apply either this OR the other patch.",
    "created_at": "2009-08-08T10:01:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6686",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6686#issuecomment-54879",
    "user": "https://github.com/qed777"
}
```

Alternative way to balance <center> tags.  Apply either this OR the other patch.



---

archive/issue_comments_054880.json:
```json
{
    "body": "Attachment [trac_6686-help_center_tag_alt.patch](tarball://root/attachments/some-uuid/ticket6686/trac_6686-help_center_tag_alt.patch) by @qed777 created at 2009-08-08 10:03:33",
    "created_at": "2009-08-08T10:03:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6686",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6686#issuecomment-54880",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_6686-help_center_tag_alt.patch](tarball://root/attachments/some-uuid/ticket6686/trac_6686-help_center_tag_alt.patch) by @qed777 created at 2009-08-08 10:03:33



---

archive/issue_comments_054881.json:
```json
{
    "body": "The second patch is fine, and makes more sense (the whole thing is centered after the top matter).  Positive review.",
    "created_at": "2009-08-26T13:47:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6686",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6686#issuecomment-54881",
    "user": "https://github.com/kcrisman"
}
```

The second patch is fine, and makes more sense (the whole thing is centered after the top matter).  Positive review.



---

archive/issue_comments_054882.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-08-26T21:13:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6686",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6686#issuecomment-54882",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_054883.json:
```json
{
    "body": "Merged `trac_6686-help_center_tag_alt.patch`.",
    "created_at": "2009-08-26T21:13:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6686",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6686#issuecomment-54883",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Merged `trac_6686-help_center_tag_alt.patch`.
