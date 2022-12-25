# Issue 4340: [with patch, positive review] Speed up Victor Miller basis code

archive/issues_004340.json:
```json
{
    "body": "Assignee: @craigcitro\n\nThe current Victor Miller basis code in Sage is painfully slow. \n\nI've already written much faster code, which I'll submit shortly.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4340\n\n",
    "closed_at": "2008-10-31T03:53:43Z",
    "created_at": "2008-10-22T18:16:47Z",
    "labels": [
        "component: modular forms",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2",
    "title": "[with patch, positive review] Speed up Victor Miller basis code",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4340",
    "user": "https://github.com/craigcitro"
}
```
Assignee: @craigcitro

The current Victor Miller basis code in Sage is painfully slow. 

I've already written much faster code, which I'll submit shortly.

Issue created by migration from https://trac.sagemath.org/ticket/4340





---

archive/issue_comments_031771.json:
```json
{
    "body": "This code is a **massive** speedup over the old code, and is still not as fast as I'm planning on making it. Even in examples as small as `victor_miller_basis(300,100)`, this gives a factor of 900 speedup. It's also now faster than Magma.\n\nI'm pretty sure I've got all the corner cases covered, too, but one can never be sure about these things ...",
    "created_at": "2008-10-30T20:00:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4340",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4340#issuecomment-31771",
    "user": "https://github.com/craigcitro"
}
```

This code is a **massive** speedup over the old code, and is still not as fast as I'm planning on making it. Even in examples as small as `victor_miller_basis(300,100)`, this gives a factor of 900 speedup. It's also now faster than Magma.

I'm pretty sure I've got all the corner cases covered, too, but one can never be sure about these things ...



---

archive/issue_events_009816.json:
```json
{
    "actor": "https://github.com/craigcitro",
    "created_at": "2008-10-30T20:00:09Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4340",
    "milestone": "sage-3.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4340#event-9816"
}
```



---

archive/issue_comments_031772.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-10-30T20:00:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4340",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4340#issuecomment-31772",
    "user": "https://github.com/craigcitro"
}
```

Changing status from new to assigned.



---

archive/issue_comments_031773.json:
```json
{
    "body": "Looks good to me--I had to add a \"var\" argument to modform/eis_series.py though, does this depend on a patch somewhere. But after that it seems to work fine (and fast). \n\nAlso, \"F62\" threw me for a bit, perhaps \"F6sqare\" or something like that would be better?",
    "created_at": "2008-10-30T20:56:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4340",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4340#issuecomment-31773",
    "user": "https://github.com/robertwb"
}
```

Looks good to me--I had to add a "var" argument to modform/eis_series.py though, does this depend on a patch somewhere. But after that it seems to work fine (and fast). 

Also, "F62" threw me for a bit, perhaps "F6sqare" or something like that would be better?



---

archive/issue_comments_031774.json:
```json
{
    "body": "This extra argument to `eisenstein_series_qexp` was in #4359 ... \n\nYeah, I picked `F62` because it was `F_6^2` when I was writing it on paper ... should I add a comment in the code, or actually change the name?",
    "created_at": "2008-10-30T21:30:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4340",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4340#issuecomment-31774",
    "user": "https://github.com/craigcitro"
}
```

This extra argument to `eisenstein_series_qexp` was in #4359 ... 

Yeah, I picked `F62` because it was `F_6^2` when I was writing it on paper ... should I add a comment in the code, or actually change the name?



---

archive/issue_comments_031775.json:
```json
{
    "body": "OK, looks like #4359 got in, so that's good. \n\nI'd actually change the name of F62.",
    "created_at": "2008-10-30T21:36:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4340",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4340#issuecomment-31775",
    "user": "https://github.com/robertwb"
}
```

OK, looks like #4359 got in, so that's good. 

I'd actually change the name of F62.



---

archive/issue_comments_031776.json:
```json
{
    "body": "Attachment [trac-4340.patch](tarball://root/attachments/some-uuid/ticket4340/trac-4340.patch) by @craigcitro created at 2008-10-30 21:43:17\n\nNew patch with the name changed.",
    "created_at": "2008-10-30T21:43:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4340",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4340#issuecomment-31776",
    "user": "https://github.com/craigcitro"
}
```

Attachment [trac-4340.patch](tarball://root/attachments/some-uuid/ticket4340/trac-4340.patch) by @craigcitro created at 2008-10-30 21:43:17

New patch with the name changed.



---

archive/issue_comments_031777.json:
```json
{
    "body": "Positive review. Very nice work :).",
    "created_at": "2008-10-30T21:46:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4340",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4340#issuecomment-31777",
    "user": "https://github.com/robertwb"
}
```

Positive review. Very nice work :).



---

archive/issue_comments_031778.json:
```json
{
    "body": "Sorry, but\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n| Sage Version 3.2.alpha1, Release Date: 2008-10-26                  |\n| Type notebook() for the GUI, and license() for information.        |\nsage: f = ModularForms(1,4).0\nsage: time L = f.modform_lseries()\nWARNING: possible bug in q_expansion_basis for modular forms space Modular Forms space of dimension 1 for Congruence Subgroup Gamma0(1) of weight 4 over Rational Field\nWARNING: possible bug in q_expansion_basis for modular forms space Modular Forms space of dimension 1 for Congruence Subgroup Gamma0(1) of weight 4 over Rational Field\nWARNING: possible bug in q_expansion_basis for modular forms space Modular Forms space of dimension 1 for Congruence Subgroup Gamma0(1) of weight 4 over Rational Field\nWARNING: possible bug in q_expansion_basis for modular forms space Modular Forms space of dimension 1 for Congruence Subgroup Gamma0(1) of weight 4 over Rational Field\nWARNING: possible bug in q_expansion_basis for modular forms space Modular Forms space of dimension 1 for Congruence Subgroup Gamma0(1) of weight 4 over Rational Field\nWARNING: possible bug in q_expansion_basis for modular forms space Modular Forms space of dimension 1 for Congruence Subgroup Gamma0(1) of weight 4 over Rational Field\n<SNIP potentially infinite repetition - I killed the process after 20 minutes CPU time>\n```\nThis is on sage.math with my 3.2.alph2 merge tree. Other than the above problem all doctests passed.\n\nCheers,\n\nMichael",
    "created_at": "2008-10-31T01:03:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4340",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4340#issuecomment-31778",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Sorry, but

```
----------------------------------------------------------------------
----------------------------------------------------------------------
| Sage Version 3.2.alpha1, Release Date: 2008-10-26                  |
| Type notebook() for the GUI, and license() for information.        |
sage: f = ModularForms(1,4).0
sage: time L = f.modform_lseries()
WARNING: possible bug in q_expansion_basis for modular forms space Modular Forms space of dimension 1 for Congruence Subgroup Gamma0(1) of weight 4 over Rational Field
WARNING: possible bug in q_expansion_basis for modular forms space Modular Forms space of dimension 1 for Congruence Subgroup Gamma0(1) of weight 4 over Rational Field
WARNING: possible bug in q_expansion_basis for modular forms space Modular Forms space of dimension 1 for Congruence Subgroup Gamma0(1) of weight 4 over Rational Field
WARNING: possible bug in q_expansion_basis for modular forms space Modular Forms space of dimension 1 for Congruence Subgroup Gamma0(1) of weight 4 over Rational Field
WARNING: possible bug in q_expansion_basis for modular forms space Modular Forms space of dimension 1 for Congruence Subgroup Gamma0(1) of weight 4 over Rational Field
WARNING: possible bug in q_expansion_basis for modular forms space Modular Forms space of dimension 1 for Congruence Subgroup Gamma0(1) of weight 4 over Rational Field
<SNIP potentially infinite repetition - I killed the process after 20 minutes CPU time>
```
This is on sage.math with my 3.2.alph2 merge tree. Other than the above problem all doctests passed.

Cheers,

Michael



---

archive/issue_events_009817.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-10-31T01:03:30Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4340",
    "milestone": "sage-3.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4340#event-9817"
}
```



---

archive/issue_events_009818.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-10-31T01:03:30Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4340",
    "milestone": "sage-3.2.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4340#event-9818"
}
```



