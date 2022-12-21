# Issue 5815: [with patch, needs review] Disable TinyMCE in the live documentation

Issue created by migration from Trac.

Original creator: mpatel

Original creation time: 2009-04-18 09:32:47

Assignee: boothby

Double-clicking on a text cell in the live documentation --- I've done this accidentally several times --- fires up TinyMCE, which acts strangely.  More importantly, no changes will be saved, as Jason Grout pointed out on sage-devel:

http://groups.google.com/group/sage-devel/browse_thread/thread/8c8fe7c5d0c0f725



---

Attachment

See the comment.


---

Comment by mpatel created at 2009-04-18 09:43:32

The new line of code, like the CSS "hack" which follows it, depends, I think, on an exact match.

Perhaps it's better to add code which disables editing.


---

Comment by jason created at 2009-04-22 02:11:54

I agree that the above patch is the wrong solution.  I'll post a patch momentarily which disables it just like when the sheet is published.


---

Comment by jason created at 2009-04-22 02:20:47

apply instead of previous patch.


---

Attachment

trac-5815-docs-and-tinymce.patch takes care of this issue by implementing the idea from the comment above (i.e., don't put the TinyMCE trigger in when you are looking at a doc page).

mpatel, can you review this patch?


---

Comment by mpatel created at 2009-04-22 03:34:09

The new patch works and is definitely better than the first.

I noticed that copying or printing a docbrowser worksheet omits Sphinx' stylesheet.  One-cell mode also appears to be broken.  Of course, these are separate issues, and I can open new tickets.


---

Comment by mpatel created at 2009-04-22 03:45:30

Replying to [comment:4 mpatel]:
> I noticed that copying or printing a docbrowser worksheet omits Sphinx' stylesheet.  One-cell mode also appears to be broken.  Of course, these are separate issues, and I can open new tickets.
Oops!  One-cell mode is fine.  Sorry.


---

Comment by mabshoff created at 2009-04-24 09:46:25

Merged trac-5815-docs-and-tinymce.patch in Sage 3.4.2.alpha0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-24 09:46:25

Resolution: fixed
