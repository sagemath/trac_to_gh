# Issue 2214: DSage and memory leaks

Issue created by migration from Trac.

Original creator: robertwb

Original creation time: 2008-02-19 22:05:09

Assignee: yi

If a job has a memory leak, it is not reclaimed when the worker resets itself. If the memory after reset does not go down to "normal" (or, say, twice normal) then it should warn the user that the job leaked memory and actually restart the worker. 




---

Comment by yi created at 2008-02-29 06:48:02

Changing status from new to assigned.


---

Comment by yi created at 2008-02-29 06:48:02

This will be fixed once #2322 gets merged.


---

Comment by yi created at 2008-03-24 16:45:16

This bug has been fixed in 2.10.4, please close it.


---

Comment by mabshoff created at 2008-03-24 16:49:35

Resolution: fixed


---

Comment by mabshoff created at 2008-03-24 16:49:35

Fixed in Sage 2.10.4 according to Yi, so close this.
