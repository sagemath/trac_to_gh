# Issue 997: when installing sage and when installing sage binaries should do some sort of touch to avoid unecessary rebuilds

Issue created by migration from https://trac.sagemath.org/ticket/997

Original creator: was

Original creation time: 2007-10-25 06:37:32

Assignee: cwitty

A command like

```
find . -type f | xargs touch
```

which will touch all files (without spaces) in all subdirectories
may be useful.

Sorry this ticket is somewhat vague.  The point is mainly that
"sage -br" causes rebuilding everything too often, e.g., after
extracting a binary, or always if your machine has a huge clock skew, e..g, if your machine things it is a few days before the
timestamps on a release that you just downloaded or installed. 

William


---

Comment by mabshoff created at 2007-10-29 07:24:44

Resolution: invalid


---

Comment by mabshoff created at 2007-10-29 07:24:44


```
[08:19] <mabshoff> wstein: didn't you do something like #997?
[08:19] <wstein> yes, but I had to revert what I did do, which was really dumb.
[08:19] <wstein> You can close that as invalid.
```

Cheers,

Michael
