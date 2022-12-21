# Issue 7931: Improved nth root for finite fields and integer_mods

Issue created by migration from Trac.

Original creator: roed

Original creation time: 2010-01-14 15:27:30

Assignee: AlexGhitza

CC:  robertwb

Keywords: finite fields, nth root

Implements an algorithm described in 
{{
Johnston, Anna M. A generalized qth root algorithm. 
Proceedings of the tenth annual ACM-SIAM symposium on Discrete algorithms. 
Baltimore, 1999: pp 929-930.
}}}

This means we can take nth roots with large n, since we no longer need to create the polynomial x^n-a.


---

Attachment


---

Comment by roed created at 2010-01-14 15:30:14

Changing status from new to needs_review.


---

Comment by rishi created at 2010-01-21 17:09:24

Is there something I am missing?

```
sage: K = GF(31)
sage: b=K(22)^200
sage: b.nth_root(200)
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)

/virtual/scratch/rishi/sage-4.3.1.alpha2-sage.math.washington.edu-x86_64-Linux/<ipython console> in <module>()

/virtual/scratch/rishi/sage-4.3.1.alpha2-sage.math.washington.edu-x86_64-Linux/local/lib/python2.6/site-packages/sage/rings/integer_mod.so in sage.rings.integer_mod.IntegerMod_abstract.nth_root (sage/rings/integer_mod.c:11446)()

ValueError: no nth root
sage:

```



---

Comment by cremona created at 2010-01-24 18:46:58

It looks to me as if the original code (now deleted) worked with finite field elements, while thie new code works with integer-mods.  That must surely mean that for non-prime finite fields there was something which worked, but now there isn't?  If I am right, it would be a good idea to allow the original code as a fall-back.


---

Comment by cremona created at 2010-01-24 18:54:53

Changing status from needs_review to needs_work.


---

Comment by cremona created at 2010-01-24 18:54:53

Patch applies fine to 4.3.1 and tests pass, but I reproduced the example from rishi, so -- "needs work".


---

Attachment

Should fix the problem observed earlier


---

Comment by roed created at 2010-02-23 15:30:38

Changing status from needs_work to needs_review.


---

Comment by zimmerma created at 2010-02-25 22:29:00

David, should the 2nd patch be applied after the 1st one or alone?


---

Comment by zimmerma created at 2010-02-25 22:29:00

Changing status from needs_review to needs_info.


---

Comment by roed created at 2010-02-25 23:46:33

Alone.  Sorry about that.


---

Comment by roed created at 2010-02-25 23:46:33

Changing status from needs_info to needs_review.


---

Comment by roed created at 2010-02-25 23:49:27

Changing assignee from AlexGhitza to roed.


---

Comment by roed created at 2010-02-25 23:49:27

Oops.  I made it depend on a bunch of other changes

```
8218 -> 8332 -> 7880 -> 7883 -> 8333 -> 8334 -> this patch
```


The actual change is fairly small; I'll try to extract it out and get something based only on 4.3.3, but I won't be able to do that tonight.


---

Comment by zimmerma created at 2010-02-26 08:21:12

> The actual change is fairly small; I'll try to extract it out and get something based only on 4.3.3, but I won't be able to do that tonight.

that would be nice. Otherwise we can wait for the other patches to be reviewed.
Paul


---

Comment by AlexGhitza created at 2010-06-05 00:19:44

Replying to [comment:8 roed]:
> Oops.  I made it depend on a bunch of other changes
> {{{
> 8218 -> 8332 -> 7880 -> 7883 -> 8333 -> 8334 -> this patch
> }}}
> 
> The actual change is fairly small; I'll try to extract it out and get something based only on 4.3.3, but I won't be able to do that tonight.

Just so we have trac's help to see which of the dependencies have already been merged: this depends on #8218, #8332, #7880, #7883, #8333, #8334.


---

Comment by davidloeffler created at 2010-09-27 10:13:59

