# Issue 8066: New libgpg_error-1.6.p3.spkg works with Open Solaris 64 bit

Issue created by migration from https://trac.sagemath.org/ticket/8066

Original creator: jsp

Original creation time: 2010-01-25 22:45:18

Assignee: drkirkby

Made the package work with Open Solaris 64 bit SAGE64="yes"

The package is here:
[http://boxen.math.washington.edu/home/jsp/ports/libgpg_error-1.6.p3.spkg](http://boxen.math.washington.edu/home/jsp/ports/libgpg_error-1.6.p3.spkg)

Jaap




---

Comment by jsp created at 2010-01-25 22:45:29

Changing status from new to needs_review.


---

Attachment

This package was building 64-bit before, so it's not entirely clear this is 100% necessary. But I agree it is desirable. It should make it more reliable. 

But it is echoing 'Mac Intel' which is incorrect. 

Dave


---

Comment by drkirkby created at 2010-01-27 13:19:11

Changing status from needs_review to needs_work.


---

Comment by drkirkby created at 2010-01-27 13:34:46

I would also put the ticket number you are fixing in SPKG.txt. You should create the ticket for the defect first. Then you have a ticket number which can be put in SPKG.txt.


---

Attachment


---

Comment by jsp created at 2010-01-27 13:42:48

Done. Didn't raise the patch level.


[http://boxen.math.washington.edu/home/jsp/ports/libgpg_error-1.6.p3.spkg](http://boxen.math.washington.edu/home/jsp/ports/libgpg_error-1.6.p3.spkg)


Jaap


---

Comment by jsp created at 2010-01-27 13:42:48

Changing status from needs_work to needs_review.


---

Comment by drkirkby created at 2010-01-27 14:12:38

Changing status from needs_review to positive_review.


---

Comment by drkirkby created at 2010-01-27 14:12:38

It would have been wiser to overwrite the patch file in this case I think. 


```
drkirkby@hawk:~/sage-4.3.1$ file local/lib/libgpg-error*
local/lib/libgpg-error.a:	current ar archive, not a dynamic executable or shared object
local/lib/libgpg-error.la:	commands text
local/lib/libgpg-error.so:	ELF 64-bit LSB dynamic lib AMD64 Version 1, dynamically linked, not stripped
local/lib/libgpg-error.so.0:	ELF 64-bit LSB dynamic lib AMD64 Version 1, dynamically linked, not stripped
local/lib/libgpg-error.so.0.4.0:	ELF 64-bit LSB dynamic lib AMD64 Version 1, dynamically linked, not stripped
```


Libraries are building 64-bit, so positive review. 

It's probably worth showing the output of the 'file' command, to show the libraries, or executables are building 64-bit. I must admit I've rarely if ever done that, but it will show that the problem is fixed, as not all packages are building properly, even with the -m64 flag added. 

Dave


---

Comment by mpatel created at 2010-02-11 15:17:16

Resolution: fixed
