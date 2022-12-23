# Issue 2706: [with patch] Fast bitset implimentation

Issue created by migration from https://trac.sagemath.org/ticket/2706

Original creator: robertwb

Original creation time: 2008-03-28 20:00:01

Assignee: rlm

CC:  rlm

Set of functions for manipulating individual bits in lists of longs. This will be especially helpful for the graph isomorphism code as it provides a level of abstraction that should help eliminate bugs. 

It is a pxi file so that the functions can be declared and used inline. 


---

Attachment


---

Attachment


---

Comment by rlm created at 2008-03-28 22:10:44

Looks good, passes tests. Applies cleanly to 2.11.alpha1.


---

Comment by mabshoff created at 2008-03-29 00:02:07

Resolution: fixed


---

Comment by mabshoff created at 2008-03-29 00:02:07

Merged in Sage 2.11.alpha2


---

Attachment

Fixed minor bug, added more doctests. 

All tests pass on 32-bit intel OS X and on sage.math (modulo limbs count)


---

Comment by mabshoff created at 2008-03-29 02:01:38

this patch should fix the limb size doctest issue on 32 vs. 64 bit


---

Attachment

Merged all four patches in Sage 2.11.alpha2
