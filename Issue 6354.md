# Issue 6354: [with patch, needs review] Advertise and improve sage -fixdoctest

archive/issues_006354.json:
```json
{
    "body": "Assignee: @nthiery\n\nCC:  sage-combinat @mwhansen @rlmill\n\nKeywords: fix doctests\n\nAfter this patch, sage -fixdoctest handles multiline doctests,\nand use the line number info of sage -t to be more robust (handles\nmultiple doctests with the same expected output in the same file).\n\nBy the way, sage -advanced advertises sage -fixdoctest.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6354\n\n",
    "created_at": "2009-06-18T05:51:15Z",
    "labels": [
        "component: doctest coverage"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3",
    "title": "[with patch, needs review] Advertise and improve sage -fixdoctest",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6354",
    "user": "https://github.com/nthiery"
}
```
Assignee: @nthiery

CC:  sage-combinat @mwhansen @rlmill

Keywords: fix doctests

After this patch, sage -fixdoctest handles multiline doctests,
and use the line number info of sage -t to be more robust (handles
multiple doctests with the same expected output in the same file).

By the way, sage -advanced advertises sage -fixdoctest.

Issue created by migration from https://trac.sagemath.org/ticket/6354





---

archive/issue_comments_050699.json:
```json
{
    "body": "Attachment [sage-fixdoctests-6354-nt.patch](tarball://root/attachments/some-uuid/ticket6354/sage-fixdoctests-6354-nt.patch) by @mwhansen created at 2009-06-18 06:43:42\n\nLooks good to me.",
    "created_at": "2009-06-18T06:43:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6354",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6354#issuecomment-50699",
    "user": "https://github.com/mwhansen"
}
```

Attachment [sage-fixdoctests-6354-nt.patch](tarball://root/attachments/some-uuid/ticket6354/sage-fixdoctests-6354-nt.patch) by @mwhansen created at 2009-06-18 06:43:42

Looks good to me.



---

archive/issue_events_006598.json:
```json
{
    "actor": "https://github.com/rlmill",
    "created_at": "2009-06-24T10:02:15Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6354",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6354#event-6598"
}
```



---

archive/issue_comments_050700.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-24T10:02:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6354",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6354#issuecomment-50700",
    "user": "https://github.com/rlmill"
}
```

Resolution: fixed



---

archive/issue_comments_050701.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2009-11-17T20:25:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6354",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6354#issuecomment-50701",
    "user": "https://github.com/nthiery"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_050702.json:
```json
{
    "body": "Replying to [comment:2 rlm]:\n\nErr, I don't see it in sage-4.2.1; was it somehow lost?",
    "created_at": "2009-11-17T20:25:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6354",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6354#issuecomment-50702",
    "user": "https://github.com/nthiery"
}
```

Replying to [comment:2 rlm]:

Err, I don't see it in sage-4.2.1; was it somehow lost?



---

archive/issue_comments_050703.json:
```json
{
    "body": "Changing status from closed to new.",
    "created_at": "2009-11-17T20:25:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6354",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6354#issuecomment-50703",
    "user": "https://github.com/nthiery"
}
```

Changing status from closed to new.



---

archive/issue_events_006599.json:
```json
{
    "actor": "https://github.com/nthiery",
    "created_at": "2009-11-17T20:25:07Z",
    "event": "reopened",
    "issue": "https://github.com/sagemath/sagetest/issues/6354",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6354#event-6599"
}
```



---

archive/issue_comments_050704.json:
```json
{
    "body": "Sorry, it must have gotten lost during merging....",
    "created_at": "2009-11-17T23:08:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6354",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6354#issuecomment-50704",
    "user": "https://github.com/rlmill"
}
```

Sorry, it must have gotten lost during merging....



---

archive/issue_comments_050705.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-11-17T23:32:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6354",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6354#issuecomment-50705",
    "user": "https://github.com/nthiery"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_050706.json:
```json
{
    "body": "Replying to [comment:4 rlm]:\n> Sorry, it must have gotten lost during merging....\n\nNo worry :-) I set it back to positive review so that it get merged in 4.3.",
    "created_at": "2009-11-17T23:32:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6354",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6354#issuecomment-50706",
    "user": "https://github.com/nthiery"
}
```

Replying to [comment:4 rlm]:
> Sorry, it must have gotten lost during merging....

No worry :-) I set it back to positive review so that it get merged in 4.3.



---

archive/issue_comments_050707.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-11-17T23:32:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6354",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6354#issuecomment-50707",
    "user": "https://github.com/nthiery"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_006600.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-11-19T17:37:58Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6354",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6354#event-6600"
}
```



---

archive/issue_comments_050708.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-11-19T17:37:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6354",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6354#issuecomment-50708",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed
