# Issue 2989: [with patch; needs review] notebook -- issue with how the notebook is run that breaks it sometimes; also fix a typo in pid.

archive/issues_002989.json:
```json
{
    "body": "Assignee: boothby\n\nI made very minor harmless change to how the notebook twisted daemon is started, which makes it more robust.   Also, it was completely broken on my system until I made this change.  This is probably related to us updating to a new version of twistd.\n\nThe change is just to cd into the notebook directory before starting the tracd server.  That's it. \n\nIssue created by migration from https://trac.sagemath.org/ticket/2989\n\n",
    "created_at": "2008-04-21T14:41:26Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "[with patch; needs review] notebook -- issue with how the notebook is run that breaks it sometimes; also fix a typo in pid.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2989",
    "user": "@williamstein"
}
```
Assignee: boothby

I made very minor harmless change to how the notebook twisted daemon is started, which makes it more robust.   Also, it was completely broken on my system until I made this change.  This is probably related to us updating to a new version of twistd.

The change is just to cd into the notebook directory before starting the tracd server.  That's it. 

Issue created by migration from https://trac.sagemath.org/ticket/2989





---

archive/issue_comments_020575.json:
```json
{
    "body": "Attachment [sage-2989.patch](tarball://root/attachments/some-uuid/ticket2989/sage-2989.patch) by boothby created at 2008-04-21 20:42:30\n\nfails to apply against alpha5 :(",
    "created_at": "2008-04-21T20:42:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2989",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2989#issuecomment-20575",
    "user": "boothby"
}
```

Attachment [sage-2989.patch](tarball://root/attachments/some-uuid/ticket2989/sage-2989.patch) by boothby created at 2008-04-21 20:42:30

fails to apply against alpha5 :(



---

archive/issue_comments_020576.json:
```json
{
    "body": "Attachment [sage-2989_rebased_part2.patch](tarball://root/attachments/some-uuid/ticket2989/sage-2989_rebased_part2.patch) by @williamstein created at 2008-04-22 04:14:03",
    "created_at": "2008-04-22T04:14:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2989",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2989#issuecomment-20576",
    "user": "@williamstein"
}
```

Attachment [sage-2989_rebased_part2.patch](tarball://root/attachments/some-uuid/ticket2989/sage-2989_rebased_part2.patch) by @williamstein created at 2008-04-22 04:14:03



---

archive/issue_comments_020577.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-22T04:57:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2989",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2989#issuecomment-20577",
    "user": "@williamstein"
}
```

Resolution: fixed
