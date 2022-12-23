# Issue 3794: [with preliminary patch, needs documentation] Create eigen functions for matrices

Issue created by migration from https://trac.sagemath.org/ticket/3794

Original creator: jason

Original creation time: 2008-08-09 14:40:16

Assignee: was

Make the following functions:

  * eigenvalues
  * eigenvectors_left, eigenvectors_right
  * eigenmatrix_left, eigenmatrix_right
  * eigenspaces_left, eigenspaces_right

(with the appropriate left_* and right_* aliases)



---

Comment by jason created at 2008-08-09 14:44:00

The patch up now adds the functions.  I'm finishing the doctests and doing any last minute polishing of the functions.


---

Attachment


---

Comment by jason created at 2008-08-10 04:02:14

This depends on #3654 and #3757


---

Comment by cremona created at 2008-08-10 11:30:33

The patch applies cleanly to 3.1.alpha0.  After also applying the patches at #3757, all doctests in sage.matrix pass.

I'm happy with the code but have some queries about the documentation mainly:

    1. In the docstrings for `eigenspaces_left()` and `eigenspaces_right()`, the sentence "If the eigenvalue is a root of a polynomial, then the algebraic multiplicity is for each root separately." is rather incomprehensible.  Do you mean something more like: "If the eigenvalues are given symbolically, as roots of an irreducible factor of the characteristic polynomial, then the algebraic multiplicity returned is the multiplicity of each conjugate eigenvalue."

    2. In the docstring for eigenvalues(self), the sentence "If the eigenvalues are roots of polynomials in CC, then QQbar elements are returned that represent each separate root." perhaps the "CC" should be "QQ"?

    3. I think it is brilliant that for matrices over QQ the eigenvalues are returned exactly in QQbar.  But I think this will confuse a lot of users who are not pure mathematicians.  Is there not an easier way of forcing eigenvalue/vector computations to be done over RR or CC?  (Apart from coercing the original matrix to be defined over one of thoswe fields.)  In any case, a docstring example showing how to see the eigenvalues as "ordinary" real or complex numbers might be welcome.

    4. The eigenmatrix examples left me wondering what would happen for non-diagonalizable matrices.  This should be explained, with examples.


---

Attachment

I've uploaded an eigenfunctions-2.patch, to be applied on top of the eigenfunctions.patch, which addresses cremona's comments.

Response to cremona's comments:

1. Change made.  Thanks.

2. Change made.  Thanks.

3. The computations could be done over RR and CC matrices, but a warning is raised since numerical error will most likely mean that the results will be junk.  The best way to approach something like this, I think, is to convert your matrix to RDF or CDF and use the numerical functions (these are also due to be overhauled and switched to a numpy backend).  The other way of doing this would be to convert from QQbar to CC, but that conversion is only enabled in 3.1 or later.  We could put in a one-line example: `[RR(eig) for eig in a.eigenvalues()]`, but not having 3.1, I can't test that very well.  If this is still an issue, I will put that one-line patch in after 3.1 comes out.

4. Doctest and explanation added.

Thanks for your comments and review!


---

Comment by cremona created at 2008-08-12 10:06:38

I'm happy with these responses.  I applied both patches to a fresh clone of 3.1.alpha1 with no trouble, and the doctests all pass.  This can go ahead in my opinion.


---

Comment by mabshoff created at 2008-08-13 00:59:30

Oops:

```
sage -t -long devel/doc/tut/tut.tex
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.1.alpha2/tmp/tut.py", line 1853:
    : g.eigenspaces()
Expected:
    [
    (4, Vector space of degree 2 and dimension 1 over Finite Field of size 7
    User basis matrix:
    [1 5]),
    (2, Vector space of degree 2 and dimension 1 over Finite Field of size 7
    User basis matrix:
    [1 1])
    ]
Got:
    [(4, Vector space of degree 2 and dimension 1 over Finite Field of size 7
    User basis matrix:
    [1 5]), (2, Vector space of degree 2 and dimension 1 over Finite Field of size 7
    User basis matrix:
    [1 1])]
**********************************************************************
1 items had failures:
   1 of   5 in __main__.example_85
***Test Failed*** 1 failures.
For whitespace errors, see the file /scratch/mabshoff/release-cycle/sage-3.1.alpha2/tmp/.doctest_tut.py

         [21.1 s]
sage -t -long devel/doc/const/const.tex
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.1.alpha2/tmp/const.py", line 1543:
    : A.eigenspaces(even_if_inexact=True) # random output
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/release-cycle/sage-3.1.alpha2/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_47[6]>", line 1, in <module>
        print "ignore this";  A.eigenspaces(even_if_inexact=True) # random output###line 1543:
    : A.eigenspaces(even_if_inexact=True) # random output
      File "matrix2.pyx", line 2433, in sage.matrix.matrix2.Matrix.eigenspaces (sage/matrix/matrix2.c:14504)
    AttributeError: 'module' object has no attribute 'deprecated'
**********************************************************************
1 items had failures:
   1 of   7 in __main__.example_47
***Test Failed*** 1 failures.
```



---

Comment by jason created at 2008-08-13 13:28:26

Thanks.  I kept testing the matrix/* directory.  I'll fix these momentarily and post a patch.

How do I doctest just the tutorial?  Right now, I'm running `make test`, and thankfully the documentation tests are near the beginning.


---

Comment by jason created at 2008-08-13 14:58:58

Both bugs were small errors in the functions, so yeah for doctests.

Attached are two patches.  eigenfunctions-3.patch is to be applied on top of the eigenfunctions-2.patch.  The eigenfunctions-doc.patch changes some of the documentation to talk about the new functions and should be applied to the doc repository.


---

Attachment


---

Comment by cremona created at 2008-08-23 17:08:09

This looks fine to me.


---

Comment by mabshoff created at 2008-08-25 22:07:32

Resolution: fixed


---

Comment by mabshoff created at 2008-08-25 22:07:32

Merged all four patches in Sage 3.1.2.alpha1
