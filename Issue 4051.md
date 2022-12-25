# Issue 4051: [with patch; needs review] Use of tar -j in sage-pkg

archive/issues_004051.json:
```json
{
    "body": "Assignee: anakha\n\nThe -j option to tar is a gnu tar specific option.  Workaround is to pipe output trough bzip2.  \n\nIssue created by migration from https://trac.sagemath.org/ticket/4051\n\n",
    "created_at": "2008-09-03T18:47:22Z",
    "labels": [
        "component: misc",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.2",
    "title": "[with patch; needs review] Use of tar -j in sage-pkg",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4051",
    "user": "https://trac.sagemath.org/admin/accounts/users/anakha"
}
```
Assignee: anakha

The -j option to tar is a gnu tar specific option.  Workaround is to pipe output trough bzip2.  

Issue created by migration from https://trac.sagemath.org/ticket/4051





---

archive/issue_comments_029147.json:
```json
{
    "body": "Attachment [trac_4051.patch](tarball://root/attachments/some-uuid/ticket4051/trac_4051.patch) by mabshoff created at 2008-09-03 18:53:08\n\nPatch looks good to me.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-03T18:53:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4051#issuecomment-29147",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [trac_4051.patch](tarball://root/attachments/some-uuid/ticket4051/trac_4051.patch) by mabshoff created at 2008-09-03 18:53:08

Patch looks good to me.

Cheers,

Michael



---

archive/issue_comments_029148.json:
```json
{
    "body": "One more thing: This does introduce a dependency on bzip2. If that turns out to be a problem (we expect tar with bzip2 support anyway) we can fall back to gtar.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-04T00:34:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4051#issuecomment-29148",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

One more thing: This does introduce a dependency on bzip2. If that turns out to be a problem (we expect tar with bzip2 support anyway) we can fall back to gtar.

Cheers,

Michael



---

archive/issue_comments_029149.json:
```json
{
    "body": "Merged in Sage 3.1.2.rc0",
    "created_at": "2008-09-04T00:36:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4051#issuecomment-29149",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.1.2.rc0



---

archive/issue_comments_029150.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-04T00:36:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4051#issuecomment-29150",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_029151.json:
```json
{
    "body": "Replying to [comment:2 mabshoff]:\n> One more thing: This does introduce a dependency on bzip2. If that turns out to be a problem (we expect tar with bzip2 support anyway) we can fall back to gtar.\n\ntar -j just invokes the bzip2 command.  So there is exactly the same dependency.  Try it on a system without bzip2 installed.\n\n> Cheers,\n> \n> Michael",
    "created_at": "2008-09-04T04:15:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4051#issuecomment-29151",
    "user": "https://trac.sagemath.org/admin/accounts/users/anakha"
}
```

Replying to [comment:2 mabshoff]:
> One more thing: This does introduce a dependency on bzip2. If that turns out to be a problem (we expect tar with bzip2 support anyway) we can fall back to gtar.

tar -j just invokes the bzip2 command.  So there is exactly the same dependency.  Try it on a system without bzip2 installed.

> Cheers,
> 
> Michael
