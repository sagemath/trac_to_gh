# Issue 4727: list method on relative number field elements is broken -- it doesn't satisfy the most basic consistency check

Issue created by migration from https://trac.sagemath.org/ticket/4727

Original creator: was

Original creation time: 2008-12-06 18:45:19

Assignee: was

What the heck is this?

```
sage: K.<j,b> = QQ[sqrt(-1), sqrt(2)]
sage: j
I
sage: K(j.list())
I - sqrt2
```



---

Comment by ncalexan created at 2009-01-24 09:31:30

The patches for #1367 fix and doctest this.  It should be closed as fixed after #1367 is merged.


---

Comment by mabshoff created at 2009-01-29 05:44:48

Fixed via #1367 in Sage 3.3.alpha3.

Cheers,

Michael


---

Comment by mabshoff created at 2009-01-29 05:44:48

Resolution: fixed
