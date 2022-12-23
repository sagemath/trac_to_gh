# Issue 9886: slow coercion from integer ring to integer mod ring

Issue created by migration from https://trac.sagemath.org/ticket/9887

Original creator: dmharvey

Original creation time: 2010-09-09 16:09:17

Assignee: tbd

Sage 4.5.3, 2.6GHz Opteron, Linux


```
sage: R = Integers(3^20)
sage: u = Integer(2)
sage: timeit("z = R(u)")
625 loops, best of 3: 6.84 µs per loop
```


Why does it take 18000 cycles to convert a tiny integer to an element of R?



---

Comment by roed created at 2010-09-23 11:22:38

This depends on #7883, #8333, #8334 and #9814.  In particular, you first need to apply

```
333_finite_fields_to_new_coercion.patch
7883_ideals.patch
7883_fixes.patch
7585_9_1_frac_and_coerce_updates.patch
8334_residue_fields-rebased_for_8446.patch
7585_12_1_fixes.patch
9814-2.patch
```

from those tickets.

On the other hand, it also addresses the speed issues in #9885, #9884, #9883 and #9882.  It should also fix #9886: the timings indicate that `ZZ.convert_map_from(R)` is getting called each time, rather than the morphism being found in the `convert_from_hash,` and I don't know why this would be the case.


---

Comment by roed created at 2010-09-23 11:22:38

Changing status from new to needs_review.


---

Comment by roed created at 2010-09-23 11:27:15

Oops, the top of the dependencies got cut off, and there are newer versions of some of these patches.  It should read:

```
8333_parent_init.patch
8333_finite_fields_to_new_coercion.2.patch
7883_ideals.patch
7883_fixes.patch
7585_9_1_frac_and_coerce_updates.patch
8334_residue_fields-rebased_for_8446.patch
7585_12_1_fixes.patch.2
9814-2.patch
```

Note that you can find `7585_12_1_fixes.patch` and `7585_9_1_frac_and_coerce_updates.patch` at #8334.


---

Comment by davidloeffler created at 2010-10-03 16:22:41

I tried the test cases from tickets #9882-#9887 under 4.5.3, under 4.6.alpha2 without this patch, and with this patch. Apologies for the crappy ASCII-art table.


```
      -------------------------------
      |   4.5.3 |  4.6.a2 | + patch |
-------------------------------------
#9882 | 19.8 µs | 15.9 µs | 3.87 µs |
#9883 | 4.25 ms |  133 µs | 21.5 µs |
#9884 | 1.04 ms |  385 µs |   18 µs |
#9885 | 1.23 µs | 1.24 µs | 1.34 µs |
#9886 | 33.7 µs | 32.5 µs | 32.9 µs |
#9887 | 6.54 µs |  966 ns |  992 ns |
-------------------------------------
```


So it looks like David's other finite rings patches have already made a dramatic speed improvement to several of these, and the patch on this ticket further improves some of them. The fact that #9885 actually slowed down marginally as a result of the patch is slightly worrying; it might just be random noise, but I did several more runs and the slight slowdowns in #9885 and (to a lesser extent) #9887 seemed quite consistent. It might be a price worth paying for the dramatic speedups elsewhere, but it would be nice if we could avoid it.

I'd be interested to see corresponding timings on other systems.


---

Comment by roed created at 2010-10-15 08:44:14

I'm not sure why there are slight slowdowns for #9885 and #9887.  But I did figure out why #9886 was unexpectedly slow: see #10130.

Here are timings on my Macbook Pro (+ patch includes the patch at #10130):

```
      -------------------------------
      | 4.3.rc0 |  4.6.a2 | + patch |
-------------------------------------
#9882 | 19.9 µs |   15 µs | 3.71 µs |
#9883 | 4.34 ms |  117 µs | 20.2 µs |
#9884 | 3.79 ms |  314 µs | 30.7 µs |
#9885 | 1.22 µs |  850 ns |  938 ns |
#9886 | 9.99 µs | 33.4 µs |  264 ns |
#9887 |    ? µs |  787 ns |  814 ns |
-------------------------------------
```

I got a range of values for #9885 in the middle column, from 835ns to 1.07µs.

I wanted to check 9.99µs in the first column in a different branch, so rebuilt only to discover that that copy of sage was built when I had an earlier version of OS X and was thus running 32 bit...


---

Comment by kedlaya created at 2011-06-17 16:07:22

Changing status from needs_review to needs_work.


---

Comment by kedlaya created at 2011-06-17 16:07:22

This patch fails to apply against 4.7:

```
cd "/home/kedlaya/Downloads/sage-4.7/devel/sage" && hg import   "/home/kedlaya/Downloads/9887.patch"
applying /home/kedlaya/Downloads/9887.patch
patching file sage/rings/finite_rings/integer_mod.pxd
Hunk #1 succeeded at 12 with fuzz 1 (offset 0 lines).
patching file sage/rings/polynomial/polynomial_ring.py
Hunk #7 FAILED at 1246
1 out of 13 hunks FAILED -- saving rejects to file sage/rings/polynomial/polynomial_ring.py.rej
abort: patch failed to apply
```



---

Attachment


---

Comment by roed created at 2011-06-21 19:53:40

It should apply against 4.7.1.alpha4.


---

Comment by roed created at 2011-06-21 19:53:40

Changing status from needs_work to needs_review.


---

Comment by roed created at 2011-06-22 08:14:03

For patchbot (and others working against 4.7), apply 9887_vs_47.patch only.


---

Comment by roed created at 2011-06-22 09:24:42

Apply against 4.7


---

Attachment

What is the status of this patch now?  It looks like it could easily bit-rot (if it hasn't already).


---

Attachment

Apply against 4.8.alpha2


---

Comment by roed created at 2011-12-15 05:24:56

Apply only 9887_vs_48a2.patch


---

Comment by davidloeffler created at 2012-03-11 16:13:08

Changing status from needs_review to needs_work.


---

Comment by davidloeffler created at 2012-03-11 16:13:08

This does not apply to the current beta, as it conflicts with #9138 and #11900, so I'm afraid it will need yet another rebase.


---

Comment by tscrim created at 2013-02-25 04:38:03

There is at least some partial work on this done in `5.7.beta3`:

```
sage: R = Integers(3^20)
sage: u = Integer(2)
sage: %timeit z = R(u)
100000 loops, best of 3: 1.48 us per loop
sage: %timeit z = R(u)
1000000 loops, best of 3: 1.74 us per loop
```


So should we close this ticket?

Edit - I'm running this test on my Ubuntu VM while video chatting on Skype in my Host OS.


---

Comment by tscrim created at 2013-02-25 04:38:03

Changing status from needs_work to needs_info.


---

Comment by AlexGhitza created at 2013-07-23 22:24:18

Changing keywords from "" to "sd51".


---

Comment by AlexGhitza created at 2013-07-23 22:24:18

Changing status from needs_info to positive_review.


---

Comment by AlexGhitza created at 2013-07-23 22:24:18

I second the request to close the ticket.  On sage-5.10:


```
sage: R = Integers(3^20)
sage: u = Integer(2)
sage: %timeit("z = R(u)")
10000000 loops, best of 3: 24.6 ns per loop
sage: %timeit("z = ZZ(u)")
10000000 loops, best of 3: 24.5 ns per loop
```


In other words, putting u into R takes the same time as putting u into ZZ (where it is already).  It shouldn't be possible to do any better.

I'll tag this as "positive review" to bring it to the release manager's attention.


---

Comment by jdemeyer created at 2013-08-13 08:43:03

Resolution: worksforme
