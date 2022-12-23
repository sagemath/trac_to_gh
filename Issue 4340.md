# Issue 4340: Speed up Victor Miller basis code

archive/issues_004340.json:
```json
{
    "body": "Assignee: craigcitro\n\nThe current Victor Miller basis code in Sage is painfully slow. \n\nI've already written much faster code, which I'll submit shortly.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4340\n\n",
    "created_at": "2008-10-22T18:16:47Z",
    "labels": [
        "modular forms",
        "major",
        "bug"
    ],
    "title": "Speed up Victor Miller basis code",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4340",
    "user": "craigcitro"
}
```
Assignee: craigcitro

The current Victor Miller basis code in Sage is painfully slow. 

I've already written much faster code, which I'll submit shortly.

Issue created by migration from https://trac.sagemath.org/ticket/4340





---

archive/issue_comments_031833.json:
```json
{
    "body": "This code is a **massive** speedup over the old code, and is still not as fast as I'm planning on making it. Even in examples as small as `victor_miller_basis(300,100)`, this gives a factor of 900 speedup. It's also now faster than Magma.\n\nI'm pretty sure I've got all the corner cases covered, too, but one can never be sure about these things ...",
    "created_at": "2008-10-30T20:00:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4340",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4340#issuecomment-31833",
    "user": "craigcitro"
}
```

This code is a **massive** speedup over the old code, and is still not as fast as I'm planning on making it. Even in examples as small as `victor_miller_basis(300,100)`, this gives a factor of 900 speedup. It's also now faster than Magma.

I'm pretty sure I've got all the corner cases covered, too, but one can never be sure about these things ...



---

archive/issue_comments_031834.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-10-30T20:00:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4340",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4340#issuecomment-31834",
    "user": "craigcitro"
}
```

Changing status from new to assigned.



---

archive/issue_comments_031835.json:
```json
{
    "body": "Looks good to me--I had to add a \"var\" argument to modform/eis_series.py though, does this depend on a patch somewhere. But after that it seems to work fine (and fast). \n\nAlso, \"F62\" threw me for a bit, perhaps \"F6sqare\" or something like that would be better?",
    "created_at": "2008-10-30T20:56:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4340",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4340#issuecomment-31835",
    "user": "robertwb"
}
```

Looks good to me--I had to add a "var" argument to modform/eis_series.py though, does this depend on a patch somewhere. But after that it seems to work fine (and fast). 

Also, "F62" threw me for a bit, perhaps "F6sqare" or something like that would be better?



---

archive/issue_comments_031836.json:
```json
{
    "body": "This extra argument to `eisenstein_series_qexp` was in #4359 ... \n\nYeah, I picked `F62` because it was `F_6^2` when I was writing it on paper ... should I add a comment in the code, or actually change the name?",
    "created_at": "2008-10-30T21:30:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4340",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4340#issuecomment-31836",
    "user": "craigcitro"
}
```

This extra argument to `eisenstein_series_qexp` was in #4359 ... 

Yeah, I picked `F62` because it was `F_6^2` when I was writing it on paper ... should I add a comment in the code, or actually change the name?



---

archive/issue_comments_031837.json:
```json
{
    "body": "OK, looks like #4359 got in, so that's good. \n\nI'd actually change the name of F62.",
    "created_at": "2008-10-30T21:36:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4340",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4340#issuecomment-31837",
    "user": "robertwb"
}
```

OK, looks like #4359 got in, so that's good. 

I'd actually change the name of F62.



---

archive/issue_comments_031838.json:
```json
{
    "body": "Attachment\n\nNew patch with the name changed.",
    "created_at": "2008-10-30T21:43:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4340",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4340#issuecomment-31838",
    "user": "craigcitro"
}
```

Attachment

New patch with the name changed.



---

archive/issue_comments_031839.json:
```json
{
    "body": "Positive review. Very nice work :).",
    "created_at": "2008-10-30T21:46:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4340",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4340#issuecomment-31839",
    "user": "robertwb"
}
```

Positive review. Very nice work :).



---

archive/issue_comments_031840.json:
```json
{
    "body": "Sorry, but\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n| Sage Version 3.2.alpha1, Release Date: 2008-10-26                  |\n| Type notebook() for the GUI, and license() for information.        |\nsage: f = ModularForms(1,4).0\nsage: time L = f.modform_lseries()\nWARNING: possible bug in q_expansion_basis for modular forms space Modular Forms space of dimension 1 for Congruence Subgroup Gamma0(1) of weight 4 over Rational Field\nWARNING: possible bug in q_expansion_basis for modular forms space Modular Forms space of dimension 1 for Congruence Subgroup Gamma0(1) of weight 4 over Rational Field\nWARNING: possible bug in q_expansion_basis for modular forms space Modular Forms space of dimension 1 for Congruence Subgroup Gamma0(1) of weight 4 over Rational Field\nWARNING: possible bug in q_expansion_basis for modular forms space Modular Forms space of dimension 1 for Congruence Subgroup Gamma0(1) of weight 4 over Rational Field\nWARNING: possible bug in q_expansion_basis for modular forms space Modular Forms space of dimension 1 for Congruence Subgroup Gamma0(1) of weight 4 over Rational Field\nWARNING: possible bug in q_expansion_basis for modular forms space Modular Forms space of dimension 1 for Congruence Subgroup Gamma0(1) of weight 4 over Rational Field\n<SNIP potentially infinite repetition - I killed the process after 20 minutes CPU time>\n```\n\nThis is on sage.math with my 3.2.alph2 merge tree. Other than the above problem all doctests passed.\n\nCheers,\n\nMichael",
    "created_at": "2008-10-31T01:03:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4340",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4340#issuecomment-31840",
    "user": "mabshoff"
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

archive/issue_comments_031841.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-10-31T03:23:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4340",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4340#issuecomment-31841",
    "user": "craigcitro"
}
```

Attachment



---

archive/issue_comments_031842.json:
```json
{
    "body": "Yep, I stupidly just ignored the `cusp_only` argument in the case where the space was one-dimensional. Attached patch fixes it.",
    "created_at": "2008-10-31T03:24:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4340",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4340#issuecomment-31842",
    "user": "craigcitro"
}
```

Yep, I stupidly just ignored the `cusp_only` argument in the case where the space was one-dimensional. Attached patch fixes it.



---

archive/issue_comments_031843.json:
```json
{
    "body": "The second patch fixes the doctest issue. Positive review, but I would be happy if an expert took another look.\n\nCheers,\n\nMichael",
    "created_at": "2008-10-31T03:51:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4340",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4340#issuecomment-31843",
    "user": "mabshoff"
}
```

The second patch fixes the doctest issue. Positive review, but I would be happy if an expert took another look.

Cheers,

Michael



---

archive/issue_comments_031844.json:
```json
{
    "body": "Merged both patches in Sage 3.2.alpha2",
    "created_at": "2008-10-31T03:53:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4340",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4340#issuecomment-31844",
    "user": "mabshoff"
}
```

Merged both patches in Sage 3.2.alpha2



---

archive/issue_comments_031845.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-10-31T03:53:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4340",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4340#issuecomment-31845",
    "user": "mabshoff"
}
```

Resolution: fixed
