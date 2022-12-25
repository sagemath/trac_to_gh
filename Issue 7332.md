# Issue 7332: Escape css id's and classes in templates

archive/issues_007332.json:
```json
{
    "body": "Assignee: boothby\n\nCC:  @williamstein @qed777\n\nCurrently, some css id's and classes have illegal values ('admin/0', for example, in `worksheet_listing.html`). This prevents jQuery and Selenium from accessing those attributes.\n\nThis adds a filter to produce legal values from those values.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7332\n\n",
    "created_at": "2009-10-28T13:50:08Z",
    "labels": [
        "component: notebook",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.2.1",
    "title": "Escape css id's and classes in templates",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7332",
    "user": "https://github.com/TimDumol"
}
```
Assignee: boothby

CC:  @williamstein @qed777

Currently, some css id's and classes have illegal values ('admin/0', for example, in `worksheet_listing.html`). This prevents jQuery and Selenium from accessing those attributes.

This adds a filter to produce legal values from those values.

Issue created by migration from https://trac.sagemath.org/ticket/7332





---

archive/issue_comments_061199.json:
```json
{
    "body": "Attachment [trac_7332-css-escape.patch](tarball://root/attachments/some-uuid/ticket7332/trac_7332-css-escape.patch) by @TimDumol created at 2009-10-28 13:55:47\n\nAdds `css_escape` filter and makes `worksheet_listing.html` use it.",
    "created_at": "2009-10-28T13:55:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7332",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7332#issuecomment-61199",
    "user": "https://github.com/TimDumol"
}
```

Attachment [trac_7332-css-escape.patch](tarball://root/attachments/some-uuid/ticket7332/trac_7332-css-escape.patch) by @TimDumol created at 2009-10-28 13:55:47

Adds `css_escape` filter and makes `worksheet_listing.html` use it.



---

archive/issue_comments_061200.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-10-28T13:56:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7332",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7332#issuecomment-61200",
    "user": "https://github.com/TimDumol"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_061201.json:
```json
{
    "body": "Fixed `notebook_lib.js` so that the checkboxes work after the patch.",
    "created_at": "2009-10-28T14:17:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7332",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7332#issuecomment-61201",
    "user": "https://github.com/TimDumol"
}
```

Fixed `notebook_lib.js` so that the checkboxes work after the patch.



---

archive/issue_comments_061202.json:
```json
{
    "body": "Attachment [trac_7332-css-escape.2.patch](tarball://root/attachments/some-uuid/ticket7332/trac_7332-css-escape.2.patch) by @TimDumol created at 2009-10-29 04:12:52\n\nDeepends on #7310.",
    "created_at": "2009-10-29T04:12:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7332",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7332#issuecomment-61202",
    "user": "https://github.com/TimDumol"
}
```

Attachment [trac_7332-css-escape.2.patch](tarball://root/attachments/some-uuid/ticket7332/trac_7332-css-escape.2.patch) by @TimDumol created at 2009-10-29 04:12:52

Deepends on #7310.



---

archive/issue_comments_061203.json:
```json
{
    "body": "Attachment [trac_7332-css-escape.3.patch](tarball://root/attachments/some-uuid/ticket7332/trac_7332-css-escape.3.patch) by @qed777 created at 2009-10-31 08:38:41\n\nAlso fix the overall checkbox (\"controlbox\"). Apply only this patch.",
    "created_at": "2009-10-31T08:38:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7332",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7332#issuecomment-61203",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_7332-css-escape.3.patch](tarball://root/attachments/some-uuid/ticket7332/trac_7332-css-escape.3.patch) by @qed777 created at 2009-10-31 08:38:41

Also fix the overall checkbox ("controlbox"). Apply only this patch.



---

archive/issue_comments_061204.json:
```json
{
    "body": "Version 3:\n\n* Rebased against #7309, #7310.  For some reason, I got\n\n```\napplying trac_7332-css-escape.2.patch\npatching file sagenb/notebook/template.py\nHunk #1 FAILED at 15\nHunk #3 FAILED at 75\n2 out of 3 hunks FAILED -- saving rejects to file sagenb/notebook/template.py.rej\npatch failed, unable to continue (try -v)\npatch failed, rejects left in working dir\n```\n\n   but the failures were inconsequential.\n\n* Fixes the overall checkbox in `notebook_lib.js`.\n\nTo the extent it counts, my review is positive.",
    "created_at": "2009-10-31T08:43:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7332",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7332#issuecomment-61204",
    "user": "https://github.com/qed777"
}
```

Version 3:

* Rebased against #7309, #7310.  For some reason, I got

```
applying trac_7332-css-escape.2.patch
patching file sagenb/notebook/template.py
Hunk #1 FAILED at 15
Hunk #3 FAILED at 75
2 out of 3 hunks FAILED -- saving rejects to file sagenb/notebook/template.py.rej
patch failed, unable to continue (try -v)
patch failed, rejects left in working dir
```

   but the failures were inconsequential.

* Fixes the overall checkbox in `notebook_lib.js`.

To the extent it counts, my review is positive.



---

archive/issue_comments_061205.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-11-11T19:43:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7332",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7332#issuecomment-61205",
    "user": "https://github.com/williamstein"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_061206.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2009-11-11T19:43:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7332",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7332#issuecomment-61206",
    "user": "https://github.com/williamstein"
}
```

Looks good to me.



---

archive/issue_comments_061207.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-11-11T19:43:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7332",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7332#issuecomment-61207",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_comments_061208.json:
```json
{
    "body": "On [this sage-devel thread](http://groups.google.com/group/sage-devel/browse_thread/thread/9da7dd211fe5570b): I forgot to account for dots (`'.'`) in login names.  A quick fix: In `sagenb/data/sage/js/notebook_lib.js`'s `check_worksheet_filenames`, replace\n\n```\n        id = worksheet_filenames[i].replace('/', '-');\n```\n\nwith\n\n```\n        id = worksheet_filenames[i].replace(/[\\/.]/g, '-');\n```\n\nI'll open a new ticket and add a patch, once I'm confident I haven't missed other special characters.",
    "created_at": "2010-01-01T21:51:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7332",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7332#issuecomment-61208",
    "user": "https://github.com/qed777"
}
```

On [this sage-devel thread](http://groups.google.com/group/sage-devel/browse_thread/thread/9da7dd211fe5570b): I forgot to account for dots (`'.'`) in login names.  A quick fix: In `sagenb/data/sage/js/notebook_lib.js`'s `check_worksheet_filenames`, replace

```
        id = worksheet_filenames[i].replace('/', '-');
```

with

```
        id = worksheet_filenames[i].replace(/[\/.]/g, '-');
```

I'll open a new ticket and add a patch, once I'm confident I haven't missed other special characters.



---

archive/issue_comments_061209.json:
```json
{
    "body": "See #7811.",
    "created_at": "2010-01-01T22:48:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7332",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7332#issuecomment-61209",
    "user": "https://github.com/qed777"
}
```

See #7811.
