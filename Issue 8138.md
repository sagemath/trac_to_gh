# Issue 8138: Single-column index in PDF documentation

archive/issues_008138.json:
```json
{
    "body": "Assignee: mvngu\n\nCC:  jhpalmieri\n\nSphinx's LaTeX and PDF builders output two-column indexes / indices, but the badness is high.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8138\n\n",
    "created_at": "2010-01-31T09:45:31Z",
    "labels": [
        "documentation",
        "minor",
        "bug"
    ],
    "title": "Single-column index in PDF documentation",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8138",
    "user": "mpatel"
}
```
Assignee: mvngu

CC:  jhpalmieri

Sphinx's LaTeX and PDF builders output two-column indexes / indices, but the badness is high.

Issue created by migration from https://trac.sagemath.org/ticket/8138





---

archive/issue_comments_071558.json:
```json
{
    "body": "One-column indexes for PDF ref. manual.  Depends on #8036's \"utfx8\" patch.",
    "created_at": "2010-01-31T10:03:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8138#issuecomment-71558",
    "user": "mpatel"
}
```

One-column indexes for PDF ref. manual.  Depends on #8036's "utfx8" patch.



---

archive/issue_comments_071559.json:
```json
{
    "body": "Attachment [trac_8138-one_column_index.patch](tarball://root/attachments/some-uuid/ticket8138/trac_8138-one_column_index.patch) by mpatel created at 2010-01-31 10:06:50",
    "created_at": "2010-01-31T10:06:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8138#issuecomment-71559",
    "user": "mpatel"
}
```

Attachment [trac_8138-one_column_index.patch](tarball://root/attachments/some-uuid/ticket8138/trac_8138-one_column_index.patch) by mpatel created at 2010-01-31 10:06:50



---

archive/issue_comments_071560.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-31T10:06:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8138#issuecomment-71560",
    "user": "mpatel"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_071561.json:
```json
{
    "body": "The patch depends on #8036's \"utf8x\" patch, but rebasing should be easy.",
    "created_at": "2010-01-31T10:07:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8138#issuecomment-71561",
    "user": "mpatel"
}
```

The patch depends on #8036's "utf8x" patch, but rebasing should be easy.



---

archive/issue_comments_071562.json:
```json
{
    "body": "The patch is adapted from [these examples](http://www.latex-community.org/forum/viewtopic.php?f=4&t=1735).",
    "created_at": "2010-01-31T10:08:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8138#issuecomment-71562",
    "user": "mpatel"
}
```

The patch is adapted from [these examples](http://www.latex-community.org/forum/viewtopic.php?f=4&t=1735).



---

archive/issue_comments_071563.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-31T16:59:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8138#issuecomment-71563",
    "user": "jhpalmieri"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_071564.json:
```json
{
    "body": "Wow, the index looks *terrible* before applying this patch, much better afterwards.  This adds 51 pages to the reference manual, but that's just a little over 1% of its total length, so I'm not concerned by that. \n\nOne small error: you need an \"r\" before the triple quotes; otherwise the latex file says \"enewenvironment\" instead of \"\\renewenvironment\".  I added it to the patch.",
    "created_at": "2010-01-31T16:59:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8138#issuecomment-71564",
    "user": "jhpalmieri"
}
```

Wow, the index looks *terrible* before applying this patch, much better afterwards.  This adds 51 pages to the reference manual, but that's just a little over 1% of its total length, so I'm not concerned by that. 

One small error: you need an "r" before the triple quotes; otherwise the latex file says "enewenvironment" instead of "\renewenvironment".  I added it to the patch.



---

archive/issue_comments_071565.json:
```json
{
    "body": "Attachment [trac_8138-one_column_index-v2.patch](tarball://root/attachments/some-uuid/ticket8138/trac_8138-one_column_index-v2.patch) by jhpalmieri created at 2010-01-31 16:59:47\n\napply instead of other patch",
    "created_at": "2010-01-31T16:59:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8138#issuecomment-71565",
    "user": "jhpalmieri"
}
```

Attachment [trac_8138-one_column_index-v2.patch](tarball://root/attachments/some-uuid/ticket8138/trac_8138-one_column_index-v2.patch) by jhpalmieri created at 2010-01-31 16:59:47

apply instead of other patch



---

archive/issue_comments_071566.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-02-11T14:53:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8138#issuecomment-71566",
    "user": "mpatel"
}
```

Resolution: fixed
