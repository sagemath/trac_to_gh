# Issue 3514: Free modules revision

Issue created by migration from https://trac.sagemath.org/ticket/3514

Original creator: kohel

Original creation time: 2008-06-26 15:28:01

Assignee: tbd

CC:  craigcitro ncalexan

Keywords: free modules

This separates quadratic modules into free_quadratic_module.py -- these 
are free modules with a user-specified inner product.

This adds 100% documentation to free_module.py and free_quadratic_module.py.

TODO: Probably we want to revise free module elements to make efficient use 
of diagonal inner_product_matrices.  I still intend to generalize the inner 
product matrix to support different image ring (real, complex, p-adic) for 
the pairing, as well as integral pairings which are given by rational matrices.



---

Comment by kohel created at 2008-06-26 15:28:43

free_modules.patch


---

Attachment


---

Comment by cremona created at 2008-06-29 17:49:37

Review by John Cremona:

    1.  I read through the code fairly carefully, and was very impressed by the thought which has gone into this.  There are a few typos in docstrings but nothing serious.
    2.  I tried applying the patch to 3.0.4.alpha0 but it failed:

```
applying /home/jec/free-modules.patch
patching file sage/modules/free_module.py
Hunk #4 FAILED at 280
Hunk #52 FAILED at 3200
Hunk #54 FAILED at 3310
Hunk #82 FAILED at 4430
Hunk #95 FAILED at 5053
5 out of 96 hunks FAILED -- saving rejects to file sage/modules/free_module.py.rej
abort: patch failed to apply
```


I expect that this is because it is based on a different release.  If I get time I'll try it on 3.0.3, but it would be much better if the author could re-base it!

Should we not have a requirement that the base version for posted patches whould always be specified (like I do...)?


---

Comment by kohel created at 2008-06-30 09:25:20

This patch applies to 3.02 (sorry for not specifying, John).

Nick Alexander expressed an interest in review this patch, 
and looked over some of it already at SAGE-Devel days.

This predates changes merging the coercion branch, so should 
first be patched to a pre-coercion SAGE.


---

Comment by cremona created at 2008-06-30 17:12:31

I happened to have a 3.0.2 build lying around, but it fared no better:

```

john@ubuntu%./sage 
----------------------------------------------------------------------
----------------------------------------------------------------------
Loading SAGE library. Current Mercurial branch is: 3514
sage: hg_sage.apply ("fre
free_module_element     frequency_distribution  
sage: hg_sage.apply("/home/john/free-modules.patch")
cd "/home/john/sage-3.0.2/devel/sage" && hg status
cd "/home/john/sage-3.0.2/devel/sage" && hg status
cd "/home/john/sage-3.0.2/devel/sage" && hg import   "/home/john/free-modules.patch"
applying /home/john/free-modules.patch
patching file sage/modules/free_module.py
Hunk #4 FAILED at 280
Hunk #54 FAILED at 3312
Hunk #82 FAILED at 4432
Hunk #95 FAILED at 5055
4 out of 96 hunks FAILED -- saving rejects to file sage/modules/free_module.py.rej
abort: patch failed to apply
```



---

Comment by gfurnish created at 2008-07-02 00:06:23

Rebased against 3.0.4.alpha1 and fixed all trivial errors/doctest problems.  This now needs review.


---

Comment by mabshoff created at 2008-07-02 20:12:12

The patch posted by Gary does not apply cleanly against 3.0.4.alpha1 or 2:

```
sage-3.0.4.alpha2/devel/sage$ patch -p1 --dry-run < trac_3514.patch\?format\=raw 
patching file sage/modules/all.py
patching file sage/modules/free_module.py
patching file sage/modules/free_quadratic_module.py
patching file sage/modules/quotient_module.py
patching file sage/coding/code_constructions.py
patching file sage/modular/modform/hecke_operator_on_qexp.py
patching file sage/modular/modsym/space.py
patching file sage/modules/free_module.py
Hunk #1 succeeded at 264 (offset -17 lines).
Hunk #2 succeeded at 289 (offset -17 lines).
Hunk #3 FAILED at 444.
Hunk #4 FAILED at 872.
Hunk #5 FAILED at 3044.
Hunk #6 succeeded at 2843 (offset -390 lines).
Hunk #7 succeeded at 2945 (offset -388 lines).
Hunk #8 FAILED at 3436.
Hunk #9 succeeded at 4140 (offset -927 lines).
Hunk #10 succeeded at 4204 (offset -927 lines).
4 out of 10 hunks FAILED -- saving rejects to file sage/modules/free_module.py.rej
patching file sage/modules/quotient_module.py
patching file sage/rings/number_field/order.py
patching file sage/schemes/elliptic_curves/period_lattice.py
```


