# Issue 8117: zodb3 fails to build in Open Solaris x64 as 64 bit if CFLAGS is not set

Issue created by migration from https://trac.sagemath.org/ticket/8117

Original creator: jsp

Original creation time: 2010-01-29 13:36:51

Assignee: drkirkby

If CFLAGS not contains -m64 zodb3-3.7.0.2 fails to build on Open Solaris x64. This works only on OSX 64 bit.

A patch is coming up.

Jaap


---

Attachment

Added spkg.

[http://boxen.math.washington.edu/home/jsp/ports/zodb3-3.7.0.p3.spkg](http://boxen.math.washington.edu/home/jsp/ports/zodb3-3.7.0.p3.spkg)



```
local/lib/python2.6/site-packages/ZODB/winlock.so:	ELF 64-bit LSB dynamic lib AMD64 Version 1, dynamically linked, not stripped
jaap@opensolaris:~/Downloads/sage-4.3.2.alpha0$ 


```


Jaap


---

Comment by jsp created at 2010-01-29 13:57:12

Changing status from new to needs_review.


---

Comment by drkirkby created at 2010-01-29 18:37:16

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-02-11 15:18:13

Resolution: fixed
