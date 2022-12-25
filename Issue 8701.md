# Issue 8701: implement scalar-valued Siegel modular forms on Sp(4,Z)

archive/issues_008701.json:
```json
{
    "body": "Assignee: @craigcitro\n\nCC:  nilsskoruppa mraum @tornaria @williamstein @novoselt @ncalexan @mstreng\n\nKeywords: siegel modular forms\n\nAt Sage Days 20.25 in Montreal, we have decided to submit an initial version of the Siegel modular forms code by Friday 16 April 2010.\n\nIt's now a few minutes before midnight, and lest I turn into a pumpkin, I am uploading a patch with what we have so far.\n\nI'm marking it as \"needs work\" since there are still a number of issues to be resolved.  I'll list these in the comments soon.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8701\n\n",
    "created_at": "2010-04-17T07:01:23Z",
    "labels": [
        "component: modular forms"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-8.1",
    "title": "implement scalar-valued Siegel modular forms on Sp(4,Z)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8701",
    "user": "https://github.com/aghitza"
}
```
Assignee: @craigcitro

CC:  nilsskoruppa mraum @tornaria @williamstein @novoselt @ncalexan @mstreng

Keywords: siegel modular forms

At Sage Days 20.25 in Montreal, we have decided to submit an initial version of the Siegel modular forms code by Friday 16 April 2010.

It's now a few minutes before midnight, and lest I turn into a pumpkin, I am uploading a patch with what we have so far.

I'm marking it as "needs work" since there are still a number of issues to be resolved.  I'll list these in the comments soon.

Issue created by migration from https://trac.sagemath.org/ticket/8701





---

archive/issue_comments_079145.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2010-04-17T07:03:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8701",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8701#issuecomment-79145",
    "user": "https://github.com/aghitza"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_079146.json:
```json
{
    "body": ":-)",
    "created_at": "2010-04-17T07:12:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8701",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8701#issuecomment-79146",
    "user": "https://github.com/williamstein"
}
```

:-)



---

archive/issue_events_021111.json:
```json
{
    "actor": "https://github.com/aghitza",
    "created_at": "2010-04-17T08:42:09Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8701",
    "milestone": "sage-4.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8701#event-21111"
}
```



---

archive/issue_comments_079147.json:
```json
{
    "body": "To clarify: I submitted this just before midnight Seattle time, so one could argue that it was before the deadline :)\n\nThe patch applies cleanly to sage-4.3.5, and passes all but one test.  The doctest coverage is 99%.  The patch should also apply cleanly to earlier versions of Sage, but depending of how far back you go the tests might not pass any more.  I checked with sage-4.3.3 and it was fine.\n\nSince this patch includes the patches at trac #8602 and #8681, it will fail to apply when those tickets get reviewed positively and merged.  In fact, #8602 just got merged into sage-4.4.alpha0, so I will eventually rebase the Siegel patch on top of that.\n\nI believe that the objective of this first submission is to have something that works perfectly in the case of scalar-valued forms on `Sp(4,Z)`.  Here are the issues that I am aware of and are still blocking this:\n\n1. `SiegelModularFormsFunctor` does not completely fit in with the other similar functors in Sage.  For one thing, it seems that the right place to put it is in sage.categories.pushout.  We should have a careful look at this class.\n2. We need top-level documentation in `siegel_modular_form.py` that explains in detail how the code is meant to be used, what the interesting features are, etc.  We also need to explain how precisions work (either in the main file or in `siegel_modular_form_prec.py`\n3. The computation of the generators for `weights='all'` breaks at the fifth generator\n4. The argument `degree` in `_siegel_modular_forms_generators` should be properly documented, and there should be a doctest for it (I don't like the name \"degree\" BTW, because it already has a meaning for Siegel modular forms)\n5. The argument `default_prec` in `SiegelModularFormsAlgebra` should be documented\n6. There are a few docstrings left that are not valid ReST, and there is one error while building the documentation \n7. We should have some tests of the form `TestSuite(s).run()`",
    "created_at": "2010-04-17T08:42:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8701",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8701#issuecomment-79147",
    "user": "https://github.com/aghitza"
}
```

To clarify: I submitted this just before midnight Seattle time, so one could argue that it was before the deadline :)

The patch applies cleanly to sage-4.3.5, and passes all but one test.  The doctest coverage is 99%.  The patch should also apply cleanly to earlier versions of Sage, but depending of how far back you go the tests might not pass any more.  I checked with sage-4.3.3 and it was fine.

