# Issue 9335: linear independence of points on an elliptic curve

Issue created by migration from https://trac.sagemath.org/ticket/9335

Original creator: jen

Original creation time: 2010-06-25 07:11:16

Assignee: was

CC:  cremona

During Sage Days 21 (while porting David Roberts' and John Cremona's  implementation of 2-descent for elliptic curves over function fields), we came across the Magma function IsLinearlyIndependent, which does not appear to have an analogue in Sage. 

What it does is the following: given a list of points on an elliptic curve, it returns true iff the points are linearly independent; else it returns false and a vector of coefficients specifying a linear combination of the points that results in torsion.

We would like to have a function that does this in Sage.


---

Comment by cremona created at 2010-06-25 07:42:25

+1!

Such a function exists somewhere in eclib.  I'm not suggesting that it should be wrapped, but could be used as a model.  Something I would be happy to do!


---

Comment by davidloeffler created at 2013-07-25 17:29:39

Changing assignee from was to cremona.


---

Comment by davidloeffler created at 2013-07-25 17:29:39

Changing component from number theory to elliptic curves.
