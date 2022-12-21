# Issue 2654: Cyclotomic polynomials -- suggested improvement

Issue created by migration from Trac.

Original creator: cremona

Original creation time: 2008-03-23 12:24:24

Assignee: malb

CC:  rlb

Keywords: cyclotomic polynomial

The current implementation of cyclotomic polynomials in sage/rings/polynomial/cyclotomic.pyx uses the Mobius inversion formula.

I think it would be more efficient to use the recursion

```
\Phi_{p*n}(X) = \Phi_n(X^p) # if p|n
              = \Phi_n(X^p)/\Phi_n(X) # else
```

(though probably not implemented recursively).  This would be simpler than what is currently done, and it would be worth implementing this to see if was really faster.

Secondly, it would be easy to implement a function is_cyclotomic() using the algorithm of Smyth and Beukers.  This could just return True/False, or even n if the input is the n'th cyclotomic poly.  One application would be to improve the function multiplicative_order() for elements of number fields (and more general algebras), by checking if the minimal poly is cyclotomic.  There are a couple of TODOs in sage.rings.number_field.number_field_element which this would address (the algorithm there describes itself as "very dumb" and it is hard to disagree!).


---

Comment by cremona created at 2008-03-23 12:57:14

I think this proves it.  Here's my new implementation as a Sage function:

```
def newcyc(n):
    assert n>0
    plist = n.prime_divisors()
    X = PolynomialRing(ZZ,'X').gen()
    f = X-1
    m = n
    for p in plist:
    	f = f(X**p)//f(X)
	m //= p
    return f.subs(X**m)
```


Now newcyc(factorial(10)) takes 15s compared with cyclotomic_polynomial(factorial(10)) whihc takes 108s.  When you take into account the fact that the old function is written in cython while the new one is in sage, I think I have proved my point!  Moreover the code for the new function is very much simpler.


---

Comment by robertwb created at 2008-03-31 20:03:45

This is due to some (very!) poor conversion code, not due to the algorithm itself. 


```
sage: import sage.rings.polynomial.cyclotomic as c
sage: n = factorial(10)
sage: time f = newcyc(n)
CPU time: 12.40 s,  Wall time: 12.53 s
sage: time L = c.cyclotomic_coeffs(n)
CPU time: 0.12 s,  Wall time: 0.13 s
```



---

Comment by cremona created at 2008-03-31 21:43:31

In that case I'll leave this alone and wait for you to provide a suitable patch!


---

Attachment


---

Comment by robertwb created at 2008-04-01 00:16:22

With timings like that, I couldn't resist


```
sage: time f = cyclotomic_polynomial(factorial(10))
CPU times: user 0.09 s, sys: 0.03 s, total: 0.12 s
Wall time: 0.13
sage: time f = cyclotomic_polynomial(10^5)
CPU times: user 0.01 s, sys: 0.00 s, total: 0.01 s
Wall time: 0.01
sage: time f = cyclotomic_polynomial(10^6)
CPU times: user 0.01 s, sys: 0.01 s, total: 0.02 s
Wall time: 0.02
sage: time f = cyclotomic_polynomial(10^7)
CPU times: user 0.14 s, sys: 0.07 s, total: 0.22 s
Wall time: 0.23
```


Implementing an `is_cyclotomic` function is also a good idea, but probably a separate ticket.


---

Comment by was created at 2008-04-01 04:40:35

REFEREE REPORT:

It builds fine.  It works fine, but gives the wrong (?) answer for n=1. 


```
sage: cyclotomic_polynomial(1)
-x + 1
sage: gp('polcyclo(1)')
x - 1
sage: magma('CyclotomicPolynomial(1)')
$.1 - 1
```


I also got it to Segfault.  Heh heh:


