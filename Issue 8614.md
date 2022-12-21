# Issue 8614: Optimize creation of modular symbols spaces by speeding up quotienting out by 2-term relations

Issue created by migration from Trac.

Original creator: was

Original creation time: 2010-03-27 03:29:42

Assignee: craigcitro

CC:  alexghitza

* The attached patch speeds up a creating ModularSymbols spaces a bunch by removing a bottleneck -- quotienting by 2-term relations -- by moving it to Cython. 

* Also the coverage for the modsym directory is improved to 100% by adding one trivial missing doctest.


---

Attachment


---

Comment by was created at 2010-03-27 03:44:06

Changing status from new to needs_review.


---

Comment by davidloeffler created at 2010-03-27 13:54:47

Which cases do you expect to be most speeded up by this patch? I ran some tests and it actually seems to make things marginally _slower_ in the cases I tried:

Before:

```
sage: time ModularSymbols(2002, 2)
CPU times: user 1.52 s, sys: 0.41 s, total: 1.93 s
Wall time: 1.93 s
Modular Symbols space of dimension 673 for Gamma_0(2002) of weight 2 with sign 0 over Rational Field
sage: time ModularSymbols(302, 4)
CPU times: user 2.21 s, sys: 0.00 s, total: 2.21 s
Wall time: 2.21 s
Modular Symbols space of dimension 228 for Gamma_0(302) of weight 4 with sign 0 over Rational Field
sage: time ModularSymbols(Gamma1(33), 4)
CPU times: user 3.04 s, sys: 0.46 s, total: 3.49 s
Wall time: 3.49 s
Modular Symbols space of dimension 240 for Gamma_1(33) of weight 4 with sign 0 and over Rational Field
sage: time ModularSymbols(DirichletGroup(308).0, 5)
CPU times: user 5.94 s, sys: 0.65 s, total: 6.59 s
Wall time: 6.59 s
Modular Symbols space of dimension 384 and level 308, weight 5, character [-1, 1, 1], sign 0, over Rational Field
```


After:

```
sage: time ModularSymbols(2002, 2)
CPU times: user 1.52 s, sys: 0.67 s, total: 2.19 s
Wall time: 2.19 s
Modular Symbols space of dimension 673 for Gamma_0(2002) of weight 2 with sign 0 over Rational Field
sage: time ModularSymbols(302, 4)
CPU times: user 2.12 s, sys: 0.18 s, total: 2.30 s
Wall time: 2.30 s
Modular Symbols space of dimension 228 for Gamma_0(302) of weight 4 with sign 0 over Rational Field
sage: time ModularSymbols(Gamma1(33), 4)
CPU times: user 2.66 s, sys: 0.90 s, total: 3.57 s
Wall time: 3.57 s
Modular Symbols space of dimension 240 for Gamma_1(33) of weight 4 with sign 0 and over Rational Field
sage: time ModularSymbols(DirichletGroup(308).0, 5)
CPU times: user 5.97 s, sys: 0.71 s, total: 6.68 s
Wall time: 6.68 s
Modular Symbols space of dimension 384 and level 308, weight 5, character [-1, 1, 1], sign 0, over Rational Field
```



---

Comment by AlexGhitza created at 2010-04-03 06:37:10

Changing status from needs_review to needs_info.


---

Comment by AlexGhitza created at 2011-01-18 00:08:36

It appears to be significantly better for high weights:

On sage-4.6.1, before the patch:


```
sage: time M = ModularSymbols(1, 810, 0, GF(809))
CPU times: user 51.57 s, sys: 0.45 s, total: 52.02 s
Wall time: 52.03 s
```


After the patch:


```
sage: time M = ModularSymbols(1, 810, 0, GF(809))
CPU times: user 16.40 s, sys: 0.17 s, total: 16.57 s
Wall time: 16.58 s
```


This makes me *very* happy.


---

Comment by davidloeffler created at 2011-01-26 14:01:38

According to the profiler, that difference seems to be coming almost entirely from the optimizations to `binomial`. The much larger chunk of new code in `relation_matrix.pyx` code only gets called when (among other conditions) the base ring is the rationals; and it doesn't seem to make much of an impact on the speed.

