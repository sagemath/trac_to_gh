# Issue 8113: gd-2.0.35.p3 fails to build on Open Solaris x64 as 64 bit without setting CFLAGS=-64 globally

Issue created by migration from https://trac.sagemath.org/ticket/8113

Original creator: jsp

Original creation time: 2010-01-28 17:24:13

Assignee: AlexGhitza

CC:  drkirkby

Build will be 32 bit, even when SAGE64="yes".

There is a simple patch coming up.

Jaap




---

Attachment


---

Comment by jsp created at 2010-01-28 17:43:46

Changing status from new to needs_review.


---

Comment by jsp created at 2010-01-28 17:43:46

I would say the usual act in spkg-install. See the patch.


The spkg is here:
[http://boxen.math.washington.edu/home/jsp/ports/gd-2.0.35.p4.spkg](http://boxen.math.washington.edu/home/jsp/ports/gd-2.0.35.p4.spkg)



```
jaap@opensolaris:~/Downloads/sage-4.3.2.alpha0/local$ file lib/libgd.so
lib/libgd.so:	ELF 64-bit LSB dynamic lib AMD64 Version 1, dynamically linked, not stripped

```


Jaap


---

Comment by jsp created at 2010-01-29 16:23:42

Changing component from algebra to porting.


---

Comment by drkirkby created at 2010-01-29 18:29:09

Changing status from needs_review to positive_review.


---

Comment by drkirkby created at 2010-01-29 18:29:09

The files are indeed 64-bit now 


```
drkirkby@hawk:~/sage-4.3.1$ file local/bin/annotate
local/bin/annotate:	ELF 64-bit LSB executable AMD64 Version 1, dynamically linked, not stripped
drkirkby@hawk:~/sage-4.3.1$ file local/lib/libgd.so.2.0.0
local/lib/libgd.so.2.0.0:	ELF 64-bit LSB dynamic lib AMD64 Version 1, dynamically linked, not stripped
```



---

Comment by mpatel created at 2010-02-11 15:16:29

Resolution: fixed
