# Issue 5250: But in multiplicative_generator function for Z/NZ

Issue created by migration from https://trac.sagemath.org/ticket/5250

Original creator: was

Original creation time: 2009-02-12 23:41:54

Assignee: was

Notice that (ZZ/162ZZ)^* *is* cyclic:

```
sage: R = Integers(162)
sage: R(5).multiplicative_order()
54
sage: euler_phi(162)
54
```


However, Sage gets this totally wrong:

```
sage: R.multiplicative_generator()
Traceback (most recent call last):
...
ValueError: multiplicative group of this ring is not cyclic
```


This bug came up for me today while doing some research.  I'm glad I didn't believe Sage :-). 


---

Comment by davidloeffler created at 2009-05-06 14:34:46

Changing status from new to assigned.


---

Comment by davidloeffler created at 2009-05-06 14:34:46

Changing assignee from was to davidloeffler.


---

Comment by davidloeffler created at 2009-05-06 14:34:46

This comes up whenever n is twice a power of an odd prime. In these cases, `multiplicative_group_is_cyclic` would wrongly return False, `multiplicative_generator` would throw an error and `unit_gens` would return a list of length 2 one of whose elements is 1.

The attached patch fixes this. It also streamlines the code a bit by using the is_prime_power function; this is more readable, and in theory should be quicker than factorisation. At the moment it is actually a tiny fraction slower, but this is a consequence of an awkward workaround for a Pari bug (see #4777) and it will presumably be fixed in the future.


---

Comment by davidloeffler created at 2009-05-06 14:40:26

Oops, just realised that this breaks one or two doctests (because various functions expect the list of unit gens to contain 1's).


---

Attachment

patch against 3.4.2.final


---

Comment by davidloeffler created at 2009-05-07 15:50:49

Here's a patch that fixes the (relatively easy) bug in multiplicative_generator and the (much deeper) bug in multiplicative_subgroups. The latter is written in such a way that it should be very easy to transplant into was's new framework for Abelian groups based on 5882.


---

Comment by cremona created at 2009-05-08 19:57:45

A valiant job: if I come against something which depends on adding functionality to abelian groups I just give up, but you did it.  (In my ideal world every finite abelian group would internally be stored and work with elementary divisors, which would make the code simpler.  Never mind).

Expecting to review this over the weekend.


---

Comment by cremona created at 2009-05-09 17:20:19

Positive review.  The code looks ok to me, applies to 3.4.2 and tests pass (I tested abelian_groups and all modular).

No doubt the subgroups function in abelian groups will be superseded one day (after #5882) but that's no reason to stop this.  And both the original bugs are fixed.


---

Comment by davidloeffler created at 2009-05-10 20:46:17

Michael: don't merge this one quite yet -- it breaks one of the new doctests I added as part of #4357, so if you apply both patches you will get a doctest failure in sage/modular/modform/ambient_eps.py. I will do yet another patch to sort this out.


---

Attachment

fix doctest from #4357 which this breaks


---

Comment by davidloeffler created at 2009-05-10 21:41:39

Right, that should fix it. (I'm trying to ensure that the tickets of mine for which I have patches up right now apply without conflicts if they are all applied *in order of ticket number*.)


---

Comment by mabshoff created at 2009-05-11 09:18:03

I am observing one more doctest failure in ambient.py with -long:

```
sage -t -long "devel/sage/sage/modular/modsym/ambient.py"   
**********************************************************************
File "/scratch/mabshoff/sage-4.0.alpha0/devel/sage/sage/modular/modsym/ambient.py", line 1104:
    sage: M.factorization()                    # long time (about 8 seconds)
Expected:
    (Modular Symbols subspace of dimension 1 of Modular Symbols space of dimension 7 and level 38, weight 2, character [1, zeta3], sign 1, over Cyclotomic Field of order 3 and degree 2) *
    (Modular Symbols subspace of dimension 2 of Modular Symbols space of dimension 7 and level 38, weight 2, character [1, zeta3], sign 1, over Cyclotomic Field of order 3 and degree 2) *
    (Modular Symbols subspace of dimension 2 of Modular Symbols space of dimension 7 and level 38, weight 2, character [1, zeta3], sign 1, over Cyclotomic Field of order 3 and degree 2) *
    (Modular Symbols subspace of dimension 2 of Modular Symbols space of dimension 7 and level 38, weight 2, character [1, zeta3], sign 1, over Cyclotomic Field of order 3 and degree 2)
Got:
    (Modular Symbols subspace of dimension 1 of Modular Symbols space of dimension 7 and level 38, weight 2, character [zeta3], sign 1, over Cyclotomic Field of order 3 and degree 2) * 
    (Modular Symbols subspace of dimension 2 of Modular Symbols space of dimension 7 and level 38, weight 2, character [zeta3], sign 1, over Cyclotomic Field of order 3 and degree 2) * 
    (Modular Symbols subspace of dimension 2 of Modular Symbols space of dimension 7 and level 38, weight 2, character [zeta3], sign 1, over Cyclotomic Field of order 3 and degree 2) * 
    (Modular Symbols subspace of dimension 2 of Modular Symbols space of dimension 7 and level 38, weight 2, character [zeta3], sign 1, over Cyclotomic Field of order 3 and degree 2)
**********************************************************************
```


Cheers,

Michael


---

Comment by davidloeffler created at 2009-05-11 09:21:28

Ah, I didn't do the long doctests. It is harmless. Patch coming in a couple of seconds.


---

Attachment

fix borken -long doctest in modsym/ambient.py


---

Comment by davidloeffler created at 2009-05-11 09:25:06

Here it is.


---

Comment by craigcitro created at 2009-05-11 09:27:12

Just as a double-check, I'll be another voice to say the last two doctest patches look good. (The old code had 1 as one of the multiplicative generators of `Z/38` ... pretty funny.)


---

Comment by cremona created at 2009-05-11 09:29:31

Replying to [comment:11 craigcitro]:
> Just as a double-check, I'll be another voice to say the last two doctest patches look good. (The old code had 1 as one of the multiplicative generators of `Z/38` ... pretty funny.)

I agree that the new output looks good (and the old one very bad for the reasons stated).


---

Comment by mabshoff created at 2009-05-11 09:31:11

Resolution: fixed


---

Comment by mabshoff created at 2009-05-11 09:31:11

Merged all three patches in Sage 4.0.alpha0.

Cheers,

Michael
