# Issue 2236: plot randomizes the endpoints of the interval and causes wiggling in the graph

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2008-02-20 22:39:42

Assignee: was


p=plot(x, (x,-1,1))
p[0][0] == -1
p[0][-1] == 1

They will almost always return false before the patch.  After the patch, the two statements should return True always.


---

Comment by was created at 2008-02-20 22:43:32

I agree with the suggestion to *not* randomize the endpoints.  That's bad.


---

Attachment


---

Comment by mabshoff created at 2008-02-20 23:05:01

Merged in Sage 2.10.2.alpha2


---

Comment by mabshoff created at 2008-02-20 23:05:01

Resolution: fixed


---

Comment by jason created at 2008-02-20 23:05:58

For the record, on IRC:

[16:55] <wstein> #2236 -- positive review.
