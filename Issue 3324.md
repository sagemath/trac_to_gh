# Issue 3324: [with patch, needs review] Matrix_mod2_dense to/from PNG routines

archive/issues_003324.json:
```json
{
    "body": "Assignee: @williamstein\n\nKeywords: gd, linear algebra, gf(2)\n\n1-bit PNGs are a pretty sweet storage format for dense GF(2) matrices\n* they are intuitive (you can even look at them)\n* they are small (since the data is compressed for you)\n* other people wrote fast C libraries to deal with them.\n\nSo this patch adds `to_png` and `from_png` functions to  `sage.matrix.matrix_mod2_dense` and uses those to implement pickling/unpickling.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3324\n\n",
    "created_at": "2008-05-28T19:07:24Z",
    "labels": [
        "component: linear algebra"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.2",
    "title": "[with patch, needs review] Matrix_mod2_dense to/from PNG routines",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3324",
    "user": "https://github.com/malb"
}
```
Assignee: @williamstein

Keywords: gd, linear algebra, gf(2)

1-bit PNGs are a pretty sweet storage format for dense GF(2) matrices
* they are intuitive (you can even look at them)
* they are small (since the data is compressed for you)
* other people wrote fast C libraries to deal with them.

So this patch adds `to_png` and `from_png` functions to  `sage.matrix.matrix_mod2_dense` and uses those to implement pickling/unpickling.

Issue created by migration from https://trac.sagemath.org/ticket/3324





---

archive/issue_comments_022993.json:
```json
{
    "body": "REFEREE CHAT:\n\n```\n\n07:44 < wstein-3324> Does to_png *have* to use a disk file?  Could it do everything in memory?\n07:44 < malb> then it couldn't use GD\n07:44 < wstein-3324> I'm just a little worried, e.g., say one pickles up 100000 2x2 GF(2) matrices.\n07:44 < wstein-3324> OK, so GD is disk only?\n07:44 < malb> I think so\n07:45 < malb> at least the public API\n07:45 < malb> but I plan to add native 1-bit PNG support \n07:45 < malb> which would work in MEM\n07:45 < wstein-3324> OK.\n07:45 < malb> and is also useful for sparse matrices \n07:45 < wstein-3324> That's enough to satisfy me.\n07:45 < wstein-3324> Should your cdef extern from \"gd.h\":  stuff go in a file gd.pxi?\n07:46 < wstein-3324> Since it probably gets re-used a lot, or could be.\n07:46 < wstein-3324> Just curious.\n07:46 < wstein-3324> Or is it not systematic and only a tiny chunk of gd.h.\n07:46 < malb> boothby did some work in that area I believe\n07:46 < wstein-3324> Did you benchmark your new code against the old code?\n07:47 < malb> it is only a small chunk\n07:47 < wstein-3324> ok, then leave as is.\n07:47 < malb> re: benchmarking\n07:47 < malb> yes\n07:47 < malb> it was unfeasible vs. 5 seconds\n07:47 < wstein-3324> sweet.\n07:47 < wstein-3324> What did you develop on?  64-bit linux?\n07:48 < malb> I use that code on a daily basis since Michael provides test data for M4RI in 1-bit PNGs\n07:48 < malb> 64-bit linux\n07:48 < wstein-3324> ok, so I'll test on 32-bit os x powerpc, say.\n07:48 < malb> yep\n07:48 < malb> but I doubt endianess issues, since I use the gd library and the most naiv bit access code available \n              in M4RI\n07:49 < wstein-3324> famous last wods.\n07:49 < malb> :-)\n\n```\n\n\nThis fails to work on OS X PPC:\n\n```\n/Users/was/build/sage-3.0.3.alpha0/local/lib/python2.5/site-packages/sage/matrix/matrix_space.py in <module>()\n     36 import matrix_modn_sparse\n     37\n---> 38 import matrix_mod2_dense\n     39 #import matrix_mod2_sparse\n     40\n\nImportError: dlopen(/Users/was/build/sage-3.0.3.alpha0/local/lib/python2.5/site-packages/sage/matrix/matrix_mod2_dense.so, 2): Symbol not found: _png_check_sig\n  Referenced from: /Users/was/build/sage-3.0.3.alpha0/local/lib//libgd.2.dylib\n  Expected in: flat namespace\n\n```\n\n\nThis fails to work on 32-bit Linux against vanilla 3.0.2 and exactly the same\nproblem on minimal 64-bit debian:\n\n```\npatching file sage/matrix/matrix_mod2_dense.pyx\nHunk #1 succeeded at 893 with fuzz 1 (offset -310 lines).\nsage:\n\nsage -br\n\nBuilding sage/matrix/matrix_mod2_dense.c because it depends on sage/matrix/matrix_mod2_dense.pyx.\npython2.5 `which cython` --embed-positions --incref-local-binop -I/home/was/build/sage-3.0.2/devel/sage-main -o sage/matrix/matrix_mod2_dense.c sage/matrix/matrix_mod2_dense.pyx\n\nError converting Pyrex file to C:\n------------------------------------------------------------\n... \n\n    A = <Matrix_mod2_dense>Matrix(GF(2),r,c)\n\n    for i from 0 <= i < r:\n        for j from 0 <= j < c:\n            mzd_write_bit(A._entries, i, j, 1-gdImageGetPixel(im, j, i))\n                        ^\n------------------------------------------------------------\n\n/home/was/build/sage-3.0.2/devel/sage-main/sage/matrix/matrix_mod2_dense.pyx:989:25: undeclared name not builtin: mzd_write_bit\n\nError converting Pyrex file to C:\n------------------------------------------------------------\n... \n    cdef int black = gdImageColorAllocate(im, 0, 0, 0)\n    cdef int white = gdImageColorAllocate(im, 255, 255, 255)\n    gdImageFilledRectangle(im, 0, 0, c-1, r-1, white)\n    for i from 0 <= i < r:\n        for j from 0 <= j < c:\n            if mzd_read_bit(A._entries, i, j):\n                          ^\n------------------------------------------------------------\n\n/home/was/build/sage-3.0.2/devel/sage-main/sage/matrix/matrix_mod2_dense.pyx:1024:27: undeclared name not builtin: mzd_read_bit\nsage: Error running cython.\nsage: There was an error installing modified sage library code.\n\n\n```\n",
    "created_at": "2008-06-03T14:55:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3324",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3324#issuecomment-22993",
    "user": "https://github.com/williamstein"
}
```

REFEREE CHAT:

```

