# Issue 8184: eclib upgrade and bugfix

archive/issues_008184.json:
```json
{
    "body": "Assignee: @JohnCremona\n\nKeywords: eclib\n\nWe provide an upgrade to eclib to patch-level 9, i.e. eclib-20080310.p9.spkg.  This does two things:\n\n1. Fixes a bug (found by Edray Goins and Jamie Wiegandt) in which second descent quartics were not tested for real-solubility, and so sometimes the rank bounds (and related selmer ranks) could be too high.\n\n2. Enhances the data available from the two_descent class so that the rank_bound and selmer_rank are separated, and both available.\n\nThe second item necessitated changes to the interface, which are here included in the patch.  In turn, some changes were needed in sage/schemes/elliptic_curve/\n\nNote that this affects #7575.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8184\n\n",
    "created_at": "2010-02-04T14:27:17Z",
    "labels": [
        "component: elliptic curves",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.3",
    "title": "eclib upgrade and bugfix",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8184",
    "user": "https://github.com/JohnCremona"
}
```
Assignee: @JohnCremona

Keywords: eclib

We provide an upgrade to eclib to patch-level 9, i.e. eclib-20080310.p9.spkg.  This does two things:

1. Fixes a bug (found by Edray Goins and Jamie Wiegandt) in which second descent quartics were not tested for real-solubility, and so sometimes the rank bounds (and related selmer ranks) could be too high.

2. Enhances the data available from the two_descent class so that the rank_bound and selmer_rank are separated, and both available.

The second item necessitated changes to the interface, which are here included in the patch.  In turn, some changes were needed in sage/schemes/elliptic_curve/

Note that this affects #7575.

Issue created by migration from https://trac.sagemath.org/ticket/8184





---

archive/issue_comments_072004.json:
```json
{
    "body": "Attachment [eclib-20080310.p9.spkg](tarball://root/attachments/some-uuid/ticket8184/eclib-20080310.p9.spkg) by @JohnCremona created at 2010-02-04 14:28:18",
    "created_at": "2010-02-04T14:28:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8184",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8184#issuecomment-72004",
    "user": "https://github.com/JohnCremona"
}
```

Attachment [eclib-20080310.p9.spkg](tarball://root/attachments/some-uuid/ticket8184/eclib-20080310.p9.spkg) by @JohnCremona created at 2010-02-04 14:28:18



---

archive/issue_comments_072005.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-04T14:31:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8184",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8184#issuecomment-72005",
    "user": "https://github.com/JohnCremona"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_072006.json:
```json
{
    "body": "I fear you uploaded the wrong patch.\n\nI am not certain how to review packages and I will read up on it; but someone might be faster at it.\n\nChris.",
    "created_at": "2010-02-04T15:43:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8184",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8184#issuecomment-72006",
    "user": "https://github.com/categorie"
}
```

I fear you uploaded the wrong patch.

I am not certain how to review packages and I will read up on it; but someone might be faster at it.

Chris.



---

archive/issue_comments_072007.json:
```json
{
    "body": "Applies to 4.3.2.alpha1",
    "created_at": "2010-02-04T15:56:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8184",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8184#issuecomment-72007",
    "user": "https://github.com/JohnCremona"
}
```

Applies to 4.3.2.alpha1



---

archive/issue_comments_072008.json:
```json
{
    "body": "Attachment [trac_8184-eclib.patch](tarball://root/attachments/some-uuid/ticket8184/trac_8184-eclib.patch) by @JohnCremona created at 2010-02-04 15:59:20\n\nSorry -- try this one.\n\nNB After building the new spkg with \"sage -f\" the patch is required before Sage will work properly.  Even in a clone, you'll be stuck with the new spkg.  I am not sure how to revert back to the old eclib (if you want to).\n\nSo I would recommend tetsing this on (say) 4.3.2.alpha1 if you have it, and if all goes wrong you can build 4.3.2.rc0 which is out!",
    "created_at": "2010-02-04T15:59:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8184",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8184#issuecomment-72008",
    "user": "https://github.com/JohnCremona"
}
```

Attachment [trac_8184-eclib.patch](tarball://root/attachments/some-uuid/ticket8184/trac_8184-eclib.patch) by @JohnCremona created at 2010-02-04 15:59:20

Sorry -- try this one.

NB After building the new spkg with "sage -f" the patch is required before Sage will work properly.  Even in a clone, you'll be stuck with the new spkg.  I am not sure how to revert back to the old eclib (if you want to).

So I would recommend tetsing this on (say) 4.3.2.alpha1 if you have it, and if all goes wrong you can build 4.3.2.rc0 which is out!



---

archive/issue_comments_072009.json:
```json
{
    "body": "Apply on top of trac_8184-eclib.patch",
    "created_at": "2010-02-04T19:08:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8184",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8184#issuecomment-72009",
    "user": "https://github.com/rlmill"
}
```

Apply on top of trac_8184-eclib.patch



---

archive/issue_comments_072010.json:
```json
{
    "body": "Attachment [trac_8184-indentation.patch](tarball://root/attachments/some-uuid/ticket8184/trac_8184-indentation.patch) by @rlmill created at 2010-02-04 19:09:33\n\nI added a patch which replaces tabs with single spaces (it looks like your editor sees tabs as eight spaces... mine only sees them as four).",
    "created_at": "2010-02-04T19:09:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8184",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8184#issuecomment-72010",
    "user": "https://github.com/rlmill"
}
```

Attachment [trac_8184-indentation.patch](tarball://root/attachments/some-uuid/ticket8184/trac_8184-indentation.patch) by @rlmill created at 2010-02-04 19:09:33

I added a patch which replaces tabs with single spaces (it looks like your editor sees tabs as eight spaces... mine only sees them as four).



---

archive/issue_comments_072011.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-02-04T20:04:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8184",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8184#issuecomment-72011",
    "user": "https://github.com/rlmill"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_072012.json:
```json
{
    "body": "I've tested this on 32-bit OS X and 64-bit Linux, and there are no problems. Looks great!",
    "created_at": "2010-02-04T20:04:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8184",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8184#issuecomment-72012",
    "user": "https://github.com/rlmill"
}
```

I've tested this on 32-bit OS X and 64-bit Linux, and there are no problems. Looks great!



---

archive/issue_comments_072013.json:
```json
{
    "body": "I knew someone would be faster. Thanks.",
    "created_at": "2010-02-05T10:07:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8184",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8184#issuecomment-72013",
    "user": "https://github.com/categorie"
}
```

I knew someone would be faster. Thanks.



---

archive/issue_comments_072014.json:
```json
{
    "body": "The indentation patch seems to be missing the committer's name and email address, and the commit string does not contain the ticket number.  I've refreshed the patch and applied it to 4.3.3.alpha0.",
    "created_at": "2010-02-10T11:24:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8184",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8184#issuecomment-72014",
    "user": "https://github.com/qed777"
}
```

The indentation patch seems to be missing the committer's name and email address, and the commit string does not contain the ticket number.  I've refreshed the patch and applied it to 4.3.3.alpha0.



---

archive/issue_comments_072015.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-02-11T14:30:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8184",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8184#issuecomment-72015",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed



---

archive/issue_events_008387.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-02-11T14:30:31Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8184",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8184#event-8387"
}
```
