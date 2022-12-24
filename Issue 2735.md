# Issue 2735: [with patch; needs review] minor eclib build system improvements

archive/issues_002735.json:
```json
{
    "body": "Assignee: tabbott\n\nCC:  cremona\n\nThe eclib root makefile doesn't have a way to install the programs such as mwrank that it builds.  \n\nThere's currently a hack around this in the spkg-install script, but I'd prefer to not reproduce this random list of programs for the Debian package.\n\nSo, I've written some code to add to its root makefile that will call \"make install_progs\" in each of the subdirectories, and modified the Debian rules file to use it to install the non-test binary programs.  I notice that one of the test binary programs is installed by SAGE, so this new makefile can't yet simplify the dpkg-install by much.\n\nThe patches are attached.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2735\n\n",
    "created_at": "2008-03-30T06:48:39Z",
    "labels": [
        "debian-package",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "[with patch; needs review] minor eclib build system improvements",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2735",
    "user": "tabbott"
}
```
Assignee: tabbott

CC:  cremona

The eclib root makefile doesn't have a way to install the programs such as mwrank that it builds.  

There's currently a hack around this in the spkg-install script, but I'd prefer to not reproduce this random list of programs for the Debian package.

So, I've written some code to add to its root makefile that will call "make install_progs" in each of the subdirectories, and modified the Debian rules file to use it to install the non-test binary programs.  I notice that one of the test binary programs is installed by SAGE, so this new makefile can't yet simplify the dpkg-install by much.

The patches are attached.

Issue created by migration from https://trac.sagemath.org/ticket/2735





---

archive/issue_comments_018812.json:
```json
{
    "body": "Attachment [eclib-debian-build-fixes.patch](tarball://root/attachments/some-uuid/ticket2735/eclib-debian-build-fixes.patch) by mabshoff created at 2008-04-01 21:09:46\n\nPatch is good. Positive review.\n\nJohn: the patch has been merged in eclib-20080310.p1.spkg which will be part of Sage 3.0.alpha0. It only touches code inside the dist/debian directory.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-01T21:09:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2735",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2735#issuecomment-18812",
    "user": "mabshoff"
}
```

Attachment [eclib-debian-build-fixes.patch](tarball://root/attachments/some-uuid/ticket2735/eclib-debian-build-fixes.patch) by mabshoff created at 2008-04-01 21:09:46

Patch is good. Positive review.

John: the patch has been merged in eclib-20080310.p1.spkg which will be part of Sage 3.0.alpha0. It only touches code inside the dist/debian directory.

Cheers,

Michael



---

archive/issue_comments_018813.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-01T21:10:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2735",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2735#issuecomment-18813",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_018814.json:
```json
{
    "body": "Merged in Sage 3.0.alpha0",
    "created_at": "2008-04-01T21:10:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2735",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2735#issuecomment-18814",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.alpha0
