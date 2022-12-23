# Issue 6366: lift method on elements of residue class field is broken / not implemented as it should be

Issue created by migration from https://trac.sagemath.org/ticket/6366

Original creator: was

Original creation time: 2009-06-20 15:14:45

Assignee: was


```
sage: K.<a> = NumberField(x^2 + 3)
sage: P = K.factor(5)[0][0]; P
Fractional ideal (5)
sage: F = P.residue_field()
sage: z = F.gen() + 2; z
abar + 2
sage: F.lift(z)
6*a + 2
sage: z.lift()
Traceback (most recent call last):
...
AttributeError: 'sage.rings.finite_field_givaro.FiniteField_givaroE' object has no attribute 'lift'
```



---

Comment by davidloeffler created at 2009-07-21 08:20:05

Changing component from number theory to number fields.


---

Comment by davidloeffler created at 2009-07-21 08:20:05

Changing assignee from was to davidloeffler.
