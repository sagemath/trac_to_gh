# Issue 686: write MPolynomial_libsingular over number fields

Issue created by migration from Trac.

Original creator: malb

Original creation time: 2007-09-18 12:45:09

Assignee: somebody

this requires writing a conversion route from/to number field elements to liBSINGULAR's native format.


---

Comment by malb created at 2007-10-21 22:51:41

Changing status from new to assigned.


---

Comment by malb created at 2007-10-21 22:51:41

Changing assignee from somebody to malb.


---

Comment by malb created at 2008-08-30 00:17:32

Well, after a year. Here is the patch


---

Comment by was created at 2008-08-30 01:07:26

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

Comment by mabshoff created at 2008-08-30 01:12:37

My guess would be Sage 3.1.2.alpha2. A lot of fixes in that area went into 3.1.2.X:

```
mabshoff`@`sage:/scratch/mabshoff/release-cycle/sage-3.1.2.alpha3/devel/sage$ patch -p1 --dry-run < mpolynomial_libsingular_qqa.patch 
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

Comment by mabshoff created at 2008-08-30 01:40:44

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

Comment by malb created at 2008-08-30 02:15:28

Yes, I based it on 3.1.2.alpha2 since so much changed there since 3.1.1. I wonder why I missed the M2 failure. I'll fix that tomorrow.


---

Comment by mabshoff created at 2008-08-30 02:18:04

Replying to [comment:7 malb]:
> Yes, I based it on 3.1.2.alpha2 since so much changed there since 3.1.1. I wonder why I missed the M2 failure. I'll fix that tomorrow.

Maybe the -long played a role? Either way: should this get a positive review by William it is trivial for either one of us to fix the issue, so don't worry about it. 

Cheers,

Michael


---

Attachment


---

Comment by malb created at 2008-08-31 16:11:06

the attached patch fixes the M2 failure by making it optional


---

Comment by AlexGhitza created at 2008-09-28 06:12:01

This applies to 3.1.3.alpha1 with one tiny reject in libs/singular/singular-cdefs.pxi which is easily fixed (it just removes the newline at the end of the file).

I have two small objections, which are however too minor to keep this from being merged (hence the positive review):

 * looking at the revised doctests, it seems that the way polynomials are now printed is slightly uglier than before: e.g. (g)*b!^2 instead of g*b!^2.  I don't know how hard this would be to fix, or even whether it would be desirable
 * a few places in the docstrings have SAGE instead of Sage; we really ought to pick one (and AFAIK this has been done) and stick with it.


---

Comment by mabshoff created at 2008-09-28 08:42:57

Replying to [comment:10 AlexGhitza]:

>  * a few places in the docstrings have SAGE instead of Sage; we really ought to pick one (and AFAIK this has been done) and stick with it.

The agreed upon spelling these days is Sage. The problem with malb's patch is that there is no TeX macro, so as is the documentation fails to build. But I will just add the `\Sage` macro to `commontex/macros-new.tex` so that this issue is gone once and for all. Once we make the ReST transition we should use Sage instead of SAGE or sage in the documentation.

Cheers,

Michael


---

Comment by malb created at 2008-09-28 12:16:06

Replying to [comment:10 AlexGhitza]:
>  * looking at the revised doctests, it seems that the way polynomials are now printed is slightly uglier than before: e.g. (g)*b!^2 instead of g*b!^2.  I don't know how hard this would be to fix, or even whether it would be desirable

As the coefficients are not atomic (e.g., a + 1) this doesn't seem too bad to me. Fixing this -- if one wanted to -- would require writing one's own print function instead of using Singular's.

>  * a few places in the docstrings have SAGE instead of Sage; we really ought to pick one (and AFAIK this has been done) and stick with it.

Yep, I can provide a follow-up patch soon-ish to deal with those.


---

Comment by mabshoff created at 2008-09-28 17:03:29

Hi malb,

when I merge this patch the sr.py doctest goes from 650 to over 1100 seconds:

```
mabshoff`@`sage:/scratch/mabshoff/release-cycle/sage-3.1.3.alpha2$ ./sage -t -long devel//sage/sage/crypto/mq/sr.py
sage -t -long devel/sage/sage/crypto/mq/sr.py
         [1116.7 s]
```

We do not seem to add any doctests to sr.py. Do you still want me to merge it? I also have #4021 and #4022 ready to merge, but since they depend on this patch I am holding off on your decision.

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-28 18:14:58


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

Comment by mabshoff created at 2008-09-28 18:15:11

Resolution: fixed


---

Comment by mabshoff created at 2008-09-28 18:15:11

Merged in Sage 3.1.3.alpha2
