# Issue 7435: notebook: help screen talks about DIR variable, which was removed from the notebook a while ago

archive/issues_007435.json:
```json
{
    "body": "Assignee: boothby\n\nCC:  acleone mpatel\n\nSo... delete the section about the DIR variable, or make sure it is defined as explained in the help screen.  What do people prefer?\n\nIssue created by migration from https://trac.sagemath.org/ticket/7435\n\n",
    "created_at": "2009-11-11T22:30:19Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "title": "notebook: help screen talks about DIR variable, which was removed from the notebook a while ago",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7435",
    "user": "was"
}
```
Assignee: boothby

CC:  acleone mpatel

So... delete the section about the DIR variable, or make sure it is defined as explained in the help screen.  What do people prefer?

Issue created by migration from https://trac.sagemath.org/ticket/7435





---

archive/issue_comments_062560.json:
```json
{
    "body": "Adds the DIR variable",
    "created_at": "2010-01-19T09:46:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7435",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7435#issuecomment-62560",
    "user": "timdumol"
}
```

Adds the DIR variable



---

archive/issue_comments_062561.json:
```json
{
    "body": "Attachment [trac_7435-dir-var.patch](tarball://root/attachments/some-uuid/ticket7435/trac_7435-dir-var.patch) by timdumol created at 2010-01-19 09:47:17\n\nThis patch adds the DIR variable.",
    "created_at": "2010-01-19T09:47:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7435",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7435#issuecomment-62561",
    "user": "timdumol"
}
```

Attachment [trac_7435-dir-var.patch](tarball://root/attachments/some-uuid/ticket7435/trac_7435-dir-var.patch) by timdumol created at 2010-01-19 09:47:17

This patch adds the DIR variable.



---

archive/issue_comments_062562.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-19T09:47:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7435",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7435#issuecomment-62562",
    "user": "timdumol"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_062563.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-19T12:48:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7435",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7435#issuecomment-62563",
    "user": "acleone"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_062564.json:
```json
{
    "body": "LGTM.",
    "created_at": "2010-01-19T12:48:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7435",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7435#issuecomment-62564",
    "user": "acleone"
}
```

LGTM.



---

archive/issue_comments_062565.json:
```json
{
    "body": "Attachment [trac_7435-dir-var.2.patch](tarball://root/attachments/some-uuid/ticket7435/trac_7435-dir-var.2.patch) by mpatel created at 2010-01-25 01:08:26\n\nRebased for SageNB 0.6 + queue in comment.  Replaces previous.",
    "created_at": "2010-01-25T01:08:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7435",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7435#issuecomment-62565",
    "user": "mpatel"
}
```

Attachment [trac_7435-dir-var.2.patch](tarball://root/attachments/some-uuid/ticket7435/trac_7435-dir-var.2.patch) by mpatel created at 2010-01-25 01:08:26

Rebased for SageNB 0.6 + queue in comment.  Replaces previous.



---

archive/issue_comments_062566.json:
```json
{
    "body": "V2 is rebased for this queue:\n\n```\nsagenb-0.6\ntrac_7249-jinja2_v9.5.patch\ntrac_7962-link-worksheets-zip-file.patch\ntrac_7969-escaped-backslash.patch\ntrac_4217-html-system-formatting.3.patch\ntrac_3083-print-documentation.5.patch\ntrac_6182-double-quotes-ws.2.patch\ntrac_5263-publish-url.patch\ntrac_7631-republish-name.patch\ntrac_6353-cookies-diff-ports.patch\ntrac_7207-sagenb-future-import.3.patch\ntrac_8000-utf-8-coding-directive.2.patch\ntrac_4450-cursor-wrap-last-cell.patch\ntrac_7848-misleading_HTML_cells.patch\ntrac_7963-download-multiple-worksheets.patch\ntrac_7752-delete-worksheet-quit.patch\ntrac_7996-invisible_text.patch\ntrac_6475-error-delete-data-file.patch\ntrac_5675-address-launch.patch\ntrac_7435-dir-var.patch\n```\n",
    "created_at": "2010-01-25T01:09:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7435",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7435#issuecomment-62566",
    "user": "mpatel"
}
```

V2 is rebased for this queue:

```
sagenb-0.6
trac_7249-jinja2_v9.5.patch
trac_7962-link-worksheets-zip-file.patch
trac_7969-escaped-backslash.patch
trac_4217-html-system-formatting.3.patch
trac_3083-print-documentation.5.patch
trac_6182-double-quotes-ws.2.patch
trac_5263-publish-url.patch
trac_7631-republish-name.patch
trac_6353-cookies-diff-ports.patch
trac_7207-sagenb-future-import.3.patch
trac_8000-utf-8-coding-directive.2.patch
trac_4450-cursor-wrap-last-cell.patch
trac_7848-misleading_HTML_cells.patch
trac_7963-download-multiple-worksheets.patch
trac_7752-delete-worksheet-quit.patch
trac_7996-invisible_text.patch
trac_6475-error-delete-data-file.patch
trac_5675-address-launch.patch
trac_7435-dir-var.patch
```




---

archive/issue_comments_062567.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-25T01:09:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7435",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7435#issuecomment-62567",
    "user": "mpatel"
}
```

Resolution: fixed



---

archive/issue_comments_062568.json:
```json
{
    "body": "Fix failed doctests.  Replaces previous.",
    "created_at": "2010-01-25T03:17:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7435",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7435#issuecomment-62568",
    "user": "mpatel"
}
```

Fix failed doctests.  Replaces previous.



---

archive/issue_comments_062569.json:
```json
{
    "body": "Changing status from closed to needs_work.",
    "created_at": "2010-01-25T03:18:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7435",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7435#issuecomment-62569",
    "user": "mpatel"
}
```

Changing status from closed to needs_work.



---

archive/issue_comments_062570.json:
```json
{
    "body": "Attachment [trac_7435-dir-var.3.patch](tarball://root/attachments/some-uuid/ticket7435/trac_7435-dir-var.3.patch) by mpatel created at 2010-01-25 03:18:50\n\nV3 adds `DIR        = None` near the top of `twist.py`, to fix failed doctests in `cell.py` and `worksheet.py`.",
    "created_at": "2010-01-25T03:18:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7435",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7435#issuecomment-62570",
    "user": "mpatel"
}
```

Attachment [trac_7435-dir-var.3.patch](tarball://root/attachments/some-uuid/ticket7435/trac_7435-dir-var.3.patch) by mpatel created at 2010-01-25 03:18:50

V3 adds `DIR        = None` near the top of `twist.py`, to fix failed doctests in `cell.py` and `worksheet.py`.



---

archive/issue_comments_062571.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-01-25T03:18:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7435",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7435#issuecomment-62571",
    "user": "mpatel"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_062572.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-25T03:22:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7435",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7435#issuecomment-62572",
    "user": "acleone"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_062573.json:
```json
{
    "body": "LGTM.",
    "created_at": "2010-01-25T03:22:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7435",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7435#issuecomment-62573",
    "user": "acleone"
}
```

LGTM.



---

archive/issue_comments_062574.json:
```json
{
    "body": "Merged into sage-4.3.2 (post Minh's sage-4.3.2).",
    "created_at": "2010-02-06T18:17:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7435",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7435#issuecomment-62574",
    "user": "was"
}
```

Merged into sage-4.3.2 (post Minh's sage-4.3.2).
