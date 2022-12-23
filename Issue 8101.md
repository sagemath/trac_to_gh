# Issue 8101: ntl fails to build in Open Solaris x64 as 64 bit if CFLAGS is not set

Issue created by migration from https://trac.sagemath.org/ticket/8101

Original creator: jsp

Original creation time: 2010-01-27 23:48:53

Assignee: drkirkby

On Open Solaris x64 as 64 bit without setting CFLAGS globally build is 32 bit.

A patch is under way.

Jaap


---

Comment by jsp created at 2010-01-27 23:58:42

Changing status from new to needs_review.


---

Attachment

An spkg can be found here:

[http://boxen.math.washington.edu/home/jsp/ports/ntl-5.4.2.p11.spkg](http://boxen.math.washington.edu/home/jsp/ports/ntl-5.4.2.p11.spkg)

Jaap


---

Comment by drkirkby created at 2010-01-28 13:51:47

Positive review. All shared libraries are indeed 64-bit now. 


```
drkirkby@hawk:~/sage-4.3.1$ file local/lib/lib*ntl*
local/lib/libntl-5.4.2.so:	ELF 64-bit LSB dynamic lib AMD64 Version 1, dynamically linked, not stripped
local/lib/libntl.a:	current ar archive, not a dynamic executable or shared object
local/lib/libntl.so:	ELF 64-bit LSB dynamic lib AMD64 Version 1, dynamically linked, not stripped
```



---

Comment by drkirkby created at 2010-01-28 13:51:47

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-02-11 15:13:21

Resolution: fixed
