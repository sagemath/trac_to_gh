# Issue 9287: improving doctest coverage for elliptic curves

Issue created by migration from https://trac.sagemath.org/ticket/9287

Original creator: wuthrich

Original creation time: 2010-06-20 23:40:48

Assignee: cremona

CC:  wstein

Keywords: doctest coverage

The bad files are

* BSD.py 85% (6 of 7)
* ell_egros.py 85% (6 of 7)
* ell_modular_symbols.py 86% (13 of 15)
* gp_cremona.py 85% (6 of 7)
* gp_simon.py 50% (1 of 2)
* mod5family.py 0% (0 of 1)
* monsky_washnitzer.py 26% (28 of 107)
* padic_height.py 0% (0 of 6) #deprecated
* padic_lseries.py 59% (19 of 32)
* padics.py 83% (10 of 12)
* sea.py 0% (0 of 1)
* sha_tate.py 80% (8 of 10)


---

Comment by wuthrich created at 2010-06-20 23:43:17

So far I have dealt with 

 * padic_lseries.py
 * modular_parametrization.py
 * padics.py

... more to come


---

Attachment

exported against 4.4.4.alpha0


---

Comment by wuthrich created at 2010-06-22 17:46:12

also exported against 4.4.4.alpha0


---

Comment by wuthrich created at 2010-06-22 17:52:15

Changing status from new to needs_review.


---

Attachment

The second patch (indep of the first) takes care of

 * ell_modular_symbol
 * sha_tate
 * ell_torsion

See trac ticket #9313 of how to take care of padic_height.py

That is how far I will do improve the documentation so far. If someone else would like to improve it further either put it back to needs_work and continue the work here or (prefered by me) open a new ticket.


---

Comment by cremona created at 2010-06-23 00:29:54

Patches apply fine to 4.4.4.alpha0, and test pass, and docs build and look fine!


---

Comment by cremona created at 2010-06-23 00:29:54

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-07-20 07:08:35

Resolution: fixed