07:44 < wstein-3324> Does to_png *have* to use a disk file?  Could it do everything in memory?
07:44 < malb> then it couldn't use GD
07:44 < wstein-3324> I'm just a little worried, e.g., say one pickles up 100000 2x2 GF(2) matrices.
07:44 < wstein-3324> OK, so GD is disk only?
07:44 < malb> I think so
07:45 < malb> at least the public API
07:45 < malb> but I plan to add native 1-bit PNG support 
07:45 < malb> which would work in MEM
07:45 < wstein-3324> OK.
07:45 < malb> and is also useful for sparse matrices 
07:45 < wstein-3324> That's enough to satisfy me.
07:45 < wstein-3324> Should your cdef extern from "gd.h":  stuff go in a file gd.pxi?
07:46 < wstein-3324> Since it probably gets re-used a lot, or could be.
07:46 < wstein-3324> Just curious.
07:46 < wstein-3324> Or is it not systematic and only a tiny chunk of gd.h.
07:46 < malb> boothby did some work in that area I believe
07:46 < wstein-3324> Did you benchmark your new code against the old code?
07:47 < malb> it is only a small chunk
07:47 < wstein-3324> ok, then leave as is.
07:47 < malb> re: benchmarking
07:47 < malb> yes
07:47 < malb> it was unfeasible vs. 5 seconds
07:47 < wstein-3324> sweet.
07:47 < wstein-3324> What did you develop on?  64-bit linux?
07:48 < malb> I use that code on a daily basis since Michael provides test data for M4RI in 1-bit PNGs
07:48 < malb> 64-bit linux
07:48 < wstein-3324> ok, so I'll test on 32-bit os x powerpc, say.
07:48 < malb> yep
07:48 < malb> but I doubt endianess issues, since I use the gd library and the most naiv bit access code available 
              in M4RI
07:49 < wstein-3324> famous last wods.
07:49 < malb> :-)

```


This fails to work on OS X PPC:

```
/Users/was/build/sage-3.0.3.alpha0/local/lib/python2.5/site-packages/sage/matrix/matrix_space.py in <module>()
     36 import matrix_modn_sparse
     37
---> 38 import matrix_mod2_dense
     39 #import matrix_mod2_sparse
     40

