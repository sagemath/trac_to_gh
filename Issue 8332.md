# Issue 8332: Changes FiniteField_givaro to Python

Issue created by migration from https://trac.sagemath.org/ticket/8332

Original creator: roed

Original creation time: 2010-02-23 14:48:18

Assignee: AlexGhitza

Residue fields and others would like to be able to multiply inherit from finite field parents.  This is the first of the two switches needed to enable that (the other being sage.rings.finite_rings.element_ntl_gf2e.FiniteField_ntl_gf2e).

This depends on 8218.


---

Attachment


---

Comment by roed created at 2010-02-23 14:52:00

Changing status from new to needs_review.


---

Comment by roed created at 2010-02-23 17:38:06

Part of a series:

```
8218 -> 8332 -> 7880 -> 7883 -> 8333 -> 8334 -> 8335
```

I tried to make each of these mostly self contained, with doctests passing after every ticket, but I didn't entirely succeed.  If you're reviewing one of these tickets, applying later tickets will hopefully fix doctest failures that you're seeing.


---

Comment by davidloeffler created at 2010-03-17 20:03:53

This applies fine to 4.3.4.rc0 (on top of 8218), and all doctests pass on 64-bit Linux except for a tiny failure in sage/structure/parent.pyx. This is just because some random code has used `GF(9,'a')` as an example of a Cython object, so it's trivial to fix. I am still waiting for Sage to build on T2, and once that happens I will test this there as well, but if that passes I think this is fine to go in.


---

Comment by davidloeffler created at 2010-03-17 20:04:48

(BTW, the aforementioned failure doesn't seem to be dealt with by any of the other tickets in the series -- none of them change that line of code.)


---

Comment by davidloeffler created at 2010-04-04 14:27:06

apply over previous patch


---

Attachment

Here is a tiny patch to fix that failure. With this patch installed, all tests (including long) pass on selmer.warwick.ac.uk (Ubuntu x86_64), except an unrelated existing problem in sage/schemes/elliptic_curves/heegner.py; and a selection of tests in sage/rings/finite_rings pass on t2.math.washington.edu (Solaris) as well.


---

Comment by davidloeffler created at 2010-04-04 14:33:38

Changing assignee from AlexGhitza to davidloeffler.


---

Comment by cremona created at 2010-04-05 13:52:17

I applied both patches on top of a 4.3.5 build on 32-bit ubuntu, after previously applying the relevant bundle & patches from #8128.

With the first patch I tested all and found only the one failure mentioned aboue in sage/structures/parent.pyx.  With the second patch this now passes.

Positive review!  Now on to #7880...


---

Comment by cremona created at 2010-04-05 13:52:17

Changing status from needs_review to positive_review.


---

Comment by cremona created at 2010-04-05 13:52:56

Replying to [comment:6 cremona]:
> I applied both patches on top of a 4.3.5 build on 32-bit ubuntu, after previously applying the relevant bundle & patches from #8128.
> 
> With the first patch I tested all and found only the one failure mentioned aboue in sage/structures/parent.pyx.  With the second patch this now passes.
> 
> Positive review!  Now on to #7880...

Sorry that should read #8218.


---

Comment by jhpalmieri created at 2010-04-15 23:40:56

Merged into 4.4.alpha0:
 - trac_8332_givaro_python.patch
 - trac_8332_fix.patch


---

Comment by jhpalmieri created at 2010-04-15 23:40:56

Resolution: fixed
