# Issue 7792: Improved docs and added Width and Height at /interfaces/povray.py

Issue created by migration from Trac.

Original creator: slosoi

Original creation time: 2009-12-29 23:01:38

Assignee: was

Keywords: povray

To improve docs of Povray.
To have width and height parameters in Povray.


---

Comment by slosoi created at 2009-12-29 23:01:51

Changing status from new to needs_info.


---

Comment by slosoi created at 2009-12-29 23:01:58

Changing status from needs_info to needs_review.


---

Comment by slosoi created at 2009-12-30 03:09:04

There are some bugs apparently in the width and height parameters in the changed code. 
The parameters F and P work differently as I expected.


---

Attachment


---

Comment by slosoi created at 2009-12-30 04:26:09

Replying to [comment:3 slosoi]:
> There are some bugs apparently in the width and height parameters in the changed code. 
> The parameters F and P work differently as I expected.

The patch -file is old one. I will submit a new one after the compilation of Sage.


---

Attachment


---

Attachment

Why are you removing the docstring from the class definition?


---

Comment by boothby created at 2010-06-23 16:58:02

Changing status from needs_review to needs_work.


---

Comment by boothby created at 2010-06-23 16:58:02

Somethings up with these patches.  Both povray_doc.patch and povray_doc.2.patch are identical and won't apply on top of povray.py.  Also, the file is missing class-level documentation and doctests, (as mhampton noted, you should move the file-level doc back) and nothing is doctested in the methods.