ImportError: dlopen(/Users/was/build/sage-3.0.3.alpha0/local/lib/python2.5/site-packages/sage/matrix/matrix_mod2_dense.so, 2): Symbol not found: _png_check_sig
  Referenced from: /Users/was/build/sage-3.0.3.alpha0/local/lib//libgd.2.dylib
  Expected in: flat namespace

```


This fails to work on 32-bit Linux against vanilla 3.0.2 and exactly the same
problem on minimal 64-bit debian:

```
patching file sage/matrix/matrix_mod2_dense.pyx
Hunk #1 succeeded at 893 with fuzz 1 (offset -310 lines).
sage:

sage -br

Building sage/matrix/matrix_mod2_dense.c because it depends on sage/matrix/matrix_mod2_dense.pyx.
python2.5 `which cython` --embed-positions --incref-local-binop -I/home/was/build/sage-3.0.2/devel/sage-main -o sage/matrix/matrix_mod2_dense.c sage/matrix/matrix_mod2_dense.pyx

Error converting Pyrex file to C:
------------------------------------------------------------
... 

    A = <Matrix_mod2_dense>Matrix(GF(2),r,c)

    for i from 0 <= i < r:
        for j from 0 <= j < c:
            mzd_write_bit(A._entries, i, j, 1-gdImageGetPixel(im, j, i))
                        ^
------------------------------------------------------------

/home/was/build/sage-3.0.2/devel/sage-main/sage/matrix/matrix_mod2_dense.pyx:989:25: undeclared name not builtin: mzd_write_bit

Error converting Pyrex file to C:
------------------------------------------------------------
... 
    cdef int black = gdImageColorAllocate(im, 0, 0, 0)
    cdef int white = gdImageColorAllocate(im, 255, 255, 255)
    gdImageFilledRectangle(im, 0, 0, c-1, r-1, white)
    for i from 0 <= i < r:
        for j from 0 <= j < c:
            if mzd_read_bit(A._entries, i, j):
                          ^
------------------------------------------------------------

/home/was/build/sage-3.0.2/devel/sage-main/sage/matrix/matrix_mod2_dense.pyx:1024:27: undeclared name not builtin: mzd_read_bit
sage: Error running cython.
sage: There was an error installing modified sage library code.


```




---

archive/issue_comments_022994.json:
```json
{
    "body": "REFEREE REPORT:\n\nI read the code and it looks fine.  However it doesn't build/work on any of my test platforms, and that's not so good.",
    "created_at": "2008-06-03T14:55:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3324",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3324#issuecomment-22994",
    "user": "https://github.com/williamstein"
}
```

REFEREE REPORT:

I read the code and it looks fine.  However it doesn't build/work on any of my test platforms, and that's not so good.



---

archive/issue_comments_022995.json:
```json
{
    "body": "The code depends on: #3204 (which is in 3.0.3.alpha0) so it won't work against 3.0.2. Sorry for not pointing that out earlier. I don't know about the OSX failure though.",
    "created_at": "2008-06-03T15:02:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3324",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3324#issuecomment-22995",
    "user": "https://github.com/malb"
}
```

The code depends on: #3204 (which is in 3.0.3.alpha0) so it won't work against 3.0.2. Sorry for not pointing that out earlier. I don't know about the OSX failure though.



---

archive/issue_comments_022996.json:
```json
{
    "body": "I've updated the patch to avoid temporary files.",
    "created_at": "2008-06-12T22:30:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3324",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3324#issuecomment-22996",
    "user": "https://github.com/malb"
}
```

I've updated the patch to avoid temporary files.



---

archive/issue_comments_022997.json:
```json
{
    "body": "Changing keywords from \"gd, linear algebra, gf(2)\" to \"gd, linear algebra, gf(2), editor_malb\".",
    "created_at": "2008-06-15T21:49:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3324",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3324#issuecomment-22997",
    "user": "https://github.com/craigcitro"
}
```

Changing keywords from "gd, linear algebra, gf(2)" to "gd, linear algebra, gf(2), editor_malb".



---

archive/issue_comments_022998.json:
```json
{
    "body": "wstein, can you review my update until 6/18?",
    "created_at": "2008-06-16T03:29:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3324",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3324#issuecomment-22998",
    "user": "https://github.com/malb"
}
```

wstein, can you review my update until 6/18?



---

archive/issue_comments_022999.json:
```json
{
    "body": "Doesn't work on OS X:\n\n\n```\nImportError: dlopen(/Users/was/s/local/lib/python2.5/site-packages/sage/matrix/matrix_mod2_dense.so, 2): Symbol not found: _png_check_sig\n  Referenced from: /Users/was/s/local/lib//libgd.2.dylib\n  Expected in: flat namespace\n```\n",
    "created_at": "2008-06-19T23:14:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3324",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3324#issuecomment-22999",
    "user": "https://github.com/williamstein"
}
```

Doesn't work on OS X:


```
ImportError: dlopen(/Users/was/s/local/lib/python2.5/site-packages/sage/matrix/matrix_mod2_dense.so, 2): Symbol not found: _png_check_sig
  Referenced from: /Users/was/s/local/lib//libgd.2.dylib
  Expected in: flat namespace
