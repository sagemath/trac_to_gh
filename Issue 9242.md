# Issue 9242: Add docstrings and tests for sage/rings/ideal_monoid.py

archive/issues_009242.json:
```json
{
    "body": "Assignee: mvngu\n\nKeywords: docstring, doctest, ideals\n\n\n```\n----------------------------------------------------------------------\nideal_monoid.py\nERROR: Please add a `TestSuite(s).run()` doctest.\nSCORE ideal_monoid.py: 0% (0 of 6)\n\nMissing documentation:\n         * IdealMonoid(R):\n         * __init__(self, R):\n         * _repr_(self):\n         * ring(self):\n         * __call__(self, x):\n         * _coerce_impl(self, x):\n\n----------------------------------------------------------------------\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9242\n\n",
    "created_at": "2010-06-15T08:51:44Z",
    "labels": [
        "component: doctest coverage",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5.2",
    "title": "Add docstrings and tests for sage/rings/ideal_monoid.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9242",
    "user": "https://github.com/loefflerd"
}
```
Assignee: mvngu

Keywords: docstring, doctest, ideals


```
----------------------------------------------------------------------
ideal_monoid.py
ERROR: Please add a `TestSuite(s).run()` doctest.
SCORE ideal_monoid.py: 0% (0 of 6)

Missing documentation:
         * IdealMonoid(R):
         * __init__(self, R):
         * _repr_(self):
         * ring(self):
         * __call__(self, x):
         * _coerce_impl(self, x):

----------------------------------------------------------------------
```


Issue created by migration from https://trac.sagemath.org/ticket/9242





---

archive/issue_comments_086775.json:
```json
{
    "body": "Here's a patch which gets coverage up to 100%, but one `TestSuite` test fails.",
    "created_at": "2010-06-15T09:18:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9242",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9242#issuecomment-86775",
    "user": "https://github.com/loefflerd"
}
```

Here's a patch which gets coverage up to 100%, but one `TestSuite` test fails.



---

archive/issue_comments_086776.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-06-15T09:18:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9242",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9242#issuecomment-86776",
    "user": "https://github.com/loefflerd"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_086777.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-06-15T10:22:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9242",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9242#issuecomment-86777",
    "user": "https://github.com/aghitza"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_086778.json:
```json
{
    "body": "There is a doctest failure in `structure/coerce.pyx` which is caused by this patch:\n\n\n```\nsage -t -long \"devel/sage/sage/structure/coerce.pyx\"        \n**********************************************************************\nFile \"/mnt/usb1/scratch/ghitza/sage-4.4.4.alpha0-boxen.math.washington.edu-x86_64-Linux/devel/sage/sage/structure/coerce.pyx\", line 357:\n    sage: cm.exception_stack()\nExpected:\n    [(<class 'sage.structure.coerce_exceptions.CoercionException'>, CoercionException(\"BUG: the base_extend method must be defined for 'Monoid of ideals of Integer Ring' (class '<class 'sage.rings.ideal_monoid.IdealMonoid_c'>')\",), <traceback object at ...>), (<type 'exceptions.TypeError'>,  TypeError(\"no common canonical parent for objects with parents: 'Rational Field' and 'Finite Field of size 3'\",),  <traceback object at ...>)]\nGot:\n    [(<class 'sage.structure.coerce_exceptions.CoercionException'>, CoercionException(AttributeError(\"'IdealMonoid_c_with_category' object has no attribute 'base_extend'\",),), <traceback object at 0x1049ea8>), (<type 'exceptions.TypeError'>, TypeError(\"no common canonical parent for objects with parents: 'Rational Field' and 'Finite Field of size 3'\",), <traceback object at 0x1049c20>)]\n```\n\n\nI don't know what's going on.",
    "created_at": "2010-06-15T10:22:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9242",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9242#issuecomment-86778",
    "user": "https://github.com/aghitza"
}
```

There is a doctest failure in `structure/coerce.pyx` which is caused by this patch:


```
sage -t -long "devel/sage/sage/structure/coerce.pyx"        
**********************************************************************
File "/mnt/usb1/scratch/ghitza/sage-4.4.4.alpha0-boxen.math.washington.edu-x86_64-Linux/devel/sage/sage/structure/coerce.pyx", line 357:
    sage: cm.exception_stack()
Expected:
    [(<class 'sage.structure.coerce_exceptions.CoercionException'>, CoercionException("BUG: the base_extend method must be defined for 'Monoid of ideals of Integer Ring' (class '<class 'sage.rings.ideal_monoid.IdealMonoid_c'>')",), <traceback object at ...>), (<type 'exceptions.TypeError'>,  TypeError("no common canonical parent for objects with parents: 'Rational Field' and 'Finite Field of size 3'",),  <traceback object at ...>)]
Got:
    [(<class 'sage.structure.coerce_exceptions.CoercionException'>, CoercionException(AttributeError("'IdealMonoid_c_with_category' object has no attribute 'base_extend'",),), <traceback object at 0x1049ea8>), (<type 'exceptions.TypeError'>, TypeError("no common canonical parent for objects with parents: 'Rational Field' and 'Finite Field of size 3'",), <traceback object at 0x1049c20>)]
```


I don't know what's going on.



---

archive/issue_comments_086779.json:
```json
{
    "body": "patch against 4.4.4.alpha0",
    "created_at": "2010-06-15T10:42:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9242",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9242#issuecomment-86779",
    "user": "https://github.com/loefflerd"
}
```

patch against 4.4.4.alpha0



---

archive/issue_comments_086780.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-06-15T10:44:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9242",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9242#issuecomment-86780",
    "user": "https://github.com/loefflerd"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_086781.json:
```json
{
    "body": "Attachment [trac_9242-ideal_monoid_docs.patch](tarball://root/attachments/some-uuid/ticket9242/trac_9242-ideal_monoid_docs.patch) by @loefflerd created at 2010-06-15 10:44:10\n\nIt's harmess (if you look, the exception stack is actually identical, just with slightly different string representation for some of the classes). I've uploaded a new patch.",
    "created_at": "2010-06-15T10:44:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9242",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9242#issuecomment-86781",
    "user": "https://github.com/loefflerd"
}
```

Attachment [trac_9242-ideal_monoid_docs.patch](tarball://root/attachments/some-uuid/ticket9242/trac_9242-ideal_monoid_docs.patch) by @loefflerd created at 2010-06-15 10:44:10

It's harmess (if you look, the exception stack is actually identical, just with slightly different string representation for some of the classes). I've uploaded a new patch.



---

archive/issue_comments_086782.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-15T11:36:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9242",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9242#issuecomment-86782",
    "user": "https://github.com/aghitza"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_086783.json:
```json
{
    "body": "Great.  I'm happy with this; the category fix can be on a new ticket.",
    "created_at": "2010-06-15T11:36:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9242",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9242#issuecomment-86783",
    "user": "https://github.com/aghitza"
}
```

Great.  I'm happy with this; the category fix can be on a new ticket.



---

archive/issue_comments_086784.json:
```json
{
    "body": "Milestone sage-4.4.5 deleted",
    "created_at": "2010-06-22T04:36:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9242",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9242#issuecomment-86784",
    "user": "https://github.com/williamstein"
}
```

Milestone sage-4.4.5 deleted



---

archive/issue_comments_086785.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-22T07:49:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9242",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9242#issuecomment-86785",
    "user": "https://github.com/dandrake"
}
```

Resolution: fixed
