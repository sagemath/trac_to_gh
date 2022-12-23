# Issue 946: hang when doctesting calculus.py on some systems

Issue created by migration from https://trac.sagemath.org/ticket/946

Original creator: was

Original creation time: 2007-10-20 17:23:23

Assignee: was

Remove the lines with # not tested -- trac #number
in them from calculus.py to replicate this problem on sage.math. 
It might be a weird hanging issue with maxima.


---

Comment by mabshoff created at 2007-10-29 05:48:37

This needs some investigation, so if it doesn't make it this should be BD5 material.

Cheers,

Michael


---

Attachment


---

Comment by was created at 2007-11-18 04:06:25

GOOD -- if when applied the tests still work then by definition this patch is good.


---

Comment by was created at 2007-11-27 06:25:12

Resolution: fixed
