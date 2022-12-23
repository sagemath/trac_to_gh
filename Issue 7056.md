# Issue 7056: Fix build issues so Sage builds with the Sun Studio Compiler suite.

Issue created by migration from https://trac.sagemath.org/ticket/7056

Original creator: drkirkby

Original creation time: 2009-09-28 20:23:10

Assignee: tbd

CC:  chapoton

Sun's compiler on Solaris produces faster code than gcc, and is more reliable with 64-bit code than gcc. This ticket outlines the issues that need to be resolved to get Sage to build on Sun Studio, and are specific to Sun Studio. As more are discovered, I'll add them to the description, so it's easy to them all, rather than find them buried well down the page. 

In many cases, the bugs can potentially affect all compilers, but are only observed on Sun Studio. 

The hostname of at least one machine 

|          |          |           |      |       |       |              |            |        |
|----------|----------|-----------|------|-------|-------|--------------|------------|--------|
|*Hostname*|*Hardware*|*Processor*|*CPUs*|*Cores*|*Speed*|*Architecture*|*OS version*|Compiler|
|swan|Sun Blade 2000|UltraSPARC-III+|2|2|1200 MHz|sun4u|Solaris 10 update 7|Sun Studio 12.1|
|t2|Sun T5240|SPARC T2+|2|16|1167 MHz|sun4v|Solaris 10 update 7|Sun Studio 12|
|main-webserver|Sun Ultra 60|UltraSPARC-II|2|2| 450 MHz |sun4u|Solaris 10 update 4||

The actual bugs found, along with the trac number are listed below. The hostname is marked as N/A if they are expected to be seen on any Solaris host, but if they are only expected to be seen on some hosts, then the hostname on which the bug was found are listed. 

|             |          |        |         |
|-------------|----------|--------|---------|
|*Description*|*hostname*|*Trac #*|*Note(s)*|
|                             ||     | |
|-----------------------------||-----|-|
|Update prereq from 0.3 to 0.4||#7021|1|
|zn_poly-0.9 uses gcc, irrespective of setting of CC||#7039|2|
|symmetrica ignores CC||#7032|2|
|ATLAS ignores CC variable, then dumps core when trying to build with Sun Studio on Solaris|swan|#7048|2,3|
|Flint ignores CC and CXX||#7024|2|
|lapack sends GNU option -fPIC to Sun fortran compiler||#7047||
|eclib 20080310.p7 has code Sun's C++ compiler does not understand||#7044||
|Code actually in Sage (not other project) ignores CC and uses gcc||#7040|2|
|ntl 5.4.2.p9 passes -fPIC to Sun linker with Sun Studio||#7043||
|givaro 3.2.13rc2 says GMP is not installed, even though MPIR is|swan|#7025|4,5|
|linbox 1.1.6.p0 says GMP is not installed, even though MPIR is|swan|#7026|4,5|
|R sends the correct Sun flags to C and C++ compilers, but not Fortran||#7035||
|GAP purposely unsets CC which screws up Sun Studio build||#7041|6|
|libm4ri thinks the C compiler is broken|swan|#7037||
|rubiks ignroes CXX and uses g++ even if CXX is Sun compiler||#7036||
|ratpoints 2.1.2.p2 ignores CC and uses gcc whatever||#7038|2|
|ibfplll can't find _gmpz_init in -lgmp||#7033|5|
*Notes*

1) This update should have benefits to Sage on any platform, with any compiler. It is however *absolutely essential* this is fixed for Sun Studio. 

2) Although discovered when testing with Sun Studio, the bug relates to the failure of a program to properly observe CC, CXX or SAGE_FORTRAN, so it can be expected to exist with any compiler.

3) The core dump was observed on hostname 'swan'. The failure to observe CC can be expected on any platform, but dumping core may be only on this machine. 

4) Checked only on the hostname. This may or may not be specific to that machine.

5) Tickets #7025, #7026 and #7033 are very closely related, as they all relate to a failure of a program to reconsise GMP being installed. Of course, it is not installed, but MPIR is, which is a substitute. 

6) Although easy to fix, to do some introduces a major impact on the time to build Sage.


---

Comment by mkoeppe created at 2020-04-01 14:10:32

Should be closed as outdated.


---

Comment by mkoeppe created at 2020-04-01 14:10:32

Changing status from new to needs_review.


---

Comment by chapoton created at 2020-04-01 14:21:31

Resolution: invalid


---

Comment by chapoton created at 2020-04-01 14:21:31

agreed again
