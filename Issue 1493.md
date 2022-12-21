# Issue 1493: polybori doesn't free m4ri data on exit

Issue created by migration from Trac.

Original creator: burcin

Original creation time: 2007-12-13 20:39:42

Assignee: burcin

The polybori wrapper initializes m4ri by building some tables, but this is not freed on exit. As polybori is now imported from top level, this shows up as still reachable memory on valgrind for every sage session.

The bundle attached fixes this, along with a minor modification to remove a workaround for a polybori bug which is now fixed.


---

Comment by mabshoff created at 2007-12-14 02:28:18

Resolution: fixed


---

Attachment

Merged in 2.9.alpha7.
