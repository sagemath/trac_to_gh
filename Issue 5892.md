# Issue 5892: Do not give workaround instructions when SIMD instructions aren't compatible

Issue created by migration from https://trac.sagemath.org/ticket/5892

Original creator: mabshoff

Original creation time: 2009-04-25 09:11:58

Assignee: mabshoff

When Sage gives a warning about SIMD instructions way too many _experts_ just delete the file as indicated and then complain about Sage blowing up. Don't give them the chance to do something stupid any more by removing the work around instructions. 

Cheers,

Michael


---

Comment by was created at 2009-06-15 23:27:48

Resolution: invalid


---

Comment by was created at 2009-06-15 23:27:48

The right fix is to (1) remove this SIMD stuff (already done), and (2) make a SAGE_FAT_BINARY option that actually *works*.  So far, absolutely nothing at all that has been done toward this problem has worked in the list bit.  I'm closing this ticket as invalid.
