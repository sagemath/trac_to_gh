# Issue 9168: cygwin: ratpoints does not work correctly

Issue created by migration from Trac.

Original creator: was

Original creation time: 2010-06-07 04:28:53

Assignee: tbd

CC:  jpflori

Some ratpoints tests fail on cygwin, e.g.:

```

sage -t  "devel/sage/sage/libs/ratpoints.pyx"               
**********************************************************************
File "/home/wstein/sage-4.4.3/devel/sage/sage/libs/ratpoints.pyx", line 57:
    sage: for x,y,z in ratpoints([1..6], 200):
       print -Integer(1)*y**Integer(2) + Integer(1)*z**Integer(6) + Integer(2)*x*z**Integer(5) + Integer(3)*x**Integer(2)*z**Integer(4) + Integer(4)*x**Integer(3)*z**Integer(3) + Integer(5)*x**Integer(4)*z**Integer(2) + Integer(6)*x**Integer(5)*z
Expected:
    0
    0
    0
    0
    0
    0
    0
Got:
    0
    0
    0
```


What happens when the same is done manually:


```

sage: from sage.libs.ratpoints import ratpoints
sage: 
sage: for x,y,z in ratpoints([1..6], 200):
....:     print -1*y^2 + 1*z^6 + 2*x*z^5 + 3*x^2*z^4 + 4*x^3*z^3 + 5*x^4*z^2 + 6*x^5*z
....:     
0
0
0
```


So the problem is simply that less points are found.  Sounds pretty serious...


---

Comment by kcrisman created at 2011-08-02 02:28:48

This files passes tests on a recent build on XP.


---

Comment by kcrisman created at 2011-08-19 14:45:48

But the same thing happens by hand. Why are all these tests passing on Cygwin?


---

Comment by kcrisman created at 2013-01-15 16:16:57

Changing status from new to needs_review.


---

Comment by kcrisman created at 2013-01-15 16:16:57

This now passes, _and_ when I do it by hand I do indeed get seven zeros.  JP, if you can confirm this, then we can close this ticket as no longer valid.


---

Comment by jpflori created at 2013-01-15 17:54:56

Works for me too.


---

Comment by jpflori created at 2013-01-15 17:54:56

Changing keywords from "" to "cygwin".


---

Comment by jpflori created at 2013-01-15 17:54:56

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2013-01-17 10:04:39

Resolution: worksforme
