# Issue 8044: Categories for finite (permutation) groups

archive/issues_008044.json:
```json
{
    "body": "Assignee: nthiery\n\nCC:  sage-combinat vengoroso@gmail.com\n\nKeywords: Finite groups, permutation groups\n\nThis patch:\n\n- Introduces two new categories, FiniteGroups and FinitePermutationGroups\n- Deprecates the class sage.groups.group.FiniteGroup\n  (content moved to the FiniteGroups category; this is essentially\n  the cayley_graph method)\n- Puts all permutation groups and most other finite groups in the\n  corresponding categories\n- As a result, this standardizes the interface of those groups\n  (cardinality, one, ...), and reveals lots of failures in the\n  completely undocumented PariGroup (category not set properly yet)\n- Makes a minor improvement to FiniteEnumeratedSets tests for\n  large finite enumerated sets\n\nIssue created by migration from https://trac.sagemath.org/ticket/8044\n\n",
    "created_at": "2010-01-23T10:29:04Z",
    "labels": [
        "group theory",
        "major",
        "bug"
    ],
    "title": "Categories for finite (permutation) groups",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8044",
    "user": "nthiery"
}
```
Assignee: nthiery

CC:  sage-combinat vengoroso@gmail.com

Keywords: Finite groups, permutation groups

This patch:

- Introduces two new categories, FiniteGroups and FinitePermutationGroups
- Deprecates the class sage.groups.group.FiniteGroup
  (content moved to the FiniteGroups category; this is essentially
  the cayley_graph method)
- Puts all permutation groups and most other finite groups in the
  corresponding categories
- As a result, this standardizes the interface of those groups
  (cardinality, one, ...), and reveals lots of failures in the
  completely undocumented PariGroup (category not set properly yet)
- Makes a minor improvement to FiniteEnumeratedSets tests for
  large finite enumerated sets

Issue created by migration from https://trac.sagemath.org/ticket/8044





---

archive/issue_comments_070297.json:
```json
{
    "body": "Non finalized patch on: http://combinat.sagemath.org/hgwebdir.cgi/patches/file/tip/trac_8044-categories_finite_groups-nt.patch",
    "created_at": "2010-01-23T10:32:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8044",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8044#issuecomment-70297",
    "user": "nthiery"
}
```

Non finalized patch on: http://combinat.sagemath.org/hgwebdir.cgi/patches/file/tip/trac_8044-categories_finite_groups-nt.patch



---

archive/issue_comments_070298.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2010-01-27T22:02:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8044",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8044#issuecomment-70298",
    "user": "nthiery"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_070299.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-27T22:02:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8044",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8044#issuecomment-70299",
    "user": "nthiery"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_070300.json:
```json
{
    "body": "Changing keywords from \"Finite groups, permutation groups\" to \"Finite groups, permutation groups, symmetric groups\".",
    "created_at": "2010-01-27T22:05:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8044",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8044#issuecomment-70300",
    "user": "nthiery"
}
```

Changing keywords from "Finite groups, permutation groups" to "Finite groups, permutation groups, symmetric groups".



---

archive/issue_comments_070301.json:
```json
{
    "body": "The attached patch passes all tests on 4.3.1 + the sage-combinat patches already merged in 4.3.2: !#7976 #7921 #7938 !#8028 #8001 !#5524",
    "created_at": "2010-01-27T22:05:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8044",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8044#issuecomment-70301",
    "user": "nthiery"
}
```

The attached patch passes all tests on 4.3.1 + the sage-combinat patches already merged in 4.3.2: !#7976 #7921 #7938 !#8028 #8001 !#5524



---

archive/issue_comments_070302.json:
```json
{
    "body": "Applies over the precedent patch.",
    "created_at": "2010-01-29T16:07:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8044",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8044#issuecomment-70302",
    "user": "slabbe"
}
```

Applies over the precedent patch.



---

archive/issue_comments_070303.json:
```json
{
    "body": "Attachment\n\nI just added a patch which adds some examples of cayley graphs.\n\nIt also adds `FiniteGroup` to the base classes of `MatrixGroup_gap_finite_field`.",
    "created_at": "2010-01-29T16:09:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8044",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8044#issuecomment-70303",
    "user": "slabbe"
}
```

