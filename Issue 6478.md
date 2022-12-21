# Issue 6478: [with patch, needs review] Make sage -combinat work without touching .hgrc

Issue created by migration from Trac.

Original creator: nthiery

Original creation time: 2009-07-08 06:26:33

Assignee: nthiery

CC:  sage-combinat

Keywords: sage -combinat

With the attached patch, sage -combinat uses the --config switch of hg to request it to load the mq extension. This relieves the user from creating a .hgrc for basic usage of sage -combinat.


---

Attachment


---

Comment by ddrake created at 2009-07-08 08:41:00

Looks good. Positive review.


---

Comment by rlm created at 2009-07-08 20:22:50

Merged in sage-4.1 final.


---

Comment by rlm created at 2009-07-08 20:22:50

Resolution: fixed
