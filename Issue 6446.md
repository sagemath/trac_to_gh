# Issue 6446: memory issue from #6394

Issue created by migration from Trac.

Original creator: rlm

Original creation time: 2009-06-29 17:29:46

Assignee: tbd




---

Attachment


---

Comment by cremona created at 2009-06-29 18:16:00

I'm testing this now....


---

Comment by cremona created at 2009-06-29 18:23:46

Testing on the same machine & build where I reported the problem (ububtu 32-bit):  I applied the patch and now there is no problem with testing graphs/graph.py, or sage/groups/perm_gps/partn_ref/refinement_graphs.pyx (the file patched).

So: positive reivew!


---

Comment by rlm created at 2009-06-29 20:43:05

Resolution: fixed
