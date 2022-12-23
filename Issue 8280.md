# Issue 8280: cygwin: zn_poly shared library named incorrectly on cygwin

Issue created by migration from https://trac.sagemath.org/ticket/8280

Original creator: was

Original creation time: 2010-02-16 02:08:16

Assignee: tbd

When trying to build sage on cygwin, I had to do this:


```
wstein@winxp ~/build/sage-4.3.3.alpha0/local/lib
$ ln -s libzn_poly.so libzn_poly.dll
```



---

Comment by mhansen created at 2010-02-16 04:47:15

I've posted an spkg which fixes this at http://sage.math.washington.edu/home/mhansen/cygwin_port/zn_poly-0.9.p2.spkg


---

Comment by mhansen created at 2010-02-16 04:47:15

Changing status from new to needs_review.


---

Comment by mvngu created at 2010-02-16 07:37:05

What is the purpose of this change?

```
-#!/usr/bin/env bash
+B#!/usr/bin/env bash
```



---

Comment by mhansen created at 2010-02-16 07:40:09

Oops -- just a typo.  I've fixed it now.


---

Comment by mvngu created at 2010-02-17 00:29:13

The changes looks OK to me. Sage 4.3.3.alpha0 compiled OK with this updated spkg. All doctests pass. The Cygwin build went pass the compilation process of zn_poly.


---

Comment by mvngu created at 2010-02-17 00:29:13

Changing status from needs_review to positive_review.


---

Comment by mvngu created at 2010-02-17 00:29:39

Resolution: fixed
