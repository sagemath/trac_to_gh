# Issue 5118: [with patch, needs review] Improve elliptic curve printing

Issue created by migration from Trac.

Original creator: rlm

Original creation time: 2009-01-28 19:05:22

Assignee: was

CC:  cremona

Before:

```
Elliptic Curve defined by y^2  = x^3 + x +1 ...
```


After:

```
Elliptic Curve defined by y^2 = x^3 + x + 1 ...
```



---

Attachment

Passes doctests and makes the printing consistent regarding spaces. Positive review. 

I am CCing John since he might be affected by this patch.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-02 05:53:43

Resolution: fixed


---

Comment by mabshoff created at 2009-02-02 05:53:43

Merged in Sage 3.3.alpha4.

Cheers,

Michael
