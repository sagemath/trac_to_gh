# Issue 848: Using strings for infinity

Issue created by migration from Trac.

Original creator: robertwb

Original creation time: 2007-10-11 09:02:45

Assignee: was

sage/gsl/integration.pyx uses the strings 'inf' and '-inf' rather than the infinity element for its bounds. 



---

Attachment

See the attached patch.


---

Comment by mhansen created at 2008-04-14 22:52:56

Looks good to me.  All tests in gsl/ pass.


---

Comment by mabshoff created at 2008-04-14 23:56:26

Resolution: fixed


---

Comment by mabshoff created at 2008-04-14 23:56:26

Merged in Sage 3.0.alpha5
