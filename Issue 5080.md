# Issue 5080: Bug in decomposing modular symbol subspace

Issue created by migration from Trac.

Original creator: robertwb

Original creation time: 2009-01-24 00:31:15

Assignee: craigcitro

CC:  craigcitro


```
sage: E = EllipticCurve("128a") 
sage: E.congruence_number()
------------------------------------------------------------
Traceback (most recent call last):
  File "<ipython console>", line 1, in <module>
  File "/Users/robert/sage/sage-3.1.3/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_rational_field.py", line 2618, in congruence_number
    self.__congruence_number = W.congruence_number(V)
  File "/Users/robert/sage/sage-3.1.3/local/lib/python2.5/site-packages/sage/modular/modsym/space.py", line 938, in congruence_number
    W = other.q_expansion_module(prec, ZZ)
  File "/Users/robert/sage/sage-3.1.3/local/lib/python2.5/site-packages/sage/modular/modsym/space.py", line 770, in q_expansion_module
    return self._q_expansion_module_integral(prec)
  File "/Users/robert/sage/sage-3.1.3/local/lib/python2.5/site-packages/sage/modular/modsym/space.py", line 910, in _q_expansion_module_integral
    V = self.q_expansion_module(prec, QQ)
  File "/Users/robert/sage/sage-3.1.3/local/lib/python2.5/site-packages/sage/modular/modsym/space.py", line 772, in q_expansion_module
    return self._q_expansion_module_rational(prec)
  File "/Users/robert/sage/sage-3.1.3/local/lib/python2.5/site-packages/sage/modular/modsym/space.py", line 861, in _q_expansion_module_rational
    return self._q_expansion_module(prec)
  File "/Users/robert/sage/sage-3.1.3/local/lib/python2.5/site-packages/sage/modular/modsym/space.py", line 820, in _q_expansion_module
    return A.span([f.padded_list(prec) for f in self.q_expansion_basis(prec, algorithm)])
  File "/Users/robert/sage/sage-3.1.3/local/lib/python2.5/site-packages/sage/modular/modsym/space.py", line 602, in q_expansion_basis
    return Sequence(self._q_expansion_basis_hecke_dual(prec), cr=True)
  File "/Users/robert/sage/sage-3.1.3/local/lib/python2.5/site-packages/sage/modular/modsym/space.py", line 1073, in _q_expansion_basis_hecke_dual
    v = [self.dual_hecke_matrix(n).column(i) for n in range(1,prec)]
  File "/Users/robert/sage/sage-3.1.3/local/lib/python2.5/site-packages/sage/modular/hecke/module.py", line 797, in dual_hecke_matrix
    T = self._compute_dual_hecke_matrix(n)
  File "/Users/robert/sage/current/local/lib/python2.5/site-packages/sage/modular/hecke/submodule.py", line 110, in _compute_dual_hecke_matrix
    return A.restrict(self.dual_free_module(), check=check)
  File "/Users/robert/sage/current/local/lib/python2.5/site-packages/sage/modular/hecke/submodule.py", line 320, in dual_free_module
    "(cut down to rank %s, but should have cut down to rank %s)."%(V.rank(), self.rank())
RuntimeError: Computation of embedded dual vector space failed (cut down to rank 9, but should have cut down to rank 8).
```



---

Comment by AlexGhitza created at 2009-01-24 01:17:45

for the record, here are all the optimal elliptic curves of conductor at most 250 that exhibit the same problem (listed with Cremona labels): 128a1, 128b1, 128c1, 128d1, 144b1, 192a1, 192b1, 192c1, 192d1, 225c1, 225d1, 225e1


---

Comment by davidloeffler created at 2009-05-13 17:26:01

I have had a careful look at this, and I think I know what's going on. The problem is that for each of these curves, if f is the corresponding newform, then there is a finite set of forms f_1 ... f_m (none of them equal to f) in the space such that for every p, a_p(f) = a_p(f_i) for some i. It was a bit of a surprise to me that this is possible, but it doesn't contradict multiplicity one, and in fact if you take any fixed form and consider its twists by chi1, chi2, and chi1 * chi2 for any two quadratic characters chi1, chi2 of coprime moduli then you get an example.

