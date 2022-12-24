# Issue 5916: [with patch, needs review] show mathematica expression using jsmath

archive/issues_005916.json:
```json
{
    "body": "Assignee: whuss\n\nCC:  @jasongrout\n\nShow mathematica expressions in the notebook using jsmath.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5916\n\n",
    "created_at": "2009-04-28T08:35:25Z",
    "labels": [
        "interfaces",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0.1",
    "title": "[with patch, needs review] show mathematica expression using jsmath",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5916",
    "user": "whuss"
}
```
Assignee: whuss

CC:  @jasongrout

Show mathematica expressions in the notebook using jsmath.

Issue created by migration from https://trac.sagemath.org/ticket/5916





---

archive/issue_comments_046753.json:
```json
{
    "body": "Attachment [mathematica_jsmath.patch](tarball://root/attachments/some-uuid/ticket5916/mathematica_jsmath.patch) by @jasongrout created at 2009-05-06 03:28:51",
    "created_at": "2009-05-06T03:28:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5916",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5916#issuecomment-46753",
    "user": "@jasongrout"
}
```

Attachment [mathematica_jsmath.patch](tarball://root/attachments/some-uuid/ticket5916/mathematica_jsmath.patch) by @jasongrout created at 2009-05-06 03:28:51



---

archive/issue_comments_046754.json:
```json
{
    "body": "This works great and passes doctests in the file.  Positive review.",
    "created_at": "2009-05-30T06:21:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5916",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5916#issuecomment-46754",
    "user": "@jasongrout"
}
```

This works great and passes doctests in the file.  Positive review.



---

archive/issue_comments_046755.json:
```json
{
    "body": "Merged in 4.0.1.alpha0.",
    "created_at": "2009-06-01T01:09:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5916",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5916#issuecomment-46755",
    "user": "@mwhansen"
}
```

Merged in 4.0.1.alpha0.



---

archive/issue_comments_046756.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-01T01:09:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5916",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5916#issuecomment-46756",
    "user": "@mwhansen"
}
```

Resolution: fixed



---

archive/issue_comments_046757.json:
```json
{
    "body": "It looks like we can use a screenshot to show the feature this patch introduces. If I'm not mistaken, can someone please upload such a screenshot so it can be put in the release tour.",
    "created_at": "2009-06-04T13:56:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5916",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5916#issuecomment-46757",
    "user": "mvngu"
}
```

It looks like we can use a screenshot to show the feature this patch introduces. If I'm not mistaken, can someone please upload such a screenshot so it can be put in the release tour.



---

archive/issue_comments_046758.json:
```json
{
    "body": "Attachment [mathematica.png](tarball://root/attachments/some-uuid/ticket5916/mathematica.png) by whuss created at 2009-06-04 15:09:03\n\nReplying to [comment:4 mvngu]:\n> It looks like we can use a screenshot to show the feature this patch introduces. If I'm not mistaken, can someone please upload such a screenshot so it can be put in the release tour.\n\nI attached the image which is produced by:\n\n\n```\nm = mathematica(\"Product[(3/2)^i, {i, 1, n}]\")\nshow(m)\n```\n",
    "created_at": "2009-06-04T15:09:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5916",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5916#issuecomment-46758",
    "user": "whuss"
}
```

Attachment [mathematica.png](tarball://root/attachments/some-uuid/ticket5916/mathematica.png) by whuss created at 2009-06-04 15:09:03

Replying to [comment:4 mvngu]:
> It looks like we can use a screenshot to show the feature this patch introduces. If I'm not mistaken, can someone please upload such a screenshot so it can be put in the release tour.

I attached the image which is produced by:


```
m = mathematica("Product[(3/2)^i, {i, 1, n}]")
show(m)
```

