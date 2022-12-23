# Issue 2634: (easy fix?) Unable to create certain multivariate polynomial rings since libsingular is invoked instead of generic code

Issue created by migration from https://trac.sagemath.org/ticket/2634

Original creator: was

Original creation time: 2008-03-21 18:48:19

Assignee: malb


```
sage: k = GF(next_prime(2^31)^2,'x')
sage: k['y,z']
Traceback (most recent call last):
...
OverflowError: long int too large to convert to int
sage: PolynomialRing(k,2,'x,y')
Traceback (most recent call last):
...
OverflowError: long int too large to convert to int
```



This is caused because Sage is trying to use libsingular
to create the poly ring, but should be using its own code
when the size of the base ring is too big. 

Martin Albrecht will be able to fix this very easily.


---

Attachment

The attached patch implements the easy fix and worksforme. However, my installation is FUBAR right now so a referee would have to run `make test` but there should be no surprises. Sorry for the mess.


---

Comment by malb created at 2008-03-22 14:18:25

Changing status from new to assigned.


---

Comment by AlexGhitza created at 2008-03-22 14:45:22

Hi,

It's good but there are two issues:

1. sage -t sage/schemes/generic/affine_space.py fails:


```
sage -t  schemes/generic/affine_space.py                    **********************************************************************
File "affine_space.py", line 196:
    sage: AffineSpace(ZZ,1, 'a') == AffineSpace(ZZ, 0, 'a')
Exception raised:
    Traceback (most recent call last):
      File "/opt/sage/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_5[1]>", line 1, in <module>
        AffineSpace(ZZ,Integer(1), 'a') == AffineSpace(ZZ, Integer(0), 'a')###line 196:
    sage: AffineSpace(ZZ,1, 'a') == AffineSpace(ZZ, 0, 'a')
      File "/opt/sage/local/lib/python2.5/site-packages/sage/schemes/generic/affine_space.py", line 204, in __cmp__
        [right.dimension(), right.coordinate_ring()])
      File "/opt/sage/local/lib/python2.5/site-packages/sage/schemes/generic/affine_space.py", line 262, in coordinate_ring
        self._coordinate_ring = MPolynomialRing(self.base_ring(), self.dimension(), names=self.variable_names())
      File "/opt/sage/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_ring_constructor.py", line 248, in PolynomialRing
        R = _multi_variate(base_ring, names, n, sparse, order)
      File "/opt/sage/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_ring_constructor.py", line 365, in _multi_variate
        R = MPolynomialRing_libsingular(base_ring, n, names, order)
      File "multi_polynomial_libsingular.pyx", line 196, in sage.rings.polynomial.multi_polynomial_libsingular.MPolynomialRing_libsingular.__init__
    ArithmeticError: number of variables must be at least 1
**********************************************************************
```



2. this is minor; there's a typo in the new error message in multi_polynomial_libsingular.pyx: should be


```
raise NotImplementedError, "Number fields are not fully supported yet." 
```


instead of 


```
raise NotImplementedError, "Number fields are not fully support yet."
```


I'll very happily give this a quick positive review as soon as these things get fixed.


---

Comment by malb created at 2008-03-24 00:15:47

fixes the typo reported by Alex.


---

Attachment

allow 0 gens for multivariate polynomial rings (debatable!)


---

Comment by malb created at 2008-03-24 00:18:37

I've attached patches for both issues reported by Alex, *but* I am not convinced that it is actually desired to allow 0 generators for multivariate polynomial rings. We allowed that before and thus I reintroduced that behaviour but I would like to get rid of it: It will be a no fun to support once the generic multivariate polynomials get closer to C and I don't see the point.


---

Comment by AlexGhitza created at 2008-03-24 02:49:17

I understand your objection.  I'm not comfortable deciding about that, so I'll throw it on sage-devel and see what people say.

In the mean time, the patches look good and doctest well.  I think we should apply them.


---

Comment by mabshoff created at 2008-03-24 08:14:12

To quote William from https://groups.google.com/group/sage-devel/t/2d722ebda3887a56

```
I definitely think multivariate polynomial rings with 0 generators
should be supported
for exactly the same reason matrices with 0 rows or columns should be
supported -- algorithms are much more likely to work in corner cases and code
is cleaner.

I've been incredibly glad on numerous occasions that across the board
Sage works very well with matrices that have 0 rows or columns, though
this took a lot of extra work initially.   The only argument put forth for
removing multivariate polynomials rings with 0 generators is "It will
be a no fun to support".   That is not compelling.

William 
```


This leads me to merge this patch now to fix the issue. I assume we will revisit this in the future since Martin commented right after William that

```

libSingular doesn't support it and as soon as more pointers are involved the
generic implementation will too have problems (== NULL pointers). Maybe a
special implementation for zero generators is in order then?

Martin 
```


Cheers,

Michael


---

Comment by mabshoff created at 2008-03-24 08:35:14

Resolution: fixed


---

Comment by mabshoff created at 2008-03-24 08:35:14

Merged in Sage 2.11.alpha2
