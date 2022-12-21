# Issue 2893: [with patch; needs review] notebook -- make it explicitly clear which systems are optional

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-04-12 03:28:33

Assignee: boothby

I've noticed a lot of confusion by the list of systems in the drop-down menu for Sage, especially between the optional and non-optional systems.  This patch:
  * makes which systems are optional clear
  * Adds an html system (which is pretty funny -- all input gets html'd). 

The html part of this patch relies on #2890.




---

Attachment


---

Comment by mhansen created at 2008-04-12 07:20:13

Looks good to me.


---

Comment by mabshoff created at 2008-04-12 10:52:30

Resolution: fixed


---

Comment by mabshoff created at 2008-04-12 10:52:30

Merged in Sage 3.0.alpha4
