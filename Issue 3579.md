# Issue 3579: bug in RandonGNP graph constructor

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-07-07 00:37:28

Assignee: rlm


```
17:32 < itolkov> sage: graphs.RandomGNP(n=4, p=1)
17:32 < itolkov> Traceback ... OverflowError: math range error
17:32 < itolkov> bug?
17:34 < wstein-3576> nt necessarily.
17:35 < wstein-3576> the line lp=math.log(1.0-p) shows why it doesn't work.
17:35 < wstein-3576> The docs do not ban probability 1, so yes, it is a bug.
```



---

Attachment


---

Comment by rlm created at 2008-07-10 17:09:28

+1


---

Comment by mabshoff created at 2008-07-15 01:49:19

Resolution: fixed


---

Comment by mabshoff created at 2008-07-15 01:49:19

Merged in Sage 3.0.6.alpha0
