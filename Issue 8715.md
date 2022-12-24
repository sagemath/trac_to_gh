# Issue 8715: fortran-20100118 ignores SAGE_FORTRAN on Linux

archive/issues_008715.json:
```json
{
    "body": "Assignee: GeorgSWeber\n\nOn Linux, fortran-20100118.spkg's spkg-install ignores SAGE_FORTRAN and instead overrides it with the first \"gfortran\" it finds in $PATH.  In my environment this fortran compiler is (more or less) broken, so I have to it explicitly and I then want it to be used.  The simple attached fix executes the relevant code path only if SAGE_FORTRAN is not set yet.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8715\n\n",
    "created_at": "2010-04-19T13:14:38Z",
    "labels": [
        "build",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.1",
    "title": "fortran-20100118 ignores SAGE_FORTRAN on Linux",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8715",
    "user": "logix"
}
```
Assignee: GeorgSWeber

On Linux, fortran-20100118.spkg's spkg-install ignores SAGE_FORTRAN and instead overrides it with the first "gfortran" it finds in $PATH.  In my environment this fortran compiler is (more or less) broken, so I have to it explicitly and I then want it to be used.  The simple attached fix executes the relevant code path only if SAGE_FORTRAN is not set yet.

Issue created by migration from https://trac.sagemath.org/ticket/8715





---

archive/issue_comments_079542.json:
```json
{
    "body": "Attachment [fortran-20100118_diff](tarball://root/attachments/some-uuid/ticket8715/fortran-20100118_diff) by logix created at 2010-04-19 13:15:50",
    "created_at": "2010-04-19T13:15:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8715",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8715#issuecomment-79542",
    "user": "logix"
}
```

Attachment [fortran-20100118_diff](tarball://root/attachments/some-uuid/ticket8715/fortran-20100118_diff) by logix created at 2010-04-19 13:15:50



---

archive/issue_comments_079543.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-04-22T14:20:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8715",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8715#issuecomment-79543",
    "user": "logix"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_079544.json:
```json
{
    "body": "Well, the patch you uploaded is not a Mercurial \"ChangeSet\"...\n\nhttp://www.sagemath.org/doc/developer/producing_patches.html",
    "created_at": "2010-04-22T19:33:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8715",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8715#issuecomment-79544",
    "user": "@nexttime"
}
```

Well, the patch you uploaded is not a Mercurial "ChangeSet"...

http://www.sagemath.org/doc/developer/producing_patches.html



---

archive/issue_comments_079545.json:
```json
{
    "body": "and/or http://www.sagemath.org/doc/developer/patching_spkgs.html",
    "created_at": "2010-04-22T19:43:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8715",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8715#issuecomment-79545",
    "user": "@nexttime"
}
```

and/or http://www.sagemath.org/doc/developer/patching_spkgs.html



---

archive/issue_comments_079546.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-04-28T22:06:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8715",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8715#issuecomment-79546",
    "user": "@williamstein"
}
```

Resolution: fixed



---

archive/issue_comments_079547.json:
```json
{
    "body": "Good idea.  Looks good.  Thanks! Positive review, and merged into 4.4.1.alpha1.",
    "created_at": "2010-04-28T22:06:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8715",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8715#issuecomment-79547",
    "user": "@williamstein"
}
```

Good idea.  Looks good.  Thanks! Positive review, and merged into 4.4.1.alpha1.
