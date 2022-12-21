# Issue 5095: [with patch, needs review] AJAX requests don't work from the worksheet listing page

Issue created by migration from Trac.

Original creator: mhansen

Original creation time: 2009-01-25 07:16:04

Assignee: boothby

This is because the TinyMCE patch made the AJAX requests dependent of jQuery, but the worksheet listing page did not include jQuery. 


---

Attachment


---

Comment by jhpalmieri created at 2009-01-25 16:55:06

works for me.


---

Comment by mabshoff created at 2009-01-28 13:03:24

Merged in Sage 3.3.alpha3.

Cheers,

Michael


---

Comment by mabshoff created at 2009-01-28 13:03:24

Resolution: fixed
