# Issue 15: sin(integer) precision issue

Issue created by migration from Trac.

Original creator: was

Original creation time: 2006-09-12 23:15:45

Assignee: somebody

I don't like how SAGE works for this (see below) (example from Fateman's mathematica review):
   {{{
     sage: sin(3141592653589793238.0)   # very good
     -0.4463151633593201122015 
     sage: float(sin(3141592653589793238))   # very bad
     -0.64165348191050475
   }}}
   The problem is that SAGE is using the Python math library, which is the C library, which has
   precision issues.   The fix is to change sin(integer) to use mpfr.



---

Comment by was created at 2006-10-15 17:40:30

I don't want to change this.  Keeping it as it is stays very clean; changing it introduces all kinds of subtle issues that could be even more confusing in the long run.


---

Comment by was created at 2006-10-15 17:40:30

Resolution: fixed
