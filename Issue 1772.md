# Issue 1772: bug somewhere in the symbolics

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-01-14 05:58:16

Assignee: was

This is from Hector:


```
I also hit this bug while doing this (taken from the "piecewise"
documentation):

sage: f1 = lambda x:-1
sage: f2 = lambda x:2
sage: f = Piecewise([[(0,pi/2),f1],[(pi/2,pi),f2]])
sage: P = f.plot_fourier_series_partial_sum(15,pi,-5,5)   # long time
boom
...

/Users/was/s/local/lib/python2.5/site-packages/sage/calculus/calculus.py in <lambda>(i)
   3607             # We need to do this maximum to correctly handle the case where
   3608             # self is something like (sin+1)
-> 3609             n = max( max(map(lambda i: i.number_of_arguments(), self._operands)+[0]), len(variables) )
   3610         self.__number_of_args = n
   3611         return n

<type 'exceptions.AttributeError'>: 'Pi' object has no attribute 'number_of_arguments'
```





---

Comment by mhansen created at 2008-01-15 01:46:45

Changing status from new to assigned.


---

Comment by mhansen created at 2008-01-15 01:46:45

Changing assignee from was to mhansen.


---

Attachment


---

Comment by was created at 2008-01-18 21:07:53

I also fixed this in the same way earlier today (as part of one my other patches), but my patch was just a few lines to actually fix the listed problem.  The patch attached to this ticket, fixes the problem and does a HUGE amount more to vastly improve doctesting in some files, etc.  I.e., this is _great_. 

I have not fully reviewed the patch yet, though I've looked it over by eye and it looks very good.


---

Attachment

Fixes the one doctest failure in constant.py


---

Comment by mabshoff created at 2008-01-20 01:50:05

Resolution: fixed


---

Comment by mabshoff created at 2008-01-20 01:50:05

Merged in Sage 2.10.1.alpha0
