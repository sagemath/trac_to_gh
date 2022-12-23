# Issue 6020: bug in delta_qexp over finite fields

Issue created by migration from https://trac.sagemath.org/ticket/6020

Original creator: AlexGhitza

Original creation time: 2009-05-11 12:08:47

Assignee: craigcitro

Keywords: delta q-expansion finite field

This is in sage-3.4.2:


```
sage: delta_qexp(K=GF(5))
TypeError                                 Traceback (most recent call last)
...
TypeError: unable to coerce <type 'sage.libs.ntl.ntl_ZZX.ntl_ZZX'> to an integer
```


I don't have time to investigate this right now, but it might be a similar issue as #5102.



---

Attachment


---

Comment by craigcitro created at 2009-05-11 17:03:42

Okay, I've attached a patch. The issue is that we can't coerce from NTL into a finite field.

This patch isn't anything too clever -- I just do the naive thing and work over the base ring from the start instead of using NTL. It runs at the same speed for `100000` terms, and only loses about `3%` performance at `1000000`, so this should definitely do the job. I'm happy to come back and either unify these (maybe we don't need to manually use NTL anymore?) or do some additional work to speed it up in the finite field case later on.


---

Comment by was created at 2009-05-12 06:55:14

Wait a minute:  
Changing 

```
 if K is ZZ:
```

to

```
 if False and K is ZZ:
```

results in code that is way *faster*!  That's because FLINT kick's NTL's ass, and FLINT is the default for poly's over ZZ now.  Just get rid of the flint implementation.

With NTL (on my OS X laptop):

```
sage: time b = delta_qexp(50000)
CPU times: user 0.44 s, sys: 0.00 s, total: 0.44 s
Wall time: 0.44 s
sage: time b = delta_qexp(100000)
CPU times: user 1.07 s, sys: 0.07 s, total: 1.14 s
Wall time: 1.14 s
sage: time b = delta_qexp(200000)
CPU times: user 2.65 s, sys: 0.06 s, total: 2.71 s
Wall time: 2.72 s
```


With the "False" as above inserted, so FLINT gets used:

```
sage: time b = delta_qexp(50000)
CPU times: user 0.21 s, sys: 0.08 s, total: 0.29 s
Wall time: 0.30 s
sage: time b = delta_qexp(100000)
CPU times: user 0.58 s, sys: 0.12 s, total: 0.70 s
Wall time: 0.70 s
sage: time b = delta_qexp(200000)
CPU times: user 1.35 s, sys: 0.33 s, total: 1.68 s
Wall time: 1.68 s
```



---

Comment by craigcitro created at 2009-05-12 07:22:17

This is pretty interesting: I get entirely different timings on my laptop, which is why I didn't remove the NTL code. I wonder if something funky went on with my FLINT compilation?

The `NTL` version:


```
sage: time b = delta_qexp(50000)
CPU times: user 0.50 s, sys: 0.02 s, total: 0.52 s
Wall time: 0.53 s

sage: time b = delta_qexp(100000)
CPU times: user 1.04 s, sys: 0.04 s, total: 1.08 s
Wall time: 1.15 s

sage: time b = delta_qexp(200000)
CPU times: user 2.08 s, sys: 0.09 s, total: 2.18 s
Wall time: 2.20 s
```


The `FLINT` version:


```
sage: time b = delta_qexp(50000)
CPU times: user 1.01 s, sys: 0.35 s, total: 1.36 s
Wall time: 1.37 s

sage: time b = delta_qexp(100000)
CPU times: user 2.08 s, sys: 0.70 s, total: 2.78 s
Wall time: 2.81 s

sage: time b = delta_qexp(200000)
CPU times: user 4.34 s, sys: 1.46 s, total: 5.80 s
Wall time: 5.88 s
```


That seems really weird ... I'm going to try looking at this tomorrow when I'm sitting next to you. This is kinda weird; I'd like to do some random timing comparisons.


---

Comment by davidloeffler created at 2009-05-12 09:20:15

On my 32-bit Linux laptop, I get these timings:

With NTL:


```
sage: sage: time b = delta_qexp(50000)
CPU times: user 0.95 s, sys: 0.04 s, total: 0.99 s
Wall time: 1.01 s
sage: sage: time b = delta_qexp(100000)
CPU times: user 2.03 s, sys: 0.04 s, total: 2.06 s
Wall time: 2.08 s
sage: sage: time b = delta_qexp(200000)
CPU times: user 4.46 s, sys: 0.13 s, total: 4.59 s
Wall time: 4.91 s
```


With FLINT, i.e. with the "if False" hack:


```
sage: sage: time b = delta_qexp(50000)
CPU times: user 0.76 s, sys: 0.07 s, total: 0.83 s
Wall time: 0.85 s
sage: sage: time b = delta_qexp(100000)
CPU times: user 1.62 s, sys: 0.16 s, total: 1.78 s
Wall time: 1.79 s
sage: sage: time b = delta_qexp(200000)
CPU times: user 3.50 s, sys: 0.40 s, total: 3.91 s
Wall time: 4.03 s
```


So FLINT is faster for me (but not by so much as for William).


---

Comment by mabshoff created at 2009-05-14 05:27:10

What is the status here?

Cheers,

Michael


---

Comment by craigcitro created at 2009-05-14 05:56:54

I'm going to fix this soon, at SD15 if not before. (Me giving three talks during SD15 may prevent it from happening before.)

Here's the status, though: we've discovered that on 64-bit OSX and on `sage.math`, it's much faster to just call the naive code (the `else` clause in the patch above. However, it's *slower* on 32-bit OSX. So I looked at the code a little more, and we're spending a fair amount of time doing silly things (coercion, poor use of truncation, etc.). So I'm going to make a new ticket with some fixes/additions to the polynomial code, and then rewrite this patch to use these improvements. I suspect that it'll beat the old code on all architectures in that case (I'm basing this on some rough timings on my laptop), in which case we're all set.

I'm changing the status to something slightly snarky to summarize the above. :)


---

Comment by mraum created at 2010-04-09 17:11:10

As I said #6671 I merge this with the new code given there. I did some timings and the result is clear: Coercion into the new ring after using FLINT is fast.
Timeing:

```
sage: P = PowerSeriesRing(GF(7), 'q')
sage: from sage.modular.modform.vm_basis import _delta_poly

sage: %timeit P(_delta_poly(50).list(), check = True)
625 loops, best of 3: 407 µs per loop
sage: %timeit _delta_poly(50, GF(7))
625 loops, best of 3: 1.41 ms per loop

sage: %timeit P(_delta_poly(10**5).list(), check = True)
5 loops, best of 3: 620 ms per loop
sage: %timeit _delta_poly(10**5, GF(7))
5 loops, best of 3: 1.62 s per loop

sage: %timeit h = P(_delta_poly(10**6).list(), check = True)
5 loops, best of 3: 7.98 s per loop
sage: %timeit h =_delta_poly(10**6, GF(7))
5 loops, best of 3: 16.9 s per loop

```


I conclude that it is better to wait for Craig's new code. If nobody is opposed I will asked the current release manager (I think it's Minh) to make this as closed (since it is fixed by #6671).


---

Comment by davidloeffler created at 2010-04-12 14:10:52

Changing status from needs_work to needs_review.


---

Comment by davidloeffler created at 2010-04-12 14:11:05

Changing status from needs_review to positive_review.


---

Comment by jhpalmieri created at 2010-04-15 05:56:20

Resolution: worksforme


---

Comment by jhpalmieri created at 2010-04-15 05:56:20

Closed as requested (fixed by #6671).
