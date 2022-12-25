# Issue 5890: [with patch, woth positive review] clean up schemes/elliptic_curves/ell_generic.py

archive/issues_005890.json:
```json
{
    "body": "Assignee: @aghitza\n\nCC:  @williamstein @JohnCremona\n\nKeywords: elliptic curve field\n\nAs noted at #5765, `ell_generic.py` has some functions that do not make sense over a general ring and should rather be moved down to `ell_field.py` or one of its descendants.\n\nNote also William's comment from #5765: I think it would be nice to be able to implement the elliptic curve factorization method (ECM) without having to use this hack:\n\n```\nR = Zmod(N)\nR.is_field = lambda: True\nE = EllipticCurve(R, [-1,0])\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5890\n\n",
    "closed_at": "2009-04-30T00:54:18Z",
    "created_at": "2009-04-24T23:43:37Z",
    "labels": [
        "component: number theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.2",
    "title": "[with patch, woth positive review] clean up schemes/elliptic_curves/ell_generic.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5890",
    "user": "https://github.com/aghitza"
}
```
Assignee: @aghitza

CC:  @williamstein @JohnCremona

Keywords: elliptic curve field

As noted at #5765, `ell_generic.py` has some functions that do not make sense over a general ring and should rather be moved down to `ell_field.py` or one of its descendants.

Note also William's comment from #5765: I think it would be nice to be able to implement the elliptic curve factorization method (ECM) without having to use this hack:

```
R = Zmod(N)
R.is_field = lambda: True
E = EllipticCurve(R, [-1,0])
```


Issue created by migration from https://trac.sagemath.org/ticket/5890





---

archive/issue_comments_046481.json:
```json
{
    "body": "For the record, to understand William's comment have a look at line 572 of `tests/book_stein_ent.py`, where he implements ECM and uses this hack.\n\nHowever, his function works for me in 3.4.1, so I think it's already been fixed.",
    "created_at": "2009-04-25T05:07:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5890",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5890#issuecomment-46481",
    "user": "https://github.com/aghitza"
}
```

For the record, to understand William's comment have a look at line 572 of `tests/book_stein_ent.py`, where he implements ECM and uses this hack.

However, his function works for me in 3.4.1, so I think it's already been fixed.



---

archive/issue_comments_046482.json:
```json
{
    "body": "Replying to [comment:1 AlexGhitza]:\n> For the record, to understand William's comment have a look at line 572 of `tests/book_stein_ent.py`, where he implements ECM and uses this hack.\n> \n> However, his function works for me in 3.4.1, so I think it's already been fixed.\n> \n\n I mean of course that it works for me in 3.4.1 without the hackish line that fools Sage into thinking that R is a field.",
    "created_at": "2009-04-25T05:08:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5890",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5890#issuecomment-46482",
    "user": "https://github.com/aghitza"
}
```

Replying to [comment:1 AlexGhitza]:
> For the record, to understand William's comment have a look at line 572 of `tests/book_stein_ent.py`, where he implements ECM and uses this hack.
> 
> However, his function works for me in 3.4.1, so I think it's already been fixed.
> 

 I mean of course that it works for me in 3.4.1 without the hackish line that fools Sage into thinking that R is a field.



---

archive/issue_comments_046483.json:
```json
{
    "body": "The attached patch does some cleaning up, and it depends on #5765.\n\nIt moves all the twists-related methods from `ell_generic.py` to `ell_field.py`, as well as the alias `base_field = base_ring`.\n\nIt also makes `change_ring` into an alias for `base_extend`, since the two have the exact same functionality and equivalent code.\n\nLastly, the standalone function `Hasse_bounds` is moved from `ell_generic.py` to `schemes/plane_curves/projective_curve.py`, which is a more natural place for it.\n\nThere are more things to do, but they are issues with the generic code for curves rather than the code for elliptic curves, so I think they should be fixed in `schemes/plane_curves` instead.  I'll be looking into that soon.",
    "created_at": "2009-04-25T05:15:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5890",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5890#issuecomment-46483",
    "user": "https://github.com/aghitza"
}
```

The attached patch does some cleaning up, and it depends on #5765.

It moves all the twists-related methods from `ell_generic.py` to `ell_field.py`, as well as the alias `base_field = base_ring`.

It also makes `change_ring` into an alias for `base_extend`, since the two have the exact same functionality and equivalent code.

Lastly, the standalone function `Hasse_bounds` is moved from `ell_generic.py` to `schemes/plane_curves/projective_curve.py`, which is a more natural place for it.

There are more things to do, but they are issues with the generic code for curves rather than the code for elliptic curves, so I think they should be fixed in `schemes/plane_curves` instead.  I'll be looking into that soon.



---

archive/issue_comments_046484.json:
```json
{
    "body": "Changing assignee from @williamstein to @aghitza.",
    "created_at": "2009-04-25T05:15:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5890",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5890#issuecomment-46484",
    "user": "https://github.com/aghitza"
}
```

Changing assignee from @williamstein to @aghitza.



---

archive/issue_comments_046485.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-04-25T05:15:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5890",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5890#issuecomment-46485",
    "user": "https://github.com/aghitza"
}
```

Changing status from new to assigned.



---

archive/issue_comments_046486.json:
```json
{
    "body": "depends on the latest patch at #5765",
    "created_at": "2009-04-25T05:16:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5890",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5890#issuecomment-46486",
    "user": "https://github.com/aghitza"
}
```

depends on the latest patch at #5765



---

archive/issue_comments_046487.json:
```json
{
    "body": "Attachment [trac_5890.patch](tarball://root/attachments/some-uuid/ticket5890/trac_5890.patch) by @aghitza created at 2009-04-25 05:26:32",
    "created_at": "2009-04-25T05:26:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5890",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5890#issuecomment-46487",
    "user": "https://github.com/aghitza"
}
```

