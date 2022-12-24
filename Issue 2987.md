# Issue 2987: [with patch; needs review] Debian build support for zn_poly

archive/issues_002987.json:
```json
{
    "body": "Assignee: tabbott\n\nI've made a Debian package for zn_poly.  Patch is attached.  \n\nIssue created by migration from https://trac.sagemath.org/ticket/2987\n\n",
    "created_at": "2008-04-21T06:32:09Z",
    "labels": [
        "debian-package",
        "blocker",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "[with patch; needs review] Debian build support for zn_poly",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2987",
    "user": "tabbott"
}
```
Assignee: tabbott

I've made a Debian package for zn_poly.  Patch is attached.  

Issue created by migration from https://trac.sagemath.org/ticket/2987





---

archive/issue_comments_020564.json:
```json
{
    "body": "Attachment [zn_poly-debian.patch](tarball://root/attachments/some-uuid/ticket2987/zn_poly-debian.patch) by tabbott created at 2008-04-21 06:32:24",
    "created_at": "2008-04-21T06:32:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2987",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2987#issuecomment-20564",
    "user": "tabbott"
}
```

Attachment [zn_poly-debian.patch](tarball://root/attachments/some-uuid/ticket2987/zn_poly-debian.patch) by tabbott created at 2008-04-21 06:32:24



---

archive/issue_comments_020565.json:
```json
{
    "body": "Tim, ther is some predecessor patch missing. Neither the 0.4.1.p0 nor the 0.8.p0 spkg has any dist/debian directory. So, is there another patch?\n\nCheers,\n\nMichael",
    "created_at": "2008-04-21T07:03:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2987",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2987#issuecomment-20565",
    "user": "mabshoff"
}
```

Tim, ther is some predecessor patch missing. Neither the 0.4.1.p0 nor the 0.8.p0 spkg has any dist/debian directory. So, is there another patch?

Cheers,

Michael



---

archive/issue_comments_020566.json:
```json
{
    "body": "Ahh, I did 3 commits and \"hg export\"ed all 3 to make this patch file.  Lower down in the patch file it creates the directories.  Maybe this doesn't actually work.",
    "created_at": "2008-04-21T15:55:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2987",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2987#issuecomment-20566",
    "user": "tabbott"
}
```

Ahh, I did 3 commits and "hg export"ed all 3 to make this patch file.  Lower down in the patch file it creates the directories.  Maybe this doesn't actually work.



---

archive/issue_comments_020567.json:
```json
{
    "body": "Tim,\n\nfor mercurial you cannot concatenate patches - at least not in the order you did with this patch. I cut the three patches apart and applied them to \n\nhttp://sage.math.washington.edu/home/mabshoff/release-cycles-3.0/final/zn_poly-0.8.p0.spkg\n\nCheers,\n\nMichael",
    "created_at": "2008-04-22T03:43:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2987",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2987#issuecomment-20567",
    "user": "mabshoff"
}
```

Tim,

for mercurial you cannot concatenate patches - at least not in the order you did with this patch. I cut the three patches apart and applied them to 

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.0/final/zn_poly-0.8.p0.spkg

Cheers,

Michael



---

archive/issue_comments_020568.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-22T03:43:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2987",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2987#issuecomment-20568",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_020569.json:
```json
{
    "body": "Merged in Sage 3.0.final",
    "created_at": "2008-04-22T03:43:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2987",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2987#issuecomment-20569",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.final
