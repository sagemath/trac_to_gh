# Issue 3663: add support for affine crystals

Issue created by migration from https://trac.sagemath.org/ticket/3663

Original creator: mhansen

Original creation time: 2008-07-16 00:41:55

Assignee: mhansen

CC:  sage-combinat bump@match.stanford.edu




---

Comment by aschilling created at 2009-05-27 21:32:37

Changing keywords from "" to "affine crystals".


---

Comment by aschilling created at 2009-05-27 21:32:37

Changing assignee from mhansen to aschilling.


---

Attachment


---

Attachment


---

Attachment


---

Attachment

improved documentation links added


---

Attachment

corrected problems with documentation in crystal_morphism


---

Comment by bump created at 2009-10-20 01:36:07

I am reviewing the version of the patch that is in the combinat queue, running under sage 4.1.1.

I ran `sage -testall`.
The patch introduces no new failures. (Where it appears in the queue there are some failures, but the same failures still occur if you qpop the patch, rebuild and run testall again, so they are not caused by this patch.)

All new methods have docstrings and tests.

Kirillov-Reshetikhin crystals for are crystal bases on modules of quantized enveloping algebras of affine Kac-Moody Lie algebras. They had their origin in the observation that it was sometimes possible to define crystal bases on the data parametrizing the eigenstates in the Bethe Ansatz. Beyond that, they tend to be perfect crystals, from which all integrable modules of the quantum group can be constructed. There is one Kirillov-Reshetikhin crystal `B(r,s)` based on tableaux of rectangular shape `s^r` for every positive integer s and index r of the underlying classical crystal.

Constructions of all for the classical untwisted and untwisted types are summarized in Fourier, Schilling and Okado
http://front.math.ucdavis.edu/0811.1604. Most but all of these are implemented in sage by this patch.

The unimplemented crystals are listed here: http://groups.google.com/group/sage-combinat-devel/msg/9571cf3991bca4db?hl=en

I generated quite a few of these and ran `C.check()` on them. I looked at a few of them more closely. I am confident that the patch is correct. It is also an important advance to have these affine crystals in sage.

Some useful functionality is also added in `crystals.py`. Namely, morphisms of crystals and some root string operations.


---

Comment by mhansen created at 2009-11-17 16:35:59

Changing status from new to needs_review.


---

Comment by mhansen created at 2009-11-17 16:36:06

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2009-11-19 17:01:55

Resolution: fixed