I suggest we split this into two tickets: one for the changes to binomial and the other miscellaneous fixes, which I would be happy to give a positive review to on the spot, and the other for the cythonization of the 2-term relations stuff, which seems a bit less clear-cut to me.


---

Comment by AlexGhitza created at 2011-01-26 14:27:12

Replying to [comment:7 davidloeffler]:
> According to the profiler, that difference seems to be coming almost entirely from the optimizations to `binomial`. The much larger chunk of new code in `relation_matrix.pyx` code only gets called when (among other conditions) the base ring is the rationals; and it doesn't seem to make much of an impact on the speed.
> 
> I suggest we split this into two tickets: one for the changes to binomial and the other miscellaneous fixes, which I would be happy to give a positive review to on the spot, and the other for the cythonization of the 2-term relations stuff, which seems a bit less clear-cut to me.

I agree, and I had noticed the point about `binomial` myself.  It's late (or really early) here, but I'll try to split off the easier bits tomorrow.


---

Comment by AlexGhitza created at 2011-01-26 14:27:12

Changing status from needs_info to needs_work.


---

Comment by AlexGhitza created at 2011-01-29 06:06:39

OK, so I have split off the part not directly involved in the 2-term relations into two other tickets: #10709 for the binomial coefficients in the matrix actions on Manin symbols, and #10710 for the various docstring/doctest/comment fixes.

I will soon update the patch on this ticket by removing those parts.


---

Attachment

I rebased the patch to 4.7alpha2 (with #10709 applied). Its not true that the new code is slower. I ran the following small tests:


```
%time M = ModularSymbols(1000,2,sign=1).new_subspace().cuspidal_subspace()
%time t3 = M.hecke_matrix(3)
%time time d = t3.decomposition(algorithm='multimodular', height_guess=1)

%time ModularSymbols(2002, 2)
%time ModularSymbols(302, 4)
%time ModularSymbols(Gamma1(33), 4)
%time ModularSymbols(DirichletGroup(308).0, 5)
%time M = ModularSymbols(1, 810, 0, GF(809))
```


Without the patch:

```
Wall time: 2.92 s
Wall time: 0.19 s
Wall time: 0.09 s

Wall time: 1.34 s
Wall time: 4.08 s
Wall time: 2.20 s
Wall time: 10.97 s
Wall time: 16.23 s
```


With the patch applied:

```
Wall time: 2.77 s
Wall time: 0.13 s
Wall time: 0.09 s

Wall time: 1.22 s
Wall time: 4.38 s
Wall time: 2.10 s
Wall time: 11.12 s
Wall time: 15.33 s
```


None of the differences is significant in the sense that %timeit could reproduce it. A profile

```
%prun M = ModularSymbols(Gamma1(52), 4)
```

shows that indeed the new code is three times as fast as the old one. But since the relevant function only needs 0.1s and 0.03s, respectively, this can be hardly tracked.

Martin


---

Comment by mraum created at 2011-03-22 02:25:56

Changing status from needs_work to needs_review.


---

Comment by cremona created at 2011-03-25 19:55:22

The patch looks good to me (applied to 4.7.alpha2) and I am testing now, by testing whether ModularSymbols(N) and CremonaModularSymbols(N) have the same dimension for N up to `10^4`.  And some more.


---

Comment by cremona created at 2011-03-25 22:10:26

Replying to [comment:11 cremona]:
> The patch looks good to me (applied to 4.7.alpha2) and I am testing now, by testing whether ModularSymbols(N) and CremonaModularSymbols(N) have the same dimension for N up to `10^4`.  And some more.


```
sage: time a=[CremonaModularSymbols(N).dimension() for N in [1000..2000]]
CPU times: user 31.12 s, sys: 0.52 s, total: 31.64 s
Wall time: 31.68 s
sage: time b=[ModularSymbols(N).dimension() for N in [1000..2000]]       
CPU times: user 636.90 s, sys: 0.14 s, total: 637.04 s
Wall time: 637.91 s
sage: a==b
True
```


This is enough to convince me that the implementation is ok.  I tested the complete library too.


---

Comment by cremona created at 2011-03-25 22:10:26

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2011-04-13 07:42:29

Resolution: fixed
