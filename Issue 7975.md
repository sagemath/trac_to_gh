# Issue 7975: remove dsage from sage

archive/issues_007975.json:
```json
{
    "body": "Assignee: tbd\n\nI just noticed that dsage is completely broken in sage-4.3 and sage-4.3.1.rc0, etc.:\n\n```\nsage: dsage.setup()\nsage: D = dsage.start_all()\nsage: a = D('2+3')\nBOOM?\nsage: a\nBOOM!\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7975\n\n",
    "created_at": "2010-01-18T12:42:39Z",
    "labels": [
        "packages: standard",
        "critical",
        "bug"
    ],
    "title": "remove dsage from sage",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7975",
    "user": "was"
}
```
Assignee: tbd

I just noticed that dsage is completely broken in sage-4.3 and sage-4.3.1.rc0, etc.:

```
sage: dsage.setup()
sage: D = dsage.start_all()
sage: a = D('2+3')
BOOM?
sage: a
BOOM!
```


Issue created by migration from https://trac.sagemath.org/ticket/7975





---

archive/issue_comments_069570.json:
```json
{
    "body": "Reminder to anyone who wants to deal with this: in addition to removing any actual dsage code, also remove the sections on dsage from the tutorial (English and French) and reference manual.",
    "created_at": "2010-01-18T15:28:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7975",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7975#issuecomment-69570",
    "user": "jhpalmieri"
}
```

Reminder to anyone who wants to deal with this: in addition to removing any actual dsage code, also remove the sections on dsage from the tutorial (English and French) and reference manual.



---

archive/issue_comments_069571.json:
```json
{
    "body": "Attachment [sagelib-7975-part2-DOCUMENTATION.patch](tarball://root/attachments/some-uuid/ticket7975/sagelib-7975-part2-DOCUMENTATION.patch) by was created at 2010-01-19 06:27:38",
    "created_at": "2010-01-19T06:27:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7975",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7975#issuecomment-69571",
    "user": "was"
}
```

Attachment [sagelib-7975-part2-DOCUMENTATION.patch](tarball://root/attachments/some-uuid/ticket7975/sagelib-7975-part2-DOCUMENTATION.patch) by was created at 2010-01-19 06:27:38



---

archive/issue_comments_069572.json:
```json
{
    "body": "This is the new deps file, which is fine assuming you didn't change the deps file in making the 4.3.1.rc1 release (I just took 4.3.1.rc0's deps and fixed it).",
    "created_at": "2010-01-19T06:39:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7975",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7975#issuecomment-69572",
    "user": "was"
}
```

This is the new deps file, which is fine assuming you didn't change the deps file in making the 4.3.1.rc1 release (I just took 4.3.1.rc0's deps and fixed it).



---

archive/issue_comments_069573.json:
```json
{
    "body": "Attachment [deps](tarball://root/attachments/some-uuid/ticket7975/deps) by was created at 2010-01-19 06:40:31\n\nThis is the new spkg/install file, which is fine assuming you didn't change the install file in making the 4.3.1.rc1 release (I just took 4.3.1.rc0's install and fixed it).",
    "created_at": "2010-01-19T06:40:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7975",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7975#issuecomment-69573",
    "user": "was"
}
```

Attachment [deps](tarball://root/attachments/some-uuid/ticket7975/deps) by was created at 2010-01-19 06:40:31

This is the new spkg/install file, which is fine assuming you didn't change the install file in making the 4.3.1.rc1 release (I just took 4.3.1.rc0's install and fixed it).



---

archive/issue_comments_069574.json:
```json
{
    "body": "Attachment [install](tarball://root/attachments/some-uuid/ticket7975/install) by was created at 2010-01-19 07:17:21",
    "created_at": "2010-01-19T07:17:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7975",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7975#issuecomment-69574",
    "user": "was"
}
```

Attachment [install](tarball://root/attachments/some-uuid/ticket7975/install) by was created at 2010-01-19 07:17:21



---

archive/issue_comments_069575.json:
```json
{
    "body": "Attachment [sagenb-7975.patch](tarball://root/attachments/some-uuid/ticket7975/sagenb-7975.patch) by was created at 2010-01-19 07:20:24\n\nSee http://boxen.math.washington.edu/home/wstein/patches/sagenb/sagenb-0.6.spkg for the new sagenb spkg.",
    "created_at": "2010-01-19T07:20:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7975",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7975#issuecomment-69575",
    "user": "was"
}
```

Attachment [sagenb-7975.patch](tarball://root/attachments/some-uuid/ticket7975/sagenb-7975.patch) by was created at 2010-01-19 07:20:24

See http://boxen.math.washington.edu/home/wstein/patches/sagenb/sagenb-0.6.spkg for the new sagenb spkg.



---

archive/issue_comments_069576.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-19T07:22:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7975",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7975#issuecomment-69576",
    "user": "was"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_069577.json:
```json
{
    "body": "Attachment [scripts-7975.patch](tarball://root/attachments/some-uuid/ticket7975/scripts-7975.patch) by was created at 2010-01-19 07:29:35",
    "created_at": "2010-01-19T07:29:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7975",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7975#issuecomment-69577",
    "user": "was"
}
```

Attachment [scripts-7975.patch](tarball://root/attachments/some-uuid/ticket7975/scripts-7975.patch) by was created at 2010-01-19 07:29:35



---

archive/issue_comments_069578.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-19T07:32:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7975",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7975#issuecomment-69578",
    "user": "rlm"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_069579.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-19T07:33:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7975",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7975#issuecomment-69579",
    "user": "rlm"
}
```

Resolution: fixed
