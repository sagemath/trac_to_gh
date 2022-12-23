# Issue 4010: notebook -- Renaming worksheet: clicking OK with a blank text box should revert to worksheet's old name not name it to "null"

Issue created by migration from https://trac.sagemath.org/ticket/4010

Original creator: TimothyClemans

Original creation time: 2008-08-31 00:59:35

Assignee: boothby




---

Comment by mhansen created at 2009-01-20 10:50:52

Changing status from new to assigned.


---

Comment by mhansen created at 2009-01-20 10:50:52

Changing assignee from boothby to mhansen.


---

Attachment

Some code for this is already there except we need to handle the case where prompt returns an empty string (which is the case in Firefox).


---

Comment by jason created at 2009-01-22 15:30:17

This works for me in FF 3 in Ubuntu.  Positive Review.


---

Comment by mabshoff created at 2009-01-23 10:26:27

Merged in Sage 3.3.alpha1

Cheers,

Michael


---

Comment by mabshoff created at 2009-01-23 10:26:27

Resolution: fixed
