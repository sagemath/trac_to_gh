# Issue 3316: Fix a bug and improve documentation in jordan_form

archive/issues_003316.json:
```json
{
    "body": "Assignee: @williamstein\n\n\nI submit a patch that fixes a bug in jordan_form method in /matrix/matrix2.pyx\n\n```\nsage: A=Matrix(CDF,[[1,-2],[2,-1]])\nsage: A.jordan_form(transformation=True)\n---------------------------------------------------------------------------\nAttributeError                            Traceback (most recent call last)\n\n/media/hda2/pablo.new_home/sage/sage-3.0.2/<ipython console> in <module>()\n\n/media/hda2/pablo.new_home/sage/sage-3.0.2/matrix2.pyx in sage.matrix.matrix2.Matrix.jordan_form (sage/matrix/matrix2.c:20606)()\n\nAttributeError: 'NoneType' object has no attribute 'is_exact'\n\n``` \n\n(second issue in ticket #3249)\n\nAfter this fix, the behavior will be:\n\n```\n\nsage: A.jordan_form(transformation=True)\n---------------------------------------------------------------------------\nValueError                                Traceback (most recent call last)\n\n/media/hda2/pablo.new_home/sage/sage-3.0.2/<ipython console> in <module>()\n\n/media/hda2/pablo.new_home/sage/sage-3.0.2/matrix2.pyx in sage.matrix.matrix2.Matrix.jordan_form (sage/matrix/matrix2.c:20625)()\n\nValueError: cannot compute the transformation matrix due to lack of precision\n\n```\n\nthat it is what it is intendend in the code.\n\n(The bug was that base_ring.is_exact() was used, instead of self.base_ring().is_exact().\n\nBesides that, this patch improves the documentation of this method, by adding\n\"Transformation\" to the list of INPUT parameters\n\nIssue created by migration from https://trac.sagemath.org/ticket/3316\n\n",
    "created_at": "2008-05-27T23:36:32Z",
    "labels": [
        "component: linear algebra",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.3",
    "title": "Fix a bug and improve documentation in jordan_form",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3316",
    "user": "https://github.com/pdenapo"
}
```
Assignee: @williamstein


I submit a patch that fixes a bug in jordan_form method in /matrix/matrix2.pyx

```
sage: A=Matrix(CDF,[[1,-2],[2,-1]])
sage: A.jordan_form(transformation=True)
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)

/media/hda2/pablo.new_home/sage/sage-3.0.2/<ipython console> in <module>()

/media/hda2/pablo.new_home/sage/sage-3.0.2/matrix2.pyx in sage.matrix.matrix2.Matrix.jordan_form (sage/matrix/matrix2.c:20606)()

AttributeError: 'NoneType' object has no attribute 'is_exact'

``` 

