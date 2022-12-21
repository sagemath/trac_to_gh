# Issue 7435: notebook: help screen talks about DIR variable, which was removed from the notebook a while ago

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-11-11 22:30:19

Assignee: boothby

CC:  acleone mpatel

So... delete the section about the DIR variable, or make sure it is defined as explained in the help screen.  What do people prefer?


---

Comment by timdumol created at 2010-01-19 09:46:51

Adds the DIR variable


---

Attachment

This patch adds the DIR variable.


---

Comment by timdumol created at 2010-01-19 09:47:17

Changing status from new to needs_review.


---

Comment by acleone created at 2010-01-19 12:48:00

Changing status from needs_review to positive_review.


---

Comment by acleone created at 2010-01-19 12:48:00

LGTM.


---

Attachment

Rebased for SageNB 0.6 + queue in comment.  Replaces previous.


---

Comment by mpatel created at 2010-01-25 01:09:07

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

Comment by mpatel created at 2010-01-25 01:09:07

Resolution: fixed


---

Comment by mpatel created at 2010-01-25 03:17:15

Fix failed doctests.  Replaces previous.


---

Comment by mpatel created at 2010-01-25 03:18:50

Changing status from closed to needs_work.


---

Attachment

V3 adds `DIR        = None` near the top of `twist.py`, to fix failed doctests in `cell.py` and `worksheet.py`.


---

Comment by mpatel created at 2010-01-25 03:18:56

Changing status from needs_work to needs_review.


---

Comment by acleone created at 2010-01-25 03:22:34

Changing status from needs_review to positive_review.


---

Comment by acleone created at 2010-01-25 03:22:34

LGTM.


---

Comment by was created at 2010-02-06 18:17:02

Merged into sage-4.3.2 (post Minh's sage-4.3.2).
