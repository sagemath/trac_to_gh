# Issue 4533: divisors function slow for integers

Issue created by migration from https://trac.sagemath.org/ticket/4533

Original creator: robertwb

Original creation time: 2008-11-16 08:21:30

Assignee: tbd

CC:  craigcitro

There's *tons* of room for optimization for the divisors function in sage/rings/arith.py. This should probably be generalized to do more than integers, with a specialized divisors method on Integer. 


---

Comment by robertwb created at 2008-11-16 08:28:17

A comparison


```
sage: n = odd_part(factorial(31))
sage: time _ = divisors(n)
CPU times: user 2.27 s, sys: 0.05 s, total: 2.32 s
Wall time: 2.33 s
sage: nn = gp(n)
sage: time _ = nn.divisors()
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
Wall time: 0.15 s
sage: 2.33 / .15
15.5333333333333
```



---

Comment by robertwb created at 2008-11-16 08:51:16

A much simpler and faster algorithm. I'm sure there's a faster, balanced algorithm, but this is a huge improvement over what is there.


---

Comment by robertwb created at 2008-11-16 09:27:13

Note that this works for more than integers now too:


```
sage: K.<a> = QuadraticField(7)
sage: divisors(K.ideal(7))
[1, Fractional ideal (-a), Fractional ideal (7)]
sage: divisors(K.ideal(3))
[1, Fractional ideal (a - 2), Fractional ideal (-a - 2), Fractional ideal (3)]
sage: divisors(K.ideal(35))
[1, Fractional ideal (5), Fractional ideal (-a), Fractional ideal (-5*a), Fractional ideal (7), Fractional ideal (35)]
```



---

Comment by mabshoff created at 2008-11-16 09:51:45

Replying to [comment:3 robertwb]:
> Note that this works for more than integers now too:

Shouldn't that example then be added to the docstrings, too? :)

Cheers,

Michael


---

Comment by robertwb created at 2008-11-16 09:56:55

Of course :). I've posted an updated patch.


---

Comment by was created at 2008-11-16 19:37:37

1. The new code isn't much faster, but it is certainly better.  Here are some before and after speed comparisons (core2 2.6Ghz 32-bit osx)

Before:

```
sage: n = odd_part(factorial(31))
sage: time _ = divisors(n)
CPU times: user 1.66 s, sys: 0.03 s, total: 1.70 s
Wall time: 1.73 s
sage: n = 928304029834092384082304982093480293849028349823948
sage: time _ = divisors(n)
CPU times: user 0.30 s, sys: 0.06 s, total: 0.35 s
Wall time: 0.46 s
sage: n = 9283040298340
sage: timeit('divisors(n)')
125 loops, best of 3: 1.75 ms per loop
```



After:

```
sage: n = odd_part(factorial(31))
sage: time _ = divisors(n)
CPU times: user 0.90 s, sys: 0.06 s, total: 0.96 s
Wall time: 0.98 s
sage: time a = gp(n).divisors()
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
Wall time: 0.21 s
sage: n = 928304029834092384082304982093480293849028349823948
sage: time _ = divisors(n)
CPU times: user 0.31 s, sys: 0.06 s, total: 0.37 s
Wall time: 0.40 s
sage: n = 9283040298340
sage: timeit('divisors(n)')
625 loops, best of 3: 341 µs per loop
```


2. It no longer works on int's, which is a serious problem (this used to work fine):


```
sage: divisors(int(5))
Traceback (most recent call last):
...
AttributeError: 'int' object has no attribute 'parent'
```


There should be a doctest about that.

For a positive review fix the code to work on int/long as input, and add a doctest about that.   Regarding speeding it up to be on par with pari, that should be another ticket that *must* be opened before closing this one.  Ideas regarding speed:

   * you can easily precompute the length of the output list as 

```
prod(e+1 for _,e in f)
```

   * If the input is an int < long long (or long), could do all arithmetic with