Patch `7931_nth_root.patch` applies and builds fine and all doctests in `finite_rings` pass (with the dependencies installed); but I'm not terribly happy about the amount of code duplication that's going on -- the code added to `element_base` and `integer_mod` has about 30 lines that are virtually identical. Could it not be refactored to avoid this?


---

Comment by roed created at 2010-09-27 17:27:19

I completely agree.  In the long run I want to change `FiniteFieldElement` to `FiniteRingElement` and make `IntegerMod_abstract` inherit from that.  The `nth_root` function on `FiniteRingElement` can then be modified to handle both cases.  An additional benefit of having such a common parent is that the finite field elements can then no longer require `p` prime (or `modulus` irreducible for that matter), which will be useful for p-adic extensions.  In fact, I want to modify the finite field element classes to use templates (a la `sage.rings.polynomial.polynomial_template`): then we can share common code between polynomials, finite fields and rings, and p-adic extension fields.  Coercions between them will be much easier and faster and it will make implementing extensions of extensions easier (which are necessary for p-adic extensions that are neither unramified nor totally ramified).

The first step though, of making `IntegerMod_abstract` inherit from `FiniteRingElement` caused compile-time bugs that I couldn't figure out and I gave up for the moment.

So currently their closest common superclass is `CommutativeRingElement`.  It didn't seem like a good idea to put the common `nth_root` code there, and there wasn't another obvious way to do it.  Any suggestions?


---

Comment by roed created at 2010-09-27 17:33:23

Another problem with the current patch is that for large `n`, finding the factorization of the size of the unit group becomes a bottleneck.  There's a change in #8335 that  helps with this problem for finite fields of small characteristic by caching the factorization of p<sup>n</sup>-1 and using the Cunningham package at #7240 to speed up the computation in the first place.  Thematically it would make sense to backport it to this patch (which I've done already locally), but it makes this patch depend on #7240 (otherwise there are warnings printed when `_factor_cunningham` is used).  What do you think?


---

Comment by davidloeffler created at 2010-09-27 17:43:19

Could one perhaps have an auxilliary helper function (not a class method) that both of the nth root methods call? This is not terribly elegant, but it solves the duplication issue.

I'd argue for not making this patch depend on #7240, since that patch seems to be stalled at the moment.


---

Attachment

Apply just this patch


---

Comment by roed created at 2010-09-28 08:34:14

I factored out most of the common code, and backported a few changes from #8335.  It still doesn't depend on #7240.


---

Comment by roed created at 2010-09-29 01:53:24

Apply on top of 7931_nth_root.2.patch; moves _nth_root_common to FiniteRingElement, a new superclass of IntegerMod_abstract and the finite field elements


---

Comment by zimmerma created at 2010-09-29 08:57:33

Changing status from needs_review to needs_info.


---

Attachment

I tried applying both patches in sage-4.6.alpha1, but got a failure when running sage -br:

```
python `which cython` --embed-positions --directive cdivision=True -I/tmp/sage-4.6.alpha1/devel/sage-7931 -o sage/rings/finite_rings/element_ntl_gf2e.cpp sage/rings/finite_rings/element_ntl_gf2e.pyx

Error converting Pyrex file to C:
------------------------------------------------------------
...
        if PY_TYPE_CHECK(e, int) \
               or PY_TYPE_CHECK(e, long) or PY_TYPE_CHECK(e, Integer):
            GF2E_conv_long(res.x,int(e))
            return res

        if PY_TYPE_CHECK(e, FiniteFieldElement) or \
                                             ^
------------------------------------------------------------

/tmp/sage-4.6.alpha1/devel/sage-7931/sage/rings/finite_rings/element_ntl_gf2e.pyx:515:46: undeclared name not builtin: FiniteFieldElement
Error running command, failed with status 256.
sage: There was an error installing modified sage library code.
```

Which version was used to produce the patches?

Paul


---

Comment by zimmerma created at 2010-09-29 09:58:53

I realized that I should also apply the patches #7883 and #8334, which were included in
sage-4.6.alpha2, but were not yet in sage-4.6.alpha1. However after importing #7883
successfully in sage-4.6.alpha1, importing #8334 gives:

```
sage: hg_sage.import_patch("/tmp/8333_8334_ALL-better_commit_string.patch")
cd "/tmp/sage-4.6.alpha1/devel/sage" && hg status
cd "/tmp/sage-4.6.alpha1/devel/sage" && hg status
cd "/tmp/sage-4.6.alpha1/devel/sage" && hg import   "/tmp/8333_8334_ALL-better_commit_string.patch"
applying /tmp/8333_8334_ALL-better_commit_string.patch
patching file sage/rings/ideal_monoid.py
Hunk #1 succeeded at 90 with fuzz 2 (offset 0 lines).
patching file sage/rings/residue_field.pyx
Hunk #3 succeeded at 74 with fuzz 2 (offset 0 lines).
Hunk #15 FAILED at 624
1 out of 36 hunks FAILED -- saving rejects to file sage/rings/residue_field.pyx.rej
abort: patch failed to apply
```

and I'm stuck there. Maybe I should wait that sage-4.6.alpha2 is out.

Paul


---

Comment by davidloeffler created at 2010-09-29 10:10:19

Ticket #8334 has some other dependencies -- they are listed on that ticket (Jeroen's comment 24). With those installed the patch applies fine, and all doctests in sage/rings pass (I'm running a full ptestlong cycle now), so I'm putting this back to "needs_review".

