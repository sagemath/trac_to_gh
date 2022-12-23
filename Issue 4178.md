# Issue 4178: dist_functions.py doctest timeout is too small

Issue created by migration from https://trac.sagemath.org/ticket/4178

Original creator: GeorgSWeber

Original creation time: 2008-09-23 21:58:17

Assignee: GeorgSWeber

On my PPC Power Book 550 MHz, 768 MB RAM, Mac OS X 10.4.11, Xcode 2.5, the "long" doctest fails because the timeout is too small.

As soon as I have checked how big it should be (on that box) to make it run through, I'll add the info here. 


---

Comment by GeorgSWeber created at 2008-09-23 21:58:47

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-09-23 22:04:21

Resolution: wontfix


---

Comment by mabshoff created at 2008-09-23 22:04:21

Nope, this is a won't fix. The long timeout is *huge*, i.e. 30 minutes. The problem is another one, i.e. ecm not returning and hence the doctest never finishes. This issue is already covered by another DSage ticket.

Cheers,

Michael
