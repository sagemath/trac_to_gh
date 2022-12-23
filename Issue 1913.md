# Issue 1913: poles of gamma

Issue created by migration from https://trac.sagemath.org/ticket/1913

Original creator: burcin

Original creation time: 2008-01-24 16:37:15

Assignee: burcin

Sage cannot handle poles of the gamma function. For negative integers and 0, the result of `gamma(x)` should be unsigned infinity.


---

Attachment

make gamma return Infinity for 0, -1, ...


---

Comment by burcin created at 2008-01-25 08:48:08

attachment:1913-gamma_poles.patch makes sage.rings.complex_number.ComplexNumber.gamma return Infinity for 0 and negative integers.


---

Comment by burcin created at 2008-01-25 08:48:08

Changing status from new to assigned.


---

Comment by was created at 2008-01-25 13:50:21

Works fine for me.   Seems like a reasonable thing to do for now; definitely better than the current behavior.  (Though our infinity in Sage maybe isn't optimal for this sort of application...)


---

Comment by mabshoff created at 2008-01-25 17:26:35

Resolution: fixed


---

Comment by mabshoff created at 2008-01-25 17:26:35

Merged in Sage 2.10.1.alpha2
