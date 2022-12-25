# Issue 3083: Print does not include documentation

archive/issues_003083.json:
```json
{
    "body": "Assignee: boothby\n\nCC:  @williamstein\n\nIf I type `sage.graphs.chrompoly??` for example in a cell, and evaluate, I get a nice chunk of code. But when I hit \"print\", all I get is the input. Docs should be included in the printed worksheets.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3083\n\n",
    "created_at": "2008-05-02T19:43:37Z",
    "labels": [
        "component: notebook",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.2",
    "title": "Print does not include documentation",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3083",
    "user": "https://github.com/rlmill"
}
```
Assignee: boothby

CC:  @williamstein

If I type `sage.graphs.chrompoly??` for example in a cell, and evaluate, I get a nice chunk of code. But when I hit "print", all I get is the input. Docs should be included in the printed worksheets.

Issue created by migration from https://trac.sagemath.org/ticket/3083





---

archive/issue_comments_021226.json:
```json
{
    "body": "This bug is caused by the fact that introspection output is not saved with the worksheet. Should this be the case?",
    "created_at": "2010-01-16T21:10:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3083",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3083#issuecomment-21226",
    "user": "https://github.com/TimDumol"
}
```

This bug is caused by the fact that introspection output is not saved with the worksheet. Should this be the case?



---

archive/issue_comments_021227.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-17T08:26:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3083",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3083#issuecomment-21227",
    "user": "https://github.com/TimDumol"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_021228.json:
```json
{
    "body": "This should do the job.",
    "created_at": "2010-01-17T08:26:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3083",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3083#issuecomment-21228",
    "user": "https://github.com/TimDumol"
}
```

This should do the job.



---

archive/issue_comments_021229.json:
```json
{
    "body": "Makes evaluated (S-Enter, eval link, etc.) introspection show up in print while clearly marking that TAB introspected output is unprinted (also makes it draggable).",
    "created_at": "2010-01-17T08:34:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3083",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3083#issuecomment-21229",
    "user": "https://github.com/TimDumol"
}
```

Makes evaluated (S-Enter, eval link, etc.) introspection show up in print while clearly marking that TAB introspected output is unprinted (also makes it draggable).



---