```




---

archive/issue_comments_023000.json:
```json
{
    "body": "new patch addresses review",
    "created_at": "2008-06-20T03:44:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3324",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3324#issuecomment-23000",
    "user": "https://github.com/malb"
}
```

new patch addresses review



---

archive/issue_comments_023001.json:
```json
{
    "body": "Attachment [m4ri_png.patch](tarball://root/attachments/some-uuid/ticket3324/m4ri_png.patch) by @malb created at 2008-06-20 03:45:15\n\nThe attached patch addresses this issue.",
    "created_at": "2008-06-20T03:45:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3324",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3324#issuecomment-23001",
    "user": "https://github.com/malb"
}
```

Attachment [m4ri_png.patch](tarball://root/attachments/some-uuid/ticket3324/m4ri_png.patch) by @malb created at 2008-06-20 03:45:15

The attached patch addresses this issue.



---

archive/issue_comments_023002.json:
```json
{
    "body": "This does not fix the problem for me:\n\n\n```\n\n/Users/was/s/local/lib/python2.5/site-packages/sage/matrix/matrix_space.py in <module>()\n     36 import matrix_modn_sparse\n     37 \n---> 38 import matrix_mod2_dense\n     39 #import matrix_mod2_sparse\n     40 \n\nImportError: dlopen(/Users/was/s/local/lib/python2.5/site-packages/sage/matrix/matrix_mod2_dense.so, 2): Symbol not found: _png_check_sig\n  Referenced from: /Users/was/s/local/lib//libgd.2.dylib\n  Expected in: flat namespace\n\nsage: \n\n```\n",
    "created_at": "2008-06-20T04:12:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3324",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3324#issuecomment-23002",
    "user": "https://github.com/williamstein"
}
```

This does not fix the problem for me:


```

/Users/was/s/local/lib/python2.5/site-packages/sage/matrix/matrix_space.py in <module>()
     36 import matrix_modn_sparse
     37 
---> 38 import matrix_mod2_dense
     39 #import matrix_mod2_sparse
     40 

ImportError: dlopen(/Users/was/s/local/lib/python2.5/site-packages/sage/matrix/matrix_mod2_dense.so, 2): Symbol not found: _png_check_sig
  Referenced from: /Users/was/s/local/lib//libgd.2.dylib
  Expected in: flat namespace

sage: 

