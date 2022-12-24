# Issue 5613: [with patch; needs review] fix url to sage hg server; hg_sage.bundle(...)

archive/issues_005613.json:
```json
{
    "body": "Assignee: schilly\n\nThe command\n\n```\n\n  sage: hg_sage.send('foo.hg')\n```\n\nwas broken because http://www.sagemath.org/hg/sage-main on the new server is now at http://hg.sagemath.org/sage-main/.  The attached patch fixes this.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5613\n\n",
    "created_at": "2009-03-26T02:32:40Z",
    "labels": [
        "website/wiki",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.1",
    "title": "[with patch; needs review] fix url to sage hg server; hg_sage.bundle(...)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5613",
    "user": "was"
}
```
Assignee: schilly

The command

```

  sage: hg_sage.send('foo.hg')
```

was broken because http://www.sagemath.org/hg/sage-main on the new server is now at http://hg.sagemath.org/sage-main/.  The attached patch fixes this.

Issue created by migration from https://trac.sagemath.org/ticket/5613





---

archive/issue_comments_043847.json:
```json
{
    "body": "Attachment [trac_5613.patch](tarball://root/attachments/some-uuid/ticket5613/trac_5613.patch) by was created at 2009-03-26 02:33:13",
    "created_at": "2009-03-26T02:33:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5613",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5613#issuecomment-43847",
    "user": "was"
}
```

Attachment [trac_5613.patch](tarball://root/attachments/some-uuid/ticket5613/trac_5613.patch) by was created at 2009-03-26 02:33:13



---

archive/issue_comments_043848.json:
```json
{
    "body": "Looks good to me.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-26T20:31:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5613",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5613#issuecomment-43848",
    "user": "mabshoff"
}
```

Looks good to me.

Cheers,

Michael



---

archive/issue_comments_043849.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-03-26T20:33:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5613",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5613#issuecomment-43849",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_043850.json:
```json
{
    "body": "Merged in Sage 3.4.1.alpha0.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-26T20:33:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5613",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5613#issuecomment-43850",
    "user": "mabshoff"
}
```

Merged in Sage 3.4.1.alpha0.

Cheers,

Michael
