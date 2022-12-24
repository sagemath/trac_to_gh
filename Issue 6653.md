# Issue 6653: Add --no-pdf-links option for doc/html/index.html builder.

archive/issues_006653.json:
```json
{
    "body": "Assignee: tba\n\nCC:  schilly\n\nThe top-level `index.html` for Sage documentation now includes links to the corresponding PDF files (cf. #4460).  However, it can be useful to suppress these links.  Building on #6187, this ticket adds an option `--no-pdf-links` to `sage -docbuild`.\n\nSee #4460 for some history and an earlier version.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6653\n\n",
    "created_at": "2009-07-29T08:39:16Z",
    "labels": [
        "documentation",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3",
    "title": "Add --no-pdf-links option for doc/html/index.html builder.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6653",
    "user": "mpatel"
}
```
Assignee: tba

CC:  schilly

The top-level `index.html` for Sage documentation now includes links to the corresponding PDF files (cf. #4460).  However, it can be useful to suppress these links.  Building on #6187, this ticket adds an option `--no-pdf-links` to `sage -docbuild`.

See #4460 for some history and an earlier version.

Issue created by migration from https://trac.sagemath.org/ticket/6653





---

archive/issue_comments_054608.json:
```json
{
    "body": "Depends on #6187.",
    "created_at": "2009-07-29T09:13:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6653",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6653#issuecomment-54608",
    "user": "mpatel"
}
```

Depends on #6187.



---

archive/issue_comments_054609.json:
```json
{
    "body": "Attachment [trac_6653-no_pdf_links.patch](tarball://root/attachments/some-uuid/ticket6653/trac_6653-no_pdf_links.patch) by mpatel created at 2009-08-11 03:15:28",
    "created_at": "2009-08-11T03:15:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6653",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6653#issuecomment-54609",
    "user": "mpatel"
}
```

Attachment [trac_6653-no_pdf_links.patch](tarball://root/attachments/some-uuid/ticket6653/trac_6653-no_pdf_links.patch) by mpatel created at 2009-08-11 03:15:28



---

archive/issue_comments_054610.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-11-19T21:50:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6653",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6653#issuecomment-54610",
    "user": "jhpalmieri"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_054611.json:
```json
{
    "body": "Looks good to me: running \"sage -docbuild website html --no-pdf-links\" turns the links off, and then running \"sage -docbuild website html\" turns them back on again.",
    "created_at": "2009-11-19T21:51:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6653",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6653#issuecomment-54611",
    "user": "jhpalmieri"
}
```

Looks good to me: running "sage -docbuild website html --no-pdf-links" turns the links off, and then running "sage -docbuild website html" turns them back on again.



---

archive/issue_comments_054612.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-11-29T04:45:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6653",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6653#issuecomment-54612",
    "user": "mhansen"
}
```

Resolution: fixed
