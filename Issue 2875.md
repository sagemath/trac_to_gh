# Issue 2875: notebook -- save_session is completely broken in the notebook

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-04-11 04:39:23

Assignee: boothby




---

Comment by was created at 2008-04-12 03:31:48

Changing priority from major to blocker.


---

Attachment


---

Comment by boothby created at 2008-04-12 07:20:48

The code looks reasonable to me, but I don't know what to test.  Please add doctests to save_session() and do_sage_extensions_preparsing().


---

Comment by was created at 2008-04-13 05:45:16

See #2901 which provides the doctesting.


---

Comment by mabshoff created at 2008-04-13 23:54:30

After deleting the first hunk from the patch (since it is deleted anyway via #2901 and I had to resolve that conflict manually) the patch applies cleanly.

Cheers,

Michael


---

Comment by mabshoff created at 2008-04-13 23:54:43

Merged in Sage 3.0.alpha5


---

Comment by mabshoff created at 2008-04-13 23:54:43

Resolution: fixed
