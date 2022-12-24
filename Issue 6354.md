# Issue 6354: [with patch, needs review] Advertise and improve sage -fixdoctest

archive/issues_006354.json:
```json
{
    "body": "Assignee: nthiery\n\nCC:  sage-combinat mhansen rlm\n\nKeywords: fix doctests\n\nAfter this patch, sage -fixdoctest handles multiline doctests,\nand use the line number info of sage -t to be more robust (handles\nmultiple doctests with the same expected output in the same file).\n\nBy the way, sage -advanced advertises sage -fixdoctest.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6354\n\n",
    "created_at": "2009-06-18T05:51:15Z",
    "labels": [
        "doctest coverage",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3",
    "title": "[with patch, needs review] Advertise and improve sage -fixdoctest",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6354",
    "user": "nthiery"
}
```
Assignee: nthiery

CC:  sage-combinat mhansen rlm

Keywords: fix doctests

After this patch, sage -fixdoctest handles multiline doctests,
and use the line number info of sage -t to be more robust (handles
multiple doctests with the same expected output in the same file).

By the way, sage -advanced advertises sage -fixdoctest.

Issue created by migration from https://trac.sagemath.org/ticket/6354





---

archive/issue_comments_050796.json:
```json
{
    "body": "Attachment [sage-fixdoctests-6354-nt.patch](tarball://root/attachments/some-uuid/ticket6354/sage-fixdoctests-6354-nt.patch) by mhansen created at 2009-06-18 06:43:42\n\nLooks good to me.",
    "created_at": "2009-06-18T06:43:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6354",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6354#issuecomment-50796",
    "user": "mhansen"
}
```

Attachment [sage-fixdoctests-6354-nt.patch](tarball://root/attachments/some-uuid/ticket6354/sage-fixdoctests-6354-nt.patch) by mhansen created at 2009-06-18 06:43:42

Looks good to me.



---

archive/issue_comments_050797.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-24T10:02:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6354",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6354#issuecomment-50797",
    "user": "rlm"
}
```

Resolution: fixed



---

archive/issue_comments_050798.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2009-11-17T20:25:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6354",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6354#issuecomment-50798",
    "user": "nthiery"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_050799.json:
```json
{
    "body": "Replying to [comment:2 rlm]:\n\nErr, I don't see it in sage-4.2.1; was it somehow lost?",
    "created_at": "2009-11-17T20:25:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6354",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6354#issuecomment-50799",
    "user": "nthiery"
}
```

Replying to [comment:2 rlm]:

Err, I don't see it in sage-4.2.1; was it somehow lost?



---

archive/issue_comments_050800.json:
```json
{
    "body": "Changing status from closed to new.",
    "created_at": "2009-11-17T20:25:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6354",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6354#issuecomment-50800",
    "user": "nthiery"
}
```

Changing status from closed to new.



---

archive/issue_comments_050801.json:
```json
{
    "body": "Sorry, it must have gotten lost during merging....",
    "created_at": "2009-11-17T23:08:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6354",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6354#issuecomment-50801",
    "user": "rlm"
}
```

Sorry, it must have gotten lost during merging....



---

archive/issue_comments_050802.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-11-17T23:32:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6354",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6354#issuecomment-50802",
    "user": "nthiery"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_050803.json:
```json
{
    "body": "Replying to [comment:4 rlm]:\n> Sorry, it must have gotten lost during merging....\n\nNo worry :-) I set it back to positive review so that it get merged in 4.3.",
    "created_at": "2009-11-17T23:32:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6354",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6354#issuecomment-50803",
    "user": "nthiery"
}
```

Replying to [comment:4 rlm]:
> Sorry, it must have gotten lost during merging....

No worry :-) I set it back to positive review so that it get merged in 4.3.



---

archive/issue_comments_050804.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-11-17T23:32:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6354",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6354#issuecomment-50804",
    "user": "nthiery"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_050805.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-11-19T17:37:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6354",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6354#issuecomment-50805",
    "user": "mhansen"
}
```

Resolution: fixed
