# Issue 9914: fixes for NZMATH/Sage interoperation

Issue created by migration from https://trac.sagemath.org/ticket/9915

Original creator: cwitty

Original creation time: 2010-09-16 08:48:13

Assignee: AlexGhitza

Keywords: NZMATH

NZMATH uses a subtype of Python's "long" for its bignum type.  This works fine with plain mpmath, but when mpmath runs under Sage it uses Cython code that's incompatible with NZMATH.  This patch fixes mpmath-under-sage to fix some incompatibilities with NZMATH.  (It also modifies ZZ to allow initialization from a subclass of int/long/float.)



---

Attachment


---

Comment by cwitty created at 2010-09-16 08:52:05

Changing status from new to needs_review.


---

Comment by leif created at 2010-09-16 11:32:29

Any additional (`--[only-]optional[=...]`) tests to run with NZMATH installed?


---

Comment by leif created at 2010-09-16 13:02:47

Patch looks reasonable, and doesn't cause additional doctest failures when running `ptestlong` on (not yet released) Sage 4.6.alpha1 (with NZMATH 1.0.0 installed; Ubuntu 10.04 x86_64).

Positive review so far, still looking for optional NZMATH doctests... ;-)


---

Comment by leif created at 2010-09-16 13:02:47

Changing status from needs_review to positive_review.


---

Comment by leif created at 2010-09-16 13:54:04

Replying to [comment:3 leif]:
> ... still looking for optional NZMATH doctests... ;-)

Couldn't find any; also, NZMATH doesn't have an `spkg-check` file.


---

Comment by leif created at 2010-09-16 14:30:05

Is

```
sage: from nzmath import *
```

supposed to work? (Gives deprecation warnings and an attribute error.)

But the following works:

```
sage: import nzmath.rational
sage: r = nzmath.rational.Rational(113r, 355r)
sage: print r
113/355
sage: 
```

That's of course not much of a test. ;-)


---

Comment by mpatel created at 2010-09-29 10:48:06

Resolution: fixed
