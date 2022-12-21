# Issue 6686: [with patch, needs review] Missing closing </center> tag in notebook help page

Issue created by migration from Trac.

Original creator: mpatel

Original creation time: 2009-08-08 09:56:15

Assignee: boothby

The notebook help page `http://localhost:8000/help` is not properly centered, because a closing `</center>` tag was omitted at #6225.


---

Attachment


---

Comment by mpatel created at 2009-08-08 10:01:39

Alternative way to balance <center> tags.  Apply either this OR the other patch.


---

Attachment


---

Comment by kcrisman created at 2009-08-26 13:47:10

The second patch is fine, and makes more sense (the whole thing is centered after the top matter).  Positive review.


---

Comment by mvngu created at 2009-08-26 21:13:32

Resolution: fixed


---

Comment by mvngu created at 2009-08-26 21:13:32

Merged `trac_6686-help_center_tag_alt.patch`.
