# Issue 5048: congruence subgroups are not integrated into the coercion model

archive/issues_005048.json:
```json
{
    "body": "Assignee: was\n\nCC:  georgsweber\n\nKeywords: congruence subgroup coercion\n\n\n```\nsage: Gamma0(10).1 * Gamma0(5).2\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n\n/home/ncalexan/.sage/temp/sage.math.washington.edu/4030/_home_ncalexan__sage_init_sage_0.py in <module>()\n----> 1 \n      2 \n      3 \n      4 \n      5 \n\n/scratch/nca/sage-3.3.alpha0-sage.math-only-x86_64-Linux/local/lib/python2.5/site-packages/sage/structure/element.so in sage.structure.element.MonoidElement.__mul__ (sage/structure/element.c:7375)()\n    849 \n    850 \n--> 851 \n    852 \n    853 \n\nTypeError: unsupported operand parent(s) for '*': 'Congruence Subgroup Gamma0(10)' and 'Congruence Subgroup Gamma0(5)'\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5048\n\n",
    "created_at": "2009-01-21T08:00:00Z",
    "labels": [
        "number theory",
        "major",
        "bug"
    ],
    "title": "congruence subgroups are not integrated into the coercion model",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5048",
    "user": "ncalexan"
}
```
Assignee: was

CC:  georgsweber

Keywords: congruence subgroup coercion


```
sage: Gamma0(10).1 * Gamma0(5).2
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/ncalexan/.sage/temp/sage.math.washington.edu/4030/_home_ncalexan__sage_init_sage_0.py in <module>()
----> 1 
      2 
      3 
      4 
      5 

/scratch/nca/sage-3.3.alpha0-sage.math-only-x86_64-Linux/local/lib/python2.5/site-packages/sage/structure/element.so in sage.structure.element.MonoidElement.__mul__ (sage/structure/element.c:7375)()
    849 
    850 
--> 851 
    852 
    853 