```




---

archive/issue_comments_023003.json:
```json
{
    "body": "Are you 100% sure that you rebuilt with the patch applied? Note that I just replaced the patch and thus the download manager might have called in somewhat else when downloading. I'm just asking because it works for me on OSX. I'll try on a different machine though.",
    "created_at": "2008-06-22T17:59:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3324",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3324#issuecomment-23003",
    "user": "https://github.com/malb"
}
```

Are you 100% sure that you rebuilt with the patch applied? Note that I just replaced the patch and thus the download manager might have called in somewhat else when downloading. I'm just asking because it works for me on OSX. I'll try on a different machine though.



---

archive/issue_comments_023004.json:
```json
{
    "body": "I cleanly applied the patch on bsd.math.washington.edu to a 100% fresh clean build of sage-3.0.3.  It does not work.  You should build sage on bsd, and get the patch to work there:\n\n\n```\nLoading SAGE library. Current Mercurial branch is: review\nException exceptions.ImportError: 'dlopen(/Users/was/build/sage-3.0.3/local/lib/python2.5/site-packages/sage/matrix/matrix_mod2_dense.so, 2): Symbol not found: _png_check_sig\\n  Referenced from: /Users/was/build/sage-3.0.3/local/lib//libgd.2.dylib\\n  Expected in: flat namespace\\n' in 'sage.rings.polynomial.polynomial_element.Polynomial_generic_dense.__normalize' ignored\nException exceptions.ImportError: 'dlopen(/Users/was/build/sage-3.0.3/local/lib/python2.5/site-packages/sage/matrix/matrix_mod2_dense.so, 2): Symbol not found: _png_check_sig\\n  Referenced from: /Users/was/build/sage-3.0.3/local/lib//libgd.2.dylib\\n  Expected in: flat namespace\\n' in 'sage.rings.polynomial.polynomial_element.Polynomial_generic_dense.__normalize' ignored\n---------------------------------------------------------------------------\nImportError                               Traceback (most recent call last)\n\n/Users/was/build/sage-3.0.3/local/bin/<ipython console> in <module>()\n\n/Users/was/build/sage-3.0.3/local/lib/python2.5/site-packages/sage/all_cmdline.py in <module>()\n     12 try:\n     13 \n---> 14     from sage.all import *\n     15     from sage.calculus.predefined import x\n     16     preparser(on=True)\n\n/Users/was/build/sage-3.0.3/local/lib/python2.5/site-packages/sage/all.py in <module>()\n     64 get_sigs()\n     65 \n---> 66 from sage.rings.all      import *\n     67 from sage.matrix.all     import *\n     68 \n\n/Users/was/build/sage-3.0.3/local/lib/python2.5/site-packages/sage/rings/all.py in <module>()\n     92 \n     93 # Algebraic numbers\n---> 94 from qqbar import (AlgebraicRealField, is_AlgebraicRealField, AA,\n     95                    AlgebraicReal, is_AlgebraicReal,\n     96                    AlgebraicField, is_AlgebraicField, QQbar,\n\n/Users/was/build/sage-3.0.3/local/lib/python2.5/site-packages/sage/rings/qqbar.py in <module>()\n   4734 \n   4735 \n-> 4736 RR_1_10 = RR(ZZ(1)/10)\n   4737 QQ_0 = QQ(0)\n   4738 QQ_1 = QQ(1)\n\n/Users/was/build/sage-3.0.3/local/bin/element.pyx in sage.structure.element.RingElement.__div__ (sage/structure/element.c:9074)()\n\n/Users/was/build/sage-3.0.3/local/bin/coerce.pyx in sage.structure.coerce.CoercionModel_cache_maps.bin_op_c (sage/structure/coerce.c:5088)()\n\n/Users/was/build/sage-3.0.3/local/bin/coerce.pyx in sage.structure.coerce.CoercionModel_cache_maps.canonical_coercion_c (sage/structure/coerce.c:5462)()\n\n/Users/was/build/sage-3.0.3/local/bin/coerce.pyx in sage.structure.coerce.CoercionModel_cache_maps.coercion_maps_c (sage/structure/coerce.c:6459)()\n\n/Users/was/build/sage-3.0.3/local/bin/coerce.pyx in sage.structure.coerce.CoercionModel_cache_maps.discover_coercion_c (sage/structure/coerce.c:7479)()\n\n/Users/was/build/sage-3.0.3/local/bin/parent.pyx in sage.structure.parent.Parent.coerce_map_from_c (sage/structure/parent.c:1061)()\n\n/Users/was/build/sage-3.0.3/local/bin/integer_ring.pyx in sage.rings.integer_ring.IntegerRing_class.coerce_map_from_c_impl (sage/rings/integer_ring.c:5224)()\n\n/Users/was/build/sage-3.0.3/local/bin/integer.pyx in sage.rings.integer.int_to_Z.__init__ (sage/rings/integer.c:20488)()\n\n/Users/was/build/sage-3.0.3/local/lib/python2.5/site-packages/sage/categories/homset.py in Hom(X, Y, cat)\n     57     if hasattr(X, '_Hom_'):\n     58         return X._Hom_(Y, cat)\n---> 59     import category_types\n     60     global _cache\n     61     key = (X,Y,cat)\n\n/Users/was/build/sage-3.0.3/local/lib/python2.5/site-packages/sage/categories/category_types.py in <module>()\n     24 from category import *\n     25 import sage.rings.all\n---> 26 import sage.algebras.all\n     27 \n     28 \n\n/Users/was/build/sage-3.0.3/local/lib/python2.5/site-packages/sage/algebras/all.py in <module>()\n     26 \n     27 from free_algebra import FreeAlgebra, is_FreeAlgebra\n---> 28 from free_algebra_quotient import FreeAlgebraQuotient\n     29 from quaternion_algebra import (QuaternionAlgebra, QuaternionAlgebraWithInnerProduct,\n     30      QuaternionAlgebraWithGramMatrix, QuaternionAlgebraWithDiscriminants,\n\n/Users/was/build/sage-3.0.3/local/lib/python2.5/site-packages/sage/algebras/free_algebra_quotient.py in <module>()\n     34 \n     35 from sage.rings.integer import Integer\n---> 36 from sage.modules.free_module import FreeModule\n     37 from sage.monoids.free_monoid import FreeMonoid\n     38 from sage.monoids.free_monoid_element import FreeMonoidElement\n\n/Users/was/build/sage-3.0.3/local/lib/python2.5/site-packages/sage/modules/free_module.py in <module>()\n    133 import module\n    134 \n--> 135 import sage.matrix.matrix_space\n    136 \n    137 import sage.misc.latex as latex\n\n/Users/was/build/sage-3.0.3/local/lib/python2.5/site-packages/sage/matrix/matrix_space.py in <module>()\n     36 import matrix_modn_sparse\n     37 \n---> 38 import matrix_mod2_dense\n     39 #import matrix_mod2_sparse\n     40 \n\nImportError: dlopen(/Users/was/build/sage-3.0.3/local/lib/python2.5/site-packages/sage/matrix/matrix_mod2_dense.so, 2): Symbol not found: _png_check_sig\n  Referenced from: /Users/was/build/sage-3.0.3/local/lib//libgd.2.dylib\n  Expected in: flat namespace\n\n\n```\n",
    "created_at": "2008-06-24T03:21:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3324",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3324#issuecomment-23004",
    "user": "https://github.com/williamstein"
}
```

I cleanly applied the patch on bsd.math.washington.edu to a 100% fresh clean build of sage-3.0.3.  It does not work.  You should build sage on bsd, and get the patch to work there:


```
Loading SAGE library. Current Mercurial branch is: review
Exception exceptions.ImportError: 'dlopen(/Users/was/build/sage-3.0.3/local/lib/python2.5/site-packages/sage/matrix/matrix_mod2_dense.so, 2): Symbol not found: _png_check_sig\n  Referenced from: /Users/was/build/sage-3.0.3/local/lib//libgd.2.dylib\n  Expected in: flat namespace\n' in 'sage.rings.polynomial.polynomial_element.Polynomial_generic_dense.__normalize' ignored
Exception exceptions.ImportError: 'dlopen(/Users/was/build/sage-3.0.3/local/lib/python2.5/site-packages/sage/matrix/matrix_mod2_dense.so, 2): Symbol not found: _png_check_sig\n  Referenced from: /Users/was/build/sage-3.0.3/local/lib//libgd.2.dylib\n  Expected in: flat namespace\n' in 'sage.rings.polynomial.polynomial_element.Polynomial_generic_dense.__normalize' ignored
---------------------------------------------------------------------------
ImportError                               Traceback (most recent call last)

