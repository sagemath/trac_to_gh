# Issue 5316: some elements of NumberField_quadratic are NumberFieldElement_absolute --> segfault

Issue created by migration from Trac.

Original creator: cwitty

Original creation time: 2009-02-20 06:15:51

Assignee: cwitty

Based on a question from Alex Raichev (http://groups.google.com/group/sage-support/browse_thread/thread/71483789bc7fefb7#), I discovered this:

```
sage: var('t')
t
sage: F = NumberField(t^2+1, 'a')
sage: R.<x,y> = F[]
sage: type(x.coefficients()[0])
<type 'sage.rings.number_field.number_field_element.NumberFieldElement_absolute'>
sage: F(1) + x.coefficients()[0]


------------------------------------------------------------
Unhandled SIGSEGV: A segmentation fault occured in SAGE.
This probably occured because a *compiled* component
of SAGE has a bug in it (typically accessing invalid memory)
or is not properly wrapped with _sig_on, _sig_off.
You might want to run SAGE under gdb with 'sage -gdb' to debug this.
SAGE will now terminate (sorry).
------------------------------------------------------------
```



---

Attachment


---

Comment by cwitty created at 2009-02-20 07:03:52

The attached patch fixes the crash (and also fixes Alex's original problem.)  All doctests pass.


---

Comment by was created at 2009-02-20 07:11:07

If this passes doctests then I give it a positive review.


---

Comment by mabshoff created at 2009-02-20 07:58:15

Positive review via William's review since all doctests pass.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-20 07:58:34

Resolution: fixed


---

Comment by mabshoff created at 2009-02-20 07:58:34

Merged in Sage 3.3.rc3.

Cheers,

Michael
