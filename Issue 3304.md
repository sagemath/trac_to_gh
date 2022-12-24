# Issue 3304: [with patch; needs review] Make cddlib Debian package use shared library

archive/issues_003304.json:
```json
{
    "body": "Assignee: @timabbott\n\nCC:  @vbraun mhampton\n\nI've attached a patch to make the Debian package use the cddlib shared library code.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3304\n\n",
    "created_at": "2008-05-26T01:31:25Z",
    "labels": [
        "debian-package",
        "blocker",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.3",
    "title": "[with patch; needs review] Make cddlib Debian package use shared library",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3304",
    "user": "@timabbott"
}
```
Assignee: @timabbott

CC:  @vbraun mhampton

I've attached a patch to make the Debian package use the cddlib shared library code.

Issue created by migration from https://trac.sagemath.org/ticket/3304





---

archive/issue_comments_022849.json:
```json
{
    "body": "Changing keywords from \"\" to \"editor_mabshoff\".",
    "created_at": "2008-06-15T21:31:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3304",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3304#issuecomment-22849",
    "user": "@craigcitro"
}
```

Changing keywords from "" to "editor_mabshoff".



---

archive/issue_comments_022850.json:
```json
{
    "body": "Attachment [cddlib-debian-shared-library.patch](tarball://root/attachments/some-uuid/ticket3304/cddlib-debian-shared-library.patch) by @craigcitro created at 2008-06-15 21:31:26",
    "created_at": "2008-06-15T21:31:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3304",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3304#issuecomment-22850",
    "user": "@craigcitro"
}
```

Attachment [cddlib-debian-shared-library.patch](tarball://root/attachments/some-uuid/ticket3304/cddlib-debian-shared-library.patch) by @craigcitro created at 2008-06-15 21:31:26



---

archive/issue_comments_022851.json:
```json
{
    "body": "Attachment [cddlib-shared-library.patch](tarball://root/attachments/some-uuid/ticket3304/cddlib-shared-library.patch) by @timabbott created at 2008-12-12 18:55:11",
    "created_at": "2008-12-12T18:55:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3304",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3304#issuecomment-22851",
    "user": "@timabbott"
}
```

Attachment [cddlib-shared-library.patch](tarball://root/attachments/some-uuid/ticket3304/cddlib-shared-library.patch) by @timabbott created at 2008-12-12 18:55:11



---

archive/issue_comments_022852.json:
```json
{
    "body": "Earlier today I attached a version of the patch that doesn't mess with dist/debian (since that's no longer relevant).",
    "created_at": "2008-12-12T20:48:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3304",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3304#issuecomment-22852",
    "user": "@timabbott"
}
```

Earlier today I attached a version of the patch that doesn't mess with dist/debian (since that's no longer relevant).



---

archive/issue_comments_022853.json:
```json
{
    "body": "Well, given how long we have been sitting on this reduce priority to critical.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-15T07:12:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3304",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3304#issuecomment-22853",
    "user": "mabshoff"
}
```

Well, given how long we have been sitting on this reduce priority to critical.

Cheers,

Michael



---

archive/issue_comments_022854.json:
```json
{
    "body": "Changing priority from blocker to critical.",
    "created_at": "2009-02-15T07:12:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3304",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3304#issuecomment-22854",
    "user": "mabshoff"
}
```

Changing priority from blocker to critical.



---

archive/issue_comments_022855.json:
```json
{
    "body": "Has nothing to do with Debian, maybe that was misleading; summary changed.\n\nThe following spkg is patched in a similar way. It essentially contains tabbott's patch, but I found this report only after making the changes myself.\n\nhttp://www.stp.dias.ie/~vbraun/cddlib-094f.p3.spkg \n\nUsers of the Fedora 12 binary sage distribution must manually re-install mpir-1.2.2.p0.spkg as discussed on http://groups.google.com/group/sage-devel/msg/aec4aa6b3874fe10. This is an unrelated bug of the build system.",
    "created_at": "2010-01-27T17:34:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3304",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3304#issuecomment-22855",
    "user": "@vbraun"
}
```

Has nothing to do with Debian, maybe that was misleading; summary changed.

The following spkg is patched in a similar way. It essentially contains tabbott's patch, but I found this report only after making the changes myself.

http://www.stp.dias.ie/~vbraun/cddlib-094f.p3.spkg 

Users of the Fedora 12 binary sage distribution must manually re-install mpir-1.2.2.p0.spkg as discussed on http://groups.google.com/group/sage-devel/msg/aec4aa6b3874fe10. This is an unrelated bug of the build system.



---

archive/issue_comments_022856.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-01-27T17:34:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3304",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3304#issuecomment-22856",
    "user": "@vbraun"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_022857.json:
```json
{
    "body": "Changing priority from critical to major.",
    "created_at": "2010-01-27T17:34:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3304",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3304#issuecomment-22857",
    "user": "@vbraun"
}
```

Changing priority from critical to major.



---

archive/issue_comments_022858.json:
```json
{
    "body": "Superseded by #8115",
    "created_at": "2010-01-31T12:57:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3304",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3304#issuecomment-22858",
    "user": "@vbraun"
}
```

Superseded by #8115



---

archive/issue_comments_022859.json:
```json
{
    "body": "\n```\nAs I understand,\n\nhttp://trac.sagemath.org/sage_trac/ticket/3304\n\nshould be just closed, not reviewed, since another ticket took care of\nthe issue.\n\nSince only release managers should close tickets, I am leaving the\nticket as is and posting here.\n\nThank you,\nAndrey\n```\n",
    "created_at": "2010-06-02T23:08:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3304",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3304#issuecomment-22859",
    "user": "@williamstein"
}
```


```
As I understand,

http://trac.sagemath.org/sage_trac/ticket/3304

should be just closed, not reviewed, since another ticket took care of
the issue.

Since only release managers should close tickets, I am leaving the
ticket as is and posting here.

Thank you,
Andrey
```




---

archive/issue_comments_022860.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-02T23:09:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3304",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3304#issuecomment-22860",
    "user": "@williamstein"
}
```

Resolution: fixed
