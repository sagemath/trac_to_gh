# Issue 5785: bug in norm of vectors over CDF

Issue created by migration from Trac.

Original creator: ncalexan

Original creation time: 2009-04-14 15:55:27

Assignee: was

Keywords: CDF vector norm


```
sage: v = vector(CDF, [2, 2])
sage: v - v
(0, 0)
sage: (v - v).norm()
nan
sage: v = vector(CC, [2, 2])
sage: (v - v).norm()
0.000000000000000
```



---

Comment by jason created at 2009-04-15 05:51:13

Changing assignee from was to somebody.


---

Comment by jason created at 2009-04-15 05:51:13

The problem is this:


```
sage: RDF(0)^(1/2)
NaN
```



---

Comment by jason created at 2009-04-15 05:51:13

Changing component from linear algebra to basic arithmetic.


---

Comment by jason created at 2009-04-16 17:33:49

Does #5782 fix this?


---

Attachment

Added a doctest.


---

Comment by mabshoff created at 2009-04-16 21:19:50

Replying to [comment:2 jason]:
> Does #5782 fix this?

It looks like the same bug, having a doctest added ought to be enough to close this ticket once it is merged.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-18 00:55:44

Positive review. I changed the double colon after AUTHORS to a single colon. 

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-18 00:56:07

Resolution: fixed


---

Comment by mabshoff created at 2009-04-18 00:56:07

Merged in Sage 3.4.1.rc4.

Cheers,

Michael
