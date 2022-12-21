# Issue 6347: use faster 2^m^ implementation up to 2^62^ on 64-bit systems

Issue created by migration from Trac.

Original creator: malb

Original creation time: 2009-06-17 15:32:55

Assignee: malb

Keywords: singular

It turns out the bug discussed at #6051 and

  http://www.singular.uni-kl.de:8002/trac/ticket/138

is not an upstream bug but a problem in our conversion. Fix it!


---

Comment by malb created at 2009-09-09 19:46:16

Resolution: wontfix


---

Comment by malb created at 2009-09-09 19:46:16

I turns out  that the assumption above is wrong. There are a couple of places in the Singular code where int is assumed so this ticket cannot be implemented unless Singular changes.