By the way, Mitesh has a lovely script [merger-4.6.alpha2](http://sage.math.washington.edu/home/release/sage-4.6.alpha2/merger-4.6.alpha2), which you can run on a clean 4.6.alpha1 build and it will download and apply all of the patches and spkgs so far merged.


---

Comment by davidloeffler created at 2010-09-29 10:10:19

Changing status from needs_info to needs_review.


---

Comment by zimmerma created at 2010-09-29 11:14:54

I tried Mitesh's script on my sage-4.6.alpha1 build (after sage -b main), then I applied the two
patches from that ticket, but I still get the same error as in comment 16.

Paul


---

Comment by davidloeffler created at 2010-09-29 11:47:24

That's bizarre, because the patches apply and build fine for me.


---

Comment by davidloeffler created at 2010-09-29 12:48:10

Actually I hadn't myself tried Mitesh's script when I posted above; I just did, and I couldn't get it to work either. But it should work if you install:

```
9898_pari_decl.patch
9753.patch
9764_ideal_repr_new.patch
trac_7883-ideals-folded.patch
8333_8334_ALL-rebased_for_9764.patch
7931_nth_root.2.patch
7931_common_superclass.patch
```



---

Comment by zimmerma created at 2010-09-29 14:06:19

Changing status from needs_review to needs_work.


---

Comment by zimmerma created at 2010-09-29 14:06:19

I managed to apply the patches following comment 21, however the following seems incorrect to me:

```
sage: b=Integers(3)(2)
sage: b.nth_root(2)
1
```

whereas in say Sage 4.4.4 we got `ValueError: no nth root`.

PS: I used the following reviewer program. Feel free to add it to the doctests.

```
for n in range(2,100):
   K=Integers(n)
   for e in range(1,100):
      for a in range(1,n):
         b = K(a)
         r = b.nth_root(e)
         if r^e <> b:
            print n, e, a
            raise ValueError
```



---

Comment by roed created at 2010-09-30 00:57:13

Changing status from needs_work to needs_review.


---

Comment by roed created at 2010-09-30 00:57:13

Thanks for catching that.  I've fixed the problem and added a `_nth_root_naive` and check that the output of `b.nth_root(e, all=True)` matches `b._nth_root_naive(e)` for all `b` in `Zmod(n)` for `2 <= n < 100` and `1 <= e < 100`.  A shortened version of this test is left in as a doctest for `_nth_root_naive`.


---

Comment by roed created at 2010-09-30 03:10:46

Apply on top of 7931_nth_root.2.patch and 7931_common_superclass.patch


---

Comment by zimmerma created at 2010-09-30 08:19:44

Changing status from needs_review to needs_work.


---

Attachment

with the new patch, I still get unexpected results:

```
sage: K=Integers(6)
sage: b=K(3)
sage: b.nth_root(0,all=True)
[3]
```

Paul


---

Attachment

Apply on top of previous patches


---

Comment by roed created at 2010-09-30 09:22:47

Unexpected indeed.  Thanks for checking all these corner cases that I neglected (though some of the earlier ones were bugs I should have found if I'd tested sufficiently).

In this case I'm not quite sure what the right output is: an empty list or a ZeroDivisionError?  I've gone for the empty list, on the theory that `b.nth_root(e)` should return a list of all elements `a` with a<sup>e</sup>=b, and this makes sense even if `e=0`.


---

Comment by roed created at 2010-09-30 09:22:47

Changing status from needs_work to needs_review.


---

Comment by cremona created at 2010-09-30 10:37:54

e=0 is a hard case since there are too many solutions -- do we want to return all a in the ring? or all invertible a?

Similarly, do we allow negative e, where b must be invertible and b.nth_root(e) == (1/b).nth_root(-e), with an error if b is not invertible?

Or do we want to specify in the documentation that e must be positive, and raise an error if not?


---

Comment by zimmerma created at 2010-09-30 11:45:50

My 2 cents:

* for e=0 and b<>1, b.nth_root(e) should return the empty list

* for e=0 and b=1, b.nth_root(e) should return only one solution, for example 1
  (with all=True, return all a in the ring)

Paul


---

Comment by zimmerma created at 2010-09-30 12:11:12

Changing status from needs_review to needs_work.


---

Comment by zimmerma created at 2010-09-30 12:11:12

sorry, another problem:

```
sage: n=13777831336991389951
sage: b=3798677550250515336
sage: e=10608321776141318019
sage: K = Integers(n)
sage: b=K(b)
sage: b.nth_root(e)
---------------------------------------------------------------------------
ZeroDivisionError                         Traceback (most recent call last)
```

The documentation does not say when `ZeroDivisionError` can be obtained.
This was found with the following program:

```
while True:
   n = randint(0,2^64)
   K = Integers(n)
   b = K.random_element()
   e = randint(0,2^64)
   print n, b, e, a
   sys.stdout.flush()
   try:
      a = b.nth_root(e)
      if a^e <> b:
         print n, b, e, a
         raise NotImplementedError
   except ValueError:
      n = 0
```



---

Comment by roed created at 2010-10-01 06:14:33

You've found a bug in crt: it claims to work as long as the moduli are relatively prime, but in fact would often fail if one of them was 1.  I fixed that and clarified the behavior of `nth_root` when `n<=0` (it either returns the empty list or raises a `ValueError`, depending on the value of `all`; `mod(1,n).nth_root(0)` returns the list of all nonzero elements modulo n).


---

Comment by roed created at 2010-10-01 06:14:33

Changing status from needs_work to needs_review.


---

Comment by zimmerma created at 2010-10-01 12:05:04

Changing status from needs_review to needs_work.


---

Comment by zimmerma created at 2010-10-01 12:05:04

Replying to [comment:29 roed]:
> You've found a bug in crt: it claims to work as long as the moduli are relatively prime, but in fact would often fail if one of them was 1.  I fixed that and clarified the behavior of `nth_root` when `n<=0` (it either returns the empty list or raises a `ValueError`, depending on the value of `all`; `mod(1,n).nth_root(0)` returns the list of all nonzero elements modulo n).

Hi David,

I'm not very happy with that answer. If a bug in crt was found, I would expect you to show a
concrete example, to report it as a new ticket, and to mention in your 3rd patch that it depends
on the new ticket, and can be removed once the new ticket is fixed.

Paul


---

Attachment

Apply on top of previous patches


---

Comment by roed created at 2010-10-01 14:33:56

Changing status from needs_work to needs_review.


---

Comment by roed created at 2010-10-01 14:33:56

You're right that it needs doctests; I've added some.  I also changed `7931_fix3.patch` by updating the `nth_root` function in `element_base` to match the behavior of the one in `integer_mod` for non-positive inputs.

Personally, I don't think that the crt bug is a major enough problem to need it's own ticket.  It only applies if one of the arguments is mod(0,1).  But I've separated the fix into its own patch; if you think it needs it's own ticket would you be willing to make the ticket and move the patch over there?


---

Comment by zimmerma created at 2010-10-01 15:18:54

I don't understand the crt patch: the examples given already worked in 4.6.alpha1 (and
similarly in 4.4.4):

```
----------------------------------------------------------------------
----------------------------------------------------------------------
**********************************************************************
*                                                                    *
* Warning: this is a prerelease version, and it may be unstable.     *
*                                                                    *
**********************************************************************
sage: mod(0,1).crt(mod(4,17)) 
4
sage: mod(0,1).crt(mod(0,1)) 
0
sage: mod(21,22).crt(mod(0,1))
21
```

What is exactly the crt bug (if any)?
| Sage Version 4.6.alpha1, Release Date: 2010-09-18                  |
| Type notebook() for the GUI, and license() for information.        |
Paul


---

Comment by zimmerma created at 2010-10-01 15:18:54

Changing status from needs_review to needs_info.


---

Comment by roed created at 2010-10-01 15:49:06

Changing status from needs_info to needs_review.


---

Comment by roed created at 2010-10-01 15:49:06

Ah.  Now I understand why this problem only appeared with your latest test program that used large moduli.  The issue only occurs for `mod(0,1).crt(a)` when `a` has type `IntegerMod_gmp`.  So we didn't see it for smaller moduli.

I've updated `7931_crt.patch`, and the doctest there does fail on my unpatched `4.6.alpha1`.


---

Comment by zimmerma created at 2010-10-01 15:56:28

I understand now, this is really a bug, and I think it should be considered in a separate ticket:

```
sage: mod(0,1).crt(mod(4,2^31-2)) 
4
sage: mod(0,1).crt(mod(4,2^31-1)) 
---------------------------------------------------------------------------
ZeroDivisionError                         Traceback (most recent call last)
```



---

Comment by roed created at 2010-10-01 16:05:30

This is now #10047.


---

Attachment

This is now #10047.


---

Attachment

Qfolded patch. Apply only this patch.


---

Comment by davidloeffler created at 2011-01-19 16:33:25

It took me some while to understand what patches to apply in what order, so having done so I thought it might be helpful to qfold everything into one patch. (I'm pleasantly surprised that patchbot understood immediately.)

Now I'll have a look at the code.


---

Comment by davidloeffler created at 2011-01-19 17:22:34

The code looks plausible, and I'm pleased to report that we aren't going to have the same problem as #9304 -- old pickled objects seem to unpickle just fine. I'm not qualified to comment on the details of the algorithm though. Paul?


---

Comment by zimmerma created at 2011-01-20 07:08:56

Replying to [comment:37 davidloeffler]:
> The code looks plausible, and I'm pleased to report that we aren't going to have the same problem as #9304 -- old pickled objects seem to unpickle just fine. I'm not qualified to comment on the details of the algorithm though. Paul?

I won't have much time in the near future to look closely at the algorithm. Unless someone else
has time before me (John?) I'll look at this later. Don't hesitate to ping me.

Paul


---

Comment by davidloeffler created at 2011-01-25 13:56:57

Fixed ReST formatting


---

Comment by davidloeffler created at 2011-01-25 14:04:36

Changing status from needs_review to positive_review.


---

Attachment

I checked this one with Bill Hart, who knows much more about these things than I, and he reckons that the implementation looks correct; I've run the tests and it seems to be fine. My only contribution has been to qfold everything and adjust some of the reference manual formatting, so I guess that doesn't need a separate review. 

Apply only the last patch.


---

Comment by roed created at 2011-01-25 17:05:19

Great!  Thanks to all of the reviewers for looking at this.


---

Comment by jdemeyer created at 2011-02-07 08:14:22

Resolution: fixed