This mightily confuses two functions for submodules of Hecke modules: "complement" and "dual_free_module". The former has a workaround, in that if it can't find a complement using only one Hecke operator at a time, it falls back on calling "decomposition" (which is slower, but is immune to this problem) and works out the complement using that. The latter doesn't. But anyway, the two are basically doing the same thing, since the embedded dual free module of a submodule V is by definition the annihilator of the Hecke-stable complement of V (when this exists). So the fix is to get rid of the existing "dual_free_module" routine and replace it with a simpler routine that calls "complement" and then does some trivial linear algebra.

I will post a patch when I get a chance to code it up.


---

Attachment

apply after #5736, #4357 and #5787


---

Comment by davidloeffler created at 2009-05-14 11:44:17

Here's a patch.


---

Comment by cremona created at 2009-05-18 15:27:26

I'm about to try this out.  Is there a doctest showing that 

```
sage: E = EllipticCurve("128a") 
sage: E.congruence_number()
```

now works?


---

Comment by cremona created at 2009-05-18 15:30:28

Replying to [comment:4 cremona]:
> I'm about to try this out.  Is there a doctest showing that 
> {{{
> sage: E = EllipticCurve("128a") 
> sage: E.congruence_number()
> }}}
> now works?

Which it does:

```
sage: sage: E = EllipticCurve("128a")
sage: sage: E.congruence_number()
32
```



---

Comment by cremona created at 2009-05-18 15:47:13

Patch looks good, applies fine to 4.0.alpha0 and fixes the bug.  My only quibble is that there is no new doctest to show that the reported bug is fixed.


---

Attachment

apply after previous patch


---

Comment by davidloeffler created at 2009-05-18 15:51:30

Sorry, that was very sloppy of me. Here is a patchlet that adds the missing doctest.


---

Comment by cremona created at 2009-05-18 15:58:22

Brilliant.  And I forgot to say (on one of these tickets) -- we do now have 100% coverage on all sage/modular/modsym, and all tests pass.


---

Comment by mabshoff created at 2009-05-18 23:53:05

Unfortunately this patch causes a massive speed regression:

```
sage: time EllipticCurve('858k2').sha().an_padic(Integer(7))
CPU times: user 8.90 s, sys: 0.33 s, total: 9.23 s
Wall time: 9.52 s
7^2 + O(7^3)
```

With both patches from this ticket this one alone takes minutes, so sorry, but "needs work".

Cheers,

Michael


---

Comment by davidloeffler created at 2009-05-19 07:46:44

Groan, I suppose that going via complement to get dual free module is probably slower when the Hecke matrices are very sparse, as they are here. I generally worry first about getting a mathematically correct answer, and only then about efficiency issues. Can't look at this right now, sorry -- I've already spent far too much time on Sage stuff in the last week or two -- might get around to it sometime next week.


---

Comment by craigcitro created at 2009-05-19 08:44:16

Hey David,

It's definitely the right choice to go for correctness over speed first. I'll look into speeding this up in the next few days, if you don't beat me to it. As the simplest possible attempt, though, couldn't we just drop your new code in where the `RuntimeError` is raised? Obviously this isn't the classiest fix, but it wouldn't be bad as a first approximation.


---

Comment by davidloeffler created at 2009-05-19 09:31:49

Hi Craig,

It's a delicate thing. There are two potential first-approximation algorithms for computing complements, or (equivalently) embedded duals: either work on the dual side (cutting down to the smallest space on which Hecke acts like it does on self) or work on the ambient side (cutting down to the smallest space on which Hecke acts like it does on the quotient ambient/self). 

What we had before was one algorithm in `complement` and the other in `dual_free_module`, never exploiting the fact that the two problems are essentially equivalent. I standardised on the algorithm that `complement` was using, largely because the code to handle the pathological case (for which neither algorithm works) was already there in the `complement` routine.

The classy fix is to heuristically choose which algorithm to use, because (in non-pathological cases) the dual-side version is much quicker when the given submodule is much smaller than the ambient space, and the ambient-side version is much quicker when the given submodule is most of the ambient space. This is (roughly) what is meant by the comment in `submodule.py` saying:

```
# TODO: optimize in some cases by computing image of
# complementary factor instead of kernel...?
```


David


---

Comment by davidloeffler created at 2009-05-25 19:18:18

replaces all previous patches


---

Attachment

Here's a new patch, which causes no speed regression at all in the p-adic analytic sha for 858k1, and still solves the original 128a congruence number problem.


---

Comment by cremona created at 2009-05-30 16:09:12

Craig, are you going to review David's new patch here?  Or shall I?


---

Comment by craigcitro created at 2009-05-30 16:15:45

Hi John -- I'm planning on looking at it somewhat soon, but feel free to beat me to it! :)


