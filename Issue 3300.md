# Issue 3300: [with patch; needs review] ntl soname for Debian package

archive/issues_003300.json:
```json
{
    "body": "Assignee: tabbott\n\nI've attached the patch to make the ntl Debian package use the soname library patch we made earlier (with a few other improvements).\n\nIssue created by migration from https://trac.sagemath.org/ticket/3300\n\n",
    "created_at": "2008-05-25T18:57:23Z",
    "labels": [
        "debian-package",
        "blocker",
        "bug"
    ],
    "title": "[with patch; needs review] ntl soname for Debian package",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3300",
    "user": "tabbott"
}
```
Assignee: tabbott

I've attached the patch to make the ntl Debian package use the soname library patch we made earlier (with a few other improvements).

Issue created by migration from https://trac.sagemath.org/ticket/3300





---

archive/issue_comments_022833.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-05-25T18:57:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3300",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3300#issuecomment-22833",
    "user": "tabbott"
}
```

Attachment



---

archive/issue_comments_022834.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-05-25T22:29:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3300",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3300#issuecomment-22834",
    "user": "tabbott"
}
```

Attachment



---

archive/issue_comments_022835.json:
```json
{
    "body": "I've also attached the patch that removes the ntl version number from spkg-install.",
    "created_at": "2008-05-25T22:29:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3300",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3300#issuecomment-22835",
    "user": "tabbott"
}
```

I've also attached the patch that removes the ntl version number from spkg-install.



---

archive/issue_comments_022836.json:
```json
{
    "body": "I've also attached a patch that changes the ntl priority to optional and makes the copyright file not have a trivially weird format.",
    "created_at": "2008-05-26T04:36:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3300",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3300#issuecomment-22836",
    "user": "tabbott"
}
```

I've also attached a patch that changes the ntl priority to optional and makes the copyright file not have a trivially weird format.



---

archive/issue_comments_022837.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-05-26T04:36:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3300",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3300#issuecomment-22837",
    "user": "tabbott"
}
```

Attachment



---

archive/issue_comments_022838.json:
```json
{
    "body": "Positive review on the two patches for the Debian dist directory, but I will not apply ntl-forget-version.patch since that results in libntl.so and libntl-5.4.2.so being identical copies. There is a special option for cp on Linux [-d] that preserves the link, but this might break on Cygwin for example. Since updating NTL is rare we can certainly deal with changing the so name on occasion.\n\nCheers,\n\nMichael",
    "created_at": "2008-05-28T07:41:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3300",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3300#issuecomment-22838",
    "user": "mabshoff"
}
```

Positive review on the two patches for the Debian dist directory, but I will not apply ntl-forget-version.patch since that results in libntl.so and libntl-5.4.2.so being identical copies. There is a special option for cp on Linux [-d] that preserves the link, but this might break on Cygwin for example. Since updating NTL is rare we can certainly deal with changing the so name on occasion.

Cheers,

Michael



---

archive/issue_comments_022839.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-05-28T07:43:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3300",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3300#issuecomment-22839",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_022840.json:
```json
{
    "body": "Merged in Sage 3.0.3.alpha0\n\nThe patches have been merged in \n\nhttp://sage.math.washington.edu/home/mabshoff/release-cycles-3.0.3/alpha0/ntl-5.4.2.p3.spkg\n\nwithout incrementing the patch level to avoid rebuilds.\n\nCheers,\n\nMichael",
    "created_at": "2008-05-28T07:43:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3300",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3300#issuecomment-22840",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.3.alpha0

The patches have been merged in 

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.0.3/alpha0/ntl-5.4.2.p3.spkg

without incrementing the patch level to avoid rebuilds.

Cheers,

Michael
