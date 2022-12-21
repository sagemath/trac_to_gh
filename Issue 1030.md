# Issue 1030: [with patch] MPolynomial_libsingular mutates with call to factor

Issue created by migration from Trac.

Original creator: jbmohler

Original creation time: 2007-10-29 16:21:37

Assignee: somebody

Here's an exhibition of the bug:


```
sage: R.<x,w,v,u> = QQ['x','w','v','u']
sage: f=(1-x)*(1-w)*(2-2*v)
sage: f
-2*x*w*v + 2*x*w + 2*x*v + 2*w*v - 2*x - 2*w - 2*v + 2
sage: f.factor()
(-2) * (x - 1) * (w - 1) * (v - 1)
sage: f
x*w*v - x*w - x*v - w*v + x + w + v - 1
```


The fix is attached.


---

Comment by jbmohler created at 2007-10-29 16:21:50

the fix


---

Attachment


---

Comment by mabshoff created at 2007-10-29 20:36:04

Changing priority from critical to blocker.


---

Comment by malb created at 2007-10-31 11:54:08

I can confirm that `singclap_factorize` mutates the parameter. Also, the patch looks good and should be accepted for 2.8.11


---

Comment by mabshoff created at 2007-11-01 10:10:51

Resolution: fixed


---

Comment by mabshoff created at 2007-11-01 10:10:51

applied to 2.8.11.alpha0