```
sage: time f = cyclotomic_polynomial(2^30)
sage.bin(3624) malloc: *** error for object 0x6b089e0: incorrect checksum for freed object - object was probably modified after being freed.
*** set a breakpoint in malloc_error_break to debug
sage.bin(3624) malloc: *** error for object 0x6b0cb90: incorrect checksum for freed object - object was probably modified after being freed.
*** set a breakpoint in malloc_error_break to debug


------------------------------------------------------------
Unhandled SIGSEGV: A segmentation fault occured in SAGE.
This probably occured because a *compiled* component
of SAGE has a bug in it (typically accessing invalid memory)
or is not properly wrapped with _sig_on, _sig_off.
You might want to run SAGE under gdb with 'sage -gdb' to debug this.
SAGE will now terminate (sorry).
------------------------------------------------------------

```


Fix the above 2, and it's a positive review.


---

Attachment

Fixes area attached.


---

Comment by malb created at 2008-04-01 12:07:29

I really have no horses in this race.


---

Comment by malb created at 2008-04-01 12:07:29

Changing assignee from malb to robertwb.


---

Comment by mabshoff created at 2008-04-01 12:35:22

So far so good:

```
sage: cyclotomic_polynomial(1)
x - 1
sage: cyclotomic_polynomial(2^45)
---------------------------------------------------------------------------
<type 'exceptions.MemoryError'>           Traceback (most recent call last)

/scratch/mabshoff/release-cycle/sage-3.0.alpha0/<ipython console> in <module>()

/scratch/mabshoff/release-cycle/sage-3.0.alpha0/local/lib/python2.5/site-packages/sage/misc/functional.py in cyclotomic_polynomial(n, var)
    199     """
    200     return sage.rings.all.PolynomialRing(\
--> 201                   sage.rings.all.ZZ, name=var).cyclotomic_polynomial(n)
    202
    203 def decomposition(x):

/scratch/mabshoff/release-cycle/sage-3.0.alpha0/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_ring.py in cyclotomic_polynomial(self, n)
    594             return self.gen() - 1
    595         else:
--> 596             return self(cyclotomic.cyclotomic_coeffs(n), check=True)
    597
    598     def gen(self, n=0):

/scratch/mabshoff/release-cycle/sage-3.0.alpha0/cyclotomic.pyx in sage.rings.polynomial.cyclotomic.cyclotomic_coeffs()

<type 'exceptions.MemoryError'>: Not enough memory to calculate cyclotomic polynomial of 35184372088832
```


I tried `cyclotomic_polynomial(2^30)` on sage.math, but killed it when it started to consume more than 16GB of RAM. So can somebody please check on as 32 bit platform?

But: it causes doctest trouble for me:

```
sage -t -long devel/sage/sage/rings/polynomial/polynomial_ring.py: 1 doctests failed
sage -t -long devel/sage/sage/rings/polynomial/cyclotomic.pyx: 1 doctests failed
sage -t -long devel/sage/sage/combinat/sf/hall_littlewood.py: 16 doctests failed
sage -t -long devel/sage/sage/combinat/schubert_polynomial.py: 4 doctests failed
```


Cheers,

Michael


---

Comment by cremona created at 2008-04-01 12:58:17

These examples (powers of two) show very clearly what I was talking about.  The `2^n'th` cyclotomic polynomial is `x<sup>(2</sup>(n-1))+1` which is obtained by taking x+1 and replacing x by `x<sup>(2</sup>(n-1))`.  This should be trivial for sparse polys, and one would expect a fatal explosion for dense polys.

I'll try it on my 32 bit machine now.


---

Comment by cremona created at 2008-04-01 15:08:10

