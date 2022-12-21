# Issue 3963: [with patch, needs review] bug in converting Sage's rationals to Sympy rationals

Issue created by migration from Trac.

Original creator: mhansen

Original creation time: 2008-08-27 00:52:43

Assignee: was


```
from sympy import Symbol
QQ(1)+Symbol('x')*QQ(2)

produces an error:

TypeError                                 Traceback (most recent call
last)

/Applications/sage/<ipython console> in <module>()

/Applications/sage/element.pyx in
sage.structure.element.ModuleElement.__add__ (sage/structure/element.c:
5606)()

/Applications/sage/coerce.pyx in
sage.structure.coerce.CoercionModel_cache_maps.bin_op (sage/structure/
coerce.c:6288)()

TypeError: unsupported operand parent(s) for '+': 'Rational Field' and
'<class 'sympy.core.mul.Mul'>'
```



---

Attachment


---

Comment by mabshoff created at 2008-08-27 00:54:37

Positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-08-27 00:57:21

Resolution: fixed


---

Comment by mabshoff created at 2008-08-27 00:57:21

Merged in Sage 3.1.2.alpha1
