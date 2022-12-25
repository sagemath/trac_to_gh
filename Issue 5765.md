# Issue 5765: improve doctest coverage for schemes/generic/algebraic_scheme.py

archive/issues_005765.json:
```json
{
    "body": "Assignee: @aghitza\n\nKeywords: doctest algebraic scheme\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5765\n\n",
    "created_at": "2009-04-11T22:32:56Z",
    "labels": [
        "component: algebraic geometry",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.2",
    "title": "improve doctest coverage for schemes/generic/algebraic_scheme.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5765",
    "user": "https://github.com/aghitza"
}
```
Assignee: @aghitza

Keywords: doctest algebraic scheme



Issue created by migration from https://trac.sagemath.org/ticket/5765





---

archive/issue_comments_044975.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-04-11T22:33:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5765#issuecomment-44975",
    "user": "https://github.com/aghitza"
}
```

Changing status from new to assigned.



---

archive/issue_comments_044976.json:
```json
{
    "body": "Alex, is there a patch coming here? :)\n\nCheers,\n\nMichael",
    "created_at": "2009-04-15T06:44:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5765#issuecomment-44976",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Alex, is there a patch coming here? :)

Cheers,

Michael



---

archive/issue_comments_044977.json:
```json
{
    "body": "Good question.  I have done almost all I wanted to do with it, but unfortunately it's all mixed up with another patch that already got merged.  It will take me a bit of time to disentangle it, though.  Don't wait on it, although I'll do my best to get it done soon.",
    "created_at": "2009-04-15T06:53:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5765#issuecomment-44977",
    "user": "https://github.com/aghitza"
}
```

Good question.  I have done almost all I wanted to do with it, but unfortunately it's all mixed up with another patch that already got merged.  It will take me a bit of time to disentangle it, though.  Don't wait on it, although I'll do my best to get it done soon.



---

archive/issue_comments_044978.json:
```json
{
    "body": "Attachment [trac_5765.patch](tarball://root/attachments/some-uuid/ticket5765/trac_5765.patch) by @aghitza created at 2009-04-17 09:00:47\n\nThe attached patch brings up the doctest coverage from 24% to 87% (29 of 33).\n\nThere is also some fairly straightforward refactoring of code, e.g. moving `_validate` to the ambient spaces where it belongs logically.  I also realised that `self.complement(other)` is counterintuitive and changed it to match normal speech patterns: it should be \"the complement of self in other\", which is other-self, not self-other.  An added bonus is that now one can write `X.complement()` to get the complement of X in its ambient space, which is highly intuitive.  Normally such a change in behaviour would be tricky but since the functions were just broken until 3.4.1.rc3, this shouldn't lead to any confusion (since nobody has used them yet).\n\nNote that the patch relies on changes that only went in at 3.4.1.rc3, so it should only be applied on top of 3.4.1.rc3.",
    "created_at": "2009-04-17T09:00:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5765#issuecomment-44978",
    "user": "https://github.com/aghitza"
}
```

