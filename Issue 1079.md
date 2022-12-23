# Issue 1079: DSage improper get_worker_count

Issue created by migration from https://trac.sagemath.org/ticket/1079

Original creator: jvoight

Original creation time: 2007-11-03 17:11:50

Assignee: was

When I do D.get_worker_count(), it always tells me that I have 2 workers--even though I have 30 machines connected each with 2 workers so the answer should be 30*2 = 60.  It works OK if I have only one DSage login with, say, 12 workers.



---

Comment by yi created at 2007-11-03 17:48:53

Changing assignee from was to yi.


---

Comment by yi created at 2007-11-03 20:23:09

Resolution: fixed


---

Comment by yi created at 2007-11-03 20:23:09

Fixed.  Get bundle here:
http://sage.math.washington.edu/home/yqiang/dsage.hg


---

Comment by yi created at 2007-11-03 20:28:33

Reopening


---

Comment by yi created at 2007-11-03 20:28:33

Resolution changed from fixed to 


---

Comment by yi created at 2007-11-03 20:28:33

Changing status from closed to reopened.


---

Comment by mabshoff created at 2007-11-06 21:59:37

Resolution: fixed


---

Comment by mabshoff created at 2007-11-06 21:59:37

applied to 2.8.12.rc0
