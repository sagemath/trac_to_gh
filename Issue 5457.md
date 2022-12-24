# Issue 5457: Refactor symmetric functions

archive/issues_005457.json:
```json
{
    "body": "Assignee: @mwhansen\n\nCC:  sage-combinat @saliola @dwbump chrisjamesberg @zabrocki simonking\n\nRefactor symmetric functions to:\n- use a single entry point, as in MuPAD-Combinat. Something like:\n       S = SymmetricFunctions(field)\n       S.schur\n       S.jack(t).P\n       S.macdonald(t,q).Q\n       S.kSchur(3).H\n- use the coercion framework\n- use the category framework\n\nSee also:http://groups.google.com/group/sage-devel/msg/a49f3288fca1b75c\n\nIssue created by migration from https://trac.sagemath.org/ticket/5457\n\n",
    "created_at": "2009-03-08T20:53:00Z",
    "labels": [
        "combinatorics",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-5.4",
    "title": "Refactor symmetric functions",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5457",
    "user": "@nthiery"
}
```
Assignee: @mwhansen

CC:  sage-combinat @saliola @dwbump chrisjamesberg @zabrocki simonking

Refactor symmetric functions to:
- use a single entry point, as in MuPAD-Combinat. Something like:
       S = SymmetricFunctions(field)
       S.schur
       S.jack(t).P
       S.macdonald(t,q).Q
       S.kSchur(3).H
- use the coercion framework
- use the category framework

See also:http://groups.google.com/group/sage-devel/msg/a49f3288fca1b75c

Issue created by migration from https://trac.sagemath.org/ticket/5457





---

archive/issue_comments_042287.json:
```json
{
    "body": "Changing keywords from \"\" to \"symmetric functions, sd38, sd40\".",
    "created_at": "2012-07-15T04:38:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5457#issuecomment-42287",
    "user": "@anneschilling"
}
```

Changing keywords from "" to "symmetric functions, sd38, sd40".



---

archive/issue_comments_042288.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2012-07-15T04:55:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5457#issuecomment-42288",
    "user": "@anneschilling"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_042289.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2012-07-15T04:56:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5457#issuecomment-42289",
    "user": "@anneschilling"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_042290.json:
```json
{
    "body": "Hi Mike,\n\nI finished the doctests for the following files:\n\n- schur.py\n\n- homogeneous.py\n\n- elementrary.py\n\n- powersum.py\n\n- monomial.py\n\n- classical.py\n\n- dual.py\n\n- multiplicative.py\n\n- orthotriang.py\n\n- sf.py\n\nIn particular, at the beginning of sf.py I incorporated the tutorial that Jason and Nicolas\nwrote (which was further down the queue) and updated it. I marked them there as coauthors in\nthat file.\n\nThis leaves the doctests for \n\n- hall_littlewood.py\n\n- jack.py\n\n- llt.py\n\n- macdonald.py\n\n- ns_macdonald.py\n\n- sfa.py\n\nwhich I suppose you will do in the next couple of days?\nIn particular, in the sfa.py the deprecation warnings need to be activated which I have\nnot yet done.\n\nBest,\n\nAnne",
    "created_at": "2012-07-15T04:59:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5457#issuecomment-42290",
    "user": "@anneschilling"
}
```

Hi Mike,

I finished the doctests for the following files:

- schur.py

- homogeneous.py

- elementrary.py

- powersum.py

- monomial.py

- classical.py

- dual.py

- multiplicative.py

- orthotriang.py

- sf.py

In particular, at the beginning of sf.py I incorporated the tutorial that Jason and Nicolas
wrote (which was further down the queue) and updated it. I marked them there as coauthors in
that file.

This leaves the doctests for 

- hall_littlewood.py

- jack.py

- llt.py

- macdonald.py

- ns_macdonald.py

- sfa.py

which I suppose you will do in the next couple of days?
In particular, in the sfa.py the deprecation warnings need to be activated which I have
not yet done.

Best,

Anne



---

archive/issue_comments_042291.json:
```json
{
    "body": "Hi Mike,\n\nI completed the doctests for sfa.py and also rebased everything on top of 13109. Please put your changes to \n\n* hall_littlewood.py \n\n* jack.py \n\n* llt.py \n\n* macdonald.py \n\non top of the current patch trac_5457-symmetric_functions-mz.patch. Unfortunately we need to abandon the sage-combinat queue for the moment since it would be very cumbersome to keep it backward compatible with 13109. I will send you a separate e-mail on how to proceed.\n\nCheers,\n\nAnne",
    "created_at": "2012-07-17T06:34:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5457#issuecomment-42291",
    "user": "@anneschilling"
}
```

Hi Mike,

I completed the doctests for sfa.py and also rebased everything on top of 13109. Please put your changes to 

* hall_littlewood.py 

* jack.py 

* llt.py 

* macdonald.py 

on top of the current patch trac_5457-symmetric_functions-mz.patch. Unfortunately we need to abandon the sage-combinat queue for the moment since it would be very cumbersome to keep it backward compatible with 13109. I will send you a separate e-mail on how to proceed.

Cheers,

Anne



---

archive/issue_comments_042292.json:
```json
{
    "body": "Ok, patch is ready for review! It should apply and run cleanly on sage.5.2.rc0!\n\nAnne",
    "created_at": "2012-07-19T06:52:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5457#issuecomment-42292",
    "user": "@anneschilling"
}
```

Ok, patch is ready for review! It should apply and run cleanly on sage.5.2.rc0!

Anne



---

archive/issue_comments_042293.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2012-07-19T06:52:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5457#issuecomment-42293",
    "user": "@anneschilling"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_042294.json:
```json
{
    "body": "Apply [attachment:trac_5457-symmetric_functions-mz.patch]",
    "created_at": "2012-07-19T07:45:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5457#issuecomment-42294",
    "user": "@anneschilling"
}
```

Apply [attachment:trac_5457-symmetric_functions-mz.patch]



---

archive/issue_comments_042295.json:
```json
{
    "body": "Hi Dan!\n\nThank you very much for your comments on the failing doctests in \n\n* devel/sage/sage/algebras/nil_coxeter_algebra.py\n\n* devel/sage/sage/categories/realizations.py\n\nThey are fixed in the updated version of the patch. I do not get failures for \n\n* devel/sage/sage/sandpiles/sandpile.py\n\non my machine.\n\nlolita-4:sandpiles anne$ sage -t sandpile.py \nsage -t  \"devel/sage-sf/sage/sandpiles/sandpile.py\"         \n\t [19.0 s]\n \n----------------------------------------------------------------------\nAll tests passed!\nTotal time for all tests: 19.0 seconds\n\n\nAnne",
    "created_at": "2012-07-24T22:35:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5457#issuecomment-42295",
    "user": "@anneschilling"
}
```

Hi Dan!

Thank you very much for your comments on the failing doctests in 

* devel/sage/sage/algebras/nil_coxeter_algebra.py

* devel/sage/sage/categories/realizations.py

They are fixed in the updated version of the patch. I do not get failures for 

* devel/sage/sage/sandpiles/sandpile.py

on my machine.

