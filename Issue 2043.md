# Issue 2043: [with spkg] add proper LDFLAGS to libpng.spkg

Issue created by migration from https://trac.sagemath.org/ticket/2043

Original creator: mabshoff

Original creation time: 2008-02-04 04:29:17

Assignee: mabshoff

libpng.spkg currently relies on the system to provide a libz, so set LDFLAGS properly to pick up Sage's libz.

Cheers,

Michael


---

Comment by mabshoff created at 2008-02-17 23:43:45

This is a dupe of #2068 - William needs to pay more attention to trac :)

Cheers,

Michael


---

Comment by mabshoff created at 2008-02-17 23:43:59

Resolution: duplicate
