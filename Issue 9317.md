# Issue 9317: prime_to_S_part, is_S_unit, is_S_integral

archive/issues_009317.json:
```json
{
    "body": "Assignee: @loefflerd\n\nCC:  @JohnCremona rkirov\n\nKeywords: S_part\n\nThis contains the functions prime_to_S_part, is_S_unit, is_S_integral for number field ideals.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9317\n\n",
    "created_at": "2010-06-23T05:46:39Z",
    "labels": [
        "component: number fields",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5.2",
    "title": "prime_to_S_part, is_S_unit, is_S_integral",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9317",
    "user": "https://github.com/adeines"
}
```
Assignee: @loefflerd

CC:  @JohnCremona rkirov

Keywords: S_part

This contains the functions prime_to_S_part, is_S_unit, is_S_integral for number field ideals.

Issue created by migration from https://trac.sagemath.org/ticket/9317





---

archive/issue_comments_087661.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-06-23T05:56:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9317",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9317#issuecomment-87661",
    "user": "https://github.com/robertwb"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_087662.json:
```json
{
    "body": "Attachment [S_part.patch](tarball://root/attachments/some-uuid/ticket9317/S_part.patch) by @robertwb created at 2010-06-23 05:56:08",
    "created_at": "2010-06-23T05:56:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9317",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9317#issuecomment-87662",
    "user": "https://github.com/robertwb"
}
```

Attachment [S_part.patch](tarball://root/attachments/some-uuid/ticket9317/S_part.patch) by @robertwb created at 2010-06-23 05:56:08



---

archive/issue_comments_087663.json:
```json
{
    "body": "Shouldn't these be like ` is_s_unit `  instead of the capital s?",
    "created_at": "2010-06-23T06:39:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9317",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9317#issuecomment-87663",
    "user": "https://github.com/mwhansen"
}
```

Shouldn't these be like ` is_s_unit `  instead of the capital s?



---

archive/issue_comments_087664.json:
```json
{
    "body": "Attachment [trac_9317-review.patch](tarball://root/attachments/some-uuid/ticket9317/trac_9317-review.patch) by @JohnCremona created at 2010-06-23 07:05:44\n\nApply after previous patch",
    "created_at": "2010-06-23T07:05:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9317",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9317#issuecomment-87664",
    "user": "https://github.com/JohnCremona"
}
```

Attachment [trac_9317-review.patch](tarball://root/attachments/some-uuid/ticket9317/trac_9317-review.patch) by @JohnCremona created at 2010-06-23 07:05:44

Apply after previous patch



---

archive/issue_comments_087665.json:
```json
{
    "body": "The code looks good and applies to 4.4.4.alpha1.  There were several glitches in the formatting of the docstrings, which I have fixed in the second patch (which needs to be applied after the first).\n\nNote:  to test the syntax of the docstrings, do \"sage -docbuild reference html\" which should rebuild the reference manual pages for files which have been modified.  Look out for Warnings and Errors.  Also, look at the html output to see if it looks right!\n\nReply to mhansen:   The capital S is standard mathematical notation.  This also matches the functions sage.rings.rational.Rational.is_S_integral and sage.rings.rational.Rational.is_S_unit (which I wrote so this is not an independent test!)\n\nNote:  this patch was written by some of the students at Sage Days 22, and the intention is that some other students in the same group will review it on Wednesday June 23 as part of their Sage training!",
    "created_at": "2010-06-23T07:11:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9317",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9317#issuecomment-87665",
    "user": "https://github.com/JohnCremona"
}
```

The code looks good and applies to 4.4.4.alpha1.  There were several glitches in the formatting of the docstrings, which I have fixed in the second patch (which needs to be applied after the first).

Note:  to test the syntax of the docstrings, do "sage -docbuild reference html" which should rebuild the reference manual pages for files which have been modified.  Look out for Warnings and Errors.  Also, look at the html output to see if it looks right!

Reply to mhansen:   The capital S is standard mathematical notation.  This also matches the functions sage.rings.rational.Rational.is_S_integral and sage.rings.rational.Rational.is_S_unit (which I wrote so this is not an independent test!)

Note:  this patch was written by some of the students at Sage Days 22, and the intention is that some other students in the same group will review it on Wednesday June 23 as part of their Sage training!



---

archive/issue_comments_087666.json:
```json
{
    "body": "Replying to [comment:3 cremona]:\n> Reply to mhansen:   The capital S is standard mathematical notation.  This also matches the functions sage.rings.rational.Rational.is_S_integral and sage.rings.rational.Rational.is_S_unit (which I wrote so this is not an independent test!)\n\n\nOn the other hand, we don't capitalize things like Eulerian in `is_eulerian`.  Whatever is decided, it should be consistent :-)",
    "created_at": "2010-06-23T07:27:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9317",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9317#issuecomment-87666",
    "user": "https://github.com/mwhansen"
}
```

Replying to [comment:3 cremona]:
> Reply to mhansen:   The capital S is standard mathematical notation.  This also matches the functions sage.rings.rational.Rational.is_S_integral and sage.rings.rational.Rational.is_S_unit (which I wrote so this is not an independent test!)


On the other hand, we don't capitalize things like Eulerian in `is_eulerian`.  Whatever is decided, it should be consistent :-)



---

archive/issue_comments_087667.json:
```json
{
    "body": "Attachment [trac_9317_doctest_change.patch](tarball://root/attachments/some-uuid/ticket9317/trac_9317_doctest_change.patch) by @adeines created at 2010-06-23 16:12:35",
    "created_at": "2010-06-23T16:12:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9317",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9317#issuecomment-87667",
    "user": "https://github.com/adeines"
}
```

Attachment [trac_9317_doctest_change.patch](tarball://root/attachments/some-uuid/ticket9317/trac_9317_doctest_change.patch) by @adeines created at 2010-06-23 16:12:35



---

archive/issue_comments_087668.json:
```json
{
    "body": "I found and fixed error in the doctest.",
    "created_at": "2010-06-23T16:13:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9317",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9317#issuecomment-87668",
    "user": "https://github.com/adeines"
}
```

I found and fixed error in the doctest.



---

archive/issue_events_022961.json:
```json
{
    "actor": "https://github.com/annahaensch",
    "created_at": "2010-06-24T23:09:06Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9317",
    "milestone": "sage-4.5",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9317#event-22961"
}
```



---

archive/issue_comments_087669.json:
```json
{
    "body": "We applied the patch, ran the doctests, and everything looks good to us!",
    "created_at": "2010-06-24T23:09:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9317",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9317#issuecomment-87669",
    "user": "https://github.com/annahaensch"
}
```

We applied the patch, ran the doctests, and everything looks good to us!



---

archive/issue_comments_087670.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-24T23:09:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9317",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9317#issuecomment-87670",
    "user": "https://github.com/annahaensch"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_087671.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-20T07:53:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9317",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9317#issuecomment-87671",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed



---

archive/issue_events_022962.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-07-20T07:53:32Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9317",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9317#event-22962"
}
```