Since this patch includes the patches at trac #8602 and #8681, it will fail to apply when those tickets get reviewed positively and merged.  In fact, #8602 just got merged into sage-4.4.alpha0, so I will eventually rebase the Siegel patch on top of that.

I believe that the objective of this first submission is to have something that works perfectly in the case of scalar-valued forms on `Sp(4,Z)`.  Here are the issues that I am aware of and are still blocking this:

1. `SiegelModularFormsFunctor` does not completely fit in with the other similar functors in Sage.  For one thing, it seems that the right place to put it is in sage.categories.pushout.  We should have a careful look at this class.
2. We need top-level documentation in `siegel_modular_form.py` that explains in detail how the code is meant to be used, what the interesting features are, etc.  We also need to explain how precisions work (either in the main file or in `siegel_modular_form_prec.py`
3. The computation of the generators for `weights='all'` breaks at the fifth generator
4. The argument `degree` in `_siegel_modular_forms_generators` should be properly documented, and there should be a doctest for it (I don't like the name "degree" BTW, because it already has a meaning for Siegel modular forms)
5. The argument `default_prec` in `SiegelModularFormsAlgebra` should be documented
6. There are a few docstrings left that are not valid ReST, and there is one error while building the documentation 
7. We should have some tests of the form `TestSuite(s).run()`



---

archive/issue_comments_079148.json:
```json
{
    "body": "I am replacing the patch with one that has fixes for a couple of issues on the list (and I'm updating the list to reflect this).",
    "created_at": "2010-04-18T09:00:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8701",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8701#issuecomment-79148",
    "user": "https://github.com/aghitza"
}
```

I am replacing the patch with one that has fixes for a couple of issues on the list (and I'm updating the list to reflect this).



---

archive/issue_comments_079149.json:
```json
{
    "body": "Attachment [siegel_combined.patch](tarball://root/attachments/some-uuid/ticket8701/siegel_combined.patch) by @aghitza created at 2010-06-14 07:03:44\n\napplies to sage-4.4.3 and sage-4.4.4.alpha0",
    "created_at": "2010-06-14T07:03:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8701",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8701#issuecomment-79149",
    "user": "https://github.com/aghitza"
}
```

Attachment [siegel_combined.patch](tarball://root/attachments/some-uuid/ticket8701/siegel_combined.patch) by @aghitza created at 2010-06-14 07:03:44

applies to sage-4.4.3 and sage-4.4.4.alpha0



---

archive/issue_comments_079150.json:
```json
{
    "body": "Since a few more prerequisites went into Sage, I had to rebase the patch so it applies to 4.4.3 and 4.4.4.alpha0.",
    "created_at": "2010-06-14T07:06:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8701",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8701#issuecomment-79150",
    "user": "https://github.com/aghitza"
}
```

Since a few more prerequisites went into Sage, I had to rebase the patch so it applies to 4.4.3 and 4.4.4.alpha0.



---

archive/issue_comments_079151.json:
```json
{
    "body": "I am worried that the groups on which the forms are defined are specified by strings ('Gamma0(5)') and not on python objects.",
    "created_at": "2010-06-14T23:46:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8701",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8701#issuecomment-79151",
    "user": "https://github.com/ncalexan"
}
```

I am worried that the groups on which the forms are defined are specified by strings ('Gamma0(5)') and not on python objects.



---

archive/issue_comments_079152.json:
```json
{
    "body": "FYI, the patch is now in psage: http://code.google.com/p/purplesage/source/detail?r=508752edecf0b1f41373e5761a74b61c79024c50",
    "created_at": "2010-10-28T19:02:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8701",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8701#issuecomment-79152",
    "user": "https://github.com/williamstein"
}
```

FYI, the patch is now in psage: http://code.google.com/p/purplesage/source/detail?r=508752edecf0b1f41373e5761a74b61c79024c50



---

archive/issue_comments_079153.json:
```json
{
    "body": "Addresses many of the comments from before.   I need still need to add copyright information, include more examples at the top of siegel_modular_forms.py, and deal with the functor stuff.",
    "created_at": "2011-03-01T19:20:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8701",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8701#issuecomment-79153",
    "user": "https://trac.sagemath.org/admin/accounts/users/ncryan"
}
```

Addresses many of the comments from before.   I need still need to add copyright information, include more examples at the top of siegel_modular_forms.py, and deal with the functor stuff.



---

archive/issue_comments_079154.json:
```json
{
    "body": "Attachment [siegel_modular_group.patch](tarball://root/attachments/some-uuid/ticket8701/siegel_modular_group.patch) by ncryan created at 2011-04-21 23:04:20\n\nAddresses ncalexander's concern about the way the groups are defined",
    "created_at": "2011-04-21T23:04:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8701",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8701#issuecomment-79154",
    "user": "https://trac.sagemath.org/admin/accounts/users/ncryan"
}
```

Attachment [siegel_modular_group.patch](tarball://root/attachments/some-uuid/ticket8701/siegel_modular_group.patch) by ncryan created at 2011-04-21 23:04:20

Addresses ncalexander's concern about the way the groups are defined



---

archive/issue_comments_079155.json:
```json
{
    "body": "Attachment [hecke_operators_bad_primes_exception.patch](tarball://root/attachments/some-uuid/ticket8701/hecke_operators_bad_primes_exception.patch) by ncryan created at 2011-04-21 23:05:17\n\nRaises an exception when trying to find the image of a form F under the Hecke operator T(p) when p divides the level of F",
    "created_at": "2011-04-21T23:05:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8701",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8701#issuecomment-79155",
    "user": "https://trac.sagemath.org/admin/accounts/users/ncryan"
}
```

Attachment [hecke_operators_bad_primes_exception.patch](tarball://root/attachments/some-uuid/ticket8701/hecke_operators_bad_primes_exception.patch) by ncryan created at 2011-04-21 23:05:17

Raises an exception when trying to find the image of a form F under the Hecke operator T(p) when p divides the level of F



---

archive/issue_comments_079156.json:
```json
{
    "body": "Attachment [fix-siegel](tarball://root/attachments/some-uuid/ticket8701/fix-siegel) by @tornaria created at 2011-04-22 21:13:12\n\nFix an issue with sage 4.6.2",
    "created_at": "2011-04-22T21:13:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8701",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8701#issuecomment-79156",
    "user": "https://github.com/tornaria"
}
```

Attachment [fix-siegel](tarball://root/attachments/some-uuid/ticket8701/fix-siegel) by @tornaria created at 2011-04-22 21:13:12

Fix an issue with sage 4.6.2



---

archive/issue_comments_079157.json:
```json
{
    "body": "Have the constructor coerce the coefficients into the ring they're supposed to be",
    "created_at": "2011-04-22T21:16:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8701",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8701#issuecomment-79157",
    "user": "https://github.com/tornaria"
}
```

Have the constructor coerce the coefficients into the ring they're supposed to be



---

archive/issue_comments_079158.json:
```json
{
    "body": "Attachment [fix-coeffs-in-ring](tarball://root/attachments/some-uuid/ticket8701/fix-coeffs-in-ring) by @novoselt created at 2011-05-20 16:32:37",
    "created_at": "2011-05-20T16:32:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8701",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8701#issuecomment-79158",
    "user": "https://github.com/novoselt"
}
```

Attachment [fix-coeffs-in-ring](tarball://root/attachments/some-uuid/ticket8701/fix-coeffs-in-ring) by @novoselt created at 2011-05-20 16:32:37



---

archive/issue_events_021112.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8701",
    "milestone": "sage-4.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8701#event-21112"
}
```



---

archive/issue_events_021113.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8701",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8701#event-21113"
}
```



---

archive/issue_comments_079159.json:
```json
{
    "body": "Attachment [trac_8701_siegel_rebased.patch](tarball://root/attachments/some-uuid/ticket8701/trac_8701_siegel_rebased.patch) by @fchapoton created at 2013-09-01 12:18:09",
    "created_at": "2013-09-01T12:18:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8701",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8701#issuecomment-79159",
    "user": "https://github.com/fchapoton"
}
```

Attachment [trac_8701_siegel_rebased.patch](tarball://root/attachments/some-uuid/ticket8701/trac_8701_siegel_rebased.patch) by @fchapoton created at 2013-09-01 12:18:09



---

archive/issue_comments_079160.json:
```json
{
    "body": "For the bot:\n\napply only trac_8701_siegel_folded_v1.patch\n\nThe folded patch trac_8701_siegel_folded_v1.patch can now be used as a new starting point.",
    "created_at": "2013-09-01T12:40:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8701",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8701#issuecomment-79160",
    "user": "https://github.com/fchapoton"
}
```

For the bot:

apply only trac_8701_siegel_folded_v1.patch

The folded patch trac_8701_siegel_folded_v1.patch can now be used as a new starting point.



---

archive/issue_comments_079161.json:
```json
{
    "body": "apply only trac_8701_siegel_folded_v1.patch",
    "created_at": "2013-09-01T12:53:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8701",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8701#issuecomment-79161",
    "user": "https://github.com/fchapoton"
}
```

apply only trac_8701_siegel_folded_v1.patch



---

archive/issue_comments_079162.json:
```json
{
    "body": "Attachment [trac_8701_siegel_folded_v1.patch](tarball://root/attachments/some-uuid/ticket8701/trac_8701_siegel_folded_v1.patch) by @fchapoton created at 2013-09-06 19:18:51\n\napply only trac_8701_siegel_folded_v1.patch",
    "created_at": "2013-09-06T19:18:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8701",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8701#issuecomment-79162",
    "user": "https://github.com/fchapoton"
}
```

Attachment [trac_8701_siegel_folded_v1.patch](tarball://root/attachments/some-uuid/ticket8701/trac_8701_siegel_folded_v1.patch) by @fchapoton created at 2013-09-06 19:18:51

apply only trac_8701_siegel_folded_v1.patch



---

archive/issue_events_021114.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8701",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8701#event-21114"
}
```



---

archive/issue_events_021115.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8701",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8701#event-21115"
}
```



---

archive/issue_comments_079163.json:
```json
{
    "body": "New commits:",
    "created_at": "2014-02-13T12:51:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8701",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8701#issuecomment-79163",
    "user": "https://github.com/fchapoton"
}
```

New commits:



---

archive/issue_events_021116.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8701",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8701#event-21116"
}
```



---

archive/issue_events_021117.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8701",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8701#event-21117"
}
```



---

archive/issue_events_021118.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8701",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8701#event-21118"
}
```



---

archive/issue_events_021119.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8701",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8701#event-21119"
}
```



---

archive/issue_events_021120.json:
```json
{
    "actor": "https://github.com/fchapoton",
    "created_at": "2015-06-28T09:30:07Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8701",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8701#event-21120"
}
```



---

archive/issue_events_021121.json:
```json
{
    "actor": "https://github.com/fchapoton",
    "created_at": "2015-06-28T09:30:07Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8701",
    "milestone": "sage-6.8",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8701#event-21121"
}
```



---

archive/issue_comments_079164.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2015-08-20T09:06:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8701",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8701#issuecomment-79164",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_events_021122.json:
```json
{
    "actor": "https://github.com/fchapoton",
    "created_at": "2015-08-20T09:07:37Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8701",
    "milestone": "sage-6.8",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8701#event-21122"
}
```



---

archive/issue_events_021123.json:
```json
{
    "actor": "https://github.com/fchapoton",
    "created_at": "2015-08-20T09:07:37Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8701",
    "milestone": "sage-6.9",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8701#event-21123"
}
```



---

archive/issue_comments_079165.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2015-08-20T09:56:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8701",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8701#issuecomment-79165",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_079166.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2015-08-20T11:09:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8701",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8701#issuecomment-79166",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_079167.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2015-08-20T11:18:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8701",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8701#issuecomment-79167",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_079168.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2015-08-23T10:53:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8701",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8701#issuecomment-79168",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_079169.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2016-05-19T12:32:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8701",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8701#issuecomment-79169",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_079170.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2016-07-13T11:59:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8701",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8701#issuecomment-79170",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_079171.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2016-07-29T18:35:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8701",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8701#issuecomment-79171",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_079172.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2017-07-29T08:56:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8701",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8701#issuecomment-79172",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_079173.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2017-07-29T09:21:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8701",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8701#issuecomment-79173",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_079174.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2017-07-29T09:27:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8701",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8701#issuecomment-79174",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_events_021124.json:
```json
{
    "actor": "https://github.com/fchapoton",
    "created_at": "2017-07-29T09:28:21Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8701",
    "milestone": "sage-6.9",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8701#event-21124"
}
```



---

archive/issue_events_021125.json:
```json
{
    "actor": "https://github.com/fchapoton",
    "created_at": "2017-07-29T09:28:21Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8701",
    "milestone": "sage-8.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8701#event-21125"
}
```



---

archive/issue_comments_079175.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2017-07-29T09:40:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8701",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8701#issuecomment-79175",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_079176.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2017-07-29T12:24:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8701",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8701#issuecomment-79176",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_079177.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2018-12-17T20:48:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8701",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8701#issuecomment-79177",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:
