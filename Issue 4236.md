# Issue 4236: magma -- boolean ring conversions

Issue created by migration from https://trac.sagemath.org/ticket/4236

Original creator: was

Original creation time: 2008-10-02 16:28:41

Assignee: was


```
1) This should work (?)

sage: B.<x,y> = BooleanPolynomialRing()
sage: B*[x*y + 1, x + y]
sage: I = B*[x*y + 1, x + y]
sage: I._magma_()

Ideal of Affine Algebra of rank 2 over GF(2)
Lexicographical Order
Variables: x, y
Quotient relations:
[
x^2 + x,
y^2 + y
]
Generating basis:
[
x*y + 1,
x + y
]

sage: Im = I._magma_()
sage: Im.GroebnerBasis()
TypeError: Error evaluation Magma code.
IN:_sage_[21] := GroebnerBasis(_sage_[20]);
OUT:
>> _sage_[21] := GroebnerBasis(_sage_[20]);
                             ^
Runtime error in 'GroebnerBasis': Bad argument types
Argument types given: RngMPolRes
```


Reported by Martin Albrecht


---

Comment by was created at 2008-10-02 16:29:57

Changing status from new to assigned.


---

Comment by was created at 2008-12-11 05:55:26

This does not seem like a bug in the Sage/Magma interface.  It seems like a misunderstanding of Magma itself, which doesn't have a GroebnerBasis function that takse as input an ideal in a boolean ring.  Magma simply doesn't do that.  It only has Groebner for ideals in *polynomial* rings.  There are some functions on ideals in boolean rings, but not many.  I.e., above

```
sage: Im.IsMaximal()
true
sage: Im.PrimaryDecomposition()

[
Affine Algebra of rank 2 over GF(2)
Lexicographical Order
Variables: x, y
Quotient relations:
[
x^2 + x,
y^2 + y
]
Generating basis:
[
x + 1,
y + 1
]
]
```



---

Comment by malb created at 2008-12-11 10:18:39

We could make Magma better than Magma by 
* adding the generators of the quotient to the ideal `J = I + Q`
* computing `gb := GroebnerBasis(J)`
* coerce the result to the quotient again. 

This is equivalent to computing the GB in the quotient directly.


---

Comment by AlexGhitza created at 2009-01-23 02:42:53

Changing type from defect to enhancement.


---

Comment by malb created at 2009-09-29 08:10:32

Resolution: fixed


---

Comment by malb created at 2009-09-29 08:10:32

This is fixed with #6177
