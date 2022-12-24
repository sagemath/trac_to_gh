# Issue 2643: [with patch; needs review] Fix Debian Sections

archive/issues_002643.json:
```json
{
    "body": "Assignee: @timabbott\n\nI failed to correctly setup the Section fields of some of the Debian control files.  Attached are a series of patches to fix these problems.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2643\n\n",
    "created_at": "2008-03-22T03:40:43Z",
    "labels": [
        "debian-package",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "[with patch; needs review] Fix Debian Sections",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2643",
    "user": "@timabbott"
}
```
Assignee: @timabbott

I failed to correctly setup the Section fields of some of the Debian control files.  Attached are a series of patches to fix these problems.

Issue created by migration from https://trac.sagemath.org/ticket/2643





---

archive/issue_comments_018164.json:
```json
{
    "body": "Attachment [eclib.patch](tarball://root/attachments/some-uuid/ticket2643/eclib.patch) by @timabbott created at 2008-03-22 03:47:28",
    "created_at": "2008-03-22T03:47:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2643",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2643#issuecomment-18164",
    "user": "@timabbott"
}
```

Attachment [eclib.patch](tarball://root/attachments/some-uuid/ticket2643/eclib.patch) by @timabbott created at 2008-03-22 03:47:28



---

archive/issue_comments_018165.json:
```json
{
    "body": "Attachment [flint.patch](tarball://root/attachments/some-uuid/ticket2643/flint.patch) by @timabbott created at 2008-03-22 03:49:16",
    "created_at": "2008-03-22T03:49:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2643",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2643#issuecomment-18165",
    "user": "@timabbott"
}
```

Attachment [flint.patch](tarball://root/attachments/some-uuid/ticket2643/flint.patch) by @timabbott created at 2008-03-22 03:49:16



---

archive/issue_comments_018166.json:
```json
{
    "body": "Attachment [givaro.patch](tarball://root/attachments/some-uuid/ticket2643/givaro.patch) by @timabbott created at 2008-03-22 03:49:46",
    "created_at": "2008-03-22T03:49:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2643",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2643#issuecomment-18166",
    "user": "@timabbott"
}
```

Attachment [givaro.patch](tarball://root/attachments/some-uuid/ticket2643/givaro.patch) by @timabbott created at 2008-03-22 03:49:46



---

archive/issue_comments_018167.json:
```json
{
    "body": "Attachment [libm4ri.patch](tarball://root/attachments/some-uuid/ticket2643/libm4ri.patch) by @timabbott created at 2008-03-22 03:49:54",
    "created_at": "2008-03-22T03:49:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2643",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2643#issuecomment-18167",
    "user": "@timabbott"
}
```

Attachment [libm4ri.patch](tarball://root/attachments/some-uuid/ticket2643/libm4ri.patch) by @timabbott created at 2008-03-22 03:49:54



---

archive/issue_comments_018168.json:
```json
{
    "body": "Attachment [singular.patch](tarball://root/attachments/some-uuid/ticket2643/singular.patch) by mabshoff created at 2008-04-01 21:20:16\n\nMerged eclib.patch in eclib-20080310.p1.",
    "created_at": "2008-04-01T21:20:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2643",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2643#issuecomment-18168",
    "user": "mabshoff"
}
```

Attachment [singular.patch](tarball://root/attachments/some-uuid/ticket2643/singular.patch) by mabshoff created at 2008-04-01 21:20:16

Merged eclib.patch in eclib-20080310.p1.



---

archive/issue_comments_018169.json:
```json
{
    "body": "I should note that missing sections cause failures when trying to upload to a repository, so we should try to be sure these get merged sometime before the 3.0 release.",
    "created_at": "2008-04-10T16:13:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2643",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2643#issuecomment-18169",
    "user": "@timabbott"
}
```

I should note that missing sections cause failures when trying to upload to a repository, so we should try to be sure these get merged sometime before the 3.0 release.



---

archive/issue_comments_018170.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-04-11T22:12:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2643",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2643#issuecomment-18170",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_018171.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2008-04-11T22:12:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2643",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2643#issuecomment-18171",
    "user": "mabshoff"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_018172.json:
```json
{
    "body": "All these will go in before 3.0.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-11T22:12:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2643",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2643#issuecomment-18172",
    "user": "mabshoff"
}
```

All these will go in before 3.0.

Cheers,

Michael



---

archive/issue_comments_018173.json:
```json
{
    "body": "Changing assignee from @timabbott to mabshoff.",
    "created_at": "2008-04-11T22:12:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2643",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2643#issuecomment-18173",
    "user": "mabshoff"
}
```

Changing assignee from @timabbott to mabshoff.



---

archive/issue_comments_018174.json:
```json
{
    "body": "Merged flint.patch, givaro.patch, libm4ri.patch and singular.patch into Sage 3.0.alpha4. I did not increment the patch level of the spkgs to avoid unneeded rebuilds on upgrade.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-12T17:29:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2643",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2643#issuecomment-18174",
    "user": "mabshoff"
}
```

Merged flint.patch, givaro.patch, libm4ri.patch and singular.patch into Sage 3.0.alpha4. I did not increment the patch level of the spkgs to avoid unneeded rebuilds on upgrade.

Cheers,

Michael



---

archive/issue_comments_018175.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-12T17:29:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2643",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2643#issuecomment-18175",
    "user": "mabshoff"
}
```

Resolution: fixed
