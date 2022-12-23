# Issue 4911: convert sage.games.* docstrings to Sphinx

Issue created by migration from https://trac.sagemath.org/ticket/4911

Original creator: mhansen

Original creation time: 2009-01-01 22:51:10

Assignee: tba




---

Attachment


---

Comment by jhpalmieri created at 2009-01-07 22:05:04

line 56: "`contains the :math:`i`,:math:`j` position`" is not being rendered properly.  Maybe replace it with "`contains the :math:`i,j` position`".

Actually, why do you need :math: here at all?  I don't remember seeing it in the other files that I've looked at...


---

Attachment

I've posted a patch which fixes this issue.  The :math: was there because I had forgot to go through this file and remove them.


---

Comment by jhpalmieri created at 2009-01-08 23:36:14

Great, positive review.


---

Attachment

Merged sage.games-final.patch in Sage 3.4.alpha0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-24 18:01:53

Resolution: fixed
