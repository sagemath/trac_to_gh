# Issue 4067: [with patch, needs review] hmm.pyx and ghmm.pyx valgrind issues

Issue created by migration from https://trac.sagemath.org/ticket/4067

Original creator: mabshoff

Original creation time: 2008-09-05 10:10:37

Assignee: mabshoff

This is a broken out patch from #3984. It does not fix the doctest, but numerous issues valgrind picks up. Someone needs to remember that C strings are NULL terminated :)

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-05 10:10:43

Changing status from new to assigned.


---

Attachment

Patch looks good, I only read it though.


---

Comment by mabshoff created at 2008-09-05 11:05:13

Merged in Sage 3.1.2.rc0


---

Comment by mabshoff created at 2008-09-05 11:05:13

Resolution: fixed
