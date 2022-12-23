# Issue 6080: Add utility methods to Integer (needed for mpmath)

Issue created by migration from https://trac.sagemath.org/ticket/6080

Original creator: fredrik.johansson

Original creation time: 2009-05-19 03:35:31

Assignee: somebody

Patch adds sqrtrem (I only found an existing isqrt) and a method to count trailing zero bits, both of which are needed to make mpmath on top of sage.Integer reasonably fast.

The value of (0).trailing_zero_bits() (as well as the name of the method) could be adjusted.


---

Attachment


---

Comment by mhansen created at 2009-05-19 04:33:38

Looks good to me.


---

Comment by mabshoff created at 2009-05-19 20:37:01

Resolution: fixed


---

Comment by mabshoff created at 2009-05-19 20:37:01

Merged in Sage 4.0.rc0.

Cheers,

Michael
