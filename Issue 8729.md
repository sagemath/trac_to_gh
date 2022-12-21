# Issue 8729: simple integral using trig functions gives wrong answer

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2010-04-20 16:52:51

Assignee: burcin

CC:  kcrisman

See http://groups.google.com/group/sage-devel/browse_frm/thread/f82e24efdfe23b07/d9e563f086b1136d for a solution


```
sage: a=sqrt((sin(t))^2 + (cos(t))^2)
sage: integrate(a, t, 0, 2*pi) # WRONG!
pi
sage: a.simplify_full().simplify_trig()
1
sage: integrate(a.simplify_full().simplify_trig(), t, 0, 2*pi)
2*pi 
```



---

Comment by jason created at 2010-04-20 17:36:24

It looks like this is fixed in maxima 5.21.0, so maybe we should just upgrade.


---

Comment by jason created at 2010-05-13 04:33:41

This is fixed in the maxima upgrade at #8731


---

Comment by rlm created at 2010-06-25 11:23:32

Resolution: duplicate


---

Comment by kcrisman created at 2010-06-25 13:10:10

Note put on #8731 to check this with a doctest when that ticket is done.
