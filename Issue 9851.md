# Issue 9851: Error in edge_cut

archive/issues_009851.json:
```json
{
    "body": "Assignee: jason, ncohen, rlm\n\nThis method contains an error, as reported in \nhttp://groups.google.com/group/sage-support/browse_thread/thread/f747663b0b315105/5c1314c9855e0cfb?show_docid=5c1314c9855e0cfb&pli=1\n\nThis (very) short patch fixes it. I do not even understand why it was not like that fromt he beginning. I'm guessing a copy/paste is responsible `:-D`\n\nTo be applied on top of #9350 which is an important update and may be broken if this patch was to be applied first.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9852\n\n",
    "created_at": "2010-09-03T18:24:28Z",
    "labels": [
        "component: graph theory"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6",
    "title": "Error in edge_cut",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9851",
    "user": "https://github.com/nathanncohen"
}
```
Assignee: jason, ncohen, rlm

This method contains an error, as reported in 
http://groups.google.com/group/sage-support/browse_thread/thread/f747663b0b315105/5c1314c9855e0cfb?show_docid=5c1314c9855e0cfb&pli=1

This (very) short patch fixes it. I do not even understand why it was not like that fromt he beginning. I'm guessing a copy/paste is responsible `:-D`

To be applied on top of #9350 which is an important update and may be broken if this patch was to be applied first.

Issue created by migration from https://trac.sagemath.org/ticket/9852





---

archive/issue_comments_097075.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-09-03T18:26:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9851",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9851#issuecomment-97075",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_097076.json:
```json
{
    "body": "Changing priority from major to critical.",
    "created_at": "2010-09-03T18:26:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9851",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9851#issuecomment-97076",
    "user": "https://github.com/nathanncohen"
}
```

Changing priority from major to critical.



---

archive/issue_comments_097077.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-09-04T03:57:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9851",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9851#issuecomment-97077",
    "user": "https://github.com/dimpase"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_097078.json:
```json
{
    "body": "Attachment [trac_9852.patch](tarball://root/attachments/some-uuid/ticket9852/trac_9852.patch) by @dimpase created at 2010-09-04 03:57:46\n\nlooks reasonable.",
    "created_at": "2010-09-04T03:57:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9851",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9851#issuecomment-97078",
    "user": "https://github.com/dimpase"
}
```

Attachment [trac_9852.patch](tarball://root/attachments/some-uuid/ticket9852/trac_9852.patch) by @dimpase created at 2010-09-04 03:57:46

looks reasonable.



---

archive/issue_comments_097079.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-09-15T22:52:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9851",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9851#issuecomment-97079",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed



---

archive/issue_events_024797.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-09-15T22:52:22Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9851",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9851#event-24797"
}
```
