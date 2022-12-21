# Issue 2405: Polydict speed

Issue created by migration from Trac.

Original creator: jbmohler

Original creation time: 2008-03-06 14:21:20

Assignee: malb

We have this timing:

```
sage: R.<x,y,z,u,v,w>=ZZ[]
sage: f=prod([g^2-12*g+2 for g in R.gens()])
sage: len((f).monomials())
729
sage: %time _=f**2
CPU times: user 21.32 s, sys: 0.14 s, total: 21.46 s
Wall time: 21.46
```


I did some testing and I believe that the ETuple !__hash!__ function appears to be a quite non-trivial part of this bottleneck.  A slightly tweaked version gives me the time

```
sage: %time _=f**2
CPU times: user 7.67 s, sys: 0.07 s, total: 7.74 s
Wall time: 7.74
```


A principle part of this tweak was replacing 

```
return hash((tuple(sorted(self._data.iteritems())),self._length))
```

with 

```
return hash((tuple(self._data.items()),self._length))
```


I would have submitted a patch with this replaced code, but I think the sorting is a good part of that algorithm.  But, if we suppose that dictionaries produce their tuples in a predictable order, then I think the unsorted version should work.  However, the deeper issue is that I think we might want to consider some other storage alternatives for e-tuples -- possibly a sparse C array?  I think that the unsorted version is still pretty heavy for a hash function of an ETuple which absolutely must be super-fast.

A paper by Fateman proved to be moderately interesting:  http://www.cs.berkeley.edu/~fateman/papers/fastmult.pdf  My impression after reading that paper is that we're essentially doing the correct algorithm (that is, there is no better algorithm for generic sparse poly's than the ordinary multiplication).  So, it seems to me that there really isn't a good reason that we should be significantly slower than singular at this.  Singular does this multiplication in about 1/4 second.


---

Comment by malb created at 2008-03-06 15:11:28

> So, it seems to me that there really isn't a good reason that we should be 
> significantly slower than singular at this.  Singular does this multiplication in
> about 1/4 second.

I guess we'll need to reimplement everything in C first, using Python ints etc. is really killing us. Also we should replace the dictionaries with C hash tables (e.g., glib's). But we will always have the overhead of Python interfaced base fields and thus we will always be slower than Singular. 

Btw. for ZZ we should either
 * implement it on top of Singular's QQ polynomials (short term)
 * bug the Singular team to release their ZZ and ZZ/N code (it is 'almost done')


---

Comment by jbmohler created at 2008-03-10 18:15:32

My experiments before I entered this ticket and more afterwards indicate that there is more than the ETuple hashing and arithmetic before we're going to be comparable to singular.

So, I'm not sure how big of a deal this is.  Ultimately, yes, singular is probably the way to go, but I think that the ETuples and polydict make a really nice multivariate polynomial implementation.  I'd like to see how far we could push it.  Obviously, if no one cares enough about ETuples and polydicts to actually put in the time, we have an implicit answer about the importance of this trac ticket.

My motivation for entering it was to point out what I think is the correct starting point for improving the polydict/etuple implementation efficiency.  I don't have concrete plans for doing this and I certainly understand if no one else does either, but I do think it would be a shame to just move to singular and forget it.  I think competing implementations are good.


---

Comment by malb created at 2008-03-11 11:26:18

> So, I'm not sure how big of a deal this is.  Ultimately, yes, singular is probably the way to go, but I think that the ETuples and polydict make a really nice multivariate polynomial implementation.  I'd like to see how far we could push it.  Obviously, if no one cares enough about ETuples and polydicts to actually put in the time, we have an implicit answer about the importance of this trac ticket.

I do care, because we need a general purpose implementation and I think it would be fun to come up with something fast but general. I don't have the time right now though.


---

Comment by jbmohler created at 2008-03-15 20:23:03

The etuple-rewrite.patch appears to be robust and working.  It passes greatly augmented internal etuple doc-tests and has been successfully used to benchmark large polynomial multiplication.

Time improvements range from 2x to 50x.  I think the speed-up should be more consistent so I'm a little worried about something with this.

In any case, I post the patch now in this state to get a feel from others whether this is a sensible storage format.  Note that the original ETuple allowed (sort-of) rational exponents, but the new one does not.


---

Comment by jbmohler created at 2008-03-16 00:18:01

Preliminary ETuple Rewrite using a sparse C array (with-out doc-test fixes)


---

Attachment