lolita-4:sandpiles anne$ sage -t sandpile.py 
sage -t  "devel/sage-sf/sage/sandpiles/sandpile.py"         
	 [19.0 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 19.0 seconds


Anne



---

archive/issue_comments_042296.json:
```json
{
    "body": "Replying to [comment:20 aschilling]:\n> Hi Dan!\n> \n> Thank you very much for your comments on the failing doctests in \n> \n> * devel/sage/sage/algebras/nil_coxeter_algebra.py\n> \n> * devel/sage/sage/categories/realizations.py\n> \n> They are fixed in the updated version of the patch. I do not get failures for \n> \n> * devel/sage/sage/sandpiles/sandpile.py\n> \n> on my machine.\n\nI also get a doctest failure in sandpile.py with unpatched sage-5.2.rc0 so this failure is not caused by the patch.",
    "created_at": "2012-07-24T23:48:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5457#issuecomment-42296",
    "user": "@dwbump"
}
```

Replying to [comment:20 aschilling]:
> Hi Dan!
> 
> Thank you very much for your comments on the failing doctests in 
> 
> * devel/sage/sage/algebras/nil_coxeter_algebra.py
> 
> * devel/sage/sage/categories/realizations.py
> 
> They are fixed in the updated version of the patch. I do not get failures for 
> 
> * devel/sage/sage/sandpiles/sandpile.py
> 
> on my machine.

I also get a doctest failure in sandpile.py with unpatched sage-5.2.rc0 so this failure is not caused by the patch.



---

archive/issue_comments_042297.json:
```json
{
    "body": "Applies cleanly to sage-5.2 and passes all tests.",
    "created_at": "2012-07-30T18:31:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5457#issuecomment-42297",
    "user": "@dwbump"
}
```

Applies cleanly to sage-5.2 and passes all tests.



---

archive/issue_comments_042298.json:
```json
{
    "body": "The attached review patch trac_5457-review-as.patch incorporates most of the comments that Dan Bump raised in e-mail conversations.\n\nAnne",
    "created_at": "2012-07-30T21:28:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5457#issuecomment-42298",
    "user": "@anneschilling"
}
```

The attached review patch trac_5457-review-as.patch incorporates most of the comments that Dan Bump raised in e-mail conversations.

Anne



---

archive/issue_comments_042299.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-07-30T21:46:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5457#issuecomment-42299",
    "user": "@dwbump"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_042300.json:
```json
{
    "body": "This patch is a huge step forward for symmetric functions.\n\nIn addition to normal testing I spent quite a bit of time and privately sent comments (mainly on documentation) that have been taken into account in trac_5457-review-as.patch. I'm changing the status to positive review.",
    "created_at": "2012-07-30T21:46:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5457#issuecomment-42300",
    "user": "@dwbump"
}
```

This patch is a huge step forward for symmetric functions.

In addition to normal testing I spent quite a bit of time and privately sent comments (mainly on documentation) that have been taken into account in trac_5457-review-as.patch. I'm changing the status to positive review.



---

archive/issue_comments_042301.json:
```json
{
    "body": "Replying to [comment:25 bump]:\n> This patch is a huge step forward for symmetric functions.\n> \n> In addition to normal testing I spent quite a bit of time and privately sent comments (mainly on documentation) that have been taken into account in trac_5457-review-as.patch. I'm changing the status to positive review.\n\nDear Dan, Thank you so much for your thorough and quick review of this huge patch! Mike and I just finished the review patch. Tests pass on both of our machines.\n\nAnne",
    "created_at": "2012-07-31T01:37:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5457#issuecomment-42301",
    "user": "@anneschilling"
}
```

Replying to [comment:25 bump]:
> This patch is a huge step forward for symmetric functions.
> 
> In addition to normal testing I spent quite a bit of time and privately sent comments (mainly on documentation) that have been taken into account in trac_5457-review-as.patch. I'm changing the status to positive review.

Dear Dan, Thank you so much for your thorough and quick review of this huge patch! Mike and I just finished the review patch. Tests pass on both of our machines.

Anne



---

archive/issue_comments_042302.json:
```json
{
    "body": "I have reviewed the latest version of the patch and it still has positive review.",
    "created_at": "2012-07-31T02:20:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5457#issuecomment-42302",
    "user": "@dwbump"
}
```

I have reviewed the latest version of the patch and it still has positive review.



---

archive/issue_comments_042303.json:
```json
{
    "body": "Since http://trac.sagemath.org/sage_trac/ticket/12969 just got merged into sage-5.3.beta0, please also apply the attachment trac12969_rel_5457.patch on the ticket 12969 to this patch. Otherwise there will be doctest failures.\n\nThanks,\n\nAnne",
    "created_at": "2012-08-01T12:31:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5457#issuecomment-42303",
    "user": "@anneschilling"
}
```

Since http://trac.sagemath.org/sage_trac/ticket/12969 just got merged into sage-5.3.beta0, please also apply the attachment trac12969_rel_5457.patch on the ticket 12969 to this patch. Otherwise there will be doctest failures.

Thanks,

Anne



---

archive/issue_comments_042304.json:
```json
{
    "body": "This needs to be rebased to sage-5.3.beta0 (not yet released):\n\n```\npatching file sage/categories/realizations.py\nHunk #1 FAILED at 74\n1 out of 1 hunks FAILED -- saving rejects to file sage/categories/realizations.py.rej\npatching file sage/combinat/sf/classical.py\nHunk #3 FAILED at 88\n1 out of 9 hunks FAILED -- saving rejects to file sage/combinat/sf/classical.py.rej\npatching file sage/combinat/sf/sfa.py\nHunk #61 FAILED at 2589\n1 out of 63 hunks FAILED -- saving rejects to file sage/combinat/sf/sfa.py.rej\nabort: patch failed to apply\n```\n",
    "created_at": "2012-08-01T18:14:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5457#issuecomment-42304",
    "user": "@jdemeyer"
}
```

This needs to be rebased to sage-5.3.beta0 (not yet released):

```
patching file sage/categories/realizations.py
Hunk #1 FAILED at 74
1 out of 1 hunks FAILED -- saving rejects to file sage/categories/realizations.py.rej
patching file sage/combinat/sf/classical.py
Hunk #3 FAILED at 88
1 out of 9 hunks FAILED -- saving rejects to file sage/combinat/sf/classical.py.rej
patching file sage/combinat/sf/sfa.py
Hunk #61 FAILED at 2589
1 out of 63 hunks FAILED -- saving rejects to file sage/combinat/sf/sfa.py.rej
abort: patch failed to apply
```




---

archive/issue_comments_042305.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2012-08-01T18:15:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5457#issuecomment-42305",
    "user": "@jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_042306.json:
```json
{
    "body": "I rebased and folded the three patches with respect to sage-5.3.beta0 from yesterday.\nIt should apply cleanly now.\n\nMike and I are still going to fix one math bug that someone at FPSAC found.\n\nAnne",
    "created_at": "2012-08-02T23:18:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5457#issuecomment-42306",
    "user": "@anneschilling"
}
```

I rebased and folded the three patches with respect to sage-5.3.beta0 from yesterday.
It should apply cleanly now.

Mike and I are still going to fix one math bug that someone at FPSAC found.

Anne



---

archive/issue_comments_042307.json:
```json
{
    "body": "Hi Dan,\n\nOur new rebased patch is attached. You only need to apply trac_5457-symmetric_functions-mz.patch. Note that we did not fix apply_linear_morphism in /category/module_with_basis.py yet since Nicolas seems to have a review patch for this, but unfortunately his tests did not pass. Either he needs to fix his review patch or we will add your suggestion from the e-mail.\n\nAnne",
    "created_at": "2012-08-03T06:51:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5457#issuecomment-42307",
    "user": "@anneschilling"
}
```

Hi Dan,

Our new rebased patch is attached. You only need to apply trac_5457-symmetric_functions-mz.patch. Note that we did not fix apply_linear_morphism in /category/module_with_basis.py yet since Nicolas seems to have a review patch for this, but unfortunately his tests did not pass. Either he needs to fix his review patch or we will add your suggestion from the e-mail.

Anne



---

archive/issue_comments_042308.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2012-08-03T06:52:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5457#issuecomment-42308",
    "user": "@anneschilling"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_042309.json:
```json
{
    "body": "Note: I inserted in the queue the latest patch rebased for 5.3 beta0 from here. My review patch is also there, ready to be folded if you are happy with it.",
    "created_at": "2012-08-03T17:28:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5457#issuecomment-42309",
    "user": "@nthiery"
}
```

Note: I inserted in the queue the latest patch rebased for 5.3 beta0 from here. My review patch is also there, ready to be folded if you are happy with it.



---

archive/issue_comments_042310.json:
```json
{
    "body": "Dear Dan and Nicolas,\n\nThank you so much for your reviews and work on this patch! I incorporated the changes that Dan suggested by e-mail and folded Nicolas' review patch. In addition, Mike had some minor improvements in the documentation of llt.py which are incorporated.\n\nThe new patch should apply cleanly on sage-5.3.beta0.\n\nAnne",
    "created_at": "2012-08-04T00:10:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5457#issuecomment-42310",
    "user": "@anneschilling"
}
```

Dear Dan and Nicolas,

Thank you so much for your reviews and work on this patch! I incorporated the changes that Dan suggested by e-mail and folded Nicolas' review patch. In addition, Mike had some minor improvements in the documentation of llt.py which are incorporated.

The new patch should apply cleanly on sage-5.3.beta0.

Anne



---

archive/issue_comments_042311.json:
```json
{
    "body": "All tests pass with sage-5.3.beta0. The changes discussed over the last few days have all been incorporated. I think this is ready to go.",
    "created_at": "2012-08-04T13:20:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5457#issuecomment-42311",
    "user": "@dwbump"
}
```

All tests pass with sage-5.3.beta0. The changes discussed over the last few days have all been incorporated. I think this is ready to go.



---

archive/issue_comments_042312.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-08-04T13:21:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5457#issuecomment-42312",
    "user": "@dwbump"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_042313.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2012-08-08T12:30:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5457#issuecomment-42313",
    "user": "@jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_042314.json:
```json
{
    "body": "This fails on arando (32-bit i386 Linux):\n\n```\nsage -t --long \"devel/sage/sage/combinat/sf/llt.py\"\n**********************************************************************\nFile \"/var/lib/buildbot/build/sage/arando-1/arando_full/build/sage-5.3.beta1/devel/sage/sage/combinat/sf/llt.py\", line 329:\n    sage: cmp(L3Q, L3Z)\nExpected:\n    -1\nGot:\n    1\n**********************************************************************\n```\n",
    "created_at": "2012-08-08T12:30:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5457#issuecomment-42314",
    "user": "@jdemeyer"
}
```

This fails on arando (32-bit i386 Linux):

```
sage -t --long "devel/sage/sage/combinat/sf/llt.py"
**********************************************************************
File "/var/lib/buildbot/build/sage/arando-1/arando_full/build/sage-5.3.beta1/devel/sage/sage/combinat/sf/llt.py", line 329:
    sage: cmp(L3Q, L3Z)
