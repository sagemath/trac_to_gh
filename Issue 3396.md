# Issue 3396: [with patch, needs review] new function in misc/latex.py: print_or_typeset

Issue created by migration from https://trac.sagemath.org/ticket/3396

Original creator: jhpalmieri

Original creation time: 2008-06-11 04:31:55

Assignee: somebody

Keywords: latex, view, print

This patch defines a function in sage.misc.latex, print_or_typeset, which runs 'view' if in notebook mode with the typeset box, and runs 'print' otherwise.  See the discussion toward the end of this thread:

[http://groups.google.com/group/sage-support/browse_frm/thread/9698e83a1d1b22ac](http://groups.google.com/group/sage-support/browse_frm/thread/9698e83a1d1b22ac)




---

Comment by jhpalmieri created at 2008-06-11 04:32:32

new function, print_or_typeset


---

Attachment

apply this after the other patch


---

Comment by mabshoff created at 2008-06-15 20:07:54

Merged both patch in Sage 3.0.3.rc0


---

Comment by mabshoff created at 2008-06-15 20:07:54

Resolution: fixed
