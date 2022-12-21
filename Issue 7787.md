# Issue 7787: Use a javascript minifier instead of a packer for sagenb

Issue created by migration from Trac.

Original creator: timdumol

Original creation time: 2009-12-29 10:20:28

Assignee: was

CC:  chapoton

A minifier is safer (less likely to cause errors), is faster (no need for client-side to unpack), and smaller (with gzip).

Google has reimplemented Douglas Crockford's `jsmin.py` with a BSD License for its V8 engine. It is available here:

http://code.google.com/p/v8/source/browse/branches/bleeding_edge/tools/jsmin.py


---

Attachment

Adds Google's jsmin.py


---

Comment by timdumol created at 2009-12-29 10:34:15

Changing status from new to needs_review.


---

Attachment

Replaces JavaScriptCompressor with JavaScriptMinifier


---

Attachment

Adds Google's jsmin.py. Apply this patch alone.


---

Comment by timdumol created at 2009-12-29 15:16:57

Changing status from needs_review to needs_work.


---

Comment by timdumol created at 2009-12-29 15:16:57

Google's `jsmin.py` causes failures ("//" in a string deletes the rest of the line), and does not remove unneeded lines.


---

Comment by mkoeppe created at 2020-08-18 00:36:52

Proposing to close all sagenb tickets as outdated, so that all remaining open tickets in the notebook component are about the Jupyter notebook.


---

Comment by mkoeppe created at 2020-08-18 00:36:52

Changing status from needs_work to needs_review.


---

Comment by chapoton created at 2020-08-19 08:53:50

Resolution: invalid
