# Issue 3279: Sage 3.0.2.rc0: Copy dsage_* scripts from the scrips.spkg

Issue created by migration from https://trac.sagemath.org/ticket/3279

Original creator: mabshoff

Original creation time: 2008-05-23 15:15:55

Assignee: failure

Due to a bug not caught in #3097 we end up with an inconsistent repo in $SAGE_LOCAL/bin:

```
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.0.2.final/local/bin$ hg status
! dsage_setup.py
! dsage_worker.py
```

The files are in the scripts.spkg:

```
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.0.2.final/spkg/standard/sage_scripts-3.0.2.rc0$ ls -al dsage_*
-rwxr-xr-x 1 mabshoff 1090  7479 2008-05-22 23:19 dsage_setup.py
-rwxr-xr-x 1 mabshoff 1090 35459 2008-05-22 23:19 dsage_worker.py
```

When those two scripts are missing the DSage tests just hang.

Patch coming up.

Cheers,

Michael


---

Comment by mabshoff created at 2008-05-23 15:39:35

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-05-23 15:39:35

Changing assignee from failure to mabshoff.


---

Attachment


---

Comment by mabshoff created at 2008-05-23 16:41:46

Resolution: fixed


---

Comment by mabshoff created at 2008-05-23 16:41:46

Merged in Sage 3.0.2.rc1
