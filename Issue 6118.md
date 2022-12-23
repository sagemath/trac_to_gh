# Issue 6118: integer shifting slow

Issue created by migration from https://trac.sagemath.org/ticket/6118

Original creator: robertwb

Original creation time: 2009-05-22 00:38:29

Assignee: somebody




---

Attachment


---

Comment by robertwb created at 2009-05-22 00:43:36

Before


```
sage: a = 123; b = 11; timeit("a << b")
625 loops, best of 3: 3.61 µs per loop
sage: a = 123; b = int(11); timeit("a << b")
625 loops, best of 3: 3.99 µs per loop
```


After


```
sage: a = 123; b = 11; timeit("a << b")
625 loops, best of 3: 230 ns per loop
sage: a = 123; b = int(11); timeit("a << b")
625 loops, best of 3: 256 ns per loop
```



---

Comment by fredrik.johansson created at 2009-06-03 18:26:17

Thumbs up from me. The patch successfully applied to my 4.0 install and the tests in integer.pyx pass.

This patch is important for mpmath performance (#6196). Time for sage.libs.mpmath.all.runtests() without patch = 63.66 seconds, with patch = 51.88 seconds.


---

Comment by craigcitro created at 2009-06-04 09:56:22

I'm definitely happy with this patch. As Robert points out in the patch, there are a few inconsistencies in some of the `integer.pyx` code -- for instance, there are the incongruously named `_lshift` and `_rshift_`, which are basically the same and are barely used. I've removed them, cleaned up the bits of code that used them, and made one or two (morally) small changes to Robert's `_shift_helper` code, such as some comments and more error checking.

Interestingly, I'm having some funny results using `timeit` vs. `%timeit`, namely that `timeit` tends to be inconsistent on timings this tiny:

```
sage: a = 123 ; b = 11
sage: timeit("a << b")
625 loops, best of 3: 200 ns per loop
sage: timeit("a << b")
625 loops, best of 3: 323 ns per loop
sage: timeit("a << b")
625 loops, best of 3: 371 ns per loop
sage: timeit("a << b")
625 loops, best of 3: 360 ns per loop
sage: timeit("a << b")
625 loops, best of 3: 360 ns per loop
sage: timeit("a << b")
625 loops, best of 3: 370 ns per loop
sage: timeit("a << b")
625 loops, best of 3: 368 ns per loop
sage: timeit("a << b")
625 loops, best of 3: 418 ns per loop
```


As you can see, it's generally around `368 ns`, but the timings have several outliers. But IPython `%timeit` thinks the fast outlier is the *correct* value!


```
sage: %timeit a << b
10000000 loops, best of 3: 188 ns per loop
sage: %timeit a << b
10000000 loops, best of 3: 187 ns per loop
```


I tend to trust it, because it's running a ton of loops -- maybe the fact that my computer is doing several things at once is disturbing `timeit`?

Anyway, new patch attached. Robert, if you could look over the changes, I'd say this is a positive review. It seems to give me a nominally faster (around `5%`) timing than the previous version, but that's probably just my computer being weird.


---

Comment by robertwb created at 2009-06-05 11:25:54

I just realized this touched integer.pxd, so some comments first. We care about shifting by ints a lot because library code (especially mpmath) does a lot of stuff like "x << 1". I think the patch may make that path slower. Also, the error checking and cpdefing may make it slower too (I'll test, might be negligible). 

Also, why do 


```
if n < 0: 
    n *= -1 
    sign *= -1 
```


rather than 


```
n *= sign
```



---

Comment by robertwb created at 2009-06-06 03:32:13

Here's after just the first patch: 


```
sage: a = 5; b = 6; c = 6r
sage: %timeit a << b
10000000 loops, best of 3: 195 ns per loop
sage: %timeit a >> b
1000000 loops, best of 3: 218 ns per loop
sage: %timeit a << c
10000000 loops, best of 3: 188 ns per loop
sage: %timeit a >> c
1000000 loops, best of 3: 217 ns per loop

sage: b = -6; c = -6r
sage: %timeit a << b
1000000 loops, best of 3: 204 ns per loop
sage: %timeit a >> b
10000000 loops, best of 3: 196 ns per loop
sage: %timeit a >> c
10000000 loops, best of 3: 190 ns per loop
sage: %timeit a << c
1000000 loops, best of 3: 222 ns per loop
```


and after the second patch 


```
sage: sage: a = 5; b = 6; c = 6r
sage: sage: %timeit a << b
1000000 loops, best of 3: 192 ns per loop
sage: sage: %timeit a >> b
1000000 loops, best of 3: 204 ns per loop
sage: sage: %timeit a << c
1000000 loops, best of 3: 203 ns per loop
sage: sage: %timeit a >> c
1000000 loops, best of 3: 217 ns per loop
sage: 
sage: sage: b = -6; c = -6r
sage: sage: %timeit a << b
1000000 loops, best of 3: 206 ns per loop
sage: sage: %timeit a >> b
1000000 loops, best of 3: 197 ns per loop
sage: sage: %timeit a >> c
1000000 loops, best of 3: 203 ns per loop
sage: sage: %timeit a << c
1000000 loops, best of 3: 222 ns per loop
```


With repeated timings, the variance seems to be about 5 or so ns. The only significant differences are that Integer >> Integer is a bit faster with the second patch, and Integer << int and Integer >> int are faster with the first. 

I'm (pleasantly) surprised making it a cpdef function didn't slow it down. I don't think `shift_helper` needs to do error checking, and it seems odd to introduce a new auxiliary variable `normalize_Integer`.


---

Attachment

I've added a new version of the second patch, which mostly just adds comments and removes the inconsistencies with things like `_lshift` and `_rshift_`. 

In particular, I've come around to Robert's point that we want to speed up the `Integer << int` and `Integer >> int` cases the most -- I just did a `search_src('>>')`, and there seems to be a lot of code that shifts by literals (which will be Python `int`s). I also removed the one extra error check in `_shift_helper` and made a note about it. 

One last question, though -- do we really need the case where `y = ZZ(y)` raises a `ValueError`? Looking at the `Integer` constructor, this seems to only happen when we're given a string in a base larger than 36; in this case, the code in the `except` clause won't work, anyway. So are there other cases where this is used that I'm not thinking of? (It's obviously not too important, but I'm curious.)


---

Comment by mhansen created at 2009-09-08 06:14:26

I think that Craig's patch looks good, and his question shouldn't really hold this up.  I'll open a new ticket for that so that these can go in.


---

Comment by mvngu created at 2009-09-08 10:27:12

I got some hunk failures when applying `trac-6118-pt2.patch`:

```
[mvngu@sage sage-main]$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/6118/trac-6118-pt2.patch && hg qpush
adding trac-6118-pt2.patch to series file
applying trac-6118-pt2.patch
patching file sage/rings/integer.pxd
Hunk #1 FAILED at 15
1 out of 1 hunks FAILED -- saving rejects to file sage/rings/integer.pxd.rej
patching file sage/rings/integer.pyx
Hunk #1 FAILED at 4363
Hunk #2 FAILED at 4405
Hunk #3 FAILED at 4417
Hunk #4 FAILED at 4434
Hunk #5 FAILED at 4443
5 out of 5 hunks FAILED -- saving rejects to file sage/rings/integer.pyx.rej
patch failed, unable to continue (try -v)
patch failed, rejects left in working dir
Errors during apply, please fix and refresh trac-6118-pt2.patch
```

This needs a rebase against Sage 4.1.2.alpha1 or a later version.


---

Comment by mhansen created at 2009-09-08 20:14:06

Minh, were you applying both patches?  The second applies on top of the first.


---

Comment by was created at 2009-09-08 20:19:39

mhansen -- what's up?  a bunch of us are at the HUB working on Sage...


---

Comment by mhansen created at 2009-09-30 07:22:37

Both patches should be applied -- not just the last one.


---

Comment by mhansen created at 2009-10-15 08:48:57

Resolution: fixed
