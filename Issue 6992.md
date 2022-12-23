# Issue 6992: rename lngamma to log gamma

Issue created by migration from https://trac.sagemath.org/ticket/6992

Original creator: burcin

Original creation time: 2009-09-22 19:10:47

Assignee: burcin

The Sage convention is to use `log` for the natural logarithm. See #6902 for more discussion.

Attached patch renames the `lngamma` functions in the library, and adds deprecation notices where appropriate.



---

Attachment


---

Comment by burcin created at 2009-09-22 19:30:20

Changing status from new to assigned.


---

Comment by burcin created at 2009-09-22 19:30:20

New pynac package available at #6993.


---

Comment by kcrisman created at 2009-09-23 02:57:43

In sage/symbolic/expression.pyx, there is a plot of the log_gamma function in line 4918, which nonetheless raises the DeprecationWarning when I test it via sage -t, though not when I cut and paste that command.  It happens also upon a retest.  Do you get this?  I find it very strange, so I wonder if I did something wrong.


---

Comment by kcrisman created at 2009-09-23 20:08:30

Upon applying all the patches involved, this disappears, quite mysteriously.


---

Comment by mvngu created at 2009-09-25 22:47:17

Resolution: fixed


---

Comment by mvngu created at 2009-09-27 10:42:44

There is no 4.1.2.alpha3. Sage 4.1.2.alpha3 was William Stein's release for working on making the notebook a standalone package.


---

Comment by eviatarbach created at 2013-06-25 09:40:07

#12521 gets rid of the deprecated functions.