Expected:
    -1
Got:
    1
**********************************************************************
```




---

archive/issue_comments_042315.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2012-08-08T20:25:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5457#issuecomment-42315",
    "user": "@anneschilling"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_042316.json:
```json
{
    "body": "Hi Jeroen,\n\nHmm, this is hard for us to check since we are not running our code on that operating system. We attached a patch which will hopefully fix the problem\n\nApply\n\n* [attachment:trac_5457-symmetric_functions-mz.patch]\n* [attachment:trac_5457_docfix-mz.patch]\n\nThanks,\n\nAnne",
    "created_at": "2012-08-08T20:27:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5457#issuecomment-42316",
    "user": "@anneschilling"
}
```

Hi Jeroen,

Hmm, this is hard for us to check since we are not running our code on that operating system. We attached a patch which will hopefully fix the problem

Apply

* [attachment:trac_5457-symmetric_functions-mz.patch]
* [attachment:trac_5457_docfix-mz.patch]

Thanks,

Anne



---

archive/issue_comments_042317.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-08-08T20:27:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5457#issuecomment-42317",
    "user": "@anneschilling"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_042318.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2012-08-09T06:27:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5457#issuecomment-42318",
    "user": "@jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_042319.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2012-08-09T06:27:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5457#issuecomment-42319",
    "user": "@jdemeyer"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_042320.json:
```json
{
    "body": "I think one of the original reviewers should review this additional patch.",
    "created_at": "2012-08-09T06:27:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5457#issuecomment-42320",
    "user": "@jdemeyer"
}
```

I think one of the original reviewers should review this additional patch.



---

archive/issue_comments_042321.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-08-09T16:47:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5457#issuecomment-42321",
    "user": "@dwbump"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_042322.json:
```json
{
    "body": "> I think one of the original reviewers should review this additional patch.\n\nThis adds a __cmp__ method for SymmetricFunctions, which was missing, and that\nwas uncovered by the test in llt.py. Two SymmetricFunctions instances are\ncompared equal if and only if they have the same base ring, which is as it\nshould be.\n\nUnless I'm missing something the patch is obviously correct. I ran --testall --long\nin the sf directory and all tests passed.",
    "created_at": "2012-08-09T16:47:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5457#issuecomment-42322",
    "user": "@dwbump"
}
```

> I think one of the original reviewers should review this additional patch.

This adds a __cmp__ method for SymmetricFunctions, which was missing, and that
was uncovered by the test in llt.py. Two SymmetricFunctions instances are
compared equal if and only if they have the same base ring, which is as it
should be.

Unless I'm missing something the patch is obviously correct. I ran --testall --long
in the sf directory and all tests passed.



---

archive/issue_comments_042323.json:
```json
{
    "body": "There is no compelling reason to have a cmp function for symmetric functions (nor its bases). The order has no meaning, and equality testing should be taken care of by UniqueRepresentation.\n\nSo altogether, I'd rather not add a cmp function, and instead would rather replace the failing test by:\n\n    sage: cmp(L3Q, L3Z) != 0\n\nwhich is platform independent, and is all we care about. We could even just discard this test.\n\nNow, I don't want to slow down the integration of this patch, so I am happy leaving this issue for a latter ticket, at the author's choice.\n\nCheers,\n                   Nicolas",
    "created_at": "2012-08-09T18:11:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5457#issuecomment-42323",
    "user": "@nthiery"
}
```

There is no compelling reason to have a cmp function for symmetric functions (nor its bases). The order has no meaning, and equality testing should be taken care of by UniqueRepresentation.

So altogether, I'd rather not add a cmp function, and instead would rather replace the failing test by:

    sage: cmp(L3Q, L3Z) != 0

which is platform independent, and is all we care about. We could even just discard this test.

Now, I don't want to slow down the integration of this patch, so I am happy leaving this issue for a latter ticket, at the author's choice.

Cheers,
                   Nicolas



---

archive/issue_comments_042324.json:
```json
{
    "body": "As per Nicolas' suggestion, we are deleting the __cmp__ function from llt and moving and modifying the doctests elsewhere in the llt.py file.",
    "created_at": "2012-08-10T20:39:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5457#issuecomment-42324",
    "user": "@zabrocki"
}
```

As per Nicolas' suggestion, we are deleting the __cmp__ function from llt and moving and modifying the doctests elsewhere in the llt.py file.



---

archive/issue_comments_042325.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2012-08-10T20:39:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5457#issuecomment-42325",
    "user": "@zabrocki"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_042326.json:
```json
{
    "body": "This new patch deletes the function cmp from llt.py and inserts doctests into init in llt.py",
    "created_at": "2012-08-10T20:52:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5457#issuecomment-42326",
    "user": "@zabrocki"
}
```

This new patch deletes the function cmp from llt.py and inserts doctests into init in llt.py



---

archive/issue_comments_042327.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2012-08-10T20:52:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5457#issuecomment-42327",
    "user": "@zabrocki"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_042328.json:
```json
{
    "body": "sage -testall passes on both mine and Mike's machine (both MacOS) with trac_5457-symmetric_functions-mz.patch and trac_5457_docfix2-mz.patch applied.\n\nDan and/or Nicolas, please set a positive review if you are happy with the changes.\n\nThanks!\n\nAnne",
    "created_at": "2012-08-10T22:00:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5457#issuecomment-42328",
    "user": "@anneschilling"
}
```

sage -testall passes on both mine and Mike's machine (both MacOS) with trac_5457-symmetric_functions-mz.patch and trac_5457_docfix2-mz.patch applied.

Dan and/or Nicolas, please set a positive review if you are happy with the changes.

Thanks!

Anne



---

archive/issue_comments_042329.json:
```json
{
    "body": "Nicolas argued that there is no real reason for Sym to have a `__cmp__`\nmethod and there is no reason for the test to be deterministic. We don't\ncare if two rings or ring elements are > or < than each other, just whether they are distinct.\nTherefore the test that failed can be rewritten and the `__cmp___` method\nis not needed.\n\nThis patch removes the `__cmp__` method from llt polynomials instead\nof adding one for sf. In fact, `SymmetricFunctions` should not have had a\n`__cmp__` method because it already inherits one from `UniqueRepresentation`.\n(Tested!) On the other hand, there is no reason for the test as previously written\nto be deterministic. So this is the correct approach.",
    "created_at": "2012-08-11T00:05:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5457#issuecomment-42329",
    "user": "@dwbump"
}
```

Nicolas argued that there is no real reason for Sym to have a `__cmp__`
method and there is no reason for the test to be deterministic. We don't
care if two rings or ring elements are > or < than each other, just whether they are distinct.
Therefore the test that failed can be rewritten and the `__cmp___` method
is not needed.

This patch removes the `__cmp__` method from llt polynomials instead
of adding one for sf. In fact, `SymmetricFunctions` should not have had a
`__cmp__` method because it already inherits one from `UniqueRepresentation`.
(Tested!) On the other hand, there is no reason for the test as previously written
to be deterministic. So this is the correct approach.



---

archive/issue_comments_042330.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-08-11T00:05:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5457#issuecomment-42330",
    "user": "@dwbump"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_042331.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2012-08-11T00:12:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5457#issuecomment-42331",
    "user": "@dwbump"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_042332.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2012-08-11T12:40:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5457#issuecomment-42332",
    "user": "@dwbump"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_042333.json:
```json
{
    "body": "Thank you Dan for the review!\n\nAnne",
    "created_at": "2012-08-11T15:17:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5457#issuecomment-42333",
    "user": "@anneschilling"
}
```

Thank you Dan for the review!

Anne



---

archive/issue_comments_042334.json:
```json
{
    "body": "Folded patches.",
    "created_at": "2012-08-12T22:44:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5457#issuecomment-42334",
    "user": "@anneschilling"
}
```

Folded patches.



---

archive/issue_comments_042335.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2012-08-14T07:01:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5457#issuecomment-42335",
    "user": "@jdemeyer"
}
```

