# Issue 7697: Delete OS X meta-crap from gfan-0.3.p4

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-12-16 01:13:31

Assignee: tbd


```
      sage-4.3.rc0/spkg/standard/gfan-0.3.p4/src/.DS_Store
```



---

Comment by was created at 2009-12-18 06:26:39

Here is the spkg:  http://wstein.org/home/wstein/patches/gfan-0.3.p5.spkg


---

Comment by was created at 2009-12-18 06:26:39

Changing status from new to needs_review.


---

Comment by kcrisman created at 2009-12-30 03:54:07

Changing status from needs_review to positive_review.


---

Comment by kcrisman created at 2009-12-30 03:54:07

This seems fine, and still installs well - SPKG updated, hg fine, passes the (two!) relevant doctest files.  I sometimes have to watch for this as well, which is particularly annoying since Finder doesn't show the dot files.


---

Comment by mhansen created at 2010-01-03 22:24:03

Resolution: fixed