---

Comment by davidloeffler created at 2009-06-08 08:27:58

Changing status from new to assigned.


---

Comment by davidloeffler created at 2009-06-08 08:27:58

Changing assignee from craigcitro to davidloeffler.


---

Comment by craigcitro created at 2009-06-20 09:12:07

Sorry I've been so slow about getting to this.

The patch looks great, but I have one gripe. I hate the fact that we're working around Python's "private" obfuscation (the `_HeckeSubmodule__attr` thing). It's brittle, because if the class name changes, or if certain methods get overridden, it'll break. Worse, it's ugly. `:)` I think we should fix it, though I'm not sure I know the "right" way. Some options:

 * change these to attributes with a single underscore 
 * set these attributes to `None` in the constructor, and check if they're not `None`
 * I know the `combinat` branch has a `cached_method` decorator -- I don't know if it has a system for checking if the attribute is set, but it might.

I guess I'd lean towards the third if it works, and if not, the second (and filing a trac ticket asking for the enhancement to `cached_method`). One option I *don't* like: adding flags for each attribute to see if it's set.


---

Comment by davidloeffler created at 2009-06-20 09:34:15

Good point. I've become rather fond of `@`cached_function and `@`cached_method -- I have a patch which I haven't uploaded yet which removes about 100 lines of caching code from sage/modular/modform by systematically using `@`cached_method -- but it hadn't occurred to me to use it in this way. It seems that cached methods have a method "is_in_cache"; and if the method takes no arguments, you can call "is_in_cache" with no arguments either, and it works fine. 

I will do a new patch, but in 28 hours I will be catching a plane to Barcelona for SD16, so it might not get done before next weekend.
David


---

Comment by davidloeffler created at 2009-06-20 10:08:21

apply over trac_5080_new.patch


---

Attachment

For the first time I can remember, I wrote a fix and it worked first time. Here is a patch which removes all instances of "hasattr".

(There is potential for cleaning up elsewhere in sage/modular/hecke/submodule.py using cached_method -- the is_new, is_old, new_submodule, old_submodule calls have their own caching code which we can now get rid of -- but that is for another ticket.)

David


---

Comment by craigcitro created at 2009-06-20 21:38:13

Looks good, and I'm very happy with the changes.


---

Comment by rlm created at 2009-06-24 09:50:12

Resolution: fixed


---

Comment by was created at 2009-06-28 15:00:48

Changing status from closed to reopened.


---

Comment by was created at 2009-06-28 15:00:48


```
On Jun 27, 11:54 pm, davidloeffler <dave.loeff...`@`gmail.com> wrote:
> On SuSE, 32-bit, sage -testall -long passes except for errors in the
> same three files Jaap reported above (and a harmless timeout in
> elliptic curves).

I spoke too soon. Something rather harmful has in fact happened: the
wrong patches have been merged for track #5080. My first attempt at
fixing this problem caused a catastrophic slowdown in elliptic curve
Sha routines, so I started again from scratch and did a new patch that
worked differently. It seems that the old patch has been merged, with
the result that

sage: EllipticCurve("858k1").sha().an_padic(7)

has been slowed down by *several orders of magnitude*. That was why I
was seeing timeouts in that file.

To reiterate: the patch "trac_5080.patch" on that ticket is evil, bad
and wrong, should not have been merged, and must be removed from Sage
ASAP.

David
```



---

Comment by was created at 2009-06-28 15:00:48

Resolution changed from fixed to 


---

Comment by was created at 2009-06-28 15:01:36

Changing priority from major to blocker.


---

Attachment

Apply to 4.1.alpha2


---

Comment by davidloeffler created at 2009-06-28 17:35:47

I've just uploaded the patch trac_5080_repair.patch. Apply this patch (only) to 4.1.alpha2 gets hecke/submodule.py into the intended state. I've checked that this passes doctests in sage/modular/hecke, and that mabshoff's 858k2 example computes within a reasonable time limit.

David


---

Comment by cremona created at 2009-06-28 17:58:31

I checked that the new patch applies cleanly to 4.1.alpha2, all tests in modular/hecke pass, and the function mabshoff highlighted runs fine in about 10s.

The tag still said "positive review", but now it deserves it again.


---

Comment by rlm created at 2009-06-29 20:56:11

Resolution: fixed


---

Comment by rlm created at 2009-06-29 20:56:11

Merged the fix patch into sage-4.1.alpha3.
