# Issue 8068: New mpfr-2.4.1.p1.spkg works with Open Solaris 64 bit

archive/issues_008068.json:
```json
{
    "body": "Assignee: drkirkby\n\nCC:  drkirby was\n\nLet spkg-install handle SAGE64=\"yes\" on Open Solaris 65 bit.\n\n\nSee here:\n[http://boxen.math.washington.edu/home/jsp/ports/mpfr-2.4.1.p1.spkg](http://boxen.math.washington.edu/home/jsp/ports/mpfr-2.4.1.p1.spkg)\n\n\n\n\n```\nPASS: tpow_all\n====================\nAll 148 tests passed\n====================\nmake[2]: Leaving directory `/export/home/jaap/Downloads/sage-4.3.1/spkg/build/mpfr-2.4.1.p1/src/tests'\nmake[1]: Leaving directory `/export/home/jaap/Downloads/sage-4.3.1/spkg/build/mpfr-2.4.1.p1/src/tests'\nmake[1]: Entering directory `/export/home/jaap/Downloads/sage-4.3.1/spkg/build/mpfr-2.4.1.p1/src'\nmake[1]: Nothing to be done for `check-am'.\nmake[1]: Leaving directory `/export/home/jaap/Downloads/sage-4.3.1/spkg/build/mpfr-2.4.1.p1/src'\n\nreal\t2m15.371s\nuser\t1m22.294s\nsys\t0m54.607s\nSuccessfully installed mpfr-2.4.1.p1\n\n```\n\n\nJaap\n\nIssue created by migration from https://trac.sagemath.org/ticket/8068\n\n",
    "created_at": "2010-01-25T23:41:29Z",
    "labels": [
        "porting",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.3",
    "title": "New mpfr-2.4.1.p1.spkg works with Open Solaris 64 bit",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8068",
    "user": "jsp"
}
```
Assignee: drkirkby

CC:  drkirby was

Let spkg-install handle SAGE64="yes" on Open Solaris 65 bit.


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

real	2m15.371s
user	1m22.294s
sys	0m54.607s
Successfully installed mpfr-2.4.1.p1

```


Jaap

Issue created by migration from https://trac.sagemath.org/ticket/8068





---

archive/issue_comments_070704.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-25T23:41:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8068",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8068#issuecomment-70704",
    "user": "jsp"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_070705.json:
```json
{
    "body": "Attachment [mpfr-2.4.1.p1.patch](tarball://root/attachments/some-uuid/ticket8068/mpfr-2.4.1.p1.patch) by jsp created at 2010-01-26 18:49:34",
    "created_at": "2010-01-26T18:49:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8068",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8068#issuecomment-70705",
    "user": "jsp"
}
```

Attachment [mpfr-2.4.1.p1.patch](tarball://root/attachments/some-uuid/ticket8068/mpfr-2.4.1.p1.patch) by jsp created at 2010-01-26 18:49:34



---

archive/issue_comments_070706.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-27T12:42:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8068",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8068#issuecomment-70706",
    "user": "drkirkby"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_070707.json:
```json
{
    "body": "Changing type from enhancement to defect.",
    "created_at": "2010-01-27T12:42:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8068",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8068#issuecomment-70707",
    "user": "drkirkby"
}
```

Changing type from enhancement to defect.



---

archive/issue_comments_070708.json:
```json
{
    "body": "This works fine. In fact, the library was already building 64-bit for me, without this patch, but I believe it is safer to have this. I suspect mpfr might actually ignore the CFLAGS and work out what it needs itself, as it is uses mpir, and that would already be configured 64-bit. But I would agree this is desirable to add this. \n\nPositive review.",
    "created_at": "2010-01-27T12:42:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8068",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8068#issuecomment-70708",
    "user": "drkirkby"
}
```

This works fine. In fact, the library was already building 64-bit for me, without this patch, but I believe it is safer to have this. I suspect mpfr might actually ignore the CFLAGS and work out what it needs itself, as it is uses mpir, and that would already be configured 64-bit. But I would agree this is desirable to add this. 

Positive review.



---

archive/issue_comments_070709.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-02-11T15:17:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8068",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8068#issuecomment-70709",
    "user": "mpatel"
}
```

Resolution: fixed
