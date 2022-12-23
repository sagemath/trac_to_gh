# Issue 3673: [with patch, needs review]  NumberFieldElement

Issue created by migration from https://trac.sagemath.org/ticket/3673

Original creator: fwclarke

Original creation time: 2008-07-18 11:48:36

Assignee: was

The present definition of the `NumberFieldElement` class unreasonably 
privileges the polynomial variable 'x'.  As a result the following fails:

```
sage: y = polygen(QQ, 'y'); K.<a> = NumberField(y^2 - 2)
sage: S = K.subfields()
sage: S[0][1]
```

The patch amends the definition of `__init__` for the 
`NumberFieldElement` class to deal with this.

An extra doctest for the `subfields` method has been included.  Two other 
doctests have been adjusted to match the revised code.




---

Attachment


---

Comment by cremona created at 2008-08-10 13:18:17

The patch applies cleanly to 3.1.alpha0.  It does what it says, and all doctests in sage.rings.number_field pass.  Publish!


---

Comment by mabshoff created at 2008-08-11 07:37:40

Resolution: fixed


---

Comment by mabshoff created at 2008-08-11 07:37:40

Merged in Sage 3.1.alpha1


---

Comment by mabshoff created at 2008-08-11 07:40:00

By the way: Report 11 did not pick up this ticket since there is an extra space between "positive" and "review".

Cheers,

Michael
