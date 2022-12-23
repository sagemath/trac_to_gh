# Issue 6556: notebook: document keyboard shortcuts

Issue created by migration from https://trac.sagemath.org/ticket/6556

Original creator: mvngu

Original creation time: 2009-07-18 20:41:45

Assignee: tba

Keywords: notebook, keyboard shortcuts

This issue was raised in this [sage-support](http://groups.google.com/group/sage-support/browse_thread/thread/58284efb2a15856e) thread. All key combinations and keyboard shortcuts for the notebook should be documented in the tutorial and the reference manual. The tutorial should also inform readers about the Help link on the notebook. That link contains useful key combinations when using the Sage notebook. The file

SAGE_ROOT/devel/sage-main/sage/server/notebook/config.py

contains all known key combinations for the notebook.


---

Attachment

Reorganize notebook help page


---

Comment by hgranath created at 2009-08-07 03:43:30

I think it would be helpful for users if the info on the notebook
Help link was more organized. Here is a suggestion to group
topics, especially about key bindings, to make them easier to
find.

A few questions:

I changed "Delete Cell" form ctrl-backspace to backspace. Is there
any reason not to?

The < and > indentation bindings do not work form me in firefox
3.0.13 (tab and shift-tab do).

I added Comment/Uncomment Blocks bindings. Which bindings are
preferred, ctrl-./ctrl-, or ctrl-3/ctrl-4 ?


---

Comment by hgranath created at 2009-08-17 17:41:23

Updates help page, tutorial and reference manual


---

Attachment


---

Comment by timdumol created at 2009-08-30 19:38:13

Works perfectly, and the new documentation is great. Nice work.

Note: Only apply `trac_6556.patch`.


---

Comment by mvngu created at 2009-08-31 07:00:36

Merged `trac_6556.patch`.


---

Comment by mvngu created at 2009-08-31 07:00:36

Resolution: fixed
