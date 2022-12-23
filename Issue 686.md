# Issue 686: write MPolynomial_libsingular over number fields

archive/issues_000686.json:
```json
{
    "body": "Assignee: somebody\n\nthis requires writing a conversion route from/to number field elements to liBSINGULAR's native format.\n\nIssue created by migration from https://trac.sagemath.org/ticket/686\n\n",
    "created_at": "2007-09-18T12:45:09Z",
    "labels": [
        "basic arithmetic",
        "major",
        "enhancement"
    ],
    "title": "write MPolynomial_libsingular over number fields",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/686",
    "user": "malb"
}
```
Assignee: somebody

this requires writing a conversion route from/to number field elements to liBSINGULAR's native format.

Issue created by migration from https://trac.sagemath.org/ticket/686





---

archive/issue_comments_003561.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-10-21T22:51:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/686",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/686#issuecomment-3561",
    "user": "malb"
}
```

Changing status from new to assigned.



---

archive/issue_comments_003562.json:
```json
{
    "body": "Changing assignee from somebody to malb.",
    "created_at": "2007-10-21T22:51:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/686",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/686#issuecomment-3562",
    "user": "malb"
}
```

Changing assignee from somebody to malb.



---

archive/issue_comments_003563.json:
```json
{
    "body": "Well, after a year. Here is the patch",
    "created_at": "2008-08-30T00:17:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/686",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/686#issuecomment-3563",
    "user": "malb"
}
```

Well, after a year. Here is the patch



---

archive/issue_comments_003564.json:
```json
{
    "body": "What version of sage is this against?  I can't apply it to sage-3.1.1.  I fixed the one broken hunk and got this during the build?\n\n```\nhg_sage: hg_sage.apply('mpolynomial_libsingular_qqa.patch')\ncd \"/Users/was/s/devel/sage\" && hg status\ncd \"/Users/was/s/devel/sage\" && hg status\ncd \"/Users/was/s/devel/sage\" && hg import   \"/Users/was/Downloads/mpolynomial_libsingular_qqa.patch\"\napplying /Users/was/Downloads/mpolynomial_libsingular_qqa.patch\npatching file sage/rings/polynomial/multi_polynomial.pyx\nHunk #1 succeeded at 677 with fuzz 2 (offset -24 lines).\npatching file sage/rings/polynomial/multi_polynomial_element.py\nHunk #20 FAILED at 1276\n1 out of 24 hunks FAILED -- saving rejects to file sage/rings/polynomial/multi_polynomial_element.py.rej\nabort: patch failed to apply\n... fix hunk ...\nteragon-2:Downloads was$ sage -br\n\n----------------------------------------------------------\nsage: Building and installing modified SAGE library files.\n\n\nInstalling c_lib\nscons: `install' is up to date.\nUpdating Cython code....\nsage/structure/coerce.pyx --> /Users/was/s/local//lib/python/site-packages//sage/structure/coerce.pyx\n\nBuilding sage/structure/coerce.c because it depends on sage/structure/coerce.pyx.\npython2.5 `which cython` --embed-positions --incref-local-binop -I/Users/was/s/devel/sage-bugs -o sage/structure/coerce.c sage/structure/coerce.pyx\n\nBuilding sage/matrix/matrix_mpolynomial_dense.cpp because it depends on sage/libs/singular/singular-cdefs.pxi.\npython2.5 `which cython` --embed-positions --incref-local-binop -I/Users/was/s/devel/sage-bugs -o sage/matrix/matrix_mpolynomial_dense.cpp sage/matrix/matrix_mpolynomial_dense.pyx\n\nError converting Pyrex file to C:\n------------------------------------------------------------\n...\n    cdef object _entries\n\ncimport matrix_window\n\ncdef class MatrixWindow(matrix_window.MatrixWindow):\n    cdef Matrix_generic_dense _matrix\n                             ^\n------------------------------------------------------------\n\n/Users/was/s/devel/sage-bugs/sage/matrix/matrix_generic_dense.pxd:9:30: '_matrix' redeclared \n\nError converting Pyrex file to C:\n------------------------------------------------------------\n...\n\ncimport matrix_window\n\ncdef class MatrixWindow(matrix_window.MatrixWindow):\n    cdef Matrix_generic_dense _matrix\n    cdef int _row\n            ^\n------------------------------------------------------------\n\n/Users/was/s/devel/sage-bugs/sage/matrix/matrix_generic_dense.pxd:10:13: '_row' redeclared \n\nError converting Pyrex file to C:\n------------------------------------------------------------\n...\ncimport matrix_window\n\ncdef class MatrixWindow(matrix_window.MatrixWindow):\n    cdef Matrix_generic_dense _matrix\n    cdef int _row\n    cdef int _col\n            ^\n------------------------------------------------------------\n\n/Users/was/s/devel/sage-bugs/sage/matrix/matrix_generic_dense.pxd:11:13: '_col' redeclared \n\nError converting Pyrex file to C:\n------------------------------------------------------------\n...\n\ncdef class MatrixWindow(matrix_window.MatrixWindow):\n    cdef Matrix_generic_dense _matrix\n    cdef int _row\n    cdef int _col\n    cdef int _nrows\n            ^\n------------------------------------------------------------\n\n/Users/was/s/devel/sage-bugs/sage/matrix/matrix_generic_dense.pxd:12:13: '_nrows' redeclared \n\nError converting Pyrex file to C:\n------------------------------------------------------------\n...\ncdef class MatrixWindow(matrix_window.MatrixWindow):\n    cdef Matrix_generic_dense _matrix\n    cdef int _row\n    cdef int _col\n    cdef int _nrows\n    cdef int _ncols\n            ^\n------------------------------------------------------------\n\n/Users/was/s/devel/sage-bugs/sage/matrix/matrix_generic_dense.pxd:13:13: '_ncols' redeclared \n\nError converting Pyrex file to C:\n\n\nsage: Error running cython.\nsage: There was an error installing modified sage library code.\n\nteragon-2:Downloads was$ \n```\n\n\nAm I doing something dumb?  Thanks.",
    "created_at": "2008-08-30T01:07:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/686",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/686#issuecomment-3564",
    "user": "was"
}
```

What version of sage is this against?  I can't apply it to sage-3.1.1.  I fixed the one broken hunk and got this during the build?

```
hg_sage: hg_sage.apply('mpolynomial_libsingular_qqa.patch')
cd "/Users/was/s/devel/sage" && hg status
cd "/Users/was/s/devel/sage" && hg status
cd "/Users/was/s/devel/sage" && hg import   "/Users/was/Downloads/mpolynomial_libsingular_qqa.patch"
applying /Users/was/Downloads/mpolynomial_libsingular_qqa.patch
patching file sage/rings/polynomial/multi_polynomial.pyx
Hunk #1 succeeded at 677 with fuzz 2 (offset -24 lines).
patching file sage/rings/polynomial/multi_polynomial_element.py
Hunk #20 FAILED at 1276
1 out of 24 hunks FAILED -- saving rejects to file sage/rings/polynomial/multi_polynomial_element.py.rej
abort: patch failed to apply
... fix hunk ...
teragon-2:Downloads was$ sage -br

