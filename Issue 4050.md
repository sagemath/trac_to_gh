# Issue 4050: Shared worksheets are not copied correctly

Issue created by migration from https://trac.sagemath.org/ticket/4050

Original creator: mhampton

Original creation time: 2008-09-03 18:33:27

Assignee: boothby

Copying a shared worksheet makes a copy for the owner, not the copier, and the copy is unshared.  This is a big problem for my use in classes.


---

Comment by mhansen created at 2008-09-04 01:36:12

This is fixed by my patch at #3960.


---

Comment by mabshoff created at 2008-09-04 02:02:50

Resolution: fixed


---

Comment by mabshoff created at 2008-09-04 02:02:50

Fixed due to #3960 being merged. Thanks Mike :)

Cheers,

Michael
