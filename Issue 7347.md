# Issue 7347: numerical_integral(SR(0), 0, 1) gives an error

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2009-10-29 07:12:05

Assignee: jkantor

CC:  jason kcrisman


```
sage: numerical_integral(SR(0), 0, 1)
Traceback (most recent call last):
...
ValueError: Integrand has wrong number of parameters
```



---

Comment by dsm created at 2011-02-19 10:03:27

See #10088, a duplicate, which has a patch attached.


---

Comment by kcrisman created at 2011-08-19 13:58:00

And #10088 was merged quite some time ago. 

```
sage: numerical_integral(SR(0), 0, 1)
(0.0, 0.0)
```

Yup, works.


---

Comment by kcrisman created at 2011-08-19 13:58:06

Changing status from new to needs_review.


---

Comment by kcrisman created at 2011-08-19 13:58:11

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2011-08-22 08:09:43

Resolution: duplicate
