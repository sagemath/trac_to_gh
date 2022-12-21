# Issue 13: p-adic integers class

Issue created by migration from Trac.

Original creator: was

Original creation time: 2006-09-12 21:33:20

Assignee: somebody

from David Harvey: 
I'm kind of on the run, but I just remembered it would be good to have a pAdicInteger class. Just like we have PowerSeries vs LaurentSeries, and Integer vs Rational, it would be good to have pAdicInteger and pAdicField. Basically the idea is that it doesn't have to keep track of ordp, which currently slows down certain operations a lot (like when I convert an integer to a padic, it has to compute ordp). Essentially it would be like Integers(p^n) but with a floating precision. A very natural application would be the padic sigma stuff I'm working on now.
 
I can't implement it and send you a patch due to time constraints, but perhaps if you like the idea you can add it to the roadmap.


---

Comment by was created at 2006-09-12 21:33:30

Changing type from defect to enhancement.


---

Comment by roed created at 2007-05-20 04:08:50

Included in the new p-adics.


---

Comment by roed created at 2007-05-20 04:08:50

Resolution: fixed
