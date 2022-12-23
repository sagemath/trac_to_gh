# Issue 7150: Wrong substitution implementation for fraction fields

Issue created by migration from https://trac.sagemath.org/ticket/7150

Original creator: novoselt

Original creation time: 2009-10-08 04:40:11

CC:  was

I am getting this in 4.1.1 and find it really frustrating (especially since it took me several hours to catch):



```
sage: QQ["x", "y"].inject_variables()
Defining x, y
sage: e1 = x^2*y^3 - x^2*y - x*y
sage: e2 = e1.parent().fraction_field()(e1)
sage: print e2
x^2*y^3 - x^2*y - x*y
sage: print e2.subs(y=SR("s"))
x^2*s^3 - (x^2 - x)*s
```

The last line is wrong!


---

Comment by fwclarke created at 2009-10-08 07:43:09

But in 4.1.2.rc0:

```
sage: QQ["x", "y"].inject_variables()
Defining x, y
sage: e1 = x^2*y^3 - x^2*y - x*y
sage: e2 = e1.parent().fraction_field()(e1)
sage: print e2
x^2*y^3 - x^2*y - x*y
sage: print e2.subs(y=SR("s"))
s^3*x^2 - s*x^2 - s*x
```

So the problem may already have been solved.


---

Comment by fwclarke created at 2009-10-08 07:43:09

Changing status from new to needs_review.


---

Comment by jason created at 2009-10-14 21:24:42

This may need to be closed with 4.1.2.


---

Comment by mhansen created at 2009-10-16 05:00:29

Resolution: fixed


---

Comment by mhansen created at 2009-10-16 05:00:29

Yep, I think we can close this.
