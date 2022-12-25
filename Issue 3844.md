# Issue 3844: notebook -- worksheet should call sys.path.append(DATA) when being initalized

archive/issues_003844.json:
```json
{
    "body": "Assignee: boothby\n\nIf we do the above then one can upload/attach a .py file and import it in the worksheet, which is really sweet.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3844\n\n",
    "created_at": "2008-08-14T00:58:34Z",
    "labels": [
        "component: notebook"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.2",
    "title": "notebook -- worksheet should call sys.path.append(DATA) when being initalized",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3844",
    "user": "https://github.com/williamstein"
}
```
Assignee: boothby

If we do the above then one can upload/attach a .py file and import it in the worksheet, which is really sweet.

Issue created by migration from https://trac.sagemath.org/ticket/3844





---

archive/issue_comments_027287.json:
```json
{
    "body": "Attachment [sage-3844.patch](tarball://root/attachments/some-uuid/ticket3844/sage-3844.patch) by @williamstein created at 2008-08-14 03:07:50",
    "created_at": "2008-08-14T03:07:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3844",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3844#issuecomment-27287",
    "user": "https://github.com/williamstein"
}
```

Attachment [sage-3844.patch](tarball://root/attachments/some-uuid/ticket3844/sage-3844.patch) by @williamstein created at 2008-08-14 03:07:50



---

archive/issue_comments_027288.json:
```json
{
    "body": "When I attached hi.py, \"import hi\" didn't work. Also on http://sage.math.washington.edu:8999/home/admin/3/datafile?name=hi.py, there is no mention of this new functionality.",
    "created_at": "2008-08-14T04:43:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3844",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3844#issuecomment-27288",
    "user": "https://trac.sagemath.org/admin/accounts/users/TimothyClemans"
}
```

When I attached hi.py, "import hi" didn't work. Also on http://sage.math.washington.edu:8999/home/admin/3/datafile?name=hi.py, there is no mention of this new functionality.



---

archive/issue_comments_027289.json:
```json
{
    "body": "I've attached a totally new patch that is 1-line, works, and does the right thing, and is imho quite nice.  \n\nI still don't have my computer setup for Selenium, but a test this works is to do this in the notebook:\n\n```\nDATA in sys.path\n///\nTrue\n```",
    "created_at": "2009-11-19T23:50:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3844",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3844#issuecomment-27289",
    "user": "https://github.com/williamstein"
}
```

I've attached a totally new patch that is 1-line, works, and does the right thing, and is imho quite nice.  

I still don't have my computer setup for Selenium, but a test this works is to do this in the notebook:

```
DATA in sys.path
///
True
```



---

archive/issue_comments_027290.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-11-19T23:50:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3844",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3844#issuecomment-27290",
    "user": "https://github.com/williamstein"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_027291.json:
```json
{
    "body": "Attachment [sagenb_3844.patch](tarball://root/attachments/some-uuid/ticket3844/sagenb_3844.patch) by @williamstein created at 2009-11-19 23:51:07\n\napply only this -- ignore the old sage-3844.patch",
    "created_at": "2009-11-19T23:51:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3844",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3844#issuecomment-27291",
    "user": "https://github.com/williamstein"
}
```

Attachment [sagenb_3844.patch](tarball://root/attachments/some-uuid/ticket3844/sagenb_3844.patch) by @williamstein created at 2009-11-19 23:51:07

apply only this -- ignore the old sage-3844.patch



---

archive/issue_comments_027292.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2009-12-06T03:46:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3844",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3844#issuecomment-27292",
    "user": "https://github.com/TimDumol"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_027293.json:
```json
{
    "body": "I've come across the same problem as TimothyClemans -- importing it after attachment does not work. Also, it would probably be best to advertise the functionality on the data page, as TimothyClemans stated.",
    "created_at": "2009-12-06T03:46:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3844",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3844#issuecomment-27293",
    "user": "https://github.com/TimDumol"
}
```

I've come across the same problem as TimothyClemans -- importing it after attachment does not work. Also, it would probably be best to advertise the functionality on the data page, as TimothyClemans stated.



---

archive/issue_comments_027294.json:
```json
{
    "body": "Attachment [trac_3844-DATA_in_sys_path.2.patch](tarball://root/attachments/some-uuid/ticket3844/trac_3844-DATA_in_sys_path.2.patch) by @qed777 created at 2010-01-22 03:57:41\n\nUpdates `tutorial.py`. Replaces previous.",
    "created_at": "2010-01-22T03:57:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3844",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3844#issuecomment-27294",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_3844-DATA_in_sys_path.2.patch](tarball://root/attachments/some-uuid/ticket3844/trac_3844-DATA_in_sys_path.2.patch) by @qed777 created at 2010-01-22 03:57:41

Updates `tutorial.py`. Replaces previous.



---

archive/issue_comments_027295.json:
```json
{
    "body": "This works for me -- After I upload a data file `foo.py` (or create a new one), I can `import foo` in a worksheet cell.\n\nPositive review.  V2 just adds the changes to `tutorial.py` from the original patch.\n\nA `load` / `attach` analogue of `sys.path` might be warmly-received: #378, #1484, #5169.\n\nBy the way, FF 3.6 will permit drag-and-drop file uploads.  See [this blog post](http://hacks.mozilla.org/2009/12/file-drag-and-drop-in-firefox-3-6/) for a video and simple demo.",
    "created_at": "2010-01-22T04:19:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3844",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3844#issuecomment-27295",
    "user": "https://github.com/qed777"
}
```

This works for me -- After I upload a data file `foo.py` (or create a new one), I can `import foo` in a worksheet cell.

Positive review.  V2 just adds the changes to `tutorial.py` from the original patch.

A `load` / `attach` analogue of `sys.path` might be warmly-received: #378, #1484, #5169.

By the way, FF 3.6 will permit drag-and-drop file uploads.  See [this blog post](http://hacks.mozilla.org/2009/12/file-drag-and-drop-in-firefox-3-6/) for a video and simple demo.



---

archive/issue_comments_027296.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-01-22T04:19:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3844",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3844#issuecomment-27296",
    "user": "https://github.com/qed777"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_027297.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-22T04:19:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3844",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3844#issuecomment-27297",
    "user": "https://github.com/qed777"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_027298.json:
```json
{
    "body": "Attachment [trac_3844-DATA_in_sys_path.3.patch](tarball://root/attachments/some-uuid/ticket3844/trac_3844-DATA_in_sys_path.3.patch) by @qed777 created at 2010-01-25 01:14:37\n\nRebased for SageNB 0.6 + queue in comment.  Replaces previous.",
    "created_at": "2010-01-25T01:14:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3844",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3844#issuecomment-27298",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_3844-DATA_in_sys_path.3.patch](tarball://root/attachments/some-uuid/ticket3844/trac_3844-DATA_in_sys_path.3.patch) by @qed777 created at 2010-01-25 01:14:37

Rebased for SageNB 0.6 + queue in comment.  Replaces previous.



---

archive/issue_events_008797.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-01-25T01:14:50Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3844",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3844#event-8797"
}
```



---

archive/issue_comments_027299.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-25T01:14:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3844",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3844#issuecomment-27299",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed



---

archive/issue_comments_027300.json:
```json
{
    "body": "V3 is rebased for this queue:\n\n```\nsagenb-0.6\ntrac_7249-jinja2_v9.5.patch\ntrac_7962-link-worksheets-zip-file.patch\ntrac_7969-escaped-backslash.patch\ntrac_4217-html-system-formatting.3.patch\ntrac_3083-print-documentation.5.patch\ntrac_6182-double-quotes-ws.2.patch\ntrac_5263-publish-url.patch\ntrac_7631-republish-name.patch\ntrac_6353-cookies-diff-ports.patch\ntrac_7207-sagenb-future-import.3.patch\ntrac_8000-utf-8-coding-directive.2.patch\ntrac_4450-cursor-wrap-last-cell.patch\ntrac_7848-misleading_HTML_cells.patch\ntrac_7963-download-multiple-worksheets.patch\ntrac_7752-delete-worksheet-quit.patch\ntrac_7996-invisible_text.patch\ntrac_6475-error-delete-data-file.patch\ntrac_5675-address-launch.patch\ntrac_7435-dir-var.patch\ntrac_3844-DATA_in_sys_path.2.patch\n```\nPatch versions may be off by one.",
    "created_at": "2010-01-25T01:16:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3844",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3844#issuecomment-27300",
    "user": "https://github.com/qed777"
}
```

V3 is rebased for this queue:

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
```
Patch versions may be off by one.
