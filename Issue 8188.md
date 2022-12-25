# Issue 8188: additional functions for linear codes

archive/issues_008188.json:
```json
{
    "body": "Assignee: Kwankyu Lee\n\nA few enhancements of linear codes functionality.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8188\n\n",
    "created_at": "2010-02-05T04:01:13Z",
    "labels": [
        "component: coding theory",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.3",
    "title": "additional functions for linear codes",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8188",
    "user": "https://github.com/kwankyu"
}
```
Assignee: Kwankyu Lee

A few enhancements of linear codes functionality.

Issue created by migration from https://trac.sagemath.org/ticket/8188





---

archive/issue_comments_072047.json:
```json
{
    "body": "Is this ready for review?",
    "created_at": "2010-02-05T04:20:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8188",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8188#issuecomment-72047",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Is this ready for review?



---

archive/issue_comments_072048.json:
```json
{
    "body": "Changing assignee from Kwankyu Lee to @kwankyu.",
    "created_at": "2010-02-05T04:22:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8188",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8188#issuecomment-72048",
    "user": "https://github.com/kwankyu"
}
```

Changing assignee from Kwankyu Lee to @kwankyu.



---

archive/issue_comments_072049.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-05T04:22:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8188",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8188#issuecomment-72049",
    "user": "https://github.com/kwankyu"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_072050.json:
```json
{
    "body": "This looks good. Thank you. I'll test it and give a formal review when I get home.\n\nCan you please add a small patch which adds your name to the AUTHOR section and a brief description of what you added?",
    "created_at": "2010-02-05T12:46:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8188",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8188#issuecomment-72050",
    "user": "https://github.com/wdjoyner"
}
```

This looks good. Thank you. I'll test it and give a formal review when I get home.

Can you please add a small patch which adds your name to the AUTHOR section and a brief description of what you added?



---

archive/issue_comments_072051.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-02-05T18:39:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8188",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8188#issuecomment-72051",
    "user": "https://github.com/wdjoyner"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_072052.json:
```json
{
    "body": "This patch fails to apply to 4.3.2.rc0.\n\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n**********************************************************************\n*                                                                    *\n* Warning: this is a prerelease version, and it may be unstable.     *\n*                                                                    *\n**********************************************************************\nLoading Sage library. Current Mercurial branch is: 8188-coding\nsage: hg_sage.apply(\"/Users/wdj/sagefiles/trac_8188.patch\")\ncd \"/Users/wdj/sagefiles/sage-4.3.2.rc0/devel/sage\" && hg status\ncd \"/Users/wdj/sagefiles/sage-4.3.2.rc0/devel/sage\" && hg status\ncd \"/Users/wdj/sagefiles/sage-4.3.2.rc0/devel/sage\" && hg import   \"/Users/wdj/sagefiles/trac_8188.patch\"\napplying /Users/wdj/sagefiles/trac_8188.patch\npatching file sage/coding/linear_code.py\nHunk #1 FAILED at 1406\nHunk #2 succeeded at 1416 with fuzz 2 (offset -11 lines).\nHunk #3 succeeded at 1468 with fuzz 1 (offset -2 lines).\nHunk #4 succeeded at 1684 with fuzz 1 (offset 4 lines).\n1 out of 4 hunks FAILED -- saving rejects to file sage/coding/linear_code.py.rej\nabort: patch failed to apply\n```\n\n| Sage Version 4.3.2.rc0, Release Date: 2010-02-03                   |\n| Type notebook() for the GUI, and license() for information.        |\nPlease make the following changes\n\n(1) fix the patch so that it applies correctly\n(2) Add you name to AUTHOR\n(3) Add a short definition of systematic and information set to the docstrings.\n\nIf you do all these, and the patch applies and passes sage -testall then I'll give this a positive review.\n\nThanks for working on this!",
    "created_at": "2010-02-05T18:39:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8188",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8188#issuecomment-72052",
    "user": "https://github.com/wdjoyner"
}
```

This patch fails to apply to 4.3.2.rc0.


```
----------------------------------------------------------------------
----------------------------------------------------------------------
**********************************************************************
*                                                                    *
* Warning: this is a prerelease version, and it may be unstable.     *
*                                                                    *
**********************************************************************
Loading Sage library. Current Mercurial branch is: 8188-coding
sage: hg_sage.apply("/Users/wdj/sagefiles/trac_8188.patch")
cd "/Users/wdj/sagefiles/sage-4.3.2.rc0/devel/sage" && hg status
cd "/Users/wdj/sagefiles/sage-4.3.2.rc0/devel/sage" && hg status
cd "/Users/wdj/sagefiles/sage-4.3.2.rc0/devel/sage" && hg import   "/Users/wdj/sagefiles/trac_8188.patch"
applying /Users/wdj/sagefiles/trac_8188.patch
patching file sage/coding/linear_code.py
Hunk #1 FAILED at 1406
Hunk #2 succeeded at 1416 with fuzz 2 (offset -11 lines).
Hunk #3 succeeded at 1468 with fuzz 1 (offset -2 lines).
Hunk #4 succeeded at 1684 with fuzz 1 (offset 4 lines).
1 out of 4 hunks FAILED -- saving rejects to file sage/coding/linear_code.py.rej
abort: patch failed to apply
```

| Sage Version 4.3.2.rc0, Release Date: 2010-02-03                   |
| Type notebook() for the GUI, and license() for information.        |
Please make the following changes

(1) fix the patch so that it applies correctly
(2) Add you name to AUTHOR
(3) Add a short definition of systematic and information set to the docstrings.

If you do all these, and the patch applies and passes sage -testall then I'll give this a positive review.

Thanks for working on this!



---

archive/issue_comments_072053.json:
```json
{
    "body": "The patch applied to 4.3.2 passed doctest.",
    "created_at": "2010-02-08T06:23:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8188",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8188#issuecomment-72053",
    "user": "https://github.com/kwankyu"
}
```

The patch applied to 4.3.2 passed doctest.



---

archive/issue_comments_072054.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-02-08T06:23:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8188",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8188#issuecomment-72054",
    "user": "https://github.com/kwankyu"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_072055.json:
```json
{
    "body": "rebased on Sage 4.3.2; added more docstrings as requested",
    "created_at": "2010-02-08T07:13:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8188",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8188#issuecomment-72055",
    "user": "https://github.com/kwankyu"
}
```

rebased on Sage 4.3.2; added more docstrings as requested



---

archive/issue_comments_072056.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-02-08T13:50:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8188",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8188#issuecomment-72056",
    "user": "https://github.com/wdjoyner"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_072057.json:
```json
{
    "body": "Attachment [trac_8188.patch](tarball://root/attachments/some-uuid/ticket8188/trac_8188.patch) by @wdjoyner created at 2010-02-08 13:50:22\n\nLooks good, applies fine to 4.3.2 and passes sage -testal.\n\nThank you for adding this!\n\nPositive review.",
    "created_at": "2010-02-08T13:50:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8188",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8188#issuecomment-72057",
    "user": "https://github.com/wdjoyner"
}
```

Attachment [trac_8188.patch](tarball://root/attachments/some-uuid/ticket8188/trac_8188.patch) by @wdjoyner created at 2010-02-08 13:50:22

Looks good, applies fine to 4.3.2 and passes sage -testal.

Thank you for adding this!

Positive review.



---

archive/issue_comments_072058.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-02-11T14:53:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8188",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8188#issuecomment-72058",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed



---

archive/issue_events_008391.json:
```json
{
    "actor": "@qed777",
    "created_at": "2010-02-11T14:53:27Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8188",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8188#event-8391"
}
```
