# Issue 1844: [with bundle] Get doctest coverage in sage/modular/modform up to 100%

Issue created by migration from Trac.

Original creator: craigcitro

Original creation time: 2008-01-19 01:50:38

Assignee: craigcitro

This patch brings doctest coverage up to 100% for every file in sage/modular/modform except for find_generators.py, which isn't imported into sage by default anyway. Needless to say, there are lots of small fixes and whatnot. 


---

Attachment


---

Comment by craigcitro created at 2008-01-19 06:24:43

Changing status from new to assigned.


---

Comment by craigcitro created at 2008-01-19 06:27:21

I'm adding a patch that one should use *instead* of the .hg bundle above. (It's a patch with *just* the modular form changes, as opposed to a lot of the junk that made it into my bundle.)


---

Attachment


---

Attachment


---

Comment by mhansen created at 2008-01-19 07:55:49

I added a new patch which should apply cleanly against 2.10.


---

Attachment


---

Comment by craigcitro created at 2008-01-19 09:55:08

One should apply 1844-2.patch and then 1844-2a.patch from a clean 2.10 install. (The 2a is a very small patch.)

This should be ready to go. *crosses fingers*


---

Comment by mabshoff created at 2008-01-21 04:26:48

Resolution: fixed


---

Comment by mabshoff created at 2008-01-21 04:26:48

Merged 1844-2.patch and 1844-2a.patch in Sage 2.10.1.alpha1 - finally :)
