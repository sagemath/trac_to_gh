# Issue 7413: cython mode is whitespace-sensitive

Issue created by migration from https://trac.sagemath.org/ticket/7413

Original creator: mhampton

Original creation time: 2009-11-08 20:17:12

Assignee: boothby

If a notebook cell has the header "%cython " it produces an error (as opposed to "%cython" with no trailing whitespace).  


---

Comment by was created at 2009-11-09 02:03:33

Resolution: duplicate


---

Comment by was created at 2009-11-09 02:03:33

This is a dupe of #5324.
