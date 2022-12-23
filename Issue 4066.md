# Issue 4066: [with patch, needs review] Sage 3.1.2.alpha3: Solaris build fixes for the Sage library

Issue created by migration from https://trac.sagemath.org/ticket/4066

Original creator: mabshoff

Original creation time: 2008-09-05 06:42:16

Assignee: mabshoff

CC:  robertwb

There are two small fixes needed for the Sage library.

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-05 06:42:21

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-09-05 07:42:26

Oops, this patch is not ready for review since some doctests fail. I will post an updated patch shortly.

Cheers,

Michael


---

Attachment

Ok, I have attached an updated patch that 

 * passes -ba
 * builds fine on Solaris, OSX and Linux and passes doctests on OSX and Linux

Note that _[A-Z] are numerical constants on BSD and Solaris and should not be used as variable names.

I am CCing Robert since he was involved in writing that code (I think :))

Cheers,

Michael


---

Comment by malb created at 2008-09-05 12:04:56

It applies cleanly against my alpha3, it builds on my 64-bit Linux box, `sage -t rings` passes which should use this functionality (?)

It SEGFAULTS with `sage -tp 2 sage/rings` in bernouli_mod_p.pyx though. If that can't be reproduced it might just be a weird combination of patches on my machine.


---

Comment by mabshoff created at 2008-09-05 16:59:49

Resolution: fixed


---

Comment by mabshoff created at 2008-09-05 16:59:49

Merged in Sage 3.1.2.rc0
