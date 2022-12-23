# Issue 4191: Update eclib to eclib-20080310.p6.spkg

Issue created by migration from https://trac.sagemath.org/ticket/4191

Original creator: cremona

Original creation time: 2008-09-24 14:54:48

Assignee: mabshoff

Keywords: eclib

I applied the patch supplied by Arnaud Bergeron to use ${MAKE} instead of make.  At the same time I changed one line in src/g0n/Makefile, adding ecnf to PROGS since otherwise that binary was being left behind after "make veryclean".

I seem to remember that mabsoff said that the effect would be negligible since my Makefiles use gnu-isms anyway, but here it is.

See also #3358.

I just checked that this installs ok on a fresh 3.1.3.alpha1 build.  A fresh spkg is attached.


---

Comment by mabshoff created at 2008-09-24 20:26:37

John,

please do not attach spkgs since the trac install (and all attachments) are backed up daily and a 1.5mb spkg is rather large. So I have deleted the spkg and it is now at

http://sage.math.washington.edu/home/mabshoff/eclib-20080310.p6.spkg

Cheers,

Michael


---

Comment by cremona created at 2008-09-24 20:58:02

Replying to [comment:2 mabshoff]:
> John,
> 
> please do not attach spkgs since the trac install (and all attachments) are backed up daily and a 1.5mb spkg is rather large. So I have deleted the spkg and it is now at
> 
> http://sage.math.washington.edu/home/mabshoff/eclib-20080310.p6.spkg
> 
> Cheers,
> 
> Michael

Very sorry, I knew I would do something wrong.  Next time I'll just put it somewhere and put in a link.  Now I have a sagemath account that will be easier.


---

Comment by mabshoff created at 2008-09-25 00:54:04

Everything looks good. I deleted on stray SPKG.txt~ from the main directory. Positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-25 00:54:33

Merged in Sage 3.1.3.alpha2


---

Comment by mabshoff created at 2008-09-25 00:54:33

Resolution: fixed
