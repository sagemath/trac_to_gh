# Issue 935: remove no longer present files from the sage repo

Issue created by migration from https://trac.sagemath.org/ticket/935

Original creator: mabshoff

Original creation time: 2007-10-19 22:56:39

Assignee: was

Well, the title says it all. Patch is against 2.8.7.

Cheers,

Michael


---

Attachment


---

Comment by mabshoff created at 2007-10-20 06:14:32

Changing assignee from was to mabshoff.


---

Comment by mabshoff created at 2007-10-20 06:14:32

Changing status from new to assigned.


---

Comment by mabshoff created at 2007-10-20 19:25:55


```
[21:20] <wstein> #935 -- reject.
[21:20] <mabshoff> Why?
[21:20] <wstein> Those files *should* be in sage.
[21:20] <mabshoff> So why aren't they in the repo?
[21:20] <wstein> probably they didn't get included because of a mistake in MANIFEST.in.
[21:20] <mabshoff> ok
[21:21] <mabshoff> So mark #935 as invalid?
[21:21] <wstein> at least the one that doctests cvxopt, scipy, definitely should be remade.
[21:21] <mabshoff> That is another ticket.
[21:21] <wstein> It's not invalid, it's just that the fix isn't exactly right.
```



---

Comment by was created at 2007-10-21 01:05:39

Resolution: invalid


---

Comment by cwitty created at 2007-10-28 16:07:51

Resolution changed from invalid to 


---

Comment by cwitty created at 2007-10-28 16:07:51

Changing status from closed to reopened.


---

Comment by cwitty created at 2007-10-28 16:07:56

Changing status from reopened to new.


---

Comment by cwitty created at 2007-10-28 16:07:56

Changing assignee from mabshoff to cwitty.


---

Attachment


---

Comment by cwitty created at 2007-10-28 17:49:38

I think the attached patch should fix this problem.  (I will close the ticket once I have actually built a distribution and checked that it worked.)


---

Comment by cwitty created at 2007-10-28 21:40:17

Resolution: fixed
