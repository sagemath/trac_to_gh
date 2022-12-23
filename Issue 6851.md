# Issue 6851: hashes for derivatives of symbolic functions still collide

Issue created by migration from https://trac.sagemath.org/ticket/6851

Original creator: burcin

Original creation time: 2009-08-31 12:02:12

Assignee: burcin

It seems that #6243 didn't fix things properly:


```
Thanks to those who worked on closing ticket 6243 regarding
derivatives as dictionary keys for the release of Sage 4.1.1.  It
appears that there's still a bug, though (see below).

Alex

----------------------------------------------------------------------
----------------------------------------------------------------------
sage: f= function('f',x)
sage: d= {}
sage: for i in [1..5]:
....:     print diff(f,x,i)
....:     d[diff(f,x,i)] = i
....:
D[0](f)(x)
D[0, 0](f)(x)
<boom>
```



---

Attachment

I hope I have the right fix in pynac this time. attachment:trac_6851-fderivative_hash_collision.patch contains doctests for Sage.

I will post a new pynac package and review instructions soon.


---

Comment by burcin created at 2009-09-19 15:14:23

Changing status from new to assigned.


---

Comment by burcin created at 2009-09-22 19:28:50

New pynac package available at #6993.


---

Comment by kcrisman created at 2009-09-23 19:32:04

This works fine.  Positive review, pending of course review of the package.


---

Comment by mvngu created at 2009-09-25 22:45:59

Resolution: fixed


---

Comment by mvngu created at 2009-09-27 10:40:46

There is no 4.1.2.alpha3. Sage 4.1.2.alpha3 was William Stein's release for working on making the notebook a standalone package.
