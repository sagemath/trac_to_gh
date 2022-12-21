# Issue 3677: sage -t / sage -tp does not take into account the current directory

Issue created by migration from Trac.

Original creator: mhansen

Original creation time: 2008-07-19 01:48:02

Assignee: gfurnish

CC:  mhansen

At the end of testing when reporting the results, sage -t does not take into account the current directory.  It produces output like this:


```
	sage -t  devel/sage-combinat/sage/combinat/root_system/ambient_space.py
	sage -t  devel/sage-combinat/sage/combinat/root_system/root_lattice_realization.py
	sage -t  devel/sage-combinat/sage/combinat/root_system/root_space.py
	sage -t  devel/sage-combinat/sage/combinat/root_system/root_system.py
	sage -t  devel/sage-combinat/sage/combinat/root_system/weight_space.py
```


when it should be giving output like 


```
	sage -t  ambient_space.py
	sage -t  root_lattice_realization.py
	sage -t  root_space.py
	sage -t  root_system.py
	sage -t  weight_space.py
```


if I am in $SAGE_ROOT/devel/sage-combinat/sage/combinat/root_system .


---

Comment by gfurnish created at 2008-12-11 15:17:28

Changing status from new to assigned.


---

Attachment

This fixes this issue for sage -tp but not for sage -t.


---

Comment by gfurnish created at 2008-12-14 01:51:18

Is it possible to get this reviewed for 3.2.2?


---

Comment by gfurnish created at 2008-12-14 05:29:10

The "-t" case of this has been split to #4790


---

Comment by mabshoff created at 2008-12-14 05:38:00

Yep, this works Positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-12-14 05:38:18

Resolution: fixed


---

Comment by mabshoff created at 2008-12-14 05:38:18

Merged in Sage 3.2.2.rc0
