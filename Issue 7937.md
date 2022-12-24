# Issue 7937: Add SASS files to MANIFEST.in

archive/issues_007937.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @TimDumol @williamstein\n\nThe SASS source files from ticket #7269 are missing from [sagenb-0.5.spkg](http://boxen.math.washington.edu/home/wstein/patches/sagenb/sagenb-0.5.spkg):\n\n```sh\nhg stat\n! sass/config.rb\n! sass/readme.txt\n! sass/src/account_settings.sass\n! sass/src/main.sass\n! sass/src/master.sass\n! sass/src/partials/_mixins.sass\n! sass/src/registration.sass\n! sass/src/test_report.sass\n! sass/src/typography/_base.sass\n! sass/src/user_management.sass\n? release_notes.txt\n? setup.cfg\n```\n\nI think we just need to patch the `MANIFEST.in`.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7937\n\n",
    "created_at": "2010-01-15T18:49:44Z",
    "labels": [
        "notebook",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.1",
    "title": "Add SASS files to MANIFEST.in",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7937",
    "user": "@qed777"
}
```
Assignee: @williamstein

CC:  @TimDumol @williamstein

The SASS source files from ticket #7269 are missing from [sagenb-0.5.spkg](http://boxen.math.washington.edu/home/wstein/patches/sagenb/sagenb-0.5.spkg):

```sh
hg stat
! sass/config.rb
! sass/readme.txt
! sass/src/account_settings.sass
! sass/src/main.sass
! sass/src/master.sass
! sass/src/partials/_mixins.sass
! sass/src/registration.sass
! sass/src/test_report.sass
! sass/src/typography/_base.sass
! sass/src/user_management.sass
? release_notes.txt
? setup.cfg
```

I think we just need to patch the `MANIFEST.in`.

Issue created by migration from https://trac.sagemath.org/ticket/7937





---

archive/issue_comments_069207.json:
```json
{
    "body": "Updates `MANIFEST.in` for #7269.  Does *not* include the missing files.  sagenb repo.",
    "created_at": "2010-01-15T19:18:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7937",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7937#issuecomment-69207",
    "user": "@qed777"
}
```

Updates `MANIFEST.in` for #7269.  Does *not* include the missing files.  sagenb repo.



---

archive/issue_comments_069208.json:
```json
{
    "body": "Attachment [trac_7937-sass_manifest.patch](tarball://root/attachments/some-uuid/ticket7937/trac_7937-sass_manifest.patch) by @qed777 created at 2010-01-15 19:20:11",
    "created_at": "2010-01-15T19:20:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7937",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7937#issuecomment-69208",
    "user": "@qed777"
}
```

Attachment [trac_7937-sass_manifest.patch](tarball://root/attachments/some-uuid/ticket7937/trac_7937-sass_manifest.patch) by @qed777 created at 2010-01-15 19:20:11



---

archive/issue_comments_069209.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-15T19:20:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7937",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7937#issuecomment-69209",
    "user": "@qed777"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_069210.json:
```json
{
    "body": "LGTM. Nice catch.",
    "created_at": "2010-01-17T09:09:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7937",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7937#issuecomment-69210",
    "user": "@TimDumol"
}
```

LGTM. Nice catch.



---

archive/issue_comments_069211.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-17T09:09:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7937",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7937#issuecomment-69211",
    "user": "@TimDumol"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_069212.json:
```json
{
    "body": "Changing priority from minor to critical.",
    "created_at": "2010-01-17T09:09:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7937",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7937#issuecomment-69212",
    "user": "@TimDumol"
}
```

Changing priority from minor to critical.



---

archive/issue_comments_069213.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-19T05:04:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7937",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7937#issuecomment-69213",
    "user": "@rlmill"
}
```

Resolution: fixed
