# Issue 326: rebuild system doesn't recognise changed pyrex files on OS X

Issue created by migration from Trac.

Original creator: dmharvey

Original creation time: 2007-03-21 04:25:32

Assignee: was

When I change a pyrex file (specifically rings/integer.pyx), sage -b doesn't seem to notice. I have to manually delete the corresponding .c file to get a rebuild happening. This is mac OS 10.4.9, powerpc G5, sage 2.3.



---

Comment by was created at 2007-03-21 22:35:11

Resolution: invalid


---

Comment by was created at 2007-03-21 22:35:11

Depedency checking works fine on OS X Intel.  In fact I wrote it under OS X intel.  I
tried exactly your example and it works. 

I also just tested on a G5 intel machine and dependency testing works fine under sage-2.3.

I have no idea how your install is messed up, but the problem isn't something general.


---

Comment by was created at 2007-03-22 02:21:02

Changing status from closed to reopened.


---

Comment by was created at 2007-03-22 02:21:02

Resolution changed from invalid to 


---

Comment by was created at 2007-03-22 02:21:45

We changed some getctimes to getmtimes and all is well now for David.


---

Comment by was created at 2007-03-22 02:21:45

Resolution: fixed