Attachment

I just added a patch which adds some examples of cayley graphs.

It also adds `FiniteGroup` to the base classes of `MatrixGroup_gap_finite_field`.



---

archive/issue_comments_070304.json:
```json
{
    "body": "Applies fine to 4.3.2.a0 and passes sage -t (except those 2 apparently singular-related tests which failed before).\n\nI did not test sage -optional nor did I look carefully at how the category framework fits in with the rest of the category \nstuff (eg, Weyl groups). I did look at the permutation group aspect and positive review for that part. Was someone else going to look at the rest (Javier, vengoroso`@`gmail.com)? If not, please let me know.",
    "created_at": "2010-01-31T14:11:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8044",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8044#issuecomment-70304",
    "user": "wdj"
}
```

Applies fine to 4.3.2.a0 and passes sage -t (except those 2 apparently singular-related tests which failed before).

I did not test sage -optional nor did I look carefully at how the category framework fits in with the rest of the category 
stuff (eg, Weyl groups). I did look at the permutation group aspect and positive review for that part. Was someone else going to look at the rest (Javier, vengoroso`@`gmail.com)? If not, please let me know.



---

archive/issue_comments_070305.json:
```json
{
    "body": "Replying to [comment:7 wdj]:\n> Applies fine to 4.3.2.a0 and passes sage -t (except those 2 apparently singular-related tests which failed before).\n> \n> I did not test sage -optional nor did I look carefully at how the category framework fits in with the rest of the category \n> stuff (eg, Weyl groups). I did look at the permutation group aspect and positive review for that part. Was someone else going to look at the rest (Javier, vengoroso`@`gmail.com)? If not, please let me know.\n\nThanks much for your review!\n\nFlorent: could you have a look at the Weyl group + Cayley graph part?\nDavid: did you check the matrix part? If not, do you mind handling it?\nJavier: could you look at the category part?",
    "created_at": "2010-01-31T20:27:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8044",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8044#issuecomment-70305",
    "user": "nthiery"
}
```

Replying to [comment:7 wdj]:
> Applies fine to 4.3.2.a0 and passes sage -t (except those 2 apparently singular-related tests which failed before).
> 
> I did not test sage -optional nor did I look carefully at how the category framework fits in with the rest of the category 
> stuff (eg, Weyl groups). I did look at the permutation group aspect and positive review for that part. Was someone else going to look at the rest (Javier, vengoroso`@`gmail.com)? If not, please let me know.

Thanks much for your review!

Florent: could you have a look at the Weyl group + Cayley graph part?
David: did you check the matrix part? If not, do you mind handling it?
Javier: could you look at the category part?



---

archive/issue_comments_070306.json:
```json
{
    "body": "Replying to [comment:8 nthiery]:\n> Replying to [comment:7 wdj]:\n> > Applies fine to 4.3.2.a0 and passes sage -t (except those 2 apparently singular-related tests which failed before).\n> > \n> > I did not test sage -optional nor did I look carefully at how the category framework fits in with the rest of the category \n> > stuff (eg, Weyl groups). I did look at the permutation group aspect and positive review for that part. Was someone else going to look at the rest (Javier, vengoroso`@`gmail.com)? If not, please let me know.\n> \n> Thanks much for your review!\n> \n> Florent: could you have a look at the Weyl group + Cayley graph part?\n> David: did you check the matrix part? If not, do you mind handling it?\n\n\nYes, I looked at it and also give that part a positive review. I like the way you handled \nover different fields.\n\n\n> Javier: could you look at the category part?\n>",
    "created_at": "2010-01-31T22:25:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8044",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8044#issuecomment-70306",
    "user": "wdj"
}
```

Replying to [comment:8 nthiery]:
> Replying to [comment:7 wdj]:
> > Applies fine to 4.3.2.a0 and passes sage -t (except those 2 apparently singular-related tests which failed before).
> > 
> > I did not test sage -optional nor did I look carefully at how the category framework fits in with the rest of the category 
> > stuff (eg, Weyl groups). I did look at the permutation group aspect and positive review for that part. Was someone else going to look at the rest (Javier, vengoroso`@`gmail.com)? If not, please let me know.
> 
> Thanks much for your review!
> 
> Florent: could you have a look at the Weyl group + Cayley graph part?
> David: did you check the matrix part? If not, do you mind handling it?


