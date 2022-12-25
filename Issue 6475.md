# Issue 6475: Notebook error page after deleting data file

archive/issues_006475.json:
```json
{
    "body": "Assignee: wstein\n\nCC:  @williamstein acleone @qed777\n\nKeywords: notebook delete file error\n\nIf I delete a data file using the notebook (Data... pop up menu -> file name -> delete file name link), the file is deleted, but the browser then goes to a blank page titled \"Error | Sage Notebook\". The browser is Safari 4 on OS X 10.5, in case that makes a difference.\n\nWilliam Stein reported on Sage-Support:\n\nI've seen this.  This definitely didn't used to happen.  Somebody introduced this bug a few months ago.  Please report it to trac.  I'll fix it in September/October when I work on the notebook, if nobody beats me to it.\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6475\n\n",
    "created_at": "2009-07-07T18:22:15Z",
    "labels": [
        "component: notebook",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.2",
    "title": "Notebook error page after deleting data file",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6475",
    "user": "https://trac.sagemath.org/admin/accounts/users/khorton"
}
```
Assignee: wstein

CC:  @williamstein acleone @qed777

Keywords: notebook delete file error

If I delete a data file using the notebook (Data... pop up menu -> file name -> delete file name link), the file is deleted, but the browser then goes to a blank page titled "Error | Sage Notebook". The browser is Safari 4 on OS X 10.5, in case that makes a difference.

William Stein reported on Sage-Support:

I've seen this.  This definitely didn't used to happen.  Somebody introduced this bug a few months ago.  Please report it to trac.  I'll fix it in September/October when I work on the notebook, if nobody beats me to it.



Issue created by migration from https://trac.sagemath.org/ticket/6475





---

archive/issue_comments_052239.json:
```json
{
    "body": "Is this still a problem, in 4.3.rc0?",
    "created_at": "2009-12-14T17:35:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6475",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6475#issuecomment-52239",
    "user": "https://github.com/qed777"
}
```

Is this still a problem, in 4.3.rc0?



---

archive/issue_comments_052240.json:
```json
{
    "body": "Changes the title of the successful delete page",
    "created_at": "2010-01-19T10:54:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6475",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6475#issuecomment-52240",
    "user": "https://github.com/TimDumol"
}
```

Changes the title of the successful delete page



---

archive/issue_comments_052241.json:
```json
{
    "body": "Attachment [trac_6475-error-delete-data-file.patch](tarball://root/attachments/some-uuid/ticket6475/trac_6475-error-delete-data-file.patch) by @TimDumol created at 2010-01-19 10:54:49",
    "created_at": "2010-01-19T10:54:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6475",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6475#issuecomment-52241",
    "user": "https://github.com/TimDumol"
}
```

Attachment [trac_6475-error-delete-data-file.patch](tarball://root/attachments/some-uuid/ticket6475/trac_6475-error-delete-data-file.patch) by @TimDumol created at 2010-01-19 10:54:49



---

archive/issue_comments_052242.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-19T10:54:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6475",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6475#issuecomment-52242",
    "user": "https://github.com/TimDumol"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_052243.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-19T12:56:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6475",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6475#issuecomment-52243",
    "user": "https://trac.sagemath.org/admin/accounts/users/acleone"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_052244.json:
```json
{
    "body": "LGTM.",
    "created_at": "2010-01-19T12:56:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6475",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6475#issuecomment-52244",
    "user": "https://trac.sagemath.org/admin/accounts/users/acleone"
}
```

LGTM.



---

archive/issue_comments_052245.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-25T01:02:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6475",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6475#issuecomment-52245",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed



---

archive/issue_events_006712.json:
```json
{
    "actor": "@qed777",
    "created_at": "2010-01-25T01:02:39Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6475",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6475#event-6712"
}
```