/Users/was/build/sage-3.0.3/local/bin/<ipython console> in <module>()

/Users/was/build/sage-3.0.3/local/lib/python2.5/site-packages/sage/all_cmdline.py in <module>()
     12 try:
     13 
---> 14     from sage.all import *
     15     from sage.calculus.predefined import x
     16     preparser(on=True)

/Users/was/build/sage-3.0.3/local/lib/python2.5/site-packages/sage/all.py in <module>()
     64 get_sigs()
     65 
---> 66 from sage.rings.all      import *
     67 from sage.matrix.all     import *
     68 

/Users/was/build/sage-3.0.3/local/lib/python2.5/site-packages/sage/rings/all.py in <module>()
     92 
     93 # Algebraic numbers
---> 94 from qqbar import (AlgebraicRealField, is_AlgebraicRealField, AA,
     95                    AlgebraicReal, is_AlgebraicReal,
     96                    AlgebraicField, is_AlgebraicField, QQbar,

/Users/was/build/sage-3.0.3/local/lib/python2.5/site-packages/sage/rings/qqbar.py in <module>()
   4734 
   4735 
-> 4736 RR_1_10 = RR(ZZ(1)/10)
   4737 QQ_0 = QQ(0)
   4738 QQ_1 = QQ(1)

/Users/was/build/sage-3.0.3/local/bin/element.pyx in sage.structure.element.RingElement.__div__ (sage/structure/element.c:9074)()

/Users/was/build/sage-3.0.3/local/bin/coerce.pyx in sage.structure.coerce.CoercionModel_cache_maps.bin_op_c (sage/structure/coerce.c:5088)()

/Users/was/build/sage-3.0.3/local/bin/coerce.pyx in sage.structure.coerce.CoercionModel_cache_maps.canonical_coercion_c (sage/structure/coerce.c:5462)()

/Users/was/build/sage-3.0.3/local/bin/coerce.pyx in sage.structure.coerce.CoercionModel_cache_maps.coercion_maps_c (sage/structure/coerce.c:6459)()

/Users/was/build/sage-3.0.3/local/bin/coerce.pyx in sage.structure.coerce.CoercionModel_cache_maps.discover_coercion_c (sage/structure/coerce.c:7479)()

/Users/was/build/sage-3.0.3/local/bin/parent.pyx in sage.structure.parent.Parent.coerce_map_from_c (sage/structure/parent.c:1061)()

/Users/was/build/sage-3.0.3/local/bin/integer_ring.pyx in sage.rings.integer_ring.IntegerRing_class.coerce_map_from_c_impl (sage/rings/integer_ring.c:5224)()

/Users/was/build/sage-3.0.3/local/bin/integer.pyx in sage.rings.integer.int_to_Z.__init__ (sage/rings/integer.c:20488)()

/Users/was/build/sage-3.0.3/local/lib/python2.5/site-packages/sage/categories/homset.py in Hom(X, Y, cat)
     57     if hasattr(X, '_Hom_'):
     58         return X._Hom_(Y, cat)
---> 59     import category_types
     60     global _cache
     61     key = (X,Y,cat)

/Users/was/build/sage-3.0.3/local/lib/python2.5/site-packages/sage/categories/category_types.py in <module>()
     24 from category import *
     25 import sage.rings.all
---> 26 import sage.algebras.all
     27 
     28 

/Users/was/build/sage-3.0.3/local/lib/python2.5/site-packages/sage/algebras/all.py in <module>()
     26 
     27 from free_algebra import FreeAlgebra, is_FreeAlgebra
---> 28 from free_algebra_quotient import FreeAlgebraQuotient
     29 from quaternion_algebra import (QuaternionAlgebra, QuaternionAlgebraWithInnerProduct,
     30      QuaternionAlgebraWithGramMatrix, QuaternionAlgebraWithDiscriminants,

/Users/was/build/sage-3.0.3/local/lib/python2.5/site-packages/sage/algebras/free_algebra_quotient.py in <module>()
     34 
     35 from sage.rings.integer import Integer
---> 36 from sage.modules.free_module import FreeModule
     37 from sage.monoids.free_monoid import FreeMonoid
     38 from sage.monoids.free_monoid_element import FreeMonoidElement

/Users/was/build/sage-3.0.3/local/lib/python2.5/site-packages/sage/modules/free_module.py in <module>()
    133 import module
    134 
--> 135 import sage.matrix.matrix_space
    136 
    137 import sage.misc.latex as latex

/Users/was/build/sage-3.0.3/local/lib/python2.5/site-packages/sage/matrix/matrix_space.py in <module>()
     36 import matrix_modn_sparse
     37 
---> 38 import matrix_mod2_dense
     39 #import matrix_mod2_sparse
     40 

ImportError: dlopen(/Users/was/build/sage-3.0.3/local/lib/python2.5/site-packages/sage/matrix/matrix_mod2_dense.so, 2): Symbol not found: _png_check_sig
  Referenced from: /Users/was/build/sage-3.0.3/local/lib//libgd.2.dylib
  Expected in: flat namespace


```




---

archive/issue_comments_023005.json:
```json
{
    "body": "**State of affairs for editorial meeting 26/06/08**\n\nI do have a working copy on bsd and I'm trying to find out what exactly made it work for me.",
    "created_at": "2008-06-25T11:18:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3324",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3324#issuecomment-23005",
    "user": "https://github.com/malb"
}
```

**State of affairs for editorial meeting 26/06/08**

I do have a working copy on bsd and I'm trying to find out what exactly made it work for me.



---

archive/issue_comments_023006.json:
```json
{
    "body": "Okay, I found it:\n\n\n```\nif [ `uname` = \"Darwin\" -a \"$SAGE64\" = \"yes\" ]; then\n   echo \"Keeping 64 bit OSX libpng.dylib around\"\nelse\n    # There is a weird problem on Darwin where most programs\n    # will crash if they see the libpng built as part of this\n    # package instead of the system-wide apple libpng.  So\n    # we delete it.\n    # NOTE -- we *only* delete the dylib's.  Apps that need libpng can still link it in statically.\n    rm -f \"$SAGE_LOCAL\"/lib/libpng*dylib\n    rm -f \"$SAGE_LOCAL\"/lib/libpng*.la\nfi\n```\n\n\nfrom `spkg-install}} in libpng. Why do we even install it, if we remove it afterwards? Maybe the headers don't match the system wide libpng and thus linking for gd fails. This problem is also bigger than just my {{{Matrix_mod2_dense` patch. Mabshoff, any idea?",
    "created_at": "2008-06-25T12:52:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3324",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3324#issuecomment-23006",
    "user": "https://github.com/malb"
}
```

Okay, I found it:


```
if [ `uname` = "Darwin" -a "$SAGE64" = "yes" ]; then
   echo "Keeping 64 bit OSX libpng.dylib around"
else
    # There is a weird problem on Darwin where most programs
    # will crash if they see the libpng built as part of this
    # package instead of the system-wide apple libpng.  So
    # we delete it.
    # NOTE -- we *only* delete the dylib's.  Apps that need libpng can still link it in statically.
    rm -f "$SAGE_LOCAL"/lib/libpng*dylib
    rm -f "$SAGE_LOCAL"/lib/libpng*.la
fi
```


from `spkg-install}} in libpng. Why do we even install it, if we remove it afterwards? Maybe the headers don't match the system wide libpng and thus linking for gd fails. This problem is also bigger than just my {{{Matrix_mod2_dense` patch. Mabshoff, any idea?



