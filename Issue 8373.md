# Issue 8373: finite fields constructed with non-primitive defining polynomial

Issue created by migration from Trac.

Original creator: rkirov

Original creation time: 2010-02-26 06:47:28

Assignee: AlexGhitza

CC:  pbruin

Consider the following code:

```
sage: R.<x> = PolynomialRing(GF(2))
sage: K.<a> = GF(16, modulus=x^4+x^3+x^2+x+1)
sage: a^5
1
```


This is all fine mathematically, as long as the user is clear what a is and isn't (it isn't a generator for the multiplicative group of the finite field). So the options as I see them (in increasing difficulty for implementation):

1)GF already checks modulus for irreducibility, just add check for modulus.is_primitive().

2)Rewrite the help for the GF function to indicate that the function does not return a generator necessarily (like in this specific case).

3)Find an actual generator (that might not be the polynomial x) and return that.


Opinions?


---

Comment by fwclarke created at 2010-02-26 09:32:11

Replying to [ticket:8373 rkirov]:

In your example, `a` _is_ a generator; it's an _algebra generator_.  In fact `a` generates `K` in exactly the same sense in which `x` generates `R`.  What you're looking for is:


```
sage: R.<x> = GF(2)[]
sage: K.<a> = GF(16, modulus=x^4+x^3+x^2+x+1)
sage: K.multiplicative_generator()
a + 1
```

It would be a mistake to insist on having a primitive generator.  Of your options: 

(1) could slow Sage down unnecessarily, and what should it do if a user wanted to use a non-primitive generator?

(2) yes, if the documentation is confusing, it should be clarified.

(3) I don't quite understand.  If you mean ignore a given modulus if  it is not primitive, that would be very confusing.

What _is_ needed, for non-prime fields of large characteristic, is a much better way of finding a multiplicative generator:


```
sage: p = 65537
sage: K.<a> = GF(p^2)
sage: a.multiplicative_order() == p^2 - 1
False
sage: time K.multiplicative_generator()
CPU times: user 498.03 s, sys: 56.61 s, total: 554.64 s
Wall time: 555.20 s
a + 3
```

What's taking the time here is that the current algorithm, after deciding that `a` isn't a multiplicative generator,  pointlessly computes the multiplicative order of all the non-zero elements in the prime field, before trying `a` (again), `a + 1`, `a + 2`, and succeeding with `a + 3`.


---

Comment by rkirov created at 2010-02-26 10:50:53

I guess you are right, it is a generator as an algebra. Somehow I assumed F.<a> gives you 'a' as a multiplicative generator. So it is really a renaming of 'x'(poly var)->'a'. I didn't see the convenient function F.multiplicative_generator.

I checked that Magma has similar behavior.


```
> F2 := GF(2);
> FP<x> := PolynomialRing(F2);
> F<z> := ext< F2 | x^4+x^3+x^2+x+1 >;
```

It also seems to have different algorithm for primitive element,

```
> PrimitiveElement(F);
z^3 + z + 1
```


In any case I am leaving this open so someone can work on the bug you found.


---

Comment by jdemeyer created at 2014-06-26 14:56:10

Changing type from defect to enhancement.


---

Comment by jdemeyer created at 2014-06-26 14:56:10

This is certainly not a bug, but possibly a feature request.

I would propose adding the option `modulus="primitive"` to solve this ticket.


---

Comment by jdemeyer created at 2014-06-26 14:56:35

Changing assignee from AlexGhitza to cpernet.


---

Comment by jdemeyer created at 2014-06-26 14:56:35

Changing component from basic arithmetic to finite rings.


---

Comment by fwclarke created at 2014-08-05 17:48:43

Replying to [comment:5 jdemeyer]:

The idea of allowing modulus='primitive' is good.  But a problem with the modified description is that the discussion in comments 1 and 2 is now out of context.


---

Comment by jdemeyer created at 2014-08-05 19:35:42

Replying to [comment:6 fwclarke]:
> Replying to [comment:5 jdemeyer]:
> 
> The idea of allowing modulus='primitive' is good.
And sufficient for you to consider this issue fixed?

> But a problem with the modified description is that the discussion in comments 1 and 2 is now out of context.
Sure, but that's not really a problem, right?


---

Comment by pbruin created at 2014-09-03 12:04:12

