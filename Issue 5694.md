# Issue 5694: [with patch; needs review] _ for previous output is completely broken in the notebook due to the preparser

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-04-06 18:05:33

Assignee: boothby

In the notebook we have the following confusing bug, which caused a lot of trouble during my last Sage tutorial:


```
sage: 2 + 3
5
sage: _
5
sage: f(x,y) = x+y
sage: 2 + 10
12
sage: _
(x, y)
```



---

Attachment


---

Comment by mabshoff created at 2009-04-06 22:21:43

I think this is critical enough to make it into 3.4.1. Reassigning.

Cheers,

Mihcael


---

Comment by mabshoff created at 2009-04-06 23:10:31

Merged in Sage 3.4.1.rc2.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-06 23:10:31

Resolution: fixed
