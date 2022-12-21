# Issue 2652: notebook should let you evaluate cells without losing cursor position

Issue created by migration from Trac.

Original creator: cwitty

Original creation time: 2008-03-22 23:33:41

Assignee: boothby

Requested by jpviiva on #sage-devel...

This could be a new keystroke (Control-Enter perhaps?) that evaluates the current cell without moving the cursor to the next block.  Another possibility (probably less desirable) is to fix it so that if you evaluate a cell, then press backspace, you end up at the same cursor location instead of at the beginning of the block.


---

Comment by kcrisman created at 2014-09-18 02:42:35

Still a good idea!  Though that combo is taken.  See https://github.com/sagemath/sagenb/issues/234


---

Comment by boothby created at 2020-03-29 02:03:10

Resolution: invalid


---

Comment by boothby created at 2020-03-29 02:03:10

Closing deprecated notebook tickets
