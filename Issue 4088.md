# Issue 4088: notebook -- on list of published worksheets if no worksheets, everyone sees welcome message

Issue created by migration from Trac.

Original creator: TimothyClemans

Original creation time: 2008-09-09 14:12:18

Assignee: boothby

Make the welcome message "Welcome to Sage! You can create a new worksheet, view published worksheets, or read the documentation." not appear on the published worksheet listings ever.


---

Attachment


---

Comment by mhansen created at 2008-09-19 00:20:00

This fixes it for me, and I have added a selenium test to verify that it is indeed fixed.


---

Comment by mabshoff created at 2008-09-19 04:04:05

Resolution: fixed


---

Comment by mabshoff created at 2008-09-19 04:04:05

Merged in Sage 3.1.3.alpha0
