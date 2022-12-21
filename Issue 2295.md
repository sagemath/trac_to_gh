# Issue 2295: [with patch, needs review] build cache check fails on paths containing symlinks

Issue created by migration from Trac.

Original creator: burcin

Original creation time: 2008-02-24 20:00:54

Assignee: burcin

My SAGE_ROOT contains a symlinked component, upgrading from 2.10.2.alpha0 to 2.10.2 failed with the error message in this thread:

http://groups.google.com/group/sage-support/browse_thread/thread/d8ee3de015fbf7be

Only the filename listed was different.

This is caused by the module_path function in setup.py, assuming os.path.abspath starts with SAGE_ROOT, which is not the case when path contains a symlink. Attached patch fixes this issue.




---

Attachment

fix build cache problem when sage_root has symlinks


---

Comment by mabshoff created at 2008-02-24 20:44:31

I tested the patch with a non-symlinked $SAGE_ROOT and it keeps working. The problem has come up before and it is good that it has been finally fixed. Positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-02-24 20:45:35

Resolution: fixed


---

Comment by mabshoff created at 2008-02-24 20:45:35

Merged in Sage 2.10.3.alpha0
