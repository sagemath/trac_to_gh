# Issue 4534: Stupid error in odd_part

Issue created by migration from https://trac.sagemath.org/ticket/4534

Original creator: craigcitro

Original creation time: 2008-11-16 13:00:42

Assignee: craigcitro

I introduced an error in `odd_part` while working on #4443; the attached patch is the obvious fix, along with a doctest.


---

Comment by craigcitro created at 2008-11-16 13:01:26

Changing status from new to assigned.


---

Attachment


---

Comment by mhansen created at 2008-11-16 13:10:29

Looks good.


---

Comment by robertwb created at 2008-11-17 18:38:15

Wouldn't it be much faster to divide out by the valuation at 2?


---

Comment by craigcitro created at 2008-11-17 18:52:28

Good point. I know I timed it when I wrote it (though I obviously didn't look at the output carefully) -- of course, since the broken version doesn't do much work, it's faster. Correcting it slows it way down. 

Patch coming right up.


---

Attachment

New patch, which should be much better. Unfortunately, it touches `integer.pxd`, so it takes a while to rebuild.


---

Comment by jsp created at 2008-11-18 15:30:56

Applied trac-4534-v2.patch

Run ./sage -b and did a make check

All tests passed except the known issue with combinat/species/library.py

So I give this ticket a positive review.

Jaap


---

Comment by mabshoff created at 2008-11-18 19:39:41

Merged trac-4534-v2.patch in Sage 3.2.rc2


---

Comment by mabshoff created at 2008-11-18 19:39:41

Resolution: fixed
