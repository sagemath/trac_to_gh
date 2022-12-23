# Issue 8247: Remove package GLPK 3.9

Issue created by migration from https://trac.sagemath.org/ticket/8247

Original creator: ncohen

Original creation time: 2010-02-12 08:41:56

Assignee: tbd

CC:  mvngu

Experimental package glpk 4.9 should be removed

 * We have a more recent version of GLPK (v 4.38)
 * No one seems to know who is the package maintainer of 4.9
 * there does not seem to be any reason for having 2 different GLPK packages as 4.9 only contains glpk and no custom code... 

Nathann


---

Comment by mvngu created at 2010-02-14 16:40:43

Fixed by removing `glpk-4.9.spkg` from the [experimental packages](http://www.sagemath.org/packages/experimental/) repository.


---

Comment by mvngu created at 2010-02-14 16:40:43

Resolution: fixed
