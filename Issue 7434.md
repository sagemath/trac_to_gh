# Issue 7434: notebook: new modal jquery dialog boxes are covered by jmol 3d graphics

archive/issues_007434.json:
```json
{
    "body": "Assignee: boothby\n\nTrac #7310 introduced nice modal jquery dialog boxes.  Unfortunately, they do not play well at all with the output of jmol 3d graphics (java).  See this screenshot:\n\nIssue created by migration from https://trac.sagemath.org/ticket/7434\n\n",
    "created_at": "2009-11-11T22:20:44Z",
    "labels": [
        "component: notebook",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.2",
    "title": "notebook: new modal jquery dialog boxes are covered by jmol 3d graphics",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7434",
    "user": "https://github.com/williamstein"
}
```
Assignee: boothby

Trac #7310 introduced nice modal jquery dialog boxes.  Unfortunately, they do not play well at all with the output of jmol 3d graphics (java).  See this screenshot:

Issue created by migration from https://trac.sagemath.org/ticket/7434





---

archive/issue_comments_062430.json:
```json
{
    "body": "[This](http://stackoverflow.com/questions/638886/java-applet-z-index-problem-safari-and-beyond) appears to be relevant.",
    "created_at": "2009-11-12T02:57:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7434",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7434#issuecomment-62430",
    "user": "https://github.com/qed777"
}
```

