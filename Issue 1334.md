# Issue 1334: Constant polynomial can't be converted to rational

Issue created by migration from https://trac.sagemath.org/ticket/1334

Original creator: robertwb

Original creation time: 2007-11-29 09:31:42

Assignee: somebody


```
sage: R.<x> = QQ['x']
sage: QQ(R(1/2))
Traceback (most recent call last):
...
TypeError: Unable to coerce 1/2 (<type 'sage.rings.polynomial.polynomial_element.Polynomial_generic_dense'>) to Rational
```



---

Comment by dmharvey created at 2007-12-01 17:20:43

Changing status from new to assigned.


---

Comment by dmharvey created at 2007-12-01 17:20:43

Changing assignee from somebody to dmharvey.


---

Comment by dmharvey created at 2007-12-01 17:45:59

Fixed it:


```
sage: R.<x> = QQ['x']
sage: QQ(R(1/2))
1/2
```


More generally this patch allows coercion of any polynomial to QQ, as long as it's a constant polynomial whose constant term can be coerced into QQ.


---

Attachment


---

Comment by cwitty created at 2007-12-01 18:03:33

Looks good to me.  (doctests pass, code looks good)


---

Comment by mabshoff created at 2007-12-01 18:08:34

Resolution: fixed


---

Comment by mabshoff created at 2007-12-01 18:08:34

Merged in 2.8.15.alpha1.
