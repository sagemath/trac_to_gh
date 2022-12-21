# Issue 2497: crash in polynomial remainder

Issue created by migration from Trac.

Original creator: dmharvey

Original creation time: 2008-03-12 16:15:01

Assignee: somebody


```
sage: R.<x> = PolynomialRing(Integers(4))
sage: f = x^2 + 3
sage: f % 2
InvMod: inverse undefined
/Users/david/sage/local/bin/sage-sage: line 222: 11351 Abort trap              sage-ipython "$`@`" -c "$SAGE_STARTUP_COMMAND;"
```


This is an NTL error message, which is not being trapped or something.



---

Comment by dfdeshom created at 2008-03-14 03:39:03

This also happens in `__florrdiv__(), quo_rem()`


---

Attachment


---

Comment by mabshoff created at 2008-04-07 03:44:17

#2592 seems related and is not fixed by this patch.

Cheers,

Michael


---

Comment by mabshoff created at 2008-04-07 03:45:07

The patch fixes the issue, adds a doctest for the crash and passes doctests. Positive review.

Cheers,

Michaek


---

Comment by mabshoff created at 2008-04-07 03:46:51

Merged in Sage 3.0.alpha2


---

Comment by mabshoff created at 2008-04-07 03:46:51

Resolution: fixed