Yes, I looked at it and also give that part a positive review. I like the way you handled 
over different fields.


> Javier: could you look at the category part?
>



---

archive/issue_comments_070307.json:
```json
{
    "body": "Replying to [comment:9 wdj]:\n> > David: did you check the matrix part? If not, do you mind handling it?\n> \n> Yes, I looked at it and also give that part a positive review. \n\nThanks!\n\n> I like the way you handled over different fields.\n\n:-) \n\nBeing able to choose at run time the category, and therefore the class hierarchy, as we could do in MuPAD, was one of my big incentive for writing the category code, and going for dynamic classes.",
    "created_at": "2010-01-31T22:36:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8044",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8044#issuecomment-70307",
    "user": "nthiery"
}
```

Replying to [comment:9 wdj]:
> > David: did you check the matrix part? If not, do you mind handling it?
> 
> Yes, I looked at it and also give that part a positive review. 

Thanks!

> I like the way you handled over different fields.

:-) 

Being able to choose at run time the category, and therefore the class hierarchy, as we could do in MuPAD, was one of my big incentive for writing the category code, and going for dynamic classes.



---

archive/issue_comments_070308.json:
```json
{
    "body": "The category part looks fine to me. This is an amazing patch, btw!\n\nI am getting some doctests failures:\n\n\n\n```\n----------------------------------------------------------------------\nThe following tests failed:\n\n\n        sage -t  \"devel/sage/doc/en/tutorial/tour_advanced.rst\"\n        sage -t  \"devel/sage/doc/fr/tutorial/tour_advanced.rst\"\n        sage -t  \"devel/sage/sage/categories/finite_groups.py\"\n        sage -t  \"devel/sage/sage/categories/finite_permutation_groups.py\"\n        sage -t  \"devel/sage/sage/groups/pari_group.py\"\n        sage -t  \"devel/sage/sage/groups/perm_gps/permgroup_named.py\"\n        sage -t  \"devel/sage/sage/interfaces/r.py\"\n        sage -t  \"devel/sage/sage/rings/polynomial/groebner_fan.py\"\n        sage -t  \"devel/sage/sage/rings/polynomial/multi_polynomial_ideal.py\"\n```\n\n\nthough they don't seem too serious.\n\nThere are a couple of \"The category of (multiplicative) finite semigroups\" in the docstrings that should be corrected.\n\nFor the rest, assuming that the doctest pass (it might be something with my sage, will try with a clean install at the office in a couple of hours), positive review.",
    "created_at": "2010-02-01T09:44:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8044",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8044#issuecomment-70308",
    "user": "jlopez"
}
```

The category part looks fine to me. This is an amazing patch, btw!

I am getting some doctests failures:



```
----------------------------------------------------------------------
The following tests failed:


        sage -t  "devel/sage/doc/en/tutorial/tour_advanced.rst"
        sage -t  "devel/sage/doc/fr/tutorial/tour_advanced.rst"
        sage -t  "devel/sage/sage/categories/finite_groups.py"
        sage -t  "devel/sage/sage/categories/finite_permutation_groups.py"
        sage -t  "devel/sage/sage/groups/pari_group.py"
        sage -t  "devel/sage/sage/groups/perm_gps/permgroup_named.py"
        sage -t  "devel/sage/sage/interfaces/r.py"
        sage -t  "devel/sage/sage/rings/polynomial/groebner_fan.py"
        sage -t  "devel/sage/sage/rings/polynomial/multi_polynomial_ideal.py"
