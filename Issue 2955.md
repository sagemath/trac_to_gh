# Issue 2955: GFortran autodection on Linux/Itanium

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-04-19 04:03:42

Assignee: mabshoff

We do not ship any Fortran compiler for Linux/Itanium. Since any reasonable distribution on Itanium ships GFortran automate detection for that special case. With this ticket, #2953 and 2954 Sage 3.0 should build out of the box on SageNet's RHEL 5 and SLES 10 Itanium test boxen.

Cheers,

Michael


---

Comment by mabshoff created at 2008-04-19 04:03:49

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-04-20 06:32:46

#1642 does fix most of the problem already, but on some Itanium systems [RHEL 5 for example] there is no libgfortran.so, only a libgfortran.so.1.

Cheers,

Michael


---

Comment by mabshoff created at 2008-04-20 10:13:56

I added some more verbose output, check the arch flag for also i[345]86 [which like could cause bugs on some other systems, check for libgfortran.so[.1] relative to gfortran and link that lib into SAGE_LOCAL/lib. This makes the fortran.spkg work out of the box on RHEL 5/Itanium.

Cheers,

Michael


---

Comment by mabshoff created at 2008-04-20 10:19:55

The updated spkg is at

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.0/rc0/fortran-20071120.p4.spkg

Sorry wjp ;)

Cheers,

Michael


---

Comment by mabshoff created at 2008-04-20 10:51:21

Merged in Sage 3.0.rc0


---

Comment by mabshoff created at 2008-04-20 10:51:21

Resolution: fixed