Resolution: fixed



---

archive/issue_comments_042336.json:
```json
{
    "body": "Replying to [comment:60 jdemeyer]:\n\nWow, unbelievable!! Thank you everyone for your work on this!\n\nAnne",
    "created_at": "2012-08-14T14:19:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5457#issuecomment-42336",
    "user": "@anneschilling"
}
```

Replying to [comment:60 jdemeyer]:

Wow, unbelievable!! Thank you everyone for your work on this!

Anne



---

archive/issue_comments_042337.json:
```json
{
    "body": "Replying to [comment:61 aschilling]:\n> Wow, unbelievable!! Thank you everyone for your work on this!\n\nCongratulations!\n\nAnd thanks on behalf of all symmetric function users!\n\n                                 Nicolas",
    "created_at": "2012-08-19T18:35:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5457#issuecomment-42337",
    "user": "@nthiery"
}
```

Replying to [comment:61 aschilling]:
> Wow, unbelievable!! Thank you everyone for your work on this!

Congratulations!

And thanks on behalf of all symmetric function users!

                                 Nicolas



---

archive/issue_comments_042338.json:
```json
{
    "body": "Changing keywords from \"symmetric functions, sd38, sd40\" to \"symmetric functions, days38, sd40\".",
    "created_at": "2012-08-23T15:41:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5457#issuecomment-42338",
    "user": "@nthiery"
}
```

Changing keywords from "symmetric functions, sd38, sd40" to "symmetric functions, days38, sd40".



---

archive/issue_comments_042339.json:
```json
{
    "body": "**Additional patch** [attachment:5457_long_time.patch] needs review.",
    "created_at": "2012-08-31T21:41:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5457#issuecomment-42339",
    "user": "@jdemeyer"
}
```

**Additional patch** [attachment:5457_long_time.patch] needs review.



---

archive/issue_comments_042340.json:
```json
{
    "body": "Additional patch is a blocker, please review.",
    "created_at": "2012-09-01T09:13:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5457#issuecomment-42340",
    "user": "@jdemeyer"
}
```

Additional patch is a blocker, please review.



---

archive/issue_comments_042341.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2012-09-01T09:13:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5457#issuecomment-42341",
    "user": "@jdemeyer"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_042342.json:
```json
{
    "body": "the patch looks good and works properly. \u00a0I tested it on sage-5.3.rc0 using both --long and not --long and all tests pass. \u00a0I give it a positive review.",
    "created_at": "2012-09-01T11:49:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5457#issuecomment-42342",
    "user": "@zabrocki"
}
```

the patch looks good and works properly.  I tested it on sage-5.3.rc0 using both --long and not --long and all tests pass.  I give it a positive review.



---

archive/issue_comments_042343.json:
```json
{
    "body": "Changing priority from blocker to major.",
    "created_at": "2012-09-01T13:01:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5457#issuecomment-42343",
    "user": "@jdemeyer"
}
```

Changing priority from blocker to major.



---

archive/issue_comments_042344.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2012-09-01T13:01:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5457#issuecomment-42344",
    "user": "@jdemeyer"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_042345.json:
```json
{
    "body": "Changing status from closed to new.",
    "created_at": "2012-09-01T13:01:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5457#issuecomment-42345",
    "user": "@jdemeyer"
}
```

Changing status from closed to new.



---

archive/issue_comments_042346.json:
```json
{
    "body": "I hate to be the bringer of bad news, but after playing a bit with this patch, I think I found an actual bug:\n\n```\nsage: HS3t2 = SymmetricFunctions(QQ).llt(3,t=2).hspin()\nsage: TestSuite(HS3t2).run()\nFailure in _test_associativity:\nTraceback (most recent call last):\n  File \"/release/sage-5.3.rc1/local/lib/python2.7/site-packages/sage/misc/sage_unittest.py\", line 275, in run\n    test_method(tester = tester)\n  File \"/release/sage-5.3.rc1/local/lib/python2.7/site-packages/sage/categories/semigroups.py\", line 120, in _test_associativity\n    tester.assert_((x * y) * z == x * (y * z))\n  File \"/release/sage-5.3.rc1/local/lib/python2.7/site-packages/sage/categories/algebras.py\", line 202, in __mul__\n    return self._mul_(right)\n  File \"/release/sage-5.3.rc1/local/lib/python2.7/site-packages/sage/categories/magmas.py\", line 361, in _mul_parent\n    return self.parent().product(self, other)\n  File \"/release/sage-5.3.rc1/local/lib/python2.7/site-packages/sage/categories/algebras_with_basis.py\", line 351, in _product_from_combinatorial_algebra_multiply\n    m = self._multiply(left, right)\n  File \"/release/sage-5.3.rc1/local/lib/python2.7/site-packages/sage/combinat/sf/llt.py\", line 683, in _multiply\n    return self( self._m(left) * self._m(right) )\n  File \"parent.pyx\", line 804, in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:7228)\n  File \"morphism.pyx\", line 243, in sage.categories.morphism.SetMorphism._call_ (sage/categories/morphism.c:4412)\n  File \"/release/sage-5.3.rc1/local/lib/python2.7/site-packages/sage/combinat/sf/llt.py\", line 617, in _self_to_m\n    return self._m._from_cache(x, self._m_cache, self._self_to_m_cache, t = self.t)\n  File \"/release/sage-5.3.rc1/local/lib/python2.7/site-packages/sage/combinat/sf/sfa.py\", line 857, in _from_cache\n    cache_function(sum(part))\n  File \"/release/sage-5.3.rc1/local/lib/python2.7/site-packages/sage/combinat/sf/llt.py\", line 714, in _m_cache\n    self._m_to_self_cache, to_other_function = self._to_m)\n  File \"/release/sage-5.3.rc1/local/lib/python2.7/site-packages/sage/combinat/sf/sfa.py\", line 1057, in _invert_morphism\n    known_matrix_n[i,j] = value\n  File \"matrix0.pyx\", line 1415, in sage.matrix.matrix0.Matrix.__setitem__ (sage/matrix/matrix0.c:6745)\n  File \"matrix0.pyx\", line 1520, in sage.matrix.matrix0.Matrix._coerce_element (sage/matrix/matrix0.c:7937)\n  File \"parent.pyx\", line 804, in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:7228)\n  File \"coerce_maps.pyx\", line 82, in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3547)\n  File \"coerce_maps.pyx\", line 77, in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3449)\n  File \"rational.pyx\", line 371, in sage.rings.rational.Rational.__init__ (sage/rings/rational.c:6534)\n  File \"rational.pyx\", line 484, in sage.rings.rational.Rational.__set_value (sage/rings/rational.c:7337)\n  File \"fraction_field_element.pyx\", line 736, in sage.rings.fraction_field_element.FractionFieldElement._rational_ (sage/rings/fraction_field_element.c:7197)\n  File \"parent.pyx\", line 804, in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:7228)\n  File \"polynomial_element.pyx\", line 6521, in sage.rings.polynomial.polynomial_element.ConstantPolynomialSection._call_ (sage/rings/polynomial/polynomial_element.c:46753)\nTypeError: not a constant polynomial\n------------------------------------------------------------\nFailure in _test_distributivity:\n[...]\nTypeError: not a constant polynomial\n------------------------------------------------------------\nFailure in _test_one:\n[...]\nTypeError: not a constant polynomial\n------------------------------------------------------------\nFailure in _test_prod:\n[...]\nTypeError: not a constant polynomial\n------------------------------------------------------------\nThe following tests failed: _test_associativity, _test_distributivity, _test_one, _test_prod\n```\n",
    "created_at": "2012-09-01T13:01:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5457#issuecomment-42346",
    "user": "@jdemeyer"
}
```

I hate to be the bringer of bad news, but after playing a bit with this patch, I think I found an actual bug:

```
sage: HS3t2 = SymmetricFunctions(QQ).llt(3,t=2).hspin()
sage: TestSuite(HS3t2).run()
Failure in _test_associativity:
Traceback (most recent call last):
  File "/release/sage-5.3.rc1/local/lib/python2.7/site-packages/sage/misc/sage_unittest.py", line 275, in run
    test_method(tester = tester)
  File "/release/sage-5.3.rc1/local/lib/python2.7/site-packages/sage/categories/semigroups.py", line 120, in _test_associativity
    tester.assert_((x * y) * z == x * (y * z))
  File "/release/sage-5.3.rc1/local/lib/python2.7/site-packages/sage/categories/algebras.py", line 202, in __mul__
    return self._mul_(right)
  File "/release/sage-5.3.rc1/local/lib/python2.7/site-packages/sage/categories/magmas.py", line 361, in _mul_parent
    return self.parent().product(self, other)
  File "/release/sage-5.3.rc1/local/lib/python2.7/site-packages/sage/categories/algebras_with_basis.py", line 351, in _product_from_combinatorial_algebra_multiply
    m = self._multiply(left, right)
  File "/release/sage-5.3.rc1/local/lib/python2.7/site-packages/sage/combinat/sf/llt.py", line 683, in _multiply
    return self( self._m(left) * self._m(right) )
  File "parent.pyx", line 804, in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:7228)
  File "morphism.pyx", line 243, in sage.categories.morphism.SetMorphism._call_ (sage/categories/morphism.c:4412)
  File "/release/sage-5.3.rc1/local/lib/python2.7/site-packages/sage/combinat/sf/llt.py", line 617, in _self_to_m
    return self._m._from_cache(x, self._m_cache, self._self_to_m_cache, t = self.t)
  File "/release/sage-5.3.rc1/local/lib/python2.7/site-packages/sage/combinat/sf/sfa.py", line 857, in _from_cache
    cache_function(sum(part))
  File "/release/sage-5.3.rc1/local/lib/python2.7/site-packages/sage/combinat/sf/llt.py", line 714, in _m_cache
    self._m_to_self_cache, to_other_function = self._to_m)
  File "/release/sage-5.3.rc1/local/lib/python2.7/site-packages/sage/combinat/sf/sfa.py", line 1057, in _invert_morphism
    known_matrix_n[i,j] = value
  File "matrix0.pyx", line 1415, in sage.matrix.matrix0.Matrix.__setitem__ (sage/matrix/matrix0.c:6745)
  File "matrix0.pyx", line 1520, in sage.matrix.matrix0.Matrix._coerce_element (sage/matrix/matrix0.c:7937)
  File "parent.pyx", line 804, in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:7228)
  File "coerce_maps.pyx", line 82, in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3547)
  File "coerce_maps.pyx", line 77, in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3449)
  File "rational.pyx", line 371, in sage.rings.rational.Rational.__init__ (sage/rings/rational.c:6534)
  File "rational.pyx", line 484, in sage.rings.rational.Rational.__set_value (sage/rings/rational.c:7337)
  File "fraction_field_element.pyx", line 736, in sage.rings.fraction_field_element.FractionFieldElement._rational_ (sage/rings/fraction_field_element.c:7197)
  File "parent.pyx", line 804, in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:7228)
  File "polynomial_element.pyx", line 6521, in sage.rings.polynomial.polynomial_element.ConstantPolynomialSection._call_ (sage/rings/polynomial/polynomial_element.c:46753)
TypeError: not a constant polynomial
------------------------------------------------------------
Failure in _test_distributivity:
[...]
TypeError: not a constant polynomial
------------------------------------------------------------
Failure in _test_one:
[...]
TypeError: not a constant polynomial
------------------------------------------------------------
Failure in _test_prod:
[...]
TypeError: not a constant polynomial
------------------------------------------------------------
The following tests failed: _test_associativity, _test_distributivity, _test_one, _test_prod
```




---

archive/issue_comments_042347.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2012-09-01T13:01:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5457#issuecomment-42347",
    "user": "@jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_042348.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2012-09-01T13:01:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5457#issuecomment-42348",
    "user": "@jdemeyer"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_042349.json:
```json
{
    "body": "Just an FYI, this does not seem to be a new bug introduced by this patch.  Doc tests currently do not seem to test extensively enough to catch this (but once I knew the bug existed I was able to trigger it in all kinds of ways).  I think that I've tracked down the problem.  Here is a one line fix (class LLT_generic, method _m_cache):\n\n`-        self._invert_morphism(n, self.base_ring(), self._self_to_m_cache, \\`\n\n`+        self._invert_morphism(n, QQt, self._self_to_m_cache, \\`\n\nI will post a patch later today when I am confident that this actually fixes the problem and that there aren't similar bugs in jack/hall_littlewood/macdonald.",
    "created_at": "2012-09-01T15:37:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5457#issuecomment-42349",
    "user": "@zabrocki"
}
```

Just an FYI, this does not seem to be a new bug introduced by this patch.  Doc tests currently do not seem to test extensively enough to catch this (but once I knew the bug existed I was able to trigger it in all kinds of ways).  I think that I've tracked down the problem.  Here is a one line fix (class LLT_generic, method _m_cache):

`-        self._invert_morphism(n, self.base_ring(), self._self_to_m_cache, \`

`+        self._invert_morphism(n, QQt, self._self_to_m_cache, \`

I will post a patch later today when I am confident that this actually fixes the problem and that there aren't similar bugs in jack/hall_littlewood/macdonald.



---

archive/issue_comments_042350.json:
```json
{
    "body": "I also found that the tests that are currently in llt.py will fail if they are run separately.\n\n\n```\nsage: HSp3 = SymmetricFunctions(FractionField(QQ['t'])).llt(3).hspin()\nsage: TestSuite(HSp3).run(skip = [\"_test_associativity\", \"_test_distributivity\", \"_test_prod\"])\nsage: HS3t2 = SymmetricFunctions(QQ).llt(3,t=2).hspin()\nsage: TestSuite(HS3t2).run(skip = [\"_test_associativity\", \"_test_distributivity\", \"_test_prod\"])\n```\n\n\nExecutes without errors (even without the 'skip's).  However, if you delete the first two lines then these tests fail.  I will fix this by putting these tests in their own block.",
    "created_at": "2012-09-01T17:25:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5457#issuecomment-42350",
    "user": "@zabrocki"
}
```

I also found that the tests that are currently in llt.py will fail if they are run separately.


```
sage: HSp3 = SymmetricFunctions(FractionField(QQ['t'])).llt(3).hspin()
sage: TestSuite(HSp3).run(skip = ["_test_associativity", "_test_distributivity", "_test_prod"])
sage: HS3t2 = SymmetricFunctions(QQ).llt(3,t=2).hspin()
sage: TestSuite(HS3t2).run(skip = ["_test_associativity", "_test_distributivity", "_test_prod"])
```


Executes without errors (even without the 'skip's).  However, if you delete the first two lines then these tests fail.  I will fix this by putting these tests in their own block.



---

archive/issue_comments_042351.json:
```json
{
    "body": "The new attachment fixes the bug and makes the document changes that will test for the bug.  I removed the `skip` commands from two of the `TestSuite` commands since they weren't particularly long executions before, but they should have been the very tests which caught this bug.",
    "created_at": "2012-09-01T18:21:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5457#issuecomment-42351",
    "user": "@zabrocki"
}
```

The new attachment fixes the bug and makes the document changes that will test for the bug.  I removed the `skip` commands from two of the `TestSuite` commands since they weren't particularly long executions before, but they should have been the very tests which caught this bug.



---

archive/issue_comments_042352.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2012-09-01T18:21:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5457#issuecomment-42352",
    "user": "@zabrocki"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_042353.json:
```json
{
    "body": "Replying to [comment:70 zabrocki]:\n> Just an FYI, this does not seem to be a new bug introduced by this patch.\nWhat do you mean?  The doctest is testing code which did not exist before.  So I would say the bug was introduced by this patch.",
    "created_at": "2012-09-01T18:52:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5457#issuecomment-42353",
    "user": "@jdemeyer"
}
```

Replying to [comment:70 zabrocki]:
> Just an FYI, this does not seem to be a new bug introduced by this patch.
What do you mean?  The doctest is testing code which did not exist before.  So I would say the bug was introduced by this patch.



---

archive/issue_comments_042354.json:
```json
{
    "body": "Attachment [5457_long_time.patch](tarball://root/attachments/some-uuid/ticket5457/5457_long_time.patch) by @jdemeyer created at 2012-09-01 18:57:22\n\nAdditional patch",
    "created_at": "2012-09-01T18:57:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5457#issuecomment-42354",
    "user": "@jdemeyer"
}
```

Attachment [5457_long_time.patch](tarball://root/attachments/some-uuid/ticket5457/5457_long_time.patch) by @jdemeyer created at 2012-09-01 18:57:22

Additional patch



---

archive/issue_comments_042355.json:
```json
{
    "body": "Attachment [trac_5457-symmetric_functions-mz.patch](tarball://root/attachments/some-uuid/ticket5457/trac_5457-symmetric_functions-mz.patch) by @jdemeyer created at 2012-09-01 18:58:18\n\nI rebased the three patches (there was some fuzz) and made some additional changes to [attachment:5457_long_time.patch] (so that patch needs review again).",
    "created_at": "2012-09-01T18:58:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5457#issuecomment-42355",
    "user": "@jdemeyer"
}
```

Attachment [trac_5457-symmetric_functions-mz.patch](tarball://root/attachments/some-uuid/ticket5457/trac_5457-symmetric_functions-mz.patch) by @jdemeyer created at 2012-09-01 18:58:18

I rebased the three patches (there was some fuzz) and made some additional changes to [attachment:5457_long_time.patch] (so that patch needs review again).



---

archive/issue_comments_042356.json:
```json
{
    "body": "Replying to [comment:73 jdemeyer]:\n> Replying to [comment:70 zabrocki]:\n> > Just an FYI, this does not seem to be a new bug introduced by this patch.\n> What do you mean?  The doctest is testing code which did not exist before.  So I would say the bug was introduced by this patch.\n\nThe failures are related to failures that already existed before this patch.\nOn sage 5.0.1 (plain) one obtains\n\n```\nsage: LLTHSpin(QQ,3,t=2)\nLLT polynomials in the HSp basis at level 3 with t=2 over Rational Field\nsage: H = LLTHSpin(QQ,3,t=2)\nsage: s = SFASchur(QQ)\nsage: s(H([2,1]))\nERROR: An unexpected error occurred while tokenizing input\nThe following traceback may be corrupted or invalid\nThe error message is: ('EOF in multi-line statement', (1760, 0))\n```\n\n\nAnne",
    "created_at": "2012-09-01T20:14:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5457#issuecomment-42356",
    "user": "@anneschilling"
}
```

Replying to [comment:73 jdemeyer]:
> Replying to [comment:70 zabrocki]:
> > Just an FYI, this does not seem to be a new bug introduced by this patch.
> What do you mean?  The doctest is testing code which did not exist before.  So I would say the bug was introduced by this patch.

The failures are related to failures that already existed before this patch.
On sage 5.0.1 (plain) one obtains

```
sage: LLTHSpin(QQ,3,t=2)
LLT polynomials in the HSp basis at level 3 with t=2 over Rational Field
sage: H = LLTHSpin(QQ,3,t=2)
sage: s = SFASchur(QQ)
sage: s(H([2,1]))
ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (1760, 0))
```


Anne



---

archive/issue_comments_042357.json:
```json
{
    "body": "I reviewed and tested both patches (by applying 5457_long_time.patch and then trac_5457_llt_doc_and_bug_fix-mz.patch in this order). Tests pass and the bug seems to be fix (if I only apply  5457_long_time.patch tests do not pass, so the patches should be applied together).\n\nJeroen, I have a question. trac_5457-symmetric_functions-mz.patch was already merged into sage-5.2.beta2. Why did you rebase that patch again? Will it be merged again in a different version of sage? I am asking since in the sage-combinat queue it is currently guarded by sage-5.3.beta2.\n\nThanks,\n\nAnne",
    "created_at": "2012-09-02T03:17:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5457#issuecomment-42357",
    "user": "@anneschilling"
}
```

I reviewed and tested both patches (by applying 5457_long_time.patch and then trac_5457_llt_doc_and_bug_fix-mz.patch in this order). Tests pass and the bug seems to be fix (if I only apply  5457_long_time.patch tests do not pass, so the patches should be applied together).

Jeroen, I have a question. trac_5457-symmetric_functions-mz.patch was already merged into sage-5.2.beta2. Why did you rebase that patch again? Will it be merged again in a different version of sage? I am asking since in the sage-combinat queue it is currently guarded by sage-5.3.beta2.

Thanks,

Anne



---

archive/issue_comments_042358.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-09-02T03:17:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5457#issuecomment-42358",
    "user": "@anneschilling"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_042359.json:
```json
{
    "body": "Replying to [comment:76 aschilling]:\n> Will it be merged again in a different version of sage?\nYes, I don't want to merge any more new patches in sage-5.3 so it will be removed from sage-5.3 and then merged again in sage-5.4 such that it can be tested better.  Does this cause trouble?",
    "created_at": "2012-09-02T21:39:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5457#issuecomment-42359",
    "user": "@jdemeyer"
}
```

Replying to [comment:76 aschilling]:
> Will it be merged again in a different version of sage?
Yes, I don't want to merge any more new patches in sage-5.3 so it will be removed from sage-5.3 and then merged again in sage-5.4 such that it can be tested better.  Does this cause trouble?



---

archive/issue_comments_042360.json:
```json
{
    "body": "Replying to [comment:78 jdemeyer]:\n> Replying to [comment:76 aschilling]:\n> > Will it be merged again in a different version of sage?\n> Yes, I don't want to merge any more new patches in sage-5.3 so it will be removed from sage-5.3 and then merged again in sage-5.4 such that it can be tested better.  Does this cause trouble?\n\nMike's patch fixes a bug that is actually in the current version of Sage (as I outlined above). Wouldn't it be better to merge the two extra patches into sage-5.3 instead? Quite a lot of other patches depend on this patch (plus an upcoming book).\n\nThanks,\n\nAnne",
    "created_at": "2012-09-03T00:55:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5457#issuecomment-42360",
    "user": "@anneschilling"
}
```

Replying to [comment:78 jdemeyer]:
> Replying to [comment:76 aschilling]:
> > Will it be merged again in a different version of sage?
> Yes, I don't want to merge any more new patches in sage-5.3 so it will be removed from sage-5.3 and then merged again in sage-5.4 such that it can be tested better.  Does this cause trouble?

Mike's patch fixes a bug that is actually in the current version of Sage (as I outlined above). Wouldn't it be better to merge the two extra patches into sage-5.3 instead? Quite a lot of other patches depend on this patch (plus an upcoming book).

Thanks,

Anne



---

archive/issue_comments_042361.json:
```json
{
    "body": "Replying to [comment:79 aschilling]:\n> Mike's patch fixes a bug that is actually in the current version of Sage (as I outlined above). Wouldn't it be better to merge the two extra patches into sage-5.3 instead? Quite a lot of other patches depend on this patch (plus an upcoming book).\nI believe everything you say in this paragraph, but I see no arguments to merge it in sage-5.3.\n\nYou have to convince me that this patch will absolutely not break anything on any system, nor cause doctest timeouts.",
    "created_at": "2012-09-03T06:47:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5457#issuecomment-42361",
    "user": "@jdemeyer"
}
```

Replying to [comment:79 aschilling]:
> Mike's patch fixes a bug that is actually in the current version of Sage (as I outlined above). Wouldn't it be better to merge the two extra patches into sage-5.3 instead? Quite a lot of other patches depend on this patch (plus an upcoming book).
I believe everything you say in this paragraph, but I see no arguments to merge it in sage-5.3.

You have to convince me that this patch will absolutely not break anything on any system, nor cause doctest timeouts.



---

archive/issue_comments_042362.json:
```json
{
    "body": "Ah shoot, my comment did not get through yesterday; well, it's a bit outaded, but here it is anyway ...\n\nReplying to [comment:78 jdemeyer]:\n> Replying to [comment:76 aschilling]:\n> > Will it be merged again in a different version of sage?\n> Yes, I don't want to merge any more new patches in sage-5.3 so it will be removed from sage-5.3 and then merged again in sage-5.4 such that it can be tested better.  Does this cause trouble?\n\nTechnically, the Sage-Combinat queue can't handle patches that are merged and then unmerged. Now, this just means that we will have to everyone using a 5.3 beta to switch to 5.3 final; not a big deal.\n\nAnne, Mike: are there specific deadlines (e.g. the book or meetings) for which waiting for 5.4 could be a bother?\n\nOther than that, it's quite a big patch, on a very central feature for people in algebraic combinatorics; and the authors (Mike and Anne mostly) did put quite a lot of work and energy into it. So it will be quite frustrating for theim to not be able to cross it out of their TODO list while the semester starts. But that's life ...\n\nCheers,\n                              Nicolas",
    "created_at": "2012-09-03T11:09:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5457#issuecomment-42362",
    "user": "@nthiery"
}
```

Ah shoot, my comment did not get through yesterday; well, it's a bit outaded, but here it is anyway ...

Replying to [comment:78 jdemeyer]:
> Replying to [comment:76 aschilling]:
> > Will it be merged again in a different version of sage?
> Yes, I don't want to merge any more new patches in sage-5.3 so it will be removed from sage-5.3 and then merged again in sage-5.4 such that it can be tested better.  Does this cause trouble?

Technically, the Sage-Combinat queue can't handle patches that are merged and then unmerged. Now, this just means that we will have to everyone using a 5.3 beta to switch to 5.3 final; not a big deal.

Anne, Mike: are there specific deadlines (e.g. the book or meetings) for which waiting for 5.4 could be a bother?

Other than that, it's quite a big patch, on a very central feature for people in algebraic combinatorics; and the authors (Mike and Anne mostly) did put quite a lot of work and energy into it. So it will be quite frustrating for theim to not be able to cross it out of their TODO list while the semester starts. But that's life ...

Cheers,
                              Nicolas



---

archive/issue_comments_042363.json:
```json
{
    "body": "Replying to [comment:81 nthiery]:\n> So it will be quite frustrating for theim to not be able to cross it out of their TODO list while the semester starts.\nBut if the patch has *positive review*, then it is effectively off the TODO list, right?  Personally, I don't think it makes a big difference for a patch Author whether a patch gets merged in sage-5.3 or sage-5.4.",
    "created_at": "2012-09-03T11:26:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5457#issuecomment-42363",
    "user": "@jdemeyer"
}
```

Replying to [comment:81 nthiery]:
> So it will be quite frustrating for theim to not be able to cross it out of their TODO list while the semester starts.
But if the patch has *positive review*, then it is effectively off the TODO list, right?  Personally, I don't think it makes a big difference for a patch Author whether a patch gets merged in sage-5.3 or sage-5.4.



---

archive/issue_comments_042364.json:
```json
{
    "body": "My only worry is that several patches with positive reviews (#8899, #13399, #13404) were all reviewed on versions of sage where #5457 was already integrated.  Until last night #8899 and #13399 didn't have #5457 as a dependency (but should have) and #13404 depends on #13399.  I hope that there aren't other patches that are not similarly needed to be pushed forward that I am unaware of.",
    "created_at": "2012-09-03T11:41:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5457#issuecomment-42364",
    "user": "@zabrocki"
}
```

My only worry is that several patches with positive reviews (#8899, #13399, #13404) were all reviewed on versions of sage where #5457 was already integrated.  Until last night #8899 and #13399 didn't have #5457 as a dependency (but should have) and #13404 depends on #13399.  I hope that there aren't other patches that are not similarly needed to be pushed forward that I am unaware of.



---

archive/issue_comments_042365.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2012-09-03T11:50:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5457#issuecomment-42365",
    "user": "@jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_042366.json:
```json
{
    "body": "A small detail: the last patch needs a proper commit message.",
    "created_at": "2012-09-03T11:50:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5457#issuecomment-42366",
    "user": "@jdemeyer"
}
```

A small detail: the last patch needs a proper commit message.



---

archive/issue_comments_042367.json:
```json
{
    "body": "I'm not sure what you want in the commit message and I don't have permission to replace the previous version.  If you are satisfied with that change then please adjust the \"apply\" list so that the second version is the one that is used.",
    "created_at": "2012-09-03T12:35:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5457#issuecomment-42367",
    "user": "@zabrocki"
}
```

I'm not sure what you want in the commit message and I don't have permission to replace the previous version.  If you are satisfied with that change then please adjust the "apply" list so that the second version is the one that is used.



---

archive/issue_comments_042368.json:
```json
{
    "body": "Replying to [comment:85 zabrocki]:\n> I'm not sure what you want in the commit message\nWell, I don't want anything refering to `[mq]` or the patch name.  So if you delete the second line of the commit message in your patch, that will be fine.",
    "created_at": "2012-09-03T12:44:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5457#issuecomment-42368",
    "user": "@jdemeyer"
}
```

Replying to [comment:85 zabrocki]:
> I'm not sure what you want in the commit message
Well, I don't want anything refering to `[mq]` or the patch name.  So if you delete the second line of the commit message in your patch, that will be fine.



---

archive/issue_comments_042369.json:
```json
{
    "body": "same patch with commit message",
    "created_at": "2012-09-03T12:53:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5457#issuecomment-42369",
    "user": "@zabrocki"
}
```

same patch with commit message



---

archive/issue_comments_042370.json:
```json
{
    "body": "Attachment [trac_5457_llt_doc_and_bug_fix-mz.2.patch](tarball://root/attachments/some-uuid/ticket5457/trac_5457_llt_doc_and_bug_fix-mz.2.patch) by @zabrocki created at 2012-09-03 12:55:03\n\nI think that does it.  Sorry I don't know what the [mq] is or how it got there.",
    "created_at": "2012-09-03T12:55:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5457#issuecomment-42370",
    "user": "@zabrocki"
}
```

Attachment [trac_5457_llt_doc_and_bug_fix-mz.2.patch](tarball://root/attachments/some-uuid/ticket5457/trac_5457_llt_doc_and_bug_fix-mz.2.patch) by @zabrocki created at 2012-09-03 12:55:03

I think that does it.  Sorry I don't know what the [mq] is or how it got there.



---

archive/issue_comments_042371.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2012-09-03T13:15:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5457#issuecomment-42371",
    "user": "@jdemeyer"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_042372.json:
```json
{
    "body": "Replying to [comment:87 zabrocki]:\n> Sorry I don't know what the [mq] is or how it got there.\n\nThe [mq] is short for mercurial queue; it is automatically placed there by hg.",
    "created_at": "2012-09-03T13:21:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5457#issuecomment-42372",
    "user": "@saliola"
}
```

Replying to [comment:87 zabrocki]:
> Sorry I don't know what the [mq] is or how it got there.

The [mq] is short for mercurial queue; it is automatically placed there by hg.



---

archive/issue_comments_042373.json:
```json
{
    "body": "Hi Nicolas,\n\n> Technically, the Sage-Combinat queue can't handle patches that are merged and then unmerged. Now, this just means that we will have to everyone using a 5.3 beta to switch to 5.3 final; not a big deal.\n\nI have no idea how to handle the sage-combinat queue now. Do nothing until sage-5.3 comes out and then force everyone to move to sage-5.3?\n\n> Anne, Mike: are there specific deadlines (e.g. the book or meetings) for which waiting for 5.4 could be a bother?\n\nBeginning for the quarter for the book since my students are supposed to use it and sage!\n\nCheers,\n\nAnne",
    "created_at": "2012-09-03T14:14:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5457#issuecomment-42373",
    "user": "@anneschilling"
}
```

Hi Nicolas,

> Technically, the Sage-Combinat queue can't handle patches that are merged and then unmerged. Now, this just means that we will have to everyone using a 5.3 beta to switch to 5.3 final; not a big deal.

I have no idea how to handle the sage-combinat queue now. Do nothing until sage-5.3 comes out and then force everyone to move to sage-5.3?

> Anne, Mike: are there specific deadlines (e.g. the book or meetings) for which waiting for 5.4 could be a bother?

Beginning for the quarter for the book since my students are supposed to use it and sage!

Cheers,

Anne



---

archive/issue_comments_042374.json:
```json
{
    "body": "As far as I know this patch does not commute with #9265 which was just merged into sage. I hope Jeroen will rebase #5457 since I won't have time to do so!!!\n\nAnne",
    "created_at": "2012-09-03T14:30:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5457#issuecomment-42374",
    "user": "@anneschilling"
}
```

As far as I know this patch does not commute with #9265 which was just merged into sage. I hope Jeroen will rebase #5457 since I won't have time to do so!!!

Anne



---

archive/issue_comments_042375.json:
```json
{
    "body": "Apply trac_5457-symmetric_functions-mz.patch, 5457_long_time.patch, trac_5457_llt_doc_and_bug_fix-mz.2.patch",
    "created_at": "2012-09-03T18:46:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5457#issuecomment-42375",
    "user": "@fchapoton"
}
```

Apply trac_5457-symmetric_functions-mz.patch, 5457_long_time.patch, trac_5457_llt_doc_and_bug_fix-mz.2.patch



---

archive/issue_comments_042376.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2012-09-04T08:39:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5457#issuecomment-42376",
    "user": "@jdemeyer"
}
```

Resolution: fixed



---

archive/issue_comments_042377.json:
```json
{
    "body": "Second additional patch",
    "created_at": "2012-09-21T09:21:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5457#issuecomment-42377",
    "user": "@jdemeyer"
}
```

Second additional patch



---

archive/issue_comments_042378.json:
```json
{
    "body": "Attachment [5457_long_time_2.patch](tarball://root/attachments/some-uuid/ticket5457/5457_long_time_2.patch) by @jdemeyer created at 2012-09-21 09:21:57\n\nMy second additional patch [attachment:5457_long_time_2.patch] needs review (just mention the review in the comments, don't change the status).",
    "created_at": "2012-09-21T09:21:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5457#issuecomment-42378",
    "user": "@jdemeyer"
}
```

Attachment [5457_long_time_2.patch](tarball://root/attachments/some-uuid/ticket5457/5457_long_time_2.patch) by @jdemeyer created at 2012-09-21 09:21:57

My second additional patch [attachment:5457_long_time_2.patch] needs review (just mention the review in the comments, don't change the status).



---

archive/issue_comments_042379.json:
```json
{
    "body": "Replying to [comment:95 jdemeyer]:\n> My second additional patch [attachment:5457_long_time_2.patch] needs review (just mention the review in the comments, don't change the status).\n\nPositive review! Thanks!",
    "created_at": "2012-09-21T09:32:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5457#issuecomment-42379",
    "user": "@nthiery"
}
```

Replying to [comment:95 jdemeyer]:
> My second additional patch [attachment:5457_long_time_2.patch] needs review (just mention the review in the comments, don't change the status).

Positive review! Thanks!



---

archive/issue_comments_042380.json:
```json
{
    "body": "This patch abuses `assert` and `AssertionError`. `assert` should not be used for control flow. An `assert` checks something which should always be true, a failed assertion is always a bug in the program.\n\nFor example:\n\n```\n            sage: f.skew_by([1])\n            Traceback (most recent call last):\n            ...\n            AssertionError: x needs to be a symmetric function\n```\n\nThis is a simple user mistake, for which `assert` is not right.\n\nI think this must be fixed.",
    "created_at": "2012-09-24T07:12:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5457#issuecomment-42380",
    "user": "@jdemeyer"
}
```

This patch abuses `assert` and `AssertionError`. `assert` should not be used for control flow. An `assert` checks something which should always be true, a failed assertion is always a bug in the program.

For example:

```
            sage: f.skew_by([1])
            Traceback (most recent call last):
            ...
            AssertionError: x needs to be a symmetric function
```

This is a simple user mistake, for which `assert` is not right.

I think this must be fixed.



---

archive/issue_comments_042381.json:
```json
{
    "body": "Hi Jeroen,\n\nReplying to [comment:97 jdemeyer]:\n> This patch abuses `assert` and `AssertionError`. `assert` should not be used for control flow. An `assert` checks something which should always be true, a failed assertion is always a bug in the program.\n> \n> For example:\n> {{{\n>             sage: f.skew_by([1])\n>             Traceback (most recent call last):\n>             ...\n>             AssertionError: x needs to be a symmetric function\n> }}}\n> This is a simple user mistake, for which `assert` is not right.\n> \n> I think this must be fixed\n\nGiven the discussion on sage-devel, do we agree that there is no control flow involved and it's a not so common function, so it's ok to use assert?\n\nCheers,\n                    Nicolas",
    "created_at": "2012-09-24T09:16:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5457#issuecomment-42381",
    "user": "@nthiery"
}
```

Hi Jeroen,

Replying to [comment:97 jdemeyer]:
> This patch abuses `assert` and `AssertionError`. `assert` should not be used for control flow. An `assert` checks something which should always be true, a failed assertion is always a bug in the program.
> 
> For example:
> {{{
>             sage: f.skew_by([1])
>             Traceback (most recent call last):
>             ...
>             AssertionError: x needs to be a symmetric function
> }}}
> This is a simple user mistake, for which `assert` is not right.
> 
> I think this must be fixed

Given the discussion on sage-devel, do we agree that there is no control flow involved and it's a not so common function, so it's ok to use assert?

Cheers,
                    Nicolas



---

archive/issue_comments_042382.json:
```json
{
    "body": "Replying to [comment:97 jdemeyer]:\n> This patch abuses `assert` and `AssertionError`. `assert` should not be used for control flow. An `assert` checks something which should always be true, a failed assertion is always a bug in the program.\n> \n> For example:\n> {{{\n>             sage: f.skew_by([1])\n>             Traceback (most recent call last):\n>             ...\n>             AssertionError: x needs to be a symmetric function\n> }}}\n> This is a simple user mistake, for which `assert` is not right.\n> \n> I think this must be fixed.\n\nWe had a user who used this method wrongly at FPSAC (he used a partition instead of a symmetric function). That's why we added this (since this can potentially be a common user mistake). If this should be done differently, feel free to change it!\n\nAnne",
    "created_at": "2012-09-24T14:30:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5457#issuecomment-42382",
    "user": "@anneschilling"
}
```

Replying to [comment:97 jdemeyer]:
> This patch abuses `assert` and `AssertionError`. `assert` should not be used for control flow. An `assert` checks something which should always be true, a failed assertion is always a bug in the program.
> 
> For example:
> {{{
>             sage: f.skew_by([1])
>             Traceback (most recent call last):
>             ...
>             AssertionError: x needs to be a symmetric function
> }}}
> This is a simple user mistake, for which `assert` is not right.
> 
> I think this must be fixed.

We had a user who used this method wrongly at FPSAC (he used a partition instead of a symmetric function). That's why we added this (since this can potentially be a common user mistake). If this should be done differently, feel free to change it!

Anne



---

archive/issue_comments_042383.json:
```json
{
    "body": "Replying to [comment:99 aschilling]:\n> That's why we added this (since this can potentially be a common user mistake). If this should be done differently, feel free to change it!\nYes, it should be done differently.  The correct way would be:\n\n```\nif not needed_condition:\n    raise ValueError(\"Error message\")\n```\n\n\nAs I said: `assert` is only meant to catch *bugs*, not user errors.  Although, as Nicolas Thi\u00e9ry argued, something `assert` is acceptible.  See also the sage-devel thread.",
    "created_at": "2012-09-24T18:35:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5457#issuecomment-42383",
    "user": "@jdemeyer"
}
```

Replying to [comment:99 aschilling]:
> That's why we added this (since this can potentially be a common user mistake). If this should be done differently, feel free to change it!
Yes, it should be done differently.  The correct way would be:

```
if not needed_condition:
    raise ValueError("Error message")
```


As I said: `assert` is only meant to catch *bugs*, not user errors.  Although, as Nicolas Thiéry argued, something `assert` is acceptible.  See also the sage-devel thread.



---

archive/issue_comments_042384.json:
```json
{
    "body": "Attachment [trac_5457-symmetric_functions-mz.2.patch](tarball://root/attachments/some-uuid/ticket5457/trac_5457-symmetric_functions-mz.2.patch) by @anneschilling created at 2012-09-25 00:44:24",
    "created_at": "2012-09-25T00:44:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5457#issuecomment-42384",
    "user": "@anneschilling"
}
```

Attachment [trac_5457-symmetric_functions-mz.2.patch](tarball://root/attachments/some-uuid/ticket5457/trac_5457-symmetric_functions-mz.2.patch) by @anneschilling created at 2012-09-25 00:44:24



---

archive/issue_comments_042385.json:
```json
{
    "body": "I folded the patches and made the required change.\n\nApply: trac_5457-symmetric_functions-mz.2.patch\n\nAnne",
    "created_at": "2012-09-25T00:45:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5457#issuecomment-42385",
    "user": "@anneschilling"
}
```

I folded the patches and made the required change.

Apply: trac_5457-symmetric_functions-mz.2.patch

Anne



---

archive/issue_comments_042386.json:
```json
{
    "body": "Hi Jeroen,\n\nI am confused: was your intention to request that this change be made for this ticket?\n\n(meaning that you'd have to unmerge / remerge it)",
    "created_at": "2012-09-26T14:24:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5457#issuecomment-42386",
    "user": "@nthiery"
}
```

Hi Jeroen,

I am confused: was your intention to request that this change be made for this ticket?

(meaning that you'd have to unmerge / remerge it)



---

archive/issue_comments_042387.json:
```json
{
    "body": "Short story: for me it was far more important **that** the problem got\nfixed, not **how** it got fixed.\n\nA situation where a ticket is merged but then problems are discovered is\na difficult situation to handle.  In the past, I would have re-opened\nthe ticket and set it to needs_work but that seems to upset people (they\nthink it will postpone the merging of their patch).  So this time, I\ndecided not to reopen the ticket but my intention was indeed for the\nchances to be made on the same ticket.  However, ideally it would have\nbeen done in a separate additional patch, leaving the original\nalready-merged patch alone.  But I certainly would have been happy also\nwith a new ticket.\n\nI have no idea how any of this affect sage-combinat.\n\n\nJeroen.",
    "created_at": "2012-09-26T14:45:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5457#issuecomment-42387",
    "user": "@jdemeyer"
}
```

Short story: for me it was far more important **that** the problem got
fixed, not **how** it got fixed.

A situation where a ticket is merged but then problems are discovered is
a difficult situation to handle.  In the past, I would have re-opened
the ticket and set it to needs_work but that seems to upset people (they
think it will postpone the merging of their patch).  So this time, I
decided not to reopen the ticket but my intention was indeed for the
chances to be made on the same ticket.  However, ideally it would have
been done in a separate additional patch, leaving the original
already-merged patch alone.  But I certainly would have been happy also
with a new ticket.

I have no idea how any of this affect sage-combinat.


Jeroen.
