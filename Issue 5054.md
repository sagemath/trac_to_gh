# Issue 5054: add support for doctesting worksheets

Issue created by migration from Trac.

Original creator: mhansen

Original creation time: 2009-01-22 13:05:57

Assignee: mabshoff

If we want to ship a collection of worksheets in the future, we need some way to doctest them.

One solution would be to go through a worksheet text file, run through the cells, and make sure newly computed output matches up with the output stored in the file.


---

Comment by mabshoff created at 2009-02-06 22:59:44

3.4 is for ReST tickets only.

Cheers,

Michael


---

Comment by jhpalmieri created at 2009-07-22 03:32:52

This is a duplicate of #116.  Please close it.


---

Comment by mvngu created at 2009-08-12 07:32:36

Resolution: duplicate
