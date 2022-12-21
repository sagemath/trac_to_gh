# Issue 2868: Weight revision for fastcrystals

Issue created by migration from Trac.

Original creator: bump

Original creation time: 2008-04-09 23:48:25

Assignee: mhansen

CC:  sage-combinat

This extends the revision of the patch in:

http://sagetrac.org/sage_trac/ticket/2853

The previous patch reimplemented the weight function for vertices in crystals of letters and crystals of tableaux. The patch at hand does the corresponding reimplementation for fastcrystals. These are crystals whose definition is limited to types A2, B2, C2. They are isomorphic to crystals of tableaux but have better speed when the crystal is large, since the root operators are implemented by table lookup. 

The revised weight function should be very fast since the weight is computed by adding a few numbers together.

This patch corrects the same defect for type A2 that the previous patch addressed.

The tests in the patch were written BEFORE the weight function was reimplemented, so I am confident that it is correct.


---

Attachment


---

Comment by bump created at 2008-04-09 23:51:56

Changing status from new to assigned.


---

Comment by bump created at 2008-04-09 23:51:56

Changing assignee from mhansen to bump.


---

Comment by bump created at 2008-04-10 00:24:20

Changing assignee from bump to mhansen.


---

Comment by bump created at 2008-04-10 00:24:20

Changing status from assigned to new.


---

Attachment


---

Comment by mhansen created at 2008-04-10 03:15:08

Changing status from new to assigned.


---

Comment by mhansen created at 2008-04-10 03:15:08

I attached a new patch which removes a print statement and moves the tests down to the docstring of weight.


---

Comment by mabshoff created at 2008-04-10 03:35:04

Resolution: fixed


---

Comment by mabshoff created at 2008-04-10 03:35:04

Merged 2868.patch in Sage 3.0.alpha4
