# Issue 6904: change ring broken over QQ and GF(2)

archive/issues_006904.json:
```json
{
    "body": "Assignee: @williamstein\n\n\n```\nsage: matrix(QQ,2,[1,0,0,1]).change_ring(GF(2)) - 1\nTraceback (most recent call last):\n...\nRuntimeError\n}}\n\nIssue created by migration from https://trac.sagemath.org/ticket/6904\n\n",
    "created_at": "2009-09-08T20:13:34Z",
    "labels": [
        "linear algebra",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5.2",
    "title": "change ring broken over QQ and GF(2)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6904",
    "user": "@williamstein"
}
```
Assignee: @williamstein


```
sage: matrix(QQ,2,[1,0,0,1]).change_ring(GF(2)) - 1
Traceback (most recent call last):
...
RuntimeError
}}

Issue created by migration from https://trac.sagemath.org/ticket/6904





---

archive/issue_comments_057035.json:
```json
{
    "body": "Here's another bug that bit me while doing research today and might be caused by the same problem:\n\n```\nsage: a = matrix(QQ,22,[0, 0, 0, -1, 1, -1, -1, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0,\n0, 1, 0, 1, 0, 0, 0, -1, 1, 0, -1, 0, 1, 0, 0, -1, 0, -2, 1, -1, -1, 1,\n0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0,\n0, 1, -1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, -1, 0,\n0, -1, 1, 0, 0, -1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, -1, 0, -1, 0, 0,\n-1, 1, 0, 1, -1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, -1, 0, 0, 0, -1, 0,\n0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, -1, 0, -1, 0, 0,\n0, 1, -1, 0, 1, 0, -1, 0, 1, 1, 0, 2, 0, 0, 1, -1, 1, 0, 0, 0, 0, 0, 0,\n1, 0, 0, 0, 0, 0, 0, 0, 1, -1, 1, 0, 0, 1, 0, 0, 0, 0, 1, -2, 1, 1, 0,\n0, 0, 0, 0, 1, -1, -1, 0, -1, 0, -1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1,\n0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, -1, 1, 0, 0, 0, 0,\n0, 0, 1, -1, -1, 0, 0, -1, -1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, -1, 1, 0,\n-1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, -1, 0, 0, 0, 0, 0, 1, -1, 0, 0,\n0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, -1, 1, 0, 0, 1, 0, 0,\n0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, -1, 0, 0, 0, 0, 0, 0, 0,\n0, 0, -1, 0, 0, 0, 0, 0, 1, 0, 0, 1, -1, 0, -1, 1, 0, -1, 0, 0, 0, 0, 0,\n0, -2, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, -1, 1, 0, -1, -1, 1, 0, 0, 0, 0,\n-2, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, -1, 0, 1, 0, -1, 0, 0, 0, 0, 0, -1,\n0, 0, 0, 0, 0, -1, 0, 0, 0, 0, -1, 0, -1, 1, 1, -1, 0, 0, 0, 0, 0, 0, 0,\n0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, -1, 0, 0, 0, 0, 0, 0, -1, 0, 0,\n0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, -1, 0, 0, 0, 0, 0, 1, -1, 0, 0, 0,\n1]).change_ring(GF(2))\n\nsage: a^21\nTraceback (click to the left of this block for traceback)\n...\nTypeError: Cannot convert\nsage.matrix.matrix_modn_dense.Matrix_modn_dense to\nsage.matrix.matrix_mod2_dense.Matrix_mod2_dense\n\nTraceback (most recent call last):\n  File \"<stdin>\", line 1, in <module>\n  File \"_sage_input_79.py\", line 9, in <module>\n    open(\"___code___.py\",\"w\").write(\"# -*- coding: utf-8 -*-\\n\" + _support_.preparse_worksheet_cell(base64.b64decode(\"diA9IFsoYV5pKS5saXN0KCkgZm9yIGkgaW4gWzEuLjIxXV0=\"),globals())+\"\\n\"); execfile(os.path.abspath(\"___code___.py\"))\n  File \"\", line 1, in <module>\n    \n  File \"/tmp/tmpVclvdc/___code___.py\", line 3, in <module>\n    v = [(a**i).list() for i in (ellipsis_range(_sage_const_1 ,Ellipsis,_sage_const_21 ))]\n  File \"\", line 1, in <module>\n    \n  File \"matrix0.pyx\", line 3893, in sage.matrix.matrix0.Matrix.__pow__ (sage/matrix/matrix0.c:21527)\n  File \"element.pyx\", line 1409, in sage.structure.element.RingElement.__pow__ (sage/structure/element.c:11201)\n  File \"element.pyx\", line 3264, in sage.structure.element.generic_power_c (sage/structure/element.c:23714)\n  File \"element.pyx\", line 2134, in sage.structure.element.Matrix.__mul__ (sage/structure/element.c:14292)\n  File \"matrix_mod2_dense.pyx\", line 645, in sage.matrix.matrix_mod2_dense.Matrix_mod2_dense._matrix_times_matrix_ (sage/matrix/matrix_mod2_dense.c:5144)\nTypeError: Cannot convert sage.matrix.matrix_modn_dense.Matrix_modn_dense to sage.matrix.matrix_mod2_dense.Matrix_mod2_dense\n\n```\n",
    "created_at": "2010-02-18T23:45:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6904",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6904#issuecomment-57035",
    "user": "@williamstein"
}
```

Here's another bug that bit me while doing research today and might be caused by the same problem:

```
sage: a = matrix(QQ,22,[0, 0, 0, -1, 1, -1, -1, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0,
0, 1, 0, 1, 0, 0, 0, -1, 1, 0, -1, 0, 1, 0, 0, -1, 0, -2, 1, -1, -1, 1,
0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0,
0, 1, -1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, -1, 0,
0, -1, 1, 0, 0, -1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, -1, 0, -1, 0, 0,
-1, 1, 0, 1, -1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, -1, 0, 0, 0, -1, 0,
0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, -1, 0, -1, 0, 0,
0, 1, -1, 0, 1, 0, -1, 0, 1, 1, 0, 2, 0, 0, 1, -1, 1, 0, 0, 0, 0, 0, 0,
1, 0, 0, 0, 0, 0, 0, 0, 1, -1, 1, 0, 0, 1, 0, 0, 0, 0, 1, -2, 1, 1, 0,
0, 0, 0, 0, 1, -1, -1, 0, -1, 0, -1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1,
0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, -1, 1, 0, 0, 0, 0,
0, 0, 1, -1, -1, 0, 0, -1, -1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, -1, 1, 0,
-1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, -1, 0, 0, 0, 0, 0, 1, -1, 0, 0,
0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, -1, 1, 0, 0, 1, 0, 0,
0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, -1, 0, 0, 0, 0, 0, 0, 0,
0, 0, -1, 0, 0, 0, 0, 0, 1, 0, 0, 1, -1, 0, -1, 1, 0, -1, 0, 0, 0, 0, 0,
0, -2, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, -1, 1, 0, -1, -1, 1, 0, 0, 0, 0,
-2, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, -1, 0, 1, 0, -1, 0, 0, 0, 0, 0, -1,
0, 0, 0, 0, 0, -1, 0, 0, 0, 0, -1, 0, -1, 1, 1, -1, 0, 0, 0, 0, 0, 0, 0,
0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, -1, 0, 0, 0, 0, 0, 0, -1, 0, 0,
0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, -1, 0, 0, 0, 0, 0, 1, -1, 0, 0, 0,
1]).change_ring(GF(2))

