# Issue 9492: add computation of swinnerton-dyer polynomials to sage

Issue created by migration from https://trac.sagemath.org/ticket/9492

Original creator: was

Original creation time: 2010-07-13 22:40:49

Assignee: jason

CC:  mstreng

Magma has 'em, so we should to:

   http://magma.maths.usyd.edu.au/magma/htmlhelp/text306.htm

Sympy has them:
   

This page has a Mathematica notebook with a function that computes them:

   http://mathworld.wolfram.com/Swinnerton-DyerPolynomial.html

I tried it in Mathematica 7, and it is massively, dramatically *SLOW* compared to Magma.   For comparison, the 5th one takes 55 seconds in Mathematica, and in Magma it takes... 0.02 seconds.   


```
  n   time in seconds with Magma 2.15.11 on my macbook air
----------------
  5  | 0.02
  6  | 0.18
  7  | 6.68
  8  | 99.99 
```



---

Comment by was created at 2010-07-13 23:01:14

OK, I just wrote some Sage code from scratch that provably computes the swinnerton-dyer polynomials vastly more quickly than Magma or Mathematica.


---

Comment by was created at 2010-07-13 23:08:06

See also http://wiki.sagemath.org/days23/CodingProjects

In the attached file sd.sage, I implemented a few functions, and also copied in Jeroen Demeyer's p-adic function.  I think the interval arithmetic one (sdpoly3) is considerably faster than the p-adic one, and moreover sdpoly3 is provably correct.  It simply computes the poly using intervals until there is a unique integer in each interval.  So I think it should just be SAge-library-ified and put into sage... somewhere.


---

Attachment


---

Comment by was created at 2010-07-13 23:25:33

I think these are interesting because they are used in benchmarks for factoring and irreducibility testing.  See
  http://www.shoup.net/ntl/doc/tour-time.html

The sdpoly3 function computes the 10th Swinnerton-Dyer poly of degree 2^10=1024 in < 20 seconds. 

```
sage: time c = sdpoly3(10)
CPU times: user 17.02 s, sys: 0.05 s, total: 17.07 s
Wall time: 17.50 s
```



---

Attachment

I just adapted sdpoly3 to use a binary tree. The result is called sdpoly5, see file sd2.sage. I found sdpoly5 to be slightly faster than sdpoly3 in the tests that I have run.

When using naive polynomial multiplication, the algorithms sdpoly3 and sdpoly5 are asymptotically equivalent. As soon as FFT quasi-linear polynomial multiplication is implemented for interval arithmetic and examples become large, the algorithm sdpoly5 should be the faster one (quasi-linear).


```
sage: time sdpoly5(12)
CPU times: user 845.82 s, sys: 0.10 s, total: 845.92 s
Wall time: 846.13 s

sage: time sdpoly3(12)
CPU times: user 861.84 s, sys: 0.01 s, total: 861.85 s
Wall time: 861.98 s
```



---

Comment by was created at 2010-07-14 12:41:05

> I just adapted sdpoly3 to use a binary tree.

Thanks.  But just a remark -- the Sage prod command already uses a binary tree, at least if the input is a list or of length < 1000.    See the file

   devel/sage/sage/misc/misc_c.pyx

which Robert Bradshaw wrote.   So putting 

```
  prod(list( ... ))
```

instead of 


```
  prod( ...)
```


in sdpoly3 might be another approach.


---

Comment by was created at 2010-07-14 13:35:16

I'm at a Singular conference, so I decided to try this problem using Singular polynomial quotient rings.  It's pretty good, though it doesn't beat interval arithmetic speed-wise.

```
def sdpoly6(n):
    R = PolynomialRing(QQ,n+1,names='x')
    x = R.gens()
    v = primes_first_n(n)
    I = R.ideal([ x[i]^2-v[i] for i in range(len(v)) ])
    S = R.quotient(I)
    x = S.gens()
    C = cartesian_product_iterator([[-1,1]]*n)
    f = prod([ x[-1] + sum(s[i]*x[i] for i in range(n)) for s in C])
    return f
```


Some timings:

```
sage: time a = sdpoly6(8)
Time: CPU 0.71 s, Wall: 0.71 s
sage: time a = sdpoly6(9)
Time: CPU 3.44 s, Wall: 3.47 s
sage: time a10 = sdpoly6(10)
Time: CPU 29.03 s, Wall: 29.19 s
```


Very impressive for something non-numerical, IMHO...


---

Comment by fredrik.johansson created at 2013-06-14 16:20:08

FLINT now includes a function that computes the nth Swinnerton-Dyer polynomial. It could be wrapped trivially.


---

Comment by chapoton created at 2014-03-11 20:17:52

I have tried to wrap the flint function, but was not able to. Could someone more versed into interfaces do that ?
