# Issue 9012: singular_decomposition fails on non-interreduced Gröbner basis

Issue created by migration from https://trac.sagemath.org/ticket/9012

Original creator: mmezzarobba

Original creation time: 2010-05-21 20:14:24

Assignee: malb

The docstring of ``sage.ring.polynomial.multi_polynomial_ideal.triangular_decomposition`` says:

```
        This requires that the given basis is reduced w.r.t. to the
        lexicographical monomial ordering. If the basis of self does
        not have this property, the required Groebner basis is
        computed implicitly.
```

however (Sage 4.4.1):

```
sage: R.<x,y> = QQ[]
sage: J = Ideal(x^2+y^2-2, y^2-1)
sage: J.triangular_decomposition()
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

[...]
TypeError: Singular error:
// ** _ is no standard basis
   ? The ideal sage22 has to be given by a reduced SB
   ? error occurred in STDIN line 101: `def sage24=fglm(sage19,sage22);


---

Attachment


---

Comment by malb created at 2010-07-12 15:39:20

Changing status from new to needs_review.


---

Comment by SimonKing created at 2010-07-14 15:35:25

Changing status from needs_review to positive_review.


---

Comment by SimonKing created at 2010-07-14 15:35:25

The changes in the code are reasonable, it is doctested, and `sage -testall` passes.

So: Positive review!

Martin and I discussed one potential issue, namely that the method does not set `degBound=0` in Singular. But this should be on a different ticket and will involve decorators.


---

Comment by mpatel created at 2010-07-21 01:45:14

Resolution: fixed
