# Issue 8335: Finite Field lattices

archive/issues_008335.json:
```json
{
    "body": "Assignee: AlexGhitza\n\nCC:  defeo rbeezer hds simonking zimmerma caruso pbruin mraum fstromberg jcooley davidloeffler dfesti\n\nImplements coercion within lattices of finite fields lying above the same prime.\n\n\n```\nsage: k = GF(9)\nsage: l = GF(27)\nsage: x = k.gen() + l.gen(); x\nz6^5 + 2*z6^4 + 2*z6^3 + z6^2 + 2*z6 + 1\nsage: x.parent()\nFinite Field in z6 of size 3^6\n```\n\n\nThis feature is implemented for fields outside the range of the Conway polynomial database by the implementation of a function for finding pseudo-Conway polynomials: polynomials that satisfy all of the algebraic constraints on Conway polynomials without the lexicographic constraint that imposes uniqueness.\n\nFinite fields no longer require an explicit variable name (though they still accept one).  If a variable name is given, then outside the range of the Conway polynomial database a random or sparse polynomial is used for speed reasons; if no variable name is given then either a Conway polynomial or pseudo-Conway polynomial is used.\n\nAlso adds methods `any_root` and `squarefree_decomposition` to polynomials over finite fields.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8335\n\n",
    "created_at": "2010-02-23T17:26:08Z",
    "labels": [
        "algebra",
        "major",
        "bug"
    ],
    "title": "Finite Field lattices",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8335",
    "user": "roed"
}
```
Assignee: AlexGhitza

CC:  defeo rbeezer hds simonking zimmerma caruso pbruin mraum fstromberg jcooley davidloeffler dfesti

Implements coercion within lattices of finite fields lying above the same prime.


```
sage: k = GF(9)
sage: l = GF(27)
sage: x = k.gen() + l.gen(); x
z6^5 + 2*z6^4 + 2*z6^3 + z6^2 + 2*z6 + 1
sage: x.parent()
Finite Field in z6 of size 3^6
```


This feature is implemented for fields outside the range of the Conway polynomial database by the implementation of a function for finding pseudo-Conway polynomials: polynomials that satisfy all of the algebraic constraints on Conway polynomials without the lexicographic constraint that imposes uniqueness.

Finite fields no longer require an explicit variable name (though they still accept one).  If a variable name is given, then outside the range of the Conway polynomial database a random or sparse polynomial is used for speed reasons; if no variable name is given then either a Conway polynomial or pseudo-Conway polynomial is used.

Also adds methods `any_root` and `squarefree_decomposition` to polynomials over finite fields.

Issue created by migration from https://trac.sagemath.org/ticket/8335





---

archive/issue_comments_074279.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-23T17:33:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8335#issuecomment-74279",
    "user": "roed"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_074280.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2010-02-23T17:33:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8335#issuecomment-74280",
    "user": "roed"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_074281.json:
```json
{
    "body": "Part of a series:\n\n```\n8218 -> 8332 -> 7880 -> 7883 -> 8333 -> 8334 -> 8335\n```\n\nI tried to make each of these mostly self contained, with doctests passing after every ticket, but I didn't entirely succeed.  If you're reviewing one of these tickets, applying later tickets will hopefully fix doctest failures that you're seeing.",
    "created_at": "2010-02-23T17:37:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8335#issuecomment-74281",
    "user": "roed"
}
```

Part of a series:

```
8218 -> 8332 -> 7880 -> 7883 -> 8333 -> 8334 -> 8335
```

I tried to make each of these mostly self contained, with doctests passing after every ticket, but I didn't entirely succeed.  If you're reviewing one of these tickets, applying later tickets will hopefully fix doctest failures that you're seeing.



---

archive/issue_comments_074282.json:
```json
{
    "body": "Includes everything in 8218, 8332, 7880, 7883, 8333, 8334 and 8335 except the 8218 bundle, which you must apply first.",
    "created_at": "2010-02-23T17:50:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8335#issuecomment-74282",
    "user": "roed"
}
```

Includes everything in 8218, 8332, 7880, 7883, 8333, 8334 and 8335 except the 8218 bundle, which you must apply first.



---

archive/issue_comments_074283.json:
```json
{
    "body": "Attachment\n\nFor convenience, I added a giant patch which includes all the changes except the bundle at 8218 (which we want to leave as a bundle in order to preserve file history).",
    "created_at": "2010-02-23T17:51:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8335#issuecomment-74283",
    "user": "roed"
}
```

Attachment

For convenience, I added a giant patch which includes all the changes except the bundle at 8218 (which we want to leave as a bundle in order to preserve file history).



---

archive/issue_comments_074284.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-04-20T10:31:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8335#issuecomment-74284",
    "user": "davidloeffler"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_074285.json:
```json
{
    "body": "This doesn't apply cleanly: the patch `8335_pseudo_conway.patch` seems to conflict with something. FWIW, I am using 4.4.alpha0 with qseries\n\n```\ntrac_8446.patch\ntrac_8446_microfix.patch\ntrac_8722.patch\n7883_ideals.patch\n8333_parent_init.patch\n8333_finite_fields_to_new_coercion.patch\n7585_9_1_frac_and_coerce_updates.patch\n8334_residue_fields-rebased_for_8446.patch\n7585_12_1_fixes.patch\n8335_pseudo_conway.patch\n```\n",
    "created_at": "2010-04-20T10:31:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8335#issuecomment-74285",
    "user": "davidloeffler"
}
```

This doesn't apply cleanly: the patch `8335_pseudo_conway.patch` seems to conflict with something. FWIW, I am using 4.4.alpha0 with qseries

```
trac_8446.patch
trac_8446_microfix.patch
trac_8722.patch
7883_ideals.patch
8333_parent_init.patch
8333_finite_fields_to_new_coercion.patch
7585_9_1_frac_and_coerce_updates.patch
8334_residue_fields-rebased_for_8446.patch
7585_12_1_fixes.patch
8335_pseudo_conway.patch
```




---

archive/issue_comments_074286.json:
```json
{
    "body": "Attachment\n\nApply first",
    "created_at": "2011-06-21T13:51:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8335#issuecomment-74286",
    "user": "roed"
}
```

Attachment

Apply first



---

archive/issue_comments_074287.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-06-21T21:43:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8335#issuecomment-74287",
    "user": "roed"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_074288.json:
```json
{
    "body": "To work against 4.7, apply 8335_pseudo_conway.patch then 8335_finite_field_coerce_vs_47.patch.",
    "created_at": "2011-06-22T07:51:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8335#issuecomment-74288",
    "user": "roed"
}
```

To work against 4.7, apply 8335_pseudo_conway.patch then 8335_finite_field_coerce_vs_47.patch.



---

archive/issue_comments_074289.json:
```json
{
    "body": "Apply second",
    "created_at": "2011-06-22T08:53:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8335#issuecomment-74289",
    "user": "roed"
}
```

Apply second



---

archive/issue_comments_074290.json:
```json
{
    "body": "Attachment\n\nAgainst 4.7 for patchbot",
    "created_at": "2011-06-22T08:53:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8335#issuecomment-74290",
    "user": "roed"
}
```

Attachment

Against 4.7 for patchbot



---

archive/issue_comments_074291.json:
```json
{
    "body": "Attachment\n\nTo work against 4.7, apply 8335_pseudo_conway.patch then 8335_finite_field_coerce_vs_47.patch.",
    "created_at": "2011-06-22T08:54:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8335#issuecomment-74291",
    "user": "roed"
}
```

Attachment

To work against 4.7, apply 8335_pseudo_conway.patch then 8335_finite_field_coerce_vs_47.patch.



---

archive/issue_comments_074292.json:
```json
{
    "body": "Apply 8335_pseudo_conway.patch, 8335_finite_field_coerce_vs_47.patch",
    "created_at": "2011-06-22T08:56:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8335#issuecomment-74292",
    "user": "roed"
}
```

Apply 8335_pseudo_conway.patch, 8335_finite_field_coerce_vs_47.patch



---

archive/issue_comments_074293.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-07-13T07:04:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8335#issuecomment-74293",
    "user": "defeo"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_074294.json:
```json
{
    "body": "I still get the following failures on 4.7.1.alpha4 with 8335_pseudo_conway.patch and 8335_finite_field_coerce_vs_47.patch applied:\n\n\n```\n\tsage -t -long devel/sage/sage/matrix/matrix2.pyx # 2 doctests failed\n\tsage -t -long devel/sage/sage/rings/finite_rings/constructor.py # 1 doctests failed\n```\n",
    "created_at": "2011-07-13T07:04:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8335#issuecomment-74294",
    "user": "defeo"
}
```

I still get the following failures on 4.7.1.alpha4 with 8335_pseudo_conway.patch and 8335_finite_field_coerce_vs_47.patch applied:


```
	sage -t -long devel/sage/sage/matrix/matrix2.pyx # 2 doctests failed
	sage -t -long devel/sage/sage/rings/finite_rings/constructor.py # 1 doctests failed
