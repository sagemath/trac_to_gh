# Issue 2759: [with patch; needs review] SAGE debian/ directory updates

archive/issues_002759.json:
```json
{
    "body": "Assignee: @timabbott\n\nI'm attaching the changes to the SAGE debian/ directory that were needed to make it actually do Debian builds\n\nIssue created by migration from https://trac.sagemath.org/ticket/2759\n\n",
    "created_at": "2008-04-01T19:02:19Z",
    "labels": [
        "component: debian-package"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "[with patch; needs review] SAGE debian/ directory updates",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2759",
    "user": "https://github.com/timabbott"
}
```
Assignee: @timabbott

I'm attaching the changes to the SAGE debian/ directory that were needed to make it actually do Debian builds

Issue created by migration from https://trac.sagemath.org/ticket/2759





---

archive/issue_comments_018924.json:
```json
{
    "body": "Attachment [sage-debian-build.patch](tarball://root/attachments/some-uuid/ticket2759/sage-debian-build.patch) by mabshoff created at 2008-04-01 19:28:36\n\nPatch looks good to me. One problem is that it is against some non-existing repo, i.e. one that should be in `data/extcode/dist`. I don't have one there and all the files are check into the repo in `data/extcode/`. I applied the patch via GNU patch and committed in Tim's name. The applied patch is at\n\nhttp://sage.math.washington.edu/home/mabshoff/release-cycles-3.0/alpha0/trac_2759_sage-debian-build.patch\n\nCheers,\n\nMichael",
    "created_at": "2008-04-01T19:28:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2759",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2759#issuecomment-18924",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [sage-debian-build.patch](tarball://root/attachments/some-uuid/ticket2759/sage-debian-build.patch) by mabshoff created at 2008-04-01 19:28:36

Patch looks good to me. One problem is that it is against some non-existing repo, i.e. one that should be in `data/extcode/dist`. I don't have one there and all the files are check into the repo in `data/extcode/`. I applied the patch via GNU patch and committed in Tim's name. The applied patch is at

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.0/alpha0/trac_2759_sage-debian-build.patch

Cheers,

Michael



---

archive/issue_comments_018925.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-01T19:28:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2759",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2759#issuecomment-18925",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_018926.json:
```json
{
    "body": "Merged in Sage 3.0.alpha0",
    "created_at": "2008-04-01T19:28:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2759",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2759#issuecomment-18926",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.alpha0