archive/issue_comments_021230.json:
```json
{
    "body": "Attachment [trac_3083-print-documentation.patch](tarball://root/attachments/some-uuid/ticket3083/trac_3083-print-documentation.patch) by @williamstein created at 2010-01-17 08:50:35\n\nBig +1 to this design approach.",
    "created_at": "2010-01-17T08:50:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3083",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3083#issuecomment-21230",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac_3083-print-documentation.patch](tarball://root/attachments/some-uuid/ticket3083/trac_3083-print-documentation.patch) by @williamstein created at 2010-01-17 08:50:35

Big +1 to this design approach.



---

archive/issue_comments_021231.json:
```json
{
    "body": "Rebase on a new patch set.",
    "created_at": "2010-01-17T22:03:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3083",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3083#issuecomment-21231",
    "user": "https://github.com/TimDumol"
}
```

Rebase on a new patch set.



---

archive/issue_comments_021232.json:
```json
{
    "body": "Attachment [trac_3083-print-documentation.2.patch](tarball://root/attachments/some-uuid/ticket3083/trac_3083-print-documentation.2.patch) by @TimDumol created at 2010-01-17 22:04:25\n\nThe new patch set is:\n\n\n```\ntrac_7650-sagenb_doctesting_v6.patch\ntrac_7650-reviewer.patch\ntrac_7648-missing_indent.patch\ntrac_7663-rstrip_prompt.patch\ntrac_7847-empty-trash-no-referer.patch\ntrac_7786-template-jinja-idiomatic.patch\ntrac_7863-declare_vars_aux_js_v2.patch\ntrac_7874-typeset_interact_labels.patch\ntrac_7858-key_binding_vars_v2.patch\ntrac_7666-alphanumeric_cell_ids_B5.patch\ntrac_7666-reviewer.patch\ntrac_7835-preparsing-unicode_v2.patch\ntrac_7249_jinja2_v5.patch\ntrac_2779-sagenb-error-message.patch\n2779_2_banner.patch\ntrac_3154-spurious-u0027-output.patch\ntrac_7969-escaped-backslash.patch\ntrac_7937-sass_manifest.patch\ntrac_4217-html-system-formatting.patch\ntrac_3083-print-documentation.patch\n```\n\n\nSorry for the immense patch queue.",
    "created_at": "2010-01-17T22:04:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3083",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3083#issuecomment-21232",
    "user": "https://github.com/TimDumol"
}
```

Attachment [trac_3083-print-documentation.2.patch](tarball://root/attachments/some-uuid/ticket3083/trac_3083-print-documentation.2.patch) by @TimDumol created at 2010-01-17 22:04:25

The new patch set is:


```
trac_7650-sagenb_doctesting_v6.patch
trac_7650-reviewer.patch
trac_7648-missing_indent.patch
trac_7663-rstrip_prompt.patch
trac_7847-empty-trash-no-referer.patch
trac_7786-template-jinja-idiomatic.patch
trac_7863-declare_vars_aux_js_v2.patch
trac_7874-typeset_interact_labels.patch
trac_7858-key_binding_vars_v2.patch
trac_7666-alphanumeric_cell_ids_B5.patch
trac_7666-reviewer.patch
trac_7835-preparsing-unicode_v2.patch
trac_7249_jinja2_v5.patch
trac_2779-sagenb-error-message.patch
2779_2_banner.patch
trac_3154-spurious-u0027-output.patch
trac_7969-escaped-backslash.patch
trac_7937-sass_manifest.patch
trac_4217-html-system-formatting.patch
trac_3083-print-documentation.patch
```


Sorry for the immense patch queue.



---

archive/issue_comments_021233.json:
```json
{
    "body": "Well done!\n\n* \"Closing\" a dialog does not remove it from the DOM.  It's just hidden.  I suggest mapping the close button to, e.g., `$('.dialog').dialog('destroy').remove();`.\n\n* For `'eval'`-method docstrings, the sans-serif font becomes monospaced.\n\n* I suggest changing \"Click on the box...\" to, e.g., \"Click here...\" and binding the click event to just that `div`.  Otherwise, users who click on the docstring as they read it and/or copy examples might get an unwanted dialog.\n\n* It might be worth it to mention on the \"Help\" page or in the tutorial which docstrings are printable.\n\n* If I evaluate `factor?` in a cell, I can print the docstring with the worksheet, as desired.  People might also find it useful for evaluated docstrings to survive reopening the worksheet or to appear in published worksheets (e.g., as part of an annotated tutorial).  But I suggest waiting for feedback on the mailing lists and, if it's necessary, creating new tickets.",
    "created_at": "2010-01-20T01:41:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3083",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3083#issuecomment-21233",
    "user": "https://github.com/qed777"
}
```

Well done!

* "Closing" a dialog does not remove it from the DOM.  It's just hidden.  I suggest mapping the close button to, e.g., `$('.dialog').dialog('destroy').remove();`.

* For `'eval'`-method docstrings, the sans-serif font becomes monospaced.

* I suggest changing "Click on the box..." to, e.g., "Click here..." and binding the click event to just that `div`.  Otherwise, users who click on the docstring as they read it and/or copy examples might get an unwanted dialog.

* It might be worth it to mention on the "Help" page or in the tutorial which docstrings are printable.

* If I evaluate `factor?` in a cell, I can print the docstring with the worksheet, as desired.  People might also find it useful for evaluated docstrings to survive reopening the worksheet or to appear in published worksheets (e.g., as part of an annotated tutorial).  But I suggest waiting for feedback on the mailing lists and, if it's necessary, creating new tickets.



---

archive/issue_comments_021234.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-01-20T03:35:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3083",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3083#issuecomment-21234",
    "user": "https://github.com/qed777"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_021235.json:
```json
{
    "body": "Has all the requested changes by Patel.",
    "created_at": "2010-01-20T08:34:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3083",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3083#issuecomment-21235",
    "user": "https://github.com/TimDumol"
}
```

Has all the requested changes by Patel.



---

archive/issue_comments_021236.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-01-20T08:36:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3083",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3083#issuecomment-21236",
    "user": "https://github.com/TimDumol"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_021237.json:
```json
{
    "body": "Attachment [trac_3083-print-documentation.3.patch](tarball://root/attachments/some-uuid/ticket3083/trac_3083-print-documentation.3.patch) by @TimDumol created at 2010-01-20 08:36:44\n\nThanks for catching all of that, especially the last point. That was what I intended, and William and others here agreed with it, so it seems to be ok to implement. This patch should implement everything. I have opened a new patch to include sagenb.notebook.tutorial into the ReST documentation too: #8011.",
    "created_at": "2010-01-20T08:36:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3083",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3083#issuecomment-21237",
    "user": "https://github.com/TimDumol"
}
```

Attachment [trac_3083-print-documentation.3.patch](tarball://root/attachments/some-uuid/ticket3083/trac_3083-print-documentation.3.patch) by @TimDumol created at 2010-01-20 08:36:44

Thanks for catching all of that, especially the last point. That was what I intended, and William and others here agreed with it, so it seems to be ok to implement. This patch should implement everything. I have opened a new patch to include sagenb.notebook.tutorial into the ReST documentation too: #8011.



---

archive/issue_comments_021238.json:
```json
{
    "body": "Various fixes, small enhancements.  See comment.  Replaces previous.",
    "created_at": "2010-01-21T12:53:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3083",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3083#issuecomment-21238",
    "user": "https://github.com/qed777"
}
```

Various fixes, small enhancements.  See comment.  Replaces previous.



---

archive/issue_comments_021239.json:
```json
{
    "body": "Attachment [trac_3083-print-documentation.4.patch](tarball://root/attachments/some-uuid/ticket3083/trac_3083-print-documentation.4.patch) by @qed777 created at 2010-01-21 12:55:33",
    "created_at": "2010-01-21T12:55:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3083",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3083#issuecomment-21239",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_3083-print-documentation.4.patch](tarball://root/attachments/some-uuid/ticket3083/trac_3083-print-documentation.4.patch) by @qed777 created at 2010-01-21 12:55:33



---

archive/issue_comments_021240.json:
```json
{
    "body": "Attachment [trac_3083-print-documentation.4.2.patch](tarball://root/attachments/some-uuid/ticket3083/trac_3083-print-documentation.4.2.patch) by @qed777 created at 2010-01-21 13:15:43\n\nV4.2\n\n* Implements the \"last point\" above in a different way.  With V3, the output formatting didn't persist --- docstrings in restarted/reopened and published worksheets were escaped.  Docstrings also appeared twice in each output cell.\n\n* Popping now\n  * Resets the cell's introspection state.\n  * Puts the object's name in the dialog title, with a bit of color.\n  * Destroys just that dialog on close.  The previous query was broad enough that it could close multiple dialogs.\n\n* Moves `\"\"\"nodoctest\\n\"\"\"` back to the top of `notebook_object.py`.\n\nAgain, great work!  My review is positive, but someone should review my changes.",
    "created_at": "2010-01-21T13:15:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3083",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3083#issuecomment-21240",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_3083-print-documentation.4.2.patch](tarball://root/attachments/some-uuid/ticket3083/trac_3083-print-documentation.4.2.patch) by @qed777 created at 2010-01-21 13:15:43

V4.2

* Implements the "last point" above in a different way.  With V3, the output formatting didn't persist --- docstrings in restarted/reopened and published worksheets were escaped.  Docstrings also appeared twice in each output cell.

* Popping now
  * Resets the cell's introspection state.
  * Puts the object's name in the dialog title, with a bit of color.
  * Destroys just that dialog on close.  The previous query was broad enough that it could close multiple dialogs.

* Moves `"""nodoctest\n"""` back to the top of `notebook_object.py`.

Again, great work!  My review is positive, but someone should review my changes.



---

archive/issue_comments_021241.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-21T13:15:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3083",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3083#issuecomment-21241",
    "user": "https://github.com/qed777"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_021242.json:
```json
{
    "body": "Moves the module docstring to the top as well.",
    "created_at": "2010-01-22T22:54:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3083",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3083#issuecomment-21242",
    "user": "https://github.com/TimDumol"
}
```

Moves the module docstring to the top as well.



---

archive/issue_comments_021243.json:
```json
{
    "body": "Attachment [trac_3083-print-documentation.5.patch](tarball://root/attachments/some-uuid/ticket3083/trac_3083-print-documentation.5.patch) by @TimDumol created at 2010-01-22 23:34:36\n\nPositive review for your changes, but I've added a new patch that moves the module docstring of `notebook_object.py` to the top of the file, otherwise documentation won't build (the notebook must be `setup.py instal`ed for the updated documentation to build).",
    "created_at": "2010-01-22T23:34:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3083",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3083#issuecomment-21243",
    "user": "https://github.com/TimDumol"
}
```

Attachment [trac_3083-print-documentation.5.patch](tarball://root/attachments/some-uuid/ticket3083/trac_3083-print-documentation.5.patch) by @TimDumol created at 2010-01-22 23:34:36

Positive review for your changes, but I've added a new patch that moves the module docstring of `notebook_object.py` to the top of the file, otherwise documentation won't build (the notebook must be `setup.py instal`ed for the updated documentation to build).



---

archive/issue_events_003297.json:
```json
{
    "actor": "@qed777",
    "created_at": "2010-01-25T00:57:52Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3083",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3083#event-3297"
}
```



---

archive/issue_comments_021244.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-25T00:57:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3083",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3083#issuecomment-21244",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed



---

archive/issue_comments_021245.json:
```json
{
    "body": "Don't truncate long docstrings.  Apply on top of previous patch, e.g., #8051's sagenb-0.7.1.",
    "created_at": "2010-01-30T05:52:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3083",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3083#issuecomment-21245",
    "user": "https://github.com/qed777"
}
```

Don't truncate long docstrings.  Apply on top of previous patch, e.g., #8051's sagenb-0.7.1.



---

archive/issue_comments_021246.json:
```json
{
    "body": "Attachment [trac_3083-notruncate.patch](tarball://root/attachments/some-uuid/ticket3083/trac_3083-notruncate.patch) by @qed777 created at 2010-01-30 05:53:41\n\nI've added a \"notruncate\" patch that blocks #8051.",
    "created_at": "2010-01-30T05:53:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3083",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3083#issuecomment-21246",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_3083-notruncate.patch](tarball://root/attachments/some-uuid/ticket3083/trac_3083-notruncate.patch) by @qed777 created at 2010-01-30 05:53:41

I've added a "notruncate" patch that blocks #8051.



---

archive/issue_comments_021247.json:
```json
{
    "body": "Positive review about the idea of adding notruncate.  That makes perfect sense to me.",
    "created_at": "2010-01-30T23:52:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3083",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3083#issuecomment-21247",
    "user": "https://github.com/williamstein"
}
```

Positive review about the idea of adding notruncate.  That makes perfect sense to me.