Replying to [ticket:8373 rkirov]:

> Also add an argument `modulus="pari"` (and make it the default) to use PARI's `ffinit()`.
This already exists in `PolynomialRing_dense_mod_p.irreducible_element()` under the name `modulus="adleman-lenstra"`.  It is the default if no Conway polynomial is known and the characteristic is odd.

Some finite field implementations accept a string `modulus`, but this should be obsolete; `FiniteFieldFactory.create_key_and_extra_args()` uses the above method to convert a string `modulus` into an actual polynomial.


---

Comment by jdemeyer created at 2014-09-03 12:18:09

Thanks for the pointer, I was confused by `PolynomialRing_dense_finite_field.irreducible_element`


---

Comment by jdemeyer created at 2014-09-03 12:26:48

Replying to [comment:11 pbruin]:
> Some finite field implementations accept a string `modulus`, but this should be obsolete
Why should it be obsolete? I think the syntax

```
k.<a> = GF(p^n, modulus="primitive")
```

is very good to have. Note that the actual modulus polynomial is computed before the implementation is even considered. So it's not that every finite field implementation needs to be aware of this.


---

Comment by pbruin created at 2014-09-03 12:30:14

Replying to [comment:13 jdemeyer]:
> Replying to [comment:11 pbruin]:
> > Some finite field implementations accept a string `modulus`, but this should be obsolete
> Why should it be obsolete? I think the syntax
> {{{
> k.<a> = GF(p^n, modulus="primitive")
> }}}
> is very good to have.
Yes, it is certainly not this syntax that needs to be made obsolete!
> Note that the actual modulus polynomial is computed before the implementation is even considered. So it's not that every finite field implementation needs to be aware of this.
That is what I meant; the individual implementation should never need to consider the case where `modulus` is a string, it should all be handled by the factory.


---

Comment by jdemeyer created at 2014-09-03 13:49:45

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2014-09-03 13:49:45

New commits:


---

Comment by jdemeyer created at 2014-09-04 09:23:17

Replying to [comment:15 pbruin]:
> That is what I meant; the individual implementation should never need to consider the case where `modulus` is a string, it should all be handled by the factory.

Good, this will be #16930.


---

Comment by pbruin created at 2014-09-04 12:31:15

Changing status from needs_review to positive_review.


---

Comment by pbruin created at 2014-09-04 12:31:15

Looks good and passes tests.


---

Comment by vbraun created at 2014-09-05 21:38:37

I got this on arando (linux 32-bit):

```
sage -t --long src/sage/rings/polynomial/polynomial_ring.py
**********************************************************************
File "src/sage/rings/polynomial/polynomial_ring.py", line 2331, in sage.rings.polynomial.polynomial_ring.PolynomialRing_dense_mod_n.irreducible_element
Failed example:
    GF(5)['x'].irreducible_element(32, algorithm="primitive")
Expected:
    x^32 + 4*x^31 + x^30 + 4*x^29 + 4*x^28 + 3*x^27 + 2*x^26 + x^25 + x^24 + x^23 + 4*x^21 + 3*x^20 + x^19 + 4*x^17 + 4*x^16 + 4*x^15 + 4*x^14 + 3*x^13 + x^12 + 3*x^11 + 4*x^10 + x^9 + 4*x^8 + x^7 + 2*x^6 + 4*x^5 + 4*x^4 + x^3 + 3*x^2 + 4*x + 2
Got:
    x^32 + 3*x^31 + x^30 + 4*x^28 + 2*x^27 + 2*x^26 + 2*x^24 + 2*x^23 + 2*x^22 + x^21 + 3*x^20 + 3*x^19 + x^18 + 3*x^17 + 4*x^16 + 2*x^15 + 3*x^12 + 4*x^11 + x^10 + 2*x^8 + 3*x^7 + 2*x^6 + 3*x^5 + x^4 + 4*x^3 + x + 3
**********************************************************************
```



---

Comment by vbraun created at 2014-09-05 21:38:37

Changing status from positive_review to needs_work.


---

Comment by git created at 2014-09-06 06:33:42

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by jdemeyer created at 2014-09-06 06:55:19

Changing status from needs_work to positive_review.


---

Comment by vbraun created at 2014-09-08 08:48:58

Resolution: fixed
