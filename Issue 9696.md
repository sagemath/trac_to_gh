# Issue 9696: Add methods to AdditiveAbelianGroup

archive/issues_009696.json:
```json
{
    "body": "Assignee: joyner\n\nCC:  davidloeffler cremona\n\nPatch adds `is_cyclic()` and `_latex_()` methods to the `AdditiveAbelianGroup`s.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9696\n\n",
    "created_at": "2010-08-06T06:22:59Z",
    "labels": [
        "group theory",
        "minor",
        "enhancement"
    ],
    "title": "Add methods to AdditiveAbelianGroup",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9696",
    "user": "rbeezer"
}
```
Assignee: joyner

CC:  davidloeffler cremona

Patch adds `is_cyclic()` and `_latex_()` methods to the `AdditiveAbelianGroup`s.

Issue created by migration from https://trac.sagemath.org/ticket/9696





---

archive/issue_comments_094233.json:
```json
{
    "body": "Attachment [trac_9696-cyclic-latex-additiveabeliangroup.patch](tarball://root/attachments/some-uuid/ticket9696/trac_9696-cyclic-latex-additiveabeliangroup.patch) by rbeezer created at 2010-08-06 06:26:38",
    "created_at": "2010-08-06T06:26:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9696",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9696#issuecomment-94233",
    "user": "rbeezer"
}
```

