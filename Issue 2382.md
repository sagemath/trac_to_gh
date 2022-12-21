# Issue 2382: sage-doctest broken by removal of temp files

Issue created by migration from Trac.

Original creator: gfurnish

Original creation time: 2008-03-04 06:25:47

Assignee: gfurnish

The removal of temporary files from sage-doctest causes mysterious errors to occur


---

Comment by gfurnish created at 2008-03-04 06:25:54

Changing status from new to assigned.


---

Comment by gfurnish created at 2008-03-04 06:48:59

Changing status from assigned to new.


---

Attachment

3rd is correct patch


---

Comment by gfurnish created at 2008-03-04 06:52:26

This seems to fix the modular/space.py doctest issue.


---

Comment by gfurnish created at 2008-03-04 06:54:51

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-03-04 23:51:48

Resolution: fixed


---

Comment by mabshoff created at 2008-03-04 23:51:48

Merged trac_2382.3.patch in Sage 2.10.3.rc2
