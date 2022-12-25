# Issue 8276: The one of MatrixSpace can be changed !

archive/issues_008276.json:
```json
{
    "body": "Assignee: @hivert\n\nCC:  mraum\n\nKeywords: One mutable.\n\n\n```\nsage: A = MatrixSpace(ZZ, 3)\nsage: A.one()\n[1 0 0]\n[0 1 0]\n[0 0 1]\nsage: A.one()[1,2] = 1\nsage: A.one()\n[1 0 0]\n[0 1 1]\n[0 0 1]\n```\n\nIndeed it is mutable an cached !\n\nIssue created by migration from https://trac.sagemath.org/ticket/8276\n\n",
    "created_at": "2010-02-15T20:49:35Z",
    "labels": [
        "component: algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.4",
    "title": "The one of MatrixSpace can be changed !",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8276",
    "user": "https://github.com/hivert"
}
```
Assignee: @hivert

CC:  mraum

Keywords: One mutable.


```
sage: A = MatrixSpace(ZZ, 3)
sage: A.one()
[1 0 0]
[0 1 0]
[0 0 1]
sage: A.one()[1,2] = 1
sage: A.one()
[1 0 0]
[0 1 1]
[0 0 1]
```

Indeed it is mutable an cached !

Issue created by migration from https://trac.sagemath.org/ticket/8276





---

archive/issue_comments_073144.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2010-02-16T23:35:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8276",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8276#issuecomment-73144",
    "user": "https://github.com/hivert"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_073145.json:
```json
{
    "body": "Correcting MatrixSpace is easy, however there are a lot of places in sage where people create a matrix from the one or zero and modify it after that. I nearly corrected all these occurences. However, I'm stuck with those three files which are very complicated and depend one of each other:\n\n```\n    sage/modular/quatalg/brandt.py\n    sage/algebras/quatalg/quaternion_algebra.py\n    sage/schemes/elliptic_curves/heegner.py\n```\n\nThere are a lot of error but I can't find where it's coming from. I really\ncould use the help of a specialist. \n\nApply the patch in the following order:\n\n```\n    trac_8276-MatrixSpace_one-fh.patch\n    trac_8276-fix_sagelib-fh.patch\n```\n\nThanks for any suggestion.",
    "created_at": "2010-02-16T23:35:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8276",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8276#issuecomment-73145",
    "user": "https://github.com/hivert"
}
```

Correcting MatrixSpace is easy, however there are a lot of places in sage where people create a matrix from the one or zero and modify it after that. I nearly corrected all these occurences. However, I'm stuck with those three files which are very complicated and depend one of each other:

```
    sage/modular/quatalg/brandt.py
    sage/algebras/quatalg/quaternion_algebra.py
    sage/schemes/elliptic_curves/heegner.py
```

There are a lot of error but I can't find where it's coming from. I really
could use the help of a specialist. 

Apply the patch in the following order:

```
    trac_8276-MatrixSpace_one-fh.patch
    trac_8276-fix_sagelib-fh.patch
```

Thanks for any suggestion.



---

archive/issue_comments_073146.json:
```json
{
    "body": "Attachment [trac_8276-fix_sagelib-fh.2.patch](tarball://root/attachments/some-uuid/ticket8276/trac_8276-fix_sagelib-fh.2.patch) by @hivert created at 2010-02-16 23:54:45",
    "created_at": "2010-02-16T23:54:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8276",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8276#issuecomment-73146",
    "user": "https://github.com/hivert"
}
```