----------------------------------------------------------
sage: Building and installing modified SAGE library files.


Installing c_lib
scons: `install' is up to date.
Updating Cython code....
sage/structure/coerce.pyx --> /Users/was/s/local//lib/python/site-packages//sage/structure/coerce.pyx

Building sage/structure/coerce.c because it depends on sage/structure/coerce.pyx.
python2.5 `which cython` --embed-positions --incref-local-binop -I/Users/was/s/devel/sage-bugs -o sage/structure/coerce.c sage/structure/coerce.pyx

Building sage/matrix/matrix_mpolynomial_dense.cpp because it depends on sage/libs/singular/singular-cdefs.pxi.
python2.5 `which cython` --embed-positions --incref-local-binop -I/Users/was/s/devel/sage-bugs -o sage/matrix/matrix_mpolynomial_dense.cpp sage/matrix/matrix_mpolynomial_dense.pyx

Error converting Pyrex file to C:
------------------------------------------------------------
...
    cdef object _entries

cimport matrix_window

cdef class MatrixWindow(matrix_window.MatrixWindow):
    cdef Matrix_generic_dense _matrix
                             ^
------------------------------------------------------------

/Users/was/s/devel/sage-bugs/sage/matrix/matrix_generic_dense.pxd:9:30: '_matrix' redeclared 

Error converting Pyrex file to C:
------------------------------------------------------------
...

cimport matrix_window

cdef class MatrixWindow(matrix_window.MatrixWindow):
    cdef Matrix_generic_dense _matrix
    cdef int _row
            ^
------------------------------------------------------------

/Users/was/s/devel/sage-bugs/sage/matrix/matrix_generic_dense.pxd:10:13: '_row' redeclared 

Error converting Pyrex file to C:
------------------------------------------------------------
...
cimport matrix_window

cdef class MatrixWindow(matrix_window.MatrixWindow):
    cdef Matrix_generic_dense _matrix
    cdef int _row
    cdef int _col
            ^
------------------------------------------------------------

/Users/was/s/devel/sage-bugs/sage/matrix/matrix_generic_dense.pxd:11:13: '_col' redeclared 

Error converting Pyrex file to C:
------------------------------------------------------------
...

cdef class MatrixWindow(matrix_window.MatrixWindow):
    cdef Matrix_generic_dense _matrix
    cdef int _row
    cdef int _col
    cdef int _nrows
            ^
------------------------------------------------------------

/Users/was/s/devel/sage-bugs/sage/matrix/matrix_generic_dense.pxd:12:13: '_nrows' redeclared 

Error converting Pyrex file to C:
------------------------------------------------------------
...
cdef class MatrixWindow(matrix_window.MatrixWindow):
    cdef Matrix_generic_dense _matrix
    cdef int _row
    cdef int _col
    cdef int _nrows
    cdef int _ncols
            ^
------------------------------------------------------------

/Users/was/s/devel/sage-bugs/sage/matrix/matrix_generic_dense.pxd:13:13: '_ncols' redeclared 

Error converting Pyrex file to C:


sage: Error running cython.
sage: There was an error installing modified sage library code.

teragon-2:Downloads was$ 
```


