# Issue 5496: fix bugs in is_prime  (EASY)

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-03-12 02:55:11

Assignee: was

This is not good:

```
sage: is_prime(GF(5)(3))
True
sage: is_prime(GF(5)(4))
False
```


The fix is to totally 100% rewrite is_prime in arith.py so that it first calls x.is_prime() and if that isn't defined, then in some special cases (e.g., python ints) converts to Integer and calls is_prime.  Otherwise, it raises a NotImplementedError. 


---

Comment by kevin.stueve created at 2010-01-17 21:08:40

Right now finite fields don't seem to have an is_prime function, so I believe that currently, is_prime(GF(5)(3)) should raise NotImplementedError.  I'm going to try to fix is_prime so that it raises NotImplementedError for is_prime(GF(5)(3)).


Kevin Stueve


---

Comment by kevin.stueve created at 2010-01-17 21:49:56

Changing status from new to needs_review.


---

Attachment

changed delegation of is_prime calculation to n.is_prime()


---

Attachment


---

Comment by kevin.stueve created at 2010-01-17 23:22:22

Apply only 5496.2.patch.


---

Comment by spancratz created at 2010-01-18 01:03:21

Three small changes throughout the Sage library


---

Attachment

Second addendum, for symbolic expressions


---

Comment by spancratz created at 2010-01-18 04:53:31

Applying Kevin's second patch ``5496.2.patch`` and the two small changes I added, this now passes all doctests done with ``sage -t devel/sage/sage``, and can get a positive review.


---

Comment by spancratz created at 2010-01-18 04:53:31

Changing status from needs_review to positive_review.


---

Comment by was created at 2010-01-18 05:36:46


```
if type(n) == int or type(n)==long: 
```

should be

```
if isinstance(n, (int, long)):
```



---

Comment by was created at 2010-01-18 05:36:46

Changing status from positive_review to needs_work.


---

Comment by was created at 2010-01-18 05:37:16

Also, use `obj.pyobject()` in some cases for symbolics...


---

Comment by spancratz created at 2010-01-18 05:38:22

Third addendum, for one character change for lucas numbers


---

Attachment

I've now incorporated the handling of symbolic expressions as suggested by Burcin.  The sequence of patches should be applied in the order

- 5496.2.patch
- trac5496_rationals_to_int.patch
- trac5496_symbolic_expressions.patch
- trac5496_lucas.patch
- trac5496_symbolic_expressions2.patch

I am running doctests now, but if they pass this should get positive review again.


---

Comment by spancratz created at 2010-01-18 06:01:59

Changing status from needs_work to needs_review.


---

Attachment

Fourth addendum, for symbolic expressions


---

Comment by spancratz created at 2010-01-18 06:24:04

Changing status from needs_review to positive_review.


---

Comment by spancratz created at 2010-01-18 06:24:04

This is to confirm that all doctests have been passed, checked with "./sage -t devel/sage/sage".


---

Comment by rlm created at 2010-01-19 01:15:00

Resolution: fixed
