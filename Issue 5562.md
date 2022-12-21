# Issue 5562: coercion error with vectors and polynomial rings with 1 variable

Issue created by migration from Trac.

Original creator: ncalexan

Original creation time: 2009-03-18 23:00:00

Assignee: was

CC:  robertwb

Keywords: coercion vector polynomial ring

This is strange: it matters how many variables are specified.  This fails and I think this is a bug:


```
sage: R.<u> = PolynomialRing(RDF, 1, 'u')
sage: v1 = vector([u])
sage: v2 = vector([CDF(2)])
sage: v1 * v2
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/ncalexan/sage-3.4.rc0-sage.math-only-x86_64-Linux/devel/sage/sage/functions/riemann_theta.py in <module>()

/home/ncalexan/sage-3.4.rc0-sage.math-only-x86_64-Linux/local/lib/python2.5/site-packages/sage/structure/element.so in sage.structure.el\
ement.Vector.__mul__ (sage/structure/element.c:10435)()

/home/ncalexan/sage-3.4.rc0-sage.math-only-x86_64-Linux/local/lib/python2.5/site-packages/sage/structure/coerce.so in sage.structure.coe\
rce.CoercionModel_cache_maps.bin_op (sage/structure/coerce.c:5847)()

TypeError: unsupported operand parent(s) for '*': 'Ambient free module of rank 1 over the integral domain Multivariate Polynomial Ring i\
n u over Real Double Field' and 'Vector space of dimension 1 over Complex Double Field'
```


But both of these succeed:


```
sage: R.<u, v> = RDF[]
sage: v1 = vector([u])
sage: v2 = vector([CDF(2)])
sage: v1 * v2
2.0*u
```



```
sage: R.<u> = RDF[]
sage: v1 = vector([u])
sage: v2 = vector([CDF(2)])
sage: v1 * v2
2.0*u
```



---

Comment by tscrim created at 2012-12-10 21:22:03

Changing status from new to needs_review.


---

Comment by tscrim created at 2012-12-10 21:22:03

This seems to be fixed in `5.5.rc0`

```
sage: R.<u> = PolynomialRing(RDF, 1, 'u')
sage: v1 = vector([u])
sage: v2 = vector([CDF(2)])
sage: v1 * v2
2.0*u
```



---

Comment by cnassau created at 2013-01-26 14:54:05

I've attached a patch that adds a doctest that makes sure this keeps working.

The patch also removes plenty of trailing whitespace in the affected file. I got this for free by putting 

```
(add-hook 'before-save-hook 'delete-trailing-whitespace)
```

into my "`.emacs.rc`".

But maybe it might have been better to just give the "wontfix" a positive review instead...


---

Comment by tscrim created at 2013-01-28 17:46:16

Hey,

For doctest formatting, I would change:

```
    sage: # check that #5562 has been fixed
    sage: R.<u> = PolynomialRing(RDF, 1, 'u')
...
```

to

```
Check that :trac:`5562` has been fixed::

    sage: R.<u> = PolynomialRing(RDF, 1, 'u')
...
```


I think the trailing whitespace removal should be okay...

Best,

Travis


---

Comment by cnassau created at 2013-01-29 17:26:22

Hi Travis,

I agree, in theory, that the doctest should be reformatted. However, I don't know how to do this because the patch has apparently already been merged in 5.7.beta1. Would I create a new patch based on beta1, or edit the old one?

Cheers,
Christian


---

Comment by robertwb created at 2013-01-29 17:46:08

This won't be merged until it's positively reviewed and closed, it's just the target that was changed. You can create a new patch or edit the old, whichever makes it clearer what your changes were.


---

Attachment


---

Comment by tscrim created at 2013-01-29 18:10:20

Changing status from needs_review to positive_review.


---

Comment by tscrim created at 2013-01-29 18:10:20

Looks good to me. Thanks Christian.


---

Comment by cnassau created at 2013-01-29 18:12:41

Replying to [comment:6 tscrim]:
> Looks good to me. Thanks Christian.

Indeed, my working copy had been garbled, presumably by running "hg import" earlier when I meant "hg qimport" which made me believe that this ticket had somehow magically be merged already... anyway, glad we got rid of this now ;-)

Cheers,
Christian


---

Comment by jdemeyer created at 2013-01-31 09:18:52

Resolution: fixed