Am I doing something dumb?  Thanks.



---

archive/issue_comments_003565.json:
```json
{
    "body": "My guess would be Sage 3.1.2.alpha2. A lot of fixes in that area went into 3.1.2.X:\n\n```\nmabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.1.2.alpha3/devel/sage$ patch -p1 --dry-run < mpolynomial_libsingular_qqa.patch \npatching file sage/libs/singular/singular-cdefs.pxi\npatching file sage/libs/singular/singular.pxd\npatching file sage/libs/singular/singular.pyx\npatching file sage/rings/arith.py\npatching file sage/rings/number_field/number_field.py\nHunk #1 succeeded at 3301 (offset 14 lines).\nHunk #2 succeeded at 4200 (offset 14 lines).\npatching file sage/rings/number_field/number_field_base.pxd\npatching file sage/rings/polynomial/multi_polynomial.pyx\npatching file sage/rings/polynomial/multi_polynomial_element.py\npatching file sage/rings/polynomial/multi_polynomial_ideal.py\npatching file sage/rings/polynomial/multi_polynomial_libsingular.pyx\npatching file sage/rings/polynomial/polynomial_singular_interface.py\npatching file sage/structure/coerce.pyx\n```\n\nThere is a 3.1.2.alph2 binary for sage.math in the \"usual place\".\n\nCheers,\n\nMichael",
    "created_at": "2008-08-30T01:12:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/686",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/686#issuecomment-3565",
    "user": "mabshoff"
}
```

My guess would be Sage 3.1.2.alpha2. A lot of fixes in that area went into 3.1.2.X:

```
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.1.2.alpha3/devel/sage$ patch -p1 --dry-run < mpolynomial_libsingular_qqa.patch 
patching file sage/libs/singular/singular-cdefs.pxi
patching file sage/libs/singular/singular.pxd
patching file sage/libs/singular/singular.pyx
patching file sage/rings/arith.py
patching file sage/rings/number_field/number_field.py
Hunk #1 succeeded at 3301 (offset 14 lines).
Hunk #2 succeeded at 4200 (offset 14 lines).
patching file sage/rings/number_field/number_field_base.pxd
patching file sage/rings/polynomial/multi_polynomial.pyx
patching file sage/rings/polynomial/multi_polynomial_element.py
patching file sage/rings/polynomial/multi_polynomial_ideal.py
patching file sage/rings/polynomial/multi_polynomial_libsingular.pyx
patching file sage/rings/polynomial/polynomial_singular_interface.py
patching file sage/structure/coerce.pyx
```

There is a 3.1.2.alph2 binary for sage.math in the "usual place".

Cheers,

Michael



---

archive/issue_comments_003566.json:
```json
{
    "body": "With the patch applied I see one doctest failure which is trivial to fix by making that doctest optional:\n\n```\nsage -t -long devel/sage/sage/rings/polynomial/multi_polynomial_element.py\n**********************************************************************\nFile \"/scratch/mabshoff/release-cycle/sage-3.1.2.alpha3/tmp/multi_polynomial_element.py\", line 285:\n    sage: h = f._macaulay2_()\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/mabshoff/release-cycle/sage-3.1.2.alpha3/local/lib/python2.5/doctest.py\", line 1228, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_10[4]>\", line 1, in <module>\n        h = f._macaulay2_()###line 285:\n    sage: h = f._macaulay2_()\n      File \"/scratch/mabshoff/release-cycle/sage-3.1.2.alpha3/local/lib/python2.5/site-packages/sage/rings/polynomial/multi_polynomial_element.py\", line 296, in _macaulay2_\n        self.parent()._macaulay2_set_ring(macaulay2)\n      File \"/scratch/mabshoff/release-cycle/sage-3.1.2.alpha3/local/lib/python2.5/site-packages/sage/rings/polynomial/multi_polynomial_ring.py\", line 115, in _macaulay2_set_ring\n        self.term_order().macaulay2_str())\n      File \"/scratch/mabshoff/release-cycle/sage-3.1.2.alpha3/local/lib/python2.5/site-packages/sage/interfaces/macaulay2.py\", line 409, in ring\n        return self.new('%s[%s, MonomialSize=>16, MonomialOrder=>%s]'%(base_ring, varstr, order))\n      File \"/scratch/mabshoff/release-cycle/sage-3.1.2.alpha3/local/lib/python2.5/site-packages/sage/interfaces/expect.py\", line 1028, in new\n        return self(code)\n      File \"/scratch/mabshoff/release-cycle/sage-3.1.2.alpha3/local/lib/python2.5/site-packages/sage/interfaces/expect.py\", line 963, in __call__\n        return cls(self, x, name=name)\n      File \"/scratch/mabshoff/release-cycle/sage-3.1.2.alpha3/local/lib/python2.5/site-packages/sage/interfaces/expect.py\", line 1264, in __init__\n        raise TypeError, x\n    TypeError: Unable to start macaulay2\n**********************************************************************\n```\n",
    "created_at": "2008-08-30T01:40:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/686",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/686#issuecomment-3566",
    "user": "mabshoff"
}
```

With the patch applied I see one doctest failure which is trivial to fix by making that doctest optional:

```
sage -t -long devel/sage/sage/rings/polynomial/multi_polynomial_element.py
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.1.2.alpha3/tmp/multi_polynomial_element.py", line 285:
    sage: h = f._macaulay2_()
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/release-cycle/sage-3.1.2.alpha3/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_10[4]>", line 1, in <module>
        h = f._macaulay2_()###line 285:
    sage: h = f._macaulay2_()
      File "/scratch/mabshoff/release-cycle/sage-3.1.2.alpha3/local/lib/python2.5/site-packages/sage/rings/polynomial/multi_polynomial_element.py", line 296, in _macaulay2_
        self.parent()._macaulay2_set_ring(macaulay2)
      File "/scratch/mabshoff/release-cycle/sage-3.1.2.alpha3/local/lib/python2.5/site-packages/sage/rings/polynomial/multi_polynomial_ring.py", line 115, in _macaulay2_set_ring
        self.term_order().macaulay2_str())
      File "/scratch/mabshoff/release-cycle/sage-3.1.2.alpha3/local/lib/python2.5/site-packages/sage/interfaces/macaulay2.py", line 409, in ring
        return self.new('%s[%s, MonomialSize=>16, MonomialOrder=>%s]'%(base_ring, varstr, order))
      File "/scratch/mabshoff/release-cycle/sage-3.1.2.alpha3/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 1028, in new
        return self(code)
      File "/scratch/mabshoff/release-cycle/sage-3.1.2.alpha3/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 963, in __call__
        return cls(self, x, name=name)
      File "/scratch/mabshoff/release-cycle/sage-3.1.2.alpha3/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 1264, in __init__
        raise TypeError, x
    TypeError: Unable to start macaulay2
