# Issue 2802: Sage 3.0.alpha1: sage/misc/inline_fortran.py doctest failure

archive/issues_002802.json:
```json
{
    "body": "Assignee: jkantor\n\nI am seeing the following failure with 3.0.alpha1 on sage.math:\n\n```\nsage -t -long devel/sage/sage/misc/inline_fortran.py\n**********************************************************************\nFile \"/scratch/mabshoff/release-cycle/sage-3.0.alpha1/tmp/inline_fortran.py\", line 28:\n    sage: test_fortran(s)           # -- requires fortran\nExpected nothing\nGot:\n    Found executable /scratch/mabshoff/release-cycle/sage-3.0.alpha1/local/bin/sage-g77_shared\n    Found executable /scratch/mabshoff/release-cycle/sage-3.0.alpha1/local/bin/sage_fortran\n    Found executable /usr/bin/ld\n    Found executable /usr/bin/ar\n    Found executable /usr/bin/ranlib\n    <BLANKLINE>\n**********************************************************************\nFile \"/scratch/mabshoff/release-cycle/sage-3.0.alpha1/tmp/inline_fortran.py\", line 31:\n    sage: fib(n,int(10))            # -- requires fortran\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/mabshoff/release-cycle/sage-3.0.alpha1/local/lib/python2.5/doctest.py\", line 1212, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_0[7]>\", line 1, in <module>\n        fib(n,int(Integer(10)))            # -- requires fortran###line 31:\n    sage: fib(n,int(10))            # -- requires fortran\n    NameError: name 'fib' is not defined\n**********************************************************************\nFile \"/scratch/mabshoff/release-cycle/sage-3.0.alpha1/tmp/inline_fortran.py\", line 32:\n    sage: n                         # -- requires fortran\nExpected:\n    array([  0.,   1.,   1.,   2.,   3.,   5.,   8.,  13.,  21.,  34.])\nGot:\n    array([ 0.,  1.,  2.,  3.,  4.,  5.,  6.,  7.,  8.,  9.])\n**********************************************************************\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2802\n\n",
    "created_at": "2008-04-05T00:10:01Z",
    "labels": [
        "doctest coverage",
        "blocker",
        "bug"
    ],
    "title": "Sage 3.0.alpha1: sage/misc/inline_fortran.py doctest failure",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2802",
    "user": "mabshoff"
}
```
Assignee: jkantor

I am seeing the following failure with 3.0.alpha1 on sage.math:

```
sage -t -long devel/sage/sage/misc/inline_fortran.py
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.0.alpha1/tmp/inline_fortran.py", line 28:
    sage: test_fortran(s)           # -- requires fortran
Expected nothing
Got:
    Found executable /scratch/mabshoff/release-cycle/sage-3.0.alpha1/local/bin/sage-g77_shared
    Found executable /scratch/mabshoff/release-cycle/sage-3.0.alpha1/local/bin/sage_fortran
    Found executable /usr/bin/ld
    Found executable /usr/bin/ar
    Found executable /usr/bin/ranlib
    <BLANKLINE>
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.0.alpha1/tmp/inline_fortran.py", line 31:
    sage: fib(n,int(10))            # -- requires fortran
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/release-cycle/sage-3.0.alpha1/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[7]>", line 1, in <module>
        fib(n,int(Integer(10)))            # -- requires fortran###line 31:
    sage: fib(n,int(10))            # -- requires fortran
    NameError: name 'fib' is not defined
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.0.alpha1/tmp/inline_fortran.py", line 32:
    sage: n                         # -- requires fortran
Expected:
    array([  0.,   1.,   1.,   2.,   3.,   5.,   8.,  13.,  21.,  34.])
Got:
    array([ 0.,  1.,  2.,  3.,  4.,  5.,  6.,  7.,  8.,  9.])
**********************************************************************
```


Issue created by migration from https://trac.sagemath.org/ticket/2802





---

archive/issue_comments_019233.json:
```json
{
    "body": "This should fix the problem\n\nhttp://sage.math.washington.edu/home/jkantor/patches/inline_fortran_fix.patch",
    "created_at": "2008-04-08T06:43:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2802",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2802#issuecomment-19233",
    "user": "jkantor"
}
```

This should fix the problem

http://sage.math.washington.edu/home/jkantor/patches/inline_fortran_fix.patch



---

archive/issue_comments_019234.json:
```json
{
    "body": "Attachment [inline_fortran_fix.patch](tarball://root/attachments/some-uuid/ticket2802/inline_fortran_fix.patch) by mabshoff created at 2008-04-08 09:00:05\n\njkantor's patch",
    "created_at": "2008-04-08T09:00:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2802",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2802#issuecomment-19234",
    "user": "mabshoff"
}
```

Attachment [inline_fortran_fix.patch](tarball://root/attachments/some-uuid/ticket2802/inline_fortran_fix.patch) by mabshoff created at 2008-04-08 09:00:05

jkantor's patch



---

archive/issue_comments_019235.json:
```json
{
    "body": "The patch does not fix the issue for me. Is this a fix for a general inline Fortran issue?\n\nThoughts?",
    "created_at": "2008-04-08T10:36:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2802",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2802#issuecomment-19235",
    "user": "mabshoff"
}
```

The patch does not fix the issue for me. Is this a fix for a general inline Fortran issue?

Thoughts?



---

archive/issue_comments_019236.json:
```json
{
    "body": "Ok, lets try this one (apply against the previous one)\n\nhttp://sage.math.washington.edu/home/jkantor/patches/inline_fortran_2.patch",
    "created_at": "2008-04-08T16:56:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2802",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2802#issuecomment-19236",
    "user": "jkantor"
}
```

Ok, lets try this one (apply against the previous one)

http://sage.math.washington.edu/home/jkantor/patches/inline_fortran_2.patch



---

archive/issue_comments_019237.json:
```json
{
    "body": "Yep. Both patches together fix the issue. Positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-08T17:54:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2802",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2802#issuecomment-19237",
    "user": "mabshoff"
}
```

Yep. Both patches together fix the issue. Positive review.

Cheers,

Michael



---

archive/issue_comments_019238.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-08T17:54:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2802",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2802#issuecomment-19238",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_019239.json:
```json
{
    "body": "Merged in Sage 3.0.alpha3",
    "created_at": "2008-04-08T17:54:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2802",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2802#issuecomment-19239",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.alpha3



---

archive/issue_comments_019240.json:
```json
{
    "body": "jkantor's second patch",
    "created_at": "2008-04-08T17:56:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2802",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2802#issuecomment-19240",
    "user": "mabshoff"
}
```

jkantor's second patch
