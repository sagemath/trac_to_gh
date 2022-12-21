# Issue 5944: fix a nasty pynac bug in exp

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-04-29 22:59:30

Assignee: burcin

CC:  mhansen


```
sage: t = var('t', ns=1)
sage: a = (-2*t).exp(); a
e^(-2*t)
sage: b = (-t).exp(); b
e^(-t)
sage: a - b
0
sage: a
e^(-t)
sage: b
e^(-t)
```



---

Comment by burcin created at 2009-05-05 23:20:45

add doctests for the fix


---

Attachment

The package for pynac 0.1.6 at #5777 has a fix for this. Attached patch adds doctests.


---

Comment by burcin created at 2009-05-05 23:22:20

Changing status from new to assigned.


---

Comment by mabshoff created at 2009-05-20 23:42:27

Positive review due to symbolics getting a positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2009-05-20 23:47:28

Merged in Sage 4.0.rc0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-05-20 23:47:28

Resolution: fixed
