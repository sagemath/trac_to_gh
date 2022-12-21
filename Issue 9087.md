# Issue 9087: implement supersingular/ordinary testing for elliptic curves over finite fields

Issue created by migration from Trac.

Original creator: cremona

Original creation time: 2010-05-29 19:30:54

Assignee: cremona

CC:  kohel alexghitza

Keywords: super singular ordinary elliptic curves

I have implemented methods is_ordinary() and is_supersingular() for elliptic curves over finite fields, together with functions supersingular_j_polynomial(p) returning a polynomial over GF(p) whose roots are the supersingular j-invariants in characteristic p, a dict storing the precomputed output of this for p<300, and a function is_j_supersingular(j) testing whether a finite field element j is a supersingular j-invariant.

A patch will be ready shortly.


---

Comment by cremona created at 2010-05-30 11:26:23

Apply after #9052 patches, to 4.4.3.alpha0


---

Comment by cremona created at 2010-05-30 11:29:44

Changing status from new to needs_review.


---

Attachment

Note that this implementation is independent of the related patch #9052 which implements Hasse invariants.  It is also independent of related functions in modular/ssmod.  I am CC'ing David Kohel sine he wrote similar functions for Magma (I believe;  of course the code here has been written completely independently of that!)


---

Comment by wuthrich created at 2010-06-15 12:32:54

I have run the tests on it. They all passed (apart from an unrelated problem) so I am willing to give a positive review.

I had a look at the code and I am confident that it computes what it claims, although I have not checked every little detail (such as the list of polynomials).


---

Comment by wuthrich created at 2010-06-15 12:32:54

Changing status from needs_review to positive_review.


---

Comment by cremona created at 2010-06-15 12:51:33

Thanks.  As part of my testing, I (a) compared the polynomials individually with the ones printed in Antwerp IV, and (b) for all p in the precomputed range and for every j mod p, I constructed an elliptic curve with that j and counted its points and made sure that the supersingular j were exactly the ones which this function said were supersingular!


---

Comment by wuthrich created at 2010-06-15 13:00:43

... and I totally agree that this should be enough !
Thanks John.


---

Attachment

Version without tabs - apply only this patch


---

Comment by davidloeffler created at 2010-06-30 17:29:50

The patch `trac_9087-supersingular.patch` uses tabs for indentation, which is against sage coding conventions. I have uploaded a version with spaces instead of tabs.


---

Comment by cremona created at 2010-06-30 17:36:47

Very sorry, I was sure that I had fixed up my .emacs on all machines I ever use so this would never happen.  But obviously not...


---

Comment by mpatel created at 2010-07-20 07:13:05

Resolution: fixed
