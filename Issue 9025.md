# Issue 9025: PALP is building 32-bit on OpenSolaris - probably other platforms too.

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2010-05-23 23:57:34

Assignee: drkirkby

CC:  jsp

Attempting a 64-bit build of Sage on OpenSolaris I noticed several files are built 32-bit, even though SAGE64 is set to yes. This includes the following files. 


```
rkirkby`@`hawk:~/sage-4.4.2$ file local/bin/*.x | grep 32
local/bin/class.x:	ELF 32-bit LSB executable 80386 Version 1 [FPU], dynamically linked, not stripped
local/bin/cws.x:	ELF 32-bit LSB executable 80386 Version 1 [FPU], dynamically linked, not stripped
local/bin/nef.x:	ELF 32-bit LSB executable 80386 Version 1 [FPU], dynamically linked, not stripped
local/bin/poly.x:	ELF 32-bit LSB executable 80386 Version 1 [FPU], dynamically linked, not stripped

```


which are all part of 'PALP' There is nothing in the Makefile to force a 64-bit build on any platform, so I would not be surprised if only 32-bit objects were built on OS X or anywhere else where SAGE64 needs to be set to "yes" to get a 64-bit build.

Fixing this should be quite easy.


---

Attachment

Mercurial patch


---

Comment by drkirkby created at 2010-05-24 00:35:27

This was easily fixed by adding the flag -m64. I did this via 'sed' as it was the simplest way to change a few bytes in a large file. The revised package may be found here:

http://boxen.math.washington.edu/home/kirkby/patches/palp-1.1.p2.spkg

Now the files build 64-bit:


```
drkirkby`@`hawk:~/sage-4.4.2$ file local/bin/*.x
local/bin/class.x:	ELF 64-bit LSB executable AMD64 Version 1, dynamically linked, not stripped
local/bin/cws.x:	ELF 64-bit LSB executable AMD64 Version 1, dynamically linked, not stripped
local/bin/nef.x:	ELF 64-bit LSB executable AMD64 Version 1, dynamically linked, not stripped
local/bin/poly.x:	ELF 64-bit LSB executable AMD64 Version 1, dynamically linked, not stripped
```



---

Comment by drkirkby created at 2010-05-24 00:35:27

Changing status from new to needs_review.


---

Comment by drkirkby created at 2010-05-24 18:23:18

For other OpenSolaris issues, see #9026


---

Comment by drkirkby created at 2010-06-05 22:11:43

This needs rebasing.


---

Comment by drkirkby created at 2010-06-05 22:11:43

Changing status from needs_review to needs_work.


---

Comment by jsp created at 2010-06-14 12:18:12

Replying to [comment:5 drkirkby]:
> This needs rebasing. 

What do you mean? Isn't renaming enough?

Jaap


---

Comment by drkirkby created at 2010-06-14 12:29:11

Someone has made other changes, so they need to be considered. It is not as simple as just renaming this package. I dobut it is rocket science though - leave it with me. It will be ready for review later today. I have a chess game in half an hour, so do not have time to do it now. 

It is better if I do it, rather than you. Then you can review it. 

Dave


---

Comment by drkirkby created at 2010-06-14 13:02:44

It's here now, awaiting review. 

http://boxen.math.washington.edu/home/kirkby/patches/palp-1.1.p3.spkg


---

Comment by drkirkby created at 2010-06-14 13:02:44

Changing status from needs_work to needs_review.


---

Comment by jsp created at 2010-06-14 13:40:35

Ok, on OpenSolaris:


```
Finished installing palp-1.1.p3.spkg
-bash-4.0$ file local/bin/*.x | grep 32
-bash-4.0$ file local/bin/*.x | grep 64
local/bin/class.x:      ELF 64-bit LSB executable AMD64 Version 1, dynamically linked, not stripped
local/bin/cws.x:        ELF 64-bit LSB executable AMD64 Version 1, dynamically linked, not stripped
local/bin/nef.x:        ELF 64-bit LSB executable AMD64 Version 1, dynamically linked, not stripped
local/bin/poly.x:       ELF 64-bit LSB executable AMD64 Version 1, dynamically linked, not stripped
-bash-4.0$ 

```


Positive review.

Jaap


---

Comment by jsp created at 2010-06-14 13:40:35

Changing status from needs_review to positive_review.


---

Comment by rlm created at 2010-06-25 15:48:14

Resolution: fixed