```




---

archive/issue_comments_074295.json:
```json
{
    "body": "I also get 7 warnings when building the docs. These all seem to be missing blank lines and unmatched backquoutes in `sage/rings/finite_rings/constructor.py`",
    "created_at": "2011-07-13T18:20:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8335#issuecomment-74295",
    "user": "defeo"
}
```

I also get 7 warnings when building the docs. These all seem to be missing blank lines and unmatched backquoutes in `sage/rings/finite_rings/constructor.py`



---

archive/issue_comments_074296.json:
```json
{
    "body": "Attachment\n\nPatch for PCP; rebased on top of 5.7.beta3.",
    "created_at": "2013-02-08T14:30:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8335#issuecomment-74296",
    "user": "jpflori"
}
```

Attachment

Patch for PCP; rebased on top of 5.7.beta3.



---

archive/issue_comments_074297.json:
```json
{
    "body": "Attachment\n\nPatch for coercion; rebased on top of 5.7.beta3.",
    "created_at": "2013-02-08T14:30:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8335#issuecomment-74297",
    "user": "jpflori"
}
```

Attachment

Patch for coercion; rebased on top of 5.7.beta3.



---

archive/issue_comments_074298.json:
```json
{
    "body": "Patch for doc fixes; rebased on top of 5.7.beta3.",
    "created_at": "2013-02-08T14:31:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8335#issuecomment-74298",
    "user": "jpflori"
}
```

Patch for doc fixes; rebased on top of 5.7.beta3.



---

archive/issue_comments_074299.json:
```json
{
    "body": "Attachment\n\nThese patches were quite old and things have moved around since they were written.\nAs a consequence, part of the old patches now apply to different files, that is the case of the NTL GF2E implementation which has been split in a Python and a Cython file.\n\nSome pseudo Conway polys changed so that two doctests now fail (not corrected in the patches cause I did not take the time to think about it, feel free to do it).\nAs these pseudo Conway polynomials are not unique, I'm not sure if the procedure to generate them is deterministic or to which point randomness comes into play and if the failing doctests are just due to some routine called during the generation which may give a different result since the patches were originally written.\n\nNot really sure how to cast restriction on the is_square and squarefree_decomposition methods, nor what I've changed makes sense, I've come up with this quickly, feel free to correct it.\nThe basic problem was that now Sage supports function fields where we have no p-th roots and that raised an AttributeError when calling is_square which called squarefree_decomposition in some doctests.\n\nThe doc now builds ok and looks nice (although I did not have LaTeX on my computer), but may need some revamping.\nNonetheless it would be great to get this in quickly.",
    "created_at": "2013-02-08T14:40:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8335#issuecomment-74299",
    "user": "jpflori"
}
```

Attachment

These patches were quite old and things have moved around since they were written.
As a consequence, part of the old patches now apply to different files, that is the case of the NTL GF2E implementation which has been split in a Python and a Cython file.

Some pseudo Conway polys changed so that two doctests now fail (not corrected in the patches cause I did not take the time to think about it, feel free to do it).
As these pseudo Conway polynomials are not unique, I'm not sure if the procedure to generate them is deterministic or to which point randomness comes into play and if the failing doctests are just due to some routine called during the generation which may give a different result since the patches were originally written.

Not really sure how to cast restriction on the is_square and squarefree_decomposition methods, nor what I've changed makes sense, I've come up with this quickly, feel free to correct it.
The basic problem was that now Sage supports function fields where we have no p-th roots and that raised an AttributeError when calling is_square which called squarefree_decomposition in some doctests.

The doc now builds ok and looks nice (although I did not have LaTeX on my computer), but may need some revamping.
Nonetheless it would be great to get this in quickly.



---

archive/issue_comments_074300.json:
```json
{
    "body": "Changing status from needs_work to needs_info.",
    "created_at": "2013-02-08T14:40:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8335#issuecomment-74300",
    "user": "jpflori"
}
```

Changing status from needs_work to needs_info.



---

archive/issue_comments_074301.json:
```json
{
    "body": "I've just launche \"make ptestlong\" (only tested the ring dir before) and saw some errors on screen, will report later.",
    "created_at": "2013-02-08T14:59:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8335#issuecomment-74301",
    "user": "jpflori"
}
```

I've just launche "make ptestlong" (only tested the ring dir before) and saw some errors on screen, will report later.



---

archive/issue_comments_074302.json:
```json
{
    "body": "Fixes",
    "created_at": "2013-02-09T13:57:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8335#issuecomment-74302",
    "user": "jpflori"
}
```

Fixes



---

archive/issue_comments_074303.json:
```json
{
    "body": "Attachment\n\nThere were problem doing coercion because Sage now tried to define algebraic extension of Integers(1) and failed on ArithmeticError when trying 0^0, or depth of recursion if that was changed to return 1.\n\nI've added an extension method to the IntegerModring_generic class to handle separatly this ring.\n\nDid not check everything is fine though.",
    "created_at": "2013-02-09T13:59:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8335#issuecomment-74303",
    "user": "jpflori"
}
```

Attachment

There were problem doing coercion because Sage now tried to define algebraic extension of Integers(1) and failed on ArithmeticError when trying 0^0, or depth of recursion if that was changed to return 1.

I've added an extension method to the IntegerModring_generic class to handle separatly this ring.

Did not check everything is fine though.



---

archive/issue_comments_074304.json:
```json
{
    "body": "I went looking through some papers by Heath and Loehr and it appears that the output of an algorithm to compute a pseudo-conway polynomial will most likely not be deterministic unless `f.any_root()` is deterministic for polynomials in finite fields (something I'm not entirely sure about).\n\nIn this case, I'm not sure what to do about the tests, but I agree that it would be nice to move this patch along - but I'm not qualified to review it.",
    "created_at": "2013-02-14T09:53:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8335#issuecomment-74304",
    "user": "hds"
}
```

I went looking through some papers by Heath and Loehr and it appears that the output of an algorithm to compute a pseudo-conway polynomial will most likely not be deterministic unless `f.any_root()` is deterministic for polynomials in finite fields (something I'm not entirely sure about).

In this case, I'm not sure what to do about the tests, but I agree that it would be nice to move this patch along - but I'm not qualified to review it.



---

archive/issue_comments_074305.json:
```json
{
    "body": "We have some Sage meeting near Paris in France today, with a tutorial about ... finite fields.\nWe'll try to polish this one up there.",
    "created_at": "2013-02-14T09:56:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8335#issuecomment-74305",
    "user": "jpflori"
}
```

We have some Sage meeting near Paris in France today, with a tutorial about ... finite fields.
We'll try to polish this one up there.



---

archive/issue_comments_074306.json:
```json
{
    "body": "Fantastic!  I've been meaning to get back to this but have been busy with other things.  Let me know what comes up and I can review your changes if necessary.",
    "created_at": "2013-02-14T10:45:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8335#issuecomment-74306",
    "user": "roed"
}
```

Fantastic!  I've been meaning to get back to this but have been busy with other things.  Let me know what comes up and I can review your changes if necessary.



---

archive/issue_comments_074307.json:
```json
{
    "body": "That got broken again in 5.7.b4 by #13064.",
    "created_at": "2013-02-14T16:08:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8335#issuecomment-74307",
    "user": "jpflori"
}
```

That got broken again in 5.7.b4 by #13064.



---

archive/issue_comments_074308.json:
```json
{
    "body": "Rebased on top of 5.7.b4.",
    "created_at": "2013-02-14T16:22:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8335#issuecomment-74308",
    "user": "jpflori"
}
```

Rebased on top of 5.7.b4.



---

archive/issue_comments_074309.json:
```json
{
    "body": "With the last set of patches, it passes make ptestlong except:\n* one test in finite_rings/constructor.py because of a warning about Cunningham table, this does not seem harmful, so we should just change the test.\n* two tests in matrix2.py which is more worrying, although I did not really looked at it, because some \"is in prime field?\" fails.",
    "created_at": "2013-02-14T18:53:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8335#issuecomment-74309",
    "user": "jpflori"
}
```

With the last set of patches, it passes make ptestlong except:
* one test in finite_rings/constructor.py because of a warning about Cunningham table, this does not seem harmful, so we should just change the test.
* two tests in matrix2.py which is more worrying, although I did not really looked at it, because some "is in prime field?" fails.



---

archive/issue_comments_074310.json:
```json
{
    "body": "I've fixed some additional stuff and have new two concerns (in addition to the matrix2 stuff I've not dealt with):\n* the cunningham tables did not get standard so we cannot really use them (or we'll get that warning which will make one doctest fail), not sure we can trigger their use iff they are installed to avoid this spurious warning\n* as of now, if no name is provided when an extension field is trigerred and modulus is 'default' then it becomes 'conway' and that will potentially need the factorization (or the prime factors) of (p^n - 1), which might not be a good idea, so i'd prefer to just look to raise an error as before, or at least trigger a warning.",
    "created_at": "2013-02-18T16:21:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8335#issuecomment-74310",
    "user": "jpflori"
}
```

I've fixed some additional stuff and have new two concerns (in addition to the matrix2 stuff I've not dealt with):
* the cunningham tables did not get standard so we cannot really use them (or we'll get that warning which will make one doctest fail), not sure we can trigger their use iff they are installed to avoid this spurious warning
* as of now, if no name is provided when an extension field is trigerred and modulus is 'default' then it becomes 'conway' and that will potentially need the factorization (or the prime factors) of (p^n - 1), which might not be a good idea, so i'd prefer to just look to raise an error as before, or at least trigger a warning.



---

archive/issue_comments_074311.json:
```json
{
    "body": "The problem with matrix2.pyx is with multiplying a matrix with coefficients living in Q with a matrix with elements in an extension field.\nIt seems the coercion model tries to put the second one in the prime subfield and fails with the \"not in prime field\" TypeError.",
    "created_at": "2013-02-18T16:34:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8335#issuecomment-74311",
    "user": "jpflori"
}
```

The problem with matrix2.pyx is with multiplying a matrix with coefficients living in Q with a matrix with elements in an extension field.
It seems the coercion model tries to put the second one in the prime subfield and fails with the "not in prime field" TypeError.



---

archive/issue_comments_074312.json:
```json
{
    "body": "This is caused by the \"fix\" I proposed before to return IntegerMod(1) for algebraic extension of IntegerMod(1), because now I feel a common parent is chosen as IntegerMod(1), but this is a prime field and the element from the extension field \"cannot\" be cast there.\n\nA proper solution could be to investigate the infinite loop we get when the ArithmeticError is replaced with returning a unit when computing 0^0.\nAnother solution might be to forbid extension of IntegerMod(1) so that we don't get crappy common parents.",
    "created_at": "2013-02-18T16:50:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8335#issuecomment-74312",
    "user": "jpflori"
}
```

This is caused by the "fix" I proposed before to return IntegerMod(1) for algebraic extension of IntegerMod(1), because now I feel a common parent is chosen as IntegerMod(1), but this is a prime field and the element from the extension field "cannot" be cast there.

A proper solution could be to investigate the infinite loop we get when the ArithmeticError is replaced with returning a unit when computing 0^0.
Another solution might be to forbid extension of IntegerMod(1) so that we don't get crappy common parents.



---

archive/issue_comments_074313.json:
```json
{
    "body": "I think I got the infinite loop.\n\nDuring the initialization of the quotient ring, when trying to create the \"one\" element from the quotient ring of integer mod 1 quotiented by something, it tries to compute a remainder in polynomial_quotient_ring_element.py: \"polynomial %= f\" around line 137 but the mod operation is not defined for the Polynomial_ring_dense class, so this raises an AttributeError and falls back to the fallback implementation which tries to compute 0^0 which now tries to create 1 which is looked up for at the position 1 of a table of precomputed value of length the modulus+1 = 1 which is surely non sense, fails to create a IntegerrMod_int and raises a TypeError which gets caught in polynomial_quotient_ring.py around line 430 and loops...",
    "created_at": "2013-02-19T18:05:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8335#issuecomment-74313",
    "user": "jpflori"
}
```

I think I got the infinite loop.

During the initialization of the quotient ring, when trying to create the "one" element from the quotient ring of integer mod 1 quotiented by something, it tries to compute a remainder in polynomial_quotient_ring_element.py: "polynomial %= f" around line 137 but the mod operation is not defined for the Polynomial_ring_dense class, so this raises an AttributeError and falls back to the fallback implementation which tries to compute 0^0 which now tries to create 1 which is looked up for at the position 1 of a table of precomputed value of length the modulus+1 = 1 which is surely non sense, fails to create a IntegerrMod_int and raises a TypeError which gets caught in polynomial_quotient_ring.py around line 430 and loops...



---

archive/issue_comments_074314.json:
```json
{
    "body": "And of course if we return 0 (== 1) for 0^0, then the generic quo_rem loops forever as we are computing 0 % 0 and the degree will never fall...",
    "created_at": "2013-02-19T18:16:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8335#issuecomment-74314",
    "user": "jpflori"
}
```

And of course if we return 0 (== 1) for 0^0, then the generic quo_rem loops forever as we are computing 0 % 0 and the degree will never fall...



---

archive/issue_comments_074315.json:
```json
{
    "body": "Forget my rant about something becoming conway and having potential performance issues.\nIt only occurs if we have the conway polynomial precomputed, so no worries.\n\nI've removed the code calling factor_cunningham unconditionally (or rather, not through an option as in finite_rings/element_base.pyx).\nAt some point this should get automatically triggered when cunningham tables are included (#7240, #12133) and integer factorization is improved (#12125, #12117), so calling factor_cunningham directly won't be that useful anyway.",
    "created_at": "2013-02-20T16:08:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8335#issuecomment-74315",
    "user": "jpflori"
}
```

Forget my rant about something becoming conway and having potential performance issues.
It only occurs if we have the conway polynomial precomputed, so no worries.

I've removed the code calling factor_cunningham unconditionally (or rather, not through an option as in finite_rings/element_base.pyx).
At some point this should get automatically triggered when cunningham tables are included (#7240, #12133) and integer factorization is improved (#12125, #12117), so calling factor_cunningham directly won't be that useful anyway.



---

archive/issue_comments_074316.json:
```json
{
    "body": "The doctests which changed were surely not caused by different randomness but because some checks in compute_pseudo_conway_polynomial were wrong, e.g. the results for next_prime(10000)**11 was x^11 + x + 7 whose root is not of order p^11-1 but p^11-1/2",
    "created_at": "2013-02-21T10:11:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8335#issuecomment-74316",
    "user": "jpflori"
}
```

The doctests which changed were surely not caused by different randomness but because some checks in compute_pseudo_conway_polynomial were wrong, e.g. the results for next_prime(10000)**11 was x^11 + x + 7 whose root is not of order p^11-1 but p^11-1/2



---

archive/issue_comments_074317.json:
```json
{
    "body": "Attachment",
    "created_at": "2013-02-21T21:22:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8335#issuecomment-74317",
    "user": "jpflori"
}
```

Attachment



---

archive/issue_comments_074318.json:
```json
{
    "body": "Attachment",
    "created_at": "2013-02-21T21:25:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8335#issuecomment-74318",
    "user": "jpflori"
}
```

Attachment



---

archive/issue_comments_074319.json:
```json
{
    "body": "Attachment",
    "created_at": "2013-02-21T22:44:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8335#issuecomment-74319",
    "user": "jpflori"
}
```

Attachment



---

archive/issue_comments_074320.json:
```json
{
    "body": "Attachment",
    "created_at": "2013-02-22T10:50:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8335#issuecomment-74320",
    "user": "jpflori"
}
```

Attachment



---

archive/issue_comments_074321.json:
```json
{
    "body": "Attachment",
    "created_at": "2013-02-22T10:50:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8335#issuecomment-74321",
    "user": "jpflori"
}
```

Attachment



---

archive/issue_comments_074322.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2013-02-22T10:54:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8335#issuecomment-74322",
    "user": "jpflori"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_074323.json:
```json
{
    "body": "The patches should be quite ok now.\nThis needs 5.8.beta0, or at least > 5.7.beta4.\nI've made quite a bit of changes to all the coercion stuff, so that definitely needs review.\nWith a minimal set of changes to sources files you can now create algebraic extensions of the Integers(1) and let it be considered as a quotient of a univariate poly ring, etc. and everything that came up when I was trying to rebase the patches.\nIn particular, now the modulus var of an AlgebraicExtensionFunctor is always a polynomial, but I've added an additional optional field named conway to encode the fact we're dealing with pseudo-conway extensions of ff.\n\nPlease test, rant, whatever!",
    "created_at": "2013-02-22T10:54:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8335#issuecomment-74323",
    "user": "jpflori"
}
```

The patches should be quite ok now.
This needs 5.8.beta0, or at least > 5.7.beta4.
I've made quite a bit of changes to all the coercion stuff, so that definitely needs review.
With a minimal set of changes to sources files you can now create algebraic extensions of the Integers(1) and let it be considered as a quotient of a univariate poly ring, etc. and everything that came up when I was trying to rebase the patches.
In particular, now the modulus var of an AlgebraicExtensionFunctor is always a polynomial, but I've added an additional optional field named conway to encode the fact we're dealing with pseudo-conway extensions of ff.

Please test, rant, whatever!



---

archive/issue_comments_074324.json:
```json
{
    "body": "This passes \"make ptestlong\" on a usual x86_64 ubuntu 12.04.1.",
    "created_at": "2013-02-22T12:04:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8335#issuecomment-74324",
    "user": "jpflori"
}
```

This passes "make ptestlong" on a usual x86_64 ubuntu 12.04.1.



---

archive/issue_comments_074325.json:
```json
{
    "body": "Awesome!  I will take a look this weekend.",
    "created_at": "2013-02-22T12:05:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8335#issuecomment-74325",
    "user": "roed"
}
```

Awesome!  I will take a look this weekend.



---

archive/issue_comments_074326.json:
```json
{
    "body": "Attachment\n\nPrevious version was not qrefreshed...",
    "created_at": "2013-02-22T12:37:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8335#issuecomment-74326",
    "user": "jpflori"
}
```

Attachment

Previous version was not qrefreshed...



---

archive/issue_comments_074327.json:
```json
{
    "body": "Attachment\n\nShould really be ok now... sorry for the noise.",
    "created_at": "2013-02-22T13:32:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8335#issuecomment-74327",
    "user": "jpflori"
}
```

Attachment

Should really be ok now... sorry for the noise.



---

archive/issue_comments_074328.json:
```json
{
    "body": "Got the following failures\n\n\n```\nsage -t -long devel/sage/sage/coding/code_constructions.py # 90 doctests failed\nsage -t -long devel/sage/doc/en/thematic_tutorials/group_theory.rst # 1 doctests failed\nsage -t -long devel/sage/sage/modular/arithgroup/arithgroup_perm.py # 1 doctests failed\nsage -t -long devel/sage/sage/groups/matrix_gps/matrix_group.py # 1 doctests failed\nsage -t -long devel/sage/sage/homology/examples.py # 7 doctests failed\n```\n\n\nThey seem unrelated, though, and disapperead upon second testing. I'll dig the code and try to give a review in the next weeks.",
    "created_at": "2013-02-25T18:27:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8335#issuecomment-74328",
    "user": "defeo"
}
```

Got the following failures


```
sage -t -long devel/sage/sage/coding/code_constructions.py # 90 doctests failed
sage -t -long devel/sage/doc/en/thematic_tutorials/group_theory.rst # 1 doctests failed
sage -t -long devel/sage/sage/modular/arithgroup/arithgroup_perm.py # 1 doctests failed
sage -t -long devel/sage/sage/groups/matrix_gps/matrix_group.py # 1 doctests failed
sage -t -long devel/sage/sage/homology/examples.py # 7 doctests failed
```


They seem unrelated, though, and disapperead upon second testing. I'll dig the code and try to give a review in the next weeks.



---

archive/issue_comments_074329.json:
```json
{
    "body": "Apply trac_8335-pseudo_conway-5.8.b0.patch trac_8335-finite_field_coerce-5.8.b0.patch trac_8335-fixes-5.8.b0.patch",
    "created_at": "2013-03-18T06:54:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8335#issuecomment-74329",
    "user": "saraedum"
}
```

Apply trac_8335-pseudo_conway-5.8.b0.patch trac_8335-finite_field_coerce-5.8.b0.patch trac_8335-fixes-5.8.b0.patch



---

archive/issue_comments_074330.json:
```json
{
    "body": "Did anyone actually had the time to look at this?\nIt would have been great to have that in Sage during the FLINT workshop last week to check some results using Sage rather than Magma.\n\nI'm ok with what David initially did modulo what had to be fixed and that I hopefully fixed.\nSo what's left to do is to review the rebasing and changes I introduced.\nNote that I did not check that the patches still cleanly apply, that may be an issue now.",
    "created_at": "2013-05-13T14:39:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8335#issuecomment-74330",
    "user": "jpflori"
}
```

Did anyone actually had the time to look at this?
It would have been great to have that in Sage during the FLINT workshop last week to check some results using Sage rather than Magma.

I'm ok with what David initially did modulo what had to be fixed and that I hopefully fixed.
So what's left to do is to review the rebasing and changes I introduced.
Note that I did not check that the patches still cleanly apply, that may be an issue now.



---

archive/issue_comments_074331.json:
```json
{
    "body": "Replying to [comment:42 jpflori]:\n> Did anyone actually had the time to look at this?\nI started to look at it a while ago\u2026\n\n> So what's left to do is to review the rebasing and changes I introduced.\nThat's good to know. I don't want to make any promises about reviewing this but I would certainly like to see this in sage. In any case, I won't review this in the next three weeks.",
    "created_at": "2013-05-13T16:41:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8335#issuecomment-74331",
    "user": "saraedum"
}
```

Replying to [comment:42 jpflori]:
> Did anyone actually had the time to look at this?
I started to look at it a while ago…

> So what's left to do is to review the rebasing and changes I introduced.
That's good to know. I don't want to make any promises about reviewing this but I would certainly like to see this in sage. In any case, I won't review this in the next three weeks.



---

archive/issue_comments_074332.json:
```json
{
    "body": "Apart from fuzz 2, it still applies cleanly to 5.10.beta3 and all tests passes.\nNot sure what the patchbot complains about, missing docstrings?",
    "created_at": "2013-05-15T14:48:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8335#issuecomment-74332",
    "user": "jpflori"
}
```

Apart from fuzz 2, it still applies cleanly to 5.10.beta3 and all tests passes.
Not sure what the patchbot complains about, missing docstrings?



---

archive/issue_comments_074333.json:
```json
{
    "body": "Attachment\n\nApply trac_8335-pseudo_conway-5.8.b0.patch trac_8335-finite_field_coerce-5.8.b0.patch trac_8335-fixes-5.10.b3.patch",
    "created_at": "2013-05-16T13:13:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8335#issuecomment-74333",
    "user": "saraedum"
}
```

Attachment

Apply trac_8335-pseudo_conway-5.8.b0.patch trac_8335-finite_field_coerce-5.8.b0.patch trac_8335-fixes-5.10.b3.patch



---

archive/issue_comments_074334.json:
```json
{
    "body": "apply trac_8335-pseudo_conway-5.10.b3.patch trac_8335-finite_field_coerce-5.8.b0.patch trac_8335-fixes-5.8.b0.patch",
    "created_at": "2013-05-16T13:15:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8335#issuecomment-74334",
    "user": "saraedum"
}
```

apply trac_8335-pseudo_conway-5.10.b3.patch trac_8335-finite_field_coerce-5.8.b0.patch trac_8335-fixes-5.8.b0.patch



---

archive/issue_comments_074335.json:
```json
{
    "body": "This definitely lacks \"going down\", e.g. taking the trace from a finite field to a subfield and being able to recognize that as an element of the subfield.\nBut let's keep that for another ticket.",
    "created_at": "2013-06-04T09:09:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8335#issuecomment-74335",
    "user": "jpflori"
}
```

This definitely lacks "going down", e.g. taking the trace from a finite field to a subfield and being able to recognize that as an element of the subfield.
But let's keep that for another ticket.



---

archive/issue_comments_074336.json:
```json
{
    "body": "Changing keywords from \"\" to \"days49\".",
    "created_at": "2013-06-17T16:45:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8335#issuecomment-74336",
    "user": "defeo"
}
```

Changing keywords from "" to "days49".



---

archive/issue_comments_074337.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2013-06-17T16:45:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8335#issuecomment-74337",
    "user": "defeo"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_074338.json:
```json
{
    "body": "Hi,\n\nThe doc in `constructor.py` says\n\n\n```\n - ``modulus`` - blabla\n   - 'default': a Conway polynomial is used if in the database. Otherwise \n     a sparse polynomial is used for binary fields and a \n     random polynomial is used for other characteristics. \n```\n\n\nbut I got the impression that the default is to use pseudo-conway. By the way, is it reasonable to use pseudo-conway as default\u00a0? It is utterly slow\u00a0!\n\n\n```\nsage: %time k = GF(next_prime(100000)^2) \nCPU times: user 16.41 s, sys: 0.05 s, total: 16.45 s\nWall time: 16.18 s\nsage: %time l = GF(next_prime(100000)^3) \nCPU times: user 60.19 s, sys: 0.07 s, total: 60.26 s\nWall time: 59.97 s\nsage: %time (k.gen() + l.gen()).parent()\nCPU times: user 0.08 s, sys: 0.00 s, total: 0.09 s\nWall time: 0.07 s\nFinite Field in z6 of size 100003^6\n```\n\n\nCompare this with Magma\n\n\n```\n> time k := GF(NextPrime(100000)^2);                                                                                                  \nTime: 0.000\n> time l := GF(NextPrime(100000)^3); \nTime: 0.000\n\n> time CommonOverfield(l, k);              \nTime: 0.030\n```\n\n\nWouldn't it be better to keep using ``random`` as default, and give error messages suggesting to use ``conway`` when the user tries to add/multiply/whatever two elements in different fields?\n\n\nOn another note, I get the following messages (I suppressed them from the output above for readability).\n\n\n```\nsage: k = GF(next_prime(10000)^11)\n  ***   Warning: Mod(a,b)^n with n >> b : wasteful.\n  ***   Warning: Mod(a,b)^n with n >> b : wasteful.\n  ***   Warning: Mod(a,b)^n with n >> b : wasteful.\n  ***   Warning: Mod(a,b)^n with n >> b : wasteful.\n  ***   Warning: Mod(a,b)^n with n >> b : wasteful.\n  ***   Warning: Mod(a,b)^n with n >> b : wasteful.\n  ***   Warning: Mod(a,b)^n with n >> b : wasteful.\n  ***   Warning: Mod(a,b)^n with n >> b : wasteful.\n  ***   Warning: Mod(a,b)^n with n >> b : wasteful.\n  ***   Warning: Mod(a,b)^n with n >> b : wasteful.\n  ***   Warning: Mod(a,b)^n with n >> b : wasteful.\n  ***   Warning: Mod(a,b)^n with n >> b : wasteful.\n  ***   Warning: Mod(a,b)^n with n >> b : wasteful.\n  ***   Warning: Mod(a,b)^n with n >> b : wasteful.\n```\n\n\nAny ideas on these?",
    "created_at": "2013-06-17T16:45:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8335#issuecomment-74338",
    "user": "defeo"
}
```

Hi,

The doc in `constructor.py` says


```
 - ``modulus`` - blabla
   - 'default': a Conway polynomial is used if in the database. Otherwise 
     a sparse polynomial is used for binary fields and a 
     random polynomial is used for other characteristics. 
