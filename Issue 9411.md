# Issue 9411: Given points on an elliptic curve, this finds a LLL reduced ZZ-independent set

archive/issues_009411.json:
```json
{
    "body": "Assignee: @JohnCremona\n\nCC:  jeremywest @JohnCremona\n\nKeywords: LLL, rank\n\nThis is based on magma code from Cremona.  It takes a set of points on an elliptic curve and uses LLL to return a ZZ-independent set with the same ZZ-span.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9411\n\n",
    "created_at": "2010-07-02T20:18:16Z",
    "labels": [
        "elliptic curves",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-5.13",
    "title": "Given points on an elliptic curve, this finds a LLL reduced ZZ-independent set",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9411",
    "user": "@adeines"
}
```
Assignee: @JohnCremona

CC:  jeremywest @JohnCremona

Keywords: LLL, rank

This is based on magma code from Cremona.  It takes a set of points on an elliptic curve and uses LLL to return a ZZ-independent set with the same ZZ-span.

Issue created by migration from https://trac.sagemath.org/ticket/9411





---

archive/issue_comments_089693.json:
```json
{
    "body": "Attachment [trac_9411-LLL_points.patch](tarball://root/attachments/some-uuid/ticket9411/trac_9411-LLL_points.patch) by @adeines created at 2010-07-02 21:12:43",
    "created_at": "2010-07-02T21:12:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9411",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9411#issuecomment-89693",
    "user": "@adeines"
}
```

