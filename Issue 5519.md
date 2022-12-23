# Issue 5519: Irreducibility test is slow for polynomials over GF(2)

Issue created by migration from https://trac.sagemath.org/ticket/5519

Original creator: rhinton

Original creation time: 2009-03-14 20:43:10

Assignee: rhinton

CC:  malb zimmerma

The patch calls the NTL irreducibility test directly instead of depending on a generic algorithm.  It's not blazingly fast (e.g. Magma), but it's an improvement.

  R.<x> = GF(2)[]
  timeit('R.random_element(100).is_irreducible()')
  # before the change
  # 25 loops, best of 3: 16.2 ms per loop
  # after the change
  # 25 loops, best of 3: 3.36 ms per loop

  timeit('R.random_element(512).is_irreducible()')
  # before the change
  # 5 loops, best of 3: 323 ms per loop
  # after the change
  # 25 loops, best of 3: 18.7 ms per loop


---

Attachment

Is making it a `cpdef` function really necessary?

Also, I'm CCing Paul Zimmermann who would know about fast implementations of this.


---

Comment by malb created at 2009-03-15 12:03:42

I think your timings are off since you time the `random_element()` call.

## BEFORE


```
sage: P.<x> = GF(2)[]
sage: f = P.random_element(1000)
sage: %timeit f.is_irreducible()
10 loops, best of 3: 948 ms per loop

sage: f = P.random_element(10000)
sage: %time f.is_irreducible()
# gave up because it took minutes!
```


## AFTER


```
sage: P.<x> = GF(2)[]

sage: f = P.random_element(1000)
sage: %timeit f.is_irreducible()
10000 loops, best of 3: 22.7 µs per loop

sage: f = P.random_element(10000)
sage: %timeit f.is_irreducible()
1000 loops, best of 3: 394 µs per loop

sage: f = P.random_element(100000)
sage: %timeit f.is_irreducible()
100 loops, best of 3: 10.4 ms per loop
```


So we have 948*ms* vs. 22.3*micros* => `948*1000/22.3 = 42511.2107623318`


---

Comment by zimmerma created at 2009-03-15 21:03:19

