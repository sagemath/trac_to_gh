# Issue 2753: [with patch, needs review] new "randstate" framework for a global Sage random number seed

Issue created by migration from https://trac.sagemath.org/ticket/2753

Original creator: cwitty

Original creation time: 2008-04-01 14:28:37

Assignee: somebody

The attached patch keeps track of the random number seed used on Sage startup, and lets you set a single random number seed, which gets propagated on demand into random number generators for GMP (+ MPFR), Python, NTL, Pari, gp, GAP, and libc (so far).

Also, it moves away from libc's random() in favor of the other generators mentioned above, which are portable across operating systems and architectures; this means that doctest results using random numbers are now reproducible, so I've removed many "# random" from the doctests.

Passes testall on the platforms I have access to (32-bit x86 Linux, 64-bit x86 Linux, and 32-bit x86 OSX).


---

Attachment


---

Attachment

Applies cleanly to Sage 2.11. I am taking cwitty's word on doctests- I haven't run any of my own. IMO, this greatly improves the robustness of our doctesting infrastructure.


---

Comment by rlm created at 2008-04-04 02:27:38

Patch should be rebased on 3.0.alpha0.


---

Comment by mabshoff created at 2008-04-04 05:04:46

manula merges of the rejected hunks against my 3.0.alpha1 merge tree


---

Attachment

Merged all three patches in Sage 3.0.alpha1


---

Comment by mabshoff created at 2008-04-04 05:05:09

Resolution: fixed
