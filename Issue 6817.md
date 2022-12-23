# Issue 6817: [with SPKG, needs review] GLPK for Sage, new version

Issue created by migration from https://trac.sagemath.org/ticket/6817

Original creator: ncohen

Original creation time: 2009-08-24 09:38:08

Assignee: tbd

CC:  mvngu

New version of package GLPK for Sage. There is nothing new except that this spkg now embeds the function solveGLPK which was previously included directly into Sage ( stupid, as this is to be an optional package ).
Hence, this code has already been positively reviewed in #6502

As with package COIN-OR/CBC, the function is now compiled when the package is installed, then loaded by sage.numerical.mip when solve() is called.

The package can be installed this way

```
sage -f http://www-sop.inria.fr/members/Nathann.Cohen/glpk-4.38.spkg
}}]


---

Comment by ncohen created at 2009-08-25 09:01:46

Changing component from optional packages to packages.


---

Comment by ncohen created at 2009-08-25 09:01:46

Changing assignee from tbd to mabshoff.


---

Comment by wdj created at 2009-08-25 17:51:01

I tested this as before (with #6502). It applies fine to 4.1.1.rc2 in an intel macbook running 10..4.11 ( I could not get 4.1.1 to compile from source on that platform), so positive review from me again.


---

Comment by mvngu created at 2009-09-02 16:08:40

Resolution: fixed


---

Comment by mvngu created at 2009-09-02 16:08:40

ncohen --- In future updates to the GLPK spkg, please put your custom patches, .pyx, or .pxd files under a directory called `patch`.



Merged the updated spkg in the optional packages repository. See this web page



http://www.sagemath.org/packages/optional/



The download link is



http://www.sagemath.org/packages/optional/glpk-4.38.p0.spkg


---

Comment by mvngu created at 2009-09-03 09:45:16

Changing component from packages to optional packages.