Attachment [trac_5765.patch](tarball://root/attachments/some-uuid/ticket5765/trac_5765.patch) by @aghitza created at 2009-04-17 09:00:47

The attached patch brings up the doctest coverage from 24% to 87% (29 of 33).

There is also some fairly straightforward refactoring of code, e.g. moving `_validate` to the ambient spaces where it belongs logically.  I also realised that `self.complement(other)` is counterintuitive and changed it to match normal speech patterns: it should be "the complement of self in other", which is other-self, not self-other.  An added bonus is that now one can write `X.complement()` to get the complement of X in its ambient space, which is highly intuitive.  Normally such a change in behaviour would be tricky but since the functions were just broken until 3.4.1.rc3, this shouldn't lead to any confusion (since nobody has used them yet).

Note that the patch relies on changes that only went in at 3.4.1.rc3, so it should only be applied on top of 3.4.1.rc3.



---

archive/issue_comments_044979.json:
```json
{
    "body": "Patch applies fine and looks good.  All doctests in schemes/generic pass.  Reference manual docs build ok and look good.  Pass!",
    "created_at": "2009-04-18T15:52:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5765#issuecomment-44979",
    "user": "https://github.com/JohnCremona"
}
```

Patch applies fine and looks good.  All doctests in schemes/generic pass.  Reference manual docs build ok and look good.  Pass!



---

archive/issue_comments_044980.json:
```json
{
    "body": "There are some doctest failures against 3.4.1:\n\n```\n        sage -t  devel/sage/sage/schemes/elliptic_curves/ell_point.py # 2 doctests failed\n        sage -t  devel/sage/sage/schemes/elliptic_curves/sha_tate.py # 0 doctests failed\n        sage -t  devel/sage/sage/schemes/elliptic_curves/ell_generic.py # 3 doctests failed\n        sage -t  devel/sage/sage/schemes/plane_curves/constructor.py # 1 doctests failed\n        sage -t  devel/sage/sage/schemes/elliptic_curves/ell_field.py # 1 doctests failed\n```\n\nCheers,\n\nMichael",
    "created_at": "2009-04-23T06:41:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5765#issuecomment-44980",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

There are some doctest failures against 3.4.1:

```
        sage -t  devel/sage/sage/schemes/elliptic_curves/ell_point.py # 2 doctests failed
        sage -t  devel/sage/sage/schemes/elliptic_curves/sha_tate.py # 0 doctests failed
        sage -t  devel/sage/sage/schemes/elliptic_curves/ell_generic.py # 3 doctests failed
        sage -t  devel/sage/sage/schemes/plane_curves/constructor.py # 1 doctests failed
        sage -t  devel/sage/sage/schemes/elliptic_curves/ell_field.py # 1 doctests failed
```

Cheers,

Michael



---

archive/issue_comments_044981.json:
```json
{
    "body": "Replying to [comment:6 mabshoff]:\n> There are some doctest failures against 3.4.1:\n> \n> ```\n>         sage -t  devel/sage/sage/schemes/elliptic_curves/ell_point.py # 2 doctests failed\n>         sage -t  devel/sage/sage/schemes/elliptic_curves/sha_tate.py # 0 doctests failed\n>         sage -t  devel/sage/sage/schemes/elliptic_curves/ell_generic.py # 3 doctests failed\n>         sage -t  devel/sage/sage/schemes/plane_curves/constructor.py # 1 doctests failed\n>         sage -t  devel/sage/sage/schemes/elliptic_curves/ell_field.py # 1 doctests failed\n> ```\n> \n> Cheers,\n> \n> Michael\n\n\nThose failures are in files where I changed the docstrings recently, so I'll take a look.  John",
    "created_at": "2009-04-23T08:36:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5765#issuecomment-44981",
    "user": "https://github.com/JohnCremona"
}
```

Replying to [comment:6 mabshoff]:
> There are some doctest failures against 3.4.1:
> 
> ```
>         sage -t  devel/sage/sage/schemes/elliptic_curves/ell_point.py # 2 doctests failed
>         sage -t  devel/sage/sage/schemes/elliptic_curves/sha_tate.py # 0 doctests failed
>         sage -t  devel/sage/sage/schemes/elliptic_curves/ell_generic.py # 3 doctests failed
>         sage -t  devel/sage/sage/schemes/plane_curves/constructor.py # 1 doctests failed
>         sage -t  devel/sage/sage/schemes/elliptic_curves/ell_field.py # 1 doctests failed
> ```
> 
> Cheers,
> 
> Michael


Those failures are in files where I changed the docstrings recently, so I'll take a look.  John



---

archive/issue_comments_044982.json:
```json
{
    "body": "Attachment [trac_5765-1.patch](tarball://root/attachments/some-uuid/ticket5765/trac_5765-1.patch) by @JohnCremona created at 2009-04-23 09:38:20\n\nReplaces earlier patch",
    "created_at": "2009-04-23T09:38:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5765#issuecomment-44982",
    "user": "https://github.com/JohnCremona"
}
```

Attachment [trac_5765-1.patch](tarball://root/attachments/some-uuid/ticket5765/trac_5765-1.patch) by @JohnCremona created at 2009-04-23 09:38:20

Replaces earlier patch



---

archive/issue_comments_044983.json:
```json
{
    "body": "The new patch replaces the first one and deals with this.  (Sorry, I forgot to do \"sage -hg qnew\" so it is not a separate patch,\n\nThe problem was:  in ell_field.py the function  _check_satisfies_equations called _error_bad_coords which Alex had renamed.  But all it did was riase an error with an appropriate message, so I just raised the error in place.\n\nOne remaining question: why is the error raised a TypeError?  In my view the type is fine but the values are wrong if the coordinates do not satisfy the equation.  I would have made it a ValueError.  but for consistence with the general scheme functions I left it as a TypeError.\n\nI put this back to \"needs review\" but if Michael is happy with test passing there's no more needed.\n\nJohn",
    "created_at": "2009-04-23T09:42:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5765#issuecomment-44983",
    "user": "https://github.com/JohnCremona"
}
```

The new patch replaces the first one and deals with this.  (Sorry, I forgot to do "sage -hg qnew" so it is not a separate patch,

The problem was:  in ell_field.py the function  _check_satisfies_equations called _error_bad_coords which Alex had renamed.  But all it did was riase an error with an appropriate message, so I just raised the error in place.

One remaining question: why is the error raised a TypeError?  In my view the type is fine but the values are wrong if the coordinates do not satisfy the equation.  I would have made it a ValueError.  but for consistence with the general scheme functions I left it as a TypeError.

I put this back to "needs review" but if Michael is happy with test passing there's no more needed.

John



---

archive/issue_comments_044984.json:
```json
{
    "body": "John's changes look good and fix most of the broken doctests.\n\nThere was one left, in `schemes/plane_curves/constructor.py`.  The fix is trivial and in the new patch `trac_5765-2.patch`, which should be applied after `trac_5765-1.patch`.",
    "created_at": "2009-04-23T13:10:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5765#issuecomment-44984",
    "user": "https://github.com/aghitza"
}
```

John's changes look good and fix most of the broken doctests.

There was one left, in `schemes/plane_curves/constructor.py`.  The fix is trivial and in the new patch `trac_5765-2.patch`, which should be applied after `trac_5765-1.patch`.



---

archive/issue_events_013516.json:
```json
{
    "actor": "https://github.com/aghitza",
    "created_at": "2009-04-23T13:10:19Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5765",
    "milestone": "sage-3.4.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5765#event-13516"
}
```



---

archive/issue_comments_044985.json:
```json
{
    "body": "Attachment [trac_5765-2.patch](tarball://root/attachments/some-uuid/ticket5765/trac_5765-2.patch) by @aghitza created at 2009-04-23 13:10:52\n\napply after trac_5765-1.patch",
    "created_at": "2009-04-23T13:10:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5765#issuecomment-44985",
    "user": "https://github.com/aghitza"
}
```

Attachment [trac_5765-2.patch](tarball://root/attachments/some-uuid/ticket5765/trac_5765-2.patch) by @aghitza created at 2009-04-23 13:10:52

apply after trac_5765-1.patch



---

archive/issue_comments_044986.json:
```json
{
    "body": "Replying to [comment:9 AlexGhitza]:\n> John's changes look good and fix most of the broken doctests.\n> \n> There was one left, in `schemes/plane_curves/constructor.py`.  The fix is trivial and in the new patch `trac_5765-2.patch`, which should be applied after `trac_5765-1.patch`.\n\n\nSorry I missed that one!",
    "created_at": "2009-04-23T15:22:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5765#issuecomment-44986",
    "user": "https://github.com/JohnCremona"
}
```

Replying to [comment:9 AlexGhitza]:
> John's changes look good and fix most of the broken doctests.
> 
> There was one left, in `schemes/plane_curves/constructor.py`.  The fix is trivial and in the new patch `trac_5765-2.patch`, which should be applied after `trac_5765-1.patch`.


Sorry I missed that one!



---

archive/issue_comments_044987.json:
```json
{
    "body": "Ahh, this now collides with #5851 it seems:\n\n```\nsage-3.4.2.alpha0/devel/sage$ patch -p1 --dry-run < trac_5765-1.patch \npatching file sage/schemes/elliptic_curves/ell_field.py\nHunk #1 FAILED at 27.\n1 out of 1 hunk FAILED -- saving rejects to file sage/schemes/elliptic_curves/ell_field.py.rej\npatching file sage/schemes/elliptic_curves/ell_generic.py\npatching file sage/schemes/elliptic_curves/ell_point.py\npatching file sage/schemes/generic/affine_space.py\npatching file sage/schemes/generic/algebraic_scheme.py\npatching file sage/schemes/generic/projective_space.py\npatching file sage/schemes/generic/scheme.py\n```\nI will see if I can resolve the problem myself.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-24T02:35:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5765#issuecomment-44987",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Ahh, this now collides with #5851 it seems:

```
sage-3.4.2.alpha0/devel/sage$ patch -p1 --dry-run < trac_5765-1.patch 
patching file sage/schemes/elliptic_curves/ell_field.py
Hunk #1 FAILED at 27.
1 out of 1 hunk FAILED -- saving rejects to file sage/schemes/elliptic_curves/ell_field.py.rej
patching file sage/schemes/elliptic_curves/ell_generic.py
patching file sage/schemes/elliptic_curves/ell_point.py
patching file sage/schemes/generic/affine_space.py
patching file sage/schemes/generic/algebraic_scheme.py
patching file sage/schemes/generic/projective_space.py
patching file sage/schemes/generic/scheme.py
```
I will see if I can resolve the problem myself.

Cheers,

Michael



---

archive/issue_comments_044988.json:
```json
{
    "body": "Ok, looking at the changes I think either John or Alex will rebase this - I am on to other merges for now. So \"needs rebase\".\n\nCheers,\n\nMichael",
    "created_at": "2009-04-24T02:38:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5765#issuecomment-44988",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Ok, looking at the changes I think either John or Alex will rebase this - I am on to other merges for now. So "needs rebase".

Cheers,

Michael



---

archive/issue_comments_044989.json:
```json
{
    "body": "I'll do this in a few hours.",
    "created_at": "2009-04-24T04:44:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5765#issuecomment-44989",
    "user": "https://github.com/aghitza"
}
```

I'll do this in a few hours.



---

archive/issue_comments_044990.json:
```json
{
    "body": "I was working on rebasing the patch against 3.4.2.alpha0, when I realised that `ell_field.py` has no reason to implement `_check_satisfies_equations`, since I have fixed the corresponding function \"upstream\" in `algebraic_scheme.py`.  In other words, the inherited method now works as it should so there's no need to reimplement it for elliptic curves.\n\nOf course, once you remove `_check_satisfies_equations` from `ell_field.py`, there's nothing left.  I think we just just get rid of this file and make classes that currently inherit from `EllipticCurve_field` inherit directly from `EllipticCurve_generic` instead.\n\nThe newly attached patch `trac_5765-rebased.patch` implements all this, and is based on 3.4.2.alpha0.  Doctests pass for me, but this is a significant change so I'd like John to review this so he can object if need be.",
    "created_at": "2009-04-24T13:02:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5765#issuecomment-44990",
    "user": "https://github.com/aghitza"
}
```

I was working on rebasing the patch against 3.4.2.alpha0, when I realised that `ell_field.py` has no reason to implement `_check_satisfies_equations`, since I have fixed the corresponding function "upstream" in `algebraic_scheme.py`.  In other words, the inherited method now works as it should so there's no need to reimplement it for elliptic curves.

Of course, once you remove `_check_satisfies_equations` from `ell_field.py`, there's nothing left.  I think we just just get rid of this file and make classes that currently inherit from `EllipticCurve_field` inherit directly from `EllipticCurve_generic` instead.

The newly attached patch `trac_5765-rebased.patch` implements all this, and is based on 3.4.2.alpha0.  Doctests pass for me, but this is a significant change so I'd like John to review this so he can object if need be.



---

archive/issue_comments_044991.json:
```json
{
    "body": "While I am waiting for 3.4.2.alpha0 to build (before which I cannot test the new patch!) I want to raise an issue.\n\nI agree that the one and only function in ell_field was redundant, since the general machinery for checking that a point lies on a scheme can do what it does.  So I am happy with that.\n\nBut do we really want to eliminate the *class* EllipticCurve_field?    The design seems to be as follows.  In principle one can define elliptic curves over general base schemes.  The most important special case is elliptic curves over a field.  At the moment Sage has essentially no support for an elliptic curve over a non-field, but that might change.  So at present,  all the generic stuff in ell_generic is quite likely to only work for curves over fields anyway, and that is where anything relevant to general fields is put.  Might it not be a better plan to look carefully through ell_generic, see if there is anything there which should really only be for curves over fields, and move that to ell_field (keeping the EllipticCurve_field class)?\n\nJust a thought -- at least a move such as the one this patch does deserves a little more public debate ;)",
    "created_at": "2009-04-24T13:28:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5765#issuecomment-44991",
    "user": "https://github.com/JohnCremona"
}
```

While I am waiting for 3.4.2.alpha0 to build (before which I cannot test the new patch!) I want to raise an issue.

I agree that the one and only function in ell_field was redundant, since the general machinery for checking that a point lies on a scheme can do what it does.  So I am happy with that.

But do we really want to eliminate the *class* EllipticCurve_field?    The design seems to be as follows.  In principle one can define elliptic curves over general base schemes.  The most important special case is elliptic curves over a field.  At the moment Sage has essentially no support for an elliptic curve over a non-field, but that might change.  So at present,  all the generic stuff in ell_generic is quite likely to only work for curves over fields anyway, and that is where anything relevant to general fields is put.  Might it not be a better plan to look carefully through ell_generic, see if there is anything there which should really only be for curves over fields, and move that to ell_field (keeping the EllipticCurve_field class)?

Just a thought -- at least a move such as the one this patch does deserves a little more public debate ;)



---

archive/issue_comments_044992.json:
```json
{
    "body": "Replying to [comment:15 cremona]:\n> While I am waiting for 3.4.2.alpha0 to build (before which I cannot test the new patch!) I want to raise an issue.\n> \n> I agree that the one and only function in ell_field was redundant, since the general machinery for checking that a point lies on a scheme can do what it does.  So I am happy with that.\n> \n> But do we really want to eliminate the *class* EllipticCurve_field?    The design seems to be as follows.  In principle one can define elliptic curves over general base schemes.  The most important special case is elliptic curves over a field.  At the moment Sage has essentially no support for an elliptic curve over a non-field, but that might change.  So at present,  all the generic stuff in ell_generic is quite likely to only work for curves over fields anyway, and that is where anything relevant to general fields is put.  Might it not be a better plan to look carefully through ell_generic, see if there is anything there which should really only be for curves over fields, and move that to ell_field (keeping the EllipticCurve_field class)?\n> \n> Just a thought -- at least a move such as the one this patch does deserves a little more public debate ;)\n\n\nVery good, that's why I wanted to hear others say something about it.\n\nI don't feel strongly either way.  From what I can see, `EllipticCurve_generic` has stuff that makes sense for elliptic curves over rings.  I agree that it would be good to sift through that and see if there are methods that really only work over fields, and move these to `ell_field.py`.\n\nIn the meantime, I'll modify the patch so that it just removes `_check_satisfies_equations` and leaves only `pass` in the definition of the class `EllipticCurve_field`.\n\nI really need sleep now, but I'll have a corrected patch up in the morning.",
    "created_at": "2009-04-24T13:40:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5765#issuecomment-44992",
    "user": "https://github.com/aghitza"
}
```

Replying to [comment:15 cremona]:
> While I am waiting for 3.4.2.alpha0 to build (before which I cannot test the new patch!) I want to raise an issue.
> 
> I agree that the one and only function in ell_field was redundant, since the general machinery for checking that a point lies on a scheme can do what it does.  So I am happy with that.
> 
> But do we really want to eliminate the *class* EllipticCurve_field?    The design seems to be as follows.  In principle one can define elliptic curves over general base schemes.  The most important special case is elliptic curves over a field.  At the moment Sage has essentially no support for an elliptic curve over a non-field, but that might change.  So at present,  all the generic stuff in ell_generic is quite likely to only work for curves over fields anyway, and that is where anything relevant to general fields is put.  Might it not be a better plan to look carefully through ell_generic, see if there is anything there which should really only be for curves over fields, and move that to ell_field (keeping the EllipticCurve_field class)?
> 
> Just a thought -- at least a move such as the one this patch does deserves a little more public debate ;)


Very good, that's why I wanted to hear others say something about it.

I don't feel strongly either way.  From what I can see, `EllipticCurve_generic` has stuff that makes sense for elliptic curves over rings.  I agree that it would be good to sift through that and see if there are methods that really only work over fields, and move these to `ell_field.py`.

In the meantime, I'll modify the patch so that it just removes `_check_satisfies_equations` and leaves only `pass` in the definition of the class `EllipticCurve_field`.

I really need sleep now, but I'll have a corrected patch up in the morning.



---

archive/issue_comments_044993.json:
```json
{
    "body": "I think it would be nice to be able to implement the elliptic curve factorization method (ECM) without having to use this hack:\n\n```\nR = Zmod(N)\nR.is_field = lambda: True\nE = EllipticCurve(R, [-1,0])\n```",
    "created_at": "2009-04-24T15:55:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5765#issuecomment-44993",
    "user": "https://github.com/williamstein"
}
```

I think it would be nice to be able to implement the elliptic curve factorization method (ECM) without having to use this hack:

```
R = Zmod(N)
R.is_field = lambda: True
E = EllipticCurve(R, [-1,0])
```



---

archive/issue_comments_044994.json:
```json
{
    "body": "Attachment [trac_5765-rebased.patch](tarball://root/attachments/some-uuid/ticket5765/trac_5765-rebased.patch) by @aghitza created at 2009-04-24 23:09:45",
    "created_at": "2009-04-24T23:09:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5765#issuecomment-44994",
    "user": "https://github.com/aghitza"
}
```

Attachment [trac_5765-rebased.patch](tarball://root/attachments/some-uuid/ticket5765/trac_5765-rebased.patch) by @aghitza created at 2009-04-24 23:09:45



---

archive/issue_comments_044995.json:
```json
{
    "body": "OK, I replaced the controversial version of the patch with the tame one.  It is just a rebase of the original positive-reviewed patch, together with the removal of the redundant method `_check_satisfies_equations`, but leaving a blank `ell_field.py` for further refactoring as discussed above.\n\nI'm not sure whether this needs a review any more, but if John's around and can have a quick peak, that wouldn't hurt.  (Note that the changes to the elliptic curves code are all at the top of the patch.)",
    "created_at": "2009-04-24T23:13:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5765#issuecomment-44995",
    "user": "https://github.com/aghitza"
}
```

OK, I replaced the controversial version of the patch with the tame one.  It is just a rebase of the original positive-reviewed patch, together with the removal of the redundant method `_check_satisfies_equations`, but leaving a blank `ell_field.py` for further refactoring as discussed above.

I'm not sure whether this needs a review any more, but if John's around and can have a quick peak, that wouldn't hurt.  (Note that the changes to the elliptic curves code are all at the top of the patch.)



---

archive/issue_comments_044996.json:
```json
{
    "body": "There's a followup ticket at #5890.",
    "created_at": "2009-04-24T23:44:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5765#issuecomment-44996",
    "user": "https://github.com/aghitza"
}
```

There's a followup ticket at #5890.



---

archive/issue_comments_044997.json:
```json
{
    "body": "The patch applies but tests in ell_point.py fila revealing this horror:\n\n```\nsage: Fx.<b>=GF(2^(4*5))\nsage: Ex=EllipticCurve(Fx,[0,0,1,1,1])\nsage: Ex.defining_polynomial()\nx^3 + y^2*z + 0*x*z^2 + 0*y*z^2 + 0*z^3\n```\n-- note the zero coefficients!\n\nAdding a whole lot of print statements I get to this:\n\n```\nsage: Ex=EllipticCurve(Fx,[0,0,1,1,1])\nK =  Finite Field in b of size 2^20\nPP =  Projective Space of dimension 2 over Finite Field in b of size 2^20\nPP.coordinate_ring() =  Multivariate Polynomial Ring in x, y, z over Finite Field in b of size 2^20\nPP.coordinate_ring().base_ring() =  Finite Field in b of size 2^20\nPP.coordinate_ring()(1) =  1\nainvs =  [0, 0, 1, 1, 1]\na1, a2, a3, a4, a6 =  0 0 1 1 1\na4*x*z**2 =  0*x*z^2\na4's parent =  Finite Field in b of size 2^20\n f =  x^3 + y^2*z + 0*x*z^2 + 0*y*z^2 + 0*z^3\n```\nAt which point I am stuck.  We have the constant 1 in the multivariate poly ring in x,y,z over the field GF(2^20), but when I multiply a monomial by it it displays with coefficient zero.\n\nThis has surely been caused by something not in this patch!  I tried constructing an example outside this bit of code but failed (to make it fail in this way).  In fact this happens in unpatched 3.4.2.alpha0:\n\n```\nsage: Fx.<b>=GF(2^(4*5))\nsage: Ex=EllipticCurve(Fx,[0,0,1,1,1])\nsage: Ex.defining_polynomial()\nx^3 + y^2*z + 0*x*z^2 + 0*y*z^2 + 0*z^3\n```",
    "created_at": "2009-04-27T11:16:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5765#issuecomment-44997",
    "user": "https://github.com/JohnCremona"
}
```

The patch applies but tests in ell_point.py fila revealing this horror:

```
sage: Fx.<b>=GF(2^(4*5))
sage: Ex=EllipticCurve(Fx,[0,0,1,1,1])
sage: Ex.defining_polynomial()
x^3 + y^2*z + 0*x*z^2 + 0*y*z^2 + 0*z^3
```
-- note the zero coefficients!

Adding a whole lot of print statements I get to this:

```
sage: Ex=EllipticCurve(Fx,[0,0,1,1,1])
K =  Finite Field in b of size 2^20
PP =  Projective Space of dimension 2 over Finite Field in b of size 2^20
PP.coordinate_ring() =  Multivariate Polynomial Ring in x, y, z over Finite Field in b of size 2^20
PP.coordinate_ring().base_ring() =  Finite Field in b of size 2^20
PP.coordinate_ring()(1) =  1
ainvs =  [0, 0, 1, 1, 1]
a1, a2, a3, a4, a6 =  0 0 1 1 1
a4*x*z**2 =  0*x*z^2
a4's parent =  Finite Field in b of size 2^20
 f =  x^3 + y^2*z + 0*x*z^2 + 0*y*z^2 + 0*z^3
```
At which point I am stuck.  We have the constant 1 in the multivariate poly ring in x,y,z over the field GF(2^20), but when I multiply a monomial by it it displays with coefficient zero.

This has surely been caused by something not in this patch!  I tried constructing an example outside this bit of code but failed (to make it fail in this way).  In fact this happens in unpatched 3.4.2.alpha0:

```
sage: Fx.<b>=GF(2^(4*5))
sage: Ex=EllipticCurve(Fx,[0,0,1,1,1])
sage: Ex.defining_polynomial()
x^3 + y^2*z + 0*x*z^2 + 0*y*z^2 + 0*z^3
```



---

archive/issue_comments_044998.json:
```json
{
    "body": "After applying also the patch at #5919, all tests in sage/schemes pass, so I am changing this to \"positive review\" but note that it does depend on that patch for the tests in ell_point.py to pass.  \n\nThe patches (here and at #5919) can be merged in either order.",
    "created_at": "2009-04-28T15:52:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5765#issuecomment-44998",
    "user": "https://github.com/JohnCremona"
}
```

After applying also the patch at #5919, all tests in sage/schemes pass, so I am changing this to "positive review" but note that it does depend on that patch for the tests in ell_point.py to pass.  

The patches (here and at #5919) can be merged in either order.



---

archive/issue_events_013517.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-04-29T23:17:43Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5765",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5765#event-13517"
}
```



---

archive/issue_comments_044999.json:
```json
{
    "body": "Merged trac_5765-rebased.patch in Sage 3.4.2.rc0.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-29T23:17:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5765#issuecomment-44999",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged trac_5765-rebased.patch in Sage 3.4.2.rc0.

Cheers,

Michael



---

archive/issue_comments_045000.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-29T23:17:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5765#issuecomment-45000",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
