# Issue 6201: CC() raises exception instead of returning 0

Issue created by migration from Trac.

Original creator: fredrik.johansson

Original creation time: 2009-06-03 21:14:11

Assignee: somebody

This is inconsistent:


```
ZZ(); QQ(); RR(); CC()

0
0
0.000000000000000
Traceback (click to the left for traceback)
...
TypeError: __call__() takes at least 2 arguments (1 given)
```



---

Comment by AlexGhitza created at 2009-06-03 23:09:54

Changing assignee from somebody to AlexGhitza.


---

Comment by AlexGhitza created at 2009-06-03 23:09:54

Changing status from new to assigned.


---

Comment by AlexGhitza created at 2009-06-03 23:09:54

Simple fix up for review.


---

Attachment

Simple change to the code, includes a doctest, passes all tests, reference manual builds.  Positive review.

Now should we do the same thing with GF(2)(), CDF(), etc.?


---

Comment by ncalexan created at 2009-06-13 21:19:45

Resolution: fixed
