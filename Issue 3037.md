# Issue 3037: [with spkg, needs trivial review] cython-0.9.6.13.tip

Issue created by migration from Trac.

Original creator: gfurnish

Original creation time: 2008-04-27 01:12:56

Assignee: gfurnish

This is a new cython spkg with several enhancements:
It has a working -w feature, it is upgraded to tip in cython-devel, has the unicode bug fix, and it has a improved circular cdef import algorithm.  

Download at http://sage.math.washington.edu/home/gfurnish/spkg/cython-0.9.6.13.tip.spkg


---

Comment by mabshoff created at 2008-04-27 01:18:38

The spkg exposes #3035.

Cheers,

Michael


---

Comment by mabshoff created at 2008-04-27 01:22:12

One thing: The name of the spkg is pointless. Use cython-0.9.6.12-20080426 - since tip is alway *now*

Cheers,

Michael


---

Comment by gfurnish created at 2008-04-27 01:23:57

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-04-27 04:46:01

Merged in Sage 3.0.1.alpha1


---

Comment by mabshoff created at 2008-04-27 04:46:01

Resolution: fixed


---

Attachment
