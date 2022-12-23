# Issue 5700: [with patch, needs review] 3.4.1.rc1: reference manual fixes

Issue created by migration from https://trac.sagemath.org/ticket/5700

Original creator: jhpalmieri

Original creation time: 2009-04-06 20:41:19

Assignee: jhpalmieri

Since #5555 is not part of Sage, strings like \ZZ, \GF{q}, or \QQ in docstrings lead to errors when processing the PDF version of the reference manual (and lead to strings like \ZZ, etc., appearing as is in the html version).  This patch changes \ZZ to \mathbf{Z}, etc.



---

Attachment


---

Comment by mabshoff created at 2009-04-06 22:19:56

Does this patch conflict in any way with #5555 or can that patch then be applied later over this one?

Cheers,

Michael


---

Comment by jhpalmieri created at 2009-04-06 22:57:13

I intended this one as a stopgap -- use it until #5555 is applied (although the code here will work fine whether #5555 is applied or not -- the two are independent).

If #5555 gets into Sage first, then this ticket can be ignored.

Also, #5610 will need to undo the changes in this ticket: part 2 of the patch there contains lots of changes of the sort \mathbf{Z} --> \ZZ, to allow users to choose which style of bold face they want.


---

Comment by jhpalmieri created at 2009-04-06 23:33:14

Ignore this ticket; work on #5555 instead.


---

Comment by jhpalmieri created at 2009-04-09 20:53:34

Resolution: wontfix


---

Comment by jhpalmieri created at 2009-04-09 20:53:34

As mentioned above, this ticket will be superseded by #5555, so this ticket should not be fixed.  After discussing it with mabshoff on irc, we decided to close this one.
