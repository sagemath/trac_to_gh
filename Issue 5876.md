# Issue 5876: [with patch, needs review] Vast speedup in P1List construction

Issue created by migration from https://trac.sagemath.org/ticket/5876

Original creator: cremona

Original creation time: 2009-04-23 16:23:46

Assignee: craigcitro

CC:  georgsweber mtaranes was

Keywords: modular manin symbols

The P1List() constructor for Manin symbols (elements of `P^1(ZZ/NZZ)` was rather inefficient.  It constructed vastly too many symbols, normalised them all and then deleted duplicates.

This is quite unnecessary since it is easy to generate the list with no duplicates (and with simpler code).

As reported on sage-nt:

Before (3.4.1):


```
sage: time P1List(100000)
CPU times: user 3.52 s, sys: 0.03 s, total: 3.55 s
Wall time: 3.55 s
The projective line over the integers modulo 100000
sage: time P1List(1000000)
CPU times: user 129.11 s, sys: 0.64 s, total: 129.75 s
Wall time: 131.96 s
The projective line over the integers modulo 1000000
```


After:


```
sage: time P1List(100000)
CPU times: user 0.41 s, sys: 0.01 s, total: 0.42 s
Wall time: 0.42 s
The projective line over the integers modulo 100000
sage: time P1List(1000000)
CPU times: user 8.33 s, sys: 0.12 s, total: 8.45 s
Wall time: 8.80 s
The projective line over the integers modulo 1000000
```


The patch does this for both versions `p1list_int()` and `p1list_llong()`.

I think similar speedups are possible in the p1_normalise functions which would be significant in practice, and will try to get to that tomorrow.


---

Attachment

Based on 3.4.1


---

Comment by robertwb created at 2009-04-23 18:57:36

Cool. One question, why are you doing


```
g = arith_int.c_gcd_int(c,N)
if g==c:  # is a divisor
```


instead of simply


```
if N % c == 0:
```


Also, would it be faster to initialize the list with (1, t) for 0 <= t < N (as this is often the bulk of P<sup>1</sup>(Z/nZ)) and then ignore/not compute these ones later?


---

Comment by was created at 2009-04-23 19:15:52

Enthusiastic positive review!

> Why are you doing...

No good reason.  I just never got around to optimizing the code.

> Also, would it be faster to initialize the list with (1, t) for 
> 0 <= t < N (as this is often the bulk of P1(Z/nZ)) and then ignore/not 
> compute these ones later? 

Yes, that would be better.  That's what your g0n library does.  I always wanted that optimization to get implemented.


---

Comment by cremona created at 2009-04-23 19:39:39

Wow, I put up that patch before cycling home, spent the journey thinking of all the extra speedups which are possible (including stopping the c loop at N/2 or even N/3 when N is odd), and now I find that you are ahead of me.

I will try to improve it myself tonight (it's 8.40pm here) and post a new patch.


---

Comment by cremona created at 2009-04-23 20:02:07

replaces previous


---

Attachment

New patch replaces previous and implements suggestions.  Hard to compare times as I'm on a different machine.


---

Comment by cremona created at 2009-04-23 21:26:17

For the record, on the same machines the previous timings I now get

```
sage: time P1List(10^5)
CPU times: user 0.35 s, sys: 0.01 s, total: 0.36 s
Wall time: 0.35 s
The projective line over the integers modulo 100000
sage: time P1List(10^6)
CPU times: user 7.22 s, sys: 0.13 s, total: 7.35 s
Wall time: 7.35 s
The projective line over the integers modulo 1000000
```


Also

```
sage: time P1List(1009*1013)
CPU times: user 7.33 s, sys: 0.02 s, total: 7.35 s
Wall time: 7.36 s
The projective line over the integers modulo 1022117
sage: time P1List(1000003)
CPU times: user 8.25 s, sys: 0.03 s, total: 8.28 s
Wall time: 8.28 s
The projective line over the integers modulo 1000003
```

We could do a lot better if were allowed to factor N: i nthe last example (prime just over `10^6`) there is really nothing to do but it effectively does trial division up to N/5 !

It might be worth having a version which takes as in put as well as N a factorization (as a list of (p,e) pairs.  Or just a list of divisors of N.
which is a worthwhile extra saving.


---

Comment by cremona created at 2009-04-23 21:38:44

Last comment:  the code runs slower on a 64-bit machine (Bill Hart's, which I would have expected to be at least as fast as the standard-issue U of Warwick 32-bit desktop).  The `10^6` example takes 12.59s on Bill's machine compared with only 7.22s.

I wonder why?


---

Comment by mabshoff created at 2009-04-24 02:24:54

John, 

do you an Maite shared credit for authorship here?

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-24 02:32:11

Resolution: fixed


---

Comment by mabshoff created at 2009-04-24 02:32:11

Merged trac_5876.patch in Sage 3.4.2.alpha0.

Cheers,

Michael


---

Comment by robertwb created at 2009-04-24 02:41:16

The positive review was for the old patch, but the new one deserves one as well. Factoring/enumerating divisors would probably make a lot of sense, especially once we have fast factoring of small numbers (there's a project on this in William Stein's class right now). Not sure it would be a huge gain, as we are enumerating O(N) things anyways. 

This should certainly go in. 

- Robert


---

Comment by mabshoff created at 2009-04-24 02:54:25

Robert,

thanks for following up, I did not notice that the review by William was for the first patch only. I did assign reviewer credit to William and you, so now I am waiting on John to tell us in the morning who gets credited for writing the patch (if there is anyone besides him).

Cheers,

Michael


---

Comment by cremona created at 2009-04-24 08:09:45

Replying to [comment:10 mabshoff]:
> Robert,
> 
> thanks for following up, I did not notice that the review by William was for the first patch only. I did assign reviewer credit to William and you, so now I am waiting on John to tell us in the morning who gets credited for writing the patch (if there is anyone besides him).
> 
> Cheers,
> 
> Michael

I think I'll take the credit.  Maite and I were looking at the code since we were working out how to do the same over number fields, and I had just written my contribution to sage-nt listing 4 possible methods there.  We noticed the inefficiency together, but I wrote the new code alone.  She can get credit for the number field version when it is ready!


---

Comment by mabshoff created at 2009-04-24 08:19:24

Replying to [comment:11 cremona]:


> I think I'll take the credit.  Maite and I were looking at the code since we were working out how to do the same over number fields, and I had just written my contribution to sage-nt listing 4 possible methods there.  We noticed the inefficiency together, but I wrote the new code alone.  She can get credit for the number field version when it is ready!

Thanks for clearing this up John.

Cheers,

Michael
