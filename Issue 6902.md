# Issue 6902: log(x) is typeset as \ln x

Issue created by migration from Trac.

Original creator: burcin

Original creation time: 2009-09-07 19:05:26


```
sage: log(x)
log(x)
sage: latex(log(x))
\ln\left(x\right)
```


We should switch back to `\log`. See this thread:

http://groups.google.com/group/sage-devel/browse_thread/thread/dc6530a2071bd6db


---

Comment by burcin created at 2009-09-19 15:11:41

Set assignee to burcin.


---

Comment by burcin created at 2009-09-19 15:11:41

Changing status from new to assigned.


---

Attachment

This is fixed in my pynac tree. Doctest for Sage is in attachment:trac_6902-log_latex.patch.

I will post a new pynac spkg and review instructions soon.


---

Comment by burcin created at 2009-09-22 19:28:15

New pynac package available at #6993.


---

Comment by kcrisman created at 2009-09-23 02:35:33

This works.  Pending of course review of new Pynac as a whole.


---

Comment by mvngu created at 2009-09-25 22:44:59

Resolution: fixed


---

Comment by mvngu created at 2009-09-27 10:39:40

There is no 4.1.2.alpha3. Sage 4.1.2.alpha3 was William Stein's release for working on making the notebook a standalone package.
