# Issue 6923: Matrix numerical approximation converts complex to real

Issue created by migration from https://trac.sagemath.org/ticket/6923

Original creator: Henryk.Trappmann

Original creation time: 2009-09-11 06:40:08

Assignee: tbd

sage: A = Matrix(CC,3); A.parent()
Full MatrixSpace of 3 by 3 dense matrices over Complex Field with 53 bits of precision
sage: B = A.n(20); B.parent()
Full MatrixSpace of 3 by 3 dense matrices over Real Field with 20 bits of precision

IMHO .n() only should change the precision, no other conversion.
This is also the behaviour of .n() on ComplexField.


---

Comment by AlexGhitza created at 2009-11-15 13:09:31

Changing component from algebra to linear algebra.


---

Comment by jhonrubia6 created at 2016-05-30 10:12:30

The problem being that

```
return self.change_ring(sage.rings.real_mpfr.RealField(prec))
```

doesn't raise an error since it can coerce the motivating matrix to Real. should we avoid coercion, maybe using type checking ?