sage: a^21
Traceback (click to the left of this block for traceback)
...
TypeError: Cannot convert
sage.matrix.matrix_modn_dense.Matrix_modn_dense to
sage.matrix.matrix_mod2_dense.Matrix_mod2_dense

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "_sage_input_79.py", line 9, in <module>
    open("___code___.py","w").write("# -*- coding: utf-8 -*-\n" + _support_.preparse_worksheet_cell(base64.b64decode("diA9IFsoYV5pKS5saXN0KCkgZm9yIGkgaW4gWzEuLjIxXV0="),globals())+"\n"); execfile(os.path.abspath("___code___.py"))
  File "", line 1, in <module>
    
  File "/tmp/tmpVclvdc/___code___.py", line 3, in <module>
    v = [(a**i).list() for i in (ellipsis_range(_sage_const_1 ,Ellipsis,_sage_const_21 ))]
  File "", line 1, in <module>
    
  File "matrix0.pyx", line 3893, in sage.matrix.matrix0.Matrix.__pow__ (sage/matrix/matrix0.c:21527)
  File "element.pyx", line 1409, in sage.structure.element.RingElement.__pow__ (sage/structure/element.c:11201)
  File "element.pyx", line 3264, in sage.structure.element.generic_power_c (sage/structure/element.c:23714)
  File "element.pyx", line 2134, in sage.structure.element.Matrix.__mul__ (sage/structure/element.c:14292)
  File "matrix_mod2_dense.pyx", line 645, in sage.matrix.matrix_mod2_dense.Matrix_mod2_dense._matrix_times_matrix_ (sage/matrix/matrix_mod2_dense.c:5144)
