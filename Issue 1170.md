# Issue 1170: Behaviour of the order function for infinite groups

Issue created by migration from Trac.

Original creator: ljpk

Original creation time: 2007-11-14 15:02:07

Assignee: was

When one tries to use the order function on group elements of infinite order, one gets an error:

gl=GL(2,ZZ)
g=gl.gens()[2]
g.order()

In MAGMA, one (often) gets the answer 0 if one calls the Order function on elements of infinite order.


---

Attachment


---

Comment by cremona created at 2008-09-04 15:43:46

The patch fixes this:  for consistency with other groups, +Infinity is returned as the order for group elements of infinite order.  A doctest has been added.

The patch should apply to 3.1.2.alpha4 and later, and all doctests in sage.groups pass.

Review, Lloyd?


---

Comment by mabshoff created at 2008-09-04 22:58:15

One small nitpick which I corrected in the patch I applied: The `#` in the doctests need to be escaped, i.e.

```
See trac \#1170
```

I am not sure if this applies in case the docstring is not raw, but let's do it so that downroad we do not get bitten by it.

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-04 23:22:38

Merged in Sage 3.1.2.rc0


---

Comment by mabshoff created at 2008-09-04 23:22:38

Resolution: fixed
