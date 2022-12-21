# Issue 6919: basic arithmetic using FLINT is broken (very serious!)

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-09-10 18:56:51

Assignee: somebody

CC:  wbhart burcin

Mariah Lenox reported:

```
R.<x> = PolynomialRing(ZZ)
A = 2^(2^17+2^15)  # note the 2 rather than the "s"
a = A * x^31
b = (A * x) * x^30
a == b   # prints "False" ???
```


But

```
R.<x> = PolynomialRing(ZZ, implementation='NTL')
A = 2^(2^17+2^15)  # note the 2 rather than the "s"
a = A * (x^31)
b = A * x * (x^30)
a == b   
```

gives True.  So this is definitely either a bug in FLINT (highly likely), or a bug in our wrapper (much less likely, since our wrapper is so generic:

```
cpdef RingElement _mul_(self, RingElement right):
    r"""
    Returns self multiplied by right.

    EXAMPLES::

        sage: R.<x> = PolynomialRing(ZZ)
        sage: (x - 2)*(x^2 - 8*x + 16)
        x^3 - 10*x^2 + 32*x - 32
    """
    cdef Polynomial_integer_dense_flint x = self._new()
    _sig_on
    fmpz_poly_mul(x.__poly, self.__poly,
            (<Polynomial_integer_dense_flint>right).__poly)
    _sig_off
    return x
```

}}}


---

Comment by burcin created at 2009-09-16 13:19:27


```
Bill Hart <goodwillhart`@`googlemail.com> wrote:
<snip>
> It was caused by a bug in the FLINT FFT (the first ever found). I
> tracked the bug down to a specific piece of code and David Harvey has
> supplied a fix. There will be a new version of FLINT to patch this
> bug.
```



---

Attachment


---

Comment by mhansen created at 2009-09-25 04:13:33

I've attached a patch which makes sure that this bug is indeed fixed by FLINT 1.5.0.  The spkg can be found at http://sage.math.washington.edu/home/mhansen/flint-1.5.0.p0.spkg .  This spkg is based of 1.3.0.p3 that Ondrej did.


---

Comment by was created at 2009-09-26 01:21:55

I posted another spkg that adds one critical Cygwin fix, namely naming the library libflint.dll instead of libflint.so:

http://sage.math.washington.edu/home/wstein/patches/flint-1.5.0.p1.spkg

It's based exactly on mhansen's spkg.


---

Comment by jhpalmieri created at 2009-09-26 04:21:46

OS X 10.5, both 32-bit and 64-bit: first I applied the patch.  This produced the doctest failure described in the ticket for the file libs/flint/flint.pyx.  Then I did 'sage -f flint...' to install the new spkg .  Then this file passed doctests.


---

Comment by mvngu created at 2009-09-27 01:28:18

New FLINT package up at

http://sage.math.washington.edu/home/mvngu/release/spkg/standard/flint-1.5.0.p2.spkg

The only change from .p1 is:

 * Check in all changes in wstein's name.


---

Comment by mvngu created at 2009-09-27 03:40:12

See palmieri's and my reports at #6849.


---

Comment by mvngu created at 2009-09-27 03:40:12

Resolution: fixed


---

Comment by mvngu created at 2009-09-27 11:03:06

There is no 4.1.2.alpha3. Sage 4.1.2.alpha3 was William Stein's release for working on making the notebook a standalone package.