TypeError: Cannot convert sage.matrix.matrix_modn_dense.Matrix_modn_dense to sage.matrix.matrix_mod2_dense.Matrix_mod2_dense

```




---

archive/issue_comments_057036.json:
```json
{
    "body": "Amazingly, this is still broken in Sage-4.5.alpha4!\n\n```\n\nwstein@sage:~/build/sage-4.5.alpha4$ ./sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n**********************************************************************\n*                                                                    *\n* Warning: this is a prerelease version, and it may be unstable.     *\n*                                                                    *\n**********************************************************************\nsage: matrix(QQ,2,[1,0,0,1]).change_ring(GF(2)) - 1\n---------------------------------------------------------------------------\nRuntimeError                              Traceback (most recent call last)\n| Sage Version 4.5.alpha4, Release Date: 2010-07-06                  |\n| Type notebook() for the GUI, and license() for information.        |\n/mnt/usb1/scratch/wstein/build/sage-4.5.alpha4/<ipython console> in <module>()\n\n/mnt/usb1/scratch/wstein/build/sage-4.5.alpha4/local/lib/python2.6/site-packages/sage/structure/element.so in sage.structure.element.RingElement.__sub__ (sage/structure/element.c:11073)()\n\n/mnt/usb1/scratch/wstein/build/sage-4.5.alpha4/local/lib/python2.6/site-packages/sage/structure/coerce.so in sage.structure.coerce.CoercionModel_cache_maps.bin_op (sage/structure/coerce.c:6123)()\n\n/mnt/usb1/scratch/wstein/build/sage-4.5.alpha4/local/lib/python2.6/site-packages/sage/structure/element.so in sage.structure.element.RingElement.__sub__ (sage/structure/element.c:11005)()\n\nRuntimeError: \nsage: \n```\n",
    "created_at": "2010-07-07T06:26:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6904",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6904#issuecomment-57036",
    "user": "@williamstein"
}
```

Amazingly, this is still broken in Sage-4.5.alpha4!

```

wstein@sage:~/build/sage-4.5.alpha4$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
**********************************************************************
*                                                                    *
* Warning: this is a prerelease version, and it may be unstable.     *
*                                                                    *
**********************************************************************
sage: matrix(QQ,2,[1,0,0,1]).change_ring(GF(2)) - 1
---------------------------------------------------------------------------
RuntimeError                              Traceback (most recent call last)
| Sage Version 4.5.alpha4, Release Date: 2010-07-06                  |
| Type notebook() for the GUI, and license() for information.        |
/mnt/usb1/scratch/wstein/build/sage-4.5.alpha4/<ipython console> in <module>()

/mnt/usb1/scratch/wstein/build/sage-4.5.alpha4/local/lib/python2.6/site-packages/sage/structure/element.so in sage.structure.element.RingElement.__sub__ (sage/structure/element.c:11073)()

/mnt/usb1/scratch/wstein/build/sage-4.5.alpha4/local/lib/python2.6/site-packages/sage/structure/coerce.so in sage.structure.coerce.CoercionModel_cache_maps.bin_op (sage/structure/coerce.c:6123)()

/mnt/usb1/scratch/wstein/build/sage-4.5.alpha4/local/lib/python2.6/site-packages/sage/structure/element.so in sage.structure.element.RingElement.__sub__ (sage/structure/element.c:11005)()

