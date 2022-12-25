# Issue 4382: [with patch; needs review] notebook -- use sage-native-execute for ssh'ing for remote pexpect

archive/issues_004382.json:
```json
{
    "body": "Assignee: boothby\n\nThis patch fixes a major bug that would make it nearly impossible to setup a secure sage server. \nAll it does is make sure ssh runs without the Sage environment setup, which is good because of version mismatches.  \n\nIssue created by migration from https://trac.sagemath.org/ticket/4382\n\n",
    "created_at": "2008-10-29T22:44:29Z",
    "labels": [
        "component: notebook",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2",
    "title": "[with patch; needs review] notebook -- use sage-native-execute for ssh'ing for remote pexpect",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4382",
    "user": "https://github.com/williamstein"
}
```
Assignee: boothby

This patch fixes a major bug that would make it nearly impossible to setup a secure sage server. 
All it does is make sure ssh runs without the Sage environment setup, which is good because of version mismatches.  

Issue created by migration from https://trac.sagemath.org/ticket/4382





---

archive/issue_comments_032178.json:
```json
{
    "body": "Attachment [sage-4382.patch](tarball://root/attachments/some-uuid/ticket4382/sage-4382.patch) by mabshoff created at 2008-10-30 02:58:04\n\nPatch is good, positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-10-30T02:58:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4382",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4382#issuecomment-32178",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [sage-4382.patch](tarball://root/attachments/some-uuid/ticket4382/sage-4382.patch) by mabshoff created at 2008-10-30 02:58:04

Patch is good, positive review.

Cheers,

Michael



---

archive/issue_comments_032179.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-10-30T03:23:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4382",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4382#issuecomment-32179",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_004627.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-10-30T03:23:35Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4382",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4382#event-4627"
}
```



---

archive/issue_comments_032180.json:
```json
{
    "body": "Merged in Sage 3.2.alpha2",
    "created_at": "2008-10-30T03:23:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4382",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4382#issuecomment-32180",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.2.alpha2
