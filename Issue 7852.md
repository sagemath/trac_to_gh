# Issue 7852: solve_left for RDF matrices is WRONG

Issue created by migration from Trac.

Original creator: was

Original creation time: 2010-01-05 21:40:18

Assignee: was

CC:  jason

Observe the docstring for solve_left for an RDF matrix:

```
sage: A = random_matrix(RDF,3)
sage: A.solve_left?
Solve the equation A*x = b, where
        
        EXAMPLES:
            sage: A = matrix(RDF, 3,3, [1,2,5,7.6,2.3,1,1,2,-1]); A
            [ 1.0  2.0  5.0]
            [ 7.6  2.3  1.0]
            [ 1.0  2.0 -1.0]
            sage: b = vector(RDF,[1,2,3])
            sage: x = A.solve_left(b); x
            (-0.113695090439, 1.39018087855, -0.333333333333)
            sage: A*x
            (1.0, 2.0, 3.0)
```


But that is solve_right. 

This was evidently introduced by maybe Grout's "Switch the RDF and CDF matrices to a numpy 1.2 backend; factor out common functionality to matrix_double_dense.pyx.".

Reported by Stephanie Dietzel


---

Comment by jason created at 2010-01-05 22:16:07

This might be related to #4932.  I'll put this on my list for the bug day coming up.


---

Attachment


---

Comment by rbeezer created at 2011-02-24 22:36:39

Patch corrects the naming problem, and creates upgraded ``solve_left`` and ``solve_right``.

This required just a few touch-ups where the name had been wrong, or the improved accuracy changed results.


---

Comment by rbeezer created at 2011-02-24 22:36:39

Changing status from new to needs_review.


---

Comment by jhpalmieri created at 2011-03-21 19:16:14

Without the patch, "solve_right" seems to work for nonsquare matrices over RDF, I guess because it's using the generic "solve_right" method from matrix2.pyx.  With the patch, it looks like this won't work any more; is that right?  Is there a good reason for not allowing square matrices?  We could instead add a method `_solve_right_nonsingular_square` to matrix_double_dense.pyx, and then I think this should be called by the generic solve_right method.

For "solve_left", could we just remove the version from matrix_double_dense.pyx altogether, and just use the generic version?


---

Comment by rbeezer created at 2011-03-21 21:04:30

Replying to [comment:4 jhpalmieri]:

Yes, there is some tension in handling inexact matrices with routines designed for exact matrices (which is the root issue here, I believe).  `NumPy/SciPy` just does not do certain things, such as computing a rank.

I'm hoping to get some guidance from the `NumPy` folks here at Sage Days 29 right now and we can chat some more.


---

Comment by mraum created at 2011-03-25 03:47:19

Changing status from needs_review to needs_work.


---

Comment by mraum created at 2011-03-25 03:47:19

1) You can use svd to first get a square matrix that you can use to solve the system of linear equations.
2) Why do you copy the code for left and right solve. There is a generic fallback in matrix2.pyx. If you want to replace the docstring for this class, can't you do just that?


---

Comment by rbeezer created at 2011-03-25 17:50:52

We could use a direct call to `SciPy` solve for square nonsingular and analyze/exploit the SVD for nonsingular/rectangular.


---

Comment by rbeezer created at 2011-07-18 04:48:09

Changing status from needs_work to needs_review.


---

Comment by rbeezer created at 2011-07-18 04:48:09

Finally getting back to this one.

1.  solve_left and solve_right are confused at the moment - I think this is important to fix.

2.  The code is different, in part because the error messages are explicit, naming rows and columns when sizes do not match.

3.  The longer I think about it, the more I think we should _never_ be feeding floating-point matrices into exact routines.  We should expose the ScyPy/NumPy/LAPACK routines as much as possible and not pretend the exact routines are going to give reasonable answers as a "fallback."

