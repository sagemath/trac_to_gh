# Issue 9193: Proveable computation of L-functions

Issue created by migration from Trac.

Original creator: robertwb

Original creation time: 2010-06-09 05:42:19

Assignee: was

CC:  rishi jen

This is related to #4475.


---

Attachment


---

Attachment


---

Attachment


---

Comment by robertwb created at 2010-06-09 06:15:51

Depends on #9165, #9184, #9180.


---

Comment by was created at 2010-07-08 14:55:06

Why do you write above that this "Depends on #9165"?  There is no code there, and that is related to the Cygwin port?


---

Comment by robertwb created at 2010-07-08 16:05:07

The dependency should have been #9156 (which is a tiny, now merged, ticket) rather than #9165. 

This still needs work in two ways. Firstly, it needs more doctests/documentation (though most of the important/tricky functions are already done), and there is also a bug in computing the tail of the G-function summation that I'm still tracking down. I did some work towards this during Sage Days 22, and even thought about it a touch this week, but haven't quite gotten to the bottom of it. 


```
$ sage -coverage sage/lfunctions/lfunction.py 
----------------------------------------------------------------------
sage/lfunctions/lfunction.py
ERROR: Please add a `TestSuite(s).run()` doctest.
SCORE sage/lfunctions/lfunction.py: 61% (19 of 31)

$ sage -coverage sage/lfunctions/G_function.py 
----------------------------------------------------------------------
sage/lfunctions/G_function.py
ERROR: Please add a `TestSuite(s).run()` doctest.
SCORE sage/lfunctions/G_function.py: 59% (13 of 22)
```



---

Comment by robertwb created at 2010-07-08 16:05:07

Changing status from new to needs_work.


---

Comment by robertwb created at 2011-03-27 05:20:04

This is done except for doctests on some functions (though it could use some optimisations too).


---

Comment by was created at 2011-08-25 06:42:00

(I just rebased this with Robert for sage-4.7.2.alpha2.)


---

Attachment

All patches apply (with a minor rebase) and mostly work.  However, there is one bug. 


```
Unfortunately, this is wrong, since the coefficients of 1 and T have
to be 0.0000?.  However, the output *is* correct to 10 bits of
precision, so the correct fix is just to truncate.::

    sage: L = LFunction(EllipticCurve('389a'))
    sage: L.taylor_series(RealField(10)(1), 3, proof=True)
    -0.00002125? + 0.00001204?*T + 0.75933?*T^2 - 0.43032?*T^3 + O(T^4)
```



---

Comment by was created at 2011-08-25 07:03:13

(slightly updated)


---

Attachment
