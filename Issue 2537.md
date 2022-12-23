# Issue 2537: a.frac() should return x-x.floor()

Issue created by migration from https://trac.sagemath.org/ticket/2537

Original creator: rishi

Original creation time: 2008-03-16 01:09:45

Assignee: rishi

frac(-2.9) should be .1


---

Attachment


---

Comment by cwitty created at 2008-03-16 01:32:25

Resolution: invalid


---

Comment by cwitty created at 2008-03-16 01:32:25

There is apparently no consensus on the meaning of frac() (see http://mathworld.wolfram.com/FractionalPart.html for some discussion of the issues and the different definitions).  Since Sage's RR is mostly a wrapper for MPFR, I would prefer to stay with the current definition (which also matches my intuition for what "fractional part" should mean); this is also the definition used by the majority of a statistically meaningless sampling from a google search.

If you feel strongly about the issue, I suggest taking it to sage-devel to get a broader sampling of opinions on the question.
