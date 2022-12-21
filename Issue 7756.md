# Issue 7756: Extra, unwanted text inserted in cells by shift-enter

Issue created by migration from Trac.

Original creator: mpatel

Original creation time: 2009-12-24 06:18:37

Assignee: was

See [sage-notebook](http://groups.google.com/group/sage-notebook/browse_thread/thread/95aa96ca848ef135) and [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/47f6756f00df1f72/6f3dd9ce745832e4?#6f3dd9ce745832e4).


---

Comment by mpatel created at 2009-12-24 06:22:46

Minimal version ripped from #7666. sagenb repo.


---

Attachment

The problem seems to be that the auto-indent code "fires" too often, e.g., when the shift key comes up before the enter key.  The [attachment:trac_7756-extra_text_shift_enter.patch patch] should fix this in Cr, FF, S, and O.  If it does not, please let me know!

Note: I've extracted the patch here from the patch at #7666.


---

Comment by was created at 2009-12-24 06:56:16

This does indeed seem to fix the problem for me.  Subtle.

Merged into sagenb-0.4.8.


---

Comment by was created at 2009-12-24 06:56:16

Resolution: fixed
