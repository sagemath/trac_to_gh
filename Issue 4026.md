# Issue 4026: [with spkg, needs review] Move Macaulay2  to latest upstream

Issue created by migration from https://trac.sagemath.org/ticket/4026

Original creator: gfurnish

Original creation time: 2008-08-31 23:39:33

Assignee: mabshoff

This spkg removes the patches from #3926.
It updates upstream to r7221 of the 1.1 branch.
It also solves a build issue under gcc 4.3.1.

Download at http://sage.math.washington.edu/home/gfurnish/spkg/macaulay2-1.1-r7221.spkg


---

Comment by malb created at 2008-09-01 09:24:15

The spkg looks good, except that the HG repository has uncommitted changes.


---

Comment by gfurnish created at 2008-09-03 02:40:36

New spkg at same location with committed changes.


---

Comment by malb created at 2008-09-03 09:26:16

Good to go.


---

Comment by mabshoff created at 2008-09-03 15:47:39

Merged the spkg in the experimental spkg repo.

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-03 15:47:39

Resolution: fixed
