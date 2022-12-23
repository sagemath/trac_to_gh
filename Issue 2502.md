# Issue 2502: [with patch, needs review] doctest coverage for finite fields

Issue created by migration from https://trac.sagemath.org/ticket/2502

Original creator: malb

Original creation time: 2008-03-12 19:02:32

Assignee: failure

*Before patch:*

```
----------------------------------------------------------------------
finite_field_givaro.pyx
SCORE finite_field_givaro.pyx: 100% (61 of 61)
----------------------------------------------------------------------

----------------------------------------------------------------------
finite_field_ntl_gf2e.pyx
ERROR: Please define a s == loads(dumps(s)) doctest.
SCORE finite_field_ntl_gf2e.pyx: 64% (25 of 39)

Missing documentation:
         * __init__(FiniteField_ntl_gf2e self, q, names="a", modulus=None, repr="poly")
         * __richcmp__(left, right, int op)
         * _pari_(self, var=None)
         * unpickleFiniteField_ntl_gf2eElement(parent, elem)


Missing doctests:
         * __neg__(FiniteField_ntl_gf2eElement self)
         * __invert__(FiniteField_ntl_gf2eElement self)
         * polynomial(FiniteField_ntl_gf2eElement self, name=None)
         * _finite_field_ext_pari_element(FiniteField_ntl_gf2eElement self, k=None)
         * _magma_init_(self)
         * __copy__(self)
         * _gap_init_(self)
         * __hash__(FiniteField_ntl_gf2eElement self)
         * vector(FiniteField_ntl_gf2eElement self, reverse=False)
         * __reduce__(FiniteField_ntl_gf2eElement self)

----------------------------------------------------------------------

----------------------------------------------------------------------
finite_field_prime_modn.py
ERROR: Please define a s == loads(dumps(s)) doctest.
SCORE finite_field_prime_modn.py: 91% (11 of 12)

Missing doctests:
         * polynomial(self, name=None)

----------------------------------------------------------------------

----------------------------------------------------------------------
finite_field.py
ERROR: Please define a s == loads(dumps(s)) doctest.
SCORE finite_field.py: 100% (4 of 4)
----------------------------------------------------------------------
```


*After patch:*


```
----------------------------------------------------------------------
finite_field_ext_pari.py
SCORE finite_field_ext_pari.py: 100% (14 of 14)
----------------------------------------------------------------------

----------------------------------------------------------------------
finite_field_givaro.pyx
SCORE finite_field_givaro.pyx: 100% (61 of 61)
----------------------------------------------------------------------

----------------------------------------------------------------------
finite_field_ntl_gf2e.pyx
SCORE finite_field_ntl_gf2e.pyx: 100% (39 of 39)
----------------------------------------------------------------------

----------------------------------------------------------------------
finite_field_prime_modn.py
SCORE finite_field_prime_modn.py: 100% (12 of 12)
----------------------------------------------------------------------

----------------------------------------------------------------------
finite_field.py
ERROR: Please define a s == loads(dumps(s)) doctest.
SCORE finite_field.py: 100% (4 of 4)
----------------------------------------------------------------------
```


Note that the last "Please define a s == loads(dumps(s)) doctest." is wrong. There is no class defined in `finite_field.py`.




---

Attachment

note that finite_field_element.py is not addressed in this patch


---

Comment by jsp created at 2008-03-14 16:09:05

Works for me. All test passed.

No surprises in the code.

Jaap


---

Comment by mabshoff created at 2008-03-15 19:30:01

Merged in Sage 2.10.4.rc0


---

Comment by mabshoff created at 2008-03-15 19:30:01

Resolution: fixed
