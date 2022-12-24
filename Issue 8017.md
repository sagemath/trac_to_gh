# Issue 8017: incorrect trailing digits for continued fraction

archive/issues_008017.json:
```json
{
    "body": "Assignee: AlexGhitza\n\nCC:  was\n\n\n```\ncontinued_fraction(sqrt(2))\n[1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1]\n```\n\n\nFollowup to and depends on #5107, which documents the function better. \n\nIssue created by migration from https://trac.sagemath.org/ticket/8017\n\n",
    "created_at": "2010-01-21T00:12:58Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5.3",
    "title": "incorrect trailing digits for continued fraction",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8017",
    "user": "robertwb"
}
```
Assignee: AlexGhitza

CC:  was


```
continued_fraction(sqrt(2))
[1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1]
```


Followup to and depends on #5107, which documents the function better. 

Issue created by migration from https://trac.sagemath.org/ticket/8017





---

archive/issue_comments_070045.json:
```json
{
    "body": "Attachment [8017-cont-frac.patch](tarball://root/attachments/some-uuid/ticket8017/8017-cont-frac.patch) by robertwb created at 2010-01-21 01:23:43",
    "created_at": "2010-01-21T01:23:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8017",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8017#issuecomment-70045",
    "user": "robertwb"
}
```

Attachment [8017-cont-frac.patch](tarball://root/attachments/some-uuid/ticket8017/8017-cont-frac.patch) by robertwb created at 2010-01-21 01:23:43



---

archive/issue_comments_070046.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-21T01:25:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8017",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8017#issuecomment-70046",
    "user": "robertwb"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_070047.json:
```json
{
    "body": "This does change the definition from \"continued fraction expansion of a real approximation\" to \"truncation of continued fraction expansion.\" It also adds an nterms option to compute a specified number of terms.",
    "created_at": "2010-01-21T01:25:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8017",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8017#issuecomment-70047",
    "user": "robertwb"
}
```

This does change the definition from "continued fraction expansion of a real approximation" to "truncation of continued fraction expansion." It also adds an nterms option to compute a specified number of terms.



---

archive/issue_comments_070048.json:
```json
{
    "body": "Robert, this seems to be great work! However a small question: for *exact* symbolic input,\nthe truncated continued fraction should not depend on the initial floating-point\napproximation, and should be a truncation of the (finite or infinite) continued fraction:\n\n```\nsage: continued_fraction(22/7,bits=4)\n[3, 4]\nsage: continued_fraction(22/7,bits=5)\n[3, 8]\n```\n\nI guess the above should give instead:\n\n```\nsage: continued_fraction(RealIntervalField(4)(22/7))\n[3]\nsage: continued_fraction(RealIntervalField(5)(22/7))\n[3]\n```\n\nCan the same problem happen with say sqrt(2), or is it only for rationals?",
    "created_at": "2010-03-14T20:24:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8017",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8017#issuecomment-70048",
    "user": "zimmerma"
}
```

Robert, this seems to be great work! However a small question: for *exact* symbolic input,
the truncated continued fraction should not depend on the initial floating-point
approximation, and should be a truncation of the (finite or infinite) continued fraction:

```
sage: continued_fraction(22/7,bits=4)
[3, 4]
sage: continued_fraction(22/7,bits=5)
[3, 8]
```

I guess the above should give instead:

```
sage: continued_fraction(RealIntervalField(4)(22/7))
[3]
sage: continued_fraction(RealIntervalField(5)(22/7))
[3]
```

Can the same problem happen with say sqrt(2), or is it only for rationals?



---

archive/issue_comments_070049.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2010-03-14T20:24:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8017",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8017#issuecomment-70049",
    "user": "zimmerma"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_070050.json:
```json
{
    "body": "Attachment [8017-contfrac-referee-fixes.patch](tarball://root/attachments/some-uuid/ticket8017/8017-contfrac-referee-fixes.patch) by robertwb created at 2010-03-15 20:06:32",
    "created_at": "2010-03-15T20:06:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8017",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8017#issuecomment-70050",
    "user": "robertwb"
}
```

Attachment [8017-contfrac-referee-fixes.patch](tarball://root/attachments/some-uuid/ticket8017/8017-contfrac-referee-fixes.patch) by robertwb created at 2010-03-15 20:06:32



---

archive/issue_comments_070051.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2010-03-15T20:07:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8017",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8017#issuecomment-70051",
    "user": "robertwb"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_070052.json:
```json
{
    "body": "Thank you for looking at this. As you can probably tell, the current behavior really bothers me ;). I've fixed the case above (yes, it only impacted rationals).",
    "created_at": "2010-03-15T20:07:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8017",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8017#issuecomment-70052",
    "user": "robertwb"
}
```

Thank you for looking at this. As you can probably tell, the current behavior really bothers me ;). I've fixed the case above (yes, it only impacted rationals).



---

archive/issue_comments_070053.json:
```json
{
    "body": "while I'm running the doctests, a few comments: (1) maybe the documentation should say that the\nterms of the truncated continued fraction are (now) guaranteed exact (using interval arithmetic);\n(2) `If nterms is given, the precision is increased until the specified number of terms can be computed`: if possible, for example 22/7 will give only two terms.\n\nI also suggest giving an additional example showing that we can give as input a floating-point\ninterval, and the difference with a floating-point number (where initial rounding error can\ngive an incorrect result):\n\n```\nsage: continued_fraction(RealField(39)(e))\n[2, 1, 2, 1, 1, 4, 1, 1, 6, 1, 1, 8, 1, 1, 10, 2]\nsage: continued_fraction(RealIntervalField(39)(e))\n[2, 1, 2, 1, 1, 4, 1, 1, 6, 1, 1, 8, 1, 1, 10]\n```\n\n\nIn the meantime the doctests finished, and I get two failures:\n\n```\nsage -t  core2/devel/sage-8017/sage/combinat/words/word_generators.py # 1 doctests failed\nsage -t  core2/devel/sage-8017/sage/tests/book_stein_ent.py # 13 doctests failed\n```\n",
    "created_at": "2010-03-16T07:57:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8017",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8017#issuecomment-70053",
    "user": "zimmerma"
}
```

while I'm running the doctests, a few comments: (1) maybe the documentation should say that the
terms of the truncated continued fraction are (now) guaranteed exact (using interval arithmetic);
(2) `If nterms is given, the precision is increased until the specified number of terms can be computed`: if possible, for example 22/7 will give only two terms.

I also suggest giving an additional example showing that we can give as input a floating-point
interval, and the difference with a floating-point number (where initial rounding error can
give an incorrect result):

```
sage: continued_fraction(RealField(39)(e))
[2, 1, 2, 1, 1, 4, 1, 1, 6, 1, 1, 8, 1, 1, 10, 2]
sage: continued_fraction(RealIntervalField(39)(e))
[2, 1, 2, 1, 1, 4, 1, 1, 6, 1, 1, 8, 1, 1, 10]
```


In the meantime the doctests finished, and I get two failures:

```
sage -t  core2/devel/sage-8017/sage/combinat/words/word_generators.py # 1 doctests failed
sage -t  core2/devel/sage-8017/sage/tests/book_stein_ent.py # 13 doctests failed
```




---

archive/issue_comments_070054.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-03-16T07:57:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8017",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8017#issuecomment-70054",
    "user": "zimmerma"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_070055.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-07-29T05:21:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8017",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8017#issuecomment-70055",
    "user": "robertwb"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_070056.json:
```json
{
    "body": "positive review, good work, Robert! However I see as a side effect you had to change the doctests\nin William's book, which has the consequence that those examples will not work any more as in the\nbook (but better now). This is a concern for me with the book we wrote about Sage (btw, the\ndoctest of the number theory chapter is ready for review, see #9395).\n\nPaul",
    "created_at": "2010-07-29T09:24:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8017",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8017#issuecomment-70056",
    "user": "zimmerma"
}
```

positive review, good work, Robert! However I see as a side effect you had to change the doctests
in William's book, which has the consequence that those examples will not work any more as in the
book (but better now). This is a concern for me with the book we wrote about Sage (btw, the
doctest of the number theory chapter is ready for review, see #9395).

Paul



---

archive/issue_comments_070057.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-07-29T09:24:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8017",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8017#issuecomment-70057",
    "user": "zimmerma"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_070058.json:
```json
{
    "body": "Attachment [8017-contfrac-referee2.patch](tarball://root/attachments/some-uuid/ticket8017/8017-contfrac-referee2.patch) by robertwb created at 2010-07-29 18:15:23\n\nThanks for being so quick to look at this after such a long wait. Yes, I was thinking about this when I made these changes. The answers are not substantially different, and should be clear to any user that the current behavior is correct (e.g. by computing things out to higher precision or consulting external sources). \n\nMost importantly, the commands used are not broken or semantically different, which would be really bad. I refreshed the patch just inserting a little note about the change (and, of course, it will be fully recorded in the revision control system).",
    "created_at": "2010-07-29T18:15:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8017",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8017#issuecomment-70058",
    "user": "robertwb"
}
```

Attachment [8017-contfrac-referee2.patch](tarball://root/attachments/some-uuid/ticket8017/8017-contfrac-referee2.patch) by robertwb created at 2010-07-29 18:15:23

Thanks for being so quick to look at this after such a long wait. Yes, I was thinking about this when I made these changes. The answers are not substantially different, and should be clear to any user that the current behavior is correct (e.g. by computing things out to higher precision or consulting external sources). 

Most importantly, the commands used are not broken or semantically different, which would be really bad. I refreshed the patch just inserting a little note about the change (and, of course, it will be fully recorded in the revision control system).



---

archive/issue_comments_070059.json:
```json
{
    "body": "Should the release manager merge all three patches?  By the way, the first patch is missing a Mercurial header and the second a descriptive commit string.",
    "created_at": "2010-08-01T23:29:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8017",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8017#issuecomment-70059",
    "user": "mpatel"
}
```

Should the release manager merge all three patches?  By the way, the first patch is missing a Mercurial header and the second a descriptive commit string.



---

archive/issue_comments_070060.json:
```json
{
    "body": "Changing status from positive_review to needs_info.",
    "created_at": "2010-08-01T23:29:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8017",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8017#issuecomment-70060",
    "user": "mpatel"
}
```

Changing status from positive_review to needs_info.



---

archive/issue_comments_070061.json:
```json
{
    "body": "Attachment [8017-all.patch](tarball://root/attachments/some-uuid/ticket8017/8017-all.patch) by robertwb created at 2010-08-04 07:43:06\n\napply only this patch",
    "created_at": "2010-08-04T07:43:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8017",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8017#issuecomment-70061",
    "user": "robertwb"
}
```

Attachment [8017-all.patch](tarball://root/attachments/some-uuid/ticket8017/8017-all.patch) by robertwb created at 2010-08-04 07:43:06

apply only this patch



---

archive/issue_comments_070062.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2010-08-04T07:44:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8017",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8017#issuecomment-70062",
    "user": "robertwb"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_070063.json:
```json
{
    "body": "I have folded all three patches into 8017-all.patch, apply that one.",
    "created_at": "2010-08-04T07:44:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8017",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8017#issuecomment-70063",
    "user": "robertwb"
}
```

I have folded all three patches into 8017-all.patch, apply that one.



---

archive/issue_comments_070064.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-08-04T07:44:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8017",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8017#issuecomment-70064",
    "user": "robertwb"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_070065.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-08-09T09:47:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8017",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8017#issuecomment-70065",
    "user": "mpatel"
}
```

Resolution: fixed
