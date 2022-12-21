# Issue 6062: [with patch; needs review] QQ method is_padic_square fails when argument is python int

Issue created by migration from Trac.

Original creator: tornaria

Original creation time: 2009-05-18 05:08:40

Assignee: tornaria

With sage-4.0.alpha0:

```
sage: QQ(5).is_padic_square(int(2))
...
AttributeError: 'int' object has no attribute 'is_prime'
```



---

Comment by tornaria created at 2009-05-18 05:15:53

allow python int argument in is_padic_square


---

Attachment

Note: this is needed to fix doctests in quadratic forms (#5954, #6037, #6040).


---

Comment by tornaria created at 2009-05-18 05:33:08

Note: the added doctest requires the patch in #6064 to pass.


---

Comment by cremona created at 2009-05-18 21:18:42

Joint review with #6064: applied both patches, both are fine and tests pass.


---

Comment by mabshoff created at 2009-05-19 00:42:39

Resolution: fixed


---

Comment by mabshoff created at 2009-05-19 00:42:39

Merged iN Sage 4.0.rc0.

Cheers,

Michael