The last patch update fixes the fact that my hash code was really really screwed up.  Now, I'm getting a consistent 10x speed up compared to the unpatched arithmetic.

This means that we are approximately 3-6 times slower than singular over QQ.  It almost appears as though we are beating them asymptotically -- we're easily with-in a factor of 3 for squaring a poly with 6000 monomials.  However, with this size, both of our times are in the 1-2 minute range so I'm not patient enough to see where the cross-over occurs.


---

Comment by malb created at 2008-03-16 15:29:39

*Review*:
 * Overall, the patch looks very good and I cheer you for picking up the task of making the general multivariate polynomials faster
 * I agree that the sparse data structure makes sense for many applications, note that Singular has different data structures for different numbers of variables, e.g. if only three variables are in the ring then a dense representation is chosen.
 * you should definitely add yourself as AUTHOR
 * you can use "cpdef eadd" instead of "def eadd" and "cdef _eadd"
 * I don't see any (off-list) mentioned memleak:

```
sage: PZ.<a,b,c> =PolynomialRing(ZZ)
sage: get_memory_usage()
606.27734375
sage: %timeit a*b
100000 loops, best of 3: 10.8 µs per loop
sage: get_memory_usage()
606.27734375
```

 * Comparison with Singular for very small examples:

```
sage: PZ.<a,b,c> =PolynomialRing(ZZ)
sage: %timeit a*b
100000 loops, best of 3: 10.8 µs per loop
sage: PQ.<x,y,z> =PolynomialRing(QQ)
sage: %timeit x*y
1000000 loops, best of 3: 268 ns per loop
sage: 10800 / 268.0
40.2985074626866
```

 * I say _apply_ if Joel declares his code production ready (it looks that way to me).

I'd say that a 10x speedup is possible by replacing the `ETuple` with a C struct, replacing the `PolyDict` class with a C struct and pushing the MPolynomial_polydict class down to Cython eventually.


---

Comment by malb created at 2008-03-16 16:01:46

I have to reconsider my verdict, `sage -t` fails badly, e.g.:


```
sage -t  devel/sage-etuple/sage/rings/polynomial/multi_polynomial_element.py**********************************************************************
File "multi_polynomial_element.py", line 304:
    sage: loads(dumps(x)) == x
Exception raised:
    Traceback (most recent call last):
      File "/usr/local/sage-2.10.3.rc2/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_10[2]>", line 1, in <module>
        loads(dumps(x)) == x###line 304:
    sage: loads(dumps(x)) == x
      File "sage_object.pyx", line 562, in sage.structure.sage_object.loads
    RuntimeError: (None, <built-in function make_ETuple>, ({0: 1}, 10L))
    invalid data stream
    invalid load key, 'x'.
    Unable to load pickled data.
**********************************************************************
File "multi_polynomial_element.py", line 482:
    sage: [(c,m) for c,m in f]
Expected:
    [(3, x^3*y), (16, x), (7, 1)]
Got:
    [(16, x), (3, x^3*y), (7, 1)]
**********************************************************************
File "multi_polynomial_element.py", line 661:
    sage: g = f.homogenize('z'); g # indirect doctest
Expected:
    x^2 + 5*x*y + y*z + z^2
Got:
    y*z + z^2 + 5*x*y + x^2
**********************************************************************
File "multi_polynomial_element.py", line 726:
    sage: F
Expected:
    -1*fy^3*gx^3 + 3*fx*fy^2*gx^2*gy - 3*fx^2*fy*gx*gy^2 + fx^3*gy^3
Got:
    3*fx*fy^2*gx^2*gy - 3*fx^2*fy*gx*gy^2 + fx^3*gy^3 - fy^3*gx^3
**********************************************************************
File "multi_polynomial_element.py", line 728:
    sage: F.monomials()
Expected:
    [fy^3*gx^3, fx*fy^2*gx^2*gy, fx^2*fy*gx*gy^2, fx^3*gy^3]
Got:
    [fx*fy^2*gx^2*gy, fx^2*fy*gx*gy^2, fx^3*gy^3, fy^3*gx^3]
**********************************************************************
File "multi_polynomial_element.py", line 730:
    sage: F.coefficients()
Expected:
    [-1, 3, -3, 1]
Got:
    [3, -3, 1, -1]
**********************************************************************
File "multi_polynomial_element.py", line 202:
    sage: 3*f
Expected:
    3*x + 3*y
Got:
    3*y + 3*x
**********************************************************************
File "multi_polynomial_element.py", line 1130:
    sage: factor(x^3 - 2*y^3)
Expected:
    (x + (-s)*y) * (x^2 + s*x*y + s^2*y^2)
Got:
    ((-s)*y + x) * (s*x*y + s^2*y^2 + x^2)
**********************************************************************
File "multi_polynomial_element.py", line 1133:
    sage: k.factor()
Expected:
    (s^2 + 2/3) * (x + s*y)^2 * (x + (-s)*y)^5 * (x^2 + s*x*y + s^2*y^2)^5
Got:
    (s^2 + 2/3) * (s*y + x)^2 * ((-s)*y + x)^5 * (s*x*y + s^2*y^2 + x^2)^5
**********************************************************************
File "multi_polynomial_element.py", line 1224:
    sage: gcd(p,q)
Expected:
    x^3 + (u + 1)*y^3 + z^3
Got:
    z^3 + (u + 1)*y^3 + x^3
**********************************************************************
File "multi_polynomial_element.py", line 1298:
    sage: g.reduce(F)
Expected:
    6*y^2 - 2*y
Got:
    6*x^2 - 2*y
**********************************************************************
File "multi_polynomial_element.py", line 1300:
    sage: g.reduce(F.gens())
Expected:
    6*y^2 - 2*y
Got:
    6*x^2 - 2*y
**********************************************************************
File "multi_polynomial_element.py", line 1392:
    sage: degree_lowest_rational_function(r,a)
Expected:
          (-1, 4)
Got:
    (-1, 3)
**********************************************************************
File "multi_polynomial_element.py", line 217:
    sage: f*3
Expected:
    3*x + 3*y
Got:
    3*y + 3*x
**********************************************************************
10 items had failures:
   1 of   3 in __main__.example_10
   1 of   6 in __main__.example_16
   1 of   4 in __main__.example_22
   3 of   9 in __main__.example_24
   1 of   3 in __main__.example_4
   2 of  14 in __main__.example_40
   1 of  20 in __main__.example_42
   2 of  10 in __main__.example_45
   1 of   9 in __main__.example_46
   1 of   3 in __main__.example_5
***Test Failed*** 14 failures.
For whitespace errors, see the file .doctest_multi_polynomial_element.py
         [2.6 s]
exit code: 256

----------------------------------------------------------------------
The following tests failed:


        sage -t  devel/sage-etuple/sage/rings/polynomial/multi_polynomial_element.py
Total time for all tests: 2.6 seconds
```


 * the monomials are not printed w.r.t. to the monomial ordering anymore
 * sometimes the result is just plain wrong


---

Comment by jbmohler created at 2008-03-18 14:12:28

Yep, I knew about the doc-test failures.  I posted the preliminary patch so I could get pre-review.  Virtually all of the polydict.pyx doc-test failures are side-effects from the !__hash!__ changing.  However, I do agree that there was a bug with the final output not respecting parental ordering and fixed it.

The newly attached patch should pass doc-tests and be production ready.

Pre-patch timing:

```
sage: R.<x,y,z,a,b>=ZZ[]
sage: f=prod([2*g^2-4*g+8 for g in R.gens()])
sage: %time _=f*f
CPU times: user 2.23 s, sys: 0.00 s, total: 2.23 s
Wall time: 2.24
```


Post-patch timing:

```
sage: R.<x,y,z,a,b>=ZZ[]
sage: f=prod([2*g^2-4*g+8 for g in R.gens()])
sage: %time _=f*f
CPU times: user 0.22 s, sys: 0.00 s, total: 0.22 s
Wall time: 0.22
```


We've still got a long way to go to compete with singular.  Moving the MPolynomial_polydict to cython and speeding up creation time should make a noticable difference especially in very small problems where singular is absolutely killing us.


---

Attachment

production ready patch


---

Comment by malb created at 2008-03-19 17:24:53

*Review*:
 * everything asked for before is addressed it seems
 * small polynomials timings: 
Before:

```
sage: P.<x,y,z> = PolynomialRing(ZZ)
sage: %timeit x*y
10000 loops, best of 3: 23.2 µs per loop
```


After:

```
sage: P.<x,y,z> = PolynomialRing(ZZ)
sage: %timeit x*y
100000 loops, best of 3: 11 µs per loop
```

 * applies cleanly, doctests pass
 * I say apply


---

Comment by mabshoff created at 2008-03-20 00:46:58

Resolution: fixed


---

Comment by mabshoff created at 2008-03-20 00:46:58

Merged in Sage 2.11.alpha0