Attachment [trac_8276-fix_sagelib-fh.2.patch](tarball://root/attachments/some-uuid/ticket8276/trac_8276-fix_sagelib-fh.2.patch) by @hivert created at 2010-02-16 23:54:45



---

archive/issue_comments_073147.json:
```json
{
    "body": "I finally manage to get those !!! It should be ready for review. Apply\n\n```\n    trac_8276-MatrixSpace_one-fh.patch\n    trac_8276-fix_sagelib-fh.2.patch\n```\n\n\nFlorent",
    "created_at": "2010-02-16T23:56:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8276",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8276#issuecomment-73147",
    "user": "https://github.com/hivert"
}
```

I finally manage to get those !!! It should be ready for review. Apply

```
    trac_8276-MatrixSpace_one-fh.patch
    trac_8276-fix_sagelib-fh.2.patch
```


Florent



---

archive/issue_comments_073148.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-02-16T23:56:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8276",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8276#issuecomment-73148",
    "user": "https://github.com/hivert"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_073149.json:
```json
{
    "body": "I just added a third patch which fixes a non working optimization when creating the zero matrix from `MS(0)` or `MS()`. They are now nearly as fast as calling `copy(MS.zero_matrix())`.\n\nApply this patch after the two others.",
    "created_at": "2010-02-17T10:43:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8276",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8276#issuecomment-73149",
    "user": "https://github.com/hivert"
}
```

I just added a third patch which fixes a non working optimization when creating the zero matrix from `MS(0)` or `MS()`. They are now nearly as fast as calling `copy(MS.zero_matrix())`.

Apply this patch after the two others.



---

archive/issue_comments_073150.json:
```json
{
    "body": "Changing component from algebra to linear algebra.",
    "created_at": "2010-02-17T11:04:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8276",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8276#issuecomment-73150",
    "user": "https://github.com/hivert"
}
```

Changing component from algebra to linear algebra.



---

archive/issue_comments_073151.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-02-17T11:17:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8276",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8276#issuecomment-73151",
    "user": "https://github.com/hivert"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_073152.json:
```json
{
    "body": "The last improvement patch breaks something...",
    "created_at": "2010-02-17T11:17:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8276",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8276#issuecomment-73152",
    "user": "https://github.com/hivert"
}
```

The last improvement patch breaks something...



---

archive/issue_comments_073153.json:
```json
{
    "body": "Attachment [trac_8276-fix_sagelib-fh.patch](tarball://root/attachments/some-uuid/ticket8276/trac_8276-fix_sagelib-fh.patch) by @hivert created at 2010-02-17 17:54:54",
    "created_at": "2010-02-17T17:54:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8276",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8276#issuecomment-73153",
    "user": "https://github.com/hivert"
}
```

Attachment [trac_8276-fix_sagelib-fh.patch](tarball://root/attachments/some-uuid/ticket8276/trac_8276-fix_sagelib-fh.patch) by @hivert created at 2010-02-17 17:54:54



---

archive/issue_comments_073154.json:
```json
{
    "body": "At last thing should be OK ! Please apply in the following order:\n\n```\ntrac_8276-MatrixSpace_one-fh.patch\ntrac_8276-fix_sagelib-fh.patch\ntrac_8276-fix_zero_matrix_creation-fh.patch\n```\n\nDepends on #8294\n\nThe first patch makes the matrices immutable, the second one fixes Sage's lib accordingly the thirds patch simplifies and optimizes the creation of the zero matrix.",
    "created_at": "2010-02-17T18:09:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8276",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8276#issuecomment-73154",
    "user": "https://github.com/hivert"
}
```

At last thing should be OK ! Please apply in the following order:

```
trac_8276-MatrixSpace_one-fh.patch
trac_8276-fix_sagelib-fh.patch
trac_8276-fix_zero_matrix_creation-fh.patch
```

Depends on #8294

The first patch makes the matrices immutable, the second one fixes Sage's lib accordingly the thirds patch simplifies and optimizes the creation of the zero matrix.



---

archive/issue_comments_073155.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-02-17T18:09:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8276",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8276#issuecomment-73155",
    "user": "https://github.com/hivert"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_073156.json:
```json
{
    "body": "Attachment [trac_8276-fix_zero_matrix_creation-fh.patch](tarball://root/attachments/some-uuid/ticket8276/trac_8276-fix_zero_matrix_creation-fh.patch) by @hivert created at 2010-02-20 13:55:21",
    "created_at": "2010-02-20T13:55:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8276",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8276#issuecomment-73156",
    "user": "https://github.com/hivert"
}
```

Attachment [trac_8276-fix_zero_matrix_creation-fh.patch](tarball://root/attachments/some-uuid/ticket8276/trac_8276-fix_zero_matrix_creation-fh.patch) by @hivert created at 2010-02-20 13:55:21



---

archive/issue_comments_073157.json:
```json
{
    "body": "Oups ! I just realize I forgot to reupload `trac_8276-fix_zero_matrix_creation-fh.patch` after a last minor change. Many apologies if you started to review ! For info here is the changelog between the two last version of the patch\n\n```\n    2.31 @@ -85,6 +85,8 @@\n    2.32               []\n    2.33  +            sage: mat.is_mutable()\n    2.34  +            False\n    2.35 ++            sage: MM.zero().is_mutable()\n    2.36 ++            False\n    2.37           \"\"\"\n    2.38  -        try:\n    2.39  -            z = self.__zero_matrix\n    2.40 @@ -98,6 +100,8 @@\n    2.41  +        res.set_immutable()\n    2.42  +        return res\n    2.43  +\n    2.44 ++    zero = zero_matrix\n    2.45 ++\n    2.46       def ngens(self):\n    2.47           \"\"\"\n    2.48           Return the number of generators of this matrix space,\n```\n\nAgain, sorry for any inconvenience.\n\nFlorent",
    "created_at": "2010-02-20T13:59:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8276",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8276#issuecomment-73157",
    "user": "https://github.com/hivert"
}
```

Oups ! I just realize I forgot to reupload `trac_8276-fix_zero_matrix_creation-fh.patch` after a last minor change. Many apologies if you started to review ! For info here is the changelog between the two last version of the patch

```
    2.31 @@ -85,6 +85,8 @@
    2.32               []
    2.33  +            sage: mat.is_mutable()
    2.34  +            False
    2.35 ++            sage: MM.zero().is_mutable()
    2.36 ++            False
    2.37           """
    2.38  -        try:
    2.39  -            z = self.__zero_matrix
    2.40 @@ -98,6 +100,8 @@
    2.41  +        res.set_immutable()
    2.42  +        return res
    2.43  +
    2.44 ++    zero = zero_matrix
    2.45 ++
    2.46       def ngens(self):
    2.47           """
    2.48           Return the number of generators of this matrix space,
```

Again, sorry for any inconvenience.

Florent



---

archive/issue_comments_073158.json:
```json
{
    "body": "Martin Raum: I understand from #8294 that you intend to review this ticket quickly ! I allowed myself to put you in CC of this ticket ! Please make sure that you have the latest version of `trac_8276-fix_zero_matrix_creation-fh.patch`. I forgot to reupload it after a last change (see my previous message). \n\nThanks for your help !",
    "created_at": "2010-02-20T14:06:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8276",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8276#issuecomment-73158",
    "user": "https://github.com/hivert"
}
```

Martin Raum: I understand from #8294 that you intend to review this ticket quickly ! I allowed myself to put you in CC of this ticket ! Please make sure that you have the latest version of `trac_8276-fix_zero_matrix_creation-fh.patch`. I forgot to reupload it after a last change (see my previous message). 

Thanks for your help !



---

archive/issue_comments_073159.json:
```json
{
    "body": "Applied the following patches (in the order below).\n\n\ntrac_8276-MatrixSpace_one-fh.patch\n\n\ntrac_8276-fix_sagelib-fh.patch\n\n\ntrac_8276-fix_zero_matrix_creation-fh.patch\n\n\ntrac_8294-matrix_2x2_copy_mutability_fix-fh.patch\n\n\n*Almost* everything seems straightforward and correct but... Seems that MM(0) which has a \"mutable == True\" property/value should be updatable but the example \"MM(0)[1,2] = 3\" doesnt update MM(0) (see example below) Is that right?\n\n\n\n```\n# prepatch responses\nsage: sage: MM = MatrixSpace(ZZ, 3,3)\nsage: sage: MM(0).is_mutable()\nTrue\nsage: sage: MM.zero_matrix().is_mutable()\nTrue\nsage: sage: MM(1).is_mutable()\nTrue\nsage: sage: MM.identity_matrix().is_mutable()\nTrue\nsage: sage: timeit(\"MM(0)\")\n625 loops, best of 3: 51.1 \u00b5s per loop\nsage: sage: timeit(\"copy(MM.zero_matrix())\")\n625 loops, best of 3: 19.3 \u00b5s per loop\nsage: sage: timeit(\"MM(1)\")\n625 loops, best of 3: 65 \u00b5s per loop\nsage: sage: timeit(\"copy(MM.identity_matrix())\")\n625 loops, best of 3: 60.7 \u00b5s per loop\n\n# postpatch responses\nsage: MM = MatrixSpace(ZZ, 3,3)\nsage: MM(0).is_mutable()\nTrue\nsage: MM.zero_matrix().is_mutable()\nFalse\nsage: MM(1).is_mutable()\nTrue\nsage: MM.identity_matrix().is_mutable()\nFalse\nsage: timeit(\"MM(0)\")\n625 loops, best of 3: 35.9 \u00b5s per loop\nsage: timeit(\"copy(MM.zero_matrix())\")\n625 loops, best of 3: 29.3 \u00b5s per loop\nsage: timeit(\"MM(1)\")\n625 loops, best of 3: 46.1 \u00b5s per loop\nsage: timeit(\"copy(MM.identity_matrix())\")\n625 loops, best of 3: 29.9 \u00b5s per loop\n\nsage: MM(0)\n[0 0 0]\n[0 0 0]\n[0 0 0]\n\nsage: MM(0)[1,2]=3 \n\n# this behavior is the same before and after patches were applied\n# is this right? isnt MM(0) mutable and should be = 3 at row/col=[1,2]? \nsage: MM(0)\n[0 0 0]\n[0 0 0]\n[0 0 0]\n\nsage: MM.zero_matrix()[1,2]=3\n---------------------------------------------------------------------------\nValueError                                Traceback (most recent call last)\n/mnt/usb1/scratch/rossk/sage-4.3.3.alpha1-sage.math.washington.edu-x86_64-Linux/<ipython console> in <module>()\n/mnt/usb1/scratch/rossk/sage-4.3.3.alpha1-sage.math.washington.edu-x86_64-Linux/local/lib/python2.6/site-packages/sage/matrix/matrix0.so in sage.matrix.matrix0.Matrix.__setitem__ (sage/matrix/matrix0.c:5496)()\n/mnt/usb1/scratch/rossk/sage-4.3.3.alpha1-sage.math.washington.edu-x86_64-Linux/local/lib/python2.6/site-packages/sage/matrix/matrix0.so in sage.matrix.matrix0.Matrix.check_mutability (sage/matrix/matrix0.c:3686)()\nValueError: matrix is immutable; please change a copy instead (i.e., use copy(M) to change a copy of M).\n\n# a copy is mutable\nsage: a=copy(MM.zero_matrix())\nsage: a[1,2]=3\nsage: a\n[0 0 0]\n[0 0 3]\n[0 0 0]\n\n# here, alias_zero is pointing to same object hence it is also immutable and correctly crashes also\nsage: alias_zero = MM.zero_matrix()\nsage: alias_zero[1,2]=3\n---------------------------------------------------------------------------\nValueError                                Traceback (most recent call last)\n\n/mnt/usb1/scratch/rossk/sage-4.3.3.alpha1-sage.math.washington.edu-x86_64-Linux/<ipython console> in <module>()\n/mnt/usb1/scratch/rossk/sage-4.3.3.alpha1-sage.math.washington.edu-x86_64-Linux/local/lib/python2.6/site-packages/sage/matrix/matrix0.so in sage.matrix.matrix0.Matrix.__setitem__ (sage/matrix/matrix0.c:5496)()\n/mnt/usb1/scratch/rossk/sage-4.3.3.alpha1-sage.math.washington.edu-x86_64-Linux/local/lib/python2.6/site-packages/sage/matrix/matrix0.so in sage.matrix.matrix0.Matrix.check_mutability (sage/matrix/matrix0.c:3686)()\nValueError: matrix is immutable; please change a copy instead (i.e., use copy(M) to change a copy of M).\n\n```\n",
    "created_at": "2010-02-20T14:18:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8276",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8276#issuecomment-73159",
    "user": "https://trac.sagemath.org/admin/accounts/users/rossk"
}
```

Applied the following patches (in the order below).


trac_8276-MatrixSpace_one-fh.patch


trac_8276-fix_sagelib-fh.patch


trac_8276-fix_zero_matrix_creation-fh.patch


trac_8294-matrix_2x2_copy_mutability_fix-fh.patch


*Almost* everything seems straightforward and correct but... Seems that MM(0) which has a "mutable == True" property/value should be updatable but the example "MM(0)[1,2] = 3" doesnt update MM(0) (see example below) Is that right?



```
# prepatch responses
sage: sage: MM = MatrixSpace(ZZ, 3,3)
sage: sage: MM(0).is_mutable()
True
sage: sage: MM.zero_matrix().is_mutable()
True
sage: sage: MM(1).is_mutable()
True
sage: sage: MM.identity_matrix().is_mutable()
True
sage: sage: timeit("MM(0)")
625 loops, best of 3: 51.1 µs per loop
sage: sage: timeit("copy(MM.zero_matrix())")
625 loops, best of 3: 19.3 µs per loop
sage: sage: timeit("MM(1)")
625 loops, best of 3: 65 µs per loop
sage: sage: timeit("copy(MM.identity_matrix())")
625 loops, best of 3: 60.7 µs per loop

# postpatch responses
sage: MM = MatrixSpace(ZZ, 3,3)
sage: MM(0).is_mutable()
True
sage: MM.zero_matrix().is_mutable()
False
sage: MM(1).is_mutable()
True
sage: MM.identity_matrix().is_mutable()
False
sage: timeit("MM(0)")
625 loops, best of 3: 35.9 µs per loop
sage: timeit("copy(MM.zero_matrix())")
625 loops, best of 3: 29.3 µs per loop
sage: timeit("MM(1)")
625 loops, best of 3: 46.1 µs per loop
sage: timeit("copy(MM.identity_matrix())")
625 loops, best of 3: 29.9 µs per loop

sage: MM(0)
[0 0 0]
[0 0 0]
[0 0 0]

sage: MM(0)[1,2]=3 

# this behavior is the same before and after patches were applied
# is this right? isnt MM(0) mutable and should be = 3 at row/col=[1,2]? 
sage: MM(0)
[0 0 0]
[0 0 0]
[0 0 0]

sage: MM.zero_matrix()[1,2]=3
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
/mnt/usb1/scratch/rossk/sage-4.3.3.alpha1-sage.math.washington.edu-x86_64-Linux/<ipython console> in <module>()
/mnt/usb1/scratch/rossk/sage-4.3.3.alpha1-sage.math.washington.edu-x86_64-Linux/local/lib/python2.6/site-packages/sage/matrix/matrix0.so in sage.matrix.matrix0.Matrix.__setitem__ (sage/matrix/matrix0.c:5496)()
/mnt/usb1/scratch/rossk/sage-4.3.3.alpha1-sage.math.washington.edu-x86_64-Linux/local/lib/python2.6/site-packages/sage/matrix/matrix0.so in sage.matrix.matrix0.Matrix.check_mutability (sage/matrix/matrix0.c:3686)()
ValueError: matrix is immutable; please change a copy instead (i.e., use copy(M) to change a copy of M).

# a copy is mutable
sage: a=copy(MM.zero_matrix())
sage: a[1,2]=3
sage: a
[0 0 0]
[0 0 3]
[0 0 0]

# here, alias_zero is pointing to same object hence it is also immutable and correctly crashes also
sage: alias_zero = MM.zero_matrix()
sage: alias_zero[1,2]=3
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)

/mnt/usb1/scratch/rossk/sage-4.3.3.alpha1-sage.math.washington.edu-x86_64-Linux/<ipython console> in <module>()
/mnt/usb1/scratch/rossk/sage-4.3.3.alpha1-sage.math.washington.edu-x86_64-Linux/local/lib/python2.6/site-packages/sage/matrix/matrix0.so in sage.matrix.matrix0.Matrix.__setitem__ (sage/matrix/matrix0.c:5496)()
/mnt/usb1/scratch/rossk/sage-4.3.3.alpha1-sage.math.washington.edu-x86_64-Linux/local/lib/python2.6/site-packages/sage/matrix/matrix0.so in sage.matrix.matrix0.Matrix.check_mutability (sage/matrix/matrix0.c:3686)()
ValueError: matrix is immutable; please change a copy instead (i.e., use copy(M) to change a copy of M).

```




---

archive/issue_comments_073160.json:
```json
{
    "body": "Just saw the \"updated patch\" reference. Will include replace old patch with new tomorrow and re-test",
    "created_at": "2010-02-20T14:21:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8276",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8276#issuecomment-73160",
    "user": "https://trac.sagemath.org/admin/accounts/users/rossk"
}
```

Just saw the "updated patch" reference. Will include replace old patch with new tomorrow and re-test



---

archive/issue_comments_073161.json:
```json
{
    "body": "Replying to [comment:12 rossk]:\n> *Almost* everything seems straightforward and correct but... \n\nSure ! What wasn't straightforward was to correctly find all the places which needed to be patched and to distinguish them from those who doesn't.\n\nNote that the speed regression when calling `copy(MM.zero_matrix())` is due to a missing optimization in cached_method which should be added soon.\n\n> Seems that MM(0) which has a \"mutable == True\" property/value should be updatable but the example \"MM(0)[1,2] = 3\" doesnt update MM(0) (see example below) Is that right?\n\n\n```\n> sage: MM(0)\n> [0 0 0]\n> [0 0 0]\n> [0 0 0]\n> \n> sage: MM(0)[1,2]=3 \n> \n> # this behavior is the same before and after patches were applied\n> # is this right? isnt MM(0) mutable and should be = 3 at row/col=[1,2]? \n> sage: MM(0)\n> [0 0 0]\n> [0 0 0]\n> [0 0 0]\n```\n\nThis is perfectly normal. `MM(0)` does not design a particular matrix object. It construct a brand new matrix. So that \n\n```\nsage: MM(0)[1,2]=3\n```\n \nConstruct a matrix, modify it and forget about the result so that the next call to\n`MM(0)` gives you a brand new zero matrix. To achieve what you want you should write\n\n```\nsage: MM = MatrixSpace(ZZ, 3,3)\nsage: mat = MM(0); mat[1,2]=3\nsage: mat\n[0 0 0]\n[0 0 3]\n[0 0 0]\n```\n\n\nFlorent",
    "created_at": "2010-02-20T14:51:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8276",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8276#issuecomment-73161",
    "user": "https://github.com/hivert"
}
```

Replying to [comment:12 rossk]:
> *Almost* everything seems straightforward and correct but... 

Sure ! What wasn't straightforward was to correctly find all the places which needed to be patched and to distinguish them from those who doesn't.

Note that the speed regression when calling `copy(MM.zero_matrix())` is due to a missing optimization in cached_method which should be added soon.

> Seems that MM(0) which has a "mutable == True" property/value should be updatable but the example "MM(0)[1,2] = 3" doesnt update MM(0) (see example below) Is that right?


```
> sage: MM(0)
> [0 0 0]
> [0 0 0]
> [0 0 0]
> 
> sage: MM(0)[1,2]=3 
> 
> # this behavior is the same before and after patches were applied
> # is this right? isnt MM(0) mutable and should be = 3 at row/col=[1,2]? 
> sage: MM(0)
> [0 0 0]
> [0 0 0]
> [0 0 0]
```

This is perfectly normal. `MM(0)` does not design a particular matrix object. It construct a brand new matrix. So that 

```
sage: MM(0)[1,2]=3
```
 
Construct a matrix, modify it and forget about the result so that the next call to
`MM(0)` gives you a brand new zero matrix. To achieve what you want you should write

```
sage: MM = MatrixSpace(ZZ, 3,3)
sage: mat = MM(0); mat[1,2]=3
sage: mat
[0 0 0]
[0 0 3]
[0 0 0]
```


Florent



---

archive/issue_comments_073162.json:
```json
{
    "body": "Attachment [trac-8276-MatrixSpace_one-review.patch](tarball://root/attachments/some-uuid/ticket8276/trac-8276-MatrixSpace_one-review.patch) by mraum created at 2010-02-20 15:21:30\n\nFirst reviewed patch",
    "created_at": "2010-02-20T15:21:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8276",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8276#issuecomment-73162",
    "user": "https://trac.sagemath.org/admin/accounts/users/mraum"
}
```

Attachment [trac-8276-MatrixSpace_one-review.patch](tarball://root/attachments/some-uuid/ticket8276/trac-8276-MatrixSpace_one-review.patch) by mraum created at 2010-02-20 15:21:30

First reviewed patch



---

archive/issue_comments_073163.json:
```json
{
    "body": "Attachment [trac-8276-fix_sagelib-review.patch](tarball://root/attachments/some-uuid/ticket8276/trac-8276-fix_sagelib-review.patch) by mraum created at 2010-02-20 15:21:50\n\nSeconded reviewed patch.",
    "created_at": "2010-02-20T15:21:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8276",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8276#issuecomment-73163",
    "user": "https://trac.sagemath.org/admin/accounts/users/mraum"
}
```

Attachment [trac-8276-fix_sagelib-review.patch](tarball://root/attachments/some-uuid/ticket8276/trac-8276-fix_sagelib-review.patch) by mraum created at 2010-02-20 15:21:50

Seconded reviewed patch.



---

archive/issue_comments_073164.json:
```json
{
    "body": "Used the new patches (as well as trac_8294-matrix_2x2_copy_mutability_fix-fh.patch). All were applied and compiled with no errors.\n\n```\nThe following tests failed:\n\tsage -t  devel/sage/sage/groups/abelian_gps/dual_abelian_group_element.py # Segfault\n\tsage -t  devel/sage/sage/matrix/matrix_integer_2x2.pyx # 1 doctests failed\n\tsage -t  devel/sage/doc/fr/tutorial/programming.rst # Segfault\n```\n\nRe-tested each and got the following for the first 2 (but the 3rd one passed).\n\n```\nA mysterious error (perhaps a memory error?) occurred, which may have crashed doctest.\n```\n\nI get this \"mysterious error\" a number of times and have seen many tickets mention it. Can anyone give any advice about it? Given its not always reproduceable, should it block a positive review if the tickets functionality proves good?",
    "created_at": "2010-02-21T00:20:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8276",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8276#issuecomment-73164",
    "user": "https://trac.sagemath.org/admin/accounts/users/rossk"
}
```

Used the new patches (as well as trac_8294-matrix_2x2_copy_mutability_fix-fh.patch). All were applied and compiled with no errors.

```
The following tests failed:
	sage -t  devel/sage/sage/groups/abelian_gps/dual_abelian_group_element.py # Segfault
	sage -t  devel/sage/sage/matrix/matrix_integer_2x2.pyx # 1 doctests failed
	sage -t  devel/sage/doc/fr/tutorial/programming.rst # Segfault
```

Re-tested each and got the following for the first 2 (but the 3rd one passed).

```
A mysterious error (perhaps a memory error?) occurred, which may have crashed doctest.
```

I get this "mysterious error" a number of times and have seen many tickets mention it. Can anyone give any advice about it? Given its not always reproduceable, should it block a positive review if the tickets functionality proves good?



---

archive/issue_comments_073165.json:
```json
{
    "body": "I just have have a query now that Im looking at the ticket that someone may care to answer.\nI appreciate there may be implementation issues that differentiate the different constructs i.e.  M().zero() vs M(0) etc. But from a language point of view (i.e. not considering constructions vs coercions), why are the different matrices below treated differently i.e. why arent they all immutable)? Im just thinking that, for example, M().zero() and M().zero_matrix() and M(0) etc each return a zero matrix that cant be changed (either theres an error if its immutable or the assignment is ignored). So shouldnt they all be immutable? And why is there a variation in the mutability between the zero and identity matrices. (Apologies if there's something obvious I missed)\n\n\n```\nsage: MM(0).is_mutable()\nTrue\nsage: MM.zero_matrix().is_mutable()\nFalse\nsage: MM.zero().is_mutable()\nTrue\n\nsage: MM(1).is_mutable()\nTrue\nsage: MM.identity_matrix().is_mutable()\nFalse\nsage: MM.one().is_mutable()\nFalse\n```\n",
    "created_at": "2010-02-21T02:46:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8276",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8276#issuecomment-73165",
    "user": "https://trac.sagemath.org/admin/accounts/users/rossk"
}
```

I just have have a query now that Im looking at the ticket that someone may care to answer.
I appreciate there may be implementation issues that differentiate the different constructs i.e.  M().zero() vs M(0) etc. But from a language point of view (i.e. not considering constructions vs coercions), why are the different matrices below treated differently i.e. why arent they all immutable)? Im just thinking that, for example, M().zero() and M().zero_matrix() and M(0) etc each return a zero matrix that cant be changed (either theres an error if its immutable or the assignment is ignored). So shouldnt they all be immutable? And why is there a variation in the mutability between the zero and identity matrices. (Apologies if there's something obvious I missed)


```
sage: MM(0).is_mutable()
True
sage: MM.zero_matrix().is_mutable()
False
sage: MM.zero().is_mutable()
True

sage: MM(1).is_mutable()
True
sage: MM.identity_matrix().is_mutable()
False
sage: MM.one().is_mutable()
False
```




---

archive/issue_comments_073166.json:
```json
{
    "body": "Changing keywords from \"One mutable.\" to \"One Zero mutable.\".",
    "created_at": "2010-02-21T02:46:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8276",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8276#issuecomment-73166",
    "user": "https://trac.sagemath.org/admin/accounts/users/rossk"
}
```

Changing keywords from "One mutable." to "One Zero mutable.".



---

archive/issue_comments_073167.json:
```json
{
    "body": "The reason is the categorie framework. MatrixSpaces are vector spaces, so they implement zero(). In my oppinion this should absolutely coinside with MM(0) since everybody will expect it so do so. Hence, it should be mutable.\none() is implemented seperatedly and is just one = identity_matrix. In my oppinion this is a defect, since according to the framework is normally coincides with MM(1). If MatrixSpaces was a ring it would be exactly this.\n\nCould I hear your oppinion? If nobody is opposed I will set this to positive review tomorrow evening and I will open a follow up which sets one = lambda self : self(1) .",
    "created_at": "2010-02-21T14:26:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8276",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8276#issuecomment-73167",
    "user": "https://trac.sagemath.org/admin/accounts/users/mraum"
}
```

The reason is the categorie framework. MatrixSpaces are vector spaces, so they implement zero(). In my oppinion this should absolutely coinside with MM(0) since everybody will expect it so do so. Hence, it should be mutable.
one() is implemented seperatedly and is just one = identity_matrix. In my oppinion this is a defect, since according to the framework is normally coincides with MM(1). If MatrixSpaces was a ring it would be exactly this.

Could I hear your oppinion? If nobody is opposed I will set this to positive review tomorrow evening and I will open a follow up which sets one = lambda self : self(1) .



---

archive/issue_comments_073168.json:
```json
{
    "body": "\n```\nsage: MM.zero().is_mutable()\nTrue\n```\n\nIs corrected by my last patch. It should be False\n\nReplying to [comment:17 mraum]:\n> The reason is the categorie framework. MatrixSpaces are vector spaces, so they implement zero(). In my oppinion this should absolutely coinside with MM(0) since everybody will expect it so do so. Hence, it should be mutable.\n\nNo it isn't. See the comment in the doc of `zero` and `one` in their respective category. It has been discussed on sage-devel that `.zero()` and `.one()` should return an *immutable* matrix. The argument of the category framework applies identically to `zero` (vector space) and one (algebra which come actually from monoid).  \n\n> one() is implemented seperatedly and is just one = identity_matrix. In my oppinion this is a defect, since according to the framework is normally coincides with MM(1). If MatrixSpaces was a ring it would be exactly this.\n\nNote that my last version of the patch also implement \n\n```\nzero = zero_matrix\n```\n\n\n> Could I hear your oppinion? If nobody is opposed I will set this to positive review tomorrow evening and I will open a follow up which sets one = lambda self : self(1) .\n\nMy opinion which coincide with William's and Robert Bradshaw is that one and zero should be immutable. It was not discussed whether `MM(0)` and `MM(1)` should returns something coherent. \nplease see http://groups.google.com/group/sage-devel/browse_frm/thread/1042edd11b3854b2",
    "created_at": "2010-02-21T21:08:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8276",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8276#issuecomment-73168",
    "user": "https://github.com/hivert"
}
```


```
sage: MM.zero().is_mutable()
True
```

Is corrected by my last patch. It should be False

Replying to [comment:17 mraum]:
> The reason is the categorie framework. MatrixSpaces are vector spaces, so they implement zero(). In my oppinion this should absolutely coinside with MM(0) since everybody will expect it so do so. Hence, it should be mutable.

No it isn't. See the comment in the doc of `zero` and `one` in their respective category. It has been discussed on sage-devel that `.zero()` and `.one()` should return an *immutable* matrix. The argument of the category framework applies identically to `zero` (vector space) and one (algebra which come actually from monoid).  

> one() is implemented seperatedly and is just one = identity_matrix. In my oppinion this is a defect, since according to the framework is normally coincides with MM(1). If MatrixSpaces was a ring it would be exactly this.

Note that my last version of the patch also implement 

```
zero = zero_matrix
```


> Could I hear your oppinion? If nobody is opposed I will set this to positive review tomorrow evening and I will open a follow up which sets one = lambda self : self(1) .

My opinion which coincide with William's and Robert Bradshaw is that one and zero should be immutable. It was not discussed whether `MM(0)` and `MM(1)` should returns something coherent. 
please see http://groups.google.com/group/sage-devel/browse_frm/thread/1042edd11b3854b2



---

archive/issue_comments_073169.json:
```json
{
    "body": "Attachment [trac-8276-fix_zero_matrix_creation-review.patch](tarball://root/attachments/some-uuid/ticket8276/trac-8276-fix_zero_matrix_creation-review.patch) by mraum created at 2010-02-22 11:16:54\n\nReplacing old review; now with zero=zero_matrix",
    "created_at": "2010-02-22T11:16:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8276",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8276#issuecomment-73169",
    "user": "https://trac.sagemath.org/admin/accounts/users/mraum"
}
```

Attachment [trac-8276-fix_zero_matrix_creation-review.patch](tarball://root/attachments/some-uuid/ticket8276/trac-8276-fix_zero_matrix_creation-review.patch) by mraum created at 2010-02-22 11:16:54

Replacing old review; now with zero=zero_matrix



---

archive/issue_comments_073170.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-02-22T11:22:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8276",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8276#issuecomment-73170",
    "user": "https://trac.sagemath.org/admin/accounts/users/mraum"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_073171.json:
```json
{
    "body": "Ok, I didn't read this thread this way, but yes, you're right, a majority seems to want exactly this behaviour.\nThe review patches now include also your last change.\n\nI'm personally strongly opposed to this, so I am going to open a brief discussion on sage-devel, just to make sure that this is a general policy towards the categories framework. I hope to read your opinion there, too.\n\nrossk: I guess it's fair to say, that you also contributed to this review, so please expand your name in the review field.",
    "created_at": "2010-02-22T11:22:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8276",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8276#issuecomment-73171",
    "user": "https://trac.sagemath.org/admin/accounts/users/mraum"
}
```

Ok, I didn't read this thread this way, but yes, you're right, a majority seems to want exactly this behaviour.
The review patches now include also your last change.

I'm personally strongly opposed to this, so I am going to open a brief discussion on sage-devel, just to make sure that this is a general policy towards the categories framework. I hope to read your opinion there, too.

rossk: I guess it's fair to say, that you also contributed to this review, so please expand your name in the review field.



---

archive/issue_events_008475.json:
```json
{
    "actor": "mvngu",
    "created_at": "2010-03-03T14:30:36Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8276",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8276#event-8475"
}
```



---

archive/issue_comments_073172.json:
```json
{
    "body": "Merged in this order:\n\n1. [trac-8276-MatrixSpace_one-review.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8276/trac-8276-MatrixSpace_one-review.patch)\n2. [trac-8276-fix_sagelib-review.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8276/trac-8276-fix_sagelib-review.patch)\n3. [trac-8276-fix_zero_matrix_creation-review.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8276/trac-8276-fix_zero_matrix_creation-review.patch)",
    "created_at": "2010-03-03T14:30:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8276",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8276#issuecomment-73172",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Merged in this order:

1. [trac-8276-MatrixSpace_one-review.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8276/trac-8276-MatrixSpace_one-review.patch)
2. [trac-8276-fix_sagelib-review.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8276/trac-8276-fix_sagelib-review.patch)
3. [trac-8276-fix_zero_matrix_creation-review.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8276/trac-8276-fix_zero_matrix_creation-review.patch)



---

archive/issue_comments_073173.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-03-03T14:30:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8276",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8276#issuecomment-73173",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed
