# Issue 1683: sage -t cubegroup.py & stops instead of running in background

Issue created by migration from Trac.

Original creator: wjp

Original creation time: 2008-01-04 22:38:30

Assignee: was

When running sage -t cubegroup.py & (to run it in the background), the process is stopped.

This is caused by pexpect.sendeof() (called from rubik.py) calling termios.tcsetattr() on stdin which causes the process to be stopped with a SIGTTOU (=write to tty from a background process).

The pexpect.sendeof() function has been entirely changed in the current version of pexpect, and using that new sendeof() fixes this problem. So, updating to a newer pexpect (ticket #502) should fix this as well.


---

Comment by wjp created at 2008-01-04 22:50:03

This issue was reported by William Stein on IRC.


---

Comment by mabshoff created at 2008-01-04 23:28:20

a temporary workaround for linux only by William


---

Attachment

I merged trac-1683-partial.patch into Sage 2.9.2.rc1. But the ticket remains open for now since the workaround doesn't work on OSX.

Cheers,

Michael


---

Comment by mhansen created at 2013-07-22 13:51:12

I suggest that we can close this ticket now with the new doctest system.


---

Comment by mhansen created at 2013-07-22 13:51:12

Resolution: invalid