---

archive/issue_comments_023007.json:
```json
{
    "body": "The problem with libpng.dylib is that certain spkgs like Python and R do not have LDFLAGS and CPPFLAGS set correctly so that on rebuilding them (on upgrade for example) we pick up the systems libpng which is broken. The issue has been corrected for Python, but some more work is needed for R and likely some other spkgs. \n\nCheers,\n\nMichael",
    "created_at": "2008-08-27T02:22:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3324",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3324#issuecomment-23007",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The problem with libpng.dylib is that certain spkgs like Python and R do not have LDFLAGS and CPPFLAGS set correctly so that on rebuilding them (on upgrade for example) we pick up the systems libpng which is broken. The issue has been corrected for Python, but some more work is needed for R and likely some other spkgs. 

Cheers,

Michael



---

archive/issue_comments_023008.json:
```json
{
    "body": "Guessing from William's failure above gd is also affected here. I believe #3792 will fix that issue.\n\nCheers,\n\nMichael",
    "created_at": "2008-08-27T02:23:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3324",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3324#issuecomment-23008",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Guessing from William's failure above gd is also affected here. I believe #3792 will fix that issue.

Cheers,

Michael



---

archive/issue_comments_023009.json:
```json
{
    "body": "I fixed all the problems on OSX in libpng.spkg, python.spkg and r.spkg and with those fixes the patch applies, builds correctly and all doctests pass on OSX. Positive review pending three other tickets I am about to open.\n\nCheers,\n\nMichael",
    "created_at": "2008-08-30T17:51:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3324",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3324#issuecomment-23009",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

I fixed all the problems on OSX in libpng.spkg, python.spkg and r.spkg and with those fixes the patch applies, builds correctly and all doctests pass on OSX. Positive review pending three other tickets I am about to open.

Cheers,

Michael



---

archive/issue_comments_023010.json:
```json
{
    "body": "The spkgs at \n\n* #4007\n* #4008\n* #4009\n\nfix the issues on OSX. Those three spkgs have been merged, so we can now merge this ticket.\n\nCheers,\n\nMichael",
    "created_at": "2008-08-31T00:07:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3324",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3324#issuecomment-23010",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The spkgs at 

* #4007
* #4008
* #4009

fix the issues on OSX. Those three spkgs have been merged, so we can now merge this ticket.

Cheers,

Michael



---

archive/issue_comments_023011.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-31T00:14:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3324",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3324#issuecomment-23011",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_023012.json:
```json
{
    "body": "Merged in Sage 3.1.2.alpha3",
    "created_at": "2008-08-31T00:14:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3324",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3324#issuecomment-23012",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.1.2.alpha3



---

archive/issue_events_007458.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-08-31T00:14:57Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3324",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3324#event-7458"
}
```
