# Issue 2824: [with patch, needs review] sturm_bound incorrect for GammaH

archive/issues_002824.json:
```json
{
    "body": "Assignee: craigcitro\n\nThe Sturm bound is being calculated incorrectly for GammaH (we're just returning the bound for Gamma0, which is wrong). This fixes it.\n\nWe're actually producing wrong answers, so this is getting listed as critical.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2824\n\n",
    "created_at": "2008-04-06T07:19:22Z",
    "labels": [
        "modular forms",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "[with patch, needs review] sturm_bound incorrect for GammaH",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2824",
    "user": "craigcitro"
}
```
Assignee: craigcitro

The Sturm bound is being calculated incorrectly for GammaH (we're just returning the bound for Gamma0, which is wrong). This fixes it.

We're actually producing wrong answers, so this is getting listed as critical.

Issue created by migration from https://trac.sagemath.org/ticket/2824





---

archive/issue_comments_019396.json:
```json
{
    "body": "Attachment [trac-2824.patch](tarball://root/attachments/some-uuid/ticket2824/trac-2824.patch) by robertwb created at 2008-04-06 08:03:29\n\nVery good.",
    "created_at": "2008-04-06T08:03:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2824",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2824#issuecomment-19396",
    "user": "robertwb"
}
```

Attachment [trac-2824.patch](tarball://root/attachments/some-uuid/ticket2824/trac-2824.patch) by robertwb created at 2008-04-06 08:03:29

Very good.



---

archive/issue_comments_019397.json:
```json
{
    "body": "Merged in Sage 3.0.alpha2",
    "created_at": "2008-04-06T14:16:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2824",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2824#issuecomment-19397",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.alpha2



---

archive/issue_comments_019398.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-06T14:16:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2824",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2824#issuecomment-19398",
    "user": "mabshoff"
}
```

Resolution: fixed
