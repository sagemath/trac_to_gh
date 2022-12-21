# Issue 6070: Get doctest coverage in sage/modular to 100%

Issue created by migration from Trac.

Original creator: davidloeffler

Original creation time: 2009-05-18 14:05:40

Assignee: davidloeffler

CC:  cremona

Keywords: documentation, modular symbols

This is a follow-up of #6042. That patch increased doctest coverage in the modular subdirectory from 91.8% to 96.4%. I have finished off the job by doctesting the last few files in sage/modular/modsym, and will upload a patch soon (once I have got a ticket number to put in the patch header, and run full tests on 4.0.alpha0).


---

Comment by davidloeffler created at 2009-05-18 14:37:06

Here's a patch. The description has a typo; you're not meant to apply it over itself :-) It should say "apply over #6042 and #5080". (Without #5080 the patch will still apply, but two doctests in `sage/modular/modsym/space.py` will fail.)

In the course of doctesting the latex output functions for modular symbols, I found a bug in `sage/misc/latex.py` (it omits plus signs when latexing a formal linear combination if all the coefficients are 1). So that is also fixed in the above patch.


---

Comment by cremona created at 2009-05-18 15:53:40

Great job.  Applies fine as advertised and all looks very good.

Small point 1: in the preamble to boundary.py there a re  few things nto in math mode which could be (e.g. Gamma1).

Small point 2: is it intended that g1list & ghlist are not included in the reference manual?

I'm giving this a positive review anyway, but if David wants to make further small changes he is welcome.


---

Comment by davidloeffler created at 2009-05-18 17:55:20

I can't help taking the bait. Further patch coming. This would have taken me rather less time if I hadn't uncovered yet another bug in the process (see #6072).


---

Comment by cremona created at 2009-05-18 18:43:48

It looks fine to me ( and I hardly dare suggesting anything else new or David would write a whole book!).

Extra patch applies fine on top of old, and builds (inc. reference html) fine.  And it looks very good (including the two new files now in the ref man).


---

Comment by mabshoff created at 2009-05-18 23:42:57

This patch by itself causes a doctest failure for the pickle jar:

```
sage -t -long "devel/sage/sage/structure/sage_object.pyx"   
**********************************************************************
File "/scratch/mabshoff/sage-4.0.rc0/devel/sage/sage/structure/sage_object.pyx", line 724:
    sage: sage.structure.sage_object.unpickle_all(std)
Expected:
    doctest:...: DeprecationWarning: RQDF is deprecated; use RealField(212) instead.
    Successfully unpickled 483 objects.
    Failed to unpickle 0 objects.
Got:
    ** failed:  _class__sage_modular_modform_cuspidal_submodule_CuspidalSubmodule_g1_Q__.sobj
    doctest:1172: DeprecationWarning: RQDF is deprecated; use RealField(212) instead.
    Failed:
    _class__sage_modular_modform_cuspidal_submodule_CuspidalSubmodule_g1_Q__.sobj
    Successfully unpickled 482 objects.
    Failed to unpickle 1 objects.
**********************************************************************
1 items had failures:
   1 of   7 in __main__.example_16
***Test Failed*** 1 failures.
For whitespace errors, see the file /scratch/mabshoff/sage-4.0.rc0/tmp/.doctest_sage_object.py
         [3.2 s]
exit code: 1024
```

That is without #5080, so there is also the other two failures mentioned above. Note the comment on #5080 causing a significant slowdown in sage/schemes/elliptic_curves/sha_tate.py.

Sorry, but "needs work" :(

Cheers,

Michael


---

Attachment

replaces both previous patches


---

Comment by davidloeffler created at 2009-05-19 09:18:09

That will be because I promoted the G1list and GHlist classes from plain Python classes to Sage objects, which apparently breaks unpickling. There wasn't any particular reason to do this anyway -- it just seemed neater. So here is a new patch that doesn't do this.


---

Comment by cremona created at 2009-05-19 10:20:35

Since I gave the earlier patch a positive review I clearly don't know all the tests which need doing -- so Michael, is David's new patch passes your tests it is certainly ok with me.


---

Comment by mabshoff created at 2009-05-19 14:54:22

Replying to [comment:8 cremona]:
> Since I gave the earlier patch a positive review I clearly don't know all the tests which need doing -- so Michael, is David's new patch passes your tests it is certainly ok with me.

I haven't tried the new patch yet, but the old one caused issues in `sage/modular/modsym/space.py` which were fixed by #5080. Unfortunately that ticket caused a massive slowdown (see David's comment toward the end why), so I cannot merge both tickets due to the slowdown and this ticket due to the failure.

We are about to leave for MSR, so I won't have net access for the next 8 hours or so.

Cheers,

Michael


---

Comment by davidloeffler created at 2009-05-20 08:42:37

apply over previous patch


---

Attachment

Right, well, here's a temporary solution. The reason for the doctest failures in `modsym/space.py` without #5080 was because #5080 changed the behaviour of `dual_free_module` slightly when the ambient space had sign 0 but the given subspace had fixed sign. The new doctests I added to {{{space.py}} relied on this changed behaviour. The new patch I've just uploaded makes a trivial change to these doctests so that they pass without having #5080 applied. So we can get this merged now, without it having to wait for me (or anyone else) to get around to fixing the speed regression at #5080.

How does that sound?

David


---

Comment by cremona created at 2009-05-20 09:03:40

Sounds good as a reasonable stopgap.  

I applied both patches in turn to 4.0.alpha0.  There was this:

```
patching file sage/modular/modsym/ambient.py
Hunk #1 succeeded at 233 with fuzz 1 (offset -81 lines).
```

which I think can be ignored.  All tests (including long) in sage/modular pass, as does Michael's test of sage/structure/sage_object.pyx.  So I am reinstating the positive review and hoping for the best.


---

Comment by davidloeffler created at 2009-05-20 09:07:25

(FWIW: That fuzz can certainly be safely ignored, as it comes from the fact that I cut out the patch on top of #6042, which is already merged.)


---

Comment by mabshoff created at 2009-05-21 00:13:15

With both patches applied all tests including the pickle jar pass. The speed regression due to #5080 is avoided since the doctest has been adjusted to not hit the bug, so we are good to go.

Cheers,

Michael


---

Comment by mabshoff created at 2009-05-21 00:13:48

Resolution: fixed


---

Comment by mabshoff created at 2009-05-21 00:13:48

Merged both patches in Sage 4.0.rc0.

Cheers,

Michael
