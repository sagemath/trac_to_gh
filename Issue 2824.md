# Issue 2824: [with patch, needs review] sturm_bound incorrect for GammaH

archive/issues_002824.json:
```json
{
    "body": "Assignee: @craigcitro\n\nThe Sturm bound is being calculated incorrectly for GammaH (we're just returning the bound for Gamma0, which is wrong). This fixes it.\n\nWe're actually producing wrong answers, so this is getting listed as critical.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2824\n\n",
    "created_at": "2008-04-06T07:19:22Z",
    "labels": [
        "component: modular forms",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "[with patch, needs review] sturm_bound incorrect for GammaH",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2824",
    "user": "https://github.com/craigcitro"
}
```
Assignee: @craigcitro

The Sturm bound is being calculated incorrectly for GammaH (we're just returning the bound for Gamma0, which is wrong). This fixes it.

We're actually producing wrong answers, so this is getting listed as critical.

Issue created by migration from https://trac.sagemath.org/ticket/2824





---

archive/issue_comments_019355.json:
```json
{
    "body": "Attachment [trac-2824.patch](tarball://root/attachments/some-uuid/ticket2824/trac-2824.patch) by @robertwb created at 2008-04-06 08:03:29\n\nVery good.",
    "created_at": "2008-04-06T08:03:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2824",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2824#issuecomment-19355",
    "user": "https://github.com/robertwb"
}
```

Attachment [trac-2824.patch](tarball://root/attachments/some-uuid/ticket2824/trac-2824.patch) by @robertwb created at 2008-04-06 08:03:29

Very good.



---

archive/issue_comments_019356.json:
```json
{
    "body": "Merged in Sage 3.0.alpha2",
    "created_at": "2008-04-06T14:16:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2824",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2824#issuecomment-19356",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.alpha2



---

archive/issue_comments_019357.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-06T14:16:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2824",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2824#issuecomment-19357",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_003014.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-04-06T14:16:22Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2824",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2824#event-3014"
}
```
