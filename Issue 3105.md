# Issue 3105: [with patch, needs review]  new  _latex_  and modified  __repr__  for elements of relative number fields

Issue created by migration from https://trac.sagemath.org/ticket/3105

Original creator: mabshoff

Original creation time: 2008-05-05 12:56:27

Assignee: was

CC:  f.clarke@swansea.ac.uk

Patch by Francis Clarke. He should fill in the details once his new trac account works.

Cheers,

Michael


---

Attachment

This patch appliesw fine to 3.0.1 and the doctests in sage/rings/number_field all pass.

It looks fine to me.


---

Comment by mabshoff created at 2008-05-05 20:35:18

Merged in Sage 3.0.2.alpha0


---

Comment by mabshoff created at 2008-05-05 20:35:18

Resolution: fixed


---

Comment by fwclarke created at 2008-05-06 09:13:05

Changing status from closed to reopened.


---

Comment by fwclarke created at 2008-05-06 09:13:05

Resolution changed from fixed to 


---

Comment by fwclarke created at 2008-05-06 09:37:21


```
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 3.0, Release Date: 2008-04-21                         |
| Type notebook() for the GUI, and license() for information.        |
sage: A.<a> = CyclotomicField(3)
sage: P.<x> = PolynomialRing(A)
sage: B.<b> = NumberField(x^2 - 5)
sage: (a + b)^2
2*a*b - a + 4
sage: latex((a + b)^2)
\frac{4}{23} b^{3} - \frac{29}{23} b^{2} - \frac{8}{23} b + \frac{212}{23}
```


This is clearly wrong.  What is happening is the element is being 
represented in the absolute number field, but using the variable 
appropriate to the relative field:


```
sage: C.<c> = B.absolute_field()
sage: from_abs, to_abs = C.structure()
sage: to_abs((a + b)^2)
4/23*c^3 - 29/23*c^2 - 8/23*c + 212/23
sage: latex(to_abs((a + b)^2))
\frac{4}{23} c^{3} - \frac{29}{23} c^{2} - \frac{8}{23} c + \frac{212}{23}
```


The patch below fixes this by providing a  _latex_  function for elements of 
relative number fields.

It also simplifies  !__repr!__  for such elements slightly.


---

Comment by fwclarke created at 2008-05-06 09:37:21

Resolution: fixed
