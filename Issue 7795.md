# Issue 7795: MPolynomialRing segfaults when getting high exponents

Issue created by migration from Trac.

Original creator: SimonKing

Original creation time: 2009-12-30 11:05:21

Assignee: malb

Keywords: MPolynomialRing_libsingular segfault with high exponents

In the following example, a segfault occurs. Shouldn't an error be raised instead?

```
sage: F.<a> = FiniteField(3)
sage: P.<T,z> = PolynomialRing(F)
sage: type(P)
<type 'sage.rings.polynomial.multi_polynomial_libsingular.MPolynomialRing_libsingular'>
sage: z^(3^10)
z^59049
sage: z^(3^11)
z^177147
sage: (z^3 + T*z)^(3^4)
z^243 + T^81*z^81
sage: (z^3 + T*z)^(3^7)
z^6561 + T^2187*z^2187
sage: (z^3 + T*z)^(3^10)
z^177147 + T^59049*z^59049
sage: (z^3 + T*z)^(3^15)
/home/king/SAGE/sage-4.3/local/bin/sage-sage: line 206: 20938 Segmentation fault      sage-ipython "$`@`" -i
```




---

Comment by malb created at 2010-07-14 21:49:10

Changing status from new to needs_review.


---

Comment by SimonKing created at 2010-07-15 20:27:07

The patch does not provide tests for the new functionality. Can these be added, please?

Anyway. The patch applies, sage builds and starts. I'll now do `sage -testall`. Then I'll try some timings involving exponentiation and multiplication. And, unless Martin is quicker, I'll try to add doc tests.


---

Comment by SimonKing created at 2010-07-15 21:22:32

Changing status from needs_review to needs_work.


---

Comment by SimonKing created at 2010-07-15 21:22:32

I did `sage -tp 2 devel/sage` and obtained

```
The following tests failed:

        sage -t  devel/sage/sage/rings/polynomial/multi_polynomial_libsingular.pyx # 1 doctests failed
        sage -t  devel/sage/sage/rings/polynomial/laurent_polynomial_ring.py # 89 doctests failed
        sage -t  devel/sage/sage/rings/polynomial/laurent_polynomial.pyx # 123 doctests failed
        sage -t  devel/sage/sage/combinat/kazhdan_lusztig.py # 5 doctests failed
        sage -t  devel/sage/sage/algebras/iwahori_hecke_algebra.py # 17 doctests failed
```


At least in one case, it seems that in some places one needed to add further arguments to ring constructors.


---

Comment by malb created at 2010-07-15 22:47:50

Fixes all but one doctest failure.


---

Comment by malb created at 2010-07-16 09:15:46

Changing status from needs_work to needs_review.


---

Comment by SimonKing created at 2010-07-21 14:05:33

Some random timings:

Without the patch

```
sage: R.<x,y,z> = GF(3)[]
sage: p = R.random_element()
sage: p
-y^2 + x*z - z^2 - z
sage: timeit('q=p^100')
125 loops, best of 3: 6.24 ms per loop
```


With the new patch and the same polynomial, I get:

```
sage: timeit('q=p^100')
125 loops, best of 3: 2.99 ms per loop
```


So, this is already good news!

Criticism: The patch still does not provide doctests showing that the problem is fixed. I am now running doctests, and if they pass, I'll try to add a proper doctest via reviewer patch.


---

Comment by SimonKing created at 2010-07-21 16:56:33

Changing status from needs_review to needs_work.


---

Comment by SimonKing created at 2010-07-21 16:56:33

The original problem -- namely the segfault when doing `(z^3 + T*z)<sup>(3</sup>15)` is not resolved. It segfaults, even with the patch.


---

Comment by malb created at 2012-03-24 14:16:00

Changing status from needs_work to needs_info.


---

Comment by malb created at 2012-03-24 14:16:00

* I reported this bug upstream as it seems to be an upstream bug
 * I deleted the attachment because I moved that code to #12718


---

Comment by malb created at 2012-03-26 11:31:16

Hans posted a fix here: https://groups.google.com/group/libsingular-devel/msg/39fe65f67ae44ca2?hl=en


---

Comment by Bouillaguet created at 2012-12-30 17:44:28

Apparently, this bug is fixed in sage 5.5. I could run `(z^3 + T*z)<sup>(3</sup>15)` and it gives the expected answer (after... 9h of computation of a fast machine !). I thus suggest we close this ticket... I don't know how we could doctest that though without running a test for hours.


---

Comment by Bouillaguet created at 2012-12-30 17:44:28

Changing status from needs_info to needs_review.


---

Comment by Bouillaguet created at 2012-12-31 10:02:23

NOTE : it worked on a 64-bit machine.


---

Comment by Bouillaguet created at 2013-01-04 16:55:45

Changing status from needs_review to positive_review.


---

Comment by Bouillaguet created at 2013-01-04 16:55:45

This cannot possibly be doctested, so we might as well close this.


---

Comment by jdemeyer created at 2013-01-04 20:43:02

In this case, please set the milestone to sage-duplicate/invalid/wontfix.


---

Comment by SimonKing created at 2013-01-04 21:53:54

Replying to [comment:13 Bouillaguet]:
> This cannot possibly be doctested, so we might as well close this.

I disagree, in two regards.

First of all, if no error is raised and no crash occurs, then apparently the example is different. Could be a 32-bit versus 64-bit problem. Or not? I don't think that the problem I originally reported was 32 bit.

So, one should try to find an example in which a segfault used to occur, but an error is raised now. Can someone please test whether the following segfaults with sage-4.3?

```
sage: F.<a> = FiniteField(3)
sage: P.<T,z> = PolynomialRing(F)
sage: (T+z)^(5^15)
Traceback (most recent call last):
...
OverflowError: Exponent overflow (30517578125).
```


If that test segfaults in old Sage versions, then it is a valid test (in particular, those types of bugs _can_ be tested against).

So, who has old Sage versions hanging around?


---

Comment by SimonKing created at 2013-01-04 21:57:07

Replying to [comment:15 SimonKing]:
> So, who has old Sage versions hanging around?

Unfortunately, with sage-4.7.beta1, the error is already raised (i.e., no segfault).


---

Comment by SimonKing created at 2013-01-04 22:01:34

I am now building sage-3.4.1, from which I found the sources somewhere on my machines...


---

Comment by SimonKing created at 2013-01-04 22:01:50

Changing status from positive_review to needs_info.


---

Comment by Bouillaguet created at 2013-01-06 09:15:35

Replying to [comment:15 SimonKing]:
> First of all, if no error is raised and no crash occurs, then apparently the example is different. 

I don't think so. My understanding is that the problem has been fixed inside [lib]singular. Testing this particular example is difficult because the computation takes many hours. It used to crash, but it now works.


---

Comment by rws created at 2014-03-16 08:45:41

Changing status from needs_info to needs_review.


---

Comment by mmezzarobba created at 2014-03-16 09:16:09

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2014-03-19 04:36:16

Resolution: fixed
