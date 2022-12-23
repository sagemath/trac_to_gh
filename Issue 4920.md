# Issue 4920: convert sage.modular.* docstrings to Sphinx

Issue created by migration from https://trac.sagemath.org/ticket/4920

Original creator: mhansen

Original creation time: 2009-01-01 22:54:21

Assignee: tba

CC:  craigcitro




---

Comment by mhansen created at 2009-01-02 02:50:18

Patch at http://sage.math.washington.edu/home/mhansen/trac_4920.patch


---

Attachment


---

Comment by mhansen created at 2009-01-02 06:51:38

I've added an additional patch which fixes the documentation for sage.modular.etaproducts.


---

Comment by GeorgSWeber created at 2009-01-15 21:42:19

scheduled for January 20th


---

Comment by GeorgSWeber created at 2009-01-15 21:42:47

aargh, don't change the Milestone


---

Comment by mhansen created at 2009-01-15 21:49:08

I think we'd like to have it done before then so that we can get the ReST version out before Sage Days 12.  I can ask craigcitro to go through and look at it.


---

Comment by mabshoff created at 2009-01-15 22:14:06

Georg,

either you do a review or you don't, so please don't mark tickets like this if you plan to do it in the next week.

Cheers,

Michael


---

Comment by GeorgSWeber created at 2009-01-21 00:28:49

Positive review for both patches (they're independent).

Of course there are issues, e.g. the ridiculous name for the "abvar/morphism" file resp. chapter. But the polishing can happen only after the ReST switch has been completed, and changes can be "made visible".

The most important thing is that all the original information is still in the files, and this I did check. Looking over the Sage modular module, my fingers itch --- so much work (doctests, better and faster code, etc.), so little time ...


---

Attachment

The patch latex-fix-4920.patch fixes some markup problems that prevented the generation of PDF output.


---

Attachment


---

Comment by mabshoff created at 2009-02-24 19:11:36

Resolution: fixed


---

Comment by mabshoff created at 2009-02-24 19:11:36

Merged in Sage 3.4.alpha0.

Cheers,

Michael
