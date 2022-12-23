# Issue 7963: Downloading multiple worksheets does not work

Issue created by migration from https://trac.sagemath.org/ticket/7963

Original creator: jason

Original creation time: 2010-01-17 10:18:51

Assignee: was

CC:  timdumol jason

I do the following:

1. Start the notebook with `notebook()`
2. click the checkboxes next to a few worksheets
3. hit the "Download" button

and I get an error:


```
The resource /download_worksheets?filenames=admin/77___S_A_G_E___admin/76___S_A_G_E___admin/75___S_A_G_E___&sep=___S_A_G_E___ cannot be found.
```



---

Comment by mpatel created at 2010-01-17 15:30:50

I think this is a matter of

```diff
--- a/sagenb/data/sage/js/notebook_lib.js
+++ b/sagenb/data/sage/js/notebook_lib.js
@@ -1515,7 +1515,7 @@ function download_worksheets_button() {
     /*
     Downloads the set of checked worksheets as a zip file.
     */
-    window.location.replace("/download_worksheets?filenames=" +
+    window.location.replace("/download_worksheets.zip?filenames=" +
                             checked_worksheet_filenames() + "&sep=" + SEP);
 }
```

but I haven't posted a patch, since #7908 and some of its dependencies make a lot of changes to `notebook_lib.js`.


---

Comment by timdumol created at 2010-01-19 08:57:38

Adds mpatel's suggested fix.


---

Comment by timdumol created at 2010-01-19 08:58:00

Changing status from new to needs_review.


---

Attachment

This adds what mpatel suggested.


---

Comment by mpatel created at 2010-01-20 04:00:29

Thanks for making a patch!  It works for me, but I'm not sure I should review this by myself.


---

Comment by acleone created at 2010-01-20 06:47:04

LGTM.


---

Comment by acleone created at 2010-01-20 06:47:04

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-01-25 01:00:28

Resolution: fixed
