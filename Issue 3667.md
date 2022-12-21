# Issue 3667: [with patch; needs (easy) review] notebook -- if user history can't be loaded from disk make it blank (much better than making entire notebook not work at all)

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-07-16 07:44:35

Assignee: boothby

If the user's command log for some reason can't be loaded from disk, currently the notebook
simply fails to ever work for them again.  This is not ideal behavior.  This 1-line patches fixes
this problem by making the history log empty in this case. 


---

Attachment

As is this is next to impossible to doctest. Positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-07-16 18:27:12

Resolution: fixed


---

Comment by mabshoff created at 2008-07-16 18:27:12

Merged in Sage 3.0.6.alpha0
