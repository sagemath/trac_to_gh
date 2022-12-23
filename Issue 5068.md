# Issue 5068: change_ring fails for polynomials over finite fields in many cases

Issue created by migration from https://trac.sagemath.org/ticket/5068

Original creator: was

Original creation time: 2009-01-23 10:38:14

Assignee: robertwb


```
sage: R.<x> = GF(9,'a')[]
sage: x.change_ring(GF(3))
BOOM!

sage: R.<x,y> = GF(9,'a')[]
sage: x.change_ring(GF(3))
BOOM!
TypeError: unable to coerce <type 'sage.rings.finite_field_givaro.FiniteField_givaroElement'> to an integer
```



---

Comment by was created at 2009-01-23 11:00:13

The generic MPolynomial_polydict poly's work fine as looking at the code shows, but the libsingular ones break:

```
sage: p = next_prime(10^30); f = GF(p^2,'a')['x,y'].gen()
sage: type(f)
<class 'sage.rings.polynomial.multi_polynomial_element.MPolynomial_polydict'>
sage: f.change_ring(GF(p))
x
sage: p = next_prime(20); f = GF(p^2,'a')['x,y'].gen()
sage: type(f)
<type 'sage.rings.polynomial.multi_polynomial_libsingular.MPolynomial_libsingular'>
sage: f.change_ring(GF(p))
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/Users/wstein/.sage/temp/teragon.local/22907/_Users_wstein__sage_init_sage_0.py in <module>()
----> 1 
      2 
      3 
      4 
      5 

/Users/wstein/build/sage-3.3.alpha0/local/lib/python2.5/site-packages/sage/rings/polynomial/multi_polynomial.so in sage.rings.polynomial.multi_polynomial.MPolynomial.change_ring (sage/rings/polynomial/multi_polynomial.c:6691)()
    661 
    662 
--> 663 
    664 
    665 

/Users/wstein/build/sage-3.3.alpha0/local/lib/python2.5/site-packages/sage/rings/polynomial/multi_polynomial_libsingular.so in sage.rings.polynomial.multi_polynomial_libsingular.MPolynomialRing_libsingular.__call__ (sage/rings/polynomial/multi_polynomial_libsingular.cpp:6267)()
    616 
    617 
--> 618 
    619 
    620 

TypeError: unable to coerce <type 'sage.rings.finite_field_givaro.FiniteField_givaroElement'> to an integer
```


This is because the givaro finite field __call__ is wrong:

```
sage: GF(23)(GF(23^2,'a')(1))
BOOM!
TypeError: unable to coerce <type 'sage.rings.finite_field_givaro.FiniteField_givaroElement'> to an integer

but

sage: GF(next_prime(10^20))(GF(next_prime(10^20)^2,'a')(1))
1
```



---

Attachment


---

Comment by malb created at 2009-01-23 17:31:07

looks good.


---

Comment by mabshoff created at 2009-01-24 14:48:20

Merged in Sage 3.3.alpha2


---

Comment by mabshoff created at 2009-01-24 14:48:20

Resolution: fixed
