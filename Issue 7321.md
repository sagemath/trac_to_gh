# Issue 7321: numpy fails to build on cygwin due to not using the correct fortran compiler

archive/issues_007321.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  was\n\nThe solution is to add 'sage_fortran' to the beginning of the list of fortran compilers on the cygwin line in src/numpy/distutils/fcompiler/__init__.py\n\nIssue created by migration from https://trac.sagemath.org/ticket/7321\n\n",
    "created_at": "2009-10-27T05:17:15Z",
    "labels": [
        "porting: Cygwin",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.1",
    "title": "numpy fails to build on cygwin due to not using the correct fortran compiler",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7321",
    "user": "mhansen"
}
```
Assignee: tbd

CC:  was

The solution is to add 'sage_fortran' to the beginning of the list of fortran compilers on the cygwin line in src/numpy/distutils/fcompiler/__init__.py

Issue created by migration from https://trac.sagemath.org/ticket/7321





---

archive/issue_comments_061174.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-10-27T14:10:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7321",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7321#issuecomment-61174",
    "user": "mhansen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_061175.json:
```json
{
    "body": "The spkg can be found a http://sage.math.washington.edu/home/mhansen/numpy-1.3.0.p3.spkg",
    "created_at": "2009-10-27T14:10:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7321",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7321#issuecomment-61175",
    "user": "mhansen"
}
```

The spkg can be found a http://sage.math.washington.edu/home/mhansen/numpy-1.3.0.p3.spkg



---

archive/issue_comments_061176.json:
```json
{
    "body": "Attachment [trac_7321-1.patch](tarball://root/attachments/some-uuid/ticket7321/trac_7321-1.patch) by mhansen created at 2010-01-03 16:40:16",
    "created_at": "2010-01-03T16:40:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7321",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7321#issuecomment-61176",
    "user": "mhansen"
}
```

Attachment [trac_7321-1.patch](tarball://root/attachments/some-uuid/ticket7321/trac_7321-1.patch) by mhansen created at 2010-01-03 16:40:16



---

archive/issue_comments_061177.json:
```json
{
    "body": "Attachment [trac_7321-2.patch](tarball://root/attachments/some-uuid/ticket7321/trac_7321-2.patch) by mhansen created at 2010-01-03 16:40:27",
    "created_at": "2010-01-03T16:40:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7321",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7321#issuecomment-61177",
    "user": "mhansen"
}
```

Attachment [trac_7321-2.patch](tarball://root/attachments/some-uuid/ticket7321/trac_7321-2.patch) by mhansen created at 2010-01-03 16:40:27



---

archive/issue_comments_061178.json:
```json
{
    "body": "trac_7321-1.patch appears to already be part of numpy-1.3.0.p2 and I won't comment on it.\n\ntrac_7321-2.patch appears to be correct and I'll give it a positive review.\n\nOTOH, comparing numpy-1.3.0p2.spkg in sage-4.3 with mhansen/numpy-1.3.0.p3.spkg shows a number of other differences which shouldn't be present:\n* Various emacs backup files (*~) exist\n* Various *.pyc files exist\n* patches/cygwin-core-setup.py has been copied to src/numpy/core/setup.py\n* patches/!__init!__.py has been copied to src/numpy/distutils/fcompiler/!__init!__.py\n* patches/gnu.py has been copied to src/numpy/distutils/fcompiler/gnu.py\n* patches/cygwin-lapack_lite-setup.py has been copied to src/numpy/linalg/setup.py\n* src/site.cfg exists\n* src/build exists\nOverall, your numpy-1.3.0.p3.spkg needs rerolling to only include the changes in trac_7321-2.patch",
    "created_at": "2010-01-03T23:38:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7321",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7321#issuecomment-61178",
    "user": "pjeremy"
}
```

trac_7321-1.patch appears to already be part of numpy-1.3.0.p2 and I won't comment on it.

trac_7321-2.patch appears to be correct and I'll give it a positive review.

OTOH, comparing numpy-1.3.0p2.spkg in sage-4.3 with mhansen/numpy-1.3.0.p3.spkg shows a number of other differences which shouldn't be present:
* Various emacs backup files (*~) exist
* Various *.pyc files exist
* patches/cygwin-core-setup.py has been copied to src/numpy/core/setup.py
* patches/!__init!__.py has been copied to src/numpy/distutils/fcompiler/!__init!__.py
* patches/gnu.py has been copied to src/numpy/distutils/fcompiler/gnu.py
* patches/cygwin-lapack_lite-setup.py has been copied to src/numpy/linalg/setup.py
* src/site.cfg exists
* src/build exists
Overall, your numpy-1.3.0.p3.spkg needs rerolling to only include the changes in trac_7321-2.patch



---

archive/issue_comments_061179.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-01-03T23:38:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7321",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7321#issuecomment-61179",
    "user": "pjeremy"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_061180.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-04-06T18:44:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7321",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7321#issuecomment-61180",
    "user": "mhansen"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_061181.json:
```json
{
    "body": "I've posted a new spkg based on p2 with only trac_7321-2.patch applied.  That should address the above concerns.",
    "created_at": "2010-04-06T18:44:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7321",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7321#issuecomment-61181",
    "user": "mhansen"
}
```

I've posted a new spkg based on p2 with only trac_7321-2.patch applied.  That should address the above concerns.



---

archive/issue_comments_061182.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-04-27T00:10:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7321",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7321#issuecomment-61182",
    "user": "was"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_061183.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-04-29T05:05:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7321",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7321#issuecomment-61183",
    "user": "was"
}
```

Resolution: fixed
