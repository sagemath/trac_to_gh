# Issue 4382: [with patch; needs review] notebook -- use sage-native-execute for ssh'ing for remote pexpect

archive/issues_004382.json:
```json
{
    "body": "Assignee: boothby\n\nThis patch fixes a major bug that would make it nearly impossible to setup a secure sage server. \nAll it does is make sure ssh runs without the Sage environment setup, which is good because of version mismatches.  \n\nIssue created by migration from https://trac.sagemath.org/ticket/4382\n\n",
    "created_at": "2008-10-29T22:44:29Z",
    "labels": [
        "notebook",
        "critical",
        "bug"
    ],
    "title": "[with patch; needs review] notebook -- use sage-native-execute for ssh'ing for remote pexpect",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4382",
    "user": "was"
}
```
Assignee: boothby

This patch fixes a major bug that would make it nearly impossible to setup a secure sage server. 
All it does is make sure ssh runs without the Sage environment setup, which is good because of version mismatches.  

Issue created by migration from https://trac.sagemath.org/ticket/4382





---

archive/issue_comments_032241.json:
```json
{
    "body": "Attachment\n\nPatch is good, positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-10-30T02:58:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4382",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4382#issuecomment-32241",
    "user": "mabshoff"
}
```

Attachment

Patch is good, positive review.

Cheers,

Michael



---

archive/issue_comments_032242.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-10-30T03:23:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4382",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4382#issuecomment-32242",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_032243.json:
```json
{
    "body": "Merged in Sage 3.2.alpha2",
    "created_at": "2008-10-30T03:23:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4382",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4382#issuecomment-32243",
    "user": "mabshoff"
}
```

Merged in Sage 3.2.alpha2
