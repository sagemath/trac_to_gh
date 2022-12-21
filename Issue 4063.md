# Issue 4063: properly escape the titles of worksheets

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2008-09-04 16:22:52

Assignee: boothby

CC:  mhansen

Currently the :8102 server has several javascript popups that come up when viewing the list of published worksheets.  Apparently at least one of these worksheets includes javascript code as part of the title.  This is really annoying right now, but could be more dangerous in the future.



---

Attachment


---

Comment by TimothyClemans created at 2008-09-08 13:56:54

Please remove sage-3076_1.patch


---

Comment by mabshoff created at 2008-09-16 04:55:12

This should really be in 3.1.2. Mike: can you review this?

Cheers,

Michael


---

Attachment


---

Comment by mhansen created at 2008-09-16 06:30:59

I added a few extra cases and added a doctest.  Otherwise, it looks good to me.


---

Comment by mabshoff created at 2008-09-16 06:53:20

I also agree with Mike's patch. Similar issues might lurk in a couple other places, but this fixes at least one issue that has been known to be abused.

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-16 06:53:32

Resolution: fixed


---

Comment by mabshoff created at 2008-09-16 06:53:32

Merged trac_4063.patch in Sage 3.1.2.rc5