**********************************************************************
```




---

archive/issue_comments_003567.json:
```json
{
    "body": "Yes, I based it on 3.1.2.alpha2 since so much changed there since 3.1.1. I wonder why I missed the M2 failure. I'll fix that tomorrow.",
    "created_at": "2008-08-30T02:15:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/686",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/686#issuecomment-3567",
    "user": "malb"
}
```

Yes, I based it on 3.1.2.alpha2 since so much changed there since 3.1.1. I wonder why I missed the M2 failure. I'll fix that tomorrow.



---

archive/issue_comments_003568.json:
```json
{
    "body": "Replying to [comment:7 malb]:\n> Yes, I based it on 3.1.2.alpha2 since so much changed there since 3.1.1. I wonder why I missed the M2 failure. I'll fix that tomorrow.\n\nMaybe the -long played a role? Either way: should this get a positive review by William it is trivial for either one of us to fix the issue, so don't worry about it. \n\nCheers,\n\nMichael",
    "created_at": "2008-08-30T02:18:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/686",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/686#issuecomment-3568",
    "user": "mabshoff"
}
```

Replying to [comment:7 malb]:
> Yes, I based it on 3.1.2.alpha2 since so much changed there since 3.1.1. I wonder why I missed the M2 failure. I'll fix that tomorrow.

Maybe the -long played a role? Either way: should this get a positive review by William it is trivial for either one of us to fix the issue, so don't worry about it. 

Cheers,

Michael



---

archive/issue_comments_003569.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-08-31T16:10:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/686",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/686#issuecomment-3569",
    "user": "malb"
}
```

