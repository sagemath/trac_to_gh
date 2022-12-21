# Issue 7335: tachyon fails to build on Cygwin

Issue created by migration from Trac.

Original creator: mhansen

Original creation time: 2009-10-28 19:33:41

Assignee: tbd

CC:  was

It fails with the following error


```
cc1: error: unrecognized command line option "-mpentium"
```


The fix is simply to simply remove that part of the flags from the Make-arch file for the win32 target.

I will post an updated spkg shortly.


---

Comment by mhansen created at 2009-11-06 05:08:35

Changing status from new to needs_review.


---

Comment by mhansen created at 2009-11-06 05:08:35

There is an spkg at http://sage.math.washington.edu/home/mhansen/tachyon-0.98beta.p10.spkg


---

Comment by was created at 2009-11-06 06:07:48

It works.


---

Comment by was created at 2009-11-06 06:07:48

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2009-11-12 06:16:04

Resolution: fixed


---

Comment by kcrisman created at 2011-06-16 16:57:43

#11504 is this again.

I couldn't extract this properly (it tried, and looked right, but then had 'x's next to everything and was not a folder).

Anyway, the fix is the same.
