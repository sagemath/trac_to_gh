# Issue 3213: notebook -- Account Settings page for changing password and e-mail address

Issue created by migration from https://trac.sagemath.org/ticket/3213

Original creator: TimothyClemans

Original creation time: 2008-05-16 00:22:37

Assignee: boothby




---

Comment by TimothyClemans created at 2008-05-16 00:24:58

I used sage-3.0.1 and applied http://sage.math.washington.edu/home/was/patches/bugday12.hg


---

Attachment


---

Comment by was created at 2008-05-16 05:02:48

REVIEW:

  I think the code looks fine and this should be applied.

I think the settings panel itself has a lot of work until it is the ultimate
settings panel, etc.  But this is a very good start, and additional work
should simply go in another patch.  Some comments for future work:

   * Instead of "Cancel" being the only way to leave the settings page, how about a "Save" button that saves all changes, and a "cancel" button that throws away all changes?
   * Currently changes are still saved even if you click cancel.
   * Make the thing a little more stylish. 

Please do these as a separate ticket from this ticket, since I want #3213 to get
in as is. 

This patch I think depends on Tim's other patch for "changing the password".

 -- William


---

Comment by TimothyClemans created at 2008-05-16 20:55:28

Follow up ticket with patch needing review is #3228.


---

Comment by mabshoff created at 2008-05-17 20:25:24

Resolution: fixed


---

Comment by mabshoff created at 2008-05-17 20:25:24

Merged in Sage 3.0.2.alpha1
