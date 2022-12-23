# Issue 6524: Ratio of two symbolic expressions involving derivative does not simplify

Issue created by migration from https://trac.sagemath.org/ticket/6524

Original creator: gmhossain

Original creation time: 2009-07-13 12:18:10

In new symbolics, ratio of two symbolic expressions involving derivative does not simplify


```
sage: f(x) = function('f', x)
sage: g = f(x).diff(x)
sage: h = f(x).diff(x)*sin(x)
sage: h/g
sin(x)*D[0](f)(x)/D[0](f)(x)
```



However, for some ordering it does simplify


```
sage: f(x) = function('f', x)
sage: g = f(x).diff(x)
sage: h = sin(x)*f(x).diff(x)
sage: h/g
sin(x)
```





---

Attachment


---

Comment by burcin created at 2009-09-19 15:17:03

Changing status from new to assigned.


---

Comment by burcin created at 2009-09-19 15:17:03

This is fixed in my pynac tree, attachment:trac_6524-fderivative_compare.patch contains doctests for Sage.

I will post a new pynac package and review instructions soon.


---

Comment by burcin created at 2009-09-19 15:17:03

Set assignee to burcin.


---

Comment by burcin created at 2009-09-22 19:29:27

New pynac package available at #6993.


---

Comment by kcrisman created at 2009-09-23 02:33:18

Looks like it's fixed.  Pending of course positive review of the Pynac package as a whole.


---

Comment by mvngu created at 2009-09-25 22:46:38

Resolution: fixed


---

Comment by mvngu created at 2009-09-27 10:41:41

There is no 4.1.2.alpha3. Sage 4.1.2.alpha3 was William Stein's release for working on making the notebook a standalone package.
