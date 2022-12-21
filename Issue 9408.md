# Issue 9408: relativize in number fields is broken

Issue created by migration from Trac.

Original creator: lftabera

Original creation time: 2010-07-02 16:04:23

Assignee: davidloeffler

Keywords: relativize

Does not work due to (maybe) denominators


```
sage: K.<a> = NumberField(x^4-4*x^3+12*x^2-16*x+8)
sage: L.<u,v> = K.relativize(3*a**3 - 9*a**2 + 24*a -16)
sage:#This seems OK
sage: L2.<u2,v2> = K.relativize((3/4)*a**3 - (9/4)*a**2 + 6*a -4)
```

PariError:  (8)

Simpler example


```
sage: L.<a,b> = QQ[i].relativize(1) #Ok
sage: L.<a,b> = QQ[i].relativize(1/2) #PariError
```



---

Comment by lftabera created at 2010-07-06 10:58:40

This ticket should be closed as duplicate of #252


---

Comment by lftabera created at 2010-07-06 10:58:40

Changing status from new to needs_info.


---

Comment by lftabera created at 2011-06-07 08:58:18

Changing status from needs_info to needs_review.


---

Comment by jdemeyer created at 2011-10-15 12:50:47

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2011-11-15 09:21:27

Resolution: duplicate