[This](http://stackoverflow.com/questions/638886/java-applet-z-index-problem-safari-and-beyond) appears to be relevant.



---

archive/issue_comments_062431.json:
```json
{
    "body": "Attachment [trac_7434-jmol_modal_dialogs_test.patch](tarball://root/attachments/some-uuid/ticket7434/trac_7434-jmol_modal_dialogs_test.patch) by acleone created at 2010-01-19 05:51:24",
    "created_at": "2010-01-19T05:51:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7434",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7434#issuecomment-62431",
    "user": "https://trac.sagemath.org/admin/accounts/users/acleone"
}
```

Attachment [trac_7434-jmol_modal_dialogs_test.patch](tarball://root/attachments/some-uuid/ticket7434/trac_7434-jmol_modal_dialogs_test.patch) by acleone created at 2010-01-19 05:51:24



---

archive/issue_comments_062432.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-19T05:52:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7434",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7434#issuecomment-62432",
    "user": "https://trac.sagemath.org/admin/accounts/users/acleone"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_062433.json:
```json
{
    "body": "trac_7434-jmol_modal_dialogs.patch: This patch hides all java applets on the page and puts grey boxes in their place when any modal prompts show up (in notebook_lib.js: function modal_prompt(...)).\n\ntrac_7434-jmol_modal_dialogs_test.patch: This patch adds a selenium test for the above patch.",
    "created_at": "2010-01-19T05:52:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7434",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7434#issuecomment-62433",
    "user": "https://trac.sagemath.org/admin/accounts/users/acleone"
}
```

trac_7434-jmol_modal_dialogs.patch: This patch hides all java applets on the page and puts grey boxes in their place when any modal prompts show up (in notebook_lib.js: function modal_prompt(...)).

trac_7434-jmol_modal_dialogs_test.patch: This patch adds a selenium test for the above patch.



---

archive/issue_comments_062434.json:
```json
{
    "body": "LGTM.",
    "created_at": "2010-01-19T08:27:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7434",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7434#issuecomment-62434",
    "user": "https://github.com/TimDumol"
}
```

LGTM.



---

archive/issue_comments_062435.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-19T08:27:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7434",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7434#issuecomment-62435",
    "user": "https://github.com/TimDumol"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_062436.json:
```json
{
    "body": "Rebased for SageNB 0.6 + queue in comment.  Replaces earlier version.",
    "created_at": "2010-01-25T01:27:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7434",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7434#issuecomment-62436",
    "user": "https://github.com/qed777"
}
```

Rebased for SageNB 0.6 + queue in comment.  Replaces earlier version.



---

archive/issue_comments_062437.json:
```json
{
    "body": "Attachment [trac_7434-jmol_modal_dialogs.2.patch](tarball://root/attachments/some-uuid/ticket7434/trac_7434-jmol_modal_dialogs.2.patch) by @qed777 created at 2010-01-25 02:53:08\n\nPlease ignore V2.  I've just noticed that the patch doesn't work in Cr4, IE8, and S4 on Windows XP.  It seems the WebKit browsers use `applet`s instead of `object`s.  IE8 uses `object`s, but the `type` attribute is empty.\n\nV3 fixes this with [jmolSetAppletCssClass](http://jmol.sourceforge.net/jslibrary/#jmolSetAppletCssClass) and `$('.jmol_applet')`.",
    "created_at": "2010-01-25T02:53:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7434",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7434#issuecomment-62437",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_7434-jmol_modal_dialogs.2.patch](tarball://root/attachments/some-uuid/ticket7434/trac_7434-jmol_modal_dialogs.2.patch) by @qed777 created at 2010-01-25 02:53:08

Please ignore V2.  I've just noticed that the patch doesn't work in Cr4, IE8, and S4 on Windows XP.  It seems the WebKit browsers use `applet`s instead of `object`s.  IE8 uses `object`s, but the `type` attribute is empty.

V3 fixes this with [jmolSetAppletCssClass](http://jmol.sourceforge.net/jslibrary/#jmolSetAppletCssClass) and `$('.jmol_applet')`.



---

archive/issue_comments_062438.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-01-25T02:53:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7434",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7434#issuecomment-62438",
    "user": "https://github.com/qed777"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_062439.json:
```json
{
    "body": "V3 is also rebased for\n\n```\nsagenb-0.6\ntrac_7249-jinja2_v9.5.patch\ntrac_7962-link-worksheets-zip-file.patch\ntrac_7969-escaped-backslash.patch\ntrac_4217-html-system-formatting.3.patch\ntrac_3083-print-documentation.5.patch\ntrac_6182-double-quotes-ws.2.patch\ntrac_5263-publish-url.patch\ntrac_7631-republish-name.patch\ntrac_6353-cookies-diff-ports.patch\ntrac_7207-sagenb-future-import.3.patch\ntrac_8000-utf-8-coding-directive.2.patch\ntrac_4450-cursor-wrap-last-cell.patch\ntrac_7848-misleading_HTML_cells.patch\ntrac_7963-download-multiple-worksheets.patch\ntrac_7752-delete-worksheet-quit.patch\ntrac_7996-invisible_text.patch\ntrac_6475-error-delete-data-file.patch\ntrac_5675-address-launch.patch\ntrac_7435-dir-var.patch\ntrac_3844-DATA_in_sys_path.2.patch\ntrac_6368-shift_tab_unindents.patch\ntrac_7434-jmol_modal_dialogs_test.patch\ntrac_7434-jmol_modal_dialogs.patch\n```\n",
    "created_at": "2010-01-25T02:55:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7434",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7434#issuecomment-62439",
    "user": "https://github.com/qed777"
}
```

V3 is also rebased for

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
trac_3844-DATA_in_sys_path.2.patch
trac_6368-shift_tab_unindents.patch
trac_7434-jmol_modal_dialogs_test.patch
trac_7434-jmol_modal_dialogs.patch
```




---

archive/issue_comments_062440.json:
```json
{
    "body": "Attachment [trac_7434-jmol_modal_dialogs.3.patch](tarball://root/attachments/some-uuid/ticket7434/trac_7434-jmol_modal_dialogs.3.patch) by @qed777 created at 2010-01-25 02:56:05\n\nFix WebKit, IE8 hiding. Rebase vs. queue in comment.  Replaces previous.",
    "created_at": "2010-01-25T02:56:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7434",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7434#issuecomment-62440",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_7434-jmol_modal_dialogs.3.patch](tarball://root/attachments/some-uuid/ticket7434/trac_7434-jmol_modal_dialogs.3.patch) by @qed777 created at 2010-01-25 02:56:05

Fix WebKit, IE8 hiding. Rebase vs. queue in comment.  Replaces previous.



---

archive/issue_comments_062441.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-01-25T02:56:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7434",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7434#issuecomment-62441",
    "user": "https://github.com/qed777"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_062442.json:
```json
{
    "body": "LGTM",
    "created_at": "2010-01-25T03:09:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7434",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7434#issuecomment-62442",
    "user": "https://trac.sagemath.org/admin/accounts/users/acleone"
}
```

LGTM



---

archive/issue_comments_062443.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-25T03:09:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7434",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7434#issuecomment-62443",
    "user": "https://trac.sagemath.org/admin/accounts/users/acleone"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_062444.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-25T03:09:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7434",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7434#issuecomment-62444",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed



---

archive/issue_events_007657.json:
```json
{
    "actor": "@qed777",
    "created_at": "2010-01-25T03:09:43Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7434",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7434#event-7657"
}
```
