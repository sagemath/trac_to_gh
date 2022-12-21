# Issue 280: Extensions should coerce defining polynomials into base fields

Issue created by migration from Trac.

Original creator: ncalexan

Original creation time: 2007-02-23 19:56:45

Assignee: somebody

Keywords: extension base field polynomial

Clearly ZZ['x'] coerces into K['x'], so this should not be an error.


```
sage:K.<a> = NumberField(ZZ['x'].0^3 - 5)

sage: L.<b> = K.extension(ZZ['x'].0^2 - 3)
---------------------------------------------------------------------------
<type 'exceptions.ValueError'>            Traceback (most recent call last)
...
    821         if polynomial.parent().base_ring() != base:
--> 822             raise ValueError, "The polynomial must be defined over the base field"
    823 
    824         # Generate the nf and bnf corresponding to the base field

<type 'exceptions.ValueError'>: The polynomial must be defined over the base field
```



---

Comment by was created at 2007-02-24 03:03:24

Changing assignee from somebody to ncalexan.


---

Comment by dmharvey created at 2007-12-01 14:57:06

Resolution: fixed


---

Comment by dmharvey created at 2007-12-01 14:57:06

This seems to work now:


```
sage: K.<a> = NumberField(ZZ['x'].0^3 - 5)
sage: L.<b> = K.extension(ZZ['x'].0^2 - 3)
sage: L
Number Field in b with defining polynomial x^2 - 3 over its base field
sage: L.polynomial()
x^2 - 3
sage: L.polynomial().parent()
Univariate Polynomial Ring in x over Number Field in a with defining polynomial x^3 - 5
```

