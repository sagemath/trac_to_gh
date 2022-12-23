# Issue 1638: FreeBSD: change "/bin/bash" to "/usr/bin/env bash"

Issue created by migration from https://trac.sagemath.org/ticket/1638

Original creator: mabshoff

Original creation time: 2007-12-30 12:57:41

Assignee: mabshoff

Keywords: FreeBSD

On FreeBSD the default bash installtion location is `/neusr/local`. Hence all our shell scripts with `/bin/bash` will break. The solution is to use `/usr/bin/env bash` instead. The same might apply to python and perl scripts.

Cheers,

Michael


---

Comment by mabshoff created at 2007-12-31 10:26:52

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-08-25 04:16:36

All known instances of /bin/bash have been fixed. So I am closing this and any new instances can be fixed via new tickets.

Cheers,

Michael


---

Comment by mabshoff created at 2008-08-25 04:16:36

Resolution: fixed
