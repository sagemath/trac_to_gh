# Issue 6371: Implement Riemann theta functions

archive/issues_006371.json:
```json
{
    "body": "Assignee: @cswiercz\n\nCC:  @cswiercz fredrik.johannson @mstreng jpflori @slel\n\nKeywords: riemann theta klein\n\nIn the theory of differential equations and Abelian varieties, Riemann theta functions and their relatives play an important role.  Implement these in Sage!\n\nSee also:\n\n- [RiemannTheta](https://github.com/nbruin/RiemannTheta) --\n  A Sagemath package for evaluating Riemann theta functions\n  with characteristics numerically to arbitrary precision,\n  as well as their derivatives\n\nIssue created by migration from https://trac.sagemath.org/ticket/6371\n\n",
    "created_at": "2009-06-20T18:15:55Z",
    "labels": [
        "component: numerical",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-7.1",
    "title": "Implement Riemann theta functions",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6371",
    "user": "https://github.com/ncalexan"
}
```
Assignee: @cswiercz

CC:  @cswiercz fredrik.johannson @mstreng jpflori @slel

Keywords: riemann theta klein

In the theory of differential equations and Abelian varieties, Riemann theta functions and their relatives play an important role.  Implement these in Sage!

See also:

- [RiemannTheta](https://github.com/nbruin/RiemannTheta) --
  A Sagemath package for evaluating Riemann theta functions
  with characteristics numerically to arbitrary precision,
  as well as their derivatives

Issue created by migration from https://trac.sagemath.org/ticket/6371





---

archive/issue_comments_050853.json:
```json
{
    "body": "Attachment [trac_6371-riemann-theta.patch](tarball://root/attachments/some-uuid/ticket6371/trac_6371-riemann-theta.patch) by @ncalexan created at 2009-06-20 18:39:57",
    "created_at": "2009-06-20T18:39:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6371",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6371#issuecomment-50853",
    "user": "https://github.com/ncalexan"
}
```

Attachment [trac_6371-riemann-theta.patch](tarball://root/attachments/some-uuid/ticket6371/trac_6371-riemann-theta.patch) by @ncalexan created at 2009-06-20 18:39:57



---

archive/issue_comments_050854.json:
```json
{
    "body": "I want to make sure this code doesn't get lost.  It's very much [needs work] -- I don't think all tests are tagged `optional` and `long` correctly.  I'm not certain that the output is correct to very high accuracy, either -- magma and mathematica disagree, and maple is too slow to evaluate to high precision.\n\nFredrik, somewhere in here there are lots of calls to the incomplete gamma function.  I used low precision as much as possible as you will see, because I don't really need high precision, I just need large outputs.\n\nChris, this applies against 4.0.2.alpha1 at least.  Documentation and testing appreciated!",
    "created_at": "2009-06-20T18:43:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6371",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6371#issuecomment-50854",
    "user": "https://github.com/ncalexan"
}
```

I want to make sure this code doesn't get lost.  It's very much [needs work] -- I don't think all tests are tagged `optional` and `long` correctly.  I'm not certain that the output is correct to very high accuracy, either -- magma and mathematica disagree, and maple is too slow to evaluate to high precision.

Fredrik, somewhere in here there are lots of calls to the incomplete gamma function.  I used low precision as much as possible as you will see, because I don't really need high precision, I just need large outputs.

Chris, this applies against 4.0.2.alpha1 at least.  Documentation and testing appreciated!



---

archive/issue_comments_050855.json:
```json
{
    "body": "Marco, you might be interested in this work in progress code too.",
    "created_at": "2009-06-20T18:59:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6371",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6371#issuecomment-50855",
    "user": "https://github.com/ncalexan"
}
```

Marco, you might be interested in this work in progress code too.



---

archive/issue_comments_050856.json:
```json
{
    "body": "Is double precision sufficient? Are the arguments large, integers or half-integers? In either case, very fast evaluation of the incomplete gamma function should be possible.",
    "created_at": "2009-06-21T18:40:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6371",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6371#issuecomment-50856",
    "user": "https://github.com/fredrik-johansson"
}
```

Is double precision sufficient? Are the arguments large, integers or half-integers? In either case, very fast evaluation of the incomplete gamma function should be possible.



---

archive/issue_comments_050857.json:
```json
{
    "body": "To use this, type\n\n```\nsage: hg_sage.apply('http://trac.sagemath.org/sage_trac/attachment/ticket/6371/trac_6371-riemann-theta.patch')\nsage: quit\n\nsage -br\n\nsage: now you have the new code\n```",
    "created_at": "2009-06-26T13:23:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6371",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6371#issuecomment-50857",
    "user": "https://github.com/williamstein"
}
```

To use this, type

```
sage: hg_sage.apply('http://trac.sagemath.org/sage_trac/attachment/ticket/6371/trac_6371-riemann-theta.patch')
sage: quit

sage -br

sage: now you have the new code
```



---

archive/issue_comments_050858.json:
```json
{
    "body": "Changing assignee from jkantor to @cswiercz.",
    "created_at": "2010-12-10T18:02:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6371",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6371#issuecomment-50858",
    "user": "https://github.com/cswiercz"
}
```

Changing assignee from jkantor to @cswiercz.



---

archive/issue_comments_050859.json:
```json
{
    "body": "Over the past month or two I've done considerable work vetting out the bugs and errors in the above code. Within a week or so I hope to post a replacement patch. Hence, the change of owner. I'll keep everyone who's interested posted on my progress.\n\nA word of warning, though: since I know a lot of people who are interested in my getting Riemann theta into Sage as soon as possible I had to strip Shimura phi, Siegel theta, and Klein P. I'm not qualified to review / bug fix that part of the code. I hope this is okay with the original authors and people who are interested in seeing this patch resolved. Perhaps we can move these implementations into a new patch once Riemann theta is implemented.\n\nAgain, I'll be posting a replacement patch sometime within the next two weeks or so.",
    "created_at": "2010-12-10T18:07:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6371",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6371#issuecomment-50859",
    "user": "https://github.com/cswiercz"
}
```

Over the past month or two I've done considerable work vetting out the bugs and errors in the above code. Within a week or so I hope to post a replacement patch. Hence, the change of owner. I'll keep everyone who's interested posted on my progress.

A word of warning, though: since I know a lot of people who are interested in my getting Riemann theta into Sage as soon as possible I had to strip Shimura phi, Siegel theta, and Klein P. I'm not qualified to review / bug fix that part of the code. I hope this is okay with the original authors and people who are interested in seeing this patch resolved. Perhaps we can move these implementations into a new patch once Riemann theta is implemented.

Again, I'll be posting a replacement patch sometime within the next two weeks or so.



---

archive/issue_comments_050860.json:
```json
{
    "body": "> A word of warning, though: since I know a lot of people who are interested in my getting Riemann theta into Sage as soon as possible I had to strip Shimura phi, Siegel theta, and Klein P. I'm not qualified to review / bug fix that part of the code. I hope this is okay with the original authors and people who are interested in seeing this patch resolved.\n\n\nI am the original author, and I think this is a very reasonable decision!  You should know that I use \"Siegel theta\" and \"Riemann theta\" interchangeably.  Riemann theta often seems to mean just with characteristics (0, 0, ..., 0) and Siegel theta seems to be a Mathematica-ism.  Whatever we decide on is (probably) fine by me.\n\n> Perhaps we can move these implementations into a new patch once Riemann theta is implemented.\n\n\nThese bits are interesting for my research, but probably are not all that interesting more generally.  Cut them for now.\n\nThanks for you efforts, Chris!",
    "created_at": "2010-12-10T18:18:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6371",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6371#issuecomment-50860",
    "user": "https://github.com/ncalexan"
}
```

> A word of warning, though: since I know a lot of people who are interested in my getting Riemann theta into Sage as soon as possible I had to strip Shimura phi, Siegel theta, and Klein P. I'm not qualified to review / bug fix that part of the code. I hope this is okay with the original authors and people who are interested in seeing this patch resolved.


I am the original author, and I think this is a very reasonable decision!  You should know that I use "Siegel theta" and "Riemann theta" interchangeably.  Riemann theta often seems to mean just with characteristics (0, 0, ..., 0) and Siegel theta seems to be a Mathematica-ism.  Whatever we decide on is (probably) fine by me.

> Perhaps we can move these implementations into a new patch once Riemann theta is implemented.


These bits are interesting for my research, but probably are not all that interesting more generally.  Cut them for now.

Thanks for you efforts, Chris!



---

archive/issue_comments_050861.json:
```json
{
    "body": "> I am the original author, and I think this is a very reasonable decision!  You should know that I use \"Siegel theta\" and \"Riemann theta\" interchangeably.  Riemann theta often seems to mean just with characteristics (0, 0, ..., 0) and Siegel theta seems to be a Mathematica-ism.  Whatever we decide on is (probably) fine by me.\n> Thanks for you efforts, Chris!\n\n\nHuzzah! Thank _you_ for your help!",
    "created_at": "2010-12-10T18:31:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6371",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6371#issuecomment-50861",
    "user": "https://github.com/cswiercz"
}
```

> I am the original author, and I think this is a very reasonable decision!  You should know that I use "Siegel theta" and "Riemann theta" interchangeably.  Riemann theta often seems to mean just with characteristics (0, 0, ..., 0) and Siegel theta seems to be a Mathematica-ism.  Whatever we decide on is (probably) fine by me.
> Thanks for you efforts, Chris!


Huzzah! Thank _you_ for your help!



---

archive/issue_comments_050862.json:
```json
{
    "body": "Attachment [trac_6371-riemann-theta-REPLACEMENT.patch](tarball://root/attachments/some-uuid/ticket6371/trac_6371-riemann-theta-REPLACEMENT.patch) by @cswiercz created at 2011-03-25 00:08:59\n\nReplacement for first patch by ncalexan",
    "created_at": "2011-03-25T00:08:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6371",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6371#issuecomment-50862",
    "user": "https://github.com/cswiercz"
}
```

Attachment [trac_6371-riemann-theta-REPLACEMENT.patch](tarball://root/attachments/some-uuid/ticket6371/trac_6371-riemann-theta-REPLACEMENT.patch) by @cswiercz created at 2011-03-25 00:08:59

Replacement for first patch by ncalexan



---

archive/issue_comments_050863.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-03-25T00:10:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6371",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6371#issuecomment-50863",
    "user": "https://github.com/cswiercz"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_050864.json:
```json
{
    "body": "Note that the second patch is meant to replace the first. Many many changes were made!",
    "created_at": "2011-03-25T00:10:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6371",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6371#issuecomment-50864",
    "user": "https://github.com/cswiercz"
}
```

Note that the second patch is meant to replace the first. Many many changes were made!



---

archive/issue_comments_050865.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-03-28T18:01:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6371",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6371#issuecomment-50865",
    "user": "https://github.com/cswiercz"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_050866.json:
```json
{
    "body": "Some clarifications and fine tuning needs to be made to the documentation.",
    "created_at": "2011-03-28T18:01:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6371",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6371#issuecomment-50866",
    "user": "https://github.com/cswiercz"
}
```

Some clarifications and fine tuning needs to be made to the documentation.



---

archive/issue_comments_050867.json:
```json
{
    "body": "Part 2 of the replacement patch. Includes documentation fixes.",
    "created_at": "2011-03-28T18:21:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6371",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6371#issuecomment-50867",
    "user": "https://github.com/cswiercz"
}
```

Part 2 of the replacement patch. Includes documentation fixes.



---

archive/issue_comments_050868.json:
```json
{
    "body": "Attachment [trac_6371-riemann-theta-REPLACEMENT-PART2.patch](tarball://root/attachments/some-uuid/ticket6371/trac_6371-riemann-theta-REPLACEMENT-PART2.patch) by @cswiercz created at 2011-03-28 18:22:31",
    "created_at": "2011-03-28T18:22:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6371",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6371#issuecomment-50868",
    "user": "https://github.com/cswiercz"
}
```

Attachment [trac_6371-riemann-theta-REPLACEMENT-PART2.patch](tarball://root/attachments/some-uuid/ticket6371/trac_6371-riemann-theta-REPLACEMENT-PART2.patch) by @cswiercz created at 2011-03-28 18:22:31



---

archive/issue_comments_050869.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-03-28T18:22:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6371",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6371#issuecomment-50869",
    "user": "https://github.com/cswiercz"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_050870.json:
```json
{
    "body": "Minor last-minute bug.",
    "created_at": "2011-03-28T18:31:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6371",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6371#issuecomment-50870",
    "user": "https://github.com/cswiercz"
}
```

Minor last-minute bug.



---

archive/issue_comments_050871.json:
```json
{
    "body": "Attachment [trac_6371_riemann-theta-REPLACEMENT-PART3.patch](tarball://root/attachments/some-uuid/ticket6371/trac_6371_riemann-theta-REPLACEMENT-PART3.patch) by @mstreng created at 2011-03-28 18:47:07\n\n(for patchbot)\n\nApply \n\n* [attachment:trac_6371-riemann-theta-REPLACEMENT.patch]\n\n* [attachment:trac_6371-riemann-theta-REPLACEMENT-PART2.patch]\n\n* [attachment:trac_6371_riemann-theta-REPLACEMENT-PART3.patch]",
    "created_at": "2011-03-28T18:47:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6371",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6371#issuecomment-50871",
    "user": "https://github.com/mstreng"
}
```

Attachment [trac_6371_riemann-theta-REPLACEMENT-PART3.patch](tarball://root/attachments/some-uuid/ticket6371/trac_6371_riemann-theta-REPLACEMENT-PART3.patch) by @mstreng created at 2011-03-28 18:47:07

(for patchbot)

Apply 

* [attachment:trac_6371-riemann-theta-REPLACEMENT.patch]

* [attachment:trac_6371-riemann-theta-REPLACEMENT-PART2.patch]

* [attachment:trac_6371_riemann-theta-REPLACEMENT-PART3.patch]



---

archive/issue_comments_050872.json:
```json
{
    "body": "Patchbot doesn't seem to get the message. New attempt: Apply trac_6371-riemann-theta-REPLACEMENT.patch, trac_6371-riemann-theta-REPLACEMENT-PART2.patch, trac_6371_riemann-theta-REPLACEMENT-PART3.patch",
    "created_at": "2011-03-28T19:31:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6371",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6371#issuecomment-50872",
    "user": "https://github.com/mstreng"
}
```

Patchbot doesn't seem to get the message. New attempt: Apply trac_6371-riemann-theta-REPLACEMENT.patch, trac_6371-riemann-theta-REPLACEMENT-PART2.patch, trac_6371_riemann-theta-REPLACEMENT-PART3.patch



---

archive/issue_comments_050873.json:
```json
{
    "body": "Replying to [comment:13 mstreng]:\n> Patchbot doesn't seem to get the message. New attempt: Apply trac_6371-riemann-theta-REPLACEMENT.patch, trac_6371-riemann-theta-REPLACEMENT-PART2.patch, trac_6371_riemann-theta-REPLACEMENT-PART3.patch\n\n\nI tried just deleting the first patch called \"trac_6371-riemann-theta.patch\" but I don't have permissions to do so. I'm also unfamiliar with how to tell patchbot to ignore certain patches.\n\nA manual importing of the three patches using ``sage -hg import <the patch>`` results in no issues.",
    "created_at": "2011-03-28T19:47:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6371",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6371#issuecomment-50873",
    "user": "https://github.com/cswiercz"
}
```

Replying to [comment:13 mstreng]:
> Patchbot doesn't seem to get the message. New attempt: Apply trac_6371-riemann-theta-REPLACEMENT.patch, trac_6371-riemann-theta-REPLACEMENT-PART2.patch, trac_6371_riemann-theta-REPLACEMENT-PART3.patch


I tried just deleting the first patch called "trac_6371-riemann-theta.patch" but I don't have permissions to do so. I'm also unfamiliar with how to tell patchbot to ignore certain patches.

A manual importing of the three patches using ``sage -hg import <the patch>`` results in no issues.



---

archive/issue_comments_050874.json:
```json
{
    "body": "More documentation fixes.",
    "created_at": "2011-03-28T21:20:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6371",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6371#issuecomment-50874",
    "user": "https://github.com/cswiercz"
}
```

More documentation fixes.



---

archive/issue_comments_050875.json:
```json
{
    "body": "Attachment [trac_6371-riemann-theta-REPLACEMENT-PART4.patch](tarball://root/attachments/some-uuid/ticket6371/trac_6371-riemann-theta-REPLACEMENT-PART4.patch) by @cswiercz created at 2011-03-28 21:20:31",
    "created_at": "2011-03-28T21:20:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6371",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6371#issuecomment-50875",
    "user": "https://github.com/cswiercz"
}
```

Attachment [trac_6371-riemann-theta-REPLACEMENT-PART4.patch](tarball://root/attachments/some-uuid/ticket6371/trac_6371-riemann-theta-REPLACEMENT-PART4.patch) by @cswiercz created at 2011-03-28 21:20:31



---

archive/issue_comments_050876.json:
```json
{
    "body": "doctest failures (details emailed to author)",
    "created_at": "2011-03-29T09:18:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6371",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6371#issuecomment-50876",
    "user": "https://github.com/mstreng"
}
```

doctest failures (details emailed to author)



---

archive/issue_comments_050877.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-03-29T09:18:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6371",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6371#issuecomment-50877",
    "user": "https://github.com/mstreng"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_050878.json:
```json
{
    "body": "Fixed derivative calculation errors that resulted in incorrect doctests.",
    "created_at": "2011-03-29T20:50:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6371",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6371#issuecomment-50878",
    "user": "https://github.com/cswiercz"
}
```

Fixed derivative calculation errors that resulted in incorrect doctests.



---

archive/issue_comments_050879.json:
```json
{
    "body": "Attachment [trac_6371-riemann-theta-REPLACEMENT-PART5.patch](tarball://root/attachments/some-uuid/ticket6371/trac_6371-riemann-theta-REPLACEMENT-PART5.patch) by @cswiercz created at 2011-03-29 20:51:59\n\nFixed issues with computing derivatives that resulted in doctest failures. Minor documentation fixes as well.",
    "created_at": "2011-03-29T20:51:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6371",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6371#issuecomment-50879",
    "user": "https://github.com/cswiercz"
}
```

Attachment [trac_6371-riemann-theta-REPLACEMENT-PART5.patch](tarball://root/attachments/some-uuid/ticket6371/trac_6371-riemann-theta-REPLACEMENT-PART5.patch) by @cswiercz created at 2011-03-29 20:51:59

Fixed issues with computing derivatives that resulted in doctest failures. Minor documentation fixes as well.



---

archive/issue_comments_050880.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-03-29T20:51:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6371",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6371#issuecomment-50880",
    "user": "https://github.com/cswiercz"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_050881.json:
```json
{
    "body": "With further examples, I noticed that there were some calculation issues. Traced this back to mixture of notation under Heil's transformation. Rewriting good chunk of the code using only the notation from \"Computing Riemann Theta Functions\" by Deconinck et. al.",
    "created_at": "2011-10-27T15:31:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6371",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6371#issuecomment-50881",
    "user": "https://github.com/cswiercz"
}
```

With further examples, I noticed that there were some calculation issues. Traced this back to mixture of notation under Heil's transformation. Rewriting good chunk of the code using only the notation from "Computing Riemann Theta Functions" by Deconinck et. al.



---

archive/issue_comments_050882.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-10-27T15:31:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6371",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6371#issuecomment-50882",
    "user": "https://github.com/cswiercz"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_050883.json:
```json
{
    "body": "Attachment [trac-6371-part2.patch](tarball://root/attachments/some-uuid/ticket6371/trac-6371-part2.patch) by @cswiercz created at 2011-12-07 19:06:09",
    "created_at": "2011-12-07T19:06:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6371",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6371#issuecomment-50883",
    "user": "https://github.com/cswiercz"
}
```

Attachment [trac-6371-part2.patch](tarball://root/attachments/some-uuid/ticket6371/trac-6371-part2.patch) by @cswiercz created at 2011-12-07 19:06:09



---

archive/issue_comments_050884.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-12-07T19:06:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6371",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6371#issuecomment-50884",
    "user": "https://github.com/cswiercz"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_050885.json:
```json
{
    "body": "Attachment [trac-6371-part3.patch](tarball://root/attachments/some-uuid/ticket6371/trac-6371-part3.patch) by @cswiercz created at 2011-12-07 19:38:40",
    "created_at": "2011-12-07T19:38:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6371",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6371#issuecomment-50885",
    "user": "https://github.com/cswiercz"
}
```

Attachment [trac-6371-part3.patch](tarball://root/attachments/some-uuid/ticket6371/trac-6371-part3.patch) by @cswiercz created at 2011-12-07 19:38:40



---

archive/issue_comments_050886.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-12-07T19:48:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6371",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6371#issuecomment-50886",
    "user": "https://trac.sagemath.org/admin/accounts/users/bern4rd"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_015004.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2011-12-09T10:26:54Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6371",
    "milestone": "sage-4.8",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6371#event-15004"
}
```



---

archive/issue_comments_050887.json:
```json
{
    "body": "I get a doctest failure in `devel/sage/sage/all.py`",
    "created_at": "2011-12-10T10:42:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6371",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6371#issuecomment-50887",
    "user": "https://github.com/jdemeyer"
}
```

I get a doctest failure in `devel/sage/sage/all.py`



---

archive/issue_comments_050888.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2011-12-10T10:42:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6371",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6371#issuecomment-50888",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_050889.json:
```json
{
    "body": "Replying to [comment:27 jdemeyer]:\n> I get a doctest failure in `devel/sage/sage/all.py`\n\n\nI see. The error is:\n\n```\n\nsage -t  \"devel/sage-6371/sage/all.py\"                      \n**********************************************************************\nFile \"/home/cswiercz/sage-4.7.1/devel/sage-6371/sage/all.py\", line 17:\n    sage: len(frames)\nExpected:\n    11\nGot:\n    26\n**********************************************************************\n1 items had failures:\n   1 of   8 in __main__.example_0\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file /home/cswiercz/.sage//tmp/all_20664.py\n\t [3.4 s]\n```\n\nHowever, I'm not qualified to make a fix since I don't really understand the purpose of this test. Does anyone on cc: know what's going on in this file and why my Riemann Theta code would affect it?",
    "created_at": "2011-12-10T20:01:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6371",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6371#issuecomment-50889",
    "user": "https://github.com/cswiercz"
}
```

Replying to [comment:27 jdemeyer]:
> I get a doctest failure in `devel/sage/sage/all.py`


I see. The error is:

```

sage -t  "devel/sage-6371/sage/all.py"                      
**********************************************************************
File "/home/cswiercz/sage-4.7.1/devel/sage-6371/sage/all.py", line 17:
    sage: len(frames)
Expected:
    11
Got:
    26
**********************************************************************
1 items had failures:
   1 of   8 in __main__.example_0
***Test Failed*** 1 failures.
For whitespace errors, see the file /home/cswiercz/.sage//tmp/all_20664.py
	 [3.4 s]
```

However, I'm not qualified to make a fix since I don't really understand the purpose of this test. Does anyone on cc: know what's going on in this file and why my Riemann Theta code would affect it?



---

archive/issue_comments_050890.json:
```json
{
    "body": "Chris:  Have you read #10570?   That explains what this test is about and why it is important.  Your code evidently gets imported when Sage starts up, and does something potentially leaky.",
    "created_at": "2011-12-10T20:17:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6371",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6371#issuecomment-50890",
    "user": "https://github.com/williamstein"
}
```

Chris:  Have you read #10570?   That explains what this test is about and why it is important.  Your code evidently gets imported when Sage starts up, and does something potentially leaky.



---

archive/issue_comments_050891.json:
```json
{
    "body": "Replying to [comment:29 was]:\n> Chris:  Have you read #10570?   That explains what this test is about and why it is important.  Your code evidently gets imported when Sage starts up, and does something potentially leaky. \n\n\nYes, I read this ticket but I'm not sure how to resolve the \"potential leakiness\".\n\nOne candidate for where this issue might be coming from is my use of a class constructor. I have some code in `riemann_theta.py` in the following form:\n\n```\ndef RiemannTheta_Constructor(foo, bar):\n    class RiemannTheta(Function_RiemannTheta):\n        def __init__(...):\n            self.foo = foo\n            self.bar = bar\n            Function_RiemannTheta.__init__()\n\n    return RiemannTheta(...)\n\nRiemannTheta = RiemannTheta_Constructor\n\nclass Function_RiemannTheta(BuiltinFunction):\n   ...\n```\n\nI needed to do things this way so I could parameterize `RiemannTheta` by things such as directional derivative and Riemann matrix. Otherwise, things behave not as expected due to the way `BuiltinFunction` behaves. (For example, two instances of `RiemannTheta` would share the same Riemann matrix or derivatives.) With the above code structure I found that these issues don't arise and two instances of `RiemannTheta` behaved independently as expected.\n\nI'd hate to introduce memory leaks due to my lack of understanding of `BuiltinFunction`. (Granted, the documentation for creating classes that inherit `BuiltinFunction` is severely lacking as well.) However, I don't see how I'd start fixing the issue aside from increasing `len(frames)` in the error message above from 11 to 26. Any suggested resources on how I could better perform what I'm doing in the class and function construction above? Again, the `BuiltinFunction` documentation wasn't helpful beyond copying what preexisting inheritors in `sage.functions` do.",
    "created_at": "2011-12-10T20:42:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6371",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6371#issuecomment-50891",
    "user": "https://github.com/cswiercz"
}
```

Replying to [comment:29 was]:
> Chris:  Have you read #10570?   That explains what this test is about and why it is important.  Your code evidently gets imported when Sage starts up, and does something potentially leaky. 


Yes, I read this ticket but I'm not sure how to resolve the "potential leakiness".

One candidate for where this issue might be coming from is my use of a class constructor. I have some code in `riemann_theta.py` in the following form:

```
def RiemannTheta_Constructor(foo, bar):
    class RiemannTheta(Function_RiemannTheta):
        def __init__(...):
            self.foo = foo
            self.bar = bar
            Function_RiemannTheta.__init__()

    return RiemannTheta(...)

RiemannTheta = RiemannTheta_Constructor

class Function_RiemannTheta(BuiltinFunction):
   ...
```

I needed to do things this way so I could parameterize `RiemannTheta` by things such as directional derivative and Riemann matrix. Otherwise, things behave not as expected due to the way `BuiltinFunction` behaves. (For example, two instances of `RiemannTheta` would share the same Riemann matrix or derivatives.) With the above code structure I found that these issues don't arise and two instances of `RiemannTheta` behaved independently as expected.

I'd hate to introduce memory leaks due to my lack of understanding of `BuiltinFunction`. (Granted, the documentation for creating classes that inherit `BuiltinFunction` is severely lacking as well.) However, I don't see how I'd start fixing the issue aside from increasing `len(frames)` in the error message above from 11 to 26. Any suggested resources on how I could better perform what I'm doing in the class and function construction above? Again, the `BuiltinFunction` documentation wasn't helpful beyond copying what preexisting inheritors in `sage.functions` do.



---

archive/issue_comments_050892.json:
```json
{
    "body": "I don't know much about `BuiltinFunction`, but I suspect that it isn't meant for what you are trying to do. All the examples that I know of `BuiltinFunction` are single fixed functions, independent of any parameters, such as cos, min, max, `IndefiniteIntegral`, Gamma, dirac_delta, etc.\n\nYour objects however depend on a parameter Omega, and are functions only of z. They are maps `theta(Omega): CC^g --> CC : z |--> theta(z)`. This will not be a \"built-in function of Sage\" for every Omega, so it does not sound to me like this should be a `BuiltinFunction` object. Maybe the memory leak is caused by this.\n\nThe function `theta: CC^g x H_g --> CC : (z, Omega) |--> theta(z, Omega)` definitely make sense as a built-in function, but not a function `theta(Omega) : CC^g --> C` that depends on Omega. In other words, if you have a function for which Omega is not a parameter but an actual variable, then that would make a good built-in function.\n\nps. Could you make sure you break the lines in the patch at 79 characters?",
    "created_at": "2012-01-12T12:48:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6371",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6371#issuecomment-50892",
    "user": "https://github.com/mstreng"
}
```

I don't know much about `BuiltinFunction`, but I suspect that it isn't meant for what you are trying to do. All the examples that I know of `BuiltinFunction` are single fixed functions, independent of any parameters, such as cos, min, max, `IndefiniteIntegral`, Gamma, dirac_delta, etc.

Your objects however depend on a parameter Omega, and are functions only of z. They are maps `theta(Omega): CC^g --> CC : z |--> theta(z)`. This will not be a "built-in function of Sage" for every Omega, so it does not sound to me like this should be a `BuiltinFunction` object. Maybe the memory leak is caused by this.

The function `theta: CC^g x H_g --> CC : (z, Omega) |--> theta(z, Omega)` definitely make sense as a built-in function, but not a function `theta(Omega) : CC^g --> C` that depends on Omega. In other words, if you have a function for which Omega is not a parameter but an actual variable, then that would make a good built-in function.

ps. Could you make sure you break the lines in the patch at 79 characters?



---

archive/issue_comments_050893.json:
```json
{
    "body": "Hello mstreng,\n\nReplying to [comment:31 mstreng]:\n> I don't know much about `BuiltinFunction`, but I suspect that it isn't meant for what you are trying to do. All the examples that I know of `BuiltinFunction` are single fixed functions, independent of any parameters, such as cos, min, max, `IndefiniteIntegral`, Gamma, dirac_delta, etc.\n\n\nIt was my misunderstanding that `BuiltinFunction` is necessary for doing symbolic manipulation. My only reason for using it is so I can compute derivatives, etc. If you know of an alternate way to enable symbolics then I'd love to hear about it!\n\n> Your objects however depend on a parameter Omega, and are functions only of z. They are maps `theta(Omega): CC^g --> CC : z |--> theta(z)`. This will not be a \"built-in function of Sage\" for every Omega, so it does not sound to me like this should be a `BuiltinFunction` object. Maybe the memory leak is caused by this.\n\n\nI'll experiment with the code and see if this is an issue.\n\nIn practice, $\\Omega$ is treated more as a parameter than an argument of the Riemann theta function. That is, $\\Omega$ is usually fixed and $z$ varies. Several users of my code would like to see this behavior be reflected by having the Riemann theta function be \"initialized\" by this matrix.\n\nHowever, if memory leaks are unavoidable in this context then I suppose I'll just have to make $\\Omega$ behave like an argument no different from $z$.\n\n> The function `theta: CC^g x H_g --> CC : (z, Omega) |--> theta(z, Omega)` definitely make sense as a built-in function, but not a function `theta(Omega) : CC^g --> C` that depends on Omega. In other words, if you have a function for which Omega is not a parameter but an actual variable, then that would make a good built-in function.\n\n\nMakes sense.\n\n> ps. Could you make sure you break the lines in the patch at 79 characters?\n\n\nOf course! (As an in-terminal emacs user I usually try to do this anyway.)",
    "created_at": "2012-01-18T18:48:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6371",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6371#issuecomment-50893",
    "user": "https://github.com/cswiercz"
}
```

Hello mstreng,

Replying to [comment:31 mstreng]:
> I don't know much about `BuiltinFunction`, but I suspect that it isn't meant for what you are trying to do. All the examples that I know of `BuiltinFunction` are single fixed functions, independent of any parameters, such as cos, min, max, `IndefiniteIntegral`, Gamma, dirac_delta, etc.


It was my misunderstanding that `BuiltinFunction` is necessary for doing symbolic manipulation. My only reason for using it is so I can compute derivatives, etc. If you know of an alternate way to enable symbolics then I'd love to hear about it!

> Your objects however depend on a parameter Omega, and are functions only of z. They are maps `theta(Omega): CC^g --> CC : z |--> theta(z)`. This will not be a "built-in function of Sage" for every Omega, so it does not sound to me like this should be a `BuiltinFunction` object. Maybe the memory leak is caused by this.


I'll experiment with the code and see if this is an issue.

In practice, $\Omega$ is treated more as a parameter than an argument of the Riemann theta function. That is, $\Omega$ is usually fixed and $z$ varies. Several users of my code would like to see this behavior be reflected by having the Riemann theta function be "initialized" by this matrix.

However, if memory leaks are unavoidable in this context then I suppose I'll just have to make $\Omega$ behave like an argument no different from $z$.

> The function `theta: CC^g x H_g --> CC : (z, Omega) |--> theta(z, Omega)` definitely make sense as a built-in function, but not a function `theta(Omega) : CC^g --> C` that depends on Omega. In other words, if you have a function for which Omega is not a parameter but an actual variable, then that would make a good built-in function.


Makes sense.

> ps. Could you make sure you break the lines in the patch at 79 characters?


Of course! (As an in-terminal emacs user I usually try to do this anyway.)



---

archive/issue_comments_050894.json:
```json
{
    "body": "Hi Chris,\n\nReplying to [comment:32 cswiercz]:\n> If you know of an alternate way to enable symbolics then I'd love to hear about it!\n\n\nI don't: I've never implemented any of them.\n\n> In practice, $\\Omega$ is treated more as a parameter than an argument of the Riemann theta function. That is, $\\Omega$ is usually fixed and $z$ varies.\n\n\n:) Actually, when I use theta functions in my research, Omega is usually the variable and z is usually some fixed vector in with entries in QQ.\n\nAnyway, what is the (programming technical) reason for having objects that depend on Omega? Is there some kind of caching involved? Some part of the algorithm that depends on Omega only and that you only want to do once?\n\nMarco",
    "created_at": "2012-01-18T19:31:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6371",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6371#issuecomment-50894",
    "user": "https://github.com/mstreng"
}
```

Hi Chris,

Replying to [comment:32 cswiercz]:
> If you know of an alternate way to enable symbolics then I'd love to hear about it!


I don't: I've never implemented any of them.

> In practice, $\Omega$ is treated more as a parameter than an argument of the Riemann theta function. That is, $\Omega$ is usually fixed and $z$ varies.


:) Actually, when I use theta functions in my research, Omega is usually the variable and z is usually some fixed vector in with entries in QQ.

Anyway, what is the (programming technical) reason for having objects that depend on Omega? Is there some kind of caching involved? Some part of the algorithm that depends on Omega only and that you only want to do once?

Marco



---

archive/issue_comments_050895.json:
```json
{
    "body": "Marco,\n\n> :) Actually, when I use theta functions in my research, Omega is usually the variable and z is usually some fixed vector in with entries in QQ.\n> \n> Anyway, what is the (programming technical) reason for having objects that depend on Omega? Is there some kind of caching involved? Some part of the algorithm that depends on Omega only and that you only want to do once?\n\n\nInteresting. I've only seen one other instance in which Omega was varied: it was in the context of solving particular boundary value problems.) If you don't mind, do you have a paper you can send me about your work? (cswiercz [at] gmail ]dot[ com)\n\nI agree that there should be no distinction between the two parameters. From what I understood about `BuiltinFunction}}, though, the purpose of distinguishing Omega as a parameter is to make it easy to send symbolic output. Since I initially made this decision, however, I've learned more about the way Sage ({{{BuiltinFuncion`?) handles inputs and determines if they're symbolic. A rewriting of the way arguments are sent to `RiemannTheta` should be possible.\n\nI'll see what I can do about restructuring the code. Thank you very much for your input and suggestions. I'll keep everyone posted on my (slow) progress.",
    "created_at": "2012-01-18T21:02:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6371",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6371#issuecomment-50895",
    "user": "https://github.com/cswiercz"
}
```

Marco,

> :) Actually, when I use theta functions in my research, Omega is usually the variable and z is usually some fixed vector in with entries in QQ.
> 
> Anyway, what is the (programming technical) reason for having objects that depend on Omega? Is there some kind of caching involved? Some part of the algorithm that depends on Omega only and that you only want to do once?


Interesting. I've only seen one other instance in which Omega was varied: it was in the context of solving particular boundary value problems.) If you don't mind, do you have a paper you can send me about your work? (cswiercz [at] gmail ]dot[ com)

I agree that there should be no distinction between the two parameters. From what I understood about `BuiltinFunction}}, though, the purpose of distinguishing Omega as a parameter is to make it easy to send symbolic output. Since I initially made this decision, however, I've learned more about the way Sage ({{{BuiltinFuncion`?) handles inputs and determines if they're symbolic. A rewriting of the way arguments are sent to `RiemannTheta` should be possible.

I'll see what I can do about restructuring the code. Thank you very much for your input and suggestions. I'll keep everyone posted on my (slow) progress.



---

archive/issue_events_015005.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6371",
    "milestone": "sage-4.8",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6371#event-15005"
}
```



---

archive/issue_events_015006.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6371",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6371#event-15006"
}
```



---

archive/issue_events_015007.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6371",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6371#event-15007"
}
```



---

archive/issue_events_015008.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6371",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6371#event-15008"
}
```



---

archive/issue_events_015009.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6371",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6371#event-15009"
}
```



---

archive/issue_events_015010.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6371",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6371#event-15010"
}
```



---

archive/issue_events_015011.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6371",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6371#event-15011"
}
```



---

archive/issue_events_015012.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6371",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6371#event-15012"
}
```



---

archive/issue_comments_050896.json:
```json
{
    "body": "I made a git branch from the patches, but it does not work. I have not tried to\nfind where problems are.\n\n---\nNew commits:",
    "created_at": "2015-03-10T22:15:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6371",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6371#issuecomment-50896",
    "user": "https://github.com/fchapoton"
}
```

I made a git branch from the patches, but it does not work. I have not tried to
find where problems are.

---
New commits:



---

archive/issue_comments_050897.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2015-03-10T22:17:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6371",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6371#issuecomment-50897",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_events_015013.json:
```json
{
    "actor": "https://github.com/fchapoton",
    "created_at": "2016-01-06T20:58:40Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6371",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6371#event-15013"
}
```



---

archive/issue_events_015014.json:
```json
{
    "actor": "https://github.com/fchapoton",
    "created_at": "2016-01-06T20:58:40Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6371",
    "milestone": "sage-7.0",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6371#event-15014"
}
```



---

archive/issue_comments_050898.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2016-02-18T20:20:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6371",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6371#issuecomment-50898",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_events_015015.json:
```json
{
    "actor": "https://github.com/fchapoton",
    "created_at": "2016-02-19T09:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6371",
    "milestone": "sage-7.0",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6371#event-15015"
}
```



---

archive/issue_events_015016.json:
```json
{
    "actor": "https://github.com/fchapoton",
    "created_at": "2016-02-19T09:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6371",
    "milestone": "sage-7.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6371#event-15016"
}
```



---

archive/issue_comments_050899.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2016-06-10T18:15:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6371",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6371#issuecomment-50899",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_050900.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2016-07-11T11:07:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6371",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6371#issuecomment-50900",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_050901.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2017-06-08T19:55:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6371",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6371#issuecomment-50901",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_050902.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2018-03-11T19:55:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6371",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6371#issuecomment-50902",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_050903.json:
```json
{
    "body": "A student will be doing a summer project towards getting Riemann theta functions, their directional derivatives, and characteristics into sage. Can we repurpose this ticket for that?",
    "created_at": "2021-02-25T07:47:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6371",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6371#issuecomment-50903",
    "user": "https://github.com/nbruin"
}
```

A student will be doing a summer project towards getting Riemann theta functions, their directional derivatives, and characteristics into sage. Can we repurpose this ticket for that?



---

archive/issue_comments_050904.json:
```json
{
    "body": "sure, good luck",
    "created_at": "2021-02-26T16:25:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6371",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6371#issuecomment-50904",
    "user": "https://github.com/fchapoton"
}
```

sure, good luck



---

archive/issue_comments_050905.json:
```json
{
    "body": "sounds good to me",
    "created_at": "2021-02-27T12:28:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6371",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6371#issuecomment-50905",
    "user": "https://github.com/mstreng"
}
```

sounds good to me



---

archive/issue_comments_050906.json:
```json
{
    "body": "The work is done:\n\nhttps://github.com/nbruin/RiemannTheta\n\nI have for now published it as a separate pip-able package in the hope that makes it easier for non-sage developers to install it, use it, and comment on it, but eventually the proper place is probably within sage (it's not a lot of code and it's tightly bound to a lot of sage-specific functionality). So the question prior to making a branch for inclusion into sage:\n\n* functionality and correctness checks. We tried to be careful, but testing generally needs to be done by other people too to get a good idea of how the code performs more generally\n* where to put it into sage? (sage.numerical would be appropriate, or we could place it next to riemann_surfaces because theoretically that's what it's close too -- although of course theta functions are properties of complex lattices, not particularly of Riemann surfaces.\n* do riemann_theta and siegel_reduction go in the same spot?\n\nAlso, once it's in, where/how do we expose the functionality in the global namespace (if at all)? Note that the design is a little less ambitious than the cswiercz and no attempt is made to have an `SR` wrapper of the numerical tool. It does have the big advantage that, as far as I know, the code produces answers of the accuracy one can reasonably expect and does so with reasonable efficiency.",
    "created_at": "2021-09-26T18:37:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6371",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6371#issuecomment-50906",
    "user": "https://github.com/nbruin"
}
```

The work is done:

https://github.com/nbruin/RiemannTheta

I have for now published it as a separate pip-able package in the hope that makes it easier for non-sage developers to install it, use it, and comment on it, but eventually the proper place is probably within sage (it's not a lot of code and it's tightly bound to a lot of sage-specific functionality). So the question prior to making a branch for inclusion into sage:

* functionality and correctness checks. We tried to be careful, but testing generally needs to be done by other people too to get a good idea of how the code performs more generally
* where to put it into sage? (sage.numerical would be appropriate, or we could place it next to riemann_surfaces because theoretically that's what it's close too -- although of course theta functions are properties of complex lattices, not particularly of Riemann surfaces.
* do riemann_theta and siegel_reduction go in the same spot?

Also, once it's in, where/how do we expose the functionality in the global namespace (if at all)? Note that the design is a little less ambitious than the cswiercz and no attempt is made to have an `SR` wrapper of the numerical tool. It does have the big advantage that, as far as I know, the code produces answers of the accuracy one can reasonably expect and does so with reasonable efficiency.
