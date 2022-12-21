# Issue 1642: Fortran.spkg: search for common Fortran compiles if no binary is present

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2007-12-30 18:50:22

Assignee: mabshoff

We do not have binaries on less common platforms. If SAGE_FORTRAN isn't set we just fail, but we should check for common Fortran compilers and set them then instead of failing. Preference should be:
 * gfotran
 * g95
 * g77
 * f77 - on BSD the g77 is commonly called f77

Cheers,

Michael


---

Comment by mabshoff created at 2007-12-31 10:24:03

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-04-20 06:31:21

Resolution: fixed


---

Comment by mabshoff created at 2008-04-20 06:31:21

This has been fixed by William Stein a while ago.

Cheers,

Michael
