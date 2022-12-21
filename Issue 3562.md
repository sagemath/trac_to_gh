# Issue 3562: Do not doctest pbuild files in devel/sage

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-07-06 11:35:14

Assignee: mabshoff

Currently `-tp` doctests the three pbuild files 

 * sagebuild.py
 * clib.py
 * build.py

Don't do it :).

I need to check if `-t` also picks up those files or if they are treated differently. We certainly don't doctest setup.py.

Cheers,

Michael



---

Comment by mabshoff created at 2008-07-06 11:35:25

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-07-06 17:22:42

I now tend to blame this on my stupidity doctesting devel/sage instead of devel/sage/sage as I should. But I am also wondering whether to add `nodoctest` to the three files above nonetheless to prevent accidental testing.

Cheers,

Michael


---

Comment by mabshoff created at 2008-07-06 17:43:04

This is invalid and just to blame on my stupidity.

Cheers,

Michael


---

Comment by mabshoff created at 2008-07-06 17:43:04

Resolution: invalid
