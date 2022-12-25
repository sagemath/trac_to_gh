# Issue 2987: [with patch; needs review] Debian build support for zn_poly

archive/issues_002987.json:
```json
{
    "body": "Assignee: @timabbott\n\nI've made a Debian package for zn_poly.  Patch is attached.  \n\nIssue created by migration from https://trac.sagemath.org/ticket/2987\n\n",
    "created_at": "2008-04-21T06:32:09Z",
    "labels": [
        "component: debian-package",
        "blocker"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "[with patch; needs review] Debian build support for zn_poly",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2987",
    "user": "https://github.com/timabbott"
}
```
Assignee: @timabbott

I've made a Debian package for zn_poly.  Patch is attached.  

Issue created by migration from https://trac.sagemath.org/ticket/2987





---

archive/issue_comments_020521.json:
```json
{
    "body": "Attachment [zn_poly-debian.patch](tarball://root/attachments/some-uuid/ticket2987/zn_poly-debian.patch) by @timabbott created at 2008-04-21 06:32:24",
    "created_at": "2008-04-21T06:32:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2987",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2987#issuecomment-20521",
    "user": "https://github.com/timabbott"
}
```

Attachment [zn_poly-debian.patch](tarball://root/attachments/some-uuid/ticket2987/zn_poly-debian.patch) by @timabbott created at 2008-04-21 06:32:24



---

archive/issue_comments_020522.json:
```json
{
    "body": "Tim, ther is some predecessor patch missing. Neither the 0.4.1.p0 nor the 0.8.p0 spkg has any dist/debian directory. So, is there another patch?\n\nCheers,\n\nMichael",
    "created_at": "2008-04-21T07:03:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2987",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2987#issuecomment-20522",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Tim, ther is some predecessor patch missing. Neither the 0.4.1.p0 nor the 0.8.p0 spkg has any dist/debian directory. So, is there another patch?

Cheers,

Michael



---

archive/issue_comments_020523.json:
```json
{
    "body": "Ahh, I did 3 commits and \"hg export\"ed all 3 to make this patch file.  Lower down in the patch file it creates the directories.  Maybe this doesn't actually work.",
    "created_at": "2008-04-21T15:55:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2987",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2987#issuecomment-20523",
    "user": "https://github.com/timabbott"
}
```

Ahh, I did 3 commits and "hg export"ed all 3 to make this patch file.  Lower down in the patch file it creates the directories.  Maybe this doesn't actually work.



---

archive/issue_comments_020524.json:
```json
{
    "body": "Tim,\n\nfor mercurial you cannot concatenate patches - at least not in the order you did with this patch. I cut the three patches apart and applied them to \n\nhttp://sage.math.washington.edu/home/mabshoff/release-cycles-3.0/final/zn_poly-0.8.p0.spkg\n\nCheers,\n\nMichael",
    "created_at": "2008-04-22T03:43:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2987",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2987#issuecomment-20524",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Tim,

for mercurial you cannot concatenate patches - at least not in the order you did with this patch. I cut the three patches apart and applied them to 

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.0/final/zn_poly-0.8.p0.spkg

Cheers,

Michael



---

archive/issue_comments_020525.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-22T03:43:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2987",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2987#issuecomment-20525",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_020526.json:
```json
{
    "body": "Merged in Sage 3.0.final",
    "created_at": "2008-04-22T03:43:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2987",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2987#issuecomment-20526",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.final