Attachment



---

archive/issue_comments_003570.json:
```json
{
    "body": "the attached patch fixes the M2 failure by making it optional",
    "created_at": "2008-08-31T16:11:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/686",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/686#issuecomment-3570",
    "user": "malb"
}
```

the attached patch fixes the M2 failure by making it optional



---

archive/issue_comments_003571.json:
```json
{
    "body": "This applies to 3.1.3.alpha1 with one tiny reject in libs/singular/singular-cdefs.pxi which is easily fixed (it just removes the newline at the end of the file).\n\nI have two small objections, which are however too minor to keep this from being merged (hence the positive review):\n\n* looking at the revised doctests, it seems that the way polynomials are now printed is slightly uglier than before: e.g. (g)*b!^2 instead of g*b!^2.  I don't know how hard this would be to fix, or even whether it would be desirable\n* a few places in the docstrings have SAGE instead of Sage; we really ought to pick one (and AFAIK this has been done) and stick with it.",
    "created_at": "2008-09-28T06:12:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/686",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/686#issuecomment-3571",
    "user": "AlexGhitza"
}
```

This applies to 3.1.3.alpha1 with one tiny reject in libs/singular/singular-cdefs.pxi which is easily fixed (it just removes the newline at the end of the file).

I have two small objections, which are however too minor to keep this from being merged (hence the positive review):

* looking at the revised doctests, it seems that the way polynomials are now printed is slightly uglier than before: e.g. (g)*b!^2 instead of g*b!^2.  I don't know how hard this would be to fix, or even whether it would be desirable
* a few places in the docstrings have SAGE instead of Sage; we really ought to pick one (and AFAIK this has been done) and stick with it.



---

archive/issue_comments_003572.json:
```json
{
    "body": "Replying to [comment:10 AlexGhitza]:\n\n>  * a few places in the docstrings have SAGE instead of Sage; we really ought to pick one (and AFAIK this has been done) and stick with it.\n\nThe agreed upon spelling these days is Sage. The problem with malb's patch is that there is no TeX macro, so as is the documentation fails to build. But I will just add the `\\Sage` macro to `commontex/macros-new.tex` so that this issue is gone once and for all. Once we make the ReST transition we should use Sage instead of SAGE or sage in the documentation.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-28T08:42:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/686",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/686#issuecomment-3572",
    "user": "mabshoff"
}
```

Replying to [comment:10 AlexGhitza]:

>  * a few places in the docstrings have SAGE instead of Sage; we really ought to pick one (and AFAIK this has been done) and stick with it.

The agreed upon spelling these days is Sage. The problem with malb's patch is that there is no TeX macro, so as is the documentation fails to build. But I will just add the `\Sage` macro to `commontex/macros-new.tex` so that this issue is gone once and for all. Once we make the ReST transition we should use Sage instead of SAGE or sage in the documentation.