TypeError: unsupported operand parent(s) for '*': 'Congruence Subgroup Gamma0(10)' and 'Congruence Subgroup Gamma0(5)'
```


Issue created by migration from https://trac.sagemath.org/ticket/5048





---

archive/issue_comments_038444.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2009-01-23T07:07:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5048",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5048#issuecomment-38444",
    "user": "AlexGhitza"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_038445.json:
```json
{
    "body": "Changing assignee from was to craigcitro.",
    "created_at": "2009-07-21T08:22:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5048",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5048#issuecomment-38445",
    "user": "davidloeffler"
}
```

Changing assignee from was to craigcitro.



---

archive/issue_comments_038446.json:
```json
{
    "body": "Changing component from number theory to modular forms.",
    "created_at": "2009-07-21T08:22:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5048",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5048#issuecomment-38446",
    "user": "davidloeffler"
}
```

Changing component from number theory to modular forms.



---

archive/issue_comments_038447.json:
```json
{
    "body": "Attachment [trac_5048-sl2z_coercion.patch](tarball://root/attachments/some-uuid/ticket5048/trac_5048-sl2z_coercion.patch) by davidloeffler created at 2010-12-09 20:51:47\n\npatch against 4.6.1.alpha3",
    "created_at": "2010-12-09T20:51:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5048",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5048#issuecomment-38447",
    "user": "davidloeffler"
}
```

Attachment [trac_5048-sl2z_coercion.patch](tarball://root/attachments/some-uuid/ticket5048/trac_5048-sl2z_coercion.patch) by davidloeffler created at 2010-12-09 20:51:47

patch against 4.6.1.alpha3



---

archive/issue_comments_038448.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-12-09T20:56:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5048",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5048#issuecomment-38448",
    "user": "davidloeffler"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_038449.json:
```json
{
    "body": "Here's a patch. I thought the simplest solution was to arrange that the parent of all congruence subgroup elements was always the (globally unique) SL2Z object, i.e. to make the various subgroup classes \"facade parents\" (like the prime integers example in the category docs).",
    "created_at": "2010-12-09T20:56:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5048",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5048#issuecomment-38449",
    "user": "davidloeffler"
}
```

Here's a patch. I thought the simplest solution was to arrange that the parent of all congruence subgroup elements was always the (globally unique) SL2Z object, i.e. to make the various subgroup classes "facade parents" (like the prime integers example in the category docs).



---

archive/issue_comments_038450.json:
```json
{
    "body": "Attachment [trac_5048-sl2z_coercion-rebased_for_10452.patch](tarball://root/attachments/some-uuid/ticket5048/trac_5048-sl2z_coercion-rebased_for_10452.patch) by davidloeffler created at 2010-12-09 21:06:36\n\nVersion that will apply happily after #10452",
    "created_at": "2010-12-09T21:06:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5048",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5048#issuecomment-38450",
    "user": "davidloeffler"
}
```

Attachment [trac_5048-sl2z_coercion-rebased_for_10452.patch](tarball://root/attachments/some-uuid/ticket5048/trac_5048-sl2z_coercion-rebased_for_10452.patch) by davidloeffler created at 2010-12-09 21:06:36

Version that will apply happily after #10452



---

archive/issue_comments_038451.json:
```json
{
    "body": "I just realised that the patch I just uploaded conflicts, in a rather trivial way, with the patch at #10452. The second patch will apply on top of the patch at #10452. The two patches are identical other than one line of diff context.",
    "created_at": "2010-12-09T21:11:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5048",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5048#issuecomment-38451",
    "user": "davidloeffler"
}
```

I just realised that the patch I just uploaded conflicts, in a rather trivial way, with the patch at #10452. The second patch will apply on top of the patch at #10452. The two patches are identical other than one line of diff context.



---

archive/issue_comments_038452.json:
```json
{
    "body": "Oh dear, it looks like the trac buildbot is trying to apply both patches at once, hence the red light! But it seems to have done one successful run with only the first patch installed.",
    "created_at": "2010-12-11T16:16:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5048",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5048#issuecomment-38452",
    "user": "davidloeffler"
}
```

Oh dear, it looks like the trac buildbot is trying to apply both patches at once, hence the red light! But it seems to have done one successful run with only the first patch installed.



---

archive/issue_comments_038453.json:
```json
{
    "body": "Apply trac_5048-sl2z_coercion-rebased_for_10452.patch\nDepends on #10452",
    "created_at": "2010-12-31T14:51:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5048",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5048#issuecomment-38453",
    "user": "davidloeffler"
}
```

Apply trac_5048-sl2z_coercion-rebased_for_10452.patch
Depends on #10452



---

archive/issue_comments_038454.json:
```json
{
    "body": "Changing priority from major to minor.",
    "created_at": "2011-01-25T15:40:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5048",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5048#issuecomment-38454",
    "user": "davidloeffler"
}
```

Changing priority from major to minor.



---

archive/issue_comments_038455.json:
```json
{
    "body": "version rebased to 4.7.1.alpha4 + #11422",
    "created_at": "2011-07-15T15:27:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5048",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5048#issuecomment-38455",
    "user": "davidloeffler"
}
```

version rebased to 4.7.1.alpha4 + #11422



---

archive/issue_comments_038456.json:
```json
{
    "body": "Attachment [trac_5048-rebased_for_11422.patch](tarball://root/attachments/some-uuid/ticket5048/trac_5048-rebased_for_11422.patch) by davidloeffler created at 2011-07-15 15:29:44\n\nI've uploaded a version that is rebased to apply happily over the positively-reviewed patch #11422. This is intended to form part of a series #10335 - #11422 - #11598 - this ticket - #10453 -\n #11601; but the patch itself is **independent** of #11598 and of the tickets later in the series.",
    "created_at": "2011-07-15T15:29:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5048",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5048#issuecomment-38456",
    "user": "davidloeffler"
}
```

Attachment [trac_5048-rebased_for_11422.patch](tarball://root/attachments/some-uuid/ticket5048/trac_5048-rebased_for_11422.patch) by davidloeffler created at 2011-07-15 15:29:44

I've uploaded a version that is rebased to apply happily over the positively-reviewed patch #11422. This is intended to form part of a series #10335 - #11422 - #11598 - this ticket - #10453 -
 #11601; but the patch itself is **independent** of #11598 and of the tickets later in the series.



---

archive/issue_comments_038457.json:
```json
{
    "body": "I'm raising the priority of this to \"major\" since it is a prerequisite for the (much more significant) patch #11601.",
    "created_at": "2011-07-17T10:14:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5048",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5048#issuecomment-38457",
    "user": "davidloeffler"
}
```

I'm raising the priority of this to "major" since it is a prerequisite for the (much more significant) patch #11601.



---

archive/issue_comments_038458.json:
```json
{
    "body": "Changing priority from minor to major.",
    "created_at": "2011-07-17T10:14:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5048",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5048#issuecomment-38458",
    "user": "davidloeffler"
}
```

Changing priority from minor to major.



---

archive/issue_comments_038459.json:
```json
{
    "body": "Hmmm,\nis there a quick and easy explanation for the change in the last line of the patch (file \"sage/modular/modform/constructor.py\")?\n\n- 87\t \t         <class 'sage.modular.arithgroup.congroup_gamma0.Gamma0_class'>, \n\n+ 87\t         <class 'sage.modular.arithgroup.congroup_gamma0.Gamma0_class_with_category'>, \n\n\nI mean, this might be necessary, but due to the rest of this patch or due to some earlier patch??",
    "created_at": "2011-08-10T18:21:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5048",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5048#issuecomment-38459",
    "user": "GeorgSWeber"
}
```

Hmmm,
is there a quick and easy explanation for the change in the last line of the patch (file "sage/modular/modform/constructor.py")?

- 87	 	         <class 'sage.modular.arithgroup.congroup_gamma0.Gamma0_class'>, 

+ 87	         <class 'sage.modular.arithgroup.congroup_gamma0.Gamma0_class_with_category'>, 


I mean, this might be necessary, but due to the rest of this patch or due to some earlier patch??



---

archive/issue_comments_038460.json:
```json
{
    "body": "It is necessary because the arithmetic subgroup init routine now calls ` Group.__init__ `, which was not previously the case. The group init routine subsequently calls various other init routines that link arithmetic subgroups into Sage's category framework, with all of its baroque subtleties involving dynamic classes etc.",
    "created_at": "2011-08-22T08:15:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5048",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5048#issuecomment-38460",
    "user": "davidloeffler"
}
```

It is necessary because the arithmetic subgroup init routine now calls ` Group.__init__ `, which was not previously the case. The group init routine subsequently calls various other init routines that link arithmetic subgroups into Sage's category framework, with all of its baroque subtleties involving dynamic classes etc.



---

archive/issue_comments_038461.json:
```json
{
    "body": "Georg: did you get any chance to look at this again? Since #11422 is still waiting around, I've clarified the description to point out that both the pre-#11422 and post-#11422 patches exist and are equally valid.",
    "created_at": "2011-09-19T12:17:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5048",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5048#issuecomment-38461",
    "user": "davidloeffler"
}
```

Georg: did you get any chance to look at this again? Since #11422 is still waiting around, I've clarified the description to point out that both the pre-#11422 and post-#11422 patches exist and are equally valid.



---

archive/issue_comments_038462.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-12-17T15:55:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5048",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5048#issuecomment-38462",
    "user": "johanbosman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_038463.json:
```json
{
    "body": "The patch still applies to 4.8.alpha4, the code looks sound, and all tests in sage.modular pass.",
    "created_at": "2011-12-17T15:55:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5048",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5048#issuecomment-38463",
    "user": "johanbosman"
}
```

The patch still applies to 4.8.alpha4, the code looks sound, and all tests in sage.modular pass.



---

archive/issue_comments_038464.json:
```json
{
    "body": "Hi Johan,\nthanks for looking at this one (I guess you're on SD 35 --- if so, I do envy you)!!\n\nI dimly remember that this patch introduced a function with a missing doctest in \"sage/modular/arithgroup/congroup_sl2z.py\":\n\n \t96\t    def __call__(self, x, check=True): \n \t97\t        r\"\"\" \n \t98\t        Create an element of self from x. If check=True (the default), check \n \t99\t        that x really defines a 2x2 integer matrix of det 1. \n \t100\t        \"\"\" \n \t101\t        return ArithmeticSubgroupElement(self, x, check=check) \n \t102\t \n\n\nI'm sorry I never got round to poke David about that (otherwise, the changes were OK for me) --- could you please have second look and check that independently (\"sage --coverage ...modular/arithgroups/\" or the like should show it)?\n\nThanks a lot in advance!\n\n\nCheers,\nGeorg",
    "created_at": "2011-12-17T20:51:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5048",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5048#issuecomment-38464",
    "user": "GeorgSWeber"
}
```

Hi Johan,
thanks for looking at this one (I guess you're on SD 35 --- if so, I do envy you)!!

I dimly remember that this patch introduced a function with a missing doctest in "sage/modular/arithgroup/congroup_sl2z.py":

 	96	    def __call__(self, x, check=True): 
 	97	        r""" 
 	98	        Create an element of self from x. If check=True (the default), check 
 	99	        that x really defines a 2x2 integer matrix of det 1. 
 	100	        """ 
 	101	        return ArithmeticSubgroupElement(self, x, check=check) 
 	102	 


I'm sorry I never got round to poke David about that (otherwise, the changes were OK for me) --- could you please have second look and check that independently ("sage --coverage ...modular/arithgroups/" or the like should show it)?

Thanks a lot in advance!


Cheers,
Georg



---

archive/issue_comments_038465.json:
```json
{
    "body": "Good catch, Georg! I will upload a patch shortly with the missing doctest, bringing doctest coverage in sage/modular back up to 100%. Georg, Johan: would either of you mind taking a quick look at the new patch?",
    "created_at": "2011-12-17T22:34:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5048",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5048#issuecomment-38465",
    "user": "davidloeffler"
}
```

Good catch, Georg! I will upload a patch shortly with the missing doctest, bringing doctest coverage in sage/modular back up to 100%. Georg, Johan: would either of you mind taking a quick look at the new patch?



---

archive/issue_comments_038466.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2011-12-17T22:34:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5048",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5048#issuecomment-38466",
    "user": "davidloeffler"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_038467.json:
```json
{
    "body": "apply over previous patch",
    "created_at": "2011-12-17T22:34:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5048",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5048#issuecomment-38467",
    "user": "davidloeffler"
}
```

apply over previous patch



---

archive/issue_comments_038468.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-12-17T22:35:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5048",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5048#issuecomment-38468",
    "user": "davidloeffler"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_038469.json:
```json
{
    "body": "Attachment [trac_5048-missingdoctest.patch](tarball://root/attachments/some-uuid/ticket5048/trac_5048-missingdoctest.patch) by davidloeffler created at 2011-12-17 22:35:40",
    "created_at": "2011-12-17T22:35:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5048",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5048#issuecomment-38469",
    "user": "davidloeffler"
}
```

Attachment [trac_5048-missingdoctest.patch](tarball://root/attachments/some-uuid/ticket5048/trac_5048-missingdoctest.patch) by davidloeffler created at 2011-12-17 22:35:40



---

archive/issue_comments_038470.json:
```json
{
    "body": "Attachment [trac_5048-missingdoctest.2.patch](tarball://root/attachments/some-uuid/ticket5048/trac_5048-missingdoctest.2.patch) by davidloeffler created at 2011-12-17 22:39:29\n\nNOT NEEDED! See comments",
    "created_at": "2011-12-17T22:39:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5048",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5048#issuecomment-38470",
    "user": "davidloeffler"
}
```

Attachment [trac_5048-missingdoctest.2.patch](tarball://root/attachments/some-uuid/ticket5048/trac_5048-missingdoctest.2.patch) by davidloeffler created at 2011-12-17 22:39:29

NOT NEEDED! See comments



---

archive/issue_comments_038471.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-12-17T22:43:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5048",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5048#issuecomment-38471",
    "user": "davidloeffler"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_038472.json:
```json
{
    "body": "Hang on a minute.\n\nIt is true that there is a doctest missing for this call method, but the missing doctest gets added in the next patch in the series (#11601). So I think we can ignore it here, since #11601 has a positive review; and I can safely reinstate Johan's positive review. \n\nSo: **ignore** the patch(es) I just uploaded -- it is not needed. I tried to obliterate the first patch by uploading a new blank patch on top of it, but made a hash of that. Perhaps it's time I went to bed.",
    "created_at": "2011-12-17T22:43:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5048",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5048#issuecomment-38472",
    "user": "davidloeffler"
}
```

Hang on a minute.

It is true that there is a doctest missing for this call method, but the missing doctest gets added in the next patch in the series (#11601). So I think we can ignore it here, since #11601 has a positive review; and I can safely reinstate Johan's positive review. 

So: **ignore** the patch(es) I just uploaded -- it is not needed. I tried to obliterate the first patch by uploading a new blank patch on top of it, but made a hash of that. Perhaps it's time I went to bed.



---

archive/issue_comments_038473.json:
```json
{
    "body": "Replying to [comment:20 davidloeffler]:\n> Hang on a minute.\n> \n> It is true that there is a doctest missing for this call method, but the missing doctest gets added in the next patch in the series (#11601). So I think we can ignore it here, since #11601 has a positive review; and I can safely reinstate Johan's positive review. \n> \n> So: **ignore** the patch(es) I just uploaded -- it is not needed. I tried to obliterate the first patch by uploading a new blank patch on top of it, but made a hash of that. Perhaps it's time I went to bed.\nIndeed.  I was about to mention the same thing, but your comment crossed mine. :).",
    "created_at": "2011-12-17T22:51:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5048",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5048#issuecomment-38473",
    "user": "johanbosman"
}
```

Replying to [comment:20 davidloeffler]:
> Hang on a minute.
> 
> It is true that there is a doctest missing for this call method, but the missing doctest gets added in the next patch in the series (#11601). So I think we can ignore it here, since #11601 has a positive review; and I can safely reinstate Johan's positive review. 
> 
> So: **ignore** the patch(es) I just uploaded -- it is not needed. I tried to obliterate the first patch by uploading a new blank patch on top of it, but made a hash of that. Perhaps it's time I went to bed.
Indeed.  I was about to mention the same thing, but your comment crossed mine. :).



---

archive/issue_comments_038474.json:
```json
{
    "body": "Changing keywords from \"congruence subgroup coercion\" to \"congruence subgroup coercion, sd35\".",
    "created_at": "2011-12-21T15:26:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5048",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5048#issuecomment-38474",
    "user": "saraedum"
}
```

Changing keywords from "congruence subgroup coercion" to "congruence subgroup coercion, sd35".



---

archive/issue_comments_038475.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2012-01-15T21:55:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5048",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5048#issuecomment-38475",
    "user": "jdemeyer"
}
```

Resolution: fixed



---

archive/issue_comments_038476.json:
```json
{
    "body": "Apply trac_5048-rebased_for_11422.patch\n\n(for the patchbot, so it can understand the prerequisites for #11709)",
    "created_at": "2012-03-10T14:17:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5048",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5048#issuecomment-38476",
    "user": "davidloeffler"
}
```

Apply trac_5048-rebased_for_11422.patch

(for the patchbot, so it can understand the prerequisites for #11709)
