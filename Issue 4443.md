# Issue 4443: [with patch, needs review] Massive prime_range speedup, arith* files cleanup

Issue created by migration from Trac.

Original creator: craigcitro

Original creation time: 2008-11-05 10:08:50

Assignee: craigcitro

CC:  cremona zimmerma

This bundle does several things:

 1. Massively speed up `prime_range`. Before:

    {{{
sage: time ls = prime_range(10^8)
CPU times: user 143.74 s, sys: 1.51 s, total: 145.26 s
Wall time: 145.93 s
    }}}

 After:
    
    {{{
sage: %time ls = prime_range(10^8)
CPU times: user 1.76 s, sys: 1.08 s, total: 2.84 s
Wall time: 2.87 s
    }}}

 This was first mentioned during the `3.1.3.alpha0` testing cycle. 

 2. Speed up `gcd` and `lcm`. These were rewritten to be much more robust as part of #3118. However, these were accidentally made much slower. This patch fixes that. 

 Before #3118:
    {{{
sage: n = 928374923
sage: m = 892734
sage: %timeit gcd(n,m)
100000 loops, best of 3: 6.13 Âµs per loop
    }}}
    
 After #3118:
    {{{
sage: n = 928374923
sage: m = 892734
sage: %timeit gcd(n,m)
10000 loops, best of 3: 25.7 Âµs per loop
    }}}   
   
 With this patch:
    {{{
sage: n = 928374923
sage: m = 892734
sage: %timeit gcd(n,m)
100000 loops, best of 3: 3.97 Âµs per loop
    }}}

 I also tested on lots of other kinds of input (lists of `Integer`s, list of `int`s, list of `long`s, etc), and the code *seems* to be always at least as fast as both before and after the patch at #3118. If there are cases I've missed, please let me know! 
   
 3. Tidy up `sage/rings/arith.py`. This was mostly small cosmetic changes; it would be a good project to go through this file, remove more cruft, and move some functions to Cython. If someone wants to make a ticket and assign it to me, I'll try to get to it at some point.

 4. Clean up and reorganize all of the files with `arith` in their name. In particular, I moved `sage/ext/arith.pyx` to `sage/rings/fast_arith.pyx`, and removed all of the legacy `arith_c`, `arith_gmp`, etc. Most of these were empty files that dated back to the days when Pyrex wouldn't let us keep `.pyx` files in multiple directories. There were also two files which seemed to be a Pyrex implementation of polynomials mod n, I believe by Didier Deshommes. These aren't used anywhere in Sage, and we have new code that does that (based on David Harvey's `znpoly`), so I've removed them.

I have tested all of `sage/rings/`, but one should really do a `sage -br` and a `sage -testall` before giving this bundle a positive review. I'll try to do this soon, but I wanted to get the patch posted while I was at it.

Since several files were added and removed from the mercurial archive, I'm attaching a bundle instead of a patch. I'm adding John Cremona and Paul Zimmerman to the `cc`, because they're most qualified to look at the changes I made after #3118 and see if I accidentally un-did any of their work on some corner cases.


---

Attachment


---

Comment by cremona created at 2008-11-05 11:13:29

I'm looking at it now, assuming that I can get those .hg files to apply.  john


---

Comment by cremona created at 2008-11-05 11:19:00

Replying to [comment:1 cremona]:
> I'm looking at it now, assuming that I can get those .hg files to apply.  john

What am I supposed to do with those .hg files?  For the first one I get an error message when I click on it; for the second it just displays a whole lot of changelogs.  Right-clicking and asking to save just ends up with some html in a file.  Perhaps the .patch patch file contains everything?

Awaiting instructions....


---

Comment by craigcitro created at 2008-11-05 16:35:29

Changing status from new to assigned.


---

Comment by craigcitro created at 2008-11-05 16:35:29

Well, even though it doesn't show the changesets when you click, here's what theoretically should happen:

 * click on `trac-4443.hg`
 * click on "Original Format" and save the file
 * in a new `3.2.alpha2` branch, type `hg unbundle trac-4443.hg`

You should then be good to go.


---

Comment by mabshoff created at 2008-11-05 16:42:23

There only seems to be one relevant changeset in there, i.e.

http://trac.sagemath.org/sage_trac/attachment/ticket/4443/trac-4443-huge.hg?changeset=10886

Then why not post a patch and then delete the other crap from the ticket? There is also trac-4443.patch which seems to be that one changeset?

Thoughts?

Cheers,

Michael


---

Comment by craigcitro created at 2008-11-05 16:51:03

Yes, there is only one changeset. However, I did a bunch of `hg add` and `hg remove` -- my understanding is that a patch doesn't keep track of that. Or am I just wrong? If so, feel free to delete the two bundles.


---

Comment by mabshoff created at 2008-11-05 17:17:36

Replying to [comment:5 craigcitro]:
> Yes, there is only one changeset. However, I did a bunch of `hg add` and `hg remove` -- my understanding is that a patch doesn't keep track of that. Or am I just wrong? If so, feel free to delete the two bundles.

All files removed or added to the repo before committing are in the diff - have a look yourself :). If you look at the bundle there is also only one commit, so where else should those changes be? :p

Cheers,

Michael


---

Comment by cremona created at 2008-11-05 17:26:41

If I understand correctly, this means that I can apply the *patch as normal and ignore the rest?  OK, it will be done....


---

Comment by cremona created at 2008-11-05 21:05:28

First things first:  patch applies cleanly to 3.2.alpha2, but -testall gives this:

```
The following tests failed:


	sage -t  devel/sage/sage/calculus/calculus.py
	sage -t  devel/sage/sage/tests/book_stein_modform.py
	sage -t  devel/sage/sage/tests/book_stein_ent.py
	sage -t  devel/sage/sage/schemes/elliptic_curves/sha_tate.py
	sage -t  devel/sage/sage/schemes/elliptic_curves/ell_tate_curve.py
	sage -t  devel/sage/sage/schemes/elliptic_curves/ell_rational_field.py
	sage -t  devel/sage/sage/modular/abvar/abvar.py
	sage -t  devel/sage/sage/modular/modform/eis_series.py
	sage -t  devel/sage/sage/modular/modform/ambient.py
	sage -t  devel/sage/sage/modular/modform/hecke_operator_on_qexp.py
	sage -t  devel/sage/sage/modular/modform/vm_basis.py
	sage -t  devel/sage/sage/modular/modform/j_invariant.py
	sage -t  devel/sage/sage/modular/modform/space.py
	sage -t  devel/sage/sage/modular/modform/cuspidal_submodule.py
	sage -t  devel/sage/sage/modular/modform/element.py
```

which are probably all trivial but need to be fixed.

I find a patch like this quite hard to review, since it combines a lot of moving of chunks of code around (certainly a good idea here) with all the trivial changes which that leads to;  and some real bug-fixes.  When scanning the patch one sees lots of large blue and red hunks (which may or may not hide significant code changes), and a lot of trivial changes, and buried in there is the "real meat".

One thing I could not work out easily was exactly how my earlier changes to lcm and gcd caused the slow-down!

Anyway this is a basically positive review, and I'll be happy to look at it again.


---

Attachment


---

Comment by craigcitro created at 2008-11-06 09:00:44

So the `calculus.py` failure above is a numerical noise issue, which (I hope!) is independent -- it seems to be #4436. 

Everything else comes from one single error: 

```
sage: pari(0).primepi()
BOOM!
```


I've fixed this, and all the above doctests pass.


---

Comment by cremona created at 2008-11-06 09:15:45

With the second patch applied on top of the first all the doctests which failed before (apart from the irrelevant calculus.py one) now pass. +1!

[Craig, I would still like to know what it was I did which caused the slowdown!]


---

Comment by cremona created at 2008-11-06 16:57:39

Replying to [comment:10 cremona]:

> [Craig, I would still like to know what it was I did which caused the slowdown!]

Was it just replacing the test g==1 with g==one (with one defined outside the loop)?  Maybe more classes (for which gcds are defined) should have an is_one() method as well as an is_zero() method?


---

Comment by craigcitro created at 2008-11-06 17:19:25

Hi John,

Actually, there were a few things that slowed it down. If you look at the case of `gcd(a,b)`, where `a` and `b` are of type `Integer`, then what we really need to do is call `a.gcd(b)` and return that result. 

In the current version, with these inputs, we:
  * check that `b is not None`
  * check `hasattr(a,"gcd")`
  * return `a.gcd(b)`

In the previous version, we:
  * do an import: `from sage.structure.sequence import Sequence`
  * create `Sequence((a,b))`
  * call `__GCD_sequence`
  * call `g = ZZ(0)`
  * call `g = g.gcd(a)`
  * call `g = g.gcd(b)`

So there are definitely just more steps going on. The two most expensive are the first two, as I recall. I think that just the import and the creation of the Sequence were roughly 2/3 of the time spent in `gcd(a,b)`! You can always check this by setting `a` and `b` and doing `%timeit` from the command line.

One more note: after the patch, it would actually be *faster* to do a `try`/`except` instead of the `hasattr` in the case of two `Integer`s, by a constant factor that's roughly 10% for tiny integers. However, it costs us a factor of 2-3 in the case of Python `int` or `long` -- and since these classes don't have a `gcd` method, I think this is where the code gets used most.


---

Comment by cremona created at 2008-11-06 18:33:46

Thanks -- that's a very interesting and useful explanation (which probably deserves a wider audience).  It would be nice to think that our review system for patches might have caught that.

Perhaps something we ought to add to a standard review is to check the times of doctests before and after.  But that would not be very easy since of course patches add doctests.


---

Comment by mabshoff created at 2008-11-07 18:00:58

Unfortunately this patch has now a conflict:

```
mabshoff`@`sage:/scratch/mabshoff/release-cycle/sage-3.2.rc0/devel/sage$ less sage/rings/arith.py.rej
***************
*** 795,802 ****
          sage: next_prime(2004)
          2011
      """
-     n = integer_ring.ZZ(n)
-     return n.next_prime(proof=proof)
  
  def previous_prime(n):
      """
--- 726,732 ----
          sage: next_prime(2004)
          2011
      """
+     return ZZ(n).next_prime(proof=proof)
  
  def previous_prime(n):
      """
```

I am pretty sure this is caused by #4452 which I just merged on top of 3.2.alpha3.

Cheers,

Michael


---

Attachment


---

Attachment

This should work. Apply


```
trac-4443-rebase.patch
trac-4443-pt2.patch
trac-4443-pt3.patch
```


in that order.


---

Comment by cremona created at 2008-11-07 21:01:40

It does work.  To a fresh 3.2.alpha3 clone I applied the 4452 patch and then the three listed above and had  no conflicts.

All doctests in sage/rings and sage/libs/pari pass.


---

Comment by mabshoff created at 2008-11-08 05:17:21

Merged trac-4443-rebase.patch, trac-4443-pt2.patch and trac-4443-pt3.patch in Sage 3.2.rc0

Cheers,

Michael


---

Comment by mabshoff created at 2008-11-08 05:17:21

Resolution: fixed