---

archive/issue_comments_031779.json:
```json
{
    "body": "Attachment [trac-4340-pt2.patch](tarball://root/attachments/some-uuid/ticket4340/trac-4340-pt2.patch) by @craigcitro created at 2008-10-31 03:23:44",
    "created_at": "2008-10-31T03:23:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4340",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4340#issuecomment-31779",
    "user": "https://github.com/craigcitro"
}
```

Attachment [trac-4340-pt2.patch](tarball://root/attachments/some-uuid/ticket4340/trac-4340-pt2.patch) by @craigcitro created at 2008-10-31 03:23:44



---

archive/issue_comments_031780.json:
```json
{
    "body": "Yep, I stupidly just ignored the `cusp_only` argument in the case where the space was one-dimensional. Attached patch fixes it.",
    "created_at": "2008-10-31T03:24:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4340",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4340#issuecomment-31780",
    "user": "https://github.com/craigcitro"
}
```

Yep, I stupidly just ignored the `cusp_only` argument in the case where the space was one-dimensional. Attached patch fixes it.



---

archive/issue_comments_031781.json:
```json
{
    "body": "The second patch fixes the doctest issue. Positive review, but I would be happy if an expert took another look.\n\nCheers,\n\nMichael",
    "created_at": "2008-10-31T03:51:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4340",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4340#issuecomment-31781",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The second patch fixes the doctest issue. Positive review, but I would be happy if an expert took another look.

Cheers,

Michael



---

archive/issue_events_009819.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-10-31T03:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4340",
    "milestone": "sage-3.2.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4340#event-9819"
}
```



---

archive/issue_events_009820.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-10-31T03:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4340",
    "milestone": "sage-3.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4340#event-9820"
}
```



---

archive/issue_comments_031782.json:
```json
{
    "body": "Merged both patches in Sage 3.2.alpha2",
    "created_at": "2008-10-31T03:53:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4340",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4340#issuecomment-31782",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged both patches in Sage 3.2.alpha2



---

archive/issue_events_009821.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-10-31T03:53:43Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4340",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4340#event-9821"
}
```



---

archive/issue_comments_031783.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-10-31T03:53:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4340",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4340#issuecomment-31783",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
