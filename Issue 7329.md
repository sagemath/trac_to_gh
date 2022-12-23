# Issue 7329: Make integration of vectors work (component-wise)

Issue created by migration from https://trac.sagemath.org/ticket/7329

Original creator: jason

Original creation time: 2009-10-28 02:46:06

Assignee: burcin

CC:  rbeezer kcrisman

It would be great if this worked:


```
            sage: t=var('t')                      
            sage: r=vector([t,t^2,sin(t)])
            sage: integrate(r,t)
            (1/2*t^2, 1/3*t^3, -cos(t))
            sage: integrate(r,(t,0,1))
            (1/2, 1/3, -cos(1) + 1)
```




---

Attachment


---

Comment by jason created at 2009-10-28 04:27:19

Changing status from new to needs_review.


---

Comment by rbeezer created at 2009-10-28 05:05:07

Changing status from needs_review to positive_review.


---

Comment by rbeezer created at 2009-10-28 05:05:07

Looks real good (and useful).

Builds fine, passes tests in sage/modules/module_element.py, behaves as expected, docs look good.

Positive review.


---

Comment by mhansen created at 2009-10-31 16:48:41

Resolution: fixed
