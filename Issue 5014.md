# Issue 5014: matrix rank should call echelon_form over *fraction field*

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-01-18 14:59:32

Assignee: was

CC:  mjo


```

On Sun, Jan 18, 2009 at 6:49 AM, Paul Zimmermann <Paul.Zimmermann`@`loria.fr> wrote:
>       Hi,
>
> I hit the following:
>
> sage: P.<x> = PolynomialRing(GF(17))
> sage: m = Matrix(P,2,2)
> sage: m.randomize(); m
>
> [ 6*x^2 + 8*x + 12 10*x^2 + 4*x + 11]
> [8*x^2 + 12*x + 15  8*x^2 + 9*x + 16]
> sage: m.rank()
> ...
> NotImplementedError: echelon form over Univariate Polynomial Ring in x over Finite Field of size 17 not yet implemented
>
> Isn't that provided by either GP or Linbox?

Yes, by gp.  I have no idea if it is in Linbox.

sage: gp(m).matrank()
2
sage: pari(m).matrank()
boom -- matrank not wrapped

Somebody *could* implement this by wrapping pari's matrank then doing the conversion and calling it.  Of course, much better would be to do:

sage: m.change_ring(m.base_ring().fraction_field()).rank()
2

which already works. 

I am puzzled that rank doesn't first change base to the fraction field, *then* call echelon form -- it's stupid that it tries to call echelon form over the same base ring, since that is often much harder (e.g., it is Hermite form over ZZ).

William
```



---

Comment by jason created at 2009-01-21 08:27:58

See #3211 for a related ticket, sort of.


---

Comment by dsm created at 2011-05-23 13:16:22

This seems to work now:


```

sage: version()
'Sage Version 4.6.2, Release Date: 2011-02-25'
sage: P.<x> = PolynomialRing(GF(17))
sage: m = Matrix(P,2,2)
sage: m.randomize()
sage: m
[     15*x^2 + 16*x  9*x^2 + 12*x + 12]
[13*x^2 + 16*x + 16   4*x^2 + 5*x + 12]
sage: m.rank()
2
```



---

Attachment

Add a doctest computing the rank of one of these matrices.


---

Comment by mjo created at 2012-01-08 00:10:39

This works now; I've added a doctest using the example in the description.


---

Comment by mjo created at 2012-01-08 00:10:39

Changing status from new to needs_review.


---

Comment by novoselt created at 2012-01-11 05:16:37

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2012-01-21 23:39:19

Resolution: fixed
