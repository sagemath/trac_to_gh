# Issue 1977: valgrind 3.3.0 no longer appends $PID per default to the logs

Issue created by migration from https://trac.sagemath.org/ticket/1977

Original creator: mabshoff

Original creation time: 2008-01-30 04:30:52

Assignee: mabshoff

I read something about this in the release notes, but the `--help` section of the valgrind command seems to be missing any clue how to reenable it.

Cheers,

Michael


---

Comment by mabshoff created at 2008-02-02 05:03:31

For valgrind 3.3.0 we need to append `%p` to all the logfile names.

Cheers,

Michael


---

Comment by mabshoff created at 2008-02-02 05:03:31

Changing status from new to assigned.


---

Attachment

Looks good to me.


---

Comment by mabshoff created at 2008-02-02 06:31:29

Resolution: fixed


---

Comment by mabshoff created at 2008-02-02 06:31:29

Merged in Sage 2.10.1.rc5
