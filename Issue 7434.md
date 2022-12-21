# Issue 7434: notebook: new modal jquery dialog boxes are covered by jmol 3d graphics

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-11-11 22:20:44

Assignee: boothby

Trac #7310 introduced nice modal jquery dialog boxes.  Unfortunately, they do not play well at all with the output of jmol 3d graphics (java).  See this screenshot:


---

Comment by mpatel created at 2009-11-12 02:57:47

[This](http://stackoverflow.com/questions/638886/java-applet-z-index-problem-safari-and-beyond) appears to be relevant.


---

Attachment


---

Comment by acleone created at 2010-01-19 05:52:58

Changing status from new to needs_review.


---

Comment by acleone created at 2010-01-19 05:52:58

trac_7434-jmol_modal_dialogs.patch: This patch hides all java applets on the page and puts grey boxes in their place when any modal prompts show up (in notebook_lib.js: function modal_prompt(...)).

trac_7434-jmol_modal_dialogs_test.patch: This patch adds a selenium test for the above patch.


---

Comment by timdumol created at 2010-01-19 08:27:31

LGTM.


---

Comment by timdumol created at 2010-01-19 08:27:31

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-01-25 01:27:36

Rebased for SageNB 0.6 + queue in comment.  Replaces earlier version.


---

Attachment

Please ignore V2.  I've just noticed that the patch doesn't work in Cr4, IE8, and S4 on Windows XP.  It seems the WebKit browsers use `applet`s instead of `object`s.  IE8 uses `object`s, but the `type` attribute is empty.

V3 fixes this with [jmolSetAppletCssClass](http://jmol.sourceforge.net/jslibrary/#jmolSetAppletCssClass) and `$('.jmol_applet')`.


---

Comment by mpatel created at 2010-01-25 02:53:08

Changing status from positive_review to needs_work.


---

Comment by mpatel created at 2010-01-25 02:55:21

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

Attachment

Fix WebKit, IE8 hiding. Rebase vs. queue in comment.  Replaces previous.


---

Comment by mpatel created at 2010-01-25 02:56:26

Changing status from needs_work to needs_review.


---

Comment by acleone created at 2010-01-25 03:09:12

LGTM


---

Comment by acleone created at 2010-01-25 03:09:12

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-01-25 03:09:43

Resolution: fixed
