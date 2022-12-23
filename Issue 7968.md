# Issue 7968: doctest failure in heegner.py (Sage-4.3.1.rc0)

archive/issues_007968.json:
```json
{
    "body": "Assignee: tbd\n\nOn cicero, Fedora 12, 32-bit, Pentium 4,\nand also on cleo, Red Hat Enterprise Linux Server 5.3, 64-bit, IA-64,\nas well as on Mac OS X 10.4, Core2Duo, 32 bit:\n\n[mvngu`@`cicero sage-4.3.1.rc0]$ ./sage -t -long\ndevel/sage-main/sage/schemes/elliptic_curves/heegner.py\nsage -t -long \"devel/sage-main/sage/schemes/elliptic_curves/heegner.py\"\n**********************************************************************\nFile \"/tmp/mvngu/sage-4.3.1.rc0/devel/sage-main/sage/schemes/elliptic_curves/heegner.py\",\nline 1486:\n    sage: s.__cmp__(0)\nExpected:\n    -1\nGot:\n    1\n**********************************************************************\n\nIssue created by migration from https://trac.sagemath.org/ticket/7968\n\n",
    "created_at": "2010-01-17T19:34:31Z",
    "labels": [
        "doctest coverage",
        "major",
        "bug"
    ],
    "title": "doctest failure in heegner.py (Sage-4.3.1.rc0)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7968",
    "user": "GeorgSWeber"
}
```
Assignee: tbd

On cicero, Fedora 12, 32-bit, Pentium 4,
and also on cleo, Red Hat Enterprise Linux Server 5.3, 64-bit, IA-64,
as well as on Mac OS X 10.4, Core2Duo, 32 bit:

[mvngu`@`cicero sage-4.3.1.rc0]$ ./sage -t -long
devel/sage-main/sage/schemes/elliptic_curves/heegner.py
sage -t -long "devel/sage-main/sage/schemes/elliptic_curves/heegner.py"
**********************************************************************
File "/tmp/mvngu/sage-4.3.1.rc0/devel/sage-main/sage/schemes/elliptic_curves/heegner.py",
line 1486:
    sage: s.__cmp__(0)
Expected:
    -1
Got:
    1
**********************************************************************

Issue created by migration from https://trac.sagemath.org/ticket/7968





---

archive/issue_comments_069515.json:
```json
{
    "body": "Is this \"just\" some refactoring fallout?\nAnyone any ideas??\n(Fixing the doctest by itself is obviously trivial ...)",
    "created_at": "2010-01-17T19:37:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7968",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7968#issuecomment-69515",
    "user": "GeorgSWeber"
}
```

Is this "just" some refactoring fallout?
Anyone any ideas??
(Fixing the doctest by itself is obviously trivial ...)



---

archive/issue_comments_069516.json:
```json
{
    "body": "Attachment",
    "created_at": "2010-01-17T22:41:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7968",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7968#issuecomment-69516",
    "user": "was"
}
```

Attachment



---

archive/issue_comments_069517.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2010-01-17T22:41:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7968",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7968#issuecomment-69517",
    "user": "was"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_069518.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-17T22:41:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7968",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7968#issuecomment-69518",
    "user": "was"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_069519.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-17T22:44:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7968",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7968#issuecomment-69519",
    "user": "craigcitro"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_069520.json:
```json
{
    "body": "Yep, this looks good. As William pointed out to me when I asked, the issue is just that the ordering is random -- so just having the doctest confirm that they're not equal is the right thing to do.",
    "created_at": "2010-01-17T22:44:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7968",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7968#issuecomment-69520",
    "user": "craigcitro"
}
```

Yep, this looks good. As William pointed out to me when I asked, the issue is just that the ordering is random -- so just having the doctest confirm that they're not equal is the right thing to do.



---

archive/issue_comments_069521.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-18T22:26:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7968",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7968#issuecomment-69521",
    "user": "rlm"
}
```

Resolution: fixed
