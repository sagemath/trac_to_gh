# Issue 5202: [with spkg, needs review] update MPFR to 2.4.0 (latest upstream)

Issue created by migration from https://trac.sagemath.org/ticket/5202

Original creator: mabshoff

Original creation time: 2009-02-08 01:08:28

Assignee: mabshoff

CC:  zimmerma

The spkg at

 http://sage.math.washington.edu/home/mabshoff/release-cycles-3.3/alpha6/mpfr-2.4.0.spkg

updates the mpfr.spkg to latest upstream. For now the test suite is invoked automatically. It passes on

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

with MPIR-0.9.rc3, which will be updated via a separate ticket.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-08 01:08:46

Changing status from new to assigned.


---

Comment by mabshoff created at 2009-02-08 01:11:37

Paul,

I can supply you with the config.guess output of all the machines above in case you want it for the MPFR website. I can also test on MIPS64/Linux.

Cheers,

Michael


---

Comment by mhansen created at 2009-02-08 01:48:35

Looks good.  Passes all tests for me.


---

Comment by mabshoff created at 2009-02-08 01:58:48

Resolution: fixed


---

Comment by mabshoff created at 2009-02-08 01:58:48

Merged in Sage 3.3.alpha6.

Cheers,

Michael


---

Comment by zimmerma created at 2009-02-08 09:47:17

> I can supply you with the config.guess output of all the machines above in case you want it for the MPFR website. I can also test on MIPS64/Linux.

yes please supply it for configurations not already listed for mpfr-2.4.0.

Paul
