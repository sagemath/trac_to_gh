# Issue 112: get rid of "gap_reset_workspace"

Issue created by migration from Trac.

Original creator: was

Original creation time: 2006-10-05 10:12:46

Assignee: was

The whole gap_reset_workspace() idea is bad.  It just doesn't make any sense at all!
Here's what should happen.   

1. When a new gap component is installed a file in <SAGE_ROOT> is touched.

2. When SAGE starts, if the user's local gap_workspace is older than the file in 1,
then it is recreated.

That's it!



---

Comment by was created at 2006-10-05 11:25:17

Done.  The fix is to store the workspace in <SAGE_ROOT>/local/lib/ and only allow
the admin user to change it.  That's fine since it should only be changed when
new packages are installed anyways.


---

Comment by was created at 2006-10-05 11:25:17

Resolution: fixed