```


though they don't seem too serious.

There are a couple of "The category of (multiplicative) finite semigroups" in the docstrings that should be corrected.

For the rest, assuming that the doctest pass (it might be something with my sage, will try with a clean install at the office in a couple of hours), positive review.



---

archive/issue_comments_070309.json:
```json
{
    "body": "Attachment\n\nApply only this one",
    "created_at": "2010-02-01T10:02:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8044",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8044#issuecomment-70309",
    "user": "nthiery"
}
```

Attachment

Apply only this one



---

archive/issue_comments_070310.json:
```json
{
    "body": "Replying to [comment:11 jlopez]:\n> The category part looks fine to me. This is an amazing patch, btw!\n\n:-)\n\n> I am getting some doctests failures:\n> \n> \n> {{{\n> ----------------------------------------------------------------------\n> The following tests failed:\n> \n> \n>         sage -t  \"devel/sage/doc/en/tutorial/tour_advanced.rst\"\n>         sage -t  \"devel/sage/doc/fr/tutorial/tour_advanced.rst\"\n>         sage -t  \"devel/sage/sage/categories/finite_groups.py\"\n>         sage -t  \"devel/sage/sage/categories/finite_permutation_groups.py\"\n>         sage -t  \"devel/sage/sage/groups/pari_group.py\"\n>         sage -t  \"devel/sage/sage/groups/perm_gps/permgroup_named.py\"\n>         sage -t  \"devel/sage/sage/interfaces/r.py\"\n>         sage -t  \"devel/sage/sage/rings/polynomial/groebner_fan.py\"\n>         sage -t  \"devel/sage/sage/rings/polynomial/multi_polynomial_ideal.py\"\n> }}}\n> \n> though they don't seem too serious.\n> (it might be something with my sage, will try with a clean install at the office in a couple of hours),\n\nFor the record, could you please post or attach here the complete log of the failures, even if it works at your office?\n\n> There are a couple of \"The category of (multiplicative) finite semigroups\" in the docstrings that should be corrected.\n\nOops, good catch. The updated patch fixes this.\n\n> For the rest, assuming that the doctest pass positive review.\n\nThanks!",
    "created_at": "2010-02-01T10:04:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8044",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8044#issuecomment-70310",
    "user": "nthiery"
}
```

Replying to [comment:11 jlopez]:
> The category part looks fine to me. This is an amazing patch, btw!

:-)

> I am getting some doctests failures:
> 
> 
> {{{
> ----------------------------------------------------------------------
> The following tests failed:
> 
> 
>         sage -t  "devel/sage/doc/en/tutorial/tour_advanced.rst"
>         sage -t  "devel/sage/doc/fr/tutorial/tour_advanced.rst"
>         sage -t  "devel/sage/sage/categories/finite_groups.py"
>         sage -t  "devel/sage/sage/categories/finite_permutation_groups.py"
>         sage -t  "devel/sage/sage/groups/pari_group.py"
>         sage -t  "devel/sage/sage/groups/perm_gps/permgroup_named.py"
>         sage -t  "devel/sage/sage/interfaces/r.py"
>         sage -t  "devel/sage/sage/rings/polynomial/groebner_fan.py"
>         sage -t  "devel/sage/sage/rings/polynomial/multi_polynomial_ideal.py"
> }}}
> 
> though they don't seem too serious.
> (it might be something with my sage, will try with a clean install at the office in a couple of hours),

For the record, could you please post or attach here the complete log of the failures, even if it works at your office?

> There are a couple of "The category of (multiplicative) finite semigroups" in the docstrings that should be corrected.

Oops, good catch. The updated patch fixes this.

> For the rest, assuming that the doctest pass positive review.

Thanks!



---

archive/issue_comments_070311.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-02-01T14:06:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8044",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8044#issuecomment-70311",
    "user": "jlopez"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_070312.json:
```json
{
    "body": "All tests pass on a clean install, so most probably my previous failure was due to too much fiddling with patches and source files (will upload the failures later anyway). Postive review.",
    "created_at": "2010-02-01T14:06:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8044",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8044#issuecomment-70312",
    "user": "jlopez"
}
```

All tests pass on a clean install, so most probably my previous failure was due to too much fiddling with patches and source files (will upload the failures later anyway). Postive review.



---

archive/issue_comments_070313.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-02-11T14:45:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8044",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8044#issuecomment-70313",
    "user": "mpatel"
}
```

Resolution: fixed
