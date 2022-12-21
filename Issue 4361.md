# Issue 4361: [with patch, needs review] poles of gamma on integers

Issue created by migration from Trac.

Original creator: burcin

Original creation time: 2008-10-24 09:50:25

Assignee: burcin

In 3.1.4 we have:


```
sage: gamma(-1)
+Infinity
sage: gamma(-2)
-Infinity
```


The poles should return unsigned infinity.


---

Attachment


---

Comment by mabshoff created at 2008-10-31 01:33:06

Merged in Sage 3.2.alpha2


---

Comment by mabshoff created at 2008-10-31 01:33:06

Resolution: fixed
