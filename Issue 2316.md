# Issue 2316: dsage.start_all() can leave zombie workers around

Issue created by migration from Trac.

Original creator: yi

Original creation time: 2008-02-26 17:40:08

Assignee: yi

CC:  was

Keywords: dsage

If you do dsage.start_all() and kill the server without killing the workers, the workers will be left hanging around so that the next time you do dsage.start_all(), you'll have twice as many workers.


---

Comment by yi created at 2008-04-01 22:46:31

patch which kills dsage server and workers when exiting sage


---

Attachment

Attached patch which kills the dsage server and worker on exit. This in conjunction with the sage cleaner should fix the zombie issues.


---

Comment by mhansen created at 2008-04-07 01:12:39

The patch applies to 3.0.alpha1 and fixes the issue for me.


---

Comment by mabshoff created at 2008-04-07 01:18:59

Resolution: fixed


---

Comment by mabshoff created at 2008-04-07 01:18:59

Merged in Sage 3.0.alpha2
