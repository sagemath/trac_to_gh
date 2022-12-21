# Issue 5928: multiplication of factorisations should coerce factors into a common universe

Issue created by migration from Trac.

Original creator: AlexGhitza

Original creation time: 2009-04-29 01:43:08

Assignee: AlexGhitza

CC:  cremona

Keywords: multiplication factorization coercion

This was uncovered at #5921.  Observe:


```
sage: P.<x> = ZZ
sage: f = 2*x + 2
sage: c = f.content()
sage: g = f//c
sage: F1 = c.factor(); [type(a[0]) for a in F1]
[<type 'sage.rings.integer.Integer'>]
sage: F2 = g.factor(); [type(a[0]) for a in F2]
[<type 'sage.rings.polynomial.polynomial_integer_dense_flint.Polynomial_integer_dense_flint'>]
sage: F1*F2
2 * (x + 1)
sage: [type(a[0]) for a in F1*F2]
[<type 'sage.rings.integer.Integer'>,
 <type 'sage.rings.polynomial.polynomial_integer_dense_flint.Polynomial_integer_dense_flint'>]
```


I think that multiplying two factorisations should make sure that the factors can be coerced into a common universe, so that all factors have the same parent.  If that's impossible, then an error should be thrown.



---

Comment by AlexGhitza created at 2009-04-29 05:50:09

The attached patch does this for multiplication, gcd, and lcm.  The other operations either inherit it or were dealing with this already.


---

Comment by AlexGhitza created at 2009-04-29 05:50:09

Changing status from new to assigned.


---

Attachment

This patch looks good, applies to 3.4.2.alpha0 and tests in sage/structure pass as well as those in sage/rings/*.py (I did not go into subdirectories).

I was a little disappointed by this:

```
sage: R.<x> = ZZ[]
sage: S.<y> = QQ[]
sage: f = x^2-1
sage: g = y^3-1
sage: f.factor()
(x - 1) * (x + 1)
sage: g.factor()
(y - 1) * (y^2 + y + 1)
sage: f.factor() * g.factor()
(1) * (y - 1) * (x - 1) * (x + 1) * (y^2 + y + 1)
sage: (f.factor() * g.factor()).universe()
Category of objects
```

and in fact coercion is not clever enough to allow x*y here.  but it does work if you do 

```
sage: S.<x> = QQ[]
sage: y=S.gen(0)
sage: g = y^3-1
sage: f.factor() * g.factor()
(x + 1) * (x - 1)^2 * (x^2 + x + 1)
```

-- i.e. you have to define the two rings with the same name of the variable even if you use a different name for input.  Weird, but it is not going to stop this patch!


---

Comment by mabshoff created at 2009-04-30 06:01:28

Merged in Sage 3.4.2.rc0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-30 06:01:28

Resolution: fixed
