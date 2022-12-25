# Issue 6070: Get doctest coverage in sage/modular to 100%

archive/issues_006070.json:
```json
{
    "body": "Assignee: @loefflerd\n\nCC:  @JohnCremona\n\nKeywords: documentation, modular symbols\n\nThis is a follow-up of #6042. That patch increased doctest coverage in the modular subdirectory from 91.8% to 96.4%. I have finished off the job by doctesting the last few files in sage/modular/modsym, and will upload a patch soon (once I have got a ticket number to put in the patch header, and run full tests on 4.0.alpha0).\n\nIssue created by migration from https://trac.sagemath.org/ticket/6070\n\n",
    "created_at": "2009-05-18T14:05:40Z",
    "labels": [
        "component: modular forms",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0",
    "title": "Get doctest coverage in sage/modular to 100%",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6070",
    "user": "https://github.com/loefflerd"
}
```
Assignee: @loefflerd

CC:  @JohnCremona

Keywords: documentation, modular symbols

This is a follow-up of #6042. That patch increased doctest coverage in the modular subdirectory from 91.8% to 96.4%. I have finished off the job by doctesting the last few files in sage/modular/modsym, and will upload a patch soon (once I have got a ticket number to put in the patch header, and run full tests on 4.0.alpha0).

Issue created by migration from https://trac.sagemath.org/ticket/6070





---

archive/issue_comments_048216.json:
```json
{
    "body": "Here's a patch. The description has a typo; you're not meant to apply it over itself :-) It should say \"apply over #6042 and #5080\". (Without #5080 the patch will still apply, but two doctests in `sage/modular/modsym/space.py` will fail.)\n\nIn the course of doctesting the latex output functions for modular symbols, I found a bug in `sage/misc/latex.py` (it omits plus signs when latexing a formal linear combination if all the coefficients are 1). So that is also fixed in the above patch.",
    "created_at": "2009-05-18T14:37:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6070",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6070#issuecomment-48216",
    "user": "https://github.com/loefflerd"
}
```

