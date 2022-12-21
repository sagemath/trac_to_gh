# Issue 9052: Hasse invariant for elliptic curves

Issue created by migration from Trac.

Original creator: voloch

Original creation time: 2010-05-26 01:41:30

Assignee: cremona

Keywords: Hasse invariant

Creates a method to compute the Hasse invariant of an elliptic curve over a function field of positive characteristic. 


---

Attachment


---

Comment by voloch created at 2010-05-26 01:55:23

Changing status from new to needs_review.


---

Comment by was created at 2010-05-26 02:14:17

Changing status from needs_review to positive_review.


---

Attachment

Looks good to me.


---

Comment by cremona created at 2010-05-26 08:35:56

This is a coincidence, since just yesterday I was considering implementing functions is_supersingular() and is_ordinary().  Now this can be done very simply (since s.s. curves have invariant 0 and ordinary ones have nonzero invariant).

However, I'm a little worried about the efficiency of the current implementation for even modest p, since it involves raising a degree 3 polynomial to the power (p-1)/2 and then picking out one coefficient.   There are easier ways to test supersingularity for small p, since one can precompute the s.s. j-invariants and check that.  This would be a quicker way of computing H when it is 0.  One could check that the j-invariant has degree at most 2 (else ordinary).  And over the prime field GF(p), s.s. curves have cardinality p+1, and another way to check ordinary-ness is to take random points and multiply then by p+1.  As a last resort one can compute the cardinality.

I guess this is enough for a second ticket!


---

Comment by cremona created at 2010-05-27 12:34:09

Apply after both previous patches


---

Attachment

The first two patches apply fine and tests pass.  I added a review patch which beefs up the docstring a little, adds some more examples (including one over a non-prime field), and also added one-liners for characteristics 5 and 7.

Strictly this should be looked at again (William?), but I don't seem to have the option of marking it as "needs review" again.  In case you are wondering about the char. 5,7 cases, as well as doing the math I also systematically checked that this gives the same as the general method for *all* curves over GF(5) and GF(7)!


---

Comment by was created at 2010-05-28 19:25:52

Looks even better to me now, by far!  Thanks John.


---

Comment by was created at 2010-05-28 19:28:08

Resolution: fixed


---

Comment by cremona created at 2010-05-28 19:31:02

Excellent.  I have nearly finished a patch which implements is_supersingular and is_ordinary (independently of computing the Hasse inv.)


---

Comment by cremona created at 2010-05-30 11:30:25

Replying to [comment:7 cremona]:
> Excellent.  I have nearly finished a patch which implements is_supersingular and is_ordinary (independently of computing the Hasse inv.)

See #9087