Attachment [trac_9411-LLL_points.patch](tarball://root/attachments/some-uuid/ticket9411/trac_9411-LLL_points.patch) by @adeines created at 2010-07-02 21:12:43



---

archive/issue_comments_089694.json:
```json
{
    "body": "Aly, would it not have been simpler to move the code of the function lll_reduce(self, points, height_matrix=None) from ell_rational_field to ell_number_field?  That function was written when we only had heights over Q but it does the same thing, essentially.\n\nApologies if I should have told you about that function earlier...\n\nThere may well be other functions which can similarly be moved up;  someone should go systematically through ell_rational_field functions to see which others there are.\n\nOn your patch, I see the following:  (1) no tests over fields other than Q; (2) in defining E why not just E=self?;  (3) better to use the pari library than the gp interface (when there's a choice).  Otherwise it applies and builds fine.",
    "created_at": "2010-07-05T16:39:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9411",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9411#issuecomment-89694",
    "user": "@JohnCremona"
}
```

Aly, would it not have been simpler to move the code of the function lll_reduce(self, points, height_matrix=None) from ell_rational_field to ell_number_field?  That function was written when we only had heights over Q but it does the same thing, essentially.

Apologies if I should have told you about that function earlier...

There may well be other functions which can similarly be moved up;  someone should go systematically through ell_rational_field functions to see which others there are.

On your patch, I see the following:  (1) no tests over fields other than Q; (2) in defining E why not just E=self?;  (3) better to use the pari library than the gp interface (when there's a choice).  Otherwise it applies and builds fine.



---

archive/issue_comments_089695.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2010-07-05T16:39:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9411",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9411#issuecomment-89695",
    "user": "@JohnCremona"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_089696.json:
```json
{
    "body": "Knowing about the lll_reduce function and finally getting back to this ticket, I've just created a patch which simply moves the function lll_reduce to ell_number_field.  I've also included doctests over quadratic number fields.  \n\nOne note, this code isn't very robust.  For example, in many cases the height pairing matrix is *not* positive definite.  In this case \n\"the output depends on the undocumented behaviour of PARI's ``lllgram()``  function\", which means there is a divide by zero error.  Here's an example:\n\n\n```\n            sage: Qrt5.<rt5>=NumberField(x^2-5)\n            sage: E = EllipticCurve([0,5-rt5,0,rt5,0])\n            sage: QuadraticForm(E.height_pairing_matrix(E.gens())).is_positive_definite()\n            False\n            sage: E.lll_reduce(E.gens())\n            Exception raised:\n            Traceback (most recent call last):\n            File \"/Users/aly/Desktop/sage-4.6.1.rc1/local/bin/ncadoctest.py\", line 1231, in run_one_test\n            self.run_one_example(test, example, filename, compileflags)\n            File \"/Users/aly/Desktop/sage-4.6.1.rc1/local/bin/sagedoctest.py\", line 38, in run_one_example\n            OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n            File \"/Users/aly/Desktop/sage-4.6.1.rc1/local/bin/ncadoctest.py\", line 1172, in run_one_example\n            compileflags, 1) in test.globs\n            File \"<doctest __main__.example_39[8]>\", line 1, in <module>\n            E.lll_reduce(E.gens())###line 2106:\n            sage: E.lll_reduce(E.gens())\n            File \"/Users/aly/Desktop/sage-4.6.1.rc1/local/lib/python/site-packages/sage/schemes/elliptic_curves/ell_number_field.py\", line 2117, in lll_reduce\n            U = pari(height_matrix).lllgram().python()\n            File \"gen.pyx\", line 7749, in sage.libs.pari.gen.gen.lllgram (sage/libs/pari/gen.c:34364)\n            File \"gen.pyx\", line 9851, in sage.libs.pari.gen._pari_trap (sage/libs/pari/gen.c:46022)\n            PariError: division by zero (27)\n```\n",
    "created_at": "2011-01-12T06:09:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9411",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9411#issuecomment-89696",
    "user": "@adeines"
}
```

Knowing about the lll_reduce function and finally getting back to this ticket, I've just created a patch which simply moves the function lll_reduce to ell_number_field.  I've also included doctests over quadratic number fields.  

One note, this code isn't very robust.  For example, in many cases the height pairing matrix is *not* positive definite.  In this case 
"the output depends on the undocumented behaviour of PARI's ``lllgram()``  function", which means there is a divide by zero error.  Here's an example:


```
            sage: Qrt5.<rt5>=NumberField(x^2-5)
            sage: E = EllipticCurve([0,5-rt5,0,rt5,0])
            sage: QuadraticForm(E.height_pairing_matrix(E.gens())).is_positive_definite()
            False
            sage: E.lll_reduce(E.gens())
            Exception raised:
            Traceback (most recent call last):
            File "/Users/aly/Desktop/sage-4.6.1.rc1/local/bin/ncadoctest.py", line 1231, in run_one_test
            self.run_one_example(test, example, filename, compileflags)
            File "/Users/aly/Desktop/sage-4.6.1.rc1/local/bin/sagedoctest.py", line 38, in run_one_example
            OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
            File "/Users/aly/Desktop/sage-4.6.1.rc1/local/bin/ncadoctest.py", line 1172, in run_one_example
            compileflags, 1) in test.globs
            File "<doctest __main__.example_39[8]>", line 1, in <module>
            E.lll_reduce(E.gens())###line 2106:
            sage: E.lll_reduce(E.gens())
            File "/Users/aly/Desktop/sage-4.6.1.rc1/local/lib/python/site-packages/sage/schemes/elliptic_curves/ell_number_field.py", line 2117, in lll_reduce
            U = pari(height_matrix).lllgram().python()
            File "gen.pyx", line 7749, in sage.libs.pari.gen.gen.lllgram (sage/libs/pari/gen.c:34364)
            File "gen.pyx", line 9851, in sage.libs.pari.gen._pari_trap (sage/libs/pari/gen.c:46022)
            PariError: division by zero (27)
