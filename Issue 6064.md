# Issue 6064: allow rationals in kronecker_symbol and legendre_symbol

Issue created by migration from Trac.

Original creator: tornaria

Original creation time: 2009-05-18 05:30:08

Assignee: tornaria

With sage-4.0.alpha0:

```
sage: kronecker(2/3,7)
...
TypeError: no conversion of this rational to integer
```

Same for `kronecker_symbol` and `legendre_symbol`. However, it does make sense for these to be defined on rationals.

This is actually used by `is_padic_square` when used with rationals, and triggered by some of the new quadratic form doctests.


---

Comment by tornaria created at 2009-05-18 05:35:10

Note: this is needed to fix doctests in quadratic forms (#5954, #6037, #6040).


---

Attachment

allow rationals in kronecker_symbol and legendre_symbol


---

Comment by cremona created at 2009-05-18 21:18:02

Joint review with #6062:  applied both patches, both are fine and tests pass.


---

Comment by mabshoff created at 2009-05-19 00:42:59

Merged in Sage 4.0.rc0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-05-19 00:42:59

Resolution: fixed
