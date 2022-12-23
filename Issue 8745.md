# Issue 8745: Steiner Triple Systems

Issue created by migration from https://trac.sagemath.org/ticket/8745

Original creator: ncohen

Original creation time: 2010-04-22 12:31:11

Assignee: sage-combinat

CC:  wdj

This patch adds a function to block_design returning a Steiner Triple System on any number of vertices n congruent to 1 or 3 modulo 6. There is none otherwise :-)

The function is pretty short, a satisfiable decomposition being explicitely given in the reference : 
http://www.utu.fi/~honkala/designs.ps

Nathann


---

Comment by ncohen created at 2010-04-22 12:34:01

Changing status from new to needs_review.


---

Attachment


---

Comment by wdj created at 2010-04-22 22:53:13

Applies fine to 4.4.a1, passes sage -testall on a 10.6.2 mac (except for the r.py failure, which is unrelated), and looks good to me in terms of examples and references.

Thanks Nathann!


---

Comment by wdj created at 2010-04-22 22:53:13

Changing status from needs_review to positive_review.


---

Comment by ncohen created at 2010-04-23 06:42:26

Whaouuuuuuu !!! Such a quick review :-)

Thank you very much too !! :-)

Nathann


---

Comment by was created at 2010-04-29 05:08:16

Resolution: fixed
