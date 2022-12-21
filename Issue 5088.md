# Issue 5088: [with patch, needs review] use Pohlig-Hellman for generic discrete logarithm

Issue created by migration from Trac.

Original creator: ylchapuy

Original creation time: 2009-01-24 15:16:29

Assignee: somebody

Algorithm summary:
http://en.wikipedia.org/wiki/Pohlig-Hellman_algorithm



---

Attachment


---

Comment by ylchapuy created at 2009-01-24 15:25:30

My patch include the Pohlig-Hellman algorithm, and also modified the arguments of discrete_log, the "ord" argument wasn't used as announced but as a bound.

I also wonder why we keep an old_discrete_log, but this another story...


---

Comment by was created at 2009-01-24 15:44:02

Can you post some timings comparing your new code to sage before your new code...?


---

Comment by ylchapuy created at 2009-01-24 16:25:57

With a smooth order:

```
sage: factor(5^15-1)
2^2 * 11 * 31 * 71 * 181 * 1741
```

BEFORE:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: F.<a>=GF(5^15)
sage: g=F.gen()
sage: u=g^123456789
sage: time log(u,g)
CPU times: user 271.39 s, sys: 4.72 s, total: 276.11 s
Wall time: 276.96 s
123456789
sage: get_memory_usage()
378.21875
```

AFTER:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
Loading Sage library. Current Mercurial branch is: yann
sage: F.<a>=GF(5^15)
sage: g=F.gen()
sage: u=g^123456789
sage: time log(u,g)
CPU times: user 0.14 s, sys: 0.00 s, total: 0.14 s
Wall time: 0.16 s
123456789
sage: get_memory_usage()
115.8984375
```



---

Comment by was created at 2009-01-24 16:38:17

NICE!


---

Comment by ylchapuy created at 2009-01-24 16:44:20

and a not so smooth example

```
sage:factor(3^13-1)
2 * 797161
```

BEFORE:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: F.<a>=GF(3**13)
sage: g=F.gen()
sage: u=g^1234567
sage: timeit('log(u,g)')
5 loops, best of 3: 1.54 s per loop
sage: get_memory_usage()
155.11328125
```

AFTER:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
Loading Sage library. Current Mercurial branch is: yann
sage: F.<a>=GF(3**13)
sage: g=F.gen()
sage: u=g^1234567
sage: timeit('log(u,g)')
5 loops, best of 3: 931 ms per loop
sage: get_memory_usage()
139.4296875
```



---

Comment by cremona created at 2009-01-24 17:36:53

I am very pleased that someone is as interested as I am in improving this!  The original discrete log was wriiten by Stin & Joiner i think;  I rewrote it to work more generaically using the generic bsgs code;  I left the old code in through squaemishness about deleting what other people have written, that's all.

Can I clarify what the changes you have made are doing?   You are still using BSGS to find dlogs in a cyclic group, but instead of doing one big computation in the whole group, you factor the order and do it in each p-primary subgroup separately.  If so, that sounds very sensible, but I think it would be a good idea to cache the group order's factorization so that the factorization is not repeated on subsequent calls.  The only way I can see of doing that is to have  the base element (which might be additive or multiplicative) cache both its own order and the factorization of that order.

The next improvement we need is to replace the BSGS by something which takes less memory, but that's not a reason for delaying this patch.

I have not reviewed this yet, only looked at the patch code, but will do.


---

Comment by mabshoff created at 2009-01-24 18:07:59

Resolution: fixed


---

Comment by mabshoff created at 2009-01-24 18:07:59

John: William already gave this a positive review.

Merged in Sage 3.3.alpha2

Cheers,

Michael


---

Comment by cremona created at 2009-01-24 18:15:44

Replying to [comment:7 mabshoff]:
> John: William already gave this a positive review.

OK, I saw that after saying I would do it.  I did have two doctest failures but they seem to be unrelated since they also fail in my unpatched main branch, and are probably due to the messed up upgrade.

> 
> Merged in Sage 3.3.alpha2
> 
> Cheers,
> 
> Michael


---

Comment by slelievre created at 2020-10-20 23:49:13

Changing keywords from "" to "discrete logarithm, speedup".


---

Comment by slelievre created at 2020-10-20 23:49:13

This ticket is mentioned in this video (from 00:17:00 to 00:22:27):

- https://www.microsoft.com/en-us/research/video/the-sage-mathematical-software-project
