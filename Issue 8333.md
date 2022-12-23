# Issue 8333: Finite fields to new coercion model

Issue created by migration from https://trac.sagemath.org/ticket/8333

Original creator: roed

Original creation time: 2010-02-23 15:07:26

Assignee: AlexGhitza

Moves finite fields to the new coercion model.


---

Attachment


---

Attachment

The two patches can be applied in either order.


---

Comment by roed created at 2010-02-23 17:37:44

Changing status from new to needs_review.


---

Comment by roed created at 2010-02-23 17:37:54

Part of a series:

```
8218 -> 8332 -> 7880 -> 7883 -> 8333 -> 8334 -> 8335
```

I tried to make each of these mostly self contained, with doctests passing after every ticket, but I didn't entirely succeed.  If you're reviewing one of these tickets, applying later tickets will hopefully fix doctest failures that you're seeing.


---

Comment by davidloeffler created at 2010-03-18 16:44:14

Some strange things going on here. I installed the patches on 4.3.4.rc0 with the preceding patches in the series applied. 

(1) It builds fine, but Sage won't start because the patched `finite_field_prime_modn.py` contains the line

```
from sage.rings.integer_mod_ring import IntegerModRing_generic
```

and that file has been removed by #8218.

(2) There is also a problem in `element_ext_pari.py` caused by the line

```
elif isinstance(value, FreeModuleElement):
```

being used without FreeModuleElement being imported first. 

(3) Next up, there's another issue in `element_ntl_gf2e` caused by trying to import `is_FiniteField` from the wrong place. 

(4) I'm getting a bunch of identical errors relating to the Singular library -- it says 

```
 File "/home/masiao/sage-4.3.4.rc0/local/lib/python/site-packages/sage/interfaces/singular.py", line 672, in has_coerce_map_from_impl
        raise NotImplementedError
```


(5) Something weird is going on in sage/modular/dirichlet.py which causes an infinite recursion error when reducing an element of a number field modulo a prime; this may well be dealt with by #8334, I haven't checked. Same in three places in sage/schemes/elliptic_curves/ell_point.py and a bunch of other elliptic curves modules, and in sage/rings/residue_field.py

(6) The patch changes a whole load of doctests in sage/libs/flint/zmod_poly_linkage for no apparent reason, and thus causes them to fail. (Are you running a newer FLINT version on your development machine?)

(7)  Various errors in the rings/finite_rings directory, e.g. this one: 

```
File "/home/masiao/sage-4.3.4.rc0/local/lib/python/site-packages/sage/rings/finite_rings/finite_field_ext_pari.py", line 580, in _coerce_map_from_
        elif self.degree() % K.degree() == 0:
    NameError: global name 'K' is not defined
```



Most of these are trivial, but (4) is beyond my ability to fix. I'm sorry, but that's definitely a "needs work".


---

Comment by davidloeffler created at 2010-03-18 16:44:14

Changing status from needs_review to needs_work.


---

Comment by davidloeffler created at 2010-03-18 16:56:32

Ah, I see what's going on. Most of these are fixed by the patch `7585_12_1_fixes.patch` at #8334. But that is dependent on #7883, which needs some substantial work.

David, I suggest you do one of the following things:

- Fix #7883 as robertwb and I have suggested; once that has a positive review then we can go on and review this ticket and #8334 together.

- Back-port the fixes from #8334 that belong here, and then I will happily review it independently of #7883 and #8334.

David


---

Comment by roed created at 2010-09-19 13:21:37

Changing status from needs_work to needs_review.


---

Comment by roed created at 2010-09-19 13:21:37

I've addressed your and Robert's suggestions on #7883 I think.  Apply these two patches after the patches at #7883 and before the patches at #8334.  Doctests won't pass until you apply the patches at #8334.  But all three are ready for review.  Sorry for the delay.


---

Comment by lftabera created at 2010-09-19 16:17:52

roed, which version of sage are you using? I cannot apply 8333_finite_fields_to_new_coercion.patch cleanly to 4.5.3


---

Comment by roed created at 2010-09-20 03:38:41

I had been using 4.5.2, but I just upgraded and it still applies cleanly.

Did you apply 8333_parent_init.patch first?


---

Comment by jhpalmieri created at 2010-09-20 05:19:43

After applying both patches from #7883 and also 8333_parent_init.patch, I see this in 4.5.3:

```
sage: hg_sage.import_patch('Downloads/8333_finite_fields_to_new_coercion.patch')
cd "/Applications/sage_builds/sage-4.5.3/devel/sage" && hg status
cd "/Applications/sage_builds/sage-4.5.3/devel/sage" && hg status
cd "/Applications/sage_builds/sage-4.5.3/devel/sage" && hg import   "/Users/palmieri/Downloads/8333_finite_fields_to_new_coercion.patch"
applying /Users/palmieri/Downloads/8333_finite_fields_to_new_coercion.patch
patching file sage/libs/flint/zmod_poly_linkage.pxi
Hunk #1 FAILED at 455
Hunk #2 FAILED at 470
2 out of 2 hunks FAILED -- saving rejects to file sage/libs/flint/zmod_poly_linkage.pxi.rej
patching file sage/rings/finite_rings/finite_field_prime_modn.py
Hunk #1 FAILED at 57
1 out of 5 hunks FAILED -- saving rejects to file sage/rings/finite_rings/finite_field_prime_modn.py.rej
abort: patch failed to apply
```

In 4.6.alpha1, I see almost the same message:

```

sage: hg_sage.import_patch('Downloads/8333_finite_fields_to_new_coercion.patch')
cd "/Applications/sage/devel/sage" && hg status
cd "/Applications/sage/devel/sage" && hg status
cd "/Applications/sage/devel/sage" && hg import   "/Users/palmieri/Downloads/8333_finite_fields_to_new_coercion.patch"
applying /Users/palmieri/Downloads/8333_finite_fields_to_new_coercion.patch
patching file sage/libs/flint/zmod_poly_linkage.pxi
Hunk #1 FAILED at 455
Hunk #2 FAILED at 470
2 out of 2 hunks FAILED -- saving rejects to file sage/libs/flint/zmod_poly_linkage.pxi.rej
patching file sage/rings/finite_rings/finite_field_ext_pari.py
Hunk #1 succeeded at 243 with fuzz 2 (offset 6 lines).
patching file sage/rings/finite_rings/finite_field_prime_modn.py
Hunk #1 FAILED at 57
1 out of 5 hunks FAILED -- saving rejects to file sage/rings/finite_rings/finite_field_prime_modn.py.rej
abort: patch failed to apply
```



---

Comment by roed created at 2010-09-20 05:36:36

Rebased against 4.5.3


---

Attachment

Oops.  Try this one.


---

Comment by davidloeffler created at 2010-09-23 16:16:24

I've had a look at this, but with mixed success.

Applying `8333_parent_init.patch` and `8333_finite_fields_to_new_coercion.2.patch` to 4.6.alpha1 on top of the new folded, positively-reviewed patch at #7883, I get one trivial failure (because I backported a hunk of one of these patches to get #7883 to work). This is fine and can happily be ignored. However, it's very broken with just those two patches (Sage won't even start up, because of a broken import statement).

I tried applying all the hunks of `7585_12_1_fixes.2.patch` other than the ones involving residue fields. That almost worked, but not quite: there was still an infinite recursion error occuring in `residue_field.pyx`. 

David: can you either get this working on its own, or rebase the patches at #8334 so I can review this and #8334 together?


---

Comment by davidloeffler created at 2010-09-23 16:16:24

Changing status from needs_review to needs_work.


---

Comment by roed created at 2010-09-23 16:48:54

I've rebased all the patches against 4.6.alpha1.  Thanks for helping with this!


---

Comment by roed created at 2010-09-23 16:48:54

Changing status from needs_work to needs_review.


---

Attachment

Folded patch. Apply only this patch. Applies to 4.6.alpha1 + trac_7883-ideals-folded.patch.


---

Comment by davidloeffler created at 2010-09-24 14:29:21

I've uploaded a folded patch, which should apply cleanly to 4.6.alpha1 on top of the folded patch at #7883. Doctests do not pass if you apply this patch on its own, so *the positive review should be understood to apply to this patch and #8334 together*. See that ticket for precise directions as to which patches to apply.


---

Comment by davidloeffler created at 2010-09-24 14:29:21

Changing status from needs_review to positive_review.


---

Comment by davidloeffler created at 2010-09-24 15:27:03

Right, so we ended up preparing a single folded patch at #8334, so *don't apply any patches from this ticket* but close it when the patch at #8333 is merged.


---

Comment by mpatel created at 2010-09-28 11:12:28

Resolution: duplicate
