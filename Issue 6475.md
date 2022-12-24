# Issue 6475: Notebook error page after deleting data file

archive/issues_006475.json:
```json
{
    "body": "Assignee: wstein\n\nCC:  was acleone mpatel\n\nKeywords: notebook delete file error\n\nIf I delete a data file using the notebook (Data... pop up menu -> file name -> delete file name link), the file is deleted, but the browser then goes to a blank page titled \"Error | Sage Notebook\". The browser is Safari 4 on OS X 10.5, in case that makes a difference.\n\nWilliam Stein reported on Sage-Support:\n\nI've seen this.  This definitely didn't used to happen.  Somebody introduced this bug a few months ago.  Please report it to trac.  I'll fix it in September/October when I work on the notebook, if nobody beats me to it.\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6475\n\n",
    "created_at": "2009-07-07T18:22:15Z",
    "labels": [
        "notebook",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.2",
    "title": "Notebook error page after deleting data file",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6475",
    "user": "khorton"
}
```
Assignee: wstein

CC:  was acleone mpatel

Keywords: notebook delete file error

If I delete a data file using the notebook (Data... pop up menu -> file name -> delete file name link), the file is deleted, but the browser then goes to a blank page titled "Error | Sage Notebook". The browser is Safari 4 on OS X 10.5, in case that makes a difference.

William Stein reported on Sage-Support:

I've seen this.  This definitely didn't used to happen.  Somebody introduced this bug a few months ago.  Please report it to trac.  I'll fix it in September/October when I work on the notebook, if nobody beats me to it.



Issue created by migration from https://trac.sagemath.org/ticket/6475





---

archive/issue_comments_052337.json:
```json
{
    "body": "Is this still a problem, in 4.3.rc0?",
    "created_at": "2009-12-14T17:35:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6475",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6475#issuecomment-52337",
    "user": "mpatel"
}
```

Is this still a problem, in 4.3.rc0?



---

archive/issue_comments_052338.json:
```json
{
    "body": "Changes the title of the successful delete page",
    "created_at": "2010-01-19T10:54:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6475",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6475#issuecomment-52338",
    "user": "timdumol"
}
```

Changes the title of the successful delete page



---

archive/issue_comments_052339.json:
```json
{
    "body": "Attachment [trac_6475-error-delete-data-file.patch](tarball://root/attachments/some-uuid/ticket6475/trac_6475-error-delete-data-file.patch) by timdumol created at 2010-01-19 10:54:49",
    "created_at": "2010-01-19T10:54:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6475",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6475#issuecomment-52339",
    "user": "timdumol"
}
```

Attachment [trac_6475-error-delete-data-file.patch](tarball://root/attachments/some-uuid/ticket6475/trac_6475-error-delete-data-file.patch) by timdumol created at 2010-01-19 10:54:49



---

archive/issue_comments_052340.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-19T10:54:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6475",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6475#issuecomment-52340",
    "user": "timdumol"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_052341.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-19T12:56:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6475",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6475#issuecomment-52341",
    "user": "acleone"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_052342.json:
```json
{
    "body": "LGTM.",
    "created_at": "2010-01-19T12:56:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6475",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6475#issuecomment-52342",
    "user": "acleone"
}
```

LGTM.



---

archive/issue_comments_052343.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-25T01:02:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6475",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6475#issuecomment-52343",
    "user": "mpatel"
}
```

Resolution: fixed