```


but I got the impression that the default is to use pseudo-conway. By the way, is it reasonable to use pseudo-conway as default ? It is utterly slow !


```
sage: %time k = GF(next_prime(100000)^2) 
CPU times: user 16.41 s, sys: 0.05 s, total: 16.45 s
Wall time: 16.18 s
sage: %time l = GF(next_prime(100000)^3) 
CPU times: user 60.19 s, sys: 0.07 s, total: 60.26 s
Wall time: 59.97 s
sage: %time (k.gen() + l.gen()).parent()
CPU times: user 0.08 s, sys: 0.00 s, total: 0.09 s
Wall time: 0.07 s
Finite Field in z6 of size 100003^6
```


Compare this with Magma


```
> time k := GF(NextPrime(100000)^2);                                                                                                  
Time: 0.000
> time l := GF(NextPrime(100000)^3); 
Time: 0.000

> time CommonOverfield(l, k);              
Time: 0.030
```


Wouldn't it be better to keep using ``random`` as default, and give error messages suggesting to use ``conway`` when the user tries to add/multiply/whatever two elements in different fields?


On another note, I get the following messages (I suppressed them from the output above for readability).


```
sage: k = GF(next_prime(10000)^11)
  ***   Warning: Mod(a,b)^n with n >> b : wasteful.
  ***   Warning: Mod(a,b)^n with n >> b : wasteful.
  ***   Warning: Mod(a,b)^n with n >> b : wasteful.
  ***   Warning: Mod(a,b)^n with n >> b : wasteful.
  ***   Warning: Mod(a,b)^n with n >> b : wasteful.
  ***   Warning: Mod(a,b)^n with n >> b : wasteful.
  ***   Warning: Mod(a,b)^n with n >> b : wasteful.
  ***   Warning: Mod(a,b)^n with n >> b : wasteful.
  ***   Warning: Mod(a,b)^n with n >> b : wasteful.
  ***   Warning: Mod(a,b)^n with n >> b : wasteful.
  ***   Warning: Mod(a,b)^n with n >> b : wasteful.
  ***   Warning: Mod(a,b)^n with n >> b : wasteful.
  ***   Warning: Mod(a,b)^n with n >> b : wasteful.
  ***   Warning: Mod(a,b)^n with n >> b : wasteful.
