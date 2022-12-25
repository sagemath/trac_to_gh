# Issue 8068: New mpfr-2.4.1.p1.spkg works with Open Solaris 64 bit

archive/issues_008068.json:
```json
{
    "body": "Assignee: drkirkby\n\nCC:  drkirby @williamstein\n\nLet spkg-install handle SAGE64=\"yes\" on Open Solaris 64 bit.\n\n\nSee here:\n[http://boxen.math.washington.edu/home/jsp/ports/mpfr-2.4.1.p1.spkg](http://boxen.math.washington.edu/home/jsp/ports/mpfr-2.4.1.p1.spkg)\n\n\n\n```\nPASS: tpow_all\n====================\nAll 148 tests passed\n====================\nmake[2]: Leaving directory `/export/home/jaap/Downloads/sage-4.3.1/spkg/build/mpfr-2.4.1.p1/src/tests'\nmake[1]: Leaving directory `/export/home/jaap/Downloads/sage-4.3.1/spkg/build/mpfr-2.4.1.p1/src/tests'\nmake[1]: Entering directory `/export/home/jaap/Downloads/sage-4.3.1/spkg/build/mpfr-2.4.1.p1/src'\nmake[1]: Nothing to be done for `check-am'.\nmake[1]: Leaving directory `/export/home/jaap/Downloads/sage-4.3.1/spkg/build/mpfr-2.4.1.p1/src'\n\nreal 2m15.371s\nuser 1m22.294s\nsys 0m54.607s\nSuccessfully installed mpfr-2.4.1.p1\n\n```\n\nJaap\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8068\n\n",
    "closed_at": "2010-02-11T15:17:33Z",
    "created_at": "2010-01-25T23:41:29Z",
    "labels": [
        "component: porting",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.3",
    "title": "New mpfr-2.4.1.p1.spkg works with Open Solaris 64 bit",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8068",
    "user": "https://github.com/jaapspies"
}
```
Assignee: drkirkby

CC:  drkirby @williamstein

Let spkg-install handle SAGE64="yes" on Open Solaris 64 bit.


See here:
[http://boxen.math.washington.edu/home/jsp/ports/mpfr-2.4.1.p1.spkg](http://boxen.math.washington.edu/home/jsp/ports/mpfr-2.4.1.p1.spkg)



```
PASS: tpow_all
====================
All 148 tests passed
====================
make[2]: Leaving directory `/export/home/jaap/Downloads/sage-4.3.1/spkg/build/mpfr-2.4.1.p1/src/tests'
make[1]: Leaving directory `/export/home/jaap/Downloads/sage-4.3.1/spkg/build/mpfr-2.4.1.p1/src/tests'
make[1]: Entering directory `/export/home/jaap/Downloads/sage-4.3.1/spkg/build/mpfr-2.4.1.p1/src'
make[1]: Nothing to be done for `check-am'.
make[1]: Leaving directory `/export/home/jaap/Downloads/sage-4.3.1/spkg/build/mpfr-2.4.1.p1/src'

real 2m15.371s
user 1m22.294s
sys 0m54.607s
Successfully installed mpfr-2.4.1.p1

```

Jaap



Issue created by migration from https://trac.sagemath.org/ticket/8068





---

archive/issue_comments_070583.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-25T23:41:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8068",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8068#issuecomment-70583",
    "user": "https://github.com/jaapspies"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_070584.json:
```json
{
    "body": "Attachment [mpfr-2.4.1.p1.patch](tarball://root/attachments/some-uuid/ticket8068/mpfr-2.4.1.p1.patch) by @jaapspies created at 2010-01-26 18:49:34",
    "created_at": "2010-01-26T18:49:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8068",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8068#issuecomment-70584",
    "user": "https://github.com/jaapspies"
}
```

Attachment [mpfr-2.4.1.p1.patch](tarball://root/attachments/some-uuid/ticket8068/mpfr-2.4.1.p1.patch) by @jaapspies created at 2010-01-26 18:49:34



---

archive/issue_comments_070585.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-27T12:42:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8068",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8068#issuecomment-70585",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_070586.json:
```json
{
    "body": "Changing type from enhancement to defect.",
    "created_at": "2010-01-27T12:42:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8068",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8068#issuecomment-70586",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing type from enhancement to defect.



---

archive/issue_comments_070587.json:
```json
{
    "body": "This works fine. In fact, the library was already building 64-bit for me, without this patch, but I believe it is safer to have this. I suspect mpfr might actually ignore the CFLAGS and work out what it needs itself, as it is uses mpir, and that would already be configured 64-bit. But I would agree this is desirable to add this. \n\nPositive review.",
    "created_at": "2010-01-27T12:42:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8068",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8068#issuecomment-70587",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

This works fine. In fact, the library was already building 64-bit for me, without this patch, but I believe it is safer to have this. I suspect mpfr might actually ignore the CFLAGS and work out what it needs itself, as it is uses mpir, and that would already be configured 64-bit. But I would agree this is desirable to add this. 

Positive review.



---

archive/issue_comments_070588.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-02-11T15:17:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8068",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8068#issuecomment-70588",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed



---

archive/issue_events_019319.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-02-11T15:17:33Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8068",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8068#event-19319"
}
```