Here's a patch. The description has a typo; you're not meant to apply it over itself :-) It should say "apply over #6042 and #5080". (Without #5080 the patch will still apply, but two doctests in `sage/modular/modsym/space.py` will fail.)

In the course of doctesting the latex output functions for modular symbols, I found a bug in `sage/misc/latex.py` (it omits plus signs when latexing a formal linear combination if all the coefficients are 1). So that is also fixed in the above patch.



---

archive/issue_comments_048217.json:
```json
{
    "body": "Great job.  Applies fine as advertised and all looks very good.\n\nSmall point 1: in the preamble to boundary.py there a re  few things nto in math mode which could be (e.g. Gamma1).\n\nSmall point 2: is it intended that g1list & ghlist are not included in the reference manual?\n\nI'm giving this a positive review anyway, but if David wants to make further small changes he is welcome.",
    "created_at": "2009-05-18T15:53:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6070",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6070#issuecomment-48217",
    "user": "https://github.com/JohnCremona"
}
```

Great job.  Applies fine as advertised and all looks very good.

Small point 1: in the preamble to boundary.py there a re  few things nto in math mode which could be (e.g. Gamma1).

Small point 2: is it intended that g1list & ghlist are not included in the reference manual?

I'm giving this a positive review anyway, but if David wants to make further small changes he is welcome.



---

archive/issue_comments_048218.json:
```json
{
    "body": "I can't help taking the bait. Further patch coming. This would have taken me rather less time if I hadn't uncovered yet another bug in the process (see #6072).",
    "created_at": "2009-05-18T17:55:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6070",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6070#issuecomment-48218",
    "user": "https://github.com/loefflerd"
}
```

I can't help taking the bait. Further patch coming. This would have taken me rather less time if I hadn't uncovered yet another bug in the process (see #6072).



---

archive/issue_comments_048219.json:
```json
{
    "body": "It looks fine to me ( and I hardly dare suggesting anything else new or David would write a whole book!).\n\nExtra patch applies fine on top of old, and builds (inc. reference html) fine.  And it looks very good (including the two new files now in the ref man).",
    "created_at": "2009-05-18T18:43:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6070",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6070#issuecomment-48219",
    "user": "https://github.com/JohnCremona"
}
```

It looks fine to me ( and I hardly dare suggesting anything else new or David would write a whole book!).

Extra patch applies fine on top of old, and builds (inc. reference html) fine.  And it looks very good (including the two new files now in the ref man).



---

archive/issue_comments_048220.json:
```json
{
    "body": "This patch by itself causes a doctest failure for the pickle jar:\n\n```\nsage -t -long \"devel/sage/sage/structure/sage_object.pyx\"   \n**********************************************************************\nFile \"/scratch/mabshoff/sage-4.0.rc0/devel/sage/sage/structure/sage_object.pyx\", line 724:\n    sage: sage.structure.sage_object.unpickle_all(std)\nExpected:\n    doctest:...: DeprecationWarning: RQDF is deprecated; use RealField(212) instead.\n    Successfully unpickled 483 objects.\n    Failed to unpickle 0 objects.\nGot:\n    ** failed:  _class__sage_modular_modform_cuspidal_submodule_CuspidalSubmodule_g1_Q__.sobj\n    doctest:1172: DeprecationWarning: RQDF is deprecated; use RealField(212) instead.\n    Failed:\n    _class__sage_modular_modform_cuspidal_submodule_CuspidalSubmodule_g1_Q__.sobj\n    Successfully unpickled 482 objects.\n    Failed to unpickle 1 objects.\n**********************************************************************\n1 items had failures:\n   1 of   7 in __main__.example_16\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file /scratch/mabshoff/sage-4.0.rc0/tmp/.doctest_sage_object.py\n         [3.2 s]\nexit code: 1024\n```\n\nThat is without #5080, so there is also the other two failures mentioned above. Note the comment on #5080 causing a significant slowdown in sage/schemes/elliptic_curves/sha_tate.py.\n\nSorry, but \"needs work\" :(\n\nCheers,\n\nMichael",
    "created_at": "2009-05-18T23:42:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6070",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6070#issuecomment-48220",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

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

archive/issue_comments_048221.json:
```json
{
    "body": "Attachment [trac_6070_new.patch](tarball://root/attachments/some-uuid/ticket6070/trac_6070_new.patch) by @loefflerd created at 2009-05-19 09:16:45\n\nreplaces both previous patches",
    "created_at": "2009-05-19T09:16:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6070",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6070#issuecomment-48221",
    "user": "https://github.com/loefflerd"
}
```

Attachment [trac_6070_new.patch](tarball://root/attachments/some-uuid/ticket6070/trac_6070_new.patch) by @loefflerd created at 2009-05-19 09:16:45

replaces both previous patches



---

archive/issue_comments_048222.json:
```json
{
    "body": "That will be because I promoted the G1list and GHlist classes from plain Python classes to Sage objects, which apparently breaks unpickling. There wasn't any particular reason to do this anyway -- it just seemed neater. So here is a new patch that doesn't do this.",
    "created_at": "2009-05-19T09:18:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6070",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6070#issuecomment-48222",
    "user": "https://github.com/loefflerd"
}
```

That will be because I promoted the G1list and GHlist classes from plain Python classes to Sage objects, which apparently breaks unpickling. There wasn't any particular reason to do this anyway -- it just seemed neater. So here is a new patch that doesn't do this.



---

archive/issue_comments_048223.json:
```json
{
    "body": "Since I gave the earlier patch a positive review I clearly don't know all the tests which need doing -- so Michael, is David's new patch passes your tests it is certainly ok with me.",
    "created_at": "2009-05-19T10:20:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6070",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6070#issuecomment-48223",
    "user": "https://github.com/JohnCremona"
}
```

Since I gave the earlier patch a positive review I clearly don't know all the tests which need doing -- so Michael, is David's new patch passes your tests it is certainly ok with me.



---

archive/issue_comments_048224.json:
```json
{
    "body": "Replying to [comment:8 cremona]:\n> Since I gave the earlier patch a positive review I clearly don't know all the tests which need doing -- so Michael, is David's new patch passes your tests it is certainly ok with me.\n\nI haven't tried the new patch yet, but the old one caused issues in `sage/modular/modsym/space.py` which were fixed by #5080. Unfortunately that ticket caused a massive slowdown (see David's comment toward the end why), so I cannot merge both tickets due to the slowdown and this ticket due to the failure.\n\nWe are about to leave for MSR, so I won't have net access for the next 8 hours or so.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-19T14:54:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6070",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6070#issuecomment-48224",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Replying to [comment:8 cremona]:
> Since I gave the earlier patch a positive review I clearly don't know all the tests which need doing -- so Michael, is David's new patch passes your tests it is certainly ok with me.

I haven't tried the new patch yet, but the old one caused issues in `sage/modular/modsym/space.py` which were fixed by #5080. Unfortunately that ticket caused a massive slowdown (see David's comment toward the end why), so I cannot merge both tickets due to the slowdown and this ticket due to the failure.

We are about to leave for MSR, so I won't have net access for the next 8 hours or so.

Cheers,

Michael



---

archive/issue_comments_048225.json:
```json
{
    "body": "apply over previous patch",
    "created_at": "2009-05-20T08:42:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6070",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6070#issuecomment-48225",
    "user": "https://github.com/loefflerd"
}
```

apply over previous patch



---

archive/issue_comments_048226.json:
```json
{
    "body": "Attachment [trac_6070_workaround.patch](tarball://root/attachments/some-uuid/ticket6070/trac_6070_workaround.patch) by @loefflerd created at 2009-05-20 08:49:10\n\nRight, well, here's a temporary solution. The reason for the doctest failures in `modsym/space.py` without #5080 was because #5080 changed the behaviour of `dual_free_module` slightly when the ambient space had sign 0 but the given subspace had fixed sign. The new doctests I added to {{{space.py}} relied on this changed behaviour. The new patch I've just uploaded makes a trivial change to these doctests so that they pass without having #5080 applied. So we can get this merged now, without it having to wait for me (or anyone else) to get around to fixing the speed regression at #5080.\n\nHow does that sound?\n\nDavid",
    "created_at": "2009-05-20T08:49:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6070",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6070#issuecomment-48226",
    "user": "https://github.com/loefflerd"
}
```

Attachment [trac_6070_workaround.patch](tarball://root/attachments/some-uuid/ticket6070/trac_6070_workaround.patch) by @loefflerd created at 2009-05-20 08:49:10

Right, well, here's a temporary solution. The reason for the doctest failures in `modsym/space.py` without #5080 was because #5080 changed the behaviour of `dual_free_module` slightly when the ambient space had sign 0 but the given subspace had fixed sign. The new doctests I added to {{{space.py}} relied on this changed behaviour. The new patch I've just uploaded makes a trivial change to these doctests so that they pass without having #5080 applied. So we can get this merged now, without it having to wait for me (or anyone else) to get around to fixing the speed regression at #5080.

How does that sound?

David



---

archive/issue_comments_048227.json:
```json
{
    "body": "Sounds good as a reasonable stopgap.  \n\nI applied both patches in turn to 4.0.alpha0.  There was this:\n\n```\npatching file sage/modular/modsym/ambient.py\nHunk #1 succeeded at 233 with fuzz 1 (offset -81 lines).\n```\n\nwhich I think can be ignored.  All tests (including long) in sage/modular pass, as does Michael's test of sage/structure/sage_object.pyx.  So I am reinstating the positive review and hoping for the best.",
    "created_at": "2009-05-20T09:03:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6070",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6070#issuecomment-48227",
    "user": "https://github.com/JohnCremona"
}
```

Sounds good as a reasonable stopgap.  

I applied both patches in turn to 4.0.alpha0.  There was this:

```
patching file sage/modular/modsym/ambient.py
Hunk #1 succeeded at 233 with fuzz 1 (offset -81 lines).
```

which I think can be ignored.  All tests (including long) in sage/modular pass, as does Michael's test of sage/structure/sage_object.pyx.  So I am reinstating the positive review and hoping for the best.



---

archive/issue_comments_048228.json:
```json
{
    "body": "(FWIW: That fuzz can certainly be safely ignored, as it comes from the fact that I cut out the patch on top of #6042, which is already merged.)",
    "created_at": "2009-05-20T09:07:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6070",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6070#issuecomment-48228",
    "user": "https://github.com/loefflerd"
}
```

(FWIW: That fuzz can certainly be safely ignored, as it comes from the fact that I cut out the patch on top of #6042, which is already merged.)



---

archive/issue_events_014247.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-05-21T00:13:15Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6070",
    "milestone": "sage-4.0",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6070#event-14247"
}
```



---

archive/issue_comments_048229.json:
```json
{
    "body": "With both patches applied all tests including the pickle jar pass. The speed regression due to #5080 is avoided since the doctest has been adjusted to not hit the bug, so we are good to go.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-21T00:13:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6070",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6070#issuecomment-48229",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

With both patches applied all tests including the pickle jar pass. The speed regression due to #5080 is avoided since the doctest has been adjusted to not hit the bug, so we are good to go.

Cheers,

Michael



---

archive/issue_events_014248.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-05-21T00:13:48Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6070",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6070#event-14248"
}
```



---

archive/issue_comments_048230.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-05-21T00:13:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6070",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6070#issuecomment-48230",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_048231.json:
```json
{
    "body": "Merged both patches in Sage 4.0.rc0.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-21T00:13:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6070",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6070#issuecomment-48231",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged both patches in Sage 4.0.rc0.

Cheers,

Michael
