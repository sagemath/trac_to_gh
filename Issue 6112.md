# Issue 6112: Remove stale file sage/graphs/graph_isom.pyx

Issue created by migration from Trac.

Original creator: rlm

Original creation time: 2009-05-21 15:03:48

Assignee: rlm

This file has been superseded by those in `sage/groups/perm_gps/partn_ref`. I think its time has come.


---

Attachment


---

Comment by ddrake created at 2009-06-16 02:25:41

Changing assignee from rlm to ddrake.


---

Comment by ddrake created at 2009-06-16 02:25:41

Changing status from new to assigned.


---

Comment by ddrake created at 2009-06-16 02:25:41

I don't know much about the graphs code, but I definitely can produce a patch which deletes a file. rlm, can you review?


---

Comment by ddrake created at 2009-06-16 02:33:44

Wait, that was stupid...you can't just remove a file and expect things that use that file to figure out what to do...! Needs work.


---

Comment by rlm created at 2009-06-16 04:01:57

I'll take care of this -- I'm currently in the middle of overhauling graphs, and this is on my list.


---

Attachment


---

Comment by rlm created at 2009-06-21 22:13:56

After deleting `graph_isom.so` and testing all of sage with `-long`, all is well.

The last test will be to actually roll an alpha and make sure everything still works, although I'm guessing all should be fine.


---

Comment by rlm created at 2009-06-24 09:58:25

Resolution: fixed
