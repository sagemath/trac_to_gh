# Issue 2209: gap on itanium - incorporate steve linton's new fixes so gap builds fine with optimizations

Issue created by migration from https://trac.sagemath.org/ticket/2209

Original creator: was

Original creation time: 2008-02-19 15:19:47

Assignee: mabshoff

The patch is here:

   http://www.gap-system.org/Faq/Hardware-OS/hardware-os8.html


---

Comment by was created at 2008-02-19 15:37:29

I've created an updated package that:
 
1. Incorporates this patch and re-enables optimizations on ia64.

2. Copies the html gap docs to SAGE_ROOT/local/doc/

The new spkg is here:

http://sage.math.washington.edu/home/was/patches/gap/gap-4.4.10.p3.spkg

Please test!


---

Comment by broune created at 2008-05-12 11:25:58

on intel mac 10.5: installed fine, doctests pass in sage/interfaces/ . Needs review on itanium to tell if the fixes actually work.


---

Comment by craigcitro created at 2008-06-15 21:38:53

Changing keywords from "" to "editor_wstein".


---

Comment by was created at 2008-06-15 22:14:31

Note -- reviewing this has to wait until SkyNet isn't down....


---

Comment by mabshoff created at 2008-06-15 22:28:54

Note that there have been many small fixes to the GAP.spkg, so the fixes have to be rebased on the current one.

Cheers,

Michael


---

Attachment


---

Comment by was created at 2008-08-27 21:22:20

I skimmed Steve Linton's patch from 

 http://www.gap-system.org/Faq/Hardware-OS/hardware-os8.html

then applied it and tested it on itanium.  It worked perfectly, and also gave a nice 5 times speed up on the first thing I tried:

```
sage: G = SymmetricGroup(16)
sage: h = G.normal_subgroups()
```


I doctested the groups directory, and have started the doctest cycle on everything else.
I'll post a note here when that is done.


---

Comment by mabshoff created at 2008-08-29 02:38:09

Second positive review from my end. Doctests on Itanium pass (with exception of the two failures at #3984)

Cheers,

Michael


---

Comment by mabshoff created at 2008-08-29 02:58:09

Merged in Sage 3.1.2.alpha2


---

Comment by mabshoff created at 2008-08-29 02:58:09

Resolution: fixed