```




---

archive/issue_comments_089697.json:
```json
{
    "body": "Attachment [trac_9411_lll_reduce_number_field.patch](tarball://root/attachments/some-uuid/ticket9411/trac_9411_lll_reduce_number_field.patch) by @adeines created at 2011-01-12 06:10:00\n\nThis replaces the previous patch.  It applies to sage-4.6.1.rc1",
    "created_at": "2011-01-12T06:10:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9411",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9411#issuecomment-89697",
    "user": "@adeines"
}
```

Attachment [trac_9411_lll_reduce_number_field.patch](tarball://root/attachments/some-uuid/ticket9411/trac_9411_lll_reduce_number_field.patch) by @adeines created at 2011-01-12 06:10:00

This replaces the previous patch.  It applies to sage-4.6.1.rc1



---

archive/issue_comments_089698.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-01-12T09:36:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9411",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9411#issuecomment-89698",
    "user": "@JohnCremona"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_089699.json:
```json
{
    "body": "Thanks for putting more work into this.  I have not time to re-review right now, but I do intend to.\n\nAbout the robustness,  a better long term solution would be to separate out two different aspects:  (1) give some points, return a maximal independent subset (or, return an independent set which has the same ZZ-span, which is not the same thing);  (2) given independent points, LLL-reduce them.  \n\nBut for this ticket I suggest that we just do the best we can using the pari function and sufficient precision.",
    "created_at": "2011-01-12T09:36:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9411",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9411#issuecomment-89699",
    "user": "@JohnCremona"
}
```

Thanks for putting more work into this.  I have not time to re-review right now, but I do intend to.

About the robustness,  a better long term solution would be to separate out two different aspects:  (1) give some points, return a maximal independent subset (or, return an independent set which has the same ZZ-span, which is not the same thing);  (2) given independent points, LLL-reduce them.  

But for this ticket I suggest that we just do the best we can using the pari function and sufficient precision.



---

archive/issue_comments_089700.json:
```json
{
    "body": "I'm working on this now.  First, I deleted the duplicate function still in ell_rational_field.py (but moved the examples there to ell_number_field.py).  I also added a precision parameter to be passed to the height pairing matrix call, and am trying to make an example where it makes a difference!",
    "created_at": "2011-04-22T17:24:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9411",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9411#issuecomment-89700",
    "user": "@JohnCremona"
}
```

I'm working on this now.  First, I deleted the duplicate function still in ell_rational_field.py (but moved the examples there to ell_number_field.py).  I also added a precision parameter to be passed to the height pairing matrix call, and am trying to make an example where it makes a difference!



---

archive/issue_comments_089701.json:
```json
{
    "body": "I uploaded my patch which is a revision of Aly's, since I did not want it to get lost.  It's fine for testing but I have not yet included an example where the precision parameter makes a difference.",
    "created_at": "2011-05-03T16:34:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9411",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9411#issuecomment-89701",
    "user": "@JohnCremona"
}
```

I uploaded my patch which is a revision of Aly's, since I did not want it to get lost.  It's fine for testing but I have not yet included an example where the precision parameter makes a difference.



---

archive/issue_comments_089702.json:
```json
{
    "body": "What's the status of this ticket? It's marked as \"needs review\", but the last comment suggests that more work is needed.",
    "created_at": "2011-12-30T17:47:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9411",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9411#issuecomment-89702",
    "user": "@loefflerd"
}
```

What's the status of this ticket? It's marked as "needs review", but the last comment suggests that more work is needed.



---

archive/issue_comments_089703.json:
```json
{
    "body": "Well, I think it is ready for review.  I certainly think that in principle the function ought to allow the user to set the precision which is used to compute the height-pairing matrix (which was not the case before).  Secondly, we now have one function in ell_number_field instead of just one function on ell_rational_field, or two functions.  So Sage is certainly enhanced by this!\n\nOf course, the reviewer might insist on seeing an example where higher precision makes a difference....but I don't and I am listed as a reviewer though the latest patch was by me so we need a third party to have a look.",
    "created_at": "2011-12-30T18:40:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9411",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9411#issuecomment-89703",
    "user": "@JohnCremona"
}
```

Well, I think it is ready for review.  I certainly think that in principle the function ought to allow the user to set the precision which is used to compute the height-pairing matrix (which was not the case before).  Secondly, we now have one function in ell_number_field instead of just one function on ell_rational_field, or two functions.  So Sage is certainly enhanced by this!

Of course, the reviewer might insist on seeing an example where higher precision makes a difference....but I don't and I am listed as a reviewer though the latest patch was by me so we need a third party to have a look.



---

archive/issue_comments_089704.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2012-01-11T15:21:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9411",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9411#issuecomment-89704",
    "user": "@zimmermann6"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_089705.json:
```json
{
    "body": "Changing keywords from \"LLL, rank\" to \"LLL, rank, sd35.5\".",
    "created_at": "2012-01-11T15:21:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9411",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9411#issuecomment-89705",
    "user": "@zimmermann6"
}
```

Changing keywords from "LLL, rank" to "LLL, rank, sd35.5".



---

archive/issue_comments_089706.json:
```json
{
    "body": "all doctests pass on top of sage-4.8.alpha6.\n\nHowever I suggest adding an example checking the relation between the input points, `newpoints`\nand the output matrix `U`:\n\n```\nsage: E = EllipticCurve([0, 1, 1, -2, 42])\nsage: Pi = E.gens()\nsage: Qi, U = E.lll_reduce(Pi)\nsage: all(sum(U[i,j]*Pi[i] for i in range(4)) == Qi[j] for j in range(4))\nTrue\n```\n\n\nAnd please add an example where an `height_matrix` is given, for example\n(this also gives an example where the precision matters):\n\n```\nsage: E = EllipticCurve([0, 1, 1, -2, 42])\nsage: Pi = E.gens()\nsage: H=E.height_pairing_matrix(Pi,3)\nsage: E.lll_reduce(Pi,height_matrix=H)\n([(-4 : 1 : 1), (-3 : 5 : 1), (-2 : 6 : 1), (1 : -7 : 1)], [1 0 0 1]\n[0 1 0 1]\n[0 0 0 1]\n[0 0 1 1])\n```\n\n\nAlso, I guess \"number of bits of precision of result\" should read \"number of bits of precision of intermediate computations\" (in fact the precision of the height matrix computation, which is\ngiven as input to Pari).\n\nPaul\n\nPS: the doctest coverage could be 100% if we could remove the deprecate function\n`local_information`. Can this be done?",
    "created_at": "2012-01-11T15:21:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9411",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9411#issuecomment-89706",
    "user": "@zimmermann6"
}
```

all doctests pass on top of sage-4.8.alpha6.

However I suggest adding an example checking the relation between the input points, `newpoints`
and the output matrix `U`:

```
sage: E = EllipticCurve([0, 1, 1, -2, 42])
sage: Pi = E.gens()
sage: Qi, U = E.lll_reduce(Pi)
sage: all(sum(U[i,j]*Pi[i] for i in range(4)) == Qi[j] for j in range(4))
True
```


And please add an example where an `height_matrix` is given, for example
(this also gives an example where the precision matters):

```
sage: E = EllipticCurve([0, 1, 1, -2, 42])
sage: Pi = E.gens()
sage: H=E.height_pairing_matrix(Pi,3)
sage: E.lll_reduce(Pi,height_matrix=H)
([(-4 : 1 : 1), (-3 : 5 : 1), (-2 : 6 : 1), (1 : -7 : 1)], [1 0 0 1]
[0 1 0 1]
[0 0 0 1]
[0 0 1 1])
```


Also, I guess "number of bits of precision of result" should read "number of bits of precision of intermediate computations" (in fact the precision of the height matrix computation, which is
given as input to Pari).

Paul

PS: the doctest coverage could be 100% if we could remove the deprecate function
`local_information`. Can this be done?



---

archive/issue_comments_089707.json:
```json
{
    "body": "apply only trac_9411_lll_reduce_number_field.2.patch",
    "created_at": "2013-08-20T13:55:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9411",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9411#issuecomment-89707",
    "user": "@fchapoton"
}
```

apply only trac_9411_lll_reduce_number_field.2.patch



---

archive/issue_comments_089708.json:
```json
{
    "body": "this needs to be rebased",
    "created_at": "2013-08-20T13:59:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9411",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9411#issuecomment-89708",
    "user": "@fchapoton"
}
```

this needs to be rebased



---

archive/issue_comments_089709.json:
```json
{
    "body": "I volunteer to do that since I wrote the current patch.  I think we can now remove that deprecated function too (if it is still there).",
    "created_at": "2013-08-20T14:06:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9411",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9411#issuecomment-89709",
    "user": "@JohnCremona"
}
```

I volunteer to do that since I wrote the current patch.  I think we can now remove that deprecated function too (if it is still there).



---

archive/issue_comments_089710.json:
```json
{
    "body": "I did the rebasing but am now also adding the tests suggested by Paul Zimmermann's comment 9.",
    "created_at": "2013-08-21T14:47:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9411",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9411#issuecomment-89710",
    "user": "@JohnCremona"
}
```

I did the rebasing but am now also adding the tests suggested by Paul Zimmermann's comment 9.



---

archive/issue_comments_089711.json:
```json
{
    "body": "Attachment [trac_9411_lll_reduce_number_field.2.patch](tarball://root/attachments/some-uuid/ticket9411/trac_9411_lll_reduce_number_field.2.patch) by @JohnCremona created at 2013-08-21 14:59:55\n\nrebased on 5.12.beta1 and added 2 new doctests",
    "created_at": "2013-08-21T14:59:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9411",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9411#issuecomment-89711",
    "user": "@JohnCremona"
}
```

Attachment [trac_9411_lll_reduce_number_field.2.patch](tarball://root/attachments/some-uuid/ticket9411/trac_9411_lll_reduce_number_field.2.patch) by @JohnCremona created at 2013-08-21 14:59:55

rebased on 5.12.beta1 and added 2 new doctests



---

archive/issue_comments_089712.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2013-08-21T15:00:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9411",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9411#issuecomment-89712",
    "user": "@JohnCremona"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_089713.json:
```json
{
    "body": "Replying to [comment:13 cremona]:\n> I did the rebasing but am now also adding the tests suggested by Paul Zimmermann's comment 9.\nDone, so back to \"needs review\".",
    "created_at": "2013-08-21T15:00:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9411",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9411#issuecomment-89713",
    "user": "@JohnCremona"
}
```

Replying to [comment:13 cremona]:
> I did the rebasing but am now also adding the tests suggested by Paul Zimmermann's comment 9.
Done, so back to "needs review".



---

archive/issue_comments_089714.json:
```json
{
    "body": "apply only trac_9411_lll_reduce_number_field.2.patch",
    "created_at": "2013-08-29T07:52:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9411",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9411#issuecomment-89714",
    "user": "@fchapoton"
}
```

apply only trac_9411_lll_reduce_number_field.2.patch



---

archive/issue_comments_089715.json:
```json
{
    "body": "looks good to me.\n\nI have made a review patch, mainly about details of the doc, but also removing the deprecated function `local_information`.\n\nIf the minor changes in my review patch are ok, this can be set to positive review\n\nfor the bot:\n\napply trac_9411_lll_reduce_number_field.2.patch, trac_9411_review.patch",
    "created_at": "2013-09-11T20:09:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9411",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9411#issuecomment-89715",
    "user": "@fchapoton"
}
```

looks good to me.

I have made a review patch, mainly about details of the doc, but also removing the deprecated function `local_information`.

If the minor changes in my review patch are ok, this can be set to positive review

for the bot:

apply trac_9411_lll_reduce_number_field.2.patch, trac_9411_review.patch



---

archive/issue_comments_089716.json:
```json
{
    "body": "Attachment [trac_9411_review.patch](tarball://root/attachments/some-uuid/ticket9411/trac_9411_review.patch) by @fchapoton created at 2013-11-25 19:07:06\n\nrebased. Once again, if my minor changes are ok, you can set this to positive review",
    "created_at": "2013-11-25T19:07:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9411",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9411#issuecomment-89716",
    "user": "@fchapoton"
}
```

Attachment [trac_9411_review.patch](tarball://root/attachments/some-uuid/ticket9411/trac_9411_review.patch) by @fchapoton created at 2013-11-25 19:07:06

rebased. Once again, if my minor changes are ok, you can set this to positive review



---

archive/issue_comments_089717.json:
```json
{
    "body": "OK, I am happy to give chapoton's reviewer's patch +1 and set this to positive review.  Since there have been other elliptic curve patches already merged into 5.14.beta4 I hope the rebasing is sufficient!",
    "created_at": "2013-11-25T19:29:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9411",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9411#issuecomment-89717",
    "user": "@JohnCremona"
}
```

OK, I am happy to give chapoton's reviewer's patch +1 and set this to positive review.  Since there have been other elliptic curve patches already merged into 5.14.beta4 I hope the rebasing is sufficient!



---

archive/issue_comments_089718.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-11-25T19:29:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9411",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9411#issuecomment-89718",
    "user": "@JohnCremona"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_089719.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2013-12-05T08:02:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9411",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9411#issuecomment-89719",
    "user": "@jdemeyer"
}
```

Resolution: fixed
