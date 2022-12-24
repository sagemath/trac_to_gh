# Issue 8179: configure Mercurial to ignore two binaries by cddlib

archive/issues_008179.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  @vbraun mhampton\n\nThe package cddlib-094f.p?.spkg places two new binaries under the directory $SAGE_LOCAL/bin, in particular:\n\n```\n[mvngu@mod bin]$ pwd\n/scratch/mvngu/release/sage-4.3.2.alpha1/local/bin\n[mvngu@mod bin]$ hg st\n? cdd_both_reps\n? cdd_both_reps_gmp\n```\n\nThese are required by the rewritten polyhedra package at #7109. A patch to $SAGE_LOCAL/bin/.hgignore is attached.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8179\n\n",
    "created_at": "2010-02-03T19:41:59Z",
    "labels": [
        "misc",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.2",
    "title": "configure Mercurial to ignore two binaries by cddlib",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8179",
    "user": "mvngu"
}
```
Assignee: tbd

CC:  @vbraun mhampton

The package cddlib-094f.p?.spkg places two new binaries under the directory $SAGE_LOCAL/bin, in particular:

```
[mvngu@mod bin]$ pwd
/scratch/mvngu/release/sage-4.3.2.alpha1/local/bin
[mvngu@mod bin]$ hg st
? cdd_both_reps
? cdd_both_reps_gmp
```

These are required by the rewritten polyhedra package at #7109. A patch to $SAGE_LOCAL/bin/.hgignore is attached.

Issue created by migration from https://trac.sagemath.org/ticket/8179





---

archive/issue_comments_072082.json:
```json
{
    "body": "apply to script repository",
    "created_at": "2010-02-03T19:43:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8179",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8179#issuecomment-72082",
    "user": "mvngu"
}
```

apply to script repository



---

archive/issue_comments_072083.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-03T19:45:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8179",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8179#issuecomment-72083",
    "user": "mvngu"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_072084.json:
```json
{
    "body": "Attachment [trac_8179-cddlib-local-bin-hgignore.patch](tarball://root/attachments/some-uuid/ticket8179/trac_8179-cddlib-local-bin-hgignore.patch) by mvngu created at 2010-02-03 19:45:00",
    "created_at": "2010-02-03T19:45:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8179",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8179#issuecomment-72084",
    "user": "mvngu"
}
```

Attachment [trac_8179-cddlib-local-bin-hgignore.patch](tarball://root/attachments/some-uuid/ticket8179/trac_8179-cddlib-local-bin-hgignore.patch) by mvngu created at 2010-02-03 19:45:00



---

archive/issue_comments_072085.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2010-02-03T22:11:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8179",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8179#issuecomment-72085",
    "user": "mvngu"
}
```

Looks good to me.



---

archive/issue_comments_072086.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-02-03T22:11:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8179",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8179#issuecomment-72086",
    "user": "mvngu"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_072087.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-02-03T22:12:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8179",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8179#issuecomment-72087",
    "user": "mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_072088.json:
```json
{
    "body": "Merged [trac_8179-cddlib-local-bin-hgignore.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8179/trac_8179-cddlib-local-bin-hgignore.patch). vbraun --- please remember to put your username and the ticket number on your patches. I have committed the above patch in your name.",
    "created_at": "2010-02-03T22:12:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8179",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8179#issuecomment-72088",
    "user": "mvngu"
}
```

Merged [trac_8179-cddlib-local-bin-hgignore.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8179/trac_8179-cddlib-local-bin-hgignore.patch). vbraun --- please remember to put your username and the ticket number on your patches. I have committed the above patch in your name.
