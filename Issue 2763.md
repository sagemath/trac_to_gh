# Issue 2763: [with patch; needs review] Debian amd64 fixes for rubiks

archive/issues_002763.json:
```json
{
    "body": "Assignee: tabbott\n\nApparently my rubiks Debian package failed to distclean, and thus some i386 binaries managed to survive during the amd64 build, which produced a very confusing error from dpkh-shlibdeps.  The attached patch fixes this.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2763\n\n",
    "created_at": "2008-04-01T22:14:11Z",
    "labels": [
        "debian-package",
        "major",
        "bug"
    ],
    "title": "[with patch; needs review] Debian amd64 fixes for rubiks",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2763",
    "user": "tabbott"
}
```
Assignee: tabbott

Apparently my rubiks Debian package failed to distclean, and thus some i386 binaries managed to survive during the amd64 build, which produced a very confusing error from dpkh-shlibdeps.  The attached patch fixes this.

Issue created by migration from https://trac.sagemath.org/ticket/2763





---

archive/issue_comments_018979.json:
```json
{
    "body": "Attachment [rubiks-amd64.patch](tarball://root/attachments/some-uuid/ticket2763/rubiks-amd64.patch) by mabshoff created at 2008-04-01 23:17:30\n\nPatch is good. Positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-01T23:17:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2763",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2763#issuecomment-18979",
    "user": "mabshoff"
}
```

Attachment [rubiks-amd64.patch](tarball://root/attachments/some-uuid/ticket2763/rubiks-amd64.patch) by mabshoff created at 2008-04-01 23:17:30

Patch is good. Positive review.

Cheers,

Michael



---

archive/issue_comments_018980.json:
```json
{
    "body": "Merged in Sage 3.0.alpha0",
    "created_at": "2008-04-01T23:26:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2763",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2763#issuecomment-18980",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.alpha0



---

archive/issue_comments_018981.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-01T23:26:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2763",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2763#issuecomment-18981",
    "user": "mabshoff"
}
```

Resolution: fixed
