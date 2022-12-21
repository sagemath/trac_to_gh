# Issue 6339: multivariate polynomial content is broken

Issue created by migration from Trac.

Original creator: ncalexan

Original creation time: 2009-06-16 19:05:07

Assignee: malb

CC:  malb

Keywords: polynomial content


```
sage: QQ['x, y'].random_element().content()
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/ncalexan/.sage/temp/sage.math.washington.edu/8651/_home_ncalexan__sage_init_sage_0.py in <module>()

/scratch/ncalexan/sage-4.0.2.alpha1/local/lib/python2.5/site-packages/sage/rings/polynomial/multi_polynomial.so in sage.rings.polynomial.multi_polynom\
ial.MPolynomial.content (sage/rings/polynomial/multi_polynomial.c:9118)()

/scratch/ncalexan/sage-4.0.2.alpha1/local/lib/python2.5/site-packages/sage/rings/arith.pyc in gcd(a, b, **kwargs)
   1209     if U is ZZ or U is int or U is long:# ZZ.has_coerce_map_from(U):
   1210         return sage.rings.integer.GCD_list(a)
-> 1211     return __GCD_sequence(seq, **kwargs)
   1212
   1213 GCD = gcd

/scratch/ncalexan/sage-4.0.2.alpha1/local/lib/python2.5/site-packages/sage/rings/arith.pyc in __GCD_sequence(v, **kwargs)
   1249     one = v.universe()(1)
   1250     for vi in v:
-> 1251         g = vi.gcd(g, **kwargs)
   1252         if g == one:
   1253             return g

TypeError: gcd() takes no keyword arguments
```



---

Attachment


---

Comment by mhansen created at 2009-09-26 04:46:59

Looks good to me.


---

Comment by mvngu created at 2009-09-26 07:47:08

Resolution: fixed


---

Comment by mvngu created at 2009-09-27 10:52:15

There is no 4.1.2.alpha3. Sage 4.1.2.alpha3 was William Stein's release for working on making the notebook a standalone package.
