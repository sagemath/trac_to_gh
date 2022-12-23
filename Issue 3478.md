# Issue 3478: clisp picks up wrong dvipdf

Issue created by migration from https://trac.sagemath.org/ticket/3478

Original creator: dmharvey

Original creation time: 2008-06-19 22:26:24

Assignee: mabshoff

on my OSX 10.4.11 intel,

the clisp build was picking up dvipdf from the wrong place (fink or darwinports or something) and failed while trying to build its docs.



---

Comment by mabshoff created at 2009-02-16 01:53:37

Resolution: fixed


---

Comment by mabshoff created at 2009-02-16 01:53:37

This is no longer an issue since Sage with MacPorts or Fink in $PATH will refuse to build. Also note that the libpng update at #5217 will fix the problem in a different way.

Cheers,

Michael
