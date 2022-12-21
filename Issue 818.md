# Issue 818: Convert of prod to Cython

Issue created by migration from Trac.

Original creator: jbmohler

Original creation time: 2007-10-04 01:33:44

Assignee: somebody

I rewrote the prod function in Cython.  Some timings illustrating the improvement:

BEFORE:
sage: l=[1]*15
sage: time for i in xrange(10000): _=prod(l)
CPU times: user 0.18 s, sys: 0.01 s, total: 0.19 s
Wall time: 0.19

AFTER:
sage: l=[1]*15
sage: time for i in xrange(10000): _=prod(l)
CPU times: user 0.06 s, sys: 0.00 s, total: 0.06 s
Wall time: 0.06

Those times make it look pretty good, but most real-world multiplications are very dominated by the actual arithmetic.



---

Attachment

convert to cython bundle


---

Comment by was created at 2007-10-04 18:09:50

Resolution: fixed
