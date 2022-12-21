# Issue 4475: create a native Sage implementation of Dokchitser's L-functions algorithm

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-11-09 04:26:47

Assignee: was

See http://wiki.sagemath.org/days11/projects for now.


---

Attachment

first very preliminary version


---

Comment by mabshoff created at 2008-11-09 06:55:50

Jen's original code which this work is based on was at #2568. Obviously Jen should get partial credit once the code from this ticket has been merged.

Cheers,

Michael


---

Attachment


---

Attachment


---

Attachment


---

Attachment

I attached a wrapping of the G_s(t) terms, and got it working (at least it computes the Riemann zeta function correctly). There is an off-by-one typo in formula (10) of the paper (the computation of the poles should be `rj k!/(pj - s)^(k+1)`). However, this fix still didn't give the right answer so I examined Dokchister's code and he has an extra summation over the poles (very last function of computel.gp) and I couldn't figure out where that was coming from. 

The weight and the exponential factor are used for calculating the intermediate precision/number of terms needed in the various series related to computing G_s(t), which turns out to be the bulk of the work of `initLdata`, so it made things a lot cleaner to simply call that function for now. 

It should be noted that to compute the value at s it may be necessary to compute the power series at s and then evaluate to let the poles and zeros of the gamma factor cancel out poles/zeros of L* appropriately.


---

Attachment

(Partial) native implementation of the G function.
