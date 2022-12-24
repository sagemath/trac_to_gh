# Issue 9914: fixes for NZMATH/Sage interoperation

archive/issues_009914.json:
```json
{
    "body": "Assignee: AlexGhitza\n\nKeywords: NZMATH\n\nNZMATH uses a subtype of Python's \"long\" for its bignum type.  This works fine with plain mpmath, but when mpmath runs under Sage it uses Cython code that's incompatible with NZMATH.  This patch fixes mpmath-under-sage to fix some incompatibilities with NZMATH.  (It also modifies ZZ to allow initialization from a subclass of int/long/float.)\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9915\n\n",
    "created_at": "2010-09-16T08:48:13Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6",
    "title": "fixes for NZMATH/Sage interoperation",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9914",
    "user": "cwitty"
}
```
Assignee: AlexGhitza

Keywords: NZMATH

NZMATH uses a subtype of Python's "long" for its bignum type.  This works fine with plain mpmath, but when mpmath runs under Sage it uses Cython code that's incompatible with NZMATH.  This patch fixes mpmath-under-sage to fix some incompatibilities with NZMATH.  (It also modifies ZZ to allow initialization from a subclass of int/long/float.)


Issue created by migration from https://trac.sagemath.org/ticket/9915





---

archive/issue_comments_098647.json:
```json
{
    "body": "Attachment [trac9915_nzmath-mpmath-fixes.patch](tarball://root/attachments/some-uuid/ticket9915/trac9915_nzmath-mpmath-fixes.patch) by cwitty created at 2010-09-16 08:51:45",
    "created_at": "2010-09-16T08:51:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9914",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9914#issuecomment-98647",
    "user": "cwitty"
}
```

Attachment [trac9915_nzmath-mpmath-fixes.patch](tarball://root/attachments/some-uuid/ticket9915/trac9915_nzmath-mpmath-fixes.patch) by cwitty created at 2010-09-16 08:51:45



---

archive/issue_comments_098648.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-09-16T08:52:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9914",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9914#issuecomment-98648",
    "user": "cwitty"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_098649.json:
```json
{
    "body": "Any additional (`--[only-]optional[=...]`) tests to run with NZMATH installed?",
    "created_at": "2010-09-16T11:32:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9914",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9914#issuecomment-98649",
    "user": "leif"
}
```

Any additional (`--[only-]optional[=...]`) tests to run with NZMATH installed?



---

archive/issue_comments_098650.json:
```json
{
    "body": "Patch looks reasonable, and doesn't cause additional doctest failures when running `ptestlong` on (not yet released) Sage 4.6.alpha1 (with NZMATH 1.0.0 installed; Ubuntu 10.04 x86_64).\n\nPositive review so far, still looking for optional NZMATH doctests... ;-)",
    "created_at": "2010-09-16T13:02:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9914",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9914#issuecomment-98650",
    "user": "leif"
}
```

Patch looks reasonable, and doesn't cause additional doctest failures when running `ptestlong` on (not yet released) Sage 4.6.alpha1 (with NZMATH 1.0.0 installed; Ubuntu 10.04 x86_64).

Positive review so far, still looking for optional NZMATH doctests... ;-)



---

archive/issue_comments_098651.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-09-16T13:02:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9914",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9914#issuecomment-98651",
    "user": "leif"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_098652.json:
```json
{
    "body": "Replying to [comment:3 leif]:\n> ... still looking for optional NZMATH doctests... ;-)\n\nCouldn't find any; also, NZMATH doesn't have an `spkg-check` file.",
    "created_at": "2010-09-16T13:54:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9914",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9914#issuecomment-98652",
    "user": "leif"
}
```

Replying to [comment:3 leif]:
> ... still looking for optional NZMATH doctests... ;-)

Couldn't find any; also, NZMATH doesn't have an `spkg-check` file.



---

archive/issue_comments_098653.json:
```json
{
    "body": "Is\n\n```\nsage: from nzmath import *\n```\n\nsupposed to work? (Gives deprecation warnings and an attribute error.)\n\nBut the following works:\n\n```\nsage: import nzmath.rational\nsage: r = nzmath.rational.Rational(113r, 355r)\nsage: print r\n113/355\nsage: \n```\n\nThat's of course not much of a test. ;-)",
    "created_at": "2010-09-16T14:30:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9914",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9914#issuecomment-98653",
    "user": "leif"
}
```

Is

```
sage: from nzmath import *
```

supposed to work? (Gives deprecation warnings and an attribute error.)

But the following works:

```
sage: import nzmath.rational
sage: r = nzmath.rational.Rational(113r, 355r)
sage: print r
113/355
sage: 
```

That's of course not much of a test. ;-)



---

archive/issue_comments_098654.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-09-29T10:48:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9914",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9914#issuecomment-98654",
    "user": "mpatel"
}
```

Resolution: fixed
