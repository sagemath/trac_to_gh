# Issue 1774: potential very serious problems with SEA and PARI-2.3.3

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-01-14 06:14:31

Assignee: was

I just received this off-list from Bill Alombert:


```
As you much probably already now, we released PARI/GP 2.3.3 in December.

Furthermore, I started to review the GP script for SEA and we fixed
several problems that could lead to wrong results being returned,
so I would suggest you update the copy in SAGE to the current CVS
version of SEA.
```



---

Comment by was created at 2008-01-15 15:56:59

Changing status from new to assigned.


---

Comment by was created at 2008-01-15 16:36:06

The patch is at:

http://sage.math.washington.edu/home/was/tmp/extcode-trac-1774.patch


---

Comment by was created at 2008-01-15 16:36:06

Changing priority from critical to blocker.


---

Comment by was created at 2008-01-15 16:37:25

Also, make very clear that the credit for this update goes to Bill Allombert!!


---

Comment by mabshoff created at 2008-01-15 19:46:26

Resolution: fixed


---

Comment by mabshoff created at 2008-01-15 19:46:26

Merged in Sage 2.10.alpha4