Attachment [trac_9696-cyclic-latex-additiveabeliangroup.patch](tarball://root/attachments/some-uuid/ticket9696/trac_9696-cyclic-latex-additiveabeliangroup.patch) by rbeezer created at 2010-08-06 06:26:38



---

archive/issue_comments_094234.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-08-06T06:28:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9696",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9696#issuecomment-94234",
    "user": "rbeezer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_094235.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-08-22T13:28:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9696",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9696#issuecomment-94235",
    "user": "cremona"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_094236.json:
```json
{
    "body": "Applies fine to 4.5.3.alpha1.   Perhaps it would be good to have a doctest showing this:\n\n```\nsage: AdditiveAbelianGroup([1])._latex_()\n'\\\\frac{\\\\ZZ}{1\\\\ZZ}'\n```\n\nwhich is not what a mathematician would write (perhaps change it to '0'). \n\nI have given a positive review anyway, but would be happy to re-review with this changed and/or doctested.",
    "created_at": "2010-08-22T13:28:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9696",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9696#issuecomment-94236",
    "user": "cremona"
}
```

Applies fine to 4.5.3.alpha1.   Perhaps it would be good to have a doctest showing this:

```
sage: AdditiveAbelianGroup([1])._latex_()
'\\frac{\\ZZ}{1\\ZZ}'
```

which is not what a mathematician would write (perhaps change it to '0'). 

I have given a positive review anyway, but would be happy to re-review with this changed and/or doctested.



---

archive/issue_comments_094237.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-08-22T18:53:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9696",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9696#issuecomment-94237",
    "user": "rbeezer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_094238.json:
```json
{
    "body": "Replying to [comment:2 cremona]:\n> which is not what a mathematician would write (perhaps change it to '0'). \n\nYes, I like the '0' suggestion, I'll make that change and post an updated patch shortly.  Thanks for the suggestion.\n\n> I have given a positive review anyway, but would be happy to re-review with this changed and/or doctested.",
    "created_at": "2010-08-22T18:53:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9696",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9696#issuecomment-94238",
    "user": "rbeezer"
}
```

Replying to [comment:2 cremona]:
> which is not what a mathematician would write (perhaps change it to '0'). 

Yes, I like the '0' suggestion, I'll make that change and post an updated patch shortly.  Thanks for the suggestion.

> I have given a positive review anyway, but would be happy to re-review with this changed and/or doctested.



---

archive/issue_comments_094239.json:
```json
{
    "body": "Attachment [trac_9696-cyclic-latex-additiveabeliangroup-v2.patch](tarball://root/attachments/some-uuid/ticket9696/trac_9696-cyclic-latex-additiveabeliangroup-v2.patch) by rbeezer created at 2010-08-22 19:55:15\n\nStand-alone patch, apply just this one",
    "created_at": "2010-08-22T19:55:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9696",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9696#issuecomment-94239",
    "user": "rbeezer"
}
```

Attachment [trac_9696-cyclic-latex-additiveabeliangroup-v2.patch](tarball://root/attachments/some-uuid/ticket9696/trac_9696-cyclic-latex-additiveabeliangroup-v2.patch) by rbeezer created at 2010-08-22 19:55:15

Stand-alone patch, apply just this one



---

archive/issue_comments_094240.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-08-22T20:00:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9696",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9696#issuecomment-94240",
    "user": "rbeezer"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_094241.json:
```json
{
    "body": "v2 patch adds a stanza to the latex representation code to detect trivial factor(s) and format as '0'.  This probably only happens when the invariant list passed in is empty, but there shouldn't be much penalty in burying this inside the construction of all the other possible terms.\n\nA doctest is added for this situation, and the affected file passes all tests.  I built the documentation, but it would appear this section is not being included in the documentation?  I could rectify that with another patch and a look at the resulting output.\n\nThanks,\nRob",
    "created_at": "2010-08-22T20:00:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9696",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9696#issuecomment-94241",
    "user": "rbeezer"
}
```

v2 patch adds a stanza to the latex representation code to detect trivial factor(s) and format as '0'.  This probably only happens when the invariant list passed in is empty, but there shouldn't be much penalty in burying this inside the construction of all the other possible terms.

A doctest is added for this situation, and the affected file passes all tests.  I built the documentation, but it would appear this section is not being included in the documentation?  I could rectify that with another patch and a look at the resulting output.

Thanks,
Rob



---

archive/issue_comments_094242.json:
```json
{
    "body": "Second patch looks good.  (I was just thinking of testing for the trivial group, but this is more general.)\n\nAbelian groups are in the reference manual:  doc/en/reference/groups.rst has\n\n```\n   sage/groups/abelian_gps/abelian_group\n   sage/groups/abelian_gps/abelian_group_element\n   sage/groups/abelian_gps/abelian_group_morphism\n   sage/groups/abelian_gps/dual_abelian_group\n```\n\n\nThere are some formatting issues with those but not caused by this patch.",
    "created_at": "2010-08-22T21:09:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9696",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9696#issuecomment-94242",
    "user": "cremona"
}
```

Second patch looks good.  (I was just thinking of testing for the trivial group, but this is more general.)

Abelian groups are in the reference manual:  doc/en/reference/groups.rst has

```
   sage/groups/abelian_gps/abelian_group
   sage/groups/abelian_gps/abelian_group_element
   sage/groups/abelian_gps/abelian_group_morphism
   sage/groups/abelian_gps/dual_abelian_group
```


There are some formatting issues with those but not caused by this patch.



---

archive/issue_comments_094243.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-08-22T21:09:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9696",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9696#issuecomment-94243",
    "user": "cremona"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_094244.json:
```json
{
    "body": "Replying to [comment:5 cremona]:\n> Second patch looks good.  (I was just thinking of testing for the trivial group, but this is more general.)\n> \n> Abelian groups are in the reference manual:  doc/en/reference/groups.rst has\n> {{{\n>    sage/groups/abelian_gps/abelian_group\n>    sage/groups/abelian_gps/abelian_group_element\n>    sage/groups/abelian_gps/abelian_group_morphism\n>    sage/groups/abelian_gps/dual_abelian_group\n> }}}\n> \n> There are some formatting issues with those but not caused by this patch.\n\nSorry, my mistake -- abelian_groups are not additive_abelian_groups, and the latter are not included.  Something for another ticket!",
    "created_at": "2010-08-22T21:11:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9696",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9696#issuecomment-94244",
    "user": "cremona"
}
```

Replying to [comment:5 cremona]:
> Second patch looks good.  (I was just thinking of testing for the trivial group, but this is more general.)
> 
> Abelian groups are in the reference manual:  doc/en/reference/groups.rst has
> {{{
>    sage/groups/abelian_gps/abelian_group
>    sage/groups/abelian_gps/abelian_group_element
>    sage/groups/abelian_gps/abelian_group_morphism
>    sage/groups/abelian_gps/dual_abelian_group
> }}}
> 
> There are some formatting issues with those but not caused by this patch.

Sorry, my mistake -- abelian_groups are not additive_abelian_groups, and the latter are not included.  Something for another ticket!



---

archive/issue_comments_094245.json:
```json
{
    "body": "Replying to [comment:6 cremona]:\n> Sorry, my mistake -- abelian_groups are not additive_abelian_groups, and the latter are not included.  Something for another ticket!\n\nNew ticket at #9783 which I will try to make some progress on.\n\nRelease manager:  Only apply the v2 patch.",
    "created_at": "2010-08-22T23:28:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9696",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9696#issuecomment-94245",
    "user": "rbeezer"
}
```

Replying to [comment:6 cremona]:
> Sorry, my mistake -- abelian_groups are not additive_abelian_groups, and the latter are not included.  Something for another ticket!

New ticket at #9783 which I will try to make some progress on.

Release manager:  Only apply the v2 patch.



---

archive/issue_comments_094246.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-09-15T10:40:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9696",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9696#issuecomment-94246",
    "user": "mpatel"
}
```

Resolution: fixed