machine says data types, since you know a priori the biggest number that will appear.   This should be special cased.   
   * Interestingly, I changed two lines of the function so it uses Python int's instead of Sage MPFR ints everywhere and the function speeds up dramatically so it is almost as fast as pari:

```
    one = int(1)
    all = [one]
    for p, e in f:
        p = int(p)

...

sage: time d = divisors(n)
CPU times: user 0.23 s, sys: 0.02 s, total: 0.24 s
Wall time: 0.25 s
sage: time w = [ZZ(a) for a in d]
CPU times: user 0.24 s, sys: 0.01 s, total: 0.25 s
Wall time: 0.26 s
sage: time w = gp(n).divisors()
CPU times: user 0.00 s, sys: 0.01 s, total: 0.01 s
Wall time: 0.18 s
```


Interestingly, as you can see above, doing everything with python ints, then converting all the python ints back to sage ints, results in something that is *twice* as fast as your code on the same input. 


3. Other remarks: 

 * pari(n).divisors() gives an AttributeError, so I guess we never wrapped that. 

 * Why is odd_part(factorial(31)) a RATIONAL?  This seems really weird.

```
sage: n = odd_part(factorial(31))
sage: type(n)
<type 'sage.rings.rational.Rational'>
sage: type(factorial(31))
<type 'sage.rings.integer.Integer'>
```



---

Comment by cremona created at 2008-11-17 09:57:16

The new code looks very like my C++ functions in eclib (there for the taking!) which include various other options such as 
   * only poitive divisors vs. both signs
   * only divisors d such that `d^2|n`
which I did once need, and so on.

Just a comment.


---

Comment by robertwb created at 2008-11-17 17:55:43

I'll make those fixes, and write a special case for word-sized integers. It should be noted that *sorting* the output often takes the majority of the time


```
sage: sage: n = ZZ(odd_part(factorial(31)))
sage: sage: time _ = divisors(n)
CPU times: user 0.53 s, sys: 0.02 s, total: 0.54 s
Wall time: 0.55 s
sage: sage: time _ = divisors(n, sorted=False)
CPU times: user 0.15 s, sys: 0.02 s, total: 0.17 s
Wall time: 0.17 s

sage: n = factorial(25)
sage: time _ = divisors(n)
CPU times: user 1.07 s, sys: 0.05 s, total: 1.12 s
Wall time: 1.12 s
sage: time _ = divisors(n, sorted=False)
CPU times: user 0.33 s, sys: 0.05 s, total: 0.38 s
Wall time: 0.38 s
```


Originally I wasn't sorting the output, which was why I thought I was so much faster. (The original code sorted the output too, but it was slow enough that the sorting didn't dominate.)


---

Comment by was created at 2008-11-18 06:29:55

> It should be noted that *sorting* the output often takes the majority of the time 

This is perhaps partly because sorting lists of GMP integers is slower than Python ints, i.e., it takes about twice as long to do a comparison:


```
sage: n = ZZ(odd_part(factorial(31)))
sage: 
sage: m = divisors(n, sorted=False)
sage: m2 = [int(j) for j in m]
sage: time m.sort()
CPU times: user 0.33 s, sys: 0.00 s, total: 0.34 s
Wall time: 0.34 s
sage: time m2.sort()
CPU times: user 0.16 s, sys: 0.00 s, total: 0.17 s
Wall time: 0.17 s
sage: a = 349; b = 678
sage: timeit('a < b')
625 loops, best of 3: 389 ns per loop
sage: a = int(349); b = int(678)
sage: timeit('a < b')
625 loops, best of 3: 213 ns per loop
```


In the timeits at the bottom, probably 100ns is spent just looking up a and b in the globals...

Anyway, some of the ints for the divisors of n above are beyond long long, so this word size discussion doesn't apply.  However, if we consider 25, notice that sorted
takes twice as long as computing the divisors:

```
sage: n = ZZ(odd_part(factorial(25)))
sage: time m = divisors(n,sorted=False)
CPU times: user 0.01 s, sys: 0.00 s, total: 0.01 s
Wall time: 0.01 s
sage: v = [int(a) for a in m]
sage: time v.sort()    # no better (see below).
CPU times: user 0.02 s, sys: 0.00 s, total: 0.02 s
Wall time: 0.02 s
sage: v = numpy.array(m).astype(numpy.int64)
sage: time v.sort()
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
Wall time: 0.00 s
sage: time m.sort()
CPU times: user 0.02 s, sys: 0.00 s, total: 0.02 s
Wall time: 0.02 s
```


However, sorting using an numpy int64 array seems to be much faster than sorting a list of GMP ints.  So if we just use some straightforward sort on a Cython long long* we should get good results. 

Unrelated: I noticed that n.divisors(...) doesn't have a sorted option.  So maybe some code in integer.pyx should be slightly changed.


---

Comment by robertwb created at 2008-11-18 06:42:07

Yep. I plan to specialize Integer.divisors() and attempt to call that in the top-level divisors function. It will have a much faster sort. 

I'm wondering though if the default should be sorted, or if one should use `sorted(divisors(n))` if one wants them in order.


---

Comment by robertwb created at 2008-11-18 23:40:09

OK, here's another patch that should resolve all of the above issues. One of the doctests depends on #4534 (odd_part returning an integer rather than a rational).


---

Comment by robertwb created at 2008-11-20 13:04:51

I updated the patch, now its faster than pari. 

There is a dependancy on #4564 for long long -> mpz_t.


---

Comment by was created at 2008-11-20 17:40:37

Is it "faster than Magma" too?    Could you do some timings?


---

Comment by robertwb created at 2008-11-20 20:26:20

Surprisingly, magma isn't super good at this problem. All timings on sage.math


```
sage: n = factorial(20)
sage: %timeit v = n.divisors()
100 loops, best of 3: 15.6 ms per loop

sage: pari_n = gp(n)
sage: %timeit v = pari_n.divisors()
10 loops, best of 3: 57.2 ms per loop

sage: magma_n = magma(n)
sage: %timeit v = magma_n.Divisors()
10 loops, best of 3: 43.5 ms per loop


sage: n = factorial(31) // 2^26
sage: %timeit v = n.divisors()
10 loops, best of 3: 145 ms per loop

sage: pari_n = gp(n)
sage: %timeit v = pari_n.divisors()
10 loops, best of 3: 408 ms per loop

sage: magma_n = magma(n)
sage: %timeit v = magma_n.Divisors()
10 loops, best of 3: 684 ms per loop
```



---

Attachment


---

Comment by mabshoff created at 2008-11-21 07:48:13

Another oops:

```
sage -t -long devel/sage/sage/combinat/species/species.py
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.2.1.alpha0/devel/sage-main/sage/combinat/species/species.py", line 292:
    sage: G.isotype_generating_series().coefficients(5)
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/release-cycle/sage-3.2.1.alpha0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mabshoff/release-cycle/sage-3.2.1.alpha0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mabshoff/release-cycle/sage-3.2.1.alpha0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_12[7]>", line 1, in <module>
        G.isotype_generating_series().coefficients(Integer(5))###line 292:
    sage: G.isotype_generating_series().coefficients(5)
      File "/scratch/mabshoff/release-cycle/sage-3.2.1.alpha0/local/lib/python2.5/site-packages/sage/combinat/species/series.py", line 668, in coefficients
        return [self.coefficient(i) for i in range(n)]
      File "/scratch/mabshoff/release-cycle/sage-3.2.1.alpha0/local/lib/python2.5/site-packages/sage/combinat/species/series.py", line 830, in coefficient
        return self._stream[n]
      File "/scratch/mabshoff/release-cycle/sage-3.2.1.alpha0/local/lib/python2.5/site-packages/sage/combinat/species/stream.py", line 311, in __getitem__
        self._list.append(self._gen.next())
      File "/scratch/mabshoff/release-cycle/sage-3.2.1.alpha0/local/lib/python2.5/site-packages/sage/combinat/species/generating_series.py", line 428, in _ogs_gen
        yield sum( self.coefficient(i).coefficients() )
      File "/scratch/mabshoff/release-cycle/sage-3.2.1.alpha0/local/lib/python2.5/site-packages/sage/combinat/species/series.py", line 830, in coefficient
        return self._stream[n]
      File "/scratch/mabshoff/release-cycle/sage-3.2.1.alpha0/local/lib/python2.5/site-packages/sage/combinat/species/stream.py", line 311, in __getitem__
        self._list.append(self._gen.next())
      File "/scratch/mabshoff/release-cycle/sage-3.2.1.alpha0/local/lib/python2.5/site-packages/sage/combinat/species/generating_series.py", line 506, in _functorial_compose_gen
        t = g._cycle_type(s)
      File "/scratch/mabshoff/release-cycle/sage-3.2.1.alpha0/local/lib/python2.5/site-packages/sage/combinat/species/generating_series.py", line 530, in _cycle_type
        for d in divisors(k):
      File "/scratch/mabshoff/release-cycle/sage-3.2.1.alpha0/local/lib/python2.5/site-packages/sage/rings/arith.py", line 924, in divisors
        n = integer_ring.ZZ(n) # we have specalized code for this case, make sure it gets used
    NameError: global name 'integer_ring' is not defined
**********************************************************************
```

The problem pops up in a lot of places.

Cheers,

Michael


---

Comment by mabshoff created at 2008-11-21 08:09:15


```
[11:56pm] craigcitro: mabshoff: there's an easy fix for the problem in #4533
[11:56pm] craigcitro: it's a rebase issue
[11:56pm] mabshoff_: mk
[11:56pm] mabshoff_: if you can rebase the patch it would be cool.
[11:56pm] craigcitro: integer_ring. occurs in the patch
[11:56pm] craigcitro: just delete that.
[11:56pm] mabshoff_: I didn't even look yet
[11:56pm] mabshoff_: ?
[11:56pm] mabshoff_: Let me see
[11:56pm] craigcitro: it refers to
[11:56pm] craigcitro: integer_ring.ZZ
[11:57pm] craigcitro: it should just be ZZ
[11:57pm] craigcitro: it's something i cleaned up when i did stuff to arith.py
[11:57pm] craigcitro: but rob was using 3.1.4 when he wrote the patch
[11:57pm] craigcitro: and it's hitting a case we didn't think to try once it was rebased, probably
[11:57pm] mabshoff_: mk
[11:58pm] craigcitro: actually, i also just spotted a minor issue in that file
[11:58pm] craigcitro: where memory is only freed in one case ...
[11:58pm] mabshoff_: ok:
[11:58pm] mabshoff_: +    if R in [int, long]:
[11:58pm] mabshoff_: +        n = ZZ(n) # we have specalized code for this case, make sure it gets used
[11:58pm] mabshoff_: +    try:
[11:58pm] craigcitro: yep
[11:58pm] mabshoff_: Well, post a new patch and I will test it.
[11:58pm] craigcitro: that should fix the problem you were hitting
[11:59pm] craigcitro: it's just outdenting one line 
[11:59pm] craigcitro: the sage_free(ptr)
[11:59pm] craigcitro: should be one level back
[11:59pm] craigcitro: oh, wait
[11:59pm] craigcitro: nevermind
[11:59pm] craigcitro: he already takes care of it somewhere else in the code.
[12:00am] craigcitro: so that's not an issue.
[12:00am] mabshoff_: Arrg, I just deleted the edited patch 
[12:00am] craigcitro: doh
[12:02am] mabshoff_: Well, I can fix it.
```



---

Comment by mabshoff created at 2008-11-21 08:47:47

Resolution: fixed


---

Comment by mabshoff created at 2008-11-21 08:47:47

Merged the edited patch in Sage 3.2.1.alpha0