This is on a 32-bit machine (Linux fermat 2.6.22-14-generic #1 SMP Tue Feb 12 07:42:25 UTC 2008 i686 GNU/Linux)



```
----------------------------------------------------------------------
----------------------------------------------------------------------
Loading SAGE library. Current Mercurial branch is: cyclo
sage: time f=cyclotomic_polynomial(2^26)
CPU times: user 0.70 s, sys: 0.54 s, total: 1.24 s
Wall time: 1.24
sage: time f=cyclotomic_polynomial(2^27)
excessive length in vector::SetLength
/home/jec/sage-2.11/local/bin/sage-sage: line 214: 30105 Aborted                 (core dumped) sage-ipython "$`@`" -c "$SAGE_STARTUP_COMMAND;"
```

| SAGE Version 2.11, Release Date: 2008-03-30                        |
| Type notebook() for the GUI, and license() for information.        |
By the way, there's a huge time penalty in displaying the results of (say) `cyclotomic_polynomial(2^26)`, after the wall time is displayed and before the poly itself is (which is why in the above clip I assigned the result to a variable instead of outputting it).  I supect that the output takes time O(degree) instead of O(number-of-terms).  If that is true, can it be fixed?


---

Comment by robertwb created at 2008-04-01 20:22:05

The SetLength crash is an NTL issue (NTL has a limit on how large polynomials can be, one can duplicate the error trying to make x<sup>{(2</sup>30)} directly by doing


```
sage: ZZ['x']({2^30: 1})
overflow in SetCoeff
/Users/robert/sage/current/local/bin/sage-sage: line 222: 13929 Abort trap              sage-ipython "$`@`" -c "$SAGE_STARTUP_COMMAND;"
```


I'll make it throw an error instead of crashing in this case. Does anyone know what the NTL limit is for polynomial degrees? 

Printing taking a long time is a more involved problem, but the real issue here is that we don't have sparse univariate polynomials. 

I'll look at the doctests too, it's strange 'cause I didn't change anything that should have affected combinat.


---

Comment by cremona created at 2008-04-01 21:12:33

Replying to [comment:14 robertwb]:
> The SetLength crash is an NTL issue (NTL has a limit on how large polynomials can be, one can duplicate the error trying to make x<sup>{(2</sup>30)} directly by doing
> 
> {{{
> sage: ZZ['x']({2^30: 1})
> overflow in SetCoeff
> /Users/robert/sage/current/local/bin/sage-sage: line 222: 13929 Abort trap              sage-ipython "$`@`" -c "$SAGE_STARTUP_COMMAND;"
> }}}
> 
> I'll make it throw an error instead of crashing in this case. Does anyone know what the NTL limit is for polynomial degrees? 
> 

No such limit is mentioned at http://www.shoup.net/ntl/doc/ZZX.txt

> Printing taking a long time is a more involved problem, but the real issue here is that we don't have sparse univariate polynomials. 
> 
> I'll look at the doctests too, it's strange 'cause I didn't change anything that should have affected combinat.


---

Attachment


---

Attachment

I implemented fast printing for `ZZ[x]`, but the generic case could be done better in some cases and I didn't touch that. 

As for the limit, it's buried in ntl/include/ctools.h. 


```
#define NTL_OVFBND (1L << (NTL_BITS_PER_LONG-4))
```


which is now checked for (rather than inducing a crash). Also, the failing doctests are fixed.


---

Comment by cremona created at 2008-04-02 21:21:59

I have succesfully applied the last two patches and tested them, and am very happy with this now.
All four patches are needed!


---

Comment by mabshoff created at 2008-04-04 13:00:59

I am seeing one doctest failure with all four patches applied on sage.math:

```
sage-3.0.alpha1$ ./sage -t -long devel/sage/sage/rings/polynomial/polynomial_integer_dense_ntl.pyx
sage -t -long devel/sage/sage/rings/polynomial/polynomial_integer_dense_ntl.pyx
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.0.alpha1/tmp/polynomial_integer_dense_ntl.py", line 131:
    sage: ZZ['x']({2^3: 1})
Expected:
    x^8
    Traceback (most recent call last):
    ...
    OverflowError: Dense NTL integer polynomials have a maximum degree of 268435455
Got:
    x^8
**********************************************************************
```


I would assume this is a 32bit vs. 64bit issue. Man, it is time for FLINT to take over Z[x].

Cheers,

Michael


---

Attachment


---

Comment by robertwb created at 2008-04-04 18:24:24

Yes, I didn't have a 64 bit tests in the doctest, so the docstring got mangled. I posted a patch to address this issue.


---

Comment by mabshoff created at 2008-04-04 18:58:31

Yep. That fixes the issue for me. Positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-04-04 19:39:49

Merged in Sage 3.0.alpha1


---

Comment by mabshoff created at 2008-04-04 19:39:49

Resolution: fixed