Attachment [trac_5890.patch](tarball://root/attachments/some-uuid/ticket5890/trac_5890.patch) by @aghitza created at 2009-04-25 05:26:32



---

archive/issue_comments_046488.json:
```json
{
    "body": "Review: first of all, this is just moving code around, all perfectly sensible (lots of stuff moved down from ell_generic to ell_field, and Hasse_bound function moved off to plane curves (where I should have put it in the first place).\n\nI applied first 12097.patch (from #5919) then trac_5765-rebased.patch (from #5765) and then trac_5890.patch (from here), all successfully.\n\nDoctests in schemes/plane_curves and schemes/elliptic_curves pass.  I will give this a positive review, despite the following, which will make it harder to do EC factoring (but the fault lies not in the patch here, rather in moving the test for a point lying on a curve which is now more sophisticated to harder to fool.... but that is not for this ticket to sort out.\n\nThe example\n\n```\nN = 1001\nR = Zmod(N)\nR.is_field = lambda: True\nE = EllipticCurve(R, [-1,0])\n```\nworks but you cannot construct a point in the curve (e.g. E(0,0)) since this happens:\n\n```\nsage: P = E(0,0)\n---------------------------------------------------------------------------\nNotImplementedError                       Traceback (most recent call last)\n\n/home/masgaj/.sage/temp/host_56_150/32116/_home_masgaj__sage_init_sage_0.py in <module>()\n\n/local/jec/sage-3.4.2.alpha0/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_generic.pyc in __call__(self, *args, **kwds)\n    609                 args = tuple(args[0])\n    610\n--> 611         return plane_curve.ProjectiveCurve_generic.__call__(self, *args, **kwds)\n    612\n    613     def _reduce_point(self, R, p):\n\n/local/jec/sage-3.4.2.alpha0/local/lib/python2.5/site-packages/sage/schemes/generic/scheme.pyc in __call__(self, *args)\n    196                 else:\n    197                     return self.point(S)\n--> 198         return self.point(args)\n    199\n    200     def point_homset(self, S = None):\n\n/local/jec/sage-3.4.2.alpha0/local/lib/python2.5/site-packages/sage/schemes/generic/scheme.pyc in point(self, v, check)\n    230\n    231     def point(self, v, check=True):\n--> 232         return self._point_class(self, v, check=check)\n    233\n    234     def _point_class(self):\n\n/local/jec/sage-3.4.2.alpha0/local/lib/python2.5/site-packages/sage/schemes/generic/morphism.pyc in __init__(self, X, v, check)\n    415     \"\"\"\n    416     def __init__(self, X, v, check=True):\n--> 417         raise NotImplementedError\n    418\n    419\n\nNotImplementedError:\n```",
    "created_at": "2009-04-29T11:39:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5890",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5890#issuecomment-46488",
    "user": "https://github.com/JohnCremona"
}
```

Review: first of all, this is just moving code around, all perfectly sensible (lots of stuff moved down from ell_generic to ell_field, and Hasse_bound function moved off to plane curves (where I should have put it in the first place).

I applied first 12097.patch (from #5919) then trac_5765-rebased.patch (from #5765) and then trac_5890.patch (from here), all successfully.

Doctests in schemes/plane_curves and schemes/elliptic_curves pass.  I will give this a positive review, despite the following, which will make it harder to do EC factoring (but the fault lies not in the patch here, rather in moving the test for a point lying on a curve which is now more sophisticated to harder to fool.... but that is not for this ticket to sort out.

The example

```
N = 1001
R = Zmod(N)
R.is_field = lambda: True
E = EllipticCurve(R, [-1,0])
```
works but you cannot construct a point in the curve (e.g. E(0,0)) since this happens:

```
sage: P = E(0,0)
---------------------------------------------------------------------------
NotImplementedError                       Traceback (most recent call last)

/home/masgaj/.sage/temp/host_56_150/32116/_home_masgaj__sage_init_sage_0.py in <module>()

/local/jec/sage-3.4.2.alpha0/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_generic.pyc in __call__(self, *args, **kwds)
    609                 args = tuple(args[0])
    610
--> 611         return plane_curve.ProjectiveCurve_generic.__call__(self, *args, **kwds)
    612
    613     def _reduce_point(self, R, p):

/local/jec/sage-3.4.2.alpha0/local/lib/python2.5/site-packages/sage/schemes/generic/scheme.pyc in __call__(self, *args)
    196                 else:
    197                     return self.point(S)
--> 198         return self.point(args)
    199
    200     def point_homset(self, S = None):

/local/jec/sage-3.4.2.alpha0/local/lib/python2.5/site-packages/sage/schemes/generic/scheme.pyc in point(self, v, check)
    230
    231     def point(self, v, check=True):
--> 232         return self._point_class(self, v, check=check)
    233
    234     def _point_class(self):

/local/jec/sage-3.4.2.alpha0/local/lib/python2.5/site-packages/sage/schemes/generic/morphism.pyc in __init__(self, X, v, check)
    415     """
    416     def __init__(self, X, v, check=True):
--> 417         raise NotImplementedError
    418
    419

NotImplementedError:
```



---

archive/issue_comments_046489.json:
```json
{
    "body": "Merged in Sage 3.4.2.rc0.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-30T00:54:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5890",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5890#issuecomment-46489",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.4.2.rc0.

Cheers,

Michael



---

archive/issue_events_013834.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-04-30T00:54:18Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5890",
    "milestone": "sage-3.4.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5890#event-13834"
}
```



---

archive/issue_events_013835.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-04-30T00:54:18Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5890",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5890#event-13835"
}
```



---

archive/issue_comments_046490.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-30T00:54:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5890",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5890#issuecomment-46490",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
