# Issue 906: bugs in special.py

Issue created by migration from Trac.

Original creator: wdj

Original creation time: 2007-10-16 03:29:15

Assignee: wdj

Over a year ago there were some bugs reported by someone on the email lists regarding the implementation of the special functions. SAGE's special functions are wrappers for Pari or Maxima functions, so basically this is an interface issue. Basically, some of the functions implemented as F(x,n) should have been called using F(n,x). A patch was created last October 2006 but never applied. This patch includes most of that old patch. 

Also, at someone's request (I think William Stein), a Bessel function class was created which implemented a few Bessel functions as class instances. 

All this is in the patch 
http://sage.math.washington.edu/home/wdj/patches/special-functions.hg
It passed sage-t.


---

Comment by was created at 2007-10-20 22:26:02

Resolution: fixed