(second issue in ticket #3249)

After this fix, the behavior will be:

```

sage: A.jordan_form(transformation=True)
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)

/media/hda2/pablo.new_home/sage/sage-3.0.2/<ipython console> in <module>()

/media/hda2/pablo.new_home/sage/sage-3.0.2/matrix2.pyx in sage.matrix.matrix2.Matrix.jordan_form (sage/matrix/matrix2.c:20625)()

ValueError: cannot compute the transformation matrix due to lack of precision

```

that it is what it is intendend in the code.

(The bug was that base_ring.is_exact() was used, instead of self.base_ring().is_exact().

Besides that, this patch improves the documentation of this method, by adding
"Transformation" to the list of INPUT parameters

Issue created by migration from https://trac.sagemath.org/ticket/3316





---

archive/issue_comments_022919.json:
```json
{
    "body": "patch for fixing a bug and improving the documentation in jordan_form",
    "created_at": "2008-05-27T23:37:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3316",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3316#issuecomment-22919",
    "user": "https://github.com/pdenapo"
}
```

patch for fixing a bug and improving the documentation in jordan_form



---

archive/issue_comments_022920.json:
```json
{
    "body": "Attachment [jordan_form_fixes.patch](tarball://root/attachments/some-uuid/ticket3316/jordan_form_fixes.patch) by @pdenapo created at 2008-05-27 23:39:40",
    "created_at": "2008-05-27T23:39:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3316",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3316#issuecomment-22920",
    "user": "https://github.com/pdenapo"
}
```

Attachment [jordan_form_fixes.patch](tarball://root/attachments/some-uuid/ticket3316/jordan_form_fixes.patch) by @pdenapo created at 2008-05-27 23:39:40



---

archive/issue_comments_022921.json:
```json
{
    "body": "There are some small doctest issues with the patch applied:\n\n```\nsage -t -long devel/sage/sage/matrix/matrix2.pyx            \n**********************************************************************\nFile \"/scratch/mabshoff/release-cycle/sage-3.0.3.alpha2/tmp/matrix2.py\", line 3640:\n    sage: jf, p = b.jordan_form(RealField(15), transformation=True)\nExpected:\n    Traceback (most recent call last):\n    ...\n    ValueError: cannot compute the transformation matrix due to lack of precision\nGot:\n    Traceback (most recent call last):\n      File \"/scratch/mabshoff/release-cycle/sage-3.0.3.alpha2/local/lib/python2.5/doctest.py\", line 1228, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_71[12]>\", line 1, in <module>\n        jf, p = b.jordan_form(RealField(Integer(15)), transformation=True)###line 3640:\n    sage: jf, p = b.jordan_form(RealField(15), transformation=True)\n      File \"matrix2.pyx\", line 3714, in sage.matrix.matrix2.Matrix.jordan_form (sage/matrix/matrix2.c:20649)\n    ValueError: cannot compute the basis of the Jordan block of size 1 with eigenvalue -1.348\n**********************************************************************\n1 items had failures:\n   1 of  23 in __main__.example_71\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file /scratch/mabshoff/release-cycle/sage-3.0.3.alpha2/tmp/.doctest_matrix2.py\n\t [7.8 s]\nexit code: 1024\n```\n\nCheers,\n\nMichael",
    "created_at": "2008-06-11T04:36:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3316",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3316#issuecomment-22921",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

There are some small doctest issues with the patch applied:

```
sage -t -long devel/sage/sage/matrix/matrix2.pyx            
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.0.3.alpha2/tmp/matrix2.py", line 3640:
    sage: jf, p = b.jordan_form(RealField(15), transformation=True)
Expected:
    Traceback (most recent call last):
    ...
    ValueError: cannot compute the transformation matrix due to lack of precision
Got:
    Traceback (most recent call last):
      File "/scratch/mabshoff/release-cycle/sage-3.0.3.alpha2/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_71[12]>", line 1, in <module>
        jf, p = b.jordan_form(RealField(Integer(15)), transformation=True)###line 3640:
    sage: jf, p = b.jordan_form(RealField(15), transformation=True)
      File "matrix2.pyx", line 3714, in sage.matrix.matrix2.Matrix.jordan_form (sage/matrix/matrix2.c:20649)
    ValueError: cannot compute the basis of the Jordan block of size 1 with eigenvalue -1.348
**********************************************************************
1 items had failures:
   1 of  23 in __main__.example_71
***Test Failed*** 1 failures.
For whitespace errors, see the file /scratch/mabshoff/release-cycle/sage-3.0.3.alpha2/tmp/.doctest_matrix2.py
	 [7.8 s]
exit code: 1024
```

Cheers,

Michael



---

archive/issue_comments_022922.json:
```json
{
    "body": "Attachment [jordan_form_fixes_correction.patch](tarball://root/attachments/some-uuid/ticket3316/jordan_form_fixes_correction.patch) by @pdenapo created at 2008-06-12 02:13:56\n\na new patch (this time correct, I hope)",
    "created_at": "2008-06-12T02:13:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3316",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3316#issuecomment-22922",
    "user": "https://github.com/pdenapo"
}
```

Attachment [jordan_form_fixes_correction.patch](tarball://root/attachments/some-uuid/ticket3316/jordan_form_fixes_correction.patch) by @pdenapo created at 2008-06-12 02:13:56

a new patch (this time correct, I hope)



---

archive/issue_comments_022923.json:
```json
{
    "body": "My previous patch was wrong (in the logic). I'm submitting a new version that is correct (I hope). I've checked it passes the doctest in matrix2.pyx",
    "created_at": "2008-06-12T02:15:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3316",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3316#issuecomment-22923",
    "user": "https://github.com/pdenapo"
}
```

My previous patch was wrong (in the logic). I'm submitting a new version that is correct (I hope). I've checked it passes the doctest in matrix2.pyx



---

archive/issue_comments_022924.json:
```json
{
    "body": "Merged jordan_form_fixes_correction.patch in Sage 3.1.3.alpha2. \n\nPablo: please make sure to post patches and not diffs in the future.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-26T04:47:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3316",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3316#issuecomment-22924",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged jordan_form_fixes_correction.patch in Sage 3.1.3.alpha2. 

Pablo: please make sure to post patches and not diffs in the future.

Cheers,

Michael



---

archive/issue_events_007449.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-09-26T04:47:40Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3316",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3316#event-7449"
}
```



---

archive/issue_comments_022925.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-26T04:47:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3316",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3316#issuecomment-22925",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
