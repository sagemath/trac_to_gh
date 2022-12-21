# Issue 8045: add elliptic integrals to the reference manual

Issue created by migration from Trac.

Original creator: jhpalmieri

Original creation time: 2010-01-23 17:19:12

Assignee: mvngu

The documentation strings for classes like `elliptic_ec` are contained in their `__init__` methods, and so doesn't show up in the reference manual.  This patch fixes that by moving the documentation to the class definition.



---

Attachment


---

Comment by jhpalmieri created at 2010-01-23 17:19:51

Changing status from new to needs_review.


---

Comment by mpatel created at 2010-01-31 01:23:12

Some cleanups.  Replaces previous.


---

Attachment

V2 makes the docstrings more consistent and fixes a mistake (I think) in `elliptic_pi`'s docstring.  For comparison, see [Maxima's documentation](http://maxima.sourceforge.net/docs/manual/en/maxima_17.html#SEC68) and [MathWorld](http://mathworld.wolfram.com/EllipticIntegraloftheThirdKind.html).

Positive review, if my changes are OK.


---

Comment by jhpalmieri created at 2010-01-31 03:09:12

We both missed two typos.  Here's version 3, plus a delta patch to see the (essentially trivial) differences.


---

Comment by jhpalmieri created at 2010-01-31 03:09:12

Changing status from needs_review to positive_review.


---

Attachment

replaces all previous patches


---

Attachment

difference between versions 2 and 3, for reference purposes only. don't merge.


---

Comment by mpatel created at 2010-01-31 03:56:57

Oops.  Thanks for catching the typos.


---

Comment by mvngu created at 2010-02-02 03:23:58

Merged [trac_8045-elliptic-v3.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8045/trac_8045-elliptic-v3.patch).


---

Comment by mvngu created at 2010-02-02 03:23:58

Resolution: fixed
