# Issue 5437: [with patch; needs review] pickle jar -- make it run through in order

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-03-04 05:32:31

Assignee: mabshoff

Current when unpickling the pickle jar the files are run through in whatever order os.listdir gives them.  This patch instead unpickles in order.


---

Attachment


---

Comment by mabshoff created at 2009-03-04 19:50:50

Positive reiview.

Cheers,

Michael


---

Comment by mabshoff created at 2009-03-04 19:51:50

Merged in Sage 3.4.rc1.

Cheers,

Michael


---

Comment by mabshoff created at 2009-03-04 19:51:50

Resolution: fixed