the GF2X library (http://wwwmaths.anu.edu.au/~brent/gf2x.html) contains a
fast test. We are currently using it for polynomials of degree 43112609.
I guess there was a ticket about including GF2X in Sage.

Paul


---

Comment by malb created at 2009-03-16 12:11:52

I'll give the patch a positive review if the `cpdef` is replaced by a normal `def`.

Paul, does GF2X also have a `is_primitive()` function of some sorts?


---

Comment by zimmerma created at 2009-03-16 12:34:27

> Paul, does GF2X also have a is_primitive() function of some sorts? 

not directly, but the factor.cpp program searches for the smaller factor (in terms of degree)
of x^r + x^s + 1, it can be used as a starting point for a general irreducibility test.

Paul


---

Comment by rhinton created at 2009-03-16 15:21:03

I'm working on pseudo-random number generators.  Supposedly, polynomials with few terms (e.g. trinomials) have relatively poor properties for PRNGs, so I think I'll stick with the NTL test for now.

malb: Why don't you like the cpdef?  That allows it to be called from Python (current usage) _and_ should make it faster if I call it from another Cython module (possible future usage), correct?  I'm new at this, so I'm happy to learn more of the "why"s of Sage coding.


---

Comment by malb created at 2009-03-16 15:42:37

Replying to [comment:7 rhinton]:
> malb: Why don't you like the cpdef?  That allows it to be called from Python (current usage) 
> _and_ should make it faster if I call it from another Cython module (possible future usage), 
> correct?  I'm new at this, so I'm happy to learn more of the "why"s of Sage coding.

Because it seems like premature optimisation. If now one wants to change stuff around one always has to touch the header now which I find annoying. Also, I see little benefit in making this optimisation. From Python the advantage is nil and from Cython it is trivial to call NTL's function directly which is *much* faster.

I agree that this is somewhat a question of taste but I'd rather avoid a false sense of optimisation.


---

Comment by zimmerma created at 2009-03-16 17:03:01

> Supposedly, polynomials with few terms (e.g. trinomials) have relatively poor properties for PRNGs...

do you have any argument supporting that claim?


---

Comment by rhinton created at 2009-03-16 20:18:14

Replying to [comment:8 malb]:
> Replying to [comment:7 rhinton]:
> > malb: Why don't you like the cpdef?  That allows it to be called from Python (current usage) 
> > _and_ should make it faster if I call it from another Cython module (possible future usage), 
> > correct?  I'm new at this, so I'm happy to learn more of the "why"s of Sage coding.
> 
> Because it seems like premature optimisation. If now one wants to change stuff around one always has to touch the header now which I find annoying. Also, I see little benefit in making this optimisation. From Python the advantage is nil and from Cython it is trivial to call NTL's function directly which is *much* faster.

You are absolutely right.  Apparently I've already blocked out calling the M4RI interface directly. :-)

> I agree that this is somewhat a question of taste but I'd rather avoid a false sense of optimisation.


---

Attachment


---

Comment by rhinton created at 2009-03-16 20:25:24

Instructions: apply only trac_5519_irred_faster.2.patch.  Sorry I clicked submit before the "overwrite" check box.

The new patch removes the cpdef.  I agree, it is much cleaner.


---

Comment by rhinton created at 2009-03-16 20:38:50

Replying to [comment:9 zimmerma]:
> > Supposedly, polynomials with few terms (e.g. trinomials) have relatively poor properties for PRNGs...
> 
> do you have any argument supporting that claim?

I'm just reciting what I've read.  I am enjoying [1] right now, available at

http://www.iro.umontreal.ca/~lecuyer/papers.html

as f2lin.pdf.  They make this claim on page 11 in the first full paragraph, and cite [2] and [3].  They malign trinomials and pentanomials in particular (no offense intended) for PRNGs.  Incidentally, I'm working on a tool to search for maximally-equidistributed WELL generators (explained in [1], defined in [4] -- also very readable).

[1] L'Ecuyer and F. Panneton, ``F_2-Linear Random Number Generators'', 2007, to appear with minor revisions in "Advancing the Frontiers of Simulation: A Festschrift in Honor of George S. Fishman." GERAD Report 2007-21. 

[2] A. Compagner. The hierarchy of correlations in random binary sequences. Journal of Statistical Physics, 63:883–896, 1991.

[3] D. Wang and A. Compagner. On the use of reducible polynomials as random number generators. Mathematics of Computation, 60:363–374, 1993.

[4] F. Panneton, P. L'Ecuyer, and M. Matsumoto, ``Improved Long-Period Generators Based on Linear Recurrences Modulo 2'', ACM Transactions on Mathematical Software, 32, 1 (2006), 1-16.

Note that [4] is also available with errata from L'Ecuyer's site along with C source code.  And I have a few additional errata not currently listed in case you want to implement one.


---

Comment by malb created at 2009-03-16 21:03:25

Patch looks good, doctests pass.


---

Comment by mvngu created at 2009-03-18 23:45:05

Replying to [comment:3 malb]:
> I think your timings are off since you time the `random_element()` call.
<SNIP>
> So we have 948*ms* vs. 22.3*micros* => `948*1000/22.3 = 42511.2107623318`
Hi Martin. Is it possible for you to provide some system info? It would be good to accompany your timing statistics with some system architecture info.


---

Comment by mvngu created at 2009-03-19 04:22:10

On Debian 5.0 Lenny with the following system info:

```
kernel: 2.6.24-1-686
CPU: Intel(R) Celeron(R) 2.00GHz 
RAM: 1.0GB
```

here are some timing statistics:

```
# BEFORE

sage: P.<x> = GF(2)[]
sage: f = P.random_element(1000)
sage: %timeit f.is_irreducible()
10 loops, best of 3: 1.14 s per loop
sage: 
sage: f = P.random_element(10000)
sage: %time f.is_irreducible()
CPU times: user 4972.13 s, sys: 2.83 s, total: 4974.95 s
Wall time: 5043.02 s
False


# AFTER

sage: P.<x> = GF(2)[]
sage: f = P.random_element(1000)
sage: %timeit f.is_irreducible()
10000 loops, best of 3: 40.7 µs per loop
sage: 
sage: f = P.random_element(10000)
sage: %timeit f.is_irreducible()
1000 loops, best of 3: 930 µs per loop
sage: 
sage: 
sage: f = P.random_element(100000)
sage: %timeit f.is_irreducible()
10 loops, best of 3: 27.6 ms per loop
```

That is, a "before" 1.14 seconds vs. an "after" 40.7 microseconds, resulting in a speedup of 28x:

```
sage: a = 1.14 * 1000  # convert to microseconds
sage: b = 40.7  # unit is microseconds
sage: (a - b) / a
0.964298245614035
sage: a / b
28.0098280098280
```



---

Comment by malb created at 2009-03-19 11:07:26

Hi Minh,

my system is a 2.33 Ghz Core2Duo running 64-bit Debian/squeeze.

Note that you mixed up the units in your calculation. `1.14` seconds are `1.14 * 10<sup>6</sup>` microseconds not `1.14 * 10<sup>3</sup>`, i.e. you're mixing it up with milliseconds.

 http://en.wikipedia.org/wiki/Orders_of_magnitude_(time)

So you need to add a factor of 1000.

For `d=10000` it seems even more:


```
  4974.95 * 10^6 / 930
```



---

Comment by mvngu created at 2009-03-20 01:10:45

Replying to [comment:16 malb]:
> my system is a 2.33 Ghz Core2Duo running 64-bit Debian/squeeze.
Thanks for this. I'll put it in the release tour.




> Note that you mixed up the units in your calculation. `1.14` seconds are `1.14 * 10<sup>6</sup>` microseconds not `1.14 * 10<sup>3</sup>`, i.e. you're mixing it up with milliseconds.
> 
>  http://en.wikipedia.org/wiki/Orders_of_magnitude_(time)
> 
> So you need to add a factor of 1000.
> 
> For `d=10000` it seems even more:
> 
> {{{
>   4974.95 * 10^6 / 930
> }}}
You're absolutely right. Thanks for catching that. I really need to learn some physics :-)


---

Comment by mabshoff created at 2009-03-23 20:17:40

Resolution: fixed


---

Comment by mabshoff created at 2009-03-23 20:17:40

Merged trac_5519_irred_faster.2.patch in Sage 3.4.1.alpha0.

Cheers,

Michael
