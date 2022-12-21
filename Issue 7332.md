# Issue 7332: Escape css id's and classes in templates

Issue created by migration from Trac.

Original creator: timdumol

Original creation time: 2009-10-28 13:50:08

Assignee: boothby

CC:  was mpatel

Currently, some css id's and classes have illegal values ('admin/0', for example, in `worksheet_listing.html`). This prevents jQuery and Selenium from accessing those attributes.

This adds a filter to produce legal values from those values.


---

Attachment

Adds `css_escape` filter and makes `worksheet_listing.html` use it.


---

Comment by timdumol created at 2009-10-28 13:56:03

Changing status from new to needs_review.


---

Comment by timdumol created at 2009-10-28 14:17:39

Fixed `notebook_lib.js` so that the checkboxes work after the patch.


---

Attachment

Deepends on #7310.


---

Attachment

Also fix the overall checkbox ("controlbox"). Apply only this patch.


---

Comment by mpatel created at 2009-10-31 08:43:29

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

Comment by was created at 2009-11-11 19:43:17

Changing status from needs_review to positive_review.


---

Comment by was created at 2009-11-11 19:43:17

Looks good to me.


---

Comment by was created at 2009-11-11 19:43:59

Resolution: fixed


---

Comment by mpatel created at 2010-01-01 21:51:12

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

Comment by mpatel created at 2010-01-01 22:48:31

See #7811.