Cheers,

Michael



---

archive/issue_comments_003573.json:
```json
{
    "body": "Replying to [comment:10 AlexGhitza]:\n>  * looking at the revised doctests, it seems that the way polynomials are now printed is slightly uglier than before: e.g. (g)*b!^2 instead of g*b!^2.  I don't know how hard this would be to fix, or even whether it would be desirable\n\nAs the coefficients are not atomic (e.g., a + 1) this doesn't seem too bad to me. Fixing this -- if one wanted to -- would require writing one's own print function instead of using Singular's.\n\n>  * a few places in the docstrings have SAGE instead of Sage; we really ought to pick one (and AFAIK this has been done) and stick with it.\n\nYep, I can provide a follow-up patch soon-ish to deal with those.",
    "created_at": "2008-09-28T12:16:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/686",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/686#issuecomment-3573",
    "user": "malb"
}
```

Replying to [comment:10 AlexGhitza]:
>  * looking at the revised doctests, it seems that the way polynomials are now printed is slightly uglier than before: e.g. (g)*b!^2 instead of g*b!^2.  I don't know how hard this would be to fix, or even whether it would be desirable

As the coefficients are not atomic (e.g., a + 1) this doesn't seem too bad to me. Fixing this -- if one wanted to -- would require writing one's own print function instead of using Singular's.

>  * a few places in the docstrings have SAGE instead of Sage; we really ought to pick one (and AFAIK this has been done) and stick with it.

Yep, I can provide a follow-up patch soon-ish to deal with those.



---

archive/issue_comments_003574.json:
```json
{
    "body": "Hi malb,\n\nwhen I merge this patch the sr.py doctest goes from 650 to over 1100 seconds:\n\n```\nmabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.1.3.alpha2$ ./sage -t -long devel//sage/sage/crypto/mq/sr.py\nsage -t -long devel/sage/sage/crypto/mq/sr.py\n         [1116.7 s]\n```\n\nWe do not seem to add any doctests to sr.py. Do you still want me to merge it? I also have #4021 and #4022 ready to merge, but since they depend on this patch I am holding off on your decision.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-28T17:03:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/686",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/686#issuecomment-3574",
    "user": "mabshoff"
}
```

Hi malb,

when I merge this patch the sr.py doctest goes from 650 to over 1100 seconds:

```
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.1.3.alpha2$ ./sage -t -long devel//sage/sage/crypto/mq/sr.py
sage -t -long devel/sage/sage/crypto/mq/sr.py
         [1116.7 s]
```

We do not seem to add any doctests to sr.py. Do you still want me to merge it? I also have #4021 and #4022 ready to merge, but since they depend on this patch I am holding off on your decision.

Cheers,

Michael



---

archive/issue_comments_003575.json:
```json
{
    "body": "\n```\n[11:08am] malb: hi mabshoff\n[11:08am] malb: I'm looking at the sr issue now\n[11:08am] mabshoff: Ok, I want to merge the patches and then deal with the speed regression later.\n[11:08am] malb: I suppose the slowdown is due to the fact that the MPolynomialRing constructor got more complicated\n[11:08am] malb: +1\n[11:08am] mabshoff: Because those patches would bitrot.\n[11:08am] mabshoff: Ok, merging then.\n```\n",
    "created_at": "2008-09-28T18:14:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/686",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/686#issuecomment-3575",
    "user": "mabshoff"
}
```


```
[11:08am] malb: hi mabshoff
[11:08am] malb: I'm looking at the sr issue now
[11:08am] mabshoff: Ok, I want to merge the patches and then deal with the speed regression later.
[11:08am] malb: I suppose the slowdown is due to the fact that the MPolynomialRing constructor got more complicated
[11:08am] malb: +1
[11:08am] mabshoff: Because those patches would bitrot.
[11:08am] mabshoff: Ok, merging then.
```




---

archive/issue_comments_003576.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-28T18:15:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/686",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/686#issuecomment-3576",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_003577.json:
```json
{
    "body": "Merged in Sage 3.1.3.alpha2",
    "created_at": "2008-09-28T18:15:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/686",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/686#issuecomment-3577",
    "user": "mabshoff"
}
```

Merged in Sage 3.1.3.alpha2
