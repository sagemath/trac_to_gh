# Issue 8506: Inefficient hash for homsets

Issue created by migration from https://trac.sagemath.org/ticket/8506

Original creator: robertwb

Original creation time: 2010-03-12 01:39:09

Assignee: cremona

This ends up affecting, in particular, hashing of elliptic curves and their point sets. 


---

Comment by robertwb created at 2010-03-12 01:41:30

As I side effect, I changed __ainvs to be stored as a tuple, rather than being converted at each request.


---

Comment by robertwb created at 2010-03-12 02:36:46

Changing status from new to needs_review.


---

Attachment


---

Comment by hivert created at 2010-03-12 08:34:45

Replying to [comment:2 robertwb]:

Hi robert, 

The problem is not only for homset ! See #8119

```
sage: h = Hom(ZZ, QQ)
sage: hash(h)
-8106914618552251573
sage: h.rename("toto")
sage: hash(h)
2314052222105390764
```

I don't know exactly what would be a generic solution of this problem. There is one if the parent inherits from `UniqueRepresentation` (see ##8120) instead of using one of the at least three other mechanisms I've seen troughout sage library. Not that as I said in that ticket, I'm not sure how robust my solution is I've a proposal for a better option. If you have any comment, please do not hesitate.

Cheers,

Florent


---

Comment by robertwb created at 2010-03-12 09:21:32

My original concern was that hashing the parents I was using was way to expensive. In particular, it was using the Parent as a key in the coercion model, and the dict lookup was many times more expensive than the actual arithmetic (or anything else I was doing in that function...) `UniqueRepresentation` is special, as one doesn't have to worry about hashes being unequal for equal objects.


---

Comment by cremona created at 2010-03-13 15:02:27

I am not competent to comment on the hashing issues.  But I applied the patch to 4.3.4.alpha1 and had the following test failures (I only tested sage/schemes/elliptic_curves, and without -long):

```
sage -t  sage/schemes/elliptic_curves/heegner.py
**********************************************************************
File "/storage/jec/sage-4.3.4.alpha1/devel/sage-8505/sage/schemes/elliptic_curves/heegner.py", line 2588:
    sage: hash(y)
Expected:
    -5236815264926108755       
Got:
    -756867903203770682
**********************************************************************
File "/storage/jec/sage-4.3.4.alpha1/devel/sage-8505/sage/schemes/elliptic_curves/heegner.py", line 2893:
    sage: hash(EllipticCurve('389a').heegner_point(-7,5))
Expected:
    -5236815264926108755             
Got:
    -756867903203770682
**********************************************************************
2 items had failures:
   1 of   4 in __main__.example_107
   1 of   3 in __main__.example_121
***Test Failed*** 2 failures.
For whitespace errors, see the file /home/jec/.sage//tmp/.doctest_heegner.py
	 [83.6 s]
```



---

Comment by cremona created at 2010-03-13 15:02:27

Changing status from needs_review to needs_work.


---

Comment by robertwb created at 2010-03-13 19:32:11

Looks like this is once again a case where the alpha differs enough from the latest release to cause issues. The changes above look innocuous enough, I'll make a new patch.


---

Attachment


---

Comment by robertwb created at 2010-03-15 19:50:12

OK, I ran all tests against the latest alpha, and those two were the only failures I got as well. I've posted a new patch fixing them. As for the hashing issues, I just changed the hash to not rely on the string representation (e.g. hashing an elliptic curve now hashes the basering and a-invariants).


---

Comment by robertwb created at 2010-03-15 19:50:12

Changing status from needs_work to needs_review.


---

Comment by cremona created at 2010-04-02 16:41:22

New patch applies to 4.3.5 OK.  Now testing on both 32- and 64-bit...


---

Comment by cremona created at 2010-04-02 19:28:36

Replying to [comment:8 cremona]:
> New patch applies to 4.3.5 OK.  Now testing on both 32- and 64-bit...

All tests pass on both -- positive review!


---

Comment by cremona created at 2010-04-02 19:28:36

Changing status from needs_review to positive_review.


---

Comment by jhpalmieri created at 2010-04-16 18:45:26

Resolution: fixed


---

Comment by jhpalmieri created at 2010-04-16 18:45:26

Merged "8506-homset-hashing-take2.patch" in 4.4.alpha0.