4.  I'm happy to try to get solutions to systems with non-square coefficient matrices with floating-point entries, but despite a lot of thought and reading, I'm not convinced of the right approach.  In any event, I'd like to fix the problem at hand, and do the non-square somewhere else.

5.  I am going to set this to "needs review" but I'm happy to entertain more discussion - I'll just need convincing.

Rob


---

Comment by mraum created at 2011-08-04 10:28:25

What I was talking about when I mentioned the fallback is a piece of generic code for solve_left that calls solve_right. Thus you only need to implement one version. And you should, because code duplication makes mistakes more likely and maintenance harder. I will change this when reviewing this, and then will wait for your approval.


---

Comment by mraum created at 2011-08-05 16:53:37

Changing status from needs_review to positive_review.


---

Comment by mraum created at 2011-08-05 16:53:37

I didn't touch the implementation of solve_right.  I changed my mind for the following simple reason. While the code is quite short and easy to check the documentation is very different (left replaced by right). So it seems quite impractical to duplicate it.

We should think about modifying the documentation so that it gets included in the reference manual. Also there is a pseudoregression in the code. Sage doesn't pretend it could solve equations with double dense matrices as right hand side. Scipy covers also this case, so we should open a new ticket for this.


---

Comment by leif created at 2011-09-08 16:32:44

Changing priority from major to blocker.


---

Comment by leif created at 2011-09-13 12:15:21

Resolution: fixed


---

Attachment

Reviewer patch. Apply on top of main patch, which causes a signed zero on Itanium 2.


---

Attachment

Reviewer patch. Apply on top of main patch, which causes doctests to fail on a couple of systems due to noisy zero terms.


---

Comment by leif created at 2011-09-26 01:32:45

Attached two reviewer patches fixing doctest errors on some systems.

Third patch to fix doctest errors in `sage/matrix/matrix_double_dense.pyx` coming soon.

The patch to the preparser examples requires #11848.


---

Comment by leif created at 2011-09-26 02:41:31

Reviewer patch. Apply on top of main patch, which causes another doctest to fail on a couple of systems due to a noisy zero in a vector result.


---

Attachment

Third reviewer patch (fixing a doctest error in `matrix_double_dense.pyx`) is up.


---

Comment by rbeezer created at 2011-09-26 03:59:04

The three reviewer patches apply, build and pass their tests once #11848 is applied to a recent alpha3 prerelease that already has the main patch.  Currently passes all tests in `sage/matrix` but will run full tests overnight.

This has a positive review from me based on the reviewer contributions, but is marked as closed right now anyway.  I'll only retreat if something unexpected happens overnight.

Leif - thank-you very much for getting these noisy tests cleaned up.

Rob


---

Comment by leif created at 2011-09-27 21:46:38

Reviewer patch. Slightly adjust threshold for noisy zero terms in polynomials, needed on MacOS X 10.6 x86_64 with GCC 4.2.1. Apply on top of other patches (i.e., the other reviewer patch to `polynomial_element.pyx`).


---

Attachment

I've attached yet another patch slightly increasing one epsilon, since one doctest still failed on MacOS X 10.6 (due to almost zero terms in a polynomial).


---

Comment by rbeezer created at 2011-09-28 14:44:59

Yes, I meant to bring this up in the flurry of noisy doctest fixes.  I have taken to not cutting it too fine on the zeros.  For example, if I get a "zero" on the order of `10^-16`, then I have taken to clipping zeros at `10^-14`.  There seems to be too much variability across systems, so if you cut it too close, then some system is eventually going to complain, it seems.

The latest patch looks good and applies and builds find, passing all tests in `sage/ring/polynomial` on the alpha3-prerelease I picked up about 10 days ago.  So ready to go, again.


---

Comment by leif created at 2011-10-07 17:16:28

Follow-up ticket further increasing the threshold for noisy zero terms in polynomials (from 2.5e-15, needed for `bsd.math`, to 2.7e-15) for MacOS X 10.4 PPC once more: #11901
