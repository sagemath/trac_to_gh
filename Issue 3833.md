# Issue 3833: [with patch; needs review] calculus -- fix bug in hashing of symbolic expressions

Issue created by migration from https://trac.sagemath.org/ticket/3833

Original creator: was

Original creation time: 2008-08-13 05:15:04

Assignee: gfurnish

This is stupid

```
sage: uniq([x-x, -x+x])
[0, 0]
```


This patch fixes this idiocy.

This was persisently reported by Rolandb.


---

Attachment


---

Comment by mabshoff created at 2008-08-13 06:29:48

Resolution: fixed


---

Comment by mabshoff created at 2008-08-13 06:29:48

Merged in Sage 3.1.alpha2