```


Any ideas on these?



---

archive/issue_comments_074339.json:
```json
{
    "body": "Replying to [comment:49 defeo]:\n> Hi,\n> \n> The doc in `constructor.py` says\n> \n> {{{\n>  - ``modulus`` - blabla\n>    - 'default': a Conway polynomial is used if in the database. Otherwise \n>      a sparse polynomial is used for binary fields and a \n>      random polynomial is used for other characteristics. \n> }}}\n> \n> but I got the impression that the default is to use pseudo-conway. By the way, is it reasonable to use pseudo-conway as default\u00a0? It is utterly slow\u00a0!\nIt is and is expected to be.\n> \n> {{{\n> sage: %time k = GF(next_prime(100000)^2) \n> CPU times: user 16.41 s, sys: 0.05 s, total: 16.45 s\n> Wall time: 16.18 s\n> sage: %time l = GF(next_prime(100000)^3) \n> CPU times: user 60.19 s, sys: 0.07 s, total: 60.26 s\n> Wall time: 59.97 s\n> sage: %time (k.gen() + l.gen()).parent()\n> CPU times: user 0.08 s, sys: 0.00 s, total: 0.09 s\n> Wall time: 0.07 s\n> Finite Field in z6 of size 100003^6\n> }}}\n> \n> Compare this with Magma\n> \n> {{{\n> > time k := GF(NextPrime(100000)^2);                                                                                                  \n> Time: 0.000\n> > time l := GF(NextPrime(100000)^3); \n> Time: 0.000\n> \n> > time CommonOverfield(l, k);              \n> Time: 0.030\n> }}}\n> \nI think the rationale is that Sage did not support finite fields with unnamed generator before this patch.\nSo IIRC you could simply not do the above.\nIf you do something which used to work like\n\n```\nK.<a> = GF(182918291829182918291892819)\n```\n\n(assuming the random typing is some prime power)\nI think it still picks up a random modulus as before (and is fast enough).\n\nI agree it's kind of a bad thing to provide a new (but still natural, especially for Magma's users) way to create finite fields which is horribly slow.\nSo we might want to fix this.\n\nAlso note that this ticket only provides lattices for finite fields created with pseudo-conway polynomials.\nThe goal is not to provide (compatible) embeddings for all finite fields (as Magma is capable of).\n> Wouldn't it be better to keep using ``random`` as default, and give error messages suggesting to use ``conway`` when the user tries to add/multiply/whatever two elements in different fields?\n> \n> \n> On another note, I get the following messages (I suppressed them from the output above for readability).\n> \n> {{{\n> sage: k = GF(next_prime(10000)^11)\n>   ***   Warning: Mod(a,b)^n with n >> b : wasteful.\n>   ***   Warning: Mod(a,b)^n with n >> b : wasteful.\n>   ***   Warning: Mod(a,b)^n with n >> b : wasteful.\n>   ***   Warning: Mod(a,b)^n with n >> b : wasteful.\n>   ***   Warning: Mod(a,b)^n with n >> b : wasteful.\n>   ***   Warning: Mod(a,b)^n with n >> b : wasteful.\n>   ***   Warning: Mod(a,b)^n with n >> b : wasteful.\n>   ***   Warning: Mod(a,b)^n with n >> b : wasteful.\n>   ***   Warning: Mod(a,b)^n with n >> b : wasteful.\n>   ***   Warning: Mod(a,b)^n with n >> b : wasteful.\n>   ***   Warning: Mod(a,b)^n with n >> b : wasteful.\n>   ***   Warning: Mod(a,b)^n with n >> b : wasteful.\n>   ***   Warning: Mod(a,b)^n with n >> b : wasteful.\n>   ***   Warning: Mod(a,b)^n with n >> b : wasteful.\n> }}}\n> \n> Any ideas on these?\nNo idea, I'll check tomorrow.",
    "created_at": "2013-06-17T16:53:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8335#issuecomment-74339",
    "user": "jpflori"
}
```

Replying to [comment:49 defeo]:
> Hi,
> 
> The doc in `constructor.py` says
> 
> {{{
>  - ``modulus`` - blabla
>    - 'default': a Conway polynomial is used if in the database. Otherwise 
>      a sparse polynomial is used for binary fields and a 
>      random polynomial is used for other characteristics. 
> }}}
> 
> but I got the impression that the default is to use pseudo-conway. By the way, is it reasonable to use pseudo-conway as default ? It is utterly slow !
It is and is expected to be.
> 
> {{{
> sage: %time k = GF(next_prime(100000)^2) 
> CPU times: user 16.41 s, sys: 0.05 s, total: 16.45 s
> Wall time: 16.18 s
> sage: %time l = GF(next_prime(100000)^3) 
> CPU times: user 60.19 s, sys: 0.07 s, total: 60.26 s
> Wall time: 59.97 s
> sage: %time (k.gen() + l.gen()).parent()
> CPU times: user 0.08 s, sys: 0.00 s, total: 0.09 s
> Wall time: 0.07 s
> Finite Field in z6 of size 100003^6
> }}}
> 
> Compare this with Magma
> 
> {{{
> > time k := GF(NextPrime(100000)^2);                                                                                                  
> Time: 0.000
> > time l := GF(NextPrime(100000)^3); 
> Time: 0.000
> 
> > time CommonOverfield(l, k);              
> Time: 0.030
> }}}
> 
I think the rationale is that Sage did not support finite fields with unnamed generator before this patch.
So IIRC you could simply not do the above.
If you do something which used to work like

```
K.<a> = GF(182918291829182918291892819)
```

(assuming the random typing is some prime power)
I think it still picks up a random modulus as before (and is fast enough).

I agree it's kind of a bad thing to provide a new (but still natural, especially for Magma's users) way to create finite fields which is horribly slow.
So we might want to fix this.

Also note that this ticket only provides lattices for finite fields created with pseudo-conway polynomials.
The goal is not to provide (compatible) embeddings for all finite fields (as Magma is capable of).
> Wouldn't it be better to keep using ``random`` as default, and give error messages suggesting to use ``conway`` when the user tries to add/multiply/whatever two elements in different fields?
> 
> 
> On another note, I get the following messages (I suppressed them from the output above for readability).
> 
> {{{
> sage: k = GF(next_prime(10000)^11)
>   ***   Warning: Mod(a,b)^n with n >> b : wasteful.
>   ***   Warning: Mod(a,b)^n with n >> b : wasteful.
>   ***   Warning: Mod(a,b)^n with n >> b : wasteful.
>   ***   Warning: Mod(a,b)^n with n >> b : wasteful.
>   ***   Warning: Mod(a,b)^n with n >> b : wasteful.
>   ***   Warning: Mod(a,b)^n with n >> b : wasteful.
>   ***   Warning: Mod(a,b)^n with n >> b : wasteful.
>   ***   Warning: Mod(a,b)^n with n >> b : wasteful.
>   ***   Warning: Mod(a,b)^n with n >> b : wasteful.
>   ***   Warning: Mod(a,b)^n with n >> b : wasteful.
>   ***   Warning: Mod(a,b)^n with n >> b : wasteful.
>   ***   Warning: Mod(a,b)^n with n >> b : wasteful.
>   ***   Warning: Mod(a,b)^n with n >> b : wasteful.
>   ***   Warning: Mod(a,b)^n with n >> b : wasteful.
> }}}
> 
> Any ideas on these?
No idea, I'll check tomorrow.



---

archive/issue_comments_074340.json:
```json
{
    "body": "Attachment",
    "created_at": "2013-06-18T14:24:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8335#issuecomment-74340",
    "user": "jpflori"
}
```

Attachment



---

archive/issue_comments_074341.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2013-06-18T14:32:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8335#issuecomment-74341",
    "user": "jpflori"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_074342.json:
```json
{
    "body": "There was some actual bug in the code which triggered the computation of the pseudo-Conway polynomials tree twice in the case where the extension degree was prime.\nFirst the way it should, and then using the same arguments as in the case where this degree is not prime which at some point triggered the computation of the power of modular integer with a small modulus and a huge exponent and PARI rants when you do that;\njust try\n\n```\nMod(3,5)._pari_()**28172187218728127182718271821982918291829182918291\n```\n\n\nSo the newly uploaded patch makes it so we only build the tree once as we always should have, and at least in Luca's example it prevents PARI rants to get on the screen.",
    "created_at": "2013-06-18T14:32:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8335#issuecomment-74342",
    "user": "jpflori"
}
```

There was some actual bug in the code which triggered the computation of the pseudo-Conway polynomials tree twice in the case where the extension degree was prime.
First the way it should, and then using the same arguments as in the case where this degree is not prime which at some point triggered the computation of the power of modular integer with a small modulus and a huge exponent and PARI rants when you do that;
just try

```
Mod(3,5)._pari_()**28172187218728127182718271821982918291829182918291
```


So the newly uploaded patch makes it so we only build the tree once as we always should have, and at least in Luca's example it prevents PARI rants to get on the screen.



---

archive/issue_comments_074343.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2013-06-18T14:38:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8335#issuecomment-74343",
    "user": "jpflori"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_074344.json:
```json
{
    "body": "If you try\n\n```\nGF(next_prime(10000)^12\n```\n\nwhich is a non-prime extension you still get PARI's rants on-screen.\n\nMore worrying is that\n\n```\nGF(next_prime(10000)^14)\n```\n\nfails with an AssertionError.",
    "created_at": "2013-06-18T14:38:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8335#issuecomment-74344",
    "user": "jpflori"
}
```

If you try

```
GF(next_prime(10000)^12
```

which is a non-prime extension you still get PARI's rants on-screen.

More worrying is that

```
GF(next_prime(10000)^14)
```

fails with an AssertionError.



---

archive/issue_comments_074345.json:
```json
{
    "body": "All these troubles seem to come from the _find_pow_of_frobenius function (the algo used inside and arguments passed to it).",
    "created_at": "2013-06-18T15:12:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8335#issuecomment-74345",
    "user": "jpflori"
}
```

All these troubles seem to come from the _find_pow_of_frobenius function (the algo used inside and arguments passed to it).



---

archive/issue_comments_074346.json:
```json
{
    "body": "New patch which pushouts elements of two extension fields of same characteristic into the extension field with degree the lcm rather than the product as the old code used to do.",
    "created_at": "2013-06-18T15:44:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8335#issuecomment-74346",
    "user": "jpflori"
}
```

New patch which pushouts elements of two extension fields of same characteristic into the extension field with degree the lcm rather than the product as the old code used to do.



---

archive/issue_comments_074347.json:
```json
{
    "body": "Thanks to Luca I had a look at the math part of the algorithms implemented and am not sure about all of it.\nIn particular, after a quick look, it seems to me that all the _frobenius_shift part is useless and all that should be implemented is the algorithm form HL99 without the last loop checking that the polynomial is indeed minimal for some order (e.g. the one used for conway polynomials).",
    "created_at": "2013-06-19T12:24:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8335#issuecomment-74347",
    "user": "jpflori"
}
```

Thanks to Luca I had a look at the math part of the algorithms implemented and am not sure about all of it.
In particular, after a quick look, it seems to me that all the _frobenius_shift part is useless and all that should be implemented is the algorithm form HL99 without the last loop checking that the polynomial is indeed minimal for some order (e.g. the one used for conway polynomials).



---

archive/issue_comments_074348.json:
```json
{
    "body": "I think I missed something in the algo so the above message is surely wrong, I need some more time...",
    "created_at": "2013-06-19T20:58:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8335#issuecomment-74348",
    "user": "jpflori"
}
```

I think I missed something in the algo so the above message is surely wrong, I need some more time...



---

archive/issue_comments_074349.json:
```json
{
    "body": "I had another look at the proofs in the paper and the _frobenius_shift stuff definitely seems to make sense (on top of the fact that without it everything is broken :)), due to the fact we use actual concrete representations of the fields whereas the algorithm is somehow more abstract.\n\nSo now we're back with the problems from http://trac.sagemath.org/sage_trac/ticket/8335#comment:52.",
    "created_at": "2013-06-20T11:49:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8335#issuecomment-74349",
    "user": "jpflori"
}
```

I had another look at the proofs in the paper and the _frobenius_shift stuff definitely seems to make sense (on top of the fact that without it everything is broken :)), due to the fact we use actual concrete representations of the fields whereas the algorithm is somehow more abstract.

So now we're back with the problems from http://trac.sagemath.org/sage_trac/ticket/8335#comment:52.



---

archive/issue_comments_074350.json:
```json
{
    "body": "This already fails with:\n\n```\nfind_pseudo_conway_polynomial_tree(5,6,False)\n```\n",
    "created_at": "2013-06-20T11:57:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8335#issuecomment-74350",
    "user": "jpflori"
}
```

This already fails with:

```
find_pseudo_conway_polynomial_tree(5,6,False)
```




---

archive/issue_comments_074351.json:
```json
{
    "body": "I think the problem is that we don't (or not anymore, there used to be two calls to the PCPT constructor before in the case where n is prime) ensure consistency of roots chosen for prime degree extension (basically running kind of _frobenius_shift when n is prime).",
    "created_at": "2013-06-20T12:12:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8335#issuecomment-74351",
    "user": "jpflori"
}
```

I think the problem is that we don't (or not anymore, there used to be two calls to the PCPT constructor before in the case where n is prime) ensure consistency of roots chosen for prime degree extension (basically running kind of _frobenius_shift when n is prime).



---

archive/issue_comments_074352.json:
```json
{
    "body": "That was easily fixed.\n\nNote that\n\n```\nfind_pseudo_conway_polynomial_tree(11,14,False)\n```\n\nseems to enter an infinite loop.",
    "created_at": "2013-06-20T12:19:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8335#issuecomment-74352",
    "user": "jpflori"
}
```

That was easily fixed.

Note that

```
find_pseudo_conway_polynomial_tree(11,14,False)
```

seems to enter an infinite loop.



---

archive/issue_comments_074353.json:
```json
{
    "body": "Ok, it seems the main issue now is that nth_root is slow for big parameters (or make the range() function oveflow).",
    "created_at": "2013-06-20T13:04:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8335#issuecomment-74353",
    "user": "jpflori"
}
```

Ok, it seems the main issue now is that nth_root is slow for big parameters (or make the range() function oveflow).



---

archive/issue_comments_074354.json:
```json
{
    "body": "The ovrflow happens because I wanted to let nth_root return all roots rather than just one as in David's code.\n\nUsing David's approach let the calculation for\n\n```\nGF(next_prime(10000**14))\n```\n\nfinish (although we still get PARI's warnings but that's \"not really\" a problem).",
    "created_at": "2013-06-20T13:11:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8335#issuecomment-74354",
    "user": "jpflori"
}
```

The ovrflow happens because I wanted to let nth_root return all roots rather than just one as in David's code.

Using David's approach let the calculation for

```
GF(next_prime(10000**14))
```

finish (although we still get PARI's warnings but that's "not really" a problem).



---

archive/issue_comments_074355.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2013-06-20T13:14:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8335#issuecomment-74355",
    "user": "jpflori"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_074356.json:
```json
{
    "body": "Ok, the set of patch looks quite clean now, so back to needs_review.\n\nThe only thing not perfect is that we still get PARI's warning in some cases...",
    "created_at": "2013-06-20T13:14:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8335#issuecomment-74356",
    "user": "jpflori"
}
```

Ok, the set of patch looks quite clean now, so back to needs_review.

The only thing not perfect is that we still get PARI's warning in some cases...



---

archive/issue_comments_074357.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2013-06-20T13:18:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8335#issuecomment-74357",
    "user": "jpflori"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_074358.json:
```json
{
    "body": "And back to needs_work, I did not check the doctests in the modified files.",
    "created_at": "2013-06-20T13:18:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8335#issuecomment-74358",
    "user": "jpflori"
}
```

And back to needs_work, I did not check the doctests in the modified files.



---

archive/issue_comments_074359.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2013-06-20T13:32:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8335#issuecomment-74359",
    "user": "jpflori"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_074360.json:
```json
{
    "body": "Should be ok now.\nReverted David's test for primitivity rather than using is_primitive which would waste a lot of time factoring over and over q = p**n -1.",
    "created_at": "2013-06-20T13:32:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8335#issuecomment-74360",
    "user": "jpflori"
}
```

Should be ok now.
Reverted David's test for primitivity rather than using is_primitive which would waste a lot of time factoring over and over q = p**n -1.



---

archive/issue_comments_074361.json:
```json
{
    "body": "(Small fix to a silly typo)",
    "created_at": "2013-06-20T13:54:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8335#issuecomment-74361",
    "user": "jpflori"
}
```

(Small fix to a silly typo)



---

archive/issue_comments_074362.json:
```json
{
    "body": "Added some doctests hopefully showing that embeddings are correct and compatible.",
    "created_at": "2013-06-20T15:43:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8335#issuecomment-74362",
    "user": "jpflori"
}
```

Added some doctests hopefully showing that embeddings are correct and compatible.



---

archive/issue_comments_074363.json:
```json
{
    "body": "Ok, the last tests I added:\n\n```\n\n        sage: old_exists_cp = sage.rings.finite_rings.constructor.exists_conway_polynomial\n        sage: sage.rings.finite_rings.constructor.exists_conway_polynomial = lambda p, n: False\n        sage: k = GF(3**10)\n        sage: l = GF(3**20)\n        sage: k.modulus() == conway_polynomial(3, 10)\n        False\n        sage: l(k.gen()**10) == l(k.gen())**10\n        True\n        sage: del k, l\n        sage: import gc\n        sage: gc.collect();\n        sage: sage.rings.finite_rings.constructor.exists_conway_polynomial = old_exists_cp\n```\n\nintroduced some failures in the test:\n\n```\nsage: GF.other_keys(key, K)\n            [(9, ('a',), x^2 + 2*x + 2, None, '{}', 3, 2, True),\n             (9, ('a',), x^2 + 2*x + 2, 'givaro', '{}', 3, 2, True)]\n```\n\nIndeed, although I explicitely asked to delete k and l and restored a proper exists_... function, the field GF(3**20) stay cached and so the pseudo-Conway, but not Conway, modulus used to build GF(3**2).\n\nThe reason for that is that we performed arithmetic on elements of k and l which triggered creation of an embedding of k into l which prevents the collection of k and l.\nThis is bad and is surely the same problem as in #14711.\n\nSo I just removed the hack forcing the use of pseudo-Conway polynomials.",
    "created_at": "2013-06-20T17:23:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8335#issuecomment-74363",
    "user": "jpflori"
}
```

Ok, the last tests I added:

```

        sage: old_exists_cp = sage.rings.finite_rings.constructor.exists_conway_polynomial
        sage: sage.rings.finite_rings.constructor.exists_conway_polynomial = lambda p, n: False
        sage: k = GF(3**10)
        sage: l = GF(3**20)
        sage: k.modulus() == conway_polynomial(3, 10)
        False
        sage: l(k.gen()**10) == l(k.gen())**10
        True
        sage: del k, l
        sage: import gc
        sage: gc.collect();
        sage: sage.rings.finite_rings.constructor.exists_conway_polynomial = old_exists_cp
```

introduced some failures in the test:

```
sage: GF.other_keys(key, K)
            [(9, ('a',), x^2 + 2*x + 2, None, '{}', 3, 2, True),
             (9, ('a',), x^2 + 2*x + 2, 'givaro', '{}', 3, 2, True)]
```

Indeed, although I explicitely asked to delete k and l and restored a proper exists_... function, the field GF(3**20) stay cached and so the pseudo-Conway, but not Conway, modulus used to build GF(3**2).

The reason for that is that we performed arithmetic on elements of k and l which triggered creation of an embedding of k into l which prevents the collection of k and l.
This is bad and is surely the same problem as in #14711.

So I just removed the hack forcing the use of pseudo-Conway polynomials.



---

archive/issue_comments_074364.json:
```json
{
    "body": "Attachment",
    "created_at": "2013-06-26T08:24:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8335#issuecomment-74364",
    "user": "caruso"
}
```

Attachment



---

archive/issue_comments_074365.json:
```json
{
    "body": "In relation to #12142, I am currently working on a patch that makes the construction of irreducible polynomials independent of the finite field implementations (prime_modn, givaro, ntl_gf2e, ext_pari and the future pari_ffelt).  Currently every finite field implementation has to do its own parsing of string values of modulus (like 'conway', 'random' etc.).  It would be more elegant to handle all these string values in the generic constructor, and always pass an actual polynomial to the finite field implementation.\n\nIn the current version of Sage, the only situation in which the implementation needs to know whether the field is defined by a Conway polynomial is when converting elements to GAP.  This means that always passing a polynomial as the modulus is fine, as long as one can check if the polynomial is a Conway polynomial if and when it is needed.  This is easy to do by checking the database.\n\nWith your patch, each implementation gets an increased dependence on string values for the modulus parameter.  I am wondering if this can be avoided by doing all the pseudo-Conway related stuff inside the generic finite field code.\n\n[...to be continued...]",
    "created_at": "2013-06-26T10:27:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8335#issuecomment-74365",
    "user": "pbruin"
}
```

In relation to #12142, I am currently working on a patch that makes the construction of irreducible polynomials independent of the finite field implementations (prime_modn, givaro, ntl_gf2e, ext_pari and the future pari_ffelt).  Currently every finite field implementation has to do its own parsing of string values of modulus (like 'conway', 'random' etc.).  It would be more elegant to handle all these string values in the generic constructor, and always pass an actual polynomial to the finite field implementation.

In the current version of Sage, the only situation in which the implementation needs to know whether the field is defined by a Conway polynomial is when converting elements to GAP.  This means that always passing a polynomial as the modulus is fine, as long as one can check if the polynomial is a Conway polynomial if and when it is needed.  This is easy to do by checking the database.

With your patch, each implementation gets an increased dependence on string values for the modulus parameter.  I am wondering if this can be avoided by doing all the pseudo-Conway related stuff inside the generic finite field code.

[...to be continued...]



---

archive/issue_comments_074366.json:
```json
{
    "body": "Replying to [comment:71 pbruin]:\n> In relation to #12142, I am currently working on a patch that makes the construction of irreducible polynomials independent of the finite field implementations (prime_modn, givaro, ntl_gf2e, ext_pari and the future pari_ffelt).  Currently every finite field implementation has to do its own parsing of string values of modulus (like 'conway', 'random' etc.).  It would be more elegant to handle all these string values in the generic constructor, and always pass an actual polynomial to the finite field implementation.\n> \n> In the current version of Sage, the only situation in which the implementation needs to know whether the field is defined by a Conway polynomial is when converting elements to GAP.  This means that always passing a polynomial as the modulus is fine, as long as one can check if the polynomial is a Conway polynomial if and when it is needed.  This is easy to do by checking the database.\nBeware that the last patch which contains my modification to the two original patches by David changes quite a lot of thing.\nIn particular, I think that with it modulus contains the real modulus as well and I use additional attributes to check for pseudo-Conway construction.\n\nAlso note that the real nice addition of this patch is mainly the compatible embeddings.\nIndeed, for practical purposes, it seems that only the Conway polynomials from the databse will be used.\nConstructing pseudo-Conway polynomials is quite as  slow as contructions genuine Conway polynomials so when you will actually use them, i.e. for quite large parameters because you have to be outside of the Conway database, it will already be quite slow and unpractical.\n\n> \n> With your patch, each implementation gets an increased dependence on string values for the modulus parameter.  I am wondering if this can be avoided by doing all the pseudo-Conway related stuff inside the generic finite field code.\n> \n> [...to be continued...]",
    "created_at": "2013-06-26T10:35:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8335#issuecomment-74366",
    "user": "jpflori"
}
```

Replying to [comment:71 pbruin]:
> In relation to #12142, I am currently working on a patch that makes the construction of irreducible polynomials independent of the finite field implementations (prime_modn, givaro, ntl_gf2e, ext_pari and the future pari_ffelt).  Currently every finite field implementation has to do its own parsing of string values of modulus (like 'conway', 'random' etc.).  It would be more elegant to handle all these string values in the generic constructor, and always pass an actual polynomial to the finite field implementation.
> 
> In the current version of Sage, the only situation in which the implementation needs to know whether the field is defined by a Conway polynomial is when converting elements to GAP.  This means that always passing a polynomial as the modulus is fine, as long as one can check if the polynomial is a Conway polynomial if and when it is needed.  This is easy to do by checking the database.
Beware that the last patch which contains my modification to the two original patches by David changes quite a lot of thing.
In particular, I think that with it modulus contains the real modulus as well and I use additional attributes to check for pseudo-Conway construction.

Also note that the real nice addition of this patch is mainly the compatible embeddings.
Indeed, for practical purposes, it seems that only the Conway polynomials from the databse will be used.
Constructing pseudo-Conway polynomials is quite as  slow as contructions genuine Conway polynomials so when you will actually use them, i.e. for quite large parameters because you have to be outside of the Conway database, it will already be quite slow and unpractical.

> 
> With your patch, each implementation gets an increased dependence on string values for the modulus parameter.  I am wondering if this can be avoided by doing all the pseudo-Conway related stuff inside the generic finite field code.
> 
> [...to be continued...]



---

archive/issue_comments_074367.json:
```json
{
    "body": "Replying to [comment:72 jpflori]:\n> Beware that the last patch which contains my modification to the two original patches by David changes quite a lot of thing.\n> In particular, I think that with it modulus contains the real modulus as well and I use additional attributes to check for pseudo-Conway construction.\n\nOK, I'll try to find out if and how my ideas about making the choice of polynomial independently of the finite field implementation can be harmonised with your patch.  At first sight there does not seem to be a huge clash.  I am mostly worried about the use of strings like 'conwayz' as a modulus, which really seems to be overloading this parameter too much.\n\n> Also note that the real nice addition of this patch is mainly the compatible embeddings.\n\nI agree that this is a very desirable thing to have, and it is also nice to be able to simply type ``F = GF(p<sup>n</sup>)`` without having to care about variable names and embeddings.  I do think it is good to think carefully about how exactly to accomplish this.\n\nIn particular, I am not sure if it is wise to say in the documentation/specification that this compatibility is achieved using (pseudo-)Conway polynomials, since different implementations are imaginable.  I am thinking of the standard models for finite fields by Lenstra and de Smit, which are constructed in a way that does not seem to be related to Conway polynomials.\n\nFrom a conceptual point of view, it is desirable that GF(p<sup>n</sup>) without any arguments should refer to the unique subfield of cardinality p<sup>n</sup> *inside a chosen algebraic closure* of GF(p).  This gives 'compatible embeddings' the very simple meaning of 'inclusions within an algebraic closure'.\n\nSuch an algebraic closure could be implemented in different ways, for example via (pseudo-)Conway polynomials; algebraic closures of GF(p) resulting from different methods would be non-canonically isomorphic.  There might be a default choice that could change in the future, and the user should be able to specify which algebraic closure should be taken.\n\nHere is how I would hope a hypothetical future Sage session to look like:\n\n\n```\nsage: p = 5\nsage: Fpbar = GF(p).algebraic_closure()\nsage: Fpbar\nAlgebraic closure of Finite Field of size 5\nsage: Fa = GF(p^2, 'a')\nsage: Fa\nFinite field in a of size 5^2\nsage: is_subfield(Fa, Fpbar)\nFalse\nsage: Fb = GF(p^2)\nSubfield of size 5^2 of Algebraic closure of Finite Field of size 5\nsage: is_subfield(Fb, Fpbar)\nTrue\nsage: type(Fpbar)\n<class 'sage.rings.AlgebraicClosureFiniteField_pseudo_conway'>\n```\n\nWould something like this be easy to achieve once this ticket has been implemented?",
    "created_at": "2013-06-26T12:16:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8335#issuecomment-74367",
    "user": "pbruin"
}
```

Replying to [comment:72 jpflori]:
> Beware that the last patch which contains my modification to the two original patches by David changes quite a lot of thing.
> In particular, I think that with it modulus contains the real modulus as well and I use additional attributes to check for pseudo-Conway construction.

OK, I'll try to find out if and how my ideas about making the choice of polynomial independently of the finite field implementation can be harmonised with your patch.  At first sight there does not seem to be a huge clash.  I am mostly worried about the use of strings like 'conwayz' as a modulus, which really seems to be overloading this parameter too much.

> Also note that the real nice addition of this patch is mainly the compatible embeddings.

I agree that this is a very desirable thing to have, and it is also nice to be able to simply type ``F = GF(p<sup>n</sup>)`` without having to care about variable names and embeddings.  I do think it is good to think carefully about how exactly to accomplish this.

In particular, I am not sure if it is wise to say in the documentation/specification that this compatibility is achieved using (pseudo-)Conway polynomials, since different implementations are imaginable.  I am thinking of the standard models for finite fields by Lenstra and de Smit, which are constructed in a way that does not seem to be related to Conway polynomials.

From a conceptual point of view, it is desirable that GF(p<sup>n</sup>) without any arguments should refer to the unique subfield of cardinality p<sup>n</sup> *inside a chosen algebraic closure* of GF(p).  This gives 'compatible embeddings' the very simple meaning of 'inclusions within an algebraic closure'.

Such an algebraic closure could be implemented in different ways, for example via (pseudo-)Conway polynomials; algebraic closures of GF(p) resulting from different methods would be non-canonically isomorphic.  There might be a default choice that could change in the future, and the user should be able to specify which algebraic closure should be taken.

Here is how I would hope a hypothetical future Sage session to look like:


```
sage: p = 5
sage: Fpbar = GF(p).algebraic_closure()
sage: Fpbar
Algebraic closure of Finite Field of size 5
sage: Fa = GF(p^2, 'a')
sage: Fa
Finite field in a of size 5^2
sage: is_subfield(Fa, Fpbar)
False
sage: Fb = GF(p^2)
Subfield of size 5^2 of Algebraic closure of Finite Field of size 5
sage: is_subfield(Fb, Fpbar)
True
sage: type(Fpbar)
<class 'sage.rings.AlgebraicClosureFiniteField_pseudo_conway'>
```

Would something like this be easy to achieve once this ticket has been implemented?



---

archive/issue_comments_074368.json:
```json
{
    "body": "Replying to [comment:73 pbruin]:\n> Replying to [comment:72 jpflori]:\n> > Beware that the last patch which contains my modification to the two original patches by David changes quite a lot of thing.\n> > In particular, I think that with it modulus contains the real modulus as well and I use additional attributes to check for pseudo-Conway construction.\n> \n> OK, I'll try to find out if and how my ideas about making the choice of polynomial independently of the finite field implementation can be harmonised with your patch.  At first sight there does not seem to be a huge clash.  I am mostly worried about the use of strings like 'conwayz' as a modulus, which really seems to be overloading this parameter too much.\n> \n> > Also note that the real nice addition of this patch is mainly the compatible embeddings.\n> \n> I agree that this is a very desirable thing to have, and it is also nice to be able to simply type ``F = GF(p<sup>n</sup>)`` without having to care about variable names and embeddings.  I do think it is good to think carefully about how exactly to accomplish this.\nAgreed.\nBut it just happened I stumled upon this ticket which already looked usable (and was two years old) and thought \"oh, let's already get this in; later on we can design better constructions of compatible embeddings and get something more general and fast\".\nSo I decided to postpone the design of a cool and fast system in #8751 and only deal with \"lattices using (pseudo) Conway polynomials\" here.\nIt's better to have something than nothing.\n> \n> In particular, I am not sure if it is wise to say in the documentation/specification that this compatibility is achieved using (pseudo-)Conway polynomials, since different implementations are imaginable.  I am thinking of the standard models for finite fields by Lenstra and de Smit, which are constructed in a way that does not seem to be related to Conway polynomials.\n> \nI completely agree that using Conway polynomials is a no go as soon as you quit fields of small cardinalities.\nI've met Eric Rains who participated in the Magma implementation (or at least the algos behind it) and he was nice enough to share with me a draft describing the algos used.\n\nDe Feo and Schost and others are also producing nice paper on how to build p- or l-adic towers of finite fields.\nWhat is very nice is that they avoid linear algebra (what Magma may not completely do).\n> From a conceptual point of view, it is desirable that GF(p<sup>n</sup>) without any arguments should refer to the unique subfield of cardinality p<sup>n</sup> *inside a chosen algebraic closure* of GF(p).  This gives 'compatible embeddings' the very simple meaning of 'inclusions within an algebraic closure'.\n> \n> Such an algebraic closure could be implemented in different ways, for example via (pseudo-)Conway polynomials; algebraic closures of GF(p) resulting from different methods would be non-canonically isomorphic.  There might be a default choice that could change in the future, and the user should be able to specify which algebraic closure should be taken.\n> \nI agree, so it makes sense to have a pseudo Conway implementation and other ones later.\n> Here is how I would hope a hypothetical future Sage session to look like:\n> \n> {{{\n> sage: p = 5\n> sage: Fpbar = GF(p).algebraic_closure()\n> sage: Fpbar\n> Algebraic closure of Finite Field of size 5\n> sage: Fa = GF(p^2, 'a')\n> sage: Fa\n> Finite field in a of size 5^2\n> sage: is_subfield(Fa, Fpbar)\n> False\n> sage: Fb = GF(p^2)\n> Subfield of size 5^2 of Algebraic closure of Finite Field of size 5\n> sage: is_subfield(Fb, Fpbar)\n> True\n> sage: type(Fpbar)\n> <class 'sage.rings.AlgebraicClosureFiniteField_pseudo_conway'>\n> }}}\n> Would something like this be easy to achieve once this ticket has been implemented?",
    "created_at": "2013-06-26T12:58:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8335#issuecomment-74368",
    "user": "jpflori"
}
```

Replying to [comment:73 pbruin]:
> Replying to [comment:72 jpflori]:
> > Beware that the last patch which contains my modification to the two original patches by David changes quite a lot of thing.
> > In particular, I think that with it modulus contains the real modulus as well and I use additional attributes to check for pseudo-Conway construction.
> 
> OK, I'll try to find out if and how my ideas about making the choice of polynomial independently of the finite field implementation can be harmonised with your patch.  At first sight there does not seem to be a huge clash.  I am mostly worried about the use of strings like 'conwayz' as a modulus, which really seems to be overloading this parameter too much.
> 
> > Also note that the real nice addition of this patch is mainly the compatible embeddings.
> 
> I agree that this is a very desirable thing to have, and it is also nice to be able to simply type ``F = GF(p<sup>n</sup>)`` without having to care about variable names and embeddings.  I do think it is good to think carefully about how exactly to accomplish this.
Agreed.
But it just happened I stumled upon this ticket which already looked usable (and was two years old) and thought "oh, let's already get this in; later on we can design better constructions of compatible embeddings and get something more general and fast".
So I decided to postpone the design of a cool and fast system in #8751 and only deal with "lattices using (pseudo) Conway polynomials" here.
It's better to have something than nothing.
> 
> In particular, I am not sure if it is wise to say in the documentation/specification that this compatibility is achieved using (pseudo-)Conway polynomials, since different implementations are imaginable.  I am thinking of the standard models for finite fields by Lenstra and de Smit, which are constructed in a way that does not seem to be related to Conway polynomials.
> 
I completely agree that using Conway polynomials is a no go as soon as you quit fields of small cardinalities.
I've met Eric Rains who participated in the Magma implementation (or at least the algos behind it) and he was nice enough to share with me a draft describing the algos used.

De Feo and Schost and others are also producing nice paper on how to build p- or l-adic towers of finite fields.
What is very nice is that they avoid linear algebra (what Magma may not completely do).
> From a conceptual point of view, it is desirable that GF(p<sup>n</sup>) without any arguments should refer to the unique subfield of cardinality p<sup>n</sup> *inside a chosen algebraic closure* of GF(p).  This gives 'compatible embeddings' the very simple meaning of 'inclusions within an algebraic closure'.
> 
> Such an algebraic closure could be implemented in different ways, for example via (pseudo-)Conway polynomials; algebraic closures of GF(p) resulting from different methods would be non-canonically isomorphic.  There might be a default choice that could change in the future, and the user should be able to specify which algebraic closure should be taken.
> 
I agree, so it makes sense to have a pseudo Conway implementation and other ones later.
> Here is how I would hope a hypothetical future Sage session to look like:
> 
> {{{
> sage: p = 5
> sage: Fpbar = GF(p).algebraic_closure()
> sage: Fpbar
> Algebraic closure of Finite Field of size 5
> sage: Fa = GF(p^2, 'a')
> sage: Fa
> Finite field in a of size 5^2
> sage: is_subfield(Fa, Fpbar)
> False
> sage: Fb = GF(p^2)
> Subfield of size 5^2 of Algebraic closure of Finite Field of size 5
> sage: is_subfield(Fb, Fpbar)
> True
> sage: type(Fpbar)
> <class 'sage.rings.AlgebraicClosureFiniteField_pseudo_conway'>
> }}}
> Would something like this be easy to achieve once this ticket has been implemented?



---

archive/issue_comments_074369.json:
```json
{
    "body": "I started to look at the patches, but was immediately struck by a problem that has nothing to do with finite fields.  In `QuotientFunctor._apply_functor`, the functor R -> R/IR (where I is an ideal of the base ring) to arbitrary rings.  This makes perfect sense for any R; you just happen to get the zero ring when IR = R.  The existing behaviour is certainly correct (although it is debatable whether the zero ring should be represented as `Integers(1)`).  Why would you want to raise an exception if R is a field?",
    "created_at": "2013-06-26T13:08:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8335#issuecomment-74369",
    "user": "pbruin"
}
```

I started to look at the patches, but was immediately struck by a problem that has nothing to do with finite fields.  In `QuotientFunctor._apply_functor`, the functor R -> R/IR (where I is an ideal of the base ring) to arbitrary rings.  This makes perfect sense for any R; you just happen to get the zero ring when IR = R.  The existing behaviour is certainly correct (although it is debatable whether the zero ring should be represented as `Integers(1)`).  Why would you want to raise an exception if R is a field?



---

archive/issue_comments_074370.json:
```json
{
    "body": "I think it was the historical Sage behavior until some recent ticket (don't really remember, you should be able to devise which one by looking at the hg log).\n\nI also agree returning the zero ring would be a better thing to do.\nBut then it breaks a bunch of generic constructions in Sage such as polynomial rings over {0} and quotients of it...\nSee http://trac.sagemath.org/sage_trac/ticket/8335#comment:24 and the few following comments (in case you manage to make some sense of my lonely rants).",
    "created_at": "2013-06-26T13:18:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8335#issuecomment-74370",
    "user": "jpflori"
}
```

I think it was the historical Sage behavior until some recent ticket (don't really remember, you should be able to devise which one by looking at the hg log).

I also agree returning the zero ring would be a better thing to do.
But then it breaks a bunch of generic constructions in Sage such as polynomial rings over {0} and quotients of it...
See http://trac.sagemath.org/sage_trac/ticket/8335#comment:24 and the few following comments (in case you manage to make some sense of my lonely rants).



---

archive/issue_comments_074371.json:
```json
{
    "body": "Replying to [comment:76 jpflori]:\n> I think it was the historical Sage behavior until some recent ticket (don't really remember, you should be able to devise which one by looking at the hg log).\n\nIn the comments it says that the behaviour used to be to return the integer 0 (?!), and that this was corrected in #9138.  Now that the current implementation is correct, it would be very bad to change something fundamental like this just to make new patches work.\n\n> I also agree returning the zero ring would be a better thing to do.\n> But then it breaks a bunch of generic constructions in Sage such as polynomial rings over {0} and quotients of it...\n> See http://trac.sagemath.org/sage_trac/ticket/8335#comment:24 and the few following comments (in case you manage to make some sense of my lonely rants).\n\nThen it seems to me that the generic constructions should be fixed.  Until then, any new code should take care that it does not use these constructions in cases where they fail.",
    "created_at": "2013-06-26T13:35:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8335#issuecomment-74371",
    "user": "pbruin"
}
```

Replying to [comment:76 jpflori]:
> I think it was the historical Sage behavior until some recent ticket (don't really remember, you should be able to devise which one by looking at the hg log).

In the comments it says that the behaviour used to be to return the integer 0 (?!), and that this was corrected in #9138.  Now that the current implementation is correct, it would be very bad to change something fundamental like this just to make new patches work.

> I also agree returning the zero ring would be a better thing to do.
> But then it breaks a bunch of generic constructions in Sage such as polynomial rings over {0} and quotients of it...
> See http://trac.sagemath.org/sage_trac/ticket/8335#comment:24 and the few following comments (in case you manage to make some sense of my lonely rants).

Then it seems to me that the generic constructions should be fixed.  Until then, any new code should take care that it does not use these constructions in cases where they fail.



---

archive/issue_comments_074372.json:
```json
{
    "body": "Replying to [comment:77 pbruin]:\n> Replying to [comment:76 jpflori]:\n> > I think it was the historical Sage behavior until some recent ticket (don't really remember, you should be able to devise which one by looking at the hg log).\n> \n> In the comments it says that the behaviour used to be to return the integer 0 (?!), and that this was corrected in #9138.  Now that the current implementation is correct, it would be very bad to change something fundamental like this just to make new patches work.\n> \n> > I also agree returning the zero ring would be a better thing to do.\n> > But then it breaks a bunch of generic constructions in Sage such as polynomial rings over {0} and quotients of it...\n> > See http://trac.sagemath.org/sage_trac/ticket/8335#comment:24 and the few following comments (in case you manage to make some sense of my lonely rants).\n> \n> Then it seems to me that the generic constructions should be fixed.  Until then, any new code should \ntake care that it does not use these constructions in cases where they fail.\nOf course.\nBut avoiding the coercion model is not that easy.\n\nI'll give it a shot, but I cannot promise to come up with anything working.\nObviously I would have done that earlier if it was really easy.",
    "created_at": "2013-06-26T14:04:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8335#issuecomment-74372",
    "user": "jpflori"
}
```

Replying to [comment:77 pbruin]:
> Replying to [comment:76 jpflori]:
> > I think it was the historical Sage behavior until some recent ticket (don't really remember, you should be able to devise which one by looking at the hg log).
> 
> In the comments it says that the behaviour used to be to return the integer 0 (?!), and that this was corrected in #9138.  Now that the current implementation is correct, it would be very bad to change something fundamental like this just to make new patches work.
> 
> > I also agree returning the zero ring would be a better thing to do.
> > But then it breaks a bunch of generic constructions in Sage such as polynomial rings over {0} and quotients of it...
> > See http://trac.sagemath.org/sage_trac/ticket/8335#comment:24 and the few following comments (in case you manage to make some sense of my lonely rants).
> 
> Then it seems to me that the generic constructions should be fixed.  Until then, any new code should 
take care that it does not use these constructions in cases where they fail.
Of course.
But avoiding the coercion model is not that easy.

I'll give it a shot, but I cannot promise to come up with anything working.
Obviously I would have done that earlier if it was really easy.



---

archive/issue_comments_074373.json:
```json
{
    "body": "In fact I think that putting back the correct behavior gives no problems and I added all needed fixes to make it work.\n\nThe real problem was that the quotient functor was applied before the fraction field one or the other way around and you always ended up working in the trivial ring.\nSo the easy way was raising an error.\nBut now the functors are applied in a more sensible it should not be a problem.\n\nI'll upload a fixed patch when I make sure no tests fail.",
    "created_at": "2013-06-26T16:00:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8335#issuecomment-74373",
    "user": "jpflori"
}
```

In fact I think that putting back the correct behavior gives no problems and I added all needed fixes to make it work.

The real problem was that the quotient functor was applied before the fraction field one or the other way around and you always ended up working in the trivial ring.
So the easy way was raising an error.
But now the functors are applied in a more sensible it should not be a problem.

I'll upload a fixed patch when I make sure no tests fail.



---

archive/issue_comments_074374.json:
```json
{
    "body": "Attachment\n\nI have some failing tests on top of 5.11.b3 but they seem completely unrelated (something with get_test_shell() and I did not test a vanilla install, so they were surely there without these patches).",
    "created_at": "2013-06-26T16:14:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8335#issuecomment-74374",
    "user": "jpflori"
}
```

Attachment

I have some failing tests on top of 5.11.b3 but they seem completely unrelated (something with get_test_shell() and I did not test a vanilla install, so they were surely there without these patches).



---

archive/issue_comments_074375.json:
```json
{
    "body": "Continuing the discussion from #13214; in the context of my remark\n\n>> there should probably be two categories into which a finite field can be put:\n>> - the category of all finite fields. In this category, between any two objects there are either several morphisms or none at all, but no canonical one.\n>> - the category of finite subfields of a given algebraic closure of Fp. In this category there is at most one morphism beteen any two objects, namely the inclusion qua subfields of the given algebraic closure.\n\nJean-Pierre Flori wrote (referring to the second option)\n\n> #8335 provides such an imlementation, though it not really practical for large fields and there is no proper categorical framework as you suggest.\n> This framework could be implemented in an independent ticket (and should if we want to be able to merge some tickets in a finite amount of time).\n\nCertainly; both this ticket and #13214 are already large enough.  The question is whether (a draft of) a categorical framework (i.e. algebraic closure of **F**<sub>*p*</sub>) should be made first, or whether the new code from this ticket should be inserted into the current framework (which implements the first of the two categories) and be moved to a new framework as soon as we have it.\n\nI would personally prefer the first option to keep things better packaged; this patch seems to make (pseudo-)Conway polynomials pop up in many different places, and moving them all to one place would require another intrusive Trac ticket later.",
    "created_at": "2013-06-26T16:44:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8335#issuecomment-74375",
    "user": "pbruin"
}
```

Continuing the discussion from #13214; in the context of my remark

>> there should probably be two categories into which a finite field can be put:
>> - the category of all finite fields. In this category, between any two objects there are either several morphisms or none at all, but no canonical one.
>> - the category of finite subfields of a given algebraic closure of Fp. In this category there is at most one morphism beteen any two objects, namely the inclusion qua subfields of the given algebraic closure.

Jean-Pierre Flori wrote (referring to the second option)

> #8335 provides such an imlementation, though it not really practical for large fields and there is no proper categorical framework as you suggest.
> This framework could be implemented in an independent ticket (and should if we want to be able to merge some tickets in a finite amount of time).

Certainly; both this ticket and #13214 are already large enough.  The question is whether (a draft of) a categorical framework (i.e. algebraic closure of **F**<sub>*p*</sub>) should be made first, or whether the new code from this ticket should be inserted into the current framework (which implements the first of the two categories) and be moved to a new framework as soon as we have it.

I would personally prefer the first option to keep things better packaged; this patch seems to make (pseudo-)Conway polynomials pop up in many different places, and moving them all to one place would require another intrusive Trac ticket later.



---

archive/issue_comments_074376.json:
```json
{
    "body": "Replying to [comment:81 pbruin]:\n> I would personally prefer the first option to keep things better packaged; this patch seems to make (pseudo-)Conway polynomials pop up in many different places, and moving them all to one place would require another intrusive Trac ticket later.\nAs far as functionalities are concerned, remember that Sage currently does not support \n\n```\nK = GF(p^n)\n```\n\nSo pseudo Conway polynomials never appear where they did not use to.\nIf you issue the command line which is currently supported:\n\n```\nK.<a> = GF(p^n)\n```\n\nyou will get the exact same behavior as before, unless he specifies modulus=\"conway\" and wants an extension of too large cardinality; maybe that should be changed back.\n\nNevertheless I agree that a user coming from Magma where\n\n```\nK := GF(p, n);\n```\n\nworks might be confused...\nThough the user might although expect embeddings of finite fields to work out of the box.\n\nBut as I just realized I guess your concern is about the dissemination of code.\nFrom what I see, apart from code in finite_field_base.py, changes to specific finite field implementations mostly consists in replacing the part about Conway polynomials and tweak it to work with pseudo-Conway ones as well.\nNonetheless it's true that properly moving all of that later will be intrusive.\n\nBut what about plain Conway polynomials? Shouldn't that be moved as well?\nOr do we consider they are standard enough to belong in the FiniteFields() category?\nBut if they do it would be a waste not to use automagically the fact that they provide simple embeddings into each other, wouldn't it? though it would make the separation between the plain finite fields and subfields of a given algebraic closure blurrier.\n\n(As you can guess, I'd prefer to get this merged first especially because I hate seeing functional code bitrotting for years on trac, but I get your point :))",
    "created_at": "2013-06-26T17:11:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8335#issuecomment-74376",
    "user": "jpflori"
}
```

Replying to [comment:81 pbruin]:
> I would personally prefer the first option to keep things better packaged; this patch seems to make (pseudo-)Conway polynomials pop up in many different places, and moving them all to one place would require another intrusive Trac ticket later.
As far as functionalities are concerned, remember that Sage currently does not support 

```
K = GF(p^n)
```

So pseudo Conway polynomials never appear where they did not use to.
If you issue the command line which is currently supported:

```
K.<a> = GF(p^n)
```

you will get the exact same behavior as before, unless he specifies modulus="conway" and wants an extension of too large cardinality; maybe that should be changed back.

Nevertheless I agree that a user coming from Magma where

```
K := GF(p, n);
```

works might be confused...
Though the user might although expect embeddings of finite fields to work out of the box.

But as I just realized I guess your concern is about the dissemination of code.
From what I see, apart from code in finite_field_base.py, changes to specific finite field implementations mostly consists in replacing the part about Conway polynomials and tweak it to work with pseudo-Conway ones as well.
Nonetheless it's true that properly moving all of that later will be intrusive.

But what about plain Conway polynomials? Shouldn't that be moved as well?
Or do we consider they are standard enough to belong in the FiniteFields() category?
But if they do it would be a waste not to use automagically the fact that they provide simple embeddings into each other, wouldn't it? though it would make the separation between the plain finite fields and subfields of a given algebraic closure blurrier.

(As you can guess, I'd prefer to get this merged first especially because I hate seeing functional code bitrotting for years on trac, but I get your point :))



---

archive/issue_comments_074377.json:
```json
{
    "body": "Replying to [comment:82 jpflori]:\n\n> As far as functionalities are concerned, remember that Sage currently does not support \n> {{{\n> K = GF(p^n)\n> }}}\n> So pseudo Conway polynomials never appear where they did not use to.\n> If you issue the command line which is currently supported:\n> {{{\n> K.<a> = GF(p^n)\n> }}}\n> you will get the exact same behavior as before, unless he specifies modulus=\"conway\" and wants an extension of too large cardinality; maybe that should be changed back.\n\nDeciding what exactly `GF(p^n)` should mean (if it should mean anything at all) is an important design decision, and it is not at all obvious that Sage should make the same choice as Magma.  Probably it is better not to make this decision in this ticket, which already adds a lot of code.  Besides, letting an important change of behaviour depend whether the user specify a variable name or not sounds like a risky idea.  \n\n> But what about plain Conway polynomials? Shouldn't that be moved as well?\n> Or do we consider they are standard enough to belong in the FiniteFields() category?\n\nThey certainly belong to the general finite fields code, but not in any specific implementation, in my opinion.  In fact, the goal of the (by now 2) patches that I'm about to post is as follows:\n\n- write a method `PolynomialRing_dense_finite_field.irreducible_element` (somewhat surprisingly the class did not exist yet) to generate an irreducible polynomial in that polynomial ring, allowing the user to optionally specify an algorithm (Adleman-Lenstra, Conway, random, lexicographically first, sparse);\n\n- modify the `FiniteField` constructor to call this algorithm if the `modulus` argument is a string or `None`, and always pass an actual polynomial to the implementation class.\n\nFor backward compatibility (unpickling), the existing implementations will continue to accept string values for the parameter `modulus`, but new ones (such as the new PARI interface, see #12142) won't have to.  The idea is that the specific implementations should \"concentrate on doing their job\", and things related to magic values of `modulus` should be in only one place.\n\n> But if they do it would be a waste not to use automagically the fact that they provide simple embeddings into each other, wouldn't it?\n\nAs I see it, that should depend on whether you are in the category of all finite fields or in the category of subfields of an algebraic closure of **F**<sub>*p*</sub>.\n\n> (As you can guess, I'd prefer to get this merged first especially because I hate seeing functional code bitrotting for years on trac, but I get your point :))\n\nOf course I understand that you want to see this finally appear in Sage, and I agree that it is a shame that Sage could have had something like this for years and still doesn't.  I guess it will be easier if this big ticket is split into smaller pieces.  It tries to do many rather different things at once: implement pseudo-Conway polynomials, adapt the construction of finite fields to use these, implement automatic coercion between the resulting fields, give a meaning to `GF(p^n)`, and in the process add some new methods to polynomial elements.  This makes it harder than necessary to understand and to review.",
    "created_at": "2013-06-26T23:20:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8335#issuecomment-74377",
    "user": "pbruin"
}
```

Replying to [comment:82 jpflori]:

> As far as functionalities are concerned, remember that Sage currently does not support 
> {{{
> K = GF(p^n)
> }}}
> So pseudo Conway polynomials never appear where they did not use to.
> If you issue the command line which is currently supported:
> {{{
> K.<a> = GF(p^n)
> }}}
> you will get the exact same behavior as before, unless he specifies modulus="conway" and wants an extension of too large cardinality; maybe that should be changed back.

Deciding what exactly `GF(p^n)` should mean (if it should mean anything at all) is an important design decision, and it is not at all obvious that Sage should make the same choice as Magma.  Probably it is better not to make this decision in this ticket, which already adds a lot of code.  Besides, letting an important change of behaviour depend whether the user specify a variable name or not sounds like a risky idea.  

> But what about plain Conway polynomials? Shouldn't that be moved as well?
> Or do we consider they are standard enough to belong in the FiniteFields() category?

They certainly belong to the general finite fields code, but not in any specific implementation, in my opinion.  In fact, the goal of the (by now 2) patches that I'm about to post is as follows:

- write a method `PolynomialRing_dense_finite_field.irreducible_element` (somewhat surprisingly the class did not exist yet) to generate an irreducible polynomial in that polynomial ring, allowing the user to optionally specify an algorithm (Adleman-Lenstra, Conway, random, lexicographically first, sparse);

- modify the `FiniteField` constructor to call this algorithm if the `modulus` argument is a string or `None`, and always pass an actual polynomial to the implementation class.

For backward compatibility (unpickling), the existing implementations will continue to accept string values for the parameter `modulus`, but new ones (such as the new PARI interface, see #12142) won't have to.  The idea is that the specific implementations should "concentrate on doing their job", and things related to magic values of `modulus` should be in only one place.

> But if they do it would be a waste not to use automagically the fact that they provide simple embeddings into each other, wouldn't it?

As I see it, that should depend on whether you are in the category of all finite fields or in the category of subfields of an algebraic closure of **F**<sub>*p*</sub>.

> (As you can guess, I'd prefer to get this merged first especially because I hate seeing functional code bitrotting for years on trac, but I get your point :))

Of course I understand that you want to see this finally appear in Sage, and I agree that it is a shame that Sage could have had something like this for years and still doesn't.  I guess it will be easier if this big ticket is split into smaller pieces.  It tries to do many rather different things at once: implement pseudo-Conway polynomials, adapt the construction of finite fields to use these, implement automatic coercion between the resulting fields, give a meaning to `GF(p^n)`, and in the process add some new methods to polynomial elements.  This makes it harder than necessary to understand and to review.



---

archive/issue_comments_074378.json:
```json
{
    "body": "Replying to [comment:83 pbruin]:\n\nThis discussion looks like the dear old dichotomy between quick feature integration and long specification design. \n\nHaving some kind of support for lattices of finite fields has been a long standing request. I agree with pbruin that a better interface between generic finite fields and their actual implementation would be beneficial. But this ticket is ready for review, while pbruin's is not. Would it be that hard to adapt pbruin's or any other interface if this ticket is merged? I'm willing to give positive review to this ticket, if it stands some more testing, and it doesn't mess too much with #12142. \n\nI'm not convinced that the interface can be decided independently of the actual algorithms. Magma's interface is engineered around the fact that constructing fields is fast, but constructing the embeddings is slow (hence the Embed function, which must explicitly be called by the user). If Sage ends up having a different construction (e.g., De Smit-Lenstra lattices... although I've looked into it, and I don't think it is viable in general), I think the interface could be different.\n\nThere are many solutions to the compatibly embedded finite fields problem, no one being ideal. I'm more in favor of seeing them emerge in parallel, being developed in different tickets under different namespaces and APIs, rather than fixing the API now, and than realizing that it needs to be amended. Once a construction clearly stands out, then we can thrash it upon the user as the default ``GF(p<sup>n</sup>)`` construction (ok, this ticket is already thrashing, but it has the merit of being the first one!).",
    "created_at": "2013-06-27T02:55:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8335#issuecomment-74378",
    "user": "defeo"
}
```

Replying to [comment:83 pbruin]:

This discussion looks like the dear old dichotomy between quick feature integration and long specification design. 

Having some kind of support for lattices of finite fields has been a long standing request. I agree with pbruin that a better interface between generic finite fields and their actual implementation would be beneficial. But this ticket is ready for review, while pbruin's is not. Would it be that hard to adapt pbruin's or any other interface if this ticket is merged? I'm willing to give positive review to this ticket, if it stands some more testing, and it doesn't mess too much with #12142. 

I'm not convinced that the interface can be decided independently of the actual algorithms. Magma's interface is engineered around the fact that constructing fields is fast, but constructing the embeddings is slow (hence the Embed function, which must explicitly be called by the user). If Sage ends up having a different construction (e.g., De Smit-Lenstra lattices... although I've looked into it, and I don't think it is viable in general), I think the interface could be different.

There are many solutions to the compatibly embedded finite fields problem, no one being ideal. I'm more in favor of seeing them emerge in parallel, being developed in different tickets under different namespaces and APIs, rather than fixing the API now, and than realizing that it needs to be amended. Once a construction clearly stands out, then we can thrash it upon the user as the default ``GF(p<sup>n</sup>)`` construction (ok, this ticket is already thrashing, but it has the merit of being the first one!).



---

archive/issue_comments_074379.json:
```json
{
    "body": "Replying to [comment:84 defeo]:\n> Replying to [comment:83 pbruin]:\n> \n> This discussion looks like the dear old dichotomy between quick feature integration and long specification design. \n\nNot quite; I am not at all advocating long specification design, and quick integration of new features (which I am all for) is in fact easier if they are smaller and don't intrude in places where they don't have to.\n\n> Having some kind of support for lattices of finite fields has been a long standing request. I agree with pbruin that a better interface between generic finite fields and their actual implementation would be beneficial. But this ticket is ready for review, while pbruin's is not.\n\nThe part that is relevant for this ticket is now ready for review: see #14832 and #14833.\n\n> Would it be that hard to adapt pbruin's or any other interface if this ticket is merged? I'm willing to give positive review to this ticket, if it stands some more testing, and it doesn't mess too much with #12142. \n\nI am actually in favour of quickly solving the main things that this ticket does (implementing pseudo-Conway polynomials and coercion between different finite fields).  I just think it shouldn't add more code to the finite fields implementations (Givaro, PARI etc.), and should not (or at least not yet) fix a meaning for `GF(p^n)`.",
    "created_at": "2013-06-27T07:56:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8335#issuecomment-74379",
    "user": "pbruin"
}
```

Replying to [comment:84 defeo]:
> Replying to [comment:83 pbruin]:
> 
> This discussion looks like the dear old dichotomy between quick feature integration and long specification design. 

Not quite; I am not at all advocating long specification design, and quick integration of new features (which I am all for) is in fact easier if they are smaller and don't intrude in places where they don't have to.

> Having some kind of support for lattices of finite fields has been a long standing request. I agree with pbruin that a better interface between generic finite fields and their actual implementation would be beneficial. But this ticket is ready for review, while pbruin's is not.

The part that is relevant for this ticket is now ready for review: see #14832 and #14833.

> Would it be that hard to adapt pbruin's or any other interface if this ticket is merged? I'm willing to give positive review to this ticket, if it stands some more testing, and it doesn't mess too much with #12142. 

I am actually in favour of quickly solving the main things that this ticket does (implementing pseudo-Conway polynomials and coercion between different finite fields).  I just think it shouldn't add more code to the finite fields implementations (Givaro, PARI etc.), and should not (or at least not yet) fix a meaning for `GF(p^n)`.



---

archive/issue_comments_074380.json:
```json
{
    "body": "Ok, so I'll be the nice guy and try to rebase this ticket on top of your tickets.",
    "created_at": "2013-06-27T08:11:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8335#issuecomment-74380",
    "user": "jpflori"
}
```

Ok, so I'll be the nice guy and try to rebase this ticket on top of your tickets.



---

archive/issue_comments_074381.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2013-06-27T08:11:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8335#issuecomment-74381",
    "user": "jpflori"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_074382.json:
```json
{
    "body": "Changing keywords from \"days49\" to \"days49 sd51\".",
    "created_at": "2013-07-13T21:05:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8335#issuecomment-74382",
    "user": "pbruin"
}
```

Changing keywords from "days49" to "days49 sd51".



---

archive/issue_comments_074383.json:
```json
{
    "body": "Replying to [comment:86 jpflori]:\n> Ok, so I'll be the nice guy and try to rebase this ticket on top of your tickets.\nWonderful; these (#12142 and dependencies, maybe also #14888) should now be fairly stable.",
    "created_at": "2013-07-13T21:05:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8335#issuecomment-74383",
    "user": "pbruin"
}
```

Replying to [comment:86 jpflori]:
> Ok, so I'll be the nice guy and try to rebase this ticket on top of your tickets.
Wonderful; these (#12142 and dependencies, maybe also #14888) should now be fairly stable.



---

archive/issue_comments_074384.json:
```json
{
    "body": "I've begun rebasing, cleaning and splitting in a better way the patches here.\n\nI have one question: in several finite field constructors based on a given implementation (let's say FiniteField_givaro), you can still pass the \"modulus\" parameter as a string and the routine corresponding to the given type of modulus is called.\nIMHO this kind of defeats what Peter tried to do in #14832 and #14833 (though it predates these patcehs of course).\nAny objection to change this behavior and instead more or less call the new irreducible_element function with the appropriate \"algorithm\" parameter?",
    "created_at": "2013-07-18T14:18:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8335#issuecomment-74384",
    "user": "jpflori"
}
```

I've begun rebasing, cleaning and splitting in a better way the patches here.

I have one question: in several finite field constructors based on a given implementation (let's say FiniteField_givaro), you can still pass the "modulus" parameter as a string and the routine corresponding to the given type of modulus is called.
IMHO this kind of defeats what Peter tried to do in #14832 and #14833 (though it predates these patcehs of course).
Any objection to change this behavior and instead more or less call the new irreducible_element function with the appropriate "algorithm" parameter?



---

archive/issue_comments_074385.json:
```json
{
    "body": "(This will potentially introduce a slow down in some constructors, e.g. in finite_field_ntl_gf2e, but this can't really be helped.)",
    "created_at": "2013-07-18T14:27:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8335#issuecomment-74385",
    "user": "jpflori"
}
```

(This will potentially introduce a slow down in some constructors, e.g. in finite_field_ntl_gf2e, but this can't really be helped.)



---

archive/issue_comments_074386.json:
```json
{
    "body": "Replying to [comment:88 jpflori]:\n> I've begun rebasing, cleaning and splitting in a better way the patches here.\n> \n> I have one question: in several finite field constructors based on a given implementation (let's say FiniteField_givaro), you can still pass the \"modulus\" parameter as a string and the routine corresponding to the given type of modulus is called.\n> IMHO this kind of defeats what Peter tried to do in #14832 and #14833 (though it predates these patcehs of course).\n> Any objection to change this behavior and instead more or less call the new irreducible_element function with the appropriate \"algorithm\" parameter?\n\nNo, I have no objection to a more unified way of generating the modulus.",
    "created_at": "2013-07-18T22:36:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8335#issuecomment-74386",
    "user": "roed"
}
```

Replying to [comment:88 jpflori]:
> I've begun rebasing, cleaning and splitting in a better way the patches here.
> 
> I have one question: in several finite field constructors based on a given implementation (let's say FiniteField_givaro), you can still pass the "modulus" parameter as a string and the routine corresponding to the given type of modulus is called.
> IMHO this kind of defeats what Peter tried to do in #14832 and #14833 (though it predates these patcehs of course).
> Any objection to change this behavior and instead more or less call the new irreducible_element function with the appropriate "algorithm" parameter?

No, I have no objection to a more unified way of generating the modulus.



---

archive/issue_comments_074387.json:
```json
{
    "body": "Ok so let's go this way.\n\nAs I'll be cut from the internet next week while the workshop in Leiden is taking place and I'm not sure what I'll be able to achieve today, here are some hints on what I plan to do.\nOf course feel free to do something completely different and merge the ticket next week!\n\n* rebase David's first patch (PC polys construction) on top of Peter's patches and include the relevant fixes (i.e. those only related to Conway and pseudo-Conway polynomials construction) from the \"fixes\" patch I posted here, move all the conway and pseudo-conway construction stuff to a separate file (I feel two files, one for Conway, one for pseudo-Conway, would be overkill, but all that stuff currently in constructor.py seems too much), maybe use two algo names \"conway\" for using the database and pseudo-conway to use the new code (and still use the database when possible). With the current patches, the PCPT is stored into the finite field (so that its not garbage collected), that is not possible with the new way of building moduli, so we have to think of another way, maybe store it in the modulus itself... (though the polynomial does not really care it's pseudo-Conway whereas the FF does). I don't think modifying irreducible_element() to return more stuff would be a good idea, any other advice welcomed!\n* rebase David's second patch (coercion) on top of Peter's patches, include relevant fixes, do not define \"GF\" without names.\n* keep the design of the AlgebraicClosure stuff for later, note that it should not be too hard to move later to the new framework, much less hard than implementing FFs through templates as for the p-adics and polynomial rings :)",
    "created_at": "2013-07-19T09:13:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8335#issuecomment-74387",
    "user": "jpflori"
}
```

Ok so let's go this way.

As I'll be cut from the internet next week while the workshop in Leiden is taking place and I'm not sure what I'll be able to achieve today, here are some hints on what I plan to do.
Of course feel free to do something completely different and merge the ticket next week!

* rebase David's first patch (PC polys construction) on top of Peter's patches and include the relevant fixes (i.e. those only related to Conway and pseudo-Conway polynomials construction) from the "fixes" patch I posted here, move all the conway and pseudo-conway construction stuff to a separate file (I feel two files, one for Conway, one for pseudo-Conway, would be overkill, but all that stuff currently in constructor.py seems too much), maybe use two algo names "conway" for using the database and pseudo-conway to use the new code (and still use the database when possible). With the current patches, the PCPT is stored into the finite field (so that its not garbage collected), that is not possible with the new way of building moduli, so we have to think of another way, maybe store it in the modulus itself... (though the polynomial does not really care it's pseudo-Conway whereas the FF does). I don't think modifying irreducible_element() to return more stuff would be a good idea, any other advice welcomed!
* rebase David's second patch (coercion) on top of Peter's patches, include relevant fixes, do not define "GF" without names.
* keep the design of the AlgebraicClosure stuff for later, note that it should not be too hard to move later to the new framework, much less hard than implementing FFs through templates as for the p-adics and polynomial rings :)



---

archive/issue_comments_074388.json:
```json
{
    "body": "I found no time to work on this today, so I'll just post the very rough and incomplete patch I produced yesterday evening, not sure it is worth anything, but just in case you can apply it after applying [attachment:trac_8335-pseudo_conway-5.10.b3.patch] (note that hg will rant and you'll get three rejection files in sage/rings/finite_rings/, just push the new patch on top of that).\nNote it does not include anything from [attachment:trac_8335-fixes-5.11.b3.patch] yet.",
    "created_at": "2013-07-19T14:29:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8335#issuecomment-74388",
    "user": "jpflori"
}
```

I found no time to work on this today, so I'll just post the very rough and incomplete patch I produced yesterday evening, not sure it is worth anything, but just in case you can apply it after applying [attachment:trac_8335-pseudo_conway-5.10.b3.patch] (note that hg will rant and you'll get three rejection files in sage/rings/finite_rings/, just push the new patch on top of that).
Note it does not include anything from [attachment:trac_8335-fixes-5.11.b3.patch] yet.



---

archive/issue_comments_074389.json:
```json
{
    "body": "Attachment",
    "created_at": "2013-07-19T14:30:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8335#issuecomment-74389",
    "user": "jpflori"
}
```

Attachment



---

archive/issue_comments_074390.json:
```json
{
    "body": "OK, thanks.  To begin with we'll start by trying to understand better how these patches work.",
    "created_at": "2013-07-22T14:25:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8335#issuecomment-74390",
    "user": "pbruin"
}
```

OK, thanks.  To begin with we'll start by trying to understand better how these patches work.



---

archive/issue_comments_074391.json:
```json
{
    "body": "There are a few small problems with applying and testing this set of patches; I am now combining them into one patch that can be applied on top of 5.11.beta3 + (dependencies of this ticket) and that we can use as a starting point during Sage Days 51.",
    "created_at": "2013-07-23T12:55:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8335#issuecomment-74391",
    "user": "pbruin"
}
```

There are a few small problems with applying and testing this set of patches; I am now combining them into one patch that can be applied on top of 5.11.beta3 + (dependencies of this ticket) and that we can use as a starting point during Sage Days 51.



---

archive/issue_comments_074392.json:
```json
{
    "body": "I'm going to split the following parts off into separate tickets, which will be dependencies of this one:\n\n- the new squarefree decomposition code and the new `any_root` function;\n- the code for pseudo-Conway polynomials.\n\nThese will hopefully be relatively easy to review.  We can then concentrate on implementing coercion between finite fields in this ticket.",
    "created_at": "2013-07-23T14:43:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8335#issuecomment-74392",
    "user": "pbruin"
}
```

I'm going to split the following parts off into separate tickets, which will be dependencies of this one:

- the new squarefree decomposition code and the new `any_root` function;
- the code for pseudo-Conway polynomials.

These will hopefully be relatively easy to review.  We can then concentrate on implementing coercion between finite fields in this ticket.



---

archive/issue_comments_074393.json:
```json
{
    "body": "Once #14957 and #14958 are stable enough, the next step will be to update [attachment:trac_8335-finite_field_coerce-5.8.b0.patch] and [attachment:trac_8335-fixes-5.11.b3.patch\u200b], according to Jean-Pierre's plan from [http://trac.sagemath.org/ticket/8335#comment:91](http://trac.sagemath.org/ticket/8335#comment:91).",
    "created_at": "2013-07-23T15:47:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8335#issuecomment-74393",
    "user": "pbruin"
}
```

Once #14957 and #14958 are stable enough, the next step will be to update [attachment:trac_8335-finite_field_coerce-5.8.b0.patch] and [attachment:trac_8335-fixes-5.11.b3.patch​], according to Jean-Pierre's plan from [http://trac.sagemath.org/ticket/8335#comment:91](http://trac.sagemath.org/ticket/8335#comment:91).



---

archive/issue_comments_074394.json:
```json
{
    "body": "The patch [attachment:trac_8335_sd51.patch] contains the changes that remain after splitting off #14957 and #14958, and has been rebased on 5.11.beta3 + (dependencies of this ticket).\n\n```\nPatchbot: apply trac_8335_sd51.patch\n```\n",
    "created_at": "2013-07-24T14:22:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8335#issuecomment-74394",
    "user": "pbruin"
}
```

The patch [attachment:trac_8335_sd51.patch] contains the changes that remain after splitting off #14957 and #14958, and has been rebased on 5.11.beta3 + (dependencies of this ticket).

```
Patchbot: apply trac_8335_sd51.patch
```




---

archive/issue_comments_074395.json:
```json
{
    "body": "to work on during Sage Days 51",
    "created_at": "2013-07-25T07:27:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8335#issuecomment-74395",
    "user": "pbruin"
}
```

to work on during Sage Days 51



---

archive/issue_comments_074396.json:
```json
{
    "body": "Attachment\n\nunified, rebased and cleaned up",
    "created_at": "2013-07-29T11:48:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8335#issuecomment-74396",
    "user": "pbruin"
}
```

Attachment

unified, rebased and cleaned up



---

archive/issue_comments_074397.json:
```json
{
    "body": "Attachment\n\nBesides everything else, the latest patch moves `_coerce_map_from_()` from the various finite field implementations to the `FiniteField` base class; it is now implementation-independent.  For this reason, this ticket now depends on #12142.  Various other changes have been made.\n\nThe syntax for constructing finite fields using Conway polynomials that admit automatic coercion is now\n\n```\nsage: F.<a> = FiniteField(5^3, conway=True, prefix='z')\n```\n\nThis is not too pretty, but it is meant as a temporary solution until we have algebraic closures of finite fields.\n\nOlder patches on this ticket contained various changes that were in older attachments and that do not seem immediately relevant to this ticket.  I deleted those changes that seemed superfluous and kept those that I thought could be necessary after all.\n\nThis ticket should be reviewed once #14958 is done.\n\nFor patchbot:\n\n```\napply trac_8335-finite_field_coerce-5.11.b3.patch\n```\n",
    "created_at": "2013-07-29T12:08:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8335#issuecomment-74397",
    "user": "pbruin"
}
```

Attachment

Besides everything else, the latest patch moves `_coerce_map_from_()` from the various finite field implementations to the `FiniteField` base class; it is now implementation-independent.  For this reason, this ticket now depends on #12142.  Various other changes have been made.

The syntax for constructing finite fields using Conway polynomials that admit automatic coercion is now

```
sage: F.<a> = FiniteField(5^3, conway=True, prefix='z')
```

This is not too pretty, but it is meant as a temporary solution until we have algebraic closures of finite fields.

Older patches on this ticket contained various changes that were in older attachments and that do not seem immediately relevant to this ticket.  I deleted those changes that seemed superfluous and kept those that I thought could be necessary after all.

This ticket should be reviewed once #14958 is done.

For patchbot:

```
apply trac_8335-finite_field_coerce-5.11.b3.patch
```




---

archive/issue_comments_074398.json:
```json
{
    "body": "Changing status from needs_work to needs_info.",
    "created_at": "2013-07-29T12:08:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8335#issuecomment-74398",
    "user": "pbruin"
}
```

Changing status from needs_work to needs_info.



---

archive/issue_comments_074399.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2013-07-30T12:27:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8335#issuecomment-74399",
    "user": "jpflori"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_074400.json:
```json
{
    "body": "Rebased on top of #14888.",
    "created_at": "2013-07-30T12:38:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8335#issuecomment-74400",
    "user": "jpflori"
}
```

Rebased on top of #14888.



---

archive/issue_comments_074401.json:
```json
{
    "body": "Attachment",
    "created_at": "2013-07-30T12:38:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8335#issuecomment-74401",
    "user": "jpflori"
}
```

Attachment



---

archive/issue_comments_074402.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2013-07-30T12:44:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8335#issuecomment-74402",
    "user": "jpflori"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_074403.json:
```json
{
    "body": "Need to be rebased because of the name changes in #14958.",
    "created_at": "2013-07-30T12:44:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8335#issuecomment-74403",
    "user": "jpflori"
}
```

Need to be rebased because of the name changes in #14958.



---

archive/issue_comments_074404.json:
```json
{
    "body": "My bad.\nI thought you still cached the lattice in the finite field but you don't.\n(Un)fortunately when the lattice is built it is only weak-cached in conway_polynomials.py (so that it can be gc'ed when no finite field uses it anymore).\n\nSo either we have to store the lattice in the finite field to keep it alive and be able to use it when building extensions/pushouts and so on, or strongly cache it in conway_polynomials.py (I don't like that solution, in fact I hate caching things too much; note that currently everything is strongly cached anyway because of comment:69, #14711).",
    "created_at": "2013-07-30T12:51:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8335#issuecomment-74404",
    "user": "jpflori"
}
```

My bad.
I thought you still cached the lattice in the finite field but you don't.
(Un)fortunately when the lattice is built it is only weak-cached in conway_polynomials.py (so that it can be gc'ed when no finite field uses it anymore).

So either we have to store the lattice in the finite field to keep it alive and be able to use it when building extensions/pushouts and so on, or strongly cache it in conway_polynomials.py (I don't like that solution, in fact I hate caching things too much; note that currently everything is strongly cached anyway because of comment:69, #14711).



---

archive/issue_comments_074405.json:
```json
{
    "body": "Attachment\n\nName changes in #14958.",
    "created_at": "2013-07-30T12:57:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8335#issuecomment-74405",
    "user": "jpflori"
}
```

Attachment

Name changes in #14958.



---

archive/issue_comments_074406.json:
```json
{
    "body": "In fact, the more I think about it, the less I like the way things are stored in the pseudo-Conway polynomial code.\n\nWe should make some big changes when implementing the AlgebraicClosure thing...\nHas anyone open a ticket for that?",
    "created_at": "2013-07-30T13:31:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8335#issuecomment-74406",
    "user": "jpflori"
}
```

In fact, the more I think about it, the less I like the way things are stored in the pseudo-Conway polynomial code.

We should make some big changes when implementing the AlgebraicClosure thing...
Has anyone open a ticket for that?



---

archive/issue_comments_074407.json:
```json
{
    "body": "Replying to [comment:106 jpflori]:\n> We should make some big changes when implementing the AlgebraicClosure thing...\n> Has anyone open a ticket for that?\nNot yet, as far as I have been able to find out; I can do it now.",
    "created_at": "2013-07-31T15:06:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8335#issuecomment-74407",
    "user": "pbruin"
}
```

Replying to [comment:106 jpflori]:
> We should make some big changes when implementing the AlgebraicClosure thing...
> Has anyone open a ticket for that?
Not yet, as far as I have been able to find out; I can do it now.



---

archive/issue_comments_074408.json:
```json
{
    "body": "Replying to [comment:106 jpflori]:\n> In fact, the more I think about it, the less I like the way things are stored in the pseudo-Conway polynomial code.\n\nI dislike it too.  It is problematic to store pseudo-Conway lattices globally in a Sage session (at least until they are garbage-collected) given that they are not uniquely defined.\n\nIt appears that the user could do the following:\n- create a finite field *k*<sub>0</sub> using a primitive polynomial *f*<sub>0</sub>\n- throw away *k*<sub>0</sub>, causing the pseudo-Conway lattice containing *f*<sub>0</sub> to be garbage-collected\n- create a field *k*<sub>1</sub> using exactly the same command as for *k*<sub>0</sub>; this will be isomorphic to *k*<sub>0</sub>, but will in general be defined by a polynomial *f*<sub>1</sub> that is different from *f*<sub>0</sub>\n- end up with a *k*<sub>1</sub> that is incompatible with things that were constructed with the help of *k*<sub>0</sub> (e.g. extensions of *k*<sub>0</sub>), even though both of them were generated using pseudo-Conway polynomials.\n\nI was also worried that storing the pseudo-Conway lattice in the finite field would mean that we would forever have to keep suitable pickling/unpickling code around to deal with this.  Actually, this is not necessary, since the pseudo-Conway lattice can be reconstructed from the defining polynomial.  However, this does not seem to solve the above problem.  Using strong references does not solve it either.  In both cases, the user may pickle *k*<sub>0</sub>, restart Sage, create *k*<sub>1</sub>, and finally unpickle *k*<sub>0</sub>; then again *k*<sub>0</sub> and *k*<sub>1</sub> will be different in general.\n\nAll of this is basically a manifestation of the fact that \"the\" field of *p<sup>n</sup>* elements is only defined up to non-canonical isomorphism.",
    "created_at": "2013-07-31T17:00:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8335#issuecomment-74408",
    "user": "pbruin"
}
```

Replying to [comment:106 jpflori]:
> In fact, the more I think about it, the less I like the way things are stored in the pseudo-Conway polynomial code.

I dislike it too.  It is problematic to store pseudo-Conway lattices globally in a Sage session (at least until they are garbage-collected) given that they are not uniquely defined.

It appears that the user could do the following:
- create a finite field *k*<sub>0</sub> using a primitive polynomial *f*<sub>0</sub>
- throw away *k*<sub>0</sub>, causing the pseudo-Conway lattice containing *f*<sub>0</sub> to be garbage-collected
- create a field *k*<sub>1</sub> using exactly the same command as for *k*<sub>0</sub>; this will be isomorphic to *k*<sub>0</sub>, but will in general be defined by a polynomial *f*<sub>1</sub> that is different from *f*<sub>0</sub>
- end up with a *k*<sub>1</sub> that is incompatible with things that were constructed with the help of *k*<sub>0</sub> (e.g. extensions of *k*<sub>0</sub>), even though both of them were generated using pseudo-Conway polynomials.

I was also worried that storing the pseudo-Conway lattice in the finite field would mean that we would forever have to keep suitable pickling/unpickling code around to deal with this.  Actually, this is not necessary, since the pseudo-Conway lattice can be reconstructed from the defining polynomial.  However, this does not seem to solve the above problem.  Using strong references does not solve it either.  In both cases, the user may pickle *k*<sub>0</sub>, restart Sage, create *k*<sub>1</sub>, and finally unpickle *k*<sub>0</sub>; then again *k*<sub>0</sub> and *k*<sub>1</sub> will be different in general.

All of this is basically a manifestation of the fact that "the" field of *p<sup>n</sup>* elements is only defined up to non-canonical isomorphism.



---

archive/issue_comments_074409.json:
```json
{
    "body": "I suggest we store a strong to the (top of the) lattice in the FF for the moment, as used to be done, and merge this ticket.\n\nAnd let's think of a better design for #14990.\nHaving AlgebraicClosure object will surely greatly simplify this.",
    "created_at": "2013-07-31T17:09:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8335#issuecomment-74409",
    "user": "jpflori"
}
```

I suggest we store a strong to the (top of the) lattice in the FF for the moment, as used to be done, and merge this ticket.

And let's think of a better design for #14990.
Having AlgebraicClosure object will surely greatly simplify this.



---

archive/issue_comments_074410.json:
```json
{
    "body": "Replying to [comment:109 jpflori]:\n> I suggest we store a strong to the (top of the) lattice in the FF for the moment\n\nWe could do that to make garbage collection less likely, but it won't really solve the problem, see comment:108.\n\n> And let's think of a better design for #14990.\n> Having AlgebraicClosure object will surely greatly simplify this.\n\nYes, the more I think about it, the more convinced I am that algebraic closures are the only real solution to the problem of compatible embeddings.\n\nJenny Cooley suggested the following idea, which I think is a good compromise: implement this ticket only for standard (not pseudo-) Conway polynomials.  Hopefully this would suffice for most practical purposes, and since they are uniquely determined, we wouldn't have to come up with half-baked solutions to the caching problem.  In #14990 (which I am working on now), pseudo-Conway polynomials can then finally be put to use, and they will be cached in the algebraic closure, where they really belong.",
    "created_at": "2013-08-01T14:12:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8335#issuecomment-74410",
    "user": "pbruin"
}
```

Replying to [comment:109 jpflori]:
> I suggest we store a strong to the (top of the) lattice in the FF for the moment

We could do that to make garbage collection less likely, but it won't really solve the problem, see comment:108.

> And let's think of a better design for #14990.
> Having AlgebraicClosure object will surely greatly simplify this.

Yes, the more I think about it, the more convinced I am that algebraic closures are the only real solution to the problem of compatible embeddings.

Jenny Cooley suggested the following idea, which I think is a good compromise: implement this ticket only for standard (not pseudo-) Conway polynomials.  Hopefully this would suffice for most practical purposes, and since they are uniquely determined, we wouldn't have to come up with half-baked solutions to the caching problem.  In #14990 (which I am working on now), pseudo-Conway polynomials can then finally be put to use, and they will be cached in the algebraic closure, where they really belong.



---

archive/issue_comments_074411.json:
```json
{
    "body": "I'm ok with that.\n\nI think I could accept anything as long as we close this ticket :)",
    "created_at": "2013-08-01T14:16:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8335#issuecomment-74411",
    "user": "jpflori"
}
```

I'm ok with that.

I think I could accept anything as long as we close this ticket :)



---

archive/issue_comments_074412.json:
```json
{
    "body": "use only (non-pseudo-)Conway polynomials",
    "created_at": "2013-08-02T11:02:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8335#issuecomment-74412",
    "user": "pbruin"
}
```

use only (non-pseudo-)Conway polynomials



---

archive/issue_comments_074413.json:
```json
{
    "body": "Attachment",
    "created_at": "2013-08-02T11:06:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8335#issuecomment-74413",
    "user": "pbruin"
}
```

Attachment



---

archive/issue_comments_074414.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2013-08-02T11:06:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8335#issuecomment-74414",
    "user": "pbruin"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_074415.json:
```json
{
    "body": "For patchbot:\n\n```\napply trac_8335-finite_field_coerce-5.11.b3-14888.patch\u200b, trac_8335-no_pseudo.patch\u200b \n```\n\nNote: [attachment:trac_8335-rebase_14958.patch\u200b] is not needed if we go for this approach.",
    "created_at": "2013-08-02T11:10:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8335#issuecomment-74415",
    "user": "pbruin"
}
```

For patchbot:

```
apply trac_8335-finite_field_coerce-5.11.b3-14888.patch​, trac_8335-no_pseudo.patch​ 
```

Note: [attachment:trac_8335-rebase_14958.patch​] is not needed if we go for this approach.



---

archive/issue_comments_074416.json:
```json
{
    "body": "Looks ok.\nStill depending on #14958 as functions related to (non-pseudo) Conway polys were moved around there.",
    "created_at": "2013-08-06T11:45:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8335#issuecomment-74416",
    "user": "jpflori"
}
```

Looks ok.
Still depending on #14958 as functions related to (non-pseudo) Conway polys were moved around there.



---

archive/issue_comments_074417.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-08-06T11:45:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8335#issuecomment-74417",
    "user": "jpflori"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_074418.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2013-10-12T09:45:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8335#issuecomment-74418",
    "user": "jdemeyer"
}
```

Resolution: fixed
