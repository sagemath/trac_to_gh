# Issue 244: linbox into SAGE

Issue created by migration from https://trac.sagemath.org/ticket/244

Original creator: was

Original creation time: 2007-02-05 01:51:04

Assignee: was

Bug problems:

  1. Find a way to turn off their very verbose output in some cases.  (The documented ways don't work.)
  2. Fix / investigate bug where charpoly hangs (see matrix2.pyx).  Or turn off using linbox by default for charpoly, since it's flake.  Or reimplement myself...
  
What will be included in the first release:
  * Fast dense echelon over QQ (via multimodular algorithm?)
  * (done) Fast minpoly over QQ
  * (done) Fast charpoly over QQ
  * Fast dense matrix multiply over Z/nZ
  * Fast sparse matrix multiply over Z/nZ
  * Fast minpoly over Z/nZ
  * Fast charpoly over Z/nZ


---

Comment by malb created at 2007-08-10 19:28:00

Resolution: fixed


---

Comment by malb created at 2007-08-10 19:28:00

LinBox was included a while ago.
