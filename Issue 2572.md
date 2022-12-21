# Issue 2572: imag() not defined for Algebraic Real Field

Issue created by migration from Trac.

Original creator: ncalexan

Original creation time: 2008-03-17 17:29:07

Assignee: malb

CC:  ncalexan

Keywords: imag algebraic reals

This makes it hard to write generic code:


```
sage: L, (_, a), L_into_A = number_field_elements_from_algebraics([sqrt(2), sqrt(-2 + sqrt(2))*I], minimal=True)
sage: L_into_A

Ring morphism:
  From: Number Field in a with defining polynomial y^4 - 4*y^2 + 2
  To:   Algebraic Real Field
  Defn: a |--> [-0.76536686473017957 .. -0.76536686473017945]
sage: L_into_A(a)
[-0.76536686473017957 .. -0.76536686473017945]
sage: L_into_A(a).imag()
---------------------------------------------------------------------------
<type 'exceptions.AttributeError'>        Traceback (most recent call last)

/Users/ncalexan/Documents/School/MATH235/genus2cm/<ipython console> in <module>()

<type 'exceptions.AttributeError'>: 'AlgebraicReal' object has no attribute 'imag'
sage: L, (z, ), L_into_A = number_field_elements_from_algebraics([QQbar.zeta(5)], minimal=True)
sage: L_into_A

Ring morphism:
  From: Cyclotomic Field of order 5 and degree 4
  To:   Algebraic Field
  Defn: zeta5 |--> [0.30901699437494739 .. 0.30901699437494746] + [0.95105651629515353 .. 0.95105651629515365]*I
sage: L_into_A(z)
[0.30901699437494739 .. 0.30901699437494746] + [0.95105651629515353 .. 0.95105651629515365]*I
sage: L_into_A(z).imag()
[0.95105651629515353 .. 0.95105651629515365]
```



---

Comment by cwitty created at 2008-03-17 21:16:46

Changing status from new to assigned.


---

Comment by cwitty created at 2008-03-17 21:16:46

Changing assignee from malb to cwitty.


---

Attachment

The attached patch adds the requested method (and .real() as well).  Doctests pass in sage/rings.


---

Comment by AlexGhitza created at 2008-03-20 01:43:44

Looks good.


---

Comment by mabshoff created at 2008-03-22 04:03:38

Resolution: fixed


---

Comment by mabshoff created at 2008-03-22 04:03:38

Merged in Sage 2.11.alpha1
