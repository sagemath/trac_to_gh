# Issue 9235: Doctest coverage for sage.categories.homset

archive/issues_009235.json:
```json
{
    "body": "Assignee: nthiery\n\nCC:  niles\n\nKeywords: doctest coverage homset\n\nThe doctest coverage for sage.categories.homset was\n\n```\nSCORE devel/sage-main/sage/categories/homset.py: 52% (13 of 25)\n```\n\n\nMy patch covers all but two methods:\n\n* get_action_c\n* coerce_map_from_c\n\nThese two return (by default) None. Is there a good *indirect* doctest for these two? I am not familiar with `get_action`, and I don't know what `coerce_map_from_c` does, compared with `_coerce_map_from_`. Perhaps the reviewer can explain it to me, so that I or s/he can add the two missing tests?\n\nIssue created by migration from https://trac.sagemath.org/ticket/9235\n\n",
    "created_at": "2010-06-14T09:59:42Z",
    "labels": [
        "categories",
        "minor",
        "bug"
    ],
    "title": "Doctest coverage for sage.categories.homset",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9235",
    "user": "SimonKing"
}
```
Assignee: nthiery

CC:  niles

Keywords: doctest coverage homset

The doctest coverage for sage.categories.homset was

```
SCORE devel/sage-main/sage/categories/homset.py: 52% (13 of 25)
```


My patch covers all but two methods:

* get_action_c
* coerce_map_from_c

These two return (by default) None. Is there a good *indirect* doctest for these two? I am not familiar with `get_action`, and I don't know what `coerce_map_from_c` does, compared with `_coerce_map_from_`. Perhaps the reviewer can explain it to me, so that I or s/he can add the two missing tests?

Issue created by migration from https://trac.sagemath.org/ticket/9235





---

archive/issue_comments_086683.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-06-14T10:03:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9235",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9235#issuecomment-86683",
    "user": "SimonKing"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_086684.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-03-08T20:52:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9235",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9235#issuecomment-86684",
    "user": "SimonKing"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_086685.json:
```json
{
    "body": "I can not reproduce the error that the patchbot recently found. I don't know how I can push it to test the patch again.\n\nSo, I'll change into needs-work and then immediately into needs-review - hope that triggers another attempt of the bot...",
    "created_at": "2011-03-08T20:52:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9235",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9235#issuecomment-86685",
    "user": "SimonKing"
}
```

I can not reproduce the error that the patchbot recently found. I don't know how I can push it to test the patch again.

So, I'll change into needs-work and then immediately into needs-review - hope that triggers another attempt of the bot...



---

archive/issue_comments_086686.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-03-08T20:52:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9235",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9235#issuecomment-86686",
    "user": "SimonKing"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_086687.json:
```json
{
    "body": "It seems to me that the doctest error found by the patchbot is unrelated with my patch: After all, the patch is a just adding documentation and tests.\n\nIs anybody inclined to review it?",
    "created_at": "2011-04-09T07:12:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9235",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9235#issuecomment-86687",
    "user": "SimonKing"
}
```

It seems to me that the doctest error found by the patchbot is unrelated with my patch: After all, the patch is a just adding documentation and tests.

Is anybody inclined to review it?



---

archive/issue_comments_086688.json:
```json
{
    "body": "-- bump --\n\nThe patch is in need of a review since *one year*. I think it would not be difficult to review a pure doctest patch. But having full doctest coverage in yet another part of Sage would be good to have.\n\nI hope that the patch still applies.",
    "created_at": "2011-05-28T09:18:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9235",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9235#issuecomment-86688",
    "user": "SimonKing"
}
```

-- bump --

The patch is in need of a review since *one year*. I think it would not be difficult to review a pure doctest patch. But having full doctest coverage in yet another part of Sage would be good to have.

I hope that the patch still applies.



---

archive/issue_comments_086689.json:
```json
{
    "body": "deprecation warnings for get_action_c and coerce_map_from_c",
    "created_at": "2011-05-29T06:47:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9235",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9235#issuecomment-86689",
    "user": "niles"
}
```

deprecation warnings for get_action_c and coerce_map_from_c



---

archive/issue_comments_086690.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-05-29T06:59:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9235",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9235#issuecomment-86690",
    "user": "niles"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_086691.json:
```json
{
    "body": "Attachment\n\nYou're right -- this shouldn't have to wait so long!  I've looked through all the changes, and they look good!  All tests pass, and the documentation builds cleanly, without warnings.  \n\nI used `search_src` to look for other places in Sage where `get_action_c` and `coerce_map_from_c` are used.  The only places they appear are in `structure/parent_old`, so I think these in Homset should be deprecated and (later) removed.  I've added a reviewer patch which adds deprecation warnings and corresponding tests, raising the coverage to 100%.\n\nThe only issue I have with `9235_doctest_homset.patch` is the following block:\n\n\n```\n    if category is None:\n        if cat_X.is_subcategory(cat_Y):\n            category = cat_Y\n        elif cat_Y.is_subcategory(cat_X):\n            # NT: this \"category is None\" test is useless and could be removed\n            # SK: Indeed! For that reason, the ValueError would never be raised\n            # NT: why is there an assymmetry between X and Y?\n            # SK: I see no reason. In particular, I don't see why an error should\n            #     be raised if cat_X is not cat_Y. So, I uncomment the following\n            #     two lines.\n##             if not (category is None) and not (cat_X is cat_Y):\n##                 raise ValueError, \"No unambiguous category found for Hom from %s to %s.\"%(X,Y)\n            category = cat_X\n        else:\n            # Search for the lowest common super category\n            subcats_X = cat_X.all_super_categories(proper = True)\n            subcats_Y = set(cat_Y.all_super_categories(proper = True))\n            category = None\n            for c in subcats_X:\n                if c in subcats_Y:\n                    category = c\n                    break\n\n            if category is None:\n                raise TypeError, \"No suitable category found for Hom from %s to %s.\"%(X,Y)\n```\n\n\nIf there's no reason to include the second \"`category is None`\" test, then it and the previous comments should simply be deleted.  And there is a third \"`category is None`\" test in this block which also looks redundant.",
    "created_at": "2011-05-29T06:59:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9235",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9235#issuecomment-86691",
    "user": "niles"
}
```

Attachment

You're right -- this shouldn't have to wait so long!  I've looked through all the changes, and they look good!  All tests pass, and the documentation builds cleanly, without warnings.  

I used `search_src` to look for other places in Sage where `get_action_c` and `coerce_map_from_c` are used.  The only places they appear are in `structure/parent_old`, so I think these in Homset should be deprecated and (later) removed.  I've added a reviewer patch which adds deprecation warnings and corresponding tests, raising the coverage to 100%.

The only issue I have with `9235_doctest_homset.patch` is the following block:


```
    if category is None:
        if cat_X.is_subcategory(cat_Y):
            category = cat_Y
        elif cat_Y.is_subcategory(cat_X):
            # NT: this "category is None" test is useless and could be removed
            # SK: Indeed! For that reason, the ValueError would never be raised
            # NT: why is there an assymmetry between X and Y?
            # SK: I see no reason. In particular, I don't see why an error should
            #     be raised if cat_X is not cat_Y. So, I uncomment the following
            #     two lines.
##             if not (category is None) and not (cat_X is cat_Y):
##                 raise ValueError, "No unambiguous category found for Hom from %s to %s."%(X,Y)
            category = cat_X
        else:
            # Search for the lowest common super category
            subcats_X = cat_X.all_super_categories(proper = True)
            subcats_Y = set(cat_Y.all_super_categories(proper = True))
            category = None
            for c in subcats_X:
                if c in subcats_Y:
                    category = c
                    break

            if category is None:
                raise TypeError, "No suitable category found for Hom from %s to %s."%(X,Y)
