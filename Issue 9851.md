# Issue 9851: Error in edge_cut

archive/issues_009851.json:
```json
{
    "body": "Assignee: jason, ncohen, rlm\n\nThis method contains an error, as reported in \nhttp://groups.google.com/group/sage-support/browse_thread/thread/f747663b0b315105/5c1314c9855e0cfb?show_docid=5c1314c9855e0cfb&pli=1\n\nThis (very) short patch fixes it. I do not even understand why it was not like that fromt he beginning. I'm guessing a copy/paste is responsible `:-D`\n\nTo be applied on top of #9350 which is an important update and may be broken if this patch was to be applied first.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9852\n\n",
    "created_at": "2010-09-03T18:24:28Z",
    "labels": [
        "graph theory",
        "major",
        "enhancement"
    ],
    "title": "Error in edge_cut",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9851",
    "user": "ncohen"
}
```
Assignee: jason, ncohen, rlm

This method contains an error, as reported in 
http://groups.google.com/group/sage-support/browse_thread/thread/f747663b0b315105/5c1314c9855e0cfb?show_docid=5c1314c9855e0cfb&pli=1

This (very) short patch fixes it. I do not even understand why it was not like that fromt he beginning. I'm guessing a copy/paste is responsible `:-D`

To be applied on top of #9350 which is an important update and may be broken if this patch was to be applied first.

Issue created by migration from https://trac.sagemath.org/ticket/9852





---

archive/issue_comments_097234.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-09-03T18:26:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9851",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9851#issuecomment-97234",
    "user": "ncohen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_097235.json:
```json
{
    "body": "Changing priority from major to critical.",
    "created_at": "2010-09-03T18:26:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9851",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9851#issuecomment-97235",
    "user": "ncohen"
}
```

Changing priority from major to critical.



---

archive/issue_comments_097236.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-09-04T03:57:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9851",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9851#issuecomment-97236",
    "user": "dimpase"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_097237.json:
```json
{
    "body": "Attachment [trac_9852.patch](tarball://root/attachments/some-uuid/ticket9852/trac_9852.patch) by dimpase created at 2010-09-04 03:57:46\n\nlooks reasonable.",
    "created_at": "2010-09-04T03:57:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9851",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9851#issuecomment-97237",
    "user": "dimpase"
}
```

Attachment [trac_9852.patch](tarball://root/attachments/some-uuid/ticket9852/trac_9852.patch) by dimpase created at 2010-09-04 03:57:46

looks reasonable.



---

archive/issue_comments_097238.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-09-15T22:52:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9851",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9851#issuecomment-97238",
    "user": "mpatel"
}
```

Resolution: fixed
