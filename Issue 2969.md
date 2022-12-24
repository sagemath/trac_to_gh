# Issue 2969: [with patches; needs review] Autocomputing Debian package version numbers

archive/issues_002969.json:
```json
{
    "body": "Assignee: @timabbott\n\nI've attached a series of patches that makes the Debian package version numbers get computed automatically from the SAGE spkg version numbers.  \n\nThe code I ran rename the existing spkgs is the following shell one-liner:\n\nfor i in `\\ls *.spkg`; do mv $i `echo $i | sed 's/\\.\\(p.*\\.spkg\\)/-\\1/'`; done\n\nThere are also a few patches that decrease version numbers of some Debian packages whose version numbers were too high, and another patch that fixes the guava Debianization to find the right version number.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2969\n\n",
    "created_at": "2008-04-20T04:20:24Z",
    "labels": [
        "debian-package",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "[with patches; needs review] Autocomputing Debian package version numbers",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2969",
    "user": "@timabbott"
}
```
Assignee: @timabbott

I've attached a series of patches that makes the Debian package version numbers get computed automatically from the SAGE spkg version numbers.  

The code I ran rename the existing spkgs is the following shell one-liner:

for i in `\ls *.spkg`; do mv $i `echo $i | sed 's/\.\(p.*\.spkg\)/-\1/'`; done

There are also a few patches that decrease version numbers of some Debian packages whose version numbers were too high, and another patch that fixes the guava Debianization to find the right version number.

Issue created by migration from https://trac.sagemath.org/ticket/2969





---

archive/issue_comments_020462.json:
```json
{
    "body": "Attachment [sage-debian-autoversion.patch](tarball://root/attachments/some-uuid/ticket2969/sage-debian-autoversion.patch) by @timabbott created at 2008-04-20 04:20:35",
    "created_at": "2008-04-20T04:20:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2969",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2969#issuecomment-20462",
    "user": "@timabbott"
}
```

Attachment [sage-debian-autoversion.patch](tarball://root/attachments/some-uuid/ticket2969/sage-debian-autoversion.patch) by @timabbott created at 2008-04-20 04:20:35



---

archive/issue_comments_020463.json:
```json
{
    "body": "Attachment [gap-guava-version.patch](tarball://root/attachments/some-uuid/ticket2969/gap-guava-version.patch) by @timabbott created at 2008-04-20 04:20:51",
    "created_at": "2008-04-20T04:20:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2969",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2969#issuecomment-20463",
    "user": "@timabbott"
}
```

Attachment [gap-guava-version.patch](tarball://root/attachments/some-uuid/ticket2969/gap-guava-version.patch) by @timabbott created at 2008-04-20 04:20:51



---

archive/issue_comments_020464.json:
```json
{
    "body": "Attachment [sympow-version.patch](tarball://root/attachments/some-uuid/ticket2969/sympow-version.patch) by @timabbott created at 2008-04-20 04:21:01",
    "created_at": "2008-04-20T04:21:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2969",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2969#issuecomment-20464",
    "user": "@timabbott"
}
```

Attachment [sympow-version.patch](tarball://root/attachments/some-uuid/ticket2969/sympow-version.patch) by @timabbott created at 2008-04-20 04:21:01



---

archive/issue_comments_020465.json:
```json
{
    "body": "Attachment [iml-version.patch](tarball://root/attachments/some-uuid/ticket2969/iml-version.patch) by @timabbott created at 2008-04-20 04:22:11",
    "created_at": "2008-04-20T04:22:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2969",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2969#issuecomment-20465",
    "user": "@timabbott"
}
```

Attachment [iml-version.patch](tarball://root/attachments/some-uuid/ticket2969/iml-version.patch) by @timabbott created at 2008-04-20 04:22:11



---

archive/issue_comments_020466.json:
```json
{
    "body": "Attachment [flintqs-version.patch](tarball://root/attachments/some-uuid/ticket2969/flintqs-version.patch) by mabshoff created at 2008-04-20 04:59:50\n\nlcalc-debian-cleanup.patch conflicts/has some of the same hunks as #2967. Reverting that patch then  makes this patch import fine.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-20T04:59:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2969",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2969#issuecomment-20466",
    "user": "mabshoff"
}
```

Attachment [flintqs-version.patch](tarball://root/attachments/some-uuid/ticket2969/flintqs-version.patch) by mabshoff created at 2008-04-20 04:59:50

lcalc-debian-cleanup.patch conflicts/has some of the same hunks as #2967. Reverting that patch then  makes this patch import fine.

Cheers,

Michael



---

archive/issue_comments_020467.json:
```json
{
    "body": "Oops, yeah, lcalc-debian-cleanup.patch is the same patch as in #2967.  Sorry about that.",
    "created_at": "2008-04-20T05:02:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2969",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2969#issuecomment-20467",
    "user": "@timabbott"
}
```

Oops, yeah, lcalc-debian-cleanup.patch is the same patch as in #2967.  Sorry about that.



---

archive/issue_comments_020468.json:
```json
{
    "body": "Patches look good to me [I fixed the issue I noted above]. Positive review.\n\nTim: no problem ;)\n\nCheers,\n\nMichael",
    "created_at": "2008-04-20T05:07:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2969",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2969#issuecomment-20468",
    "user": "mabshoff"
}
```

Patches look good to me [I fixed the issue I noted above]. Positive review.

Tim: no problem ;)

Cheers,

Michael



---

archive/issue_comments_020469.json:
```json
{
    "body": "Merged in Sage 3.0.rc0",
    "created_at": "2008-04-20T05:07:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2969",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2969#issuecomment-20469",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.rc0



---

archive/issue_comments_020470.json:
```json
{
    "body": "Merged in Sage 3.0.rc0",
    "created_at": "2008-04-20T05:08:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2969",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2969#issuecomment-20470",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.rc0



---

archive/issue_comments_020471.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-20T05:08:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2969",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2969#issuecomment-20471",
    "user": "mabshoff"
}
```

Resolution: fixed