```


If there's no reason to include the second "`category is None`" test, then it and the previous comments should simply be deleted.  And there is a third "`category is None`" test in this block which also looks redundant.



---

archive/issue_comments_086692.json:
```json
{
    "body": "I see that issuing the deprecation warning causes some failures in `modular/abvar/homspace.py`, because the deprecation message is printed.  A minimal example to produce the message is:\n\n\n```\nsage: J = J0(37)\nsage: E = J.endomorphism_ring()\nsage: x = -1*E.gens()[0]\n```\n\n\nBut I don't understand any more about this, so maybe it's better not to include the deprecation warning.  One could simply include tests of the form\n\n\n```\nsage: H = Hom(ZZ^2, ZZ^3)\nsage: H.get_action_c(ZZ,operator.add,ZZ) is None\nTrue\n\nsage: H = Hom(ZZ^2, ZZ^3)\nsage: H.coerce_map_from_c(ZZ) is None\nTrue\n```\n\n\nwithout a deprecation warning.\n\nNote that *removing* the methods `get_action_c` and `coerce_map_from_c` causes all tests in `modular/abvar/homspace.py` to pass (of course it should, since these don't do anything anyway).  No other bit of Sage code even caused the deprecation warning to be raised, so perhaps removing them really is a good idea (in which case a deprecation warning would be the first step).  But maybe this should be left for another ticket -- I'll leave it up to you at this point, Simon.",
    "created_at": "2011-05-31T03:57:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9235",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9235#issuecomment-86692",
    "user": "niles"
}
```

I see that issuing the deprecation warning causes some failures in `modular/abvar/homspace.py`, because the deprecation message is printed.  A minimal example to produce the message is:


```
sage: J = J0(37)
sage: E = J.endomorphism_ring()
sage: x = -1*E.gens()[0]
```


But I don't understand any more about this, so maybe it's better not to include the deprecation warning.  One could simply include tests of the form


```
sage: H = Hom(ZZ^2, ZZ^3)
sage: H.get_action_c(ZZ,operator.add,ZZ) is None
True

sage: H = Hom(ZZ^2, ZZ^3)
sage: H.coerce_map_from_c(ZZ) is None
True
```


without a deprecation warning.

Note that *removing* the methods `get_action_c` and `coerce_map_from_c` causes all tests in `modular/abvar/homspace.py` to pass (of course it should, since these don't do anything anyway).  No other bit of Sage code even caused the deprecation warning to be raised, so perhaps removing them really is a good idea (in which case a deprecation warning would be the first step).  But maybe this should be left for another ticket -- I'll leave it up to you at this point, Simon.



---

archive/issue_comments_086693.json:
```json
{
    "body": "patchbot: apply 9235_doctest_homset.patch",
    "created_at": "2011-05-31T03:57:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9235",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9235#issuecomment-86693",
    "user": "niles"
}
```

patchbot: apply 9235_doctest_homset.patch



---

archive/issue_comments_086694.json:
```json
{
    "body": "Again, a long time has passed, and meanwhile the patch doesn't apply (3 out of 8 hunks fail). I'll see what I can do about it.",
    "created_at": "2013-02-14T07:51:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9235",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9235#issuecomment-86694",
    "user": "SimonKing"
}
```

Again, a long time has passed, and meanwhile the patch doesn't apply (3 out of 8 hunks fail). I'll see what I can do about it.



---

archive/issue_comments_086695.json:
```json
{
    "body": "Almost full doctest coverage for homset.py",
    "created_at": "2013-02-14T08:03:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9235",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9235#issuecomment-86695",
    "user": "SimonKing"
}
```

Almost full doctest coverage for homset.py



---

archive/issue_comments_086696.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2013-02-14T08:06:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9235",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9235#issuecomment-86696",
    "user": "SimonKing"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_086697.json:
```json
{
    "body": "Attachment\n\nThe patch is updated. I think that introducing a deprecation warning for the two survivors of the old coercion model should be the subject of a new ticket. This here should be \"doctests only\".\n\nTherefore:\n\nApply 9235_doctest_homset.patch",
    "created_at": "2013-02-14T08:06:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9235",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9235#issuecomment-86697",
    "user": "SimonKing"
}
```

Attachment

The patch is updated. I think that introducing a deprecation warning for the two survivors of the old coercion model should be the subject of a new ticket. This here should be "doctests only".

Therefore:

Apply 9235_doctest_homset.patch



---

archive/issue_comments_086698.json:
```json
{
    "body": "Changing keywords from \"doctest coverage homset\" to \"doctest coverage homset, days45\".",
    "created_at": "2013-02-16T04:42:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9235",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9235#issuecomment-86698",
    "user": "tscrim"
}
```

Changing keywords from "doctest coverage homset" to "doctest coverage homset, days45".



---

archive/issue_comments_086699.json:
```json
{
    "body": "Hey Simon,\n\nI've uploaded a review patch which goes through and brings the rest of the documentation up to current standards and added the tests to the old coercion model methods with nice warning blocks. Otherwise looks good and I think we should push the actual deprecations to when we completely remove the old coercion model. If you agree with my changes, feel free to set this to positive review.\n\nThanks,\n\nTravis",
    "created_at": "2013-02-16T04:42:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9235",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9235#issuecomment-86699",
    "user": "tscrim"
}
```

Hey Simon,

I've uploaded a review patch which goes through and brings the rest of the documentation up to current standards and added the tests to the old coercion model methods with nice warning blocks. Otherwise looks good and I think we should push the actual deprecations to when we completely remove the old coercion model. If you agree with my changes, feel free to set this to positive review.

Thanks,

Travis



---

archive/issue_comments_086700.json:
```json
{
    "body": "The patchbot has correctly applied both patches (I just checked) and finds that all tests pass. Since the patch changes formatting (\"EXAMPLE:\" becomes \"EXAMPLES::\" with double colon), I built the documentation. \n\nI apologize for some misformatting that my patch has introduced (e.g., in codomain()). This is not fixed yet.\n\nWhat shall we do? Shall I fix the misformattings in my patch? Or shall you fix it by updating the reviewer patch?",
    "created_at": "2013-02-16T09:16:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9235",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9235#issuecomment-86700",
    "user": "SimonKing"
}
```

The patchbot has correctly applied both patches (I just checked) and finds that all tests pass. Since the patch changes formatting ("EXAMPLE:" becomes "EXAMPLES::" with double colon), I built the documentation. 

I apologize for some misformatting that my patch has introduced (e.g., in codomain()). This is not fixed yet.

What shall we do? Shall I fix the misformattings in my patch? Or shall you fix it by updating the reviewer patch?



---

archive/issue_comments_086701.json:
```json
{
    "body": "Attachment\n\nFixed formatting",
    "created_at": "2013-02-16T14:24:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9235",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9235#issuecomment-86701",
    "user": "tscrim"
}
```

Attachment

Fixed formatting



---

archive/issue_comments_086702.json:
```json
{
    "body": "Can't believe I missed that...this is why one should never read over a doc for errors past midnight :P\n\nI've updated my review patch; thanks for catching that.",
    "created_at": "2013-02-16T14:28:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9235",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9235#issuecomment-86702",
    "user": "tscrim"
}
```

Can't believe I missed that...this is why one should never read over a doc for errors past midnight :P

I've updated my review patch; thanks for catching that.



---

archive/issue_comments_086703.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-02-16T18:14:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9235",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9235#issuecomment-86703",
    "user": "SimonKing"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_086704.json:
```json
{
    "body": "The reviewer patch looks fine to me!\n\nApply 9235_doctest_homset.patch trac_9235-doctest_homset-review-ts.patch",
    "created_at": "2013-02-16T18:14:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9235",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9235#issuecomment-86704",
    "user": "SimonKing"
}
```

The reviewer patch looks fine to me!

Apply 9235_doctest_homset.patch trac_9235-doctest_homset-review-ts.patch



---

archive/issue_comments_086705.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2013-02-19T06:48:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9235",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9235#issuecomment-86705",
    "user": "jdemeyer"
}
```

Resolution: fixed
