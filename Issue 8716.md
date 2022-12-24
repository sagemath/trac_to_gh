# Issue 8716: Modular forms of level GammaH

archive/issues_008716.json:
```json
{
    "body": "Assignee: craigcitro\n\nWe have code for modular symbols on GammaH groups but the code for modular forms is little more than stubs. Here's a patch that should fix that.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8716\n\n",
    "created_at": "2010-04-19T16:53:25Z",
    "labels": [
        "modular forms",
        "major",
        "enhancement"
    ],
    "title": "Modular forms of level GammaH",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8716",
    "user": "davidloeffler"
}
```
Assignee: craigcitro

We have code for modular symbols on GammaH groups but the code for modular forms is little more than stubs. Here's a patch that should fix that.

Issue created by migration from https://trac.sagemath.org/ticket/8716





---

archive/issue_comments_079548.json:
```json
{
    "body": "Attachment [trac_8716-gamma_h_modforms.patch](tarball://root/attachments/some-uuid/ticket8716/trac_8716-gamma_h_modforms.patch) by davidloeffler created at 2010-04-19 16:56:23\n\npatch against 4.4.alpha0",
    "created_at": "2010-04-19T16:56:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8716",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8716#issuecomment-79548",
    "user": "davidloeffler"
}
```

Attachment [trac_8716-gamma_h_modforms.patch](tarball://root/attachments/some-uuid/ticket8716/trac_8716-gamma_h_modforms.patch) by davidloeffler created at 2010-04-19 16:56:23

patch against 4.4.alpha0



---

archive/issue_comments_079549.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-04-19T20:44:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8716",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8716#issuecomment-79549",
    "user": "davidloeffler"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_079550.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-12-06T10:46:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8716",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8716#issuecomment-79550",
    "user": "rlm"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_079551.json:
```json
{
    "body": "This patch applies fine to sage-4.6.1.alpha2 and passes all long doctests. The code looks good as well, and I think this should be merged.",
    "created_at": "2010-12-06T10:46:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8716",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8716#issuecomment-79551",
    "user": "rlm"
}
```

This patch applies fine to sage-4.6.1.alpha2 and passes all long doctests. The code looks good as well, and I think this should be merged.



---

archive/issue_comments_079552.json:
```json
{
    "body": "Tested also against sage-4.6.1.alpha3 on sage.math.washington.edu",
    "created_at": "2010-12-06T13:15:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8716",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8716#issuecomment-79552",
    "user": "jdemeyer"
}
```

Tested also against sage-4.6.1.alpha3 on sage.math.washington.edu



---

archive/issue_comments_079553.json:
```json
{
    "body": "apply over previous patch",
    "created_at": "2010-12-12T14:34:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8716",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8716#issuecomment-79553",
    "user": "davidloeffler"
}
```

apply over previous patch



---

archive/issue_comments_079554.json:
```json
{
    "body": "Attachment [trac_8716-docfix.patch](tarball://root/attachments/some-uuid/ticket8716/trac_8716-docfix.patch) by davidloeffler created at 2010-12-12 14:36:00\n\nOops, my bad: this patch causes an error when building the documentation, due to a silly latex mistake in one of the docstrings. Here's a tiny patch which fixes that. Robert, would you mind taking a quick look to OK it?",
    "created_at": "2010-12-12T14:36:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8716",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8716#issuecomment-79554",
    "user": "davidloeffler"
}
```

Attachment [trac_8716-docfix.patch](tarball://root/attachments/some-uuid/ticket8716/trac_8716-docfix.patch) by davidloeffler created at 2010-12-12 14:36:00

Oops, my bad: this patch causes an error when building the documentation, due to a silly latex mistake in one of the docstrings. Here's a tiny patch which fixes that. Robert, would you mind taking a quick look to OK it?



---

archive/issue_comments_079555.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-12-12T14:36:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8716",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8716#issuecomment-79555",
    "user": "davidloeffler"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_079556.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-12-12T14:36:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8716",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8716#issuecomment-79556",
    "user": "davidloeffler"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_079557.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-12-13T11:28:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8716",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8716#issuecomment-79557",
    "user": "rlm"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_079558.json:
```json
{
    "body": "Oops!",
    "created_at": "2010-12-13T11:28:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8716",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8716#issuecomment-79558",
    "user": "rlm"
}
```

Oops!



---

archive/issue_comments_079559.json:
```json
{
    "body": "\n```\nApply trac_8716-gamma_h_modforms.patch, trac_8716-docfix.patch\n```\n\n\n(FAO PatchBot)",
    "created_at": "2010-12-31T14:29:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8716",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8716#issuecomment-79559",
    "user": "davidloeffler"
}
```


```
Apply trac_8716-gamma_h_modforms.patch, trac_8716-docfix.patch
```


(FAO PatchBot)



---

archive/issue_comments_079560.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-01-25T08:14:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8716",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8716#issuecomment-79560",
    "user": "jdemeyer"
}
```

Resolution: fixed
