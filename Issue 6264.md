# Issue 6264: ReST bug introduced by #5452 (missing '::' before a sage block)

Issue created by migration from Trac.

Original creator: slabbe

Original creation time: 2009-06-12 03:39:58

Assignee: slabbe

The patch I proposed to solve #5452 (merged in 3.4.1) introduced a tiny ReST bug in sage/graphs/graph.py. A single '::' is missing before a sage block. 


---

Comment by slabbe created at 2009-06-12 03:47:59

Changing status from new to assigned.


---

Comment by slabbe created at 2009-06-12 04:04:14

This patch applies cleanly on sage-4.0 and is part of the sage-combinat tree.


---

Attachment

I just reloaded the patch. There was a similar ReST problem a few lines above in the same file.


---

Comment by jhpalmieri created at 2009-06-12 16:26:36

Looks in the reference manual, all tests pass.


---

Comment by ncalexan created at 2009-06-13 23:02:52

Resolution: fixed
