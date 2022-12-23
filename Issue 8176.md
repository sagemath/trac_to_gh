# Issue 8176: libpng fails to build in Open Solaris x64 as 64 bit even if SAGE64=yes

Issue created by migration from https://trac.sagemath.org/ticket/8176

Original creator: jsp

Original creation time: 2010-02-03 18:01:21

Assignee: drkirkby

Setting SAGE64=yes is only working on Darwin. To make it work on Open Solaris and possibly on other platforms a small edit of spkg-install is needed.

A patch is coming up.

Jaap




---

Comment by jsp created at 2010-02-03 18:19:44

Changing status from new to needs_review.


---

Attachment

An spkgs can be found here:

[http://boxen.math.washington.edu/home/jsp/ports/libpng-1.2.35.p0.spkg](http://boxen.math.washington.edu/home/jsp/ports/libpng-1.2.35.p0.spkg)




```
lib/libpng12.so:	ELF 64-bit LSB dynamic lib AMD64 Version 1, dynamically linked, not stripped
lib/libpng12.so.0:	ELF 64-bit LSB dynamic lib AMD64 Version 1, dynamically linked, not stripped
lib/libpng12.so.0.35.0:	ELF 64-bit LSB dynamic lib AMD64 Version 1, dynamically linked, not stripped

```


Jaap


---

Comment by drkirkby created at 2010-02-04 17:07:45

This line makes no sence whatsovever


```
if [ `uname` = "x$SAGE64" = xyes ]; then 
```


You must have a typo there. uname will return SunOS, not yes. 

Dave


---

Comment by drkirkby created at 2010-02-04 17:07:45

Changing status from needs_review to needs_work.


---

Attachment

Some stupid error I had corrected I thought.

[http://boxen.math.washington.edu/home/jsp/ports/libpng-1.2.35.p0.spkg](http://boxen.math.washington.edu/home/jsp/ports/libpng-1.2.35.p0.spkg)

Didn't change the patch level.

Jaap


---

Comment by jsp created at 2010-02-04 18:44:05

Changing status from needs_work to needs_review.


---

Comment by drkirkby created at 2010-02-04 19:00:03

That looks fine now. I see the -m64 flag is added, and it builds as 64-bit. I even checked it on a 64-bit SPARC, and see it builds as 64-bit there too. 


```
drkirkby@swan:[~/sage-4.3.2.rc0] $ file  local/lib/libpng12.so.0.35.0
local/lib/libpng12.so.0.35.0:   ELF 64-bit MSB dynamic lib SPARCV9 Version 1, dynamically linked, not stripped
```


so positive review. 

PS, for future reference, someone mentioned the other day it would be useful if the patch number was in the Mercurial commit message. That sounds quite logical to me. But there is nothing wrong with this.


---

Comment by drkirkby created at 2010-02-04 19:00:03

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-02-11 15:17:22

Resolution: fixed
