# Issue 2304: sparse_poly should probably be removed

Issue created by migration from Trac.

Original creator: dmharvey

Original creation time: 2008-02-25 21:31:04

Assignee: somebody

It looks like the module `sage.rings.sparse_poly` is deprecated and should be removed. I can't find any other references to it in the Sage library. Awaiting confirmation from wstein.

from IRC:

```
cwitty: according to  search_src('sparse_poly') it's never referred to (never imported, etc.)...
```




---

Comment by was created at 2008-02-25 21:44:13

But David, my code's so fast.  Could YOU square sum(n*x^n for n in range(1000))
in less than 1.24 seconds!?  :-)


Seriously though, I wrote that code before version 0.1 of Sage as an experiment.  It can safely be removed.  If one really did want sparse polys that are fast, the best thing for now would probably to use libsingular  with one variable, e.g., 


```
sage: R.<x,y> = MPolynomialRing(QQ,2)
sage: type(x)
<type 'sage.rings.polynomial.multi_polynomial_libsingular.MPolynomial_libsingular'>
sage: f = sum(n*x^(n^2) for n in primes(100))
sage: time g = f*f
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
Wall time: 0.00
sage: timeit('z=f*f')
625 loops, best of 3: 35.5 µs per loop

```


That said Singular polys only allow degrees up to 65K:


```
sage: x^66000
<type 'exceptions.TypeError'>: exponent is too large, max. is 65535
```


So I say delete sparse_poly.* from Sage.  If we someday want sparse polys that code could be revisited, or maybe flint will already have something much better.


---

Comment by mabshoff created at 2008-11-22 23:08:23

Still there in 3.2.1, but trivial to fix.

Cheers,

Michael


---

Comment by mabshoff created at 2008-11-22 23:08:23

Changing assignee from somebody to mabshoff.


---

Comment by mabshoff created at 2008-11-22 23:08:23

Changing status from new to assigned.


---

Attachment


---

Comment by ncalexan created at 2008-11-22 23:53:20

Fine by me.


---

Comment by mabshoff created at 2008-11-23 00:04:58

Merged in Sage 3.2.1.alpha0


---

Comment by mabshoff created at 2008-11-23 00:04:58

Resolution: fixed
