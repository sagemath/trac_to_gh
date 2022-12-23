# Issue 2528: File sage/modular/dims_doc.py should be removed soon

Issue created by migration from https://trac.sagemath.org/ticket/2528

Original creator: craigcitro

Original creation time: 2008-03-15 05:53:18

Assignee: was

This file existed for only including certain parts of dims.py into the reference manual; this is no longer necessary, and the file should be removed. Care needs to be taken to not break the reference manual -- William has a fix that he's going to submit when I post this.


---

Attachment


---

Attachment


---

Comment by craigcitro created at 2008-03-15 08:45:51

The second patch applies against the main repository, and removes the file in the title.


---

Comment by mabshoff created at 2008-03-15 22:03:34

Somebody has been sneaking an extra hunk in trac-2528.patch. The first hunk has a merge conflict, which I cannot see [maybe white space?], but I ended up merging that hunk manually.

Cheers,

Michael


---

Comment by craigcitro created at 2008-03-15 22:07:35

Actually, it's not an extra hunk -- I'm moving comments that were in `dims_doc.py` into `dims.py` so that they're not lost. Maybe I should have mentioned that more explicitly.


---

Comment by mabshoff created at 2008-03-15 22:29:52

Replying to [comment:5 craigcitro]:
> Actually, it's not an extra hunk -- I'm moving comments that were in `dims_doc.py` into `dims.py` so that they're not lost. Maybe I should have mentioned that more explicitly.
> 

Either way, it is fixed :)

Cheers,

Michael


---

Comment by mabshoff created at 2008-03-15 22:30:07

Resolution: fixed


---

Comment by mabshoff created at 2008-03-15 22:30:07

Merged in Sage 2.10.4.rc0
