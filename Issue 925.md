# Issue 925: valgrind options to sage (sage -valgrind, sage -callgrind, etc.) should be more customizable

Issue created by migration from https://trac.sagemath.org/ticket/925

Original creator: cwitty

Original creation time: 2007-10-19 06:35:35

Assignee: mabshoff

Currently, running `sage -valgrind` or `sage -callgrind` uses a hardcoded set of command-line arguments (in local/bin/sage-valgrind and local/bin/sage-callgrind respectively).  There should be some way to change the arguments.


---

Comment by mabshoff created at 2007-10-19 06:39:53

Changing status from new to assigned.


---

Comment by mabshoff created at 2007-10-19 06:39:53

A suggested fix for this is to check if some environment variable

```
SAGE_VALGRIND_OPTIONS
```

and use the content of that if it is defined. I plan to work on this during Bug Day 4.

Cheers,

Michael


---

Attachment


---

Comment by rlm created at 2008-09-15 11:28:08

I have not tested that this works, but I have been discussing with mabshoff as he has tested. Looks good to me.


---

Comment by mabshoff created at 2008-09-15 11:30:50

Resolution: fixed


---

Comment by mabshoff created at 2008-09-15 11:30:50

Merged in Sage 3.1.2.rc4
