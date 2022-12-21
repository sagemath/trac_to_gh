# Issue 5328: Make the ATLAS rebuild on tolerance incremental (followup to #1641)

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2009-02-21 07:01:14

Assignee: mabshoff

My spkg from #1641 did not work 100% due to a bug in spkg-install that detected the failure. The fix is to delete error* in ATLAS' build directory on restart. 

Since on some machines the ATLAS tune can fail hours into the build, i.e. Itanium or Sparc the incremental restart is the better solution IMHO.

Note that #5219 should be taken care of at the same time.

Cheers,

Michael 


---

Comment by mabshoff created at 2009-02-21 07:03:55

Changing status from new to assigned.


---

Comment by mabshoff created at 2009-02-21 07:33:27

This info from the ATLAS 3.8 errata page might also be relevant here:

```
How do I restart an interrupted install?

If your ATLAS install was interrupted, and you have fixed the problem, you 
can usually safely (there are always exceptions; if the install died in the 
middle of an ar command, for instance, many systems cannot recover) restart 
the install by:

(1) Edit your Make.inc and if the INSTFLAGS macro includes the flags -a 1 
change them to: -a 0. This tells ATLAS not to recopy the arch defaults 
over your partially completed results.

(2) Issuing "make" from your BLDdir directory.
```


Cheers,

Michael


---

Comment by mabshoff created at 2009-03-01 02:22:44

Better luck in 3.4.1.

Cheers,

Michael


---

Comment by jdemeyer created at 2013-05-16 07:52:22

Resolution: duplicate


---

Comment by jdemeyer created at 2013-05-16 07:52:22

I assume this is obsoleted by #10508.