David also posted a diff and Gary's patch commits all of the changes in Gary's name, which is obviously not correct.

Cheers,

Michael


---

Comment by mhansen created at 2008-07-02 21:03:29

I'll be an editor for this.


---

Comment by mhansen created at 2008-07-02 21:03:29

Changing keywords from "free modules" to "free modules editor_mhansen".


---

Attachment

I've attached trac_3514.2.patch which applies cleanly against 3.0.4.rc0.


---

Comment by mhansen created at 2008-07-09 00:36:48

Overall, I think that the patch is really good since it adds lots of good documentation and cleans things up by separating out the QuadraticSpaces.  There are a few minor things that I'd like to see addressed:

1) There are a number of "naked excepts" on lines 607,2118,2123,2239,2244,... of free_module.py that really should specify the particular type of error they are trying to catch.

2) The tests for a a couple functions that raise NotImplementedErrors do not actually test the function.  The ones I saw were __hash__ on 458, __cmp__ on 770, and echelonized_basis_matrix on 982 of free_module.py.

3) It seems there is a lot of code duplication in the span_of_basis's that could be factored out.

4) The BUG listed on line 4564 actually works fine for me.  On a related note, you need to write special code (using the __reduce__ method) if you want loads(dumps(s)) to be the exact same object as s.  This is relevant to line 111.


---

Comment by mhansen created at 2008-08-07 01:26:00

I added trac_3514-review.patch that addresses the issues above.  It'd be good for someone to review my new patch -- it should be pretty easy.

I deviated a bit from my own review comments in a few places.

2) I removed __hash__ and __cmp__ since they didn't serve any purpose, but I left echelonized_basis_matrix because the docstring provided nontrivial information for any subclass that hasn't implemented echelonized_basis_matrix.

3) After looking at the code, I thought it was more clear to leave the little bit of duplication that was there.

4) I removed line 111 since loads(dumps()) isn't guaranteed to return the exact same object.


---

Attachment


---

Comment by robertwb created at 2008-08-09 07:03:01

Switching the order of the arguments in `span` is backwards incompatible (and I have seen code that will break under this switch). The old ordering should still be accepted even if you want to make it so the basering is optional. 

In that same function, testing {{{
if not isinstance(R, principal_ideal_domain.PrincipalIdealDomain)
}}}

is potentially brittle, as there are rings which are PID's depending on their parameters (e.g. polynomial rings, Z/nZ, etc.


---

Comment by was created at 2008-08-10 22:31:52

I read the review patch by Mike Hansen.
I haven't doctested it.
I definitely agree with the changes he made though.


---

Comment by mabshoff created at 2008-08-10 22:45:00

The two patches applied after #3652 pass doctests in my current 3.1.alpha1 merge tree. So once we get a positive review here we can finally merge.

Cheers,

Michael


---

Comment by was created at 2008-08-11 06:17:04

I think this looks good.  I looked over the original patches, and also mike's comments, and this looks good.  I'm very impressed by the amount of new doctests, etc.  Yeah!


---

Comment by mabshoff created at 2008-08-11 06:29:16

Resolution: fixed


---

Comment by mabshoff created at 2008-08-11 06:29:16

Merged trac_3514.2.patch and trac_3514-review.patch in Sage 3.1.alpha1


---

Comment by was created at 2008-08-11 06:33:41

Robert's comment: "Switching the order of the arguments in span is backwards incompatible (and I have seen code that will break under this switch). The old ordering should still be accepted even if you want to make it so the basering is optional."  

I agree! See patch.


---

Attachment

Merged sage-3514_span.patch in Sage 3.1.alpha1
