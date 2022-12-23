# Issue 8060: New f2c-20070816.p2.spkg now works with Open Solaris 64 bit

Issue created by migration from https://trac.sagemath.org/ticket/8060

Original creator: jsp

Original creation time: 2010-01-25 19:57:56

Assignee: drkirkby

Made SAGE64="yes" also work on Opensolaris.

[http://boxen.math.washington.edu/home/jsp/ports/f2c-20070816.p2.spkg](http://boxen.math.washington.edu/home/jsp/ports/f2c-20070816.p2.spkg)

Jaap




---

Comment by jsp created at 2010-01-25 19:58:15

Changing status from new to needs_review.


---

Attachment


---

Comment by drkirkby created at 2010-01-27 13:49:34

Changing status from needs_review to positive_review.


---

Comment by drkirkby created at 2010-01-27 13:49:34

I changed the title, to put x64 rather than 64-bit, as there is Open Solaris running on SPARC systems, and we have no idea if this fixes issues on SPARC or not, unless we test it. You probably do not have SPARC hardware, and I don't have Open Solaris running on SPARC, so we can't actually be sure. I suspect it will work on SPARC too, but by putting x64, we make it clear it works on x64, and is untested on SPARC.


---

Comment by mpatel created at 2010-02-11 15:16:23

Resolution: fixed
