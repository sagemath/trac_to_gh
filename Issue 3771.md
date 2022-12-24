# Issue 3771: [with patch; needs review] make it so typing "sage -br" for new binary sage installs doesn't require rebuilding everything

archive/issues_003771.json:
```json
{
    "body": "Assignee: mabshoff\n\nHundreds of times people have been very annoyed when the install a fresh binary sage install, change something in the core library and type\n\n```\n  sage -br\n```\n\nonly to find that everything has to be built.   It turns out there is a trivial 2-line fix to make this not be the case.  That's attached to this ticket.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3771\n\n",
    "created_at": "2008-08-04T00:35:32Z",
    "labels": [
        "build",
        "major",
        "bug"
    ],
    "title": "[with patch; needs review] make it so typing \"sage -br\" for new binary sage installs doesn't require rebuilding everything",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3771",
    "user": "was"
}
```
Assignee: mabshoff

Hundreds of times people have been very annoyed when the install a fresh binary sage install, change something in the core library and type

```
  sage -br
```

only to find that everything has to be built.   It turns out there is a trivial 2-line fix to make this not be the case.  That's attached to this ticket.

Issue created by migration from https://trac.sagemath.org/ticket/3771





---

archive/issue_comments_026828.json:
```json
{
    "body": "Attachment [scripts-3771.patch](tarball://root/attachments/some-uuid/ticket3771/scripts-3771.patch) by craigcitro created at 2008-08-04 18:53:14\n\nThis is fantastic! I'm really excited that you sat down and fixed this.",
    "created_at": "2008-08-04T18:53:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3771",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3771#issuecomment-26828",
    "user": "craigcitro"
}
```

Attachment [scripts-3771.patch](tarball://root/attachments/some-uuid/ticket3771/scripts-3771.patch) by craigcitro created at 2008-08-04 18:53:14

This is fantastic! I'm really excited that you sat down and fixed this.



---

archive/issue_comments_026829.json:
```json
{
    "body": "Merged in Sage 3.1.alpha1",
    "created_at": "2008-08-09T00:56:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3771",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3771#issuecomment-26829",
    "user": "mabshoff"
}
```

Merged in Sage 3.1.alpha1



---

archive/issue_comments_026830.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-09T00:56:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3771",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3771#issuecomment-26830",
    "user": "mabshoff"
}
```

Resolution: fixed
