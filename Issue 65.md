# Issue 65: Profiler prints incorrect lines

Issue created by migration from https://trac.sagemath.org/ticket/65

Original creator: dmharvey

Original creation time: 2006-09-16 15:11:08

Assignee: dmharvey

The Profiler class prints incorrect source code lines when the relevant source is right near the end of the source file (or probably right at the beginning too). Seems to be because the "inspect" module returns a truncated list. Shouldn't be hard to fix.


---

Comment by was created at 2007-01-13 02:14:31

It would be much easier if there were an example with this bug report.  As is, it will be difficult to replicate (?).


---

Comment by was created at 2007-10-21 01:46:25

Resolution: invalid


---

Comment by was created at 2007-10-21 02:50:28

David says: "I'm unable to reproduce the thing that I remember going wrong. So I'm
happy for it to be closed."