RuntimeError: 
sage: 
```




---

archive/issue_comments_057037.json:
```json
{
    "body": "This is occurring in `Matrix_modn_dense._sub_()`. It gets called with 'right' of type Matrix_mod2_dense, but casts it to Matrix_modn_dense internally. (I haven't looked at all at why this is happening and if it should be happening.)",
    "created_at": "2010-07-07T09:01:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6904",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6904#issuecomment-57037",
    "user": "@wjp"
}
```

This is occurring in `Matrix_modn_dense._sub_()`. It gets called with 'right' of type Matrix_mod2_dense, but casts it to Matrix_modn_dense internally. (I haven't looked at all at why this is happening and if it should be happening.)



---

archive/issue_comments_057038.json:
```json
{
    "body": "Proposed fix for the bug #6904",
    "created_at": "2010-07-07T13:09:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6904",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6904#issuecomment-57038",
    "user": "@ClementPernet"
}
```

Proposed fix for the bug #6904



---

archive/issue_comments_057039.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-07-07T13:12:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6904",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6904#issuecomment-57039",
    "user": "@ClementPernet"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_057040.json:
```json
{
    "body": "Attachment [sage-6904.patch](tarball://root/attachments/some-uuid/ticket6904/sage-6904.patch) by @ClementPernet created at 2010-07-07 13:12:16\n\nThe problem is due to the fact that with p=2, the change_ring() method \u00a0should not create a matrix_modn_dense but a matrix_mod2_dense (wrapping m4ri).\n\nI added this special case.\n\nMeanwhile, it revealed a conflict in the declaration of ONE (in libs/pari/gens.pyx, and in m4ri). So I renammed the macros in pari/gens.*.",
    "created_at": "2010-07-07T13:12:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6904",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6904#issuecomment-57040",
    "user": "@ClementPernet"
}
```

Attachment [sage-6904.patch](tarball://root/attachments/some-uuid/ticket6904/sage-6904.patch) by @ClementPernet created at 2010-07-07 13:12:16

The problem is due to the fact that with p=2, the change_ring() method  should not create a matrix_modn_dense but a matrix_mod2_dense (wrapping m4ri).

I added this special case.

Meanwhile, it revealed a conflict in the declaration of ONE (in libs/pari/gens.pyx, and in m4ri). So I renammed the macros in pari/gens.*.



---

archive/issue_comments_057041.json:
```json
{
    "body": "Changing assignee from @williamstein to @ClementPernet.",
    "created_at": "2010-07-07T13:13:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6904",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6904#issuecomment-57041",
    "user": "@ClementPernet"
}
```

Changing assignee from @williamstein to @ClementPernet.



---

archive/issue_comments_057042.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-07-08T12:33:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6904",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6904#issuecomment-57042",
    "user": "@williamstein"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_057043.json:
```json
{
    "body": "Two changes needed:\n\n* Add the example as a doctest.\n\n* Change _mod_int_c(self, mod_int p) so it calls _mod_two if p=2.",
    "created_at": "2010-07-08T12:33:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6904",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6904#issuecomment-57043",
    "user": "@williamstein"
}
```

Two changes needed:

* Add the example as a doctest.

* Change _mod_int_c(self, mod_int p) so it calls _mod_two if p=2.



---

archive/issue_comments_057044.json:
```json
{
    "body": "Attachment [sage-6904-v2.patch](tarball://root/attachments/some-uuid/ticket6904/sage-6904-v2.patch) by @ClementPernet created at 2010-07-08 12:54:45\n\ncorrected version following the remarks by was",
    "created_at": "2010-07-08T12:54:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6904",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6904#issuecomment-57044",
    "user": "@ClementPernet"
}
```

Attachment [sage-6904-v2.patch](tarball://root/attachments/some-uuid/ticket6904/sage-6904-v2.patch) by @ClementPernet created at 2010-07-08 12:54:45

corrected version following the remarks by was



---

archive/issue_comments_057045.json:
```json
{
    "body": "fix a typo in the docstring",
    "created_at": "2010-07-08T13:02:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6904",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6904#issuecomment-57045",
    "user": "@ClementPernet"
}
```

fix a typo in the docstring



---

archive/issue_comments_057046.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2010-07-08T13:03:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6904",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6904#issuecomment-57046",
    "user": "@williamstein"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_057047.json:
```json
{
    "body": "Attachment [sage-6904-v3.patch](tarball://root/attachments/some-uuid/ticket6904/sage-6904-v3.patch) by @williamstein created at 2010-07-08 13:03:45",
    "created_at": "2010-07-08T13:03:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6904",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6904#issuecomment-57047",
    "user": "@williamstein"
}
```

Attachment [sage-6904-v3.patch](tarball://root/attachments/some-uuid/ticket6904/sage-6904-v3.patch) by @williamstein created at 2010-07-08 13:03:45



---

archive/issue_comments_057048.json:
```json
{
    "body": "I've filled in the Author(s) and Reviewer(s) fields.  If I'm wrong, please correct them.",
    "created_at": "2010-07-20T08:19:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6904",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6904#issuecomment-57048",
    "user": "@qed777"
}
```

I've filled in the Author(s) and Reviewer(s) fields.  If I'm wrong, please correct them.



---

archive/issue_comments_057049.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-20T08:19:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6904",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6904#issuecomment-57049",
    "user": "@qed777"
}
```

Resolution: fixed
