# Issue 6777: segfault with univariate polynomial, realfield, complexfield

archive/issues_006777.json:
```json
{
    "body": "Assignee: malb\n\nCC:  mjo\n\nKeywords: polynomial segfault\n\nThis is with a modified\n\n```\n```\n\n| Sage Version 4.1.rc1, Release Date: 2009-07-07                     |\nMac OS X, Intel hardware.\n\n\n```\nsage: RealField(300)['x']( [ 1, ComplexField(300).gen(), 0 ])\n\n\n------------------------------------------------------------\nUnhandled SIGSEGV: A segmentation fault occured in SAGE.\nThis probably occured because a *compiled* component\nof SAGE has a bug in it (typically accessing invalid memory)\nor is not properly wrapped with _sig_on, _sig_off.\nYou might want to run SAGE under gdb with 'sage -gdb' to debug this.\nSAGE will now terminate (sorry).\n------------------------------------------------------------\n\n\nProcess SAGE exited abnormally with code 1\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6777\n\n",
    "created_at": "2009-08-19T22:48:53Z",
    "labels": [
        "commutative algebra",
        "major",
        "bug"
    ],
    "title": "segfault with univariate polynomial, realfield, complexfield",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6777",
    "user": "ncalexan"
}
```
Assignee: malb

CC:  mjo

Keywords: polynomial segfault

This is with a modified

```
```

| Sage Version 4.1.rc1, Release Date: 2009-07-07                     |
Mac OS X, Intel hardware.


```
sage: RealField(300)['x']( [ 1, ComplexField(300).gen(), 0 ])


------------------------------------------------------------
Unhandled SIGSEGV: A segmentation fault occured in SAGE.
This probably occured because a *compiled* component
of SAGE has a bug in it (typically accessing invalid memory)
or is not properly wrapped with _sig_on, _sig_off.
You might want to run SAGE under gdb with 'sage -gdb' to debug this.
SAGE will now terminate (sorry).
------------------------------------------------------------


Process SAGE exited abnormally with code 1
```


Issue created by migration from https://trac.sagemath.org/ticket/6777





---

archive/issue_comments_055821.json:
```json
{
    "body": "I don't obtain a segmentation fault, but this is on Debian GNU/Linux.\n\nOn [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/d4807256e57cd843), it is discussed that one gets a rather strange phenomenon: Before the traceback starts, some ERROR is printed.\n\n```\nsage: RealField(300)['x']( [ 1, ComplexField(300).gen(), 0 ])\nERROR: An unexpected error occurred while tokenizing input\nThe following traceback may be corrupted or invalid\nThe error message is: ('EOF in multi-line statement', (1375, 0))\n\nERROR: An unexpected error occurred while tokenizing input\nThe following traceback may be corrupted or invalid\nThe error message is: ('EOF in multi-line statement', (1375, 0))\n\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n\n```\n\nI get this with unpatched sage (hence, no segfault), and Michael Orlitzky reports the same after fixing the segfault.\n\nHowever, with some of my patches applied, one simply gets a straight forward traceback:\n\n```\nsage: RealField(300)['x']([ ComplexField(300).gen() ]) \n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n...\nTypeError: Unable to convert x (='1.00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000*I') to real number.\n```\n\n\nCould you test whether #9138 (or perhaps #11900) actually fixes the problem already?",
    "created_at": "2011-12-15T17:44:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6777",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6777#issuecomment-55821",
    "user": "SimonKing"
}
```

I don't obtain a segmentation fault, but this is on Debian GNU/Linux.

On [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/d4807256e57cd843), it is discussed that one gets a rather strange phenomenon: Before the traceback starts, some ERROR is printed.

```
sage: RealField(300)['x']( [ 1, ComplexField(300).gen(), 0 ])
ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (1375, 0))

ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (1375, 0))

---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

```

I get this with unpatched sage (hence, no segfault), and Michael Orlitzky reports the same after fixing the segfault.

However, with some of my patches applied, one simply gets a straight forward traceback:

```
sage: RealField(300)['x']([ ComplexField(300).gen() ]) 
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
...
TypeError: Unable to convert x (='1.00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000*I') to real number.
```


Could you test whether #9138 (or perhaps #11900) actually fixes the problem already?



---

archive/issue_comments_055822.json:
```json
{
    "body": "The fix is in #11900, and it has a positive review, so I'm adding it as a dependency before a doctest can be added.",
    "created_at": "2011-12-15T18:41:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6777",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6777#issuecomment-55822",
    "user": "mjo"
}
```

The fix is in #11900, and it has a positive review, so I'm adding it as a dependency before a doctest can be added.



---

archive/issue_comments_055823.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2011-12-15T18:51:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6777",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6777#issuecomment-55823",
    "user": "mjo"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_055824.json:
```json
{
    "body": "Patch to add a doctest expecting a TypeError",
    "created_at": "2011-12-17T20:54:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6777",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6777#issuecomment-55824",
    "user": "mhansen"
}
```

Patch to add a doctest expecting a TypeError



---

archive/issue_comments_055825.json:
```json
{
    "body": "Attachment [sage-trac_6777.patch](tarball://root/attachments/some-uuid/ticket6777/sage-trac_6777.patch) by mhansen created at 2011-12-17 20:55:16\n\nmjo's patch looks good to me.  I updated the formatting slightly.",
    "created_at": "2011-12-17T20:55:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6777",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6777#issuecomment-55825",
    "user": "mhansen"
}
```

Attachment [sage-trac_6777.patch](tarball://root/attachments/some-uuid/ticket6777/sage-trac_6777.patch) by mhansen created at 2011-12-17 20:55:16

mjo's patch looks good to me.  I updated the formatting slightly.



---

archive/issue_comments_055826.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-12-17T20:55:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6777",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6777#issuecomment-55826",
    "user": "mhansen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_055827.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2012-01-18T08:08:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6777",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6777#issuecomment-55827",
    "user": "jdemeyer"
}
```

Resolution: fixed
