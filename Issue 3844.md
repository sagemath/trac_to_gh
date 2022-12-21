# Issue 3844: notebook -- worksheet should call sys.path.append(DATA) when being initalized

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-08-14 00:58:34

Assignee: boothby

If we do the above then one can upload/attach a .py file and import it in the worksheet, which is really sweet.


---

Attachment


---

Comment by TimothyClemans created at 2008-08-14 04:43:09

When I attached hi.py, "import hi" didn't work. Also on http://sage.math.washington.edu:8999/home/admin/3/datafile?name=hi.py, there is no mention of this new functionality.


---

Comment by was created at 2009-11-19 23:50:09

I've attached a totally new patch that is 1-line, works, and does the right thing, and is imho quite nice.  

I still don't have my computer setup for Selenium, but a test this works is to do this in the notebook:

```
DATA in sys.path
///
True
```



---

Comment by was created at 2009-11-19 23:50:09

Changing status from needs_work to needs_review.


---

Attachment

apply only this -- ignore the old sage-3844.patch


---

Comment by timdumol created at 2009-12-06 03:46:22

Changing status from needs_review to needs_work.


---

Comment by timdumol created at 2009-12-06 03:46:22

I've come across the same problem as TimothyClemans -- importing it after attachment does not work. Also, it would probably be best to advertise the functionality on the data page, as TimothyClemans stated.


---

Attachment

Updates `tutorial.py`. Replaces previous.


---

Comment by mpatel created at 2010-01-22 04:19:03

This works for me -- After I upload a data file `foo.py` (or create a new one), I can `import foo` in a worksheet cell.

Positive review.  V2 just adds the changes to `tutorial.py` from the original patch.

A `load` / `attach` analogue of `sys.path` might be warmly-received: #378, #1484, #5169.

By the way, FF 3.6 will permit drag-and-drop file uploads.  See [this blog post](http://hacks.mozilla.org/2009/12/file-drag-and-drop-in-firefox-3-6/) for a video and simple demo.


---

Comment by mpatel created at 2010-01-22 04:19:03

Changing status from needs_work to needs_review.


---

Comment by mpatel created at 2010-01-22 04:19:16

Changing status from needs_review to positive_review.


---

Attachment

Rebased for SageNB 0.6 + queue in comment.  Replaces previous.


---

Comment by mpatel created at 2010-01-25 01:14:50

Resolution: fixed


---

Comment by mpatel created at 2010-01-25 01:16:29

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
