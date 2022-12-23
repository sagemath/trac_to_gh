# Issue 7728: Make matrix factorizations immutable and cached

Issue created by migration from https://trac.sagemath.org/ticket/7728

Original creator: dagss

Original creation time: 2009-12-17 21:22:36

Assignee: was

The attached patch (based on 4.3.rc0):

 - changes Cholesky (all/most matrices) and SVD, QR and LU factorizations (double_dense only) so that the returned resulting matrices are immutable
 - adds caching for Cholesky, SVD and QR
 - adds pickle-able caching for LU (and it is likely there was a a bug with pickling/unpickling a matrix with a cached factorization which this patch fixes...)
 - improves doctests for SVD and QR (I wanted to more easily check that my changes didn't cause regressions...)
 - adds methods `zero_at` and `round` to dense double matrices (used in said doctests)

I hope the doctest improvements can be accepted as part of the patch even if I didn't bother to split it up.

Note that when dealing with matrix factorization doctesting, just avoiding 0 in the input goes very far with creating readable tests.



---

Attachment


---

Comment by dagss created at 2009-12-17 21:25:27

Changing status from new to needs_review.


---

Comment by dagss created at 2009-12-19 22:45:07

OK, this likely need some more docs about the caching aspect...


---

Comment by dagss created at 2009-12-19 22:45:07

Changing status from needs_review to needs_work.


---

Attachment

Last attachment contains the same changes + a little more docs.

LU was previously cached, so this just makes things more consistent by caching all decompositions -- easier to remember.

I also plan to make use of the caching if I get around to fixing #4932, see my comment there, short story: `solve_left` should be able to use the results of a call to `LU()`, which makes caching a lot more important.


---

Comment by dagss created at 2009-12-21 15:12:06

Changing status from needs_work to needs_review.


---

Comment by was created at 2009-12-21 19:27:24

Changing status from needs_review to positive_review.


---

Comment by was created at 2009-12-21 19:27:24

Bravo, this is an awesome patch!  Positive review.


Comment for future work by somebody.  I don't like this:

```
987	            U, S, V -- immutable matrices such that $A = U*S*V.conj().transpose()$ 
988	                       where U and V are orthogonal and S is zero off of the diagonal. 
```


It's not your fault -- it was like that before.  But it is wrong in so many ways wrt to Sphinx (e.g., dollar signs?  V.conj().transpose() in math mode?  variables should be listed separately, etc.


---

Comment by AlexGhitza created at 2009-12-21 21:26:44

Replying to [comment:4 was]:
> It's not your fault -- it was like that before.  But it is wrong in so many ways wrt to Sphinx (e.g., dollar signs?  V.conj().transpose() in math mode?  variables should be listed separately, etc.

Just a small comment: I believe that we can now use dollar signs for math input in Sphinx, so that shouldn't be a problem.


---

Comment by mhansen created at 2010-01-03 21:28:32

Resolution: fixed
