# Issue 8636: iconv -- put the "do not build check" in the right place

Issue created by migration from Trac.

Original creator: was

Original creation time: 2010-03-31 15:22:15

Assignee: GeorgSWeber

New spkg here

   http://boxen.math.washington.edu/home/wstein/patches/iconv-1.13.1.p1.spkg

I've already posted this to the sagemath.org website, so people get it when they upgrade.   However, it's critical that it go into sage-4.4, or the problem will just reappear. 


---

Comment by was created at 2010-03-31 15:51:49

Changing status from new to needs_review.


---

Comment by jhpalmieri created at 2010-03-31 16:24:48

Changing status from needs_review to positive_review.


---

Comment by jhpalmieri created at 2010-03-31 16:32:33

First, the code is obviously right.  Second, it works: starting with Sage 4.3.4, force-installing the previous version of the iconv spkg breaks Sage 4.3.4 on platforms other than Solaris or Cygwin.  Force-installing this one doesn't.


---

Comment by jhpalmieri created at 2010-04-16 17:22:59

Merged spkg from #8638 in 4.4.alpha0.


---

Comment by jhpalmieri created at 2010-04-16 17:22:59

Resolution: fixed
