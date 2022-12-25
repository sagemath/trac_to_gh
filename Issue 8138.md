# Issue 8138: Single-column index in PDF documentation

archive/issues_008138.json:
```json
{
    "body": "Assignee: mvngu\n\nCC:  @jhpalmieri\n\nSphinx's LaTeX and PDF builders output two-column indexes / indices, but the badness is high.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8138\n\n",
    "created_at": "2010-01-31T09:45:31Z",
    "labels": [
        "component: documentation",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.3",
    "title": "Single-column index in PDF documentation",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8138",
    "user": "https://github.com/qed777"
}
```
Assignee: mvngu

CC:  @jhpalmieri

Sphinx's LaTeX and PDF builders output two-column indexes / indices, but the badness is high.

Issue created by migration from https://trac.sagemath.org/ticket/8138





---

archive/issue_comments_071437.json:
```json
{
    "body": "One-column indexes for PDF ref. manual.  Depends on #8036's \"utfx8\" patch.",
    "created_at": "2010-01-31T10:03:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8138#issuecomment-71437",
    "user": "https://github.com/qed777"
}
```

One-column indexes for PDF ref. manual.  Depends on #8036's "utfx8" patch.



---

archive/issue_comments_071438.json:
```json
{
    "body": "Attachment [trac_8138-one_column_index.patch](tarball://root/attachments/some-uuid/ticket8138/trac_8138-one_column_index.patch) by @qed777 created at 2010-01-31 10:06:50",
    "created_at": "2010-01-31T10:06:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8138#issuecomment-71438",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_8138-one_column_index.patch](tarball://root/attachments/some-uuid/ticket8138/trac_8138-one_column_index.patch) by @qed777 created at 2010-01-31 10:06:50



---

archive/issue_comments_071439.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-31T10:06:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8138#issuecomment-71439",
    "user": "https://github.com/qed777"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_071440.json:
```json
{
    "body": "The patch depends on #8036's \"utf8x\" patch, but rebasing should be easy.",
    "created_at": "2010-01-31T10:07:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8138#issuecomment-71440",
    "user": "https://github.com/qed777"
}
```

The patch depends on #8036's "utf8x" patch, but rebasing should be easy.



---

archive/issue_comments_071441.json:
```json
{
    "body": "The patch is adapted from [these examples](http://www.latex-community.org/forum/viewtopic.php?f=4&t=1735).",
    "created_at": "2010-01-31T10:08:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8138#issuecomment-71441",
    "user": "https://github.com/qed777"
}
```

The patch is adapted from [these examples](http://www.latex-community.org/forum/viewtopic.php?f=4&t=1735).



---

archive/issue_comments_071442.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-31T16:59:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8138#issuecomment-71442",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_071443.json:
```json
{
    "body": "Wow, the index looks *terrible* before applying this patch, much better afterwards.  This adds 51 pages to the reference manual, but that's just a little over 1% of its total length, so I'm not concerned by that. \n\nOne small error: you need an \"r\" before the triple quotes; otherwise the latex file says \"enewenvironment\" instead of \"\\renewenvironment\".  I added it to the patch.",
    "created_at": "2010-01-31T16:59:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8138#issuecomment-71443",
    "user": "https://github.com/jhpalmieri"
}
```

Wow, the index looks *terrible* before applying this patch, much better afterwards.  This adds 51 pages to the reference manual, but that's just a little over 1% of its total length, so I'm not concerned by that. 

One small error: you need an "r" before the triple quotes; otherwise the latex file says "enewenvironment" instead of "\renewenvironment".  I added it to the patch.



---

archive/issue_comments_071444.json:
```json
{
    "body": "Attachment [trac_8138-one_column_index-v2.patch](tarball://root/attachments/some-uuid/ticket8138/trac_8138-one_column_index-v2.patch) by @jhpalmieri created at 2010-01-31 16:59:47\n\napply instead of other patch",
    "created_at": "2010-01-31T16:59:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8138#issuecomment-71444",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [trac_8138-one_column_index-v2.patch](tarball://root/attachments/some-uuid/ticket8138/trac_8138-one_column_index-v2.patch) by @jhpalmieri created at 2010-01-31 16:59:47

apply instead of other patch



---

archive/issue_comments_071445.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-02-11T14:53:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8138#issuecomment-71445",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed



---

archive/issue_events_019476.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-02-11T14:53:37Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8138",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8138#event-19476"
}
```
