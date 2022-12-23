# Issue 8701: implement scalar-valued Siegel modular forms on Sp(4,Z)

Issue created by migration from https://trac.sagemath.org/ticket/8701

Original creator: AlexGhitza

Original creation time: 2010-04-17 07:01:23

Assignee: craigcitro

CC:  nilsskoruppa mraum tornaria was novoselt ncalexan mstreng

Keywords: siegel modular forms

At Sage Days 20.25 in Montreal, we have decided to submit an initial version of the Siegel modular forms code by Friday 16 April 2010.

It's now a few minutes before midnight, and lest I turn into a pumpkin, I am uploading a patch with what we have so far.

I'm marking it as "needs work" since there are still a number of issues to be resolved.  I'll list these in the comments soon.


---

Comment by AlexGhitza created at 2010-04-17 07:03:03

Changing status from new to needs_work.


---

Comment by was created at 2010-04-17 07:12:39

:-)


---

Comment by AlexGhitza created at 2010-04-17 08:42:09

To clarify: I submitted this just before midnight Seattle time, so one could argue that it was before the deadline :)

The patch applies cleanly to sage-4.3.5, and passes all but one test.  The doctest coverage is 99%.  The patch should also apply cleanly to earlier versions of Sage, but depending of how far back you go the tests might not pass any more.  I checked with sage-4.3.3 and it was fine.

Since this patch includes the patches at trac #8602 and #8681, it will fail to apply when those tickets get reviewed positively and merged.  In fact, #8602 just got merged into sage-4.4.alpha0, so I will eventually rebase the Siegel patch on top of that.

I believe that the objective of this first submission is to have something that works perfectly in the case of scalar-valued forms on `Sp(4,Z)`.  Here are the issues that I am aware of and are still blocking this:

 1. `SiegelModularFormsFunctor` does not completely fit in with the other similar functors in Sage.  For one thing, it seems that the right place to put it is in sage.categories.pushout.  We should have a careful look at this class.
 1. We need top-level documentation in `siegel_modular_form.py` that explains in detail how the code is meant to be used, what the interesting features are, etc.  We also need to explain how precisions work (either in the main file or in `siegel_modular_form_prec.py`
 1. The computation of the generators for `weights='all'` breaks at the fifth generator
 1. The argument `degree` in `_siegel_modular_forms_generators` should be properly documented, and there should be a doctest for it (I don't like the name "degree" BTW, because it already has a meaning for Siegel modular forms)
 1. The argument `default_prec` in `SiegelModularFormsAlgebra` should be documented
 1. There are a few docstrings left that are not valid ReST, and there is one error while building the documentation 
 1. We should have some tests of the form `TestSuite(s).run()`


---

Comment by AlexGhitza created at 2010-04-18 09:00:53

I am replacing the patch with one that has fixes for a couple of issues on the list (and I'm updating the list to reflect this).


---

Attachment

applies to sage-4.4.3 and sage-4.4.4.alpha0


---

Comment by AlexGhitza created at 2010-06-14 07:06:29

Since a few more prerequisites went into Sage, I had to rebase the patch so it applies to 4.4.3 and 4.4.4.alpha0.


---

Comment by ncalexan created at 2010-06-14 23:46:09

I am worried that the groups on which the forms are defined are specified by strings ('Gamma0(5)') and not on python objects.


---

Comment by was created at 2010-10-28 19:02:15

FYI, the patch is now in psage: http://code.google.com/p/purplesage/source/detail?r=508752edecf0b1f41373e5761a74b61c79024c50


---

Comment by ncryan created at 2011-03-01 19:20:25

Addresses many of the comments from before.   I need still need to add copyright information, include more examples at the top of siegel_modular_forms.py, and deal with the functor stuff.


---

Attachment

Addresses ncalexander's concern about the way the groups are defined


---

Attachment

Raises an exception when trying to find the image of a form F under the Hecke operator T(p) when p divides the level of F


---

Attachment

Fix an issue with sage 4.6.2


---

Comment by tornaria created at 2011-04-22 21:16:21

Have the constructor coerce the coefficients into the ring they're supposed to be


---

Attachment


---

Attachment


---

Comment by chapoton created at 2013-09-01 12:40:19

For the bot:

apply only trac_8701_siegel_folded_v1.patch

The folded patch trac_8701_siegel_folded_v1.patch can now be used as a new starting point.


---

Comment by chapoton created at 2013-09-01 12:53:39

apply only trac_8701_siegel_folded_v1.patch


---

Attachment

apply only trac_8701_siegel_folded_v1.patch


---

Comment by chapoton created at 2014-02-13 12:51:26

New commits:


---

Comment by git created at 2015-08-20 09:06:54

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2015-08-20 09:56:02

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2015-08-20 11:09:23

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2015-08-20 11:18:30

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2015-08-23 10:53:45

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2016-05-19 12:32:44

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2016-07-13 11:59:15

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2016-07-29 18:35:30

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2017-07-29 08:56:02

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2017-07-29 09:21:41

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2017-07-29 09:27:10

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2017-07-29 09:40:01

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2017-07-29 12:24:42

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2018-12-17 20:48:21

Branch pushed to git repo; I updated commit sha1. New commits:
