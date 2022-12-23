# Issue 5203: [with spkg, needs review] Update mpir to 0.9.rc3 release [latest upstream]

Issue created by migration from https://trac.sagemath.org/ticket/5203

Original creator: mabshoff

Original creation time: 2009-02-08 01:10:15

Assignee: mabshoff

The spkg at

 
updates the gmp-mpir.spkg to latest upstream. For now the test suite is invoked automatically. It passes on

SkyNet:

 * eno (x86_64, FC9)
 * mark (Sparc, Solaris)
 * fulvia (x86, Solaris)
 * cicero (x86, FC9)
 * menas (x86_64, OpenSUSE 10.3)
 * iras (Itanium, SLES 10)
 * cleo (Itanium, RHEL 5.2)
 * varro (PPC, OSX 10.4)

Misc machines:

 * bsd (x86, OSX 10.5)
 * sage.math (x86_64, Ubuntu LTS 8.04)
 * sprocketer (x86-64, OSX 10.5)

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-08 01:10:46

Changing status from new to assigned.


---

Comment by mhansen created at 2009-02-08 01:48:12

Looks good.  Passes all tests for me.


---

Comment by mabshoff created at 2009-02-08 01:58:34

Merged in Sage 3.3.alpha6.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-08 01:58:34

Resolution: fixed
