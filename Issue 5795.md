# Issue 5795: Improved performance of MPolynomialRing_libsingular.__call__()

Issue created by migration from https://trac.sagemath.org/ticket/5795

Original creator: SimonKing

Original creation time: 2009-04-16 02:50:47

Assignee: SimonKing

CC:  malb

Keywords: MPolynomialRing_libsingular, coercion, call

One comment in the `__call__()` method of MPolynomialRing_libsingular states:
 #TODO: We can do this faster without the dict

In fact, we can!

Without the patch, we have the following timings on sage.math:

```
sage: R=PolynomialRing(QQ,5,'x')
sage: S=PolynomialRing(QQ,6,'x')
sage: T=PolynomialRing(QQ,5,'y')
sage: U=PolynomialRing(GF(2),5,'x')
sage: p=R('x0*x1+2*x4+x3*x1^2')^4
sage: timeit('q=S(p)')
625 loops, best of 3: 341 Âµs per loop
sage: timeit('q=T(p)')
625 loops, best of 3: 370 Âµs per loop
sage: timeit('q=U(p)')
625 loops, best of 3: 451 Âµs per loop
```


With the patch, we have

```
sage: timeit('q=S(p)')
625 loops, best of 3: 328 Âµs per loop
sage: timeit('q=T(p)')
625 loops, best of 3: 292 Âµs per loop
sage: timeit('q=U(p)')
625 loops, best of 3: 396 Âµs per loop
```

So, the improvement is small, but it _is_ an improvement.

Background: 
 In the original version, if the input of `__call__` is MPolynomial_libsingular, then the `dict()` method of this polynomial was called in order to get the coefficients and exponent vectors. 
 
 In the new version, the underlying libsingular methods are called directly, which is faster. The price to pay is that currRing changes more often. I hope change of currRing is not too expensive (in my examples above, apparently it isn't).



---

Attachment

Improved performance for polynomial conversion


---

Comment by malb created at 2009-04-16 08:51:18

Hi Simon, are you sure that you need all the rChangeCurrRing() business? All functions you are calling *should* be safe without it. This might save a few cycles.

Btw. you improved "conversion" not "coercion". IIRC this is how we call stuff happening in `__call__`.

Other than that the patch looks goog, which version shall I apply the patch agains?


---

Comment by SimonKing created at 2009-04-16 11:52:23

Replying to [comment:2 malb]:
> Hi Simon, are you sure that you need all the rChangeCurrRing() business? All functions you are calling *should* be safe without it. This might save a few cycles.

First, I tried it without. But then there was a problem when converting a polynomial over QQ into a polynomial over GF(2) (or the other way around, I don't remember). I found that the line

```
c = co.si2sa(p_GetCoeff(_element, El_ring), El_ring, El_base) 
```

did not work properly (always returning zero when it should return 1). 

Then, in 'coefficients()', I found that 'rChangeCurrRing()' is used. I thought that it might be for a reason, and indeed the conversion works if 'El_ring' is 'currRing'.

But I do agree that it would be nice if it were possible to avoid the ring change.
 
> Btw. you improved "conversion" not "coercion". IIRC this is how we call stuff happening in `__call__`.

Ok, I changed the key word...

> Other than that the patch looks goog, which version shall I apply the patch agains?

3.4.1.rc3

Cheers,
     Simon


---

Comment by SimonKing created at 2009-04-16 14:19:25

Replying to [comment:3 SimonKing]:
> Replying to [comment:2 malb]:
> > Other than that the patch looks goog, which version shall I apply the patch agains?
> 
> 3.4.1.rc3

Ooops, it should be 3.4.1.rc2, I think.


---

Comment by malb created at 2009-04-17 11:48:14

Doctests pass, good to go.


---

Comment by mabshoff created at 2009-04-22 18:48:37

Merged in Sage 3.4.2.alpha0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-22 18:48:37

Resolution: fixed
