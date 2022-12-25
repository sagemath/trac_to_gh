# Issue 8716: Modular forms of level GammaH

archive/issues_008716.json:
```json
{
    "body": "Assignee: @craigcitro\n\nWe have code for modular symbols on GammaH groups but the code for modular forms is little more than stubs. Here's a patch that should fix that.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8716\n\n",
    "created_at": "2010-04-19T16:53:25Z",
    "labels": [
        "component: modular forms"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6.2",
    "title": "Modular forms of level GammaH",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8716",
    "user": "https://github.com/loefflerd"
}
```
Assignee: @craigcitro

We have code for modular symbols on GammaH groups but the code for modular forms is little more than stubs. Here's a patch that should fix that.

Issue created by migration from https://trac.sagemath.org/ticket/8716





---

archive/issue_comments_079418.json:
```json
{
    "body": "Attachment [trac_8716-gamma_h_modforms.patch](tarball://root/attachments/some-uuid/ticket8716/trac_8716-gamma_h_modforms.patch) by @loefflerd created at 2010-04-19 16:56:23\n\npatch against 4.4.alpha0",
    "created_at": "2010-04-19T16:56:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8716",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8716#issuecomment-79418",
    "user": "https://github.com/loefflerd"
}
```

Attachment [trac_8716-gamma_h_modforms.patch](tarball://root/attachments/some-uuid/ticket8716/trac_8716-gamma_h_modforms.patch) by @loefflerd created at 2010-04-19 16:56:23

patch against 4.4.alpha0



---

archive/issue_comments_079419.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-04-19T20:44:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8716",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8716#issuecomment-79419",
    "user": "https://github.com/loefflerd"
}
```

Changing status from new to needs_review.



---

archive/issue_events_021161.json:
```json
{
    "actor": "https://github.com/rlmill",
    "created_at": "2010-12-06T10:46:19Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8716",
    "milestone": "sage-4.6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8716#event-21161"
}
```



---

archive/issue_comments_079420.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-12-06T10:46:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8716",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8716#issuecomment-79420",
    "user": "https://github.com/rlmill"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_079421.json:
```json
{
    "body": "This patch applies fine to sage-4.6.1.alpha2 and passes all long doctests. The code looks good as well, and I think this should be merged.",
    "created_at": "2010-12-06T10:46:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8716",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8716#issuecomment-79421",
    "user": "https://github.com/rlmill"
}
```

This patch applies fine to sage-4.6.1.alpha2 and passes all long doctests. The code looks good as well, and I think this should be merged.



---

archive/issue_comments_079422.json:
```json
{
    "body": "Tested also against sage-4.6.1.alpha3 on sage.math.washington.edu",
    "created_at": "2010-12-06T13:15:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8716",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8716#issuecomment-79422",
    "user": "https://github.com/jdemeyer"
}
```

Tested also against sage-4.6.1.alpha3 on sage.math.washington.edu



---

archive/issue_comments_079423.json:
```json
{
    "body": "apply over previous patch",
    "created_at": "2010-12-12T14:34:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8716",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8716#issuecomment-79423",
    "user": "https://github.com/loefflerd"
}
```

apply over previous patch



---

archive/issue_comments_079424.json:
```json
{
    "body": "Attachment [trac_8716-docfix.patch](tarball://root/attachments/some-uuid/ticket8716/trac_8716-docfix.patch) by @loefflerd created at 2010-12-12 14:36:00\n\nOops, my bad: this patch causes an error when building the documentation, due to a silly latex mistake in one of the docstrings. Here's a tiny patch which fixes that. Robert, would you mind taking a quick look to OK it?",
    "created_at": "2010-12-12T14:36:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8716",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8716#issuecomment-79424",
    "user": "https://github.com/loefflerd"
}
```

Attachment [trac_8716-docfix.patch](tarball://root/attachments/some-uuid/ticket8716/trac_8716-docfix.patch) by @loefflerd created at 2010-12-12 14:36:00

Oops, my bad: this patch causes an error when building the documentation, due to a silly latex mistake in one of the docstrings. Here's a tiny patch which fixes that. Robert, would you mind taking a quick look to OK it?



---

archive/issue_comments_079425.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-12-12T14:36:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8716",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8716#issuecomment-79425",
    "user": "https://github.com/loefflerd"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_079426.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-12-12T14:36:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8716",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8716#issuecomment-79426",
    "user": "https://github.com/loefflerd"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_079427.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-12-13T11:28:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8716",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8716#issuecomment-79427",
    "user": "https://github.com/rlmill"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_079428.json:
```json
{
    "body": "Oops!",
    "created_at": "2010-12-13T11:28:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8716",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8716#issuecomment-79428",
    "user": "https://github.com/rlmill"
}
```

Oops!



---

archive/issue_comments_079429.json:
```json
{
    "body": "\n```\nApply trac_8716-gamma_h_modforms.patch, trac_8716-docfix.patch\n```\n\n\n(FAO PatchBot)",
    "created_at": "2010-12-31T14:29:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8716",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8716#issuecomment-79429",
    "user": "https://github.com/loefflerd"
}
```


```
Apply trac_8716-gamma_h_modforms.patch, trac_8716-docfix.patch
```


(FAO PatchBot)



---

archive/issue_events_021162.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2011-01-25T08:14:18Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8716",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8716#event-21162"
}
```



---

archive/issue_comments_079430.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-01-25T08:14:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8716",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8716#issuecomment-79430",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed
