# Issue 7450: implement is_prime() for ideals

Issue created by migration from https://trac.sagemath.org/ticket/7450

Original creator: AlexGhitza

Original creation time: 2009-11-13 12:30:17

Assignee: malb

Keywords: prime ideal

The attached patch implements a generic primality testing method for ideals.  It is based on the computation of the associated primes of an ideal, and so at the moment will only work for ideals that have this implemented (e.g. ideals in multivariate polynomial rings that Singular can handle).

There are also a few related methods such as `is_primary()` and `embedded_primes()`.



---

Comment by malb created at 2009-11-13 13:23:53

Changing status from new to needs_work.


---

Comment by malb created at 2009-11-13 13:23:53

* patch applies cleanly against 4.2
 * doctests pass
 * reference manual builds without reporting any issues
 * note that there are macros for citations available in ReST: http://sphinx.pocoo.org/rest.html#citations

Other than the last nitpick the patch looks fine.


---

Comment by AlexGhitza created at 2009-11-13 22:14:42

Changing status from needs_work to needs_review.


---

Comment by AlexGhitza created at 2009-11-13 22:14:42

Aha!  Thanks for the pointer for citations.  I had looked in the developer guide and there was nothing about this (I'll open a new ticket to fix that).

I have replaced the patch with one that has the proper citation markup.  Having had a look at the html output, I also fixed the markup for `apply_morphism`.


---

Attachment

And I replaced it once more, having added an optional argument to `is_primary` to check whether an ideal is primary wrt a given prime ideal; also added more doctests borrowed from the Macaulay2 docs.


---

Comment by malb created at 2009-11-16 13:31:13

Changing status from needs_review to positive_review.


---

Comment by malb created at 2009-11-16 13:31:13

Looks good.


---

Comment by mhansen created at 2009-11-17 05:59:06

Resolution: fixed
