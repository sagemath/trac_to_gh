# Issue 9995: Flint is installing shared library with .so extension on AIX - it should be .a on AIX

Issue created by migration from https://trac.sagemath.org/ticket/9996

Original creator: drkirkby

Original creation time: 2010-09-24 02:17:14

Assignee: drkirkby

CC:  goodwillhart@googlemail.com jpflori chapoton

## Hardware and software
 * IBM [RS/6000 7025 F50](http://publib.boulder.ibm.com/infocenter/pseries/v5r3/index.jsp?topic=/com.ibm.pseries.doc/hardware_docs/rs6000_7025f50series.htm)
 * 4 x 332 MHz 32-bit PowerPC CPUs
 * 3 GB RAM
 * A fairly wide mixture of disks sizes (3 x 9 GB, 1 x 18 GB, 2 x 36 GB and 1 x 73 GB)
 * DDS-4 tape drive 
 * AIX 5.3 (A POSIX certified operating system)
 * gcc 4.2.4 downloaded from [pware](http://pware.hvcc.edu/)
 * sage-4.6.alpha1 

## The problem
Flint builds ok (see attached log), but the shared library has the wrong extension.


```
-bash-4.1$ ls local/lib/*flint*
local/lib/libflint.so
-bash-4.1$ file local/lib/libflint.so
local/lib/libflint.so: executable (RISC System/6000) or object module not stripped
```


This is not normal on AIX, where the extension for both shared and archive libraries should be `.a` and not `.so`. See 
[IBM compiler manual](http://publib.boulder.ibm.com/infocenter/comphelp/v7v91/index.jsp?topic=/com.ibm.vacpp7a.doc/getstart/overview/port_aix_obj_lib.htm) and [notes on GCC on AIX](http://www.ibm.com/developerworks/aix/library/au-gnu.html) 



---

Comment by wbhart created at 2012-06-01 18:21:19

Can you give me the uname -m or uname -a or whatever will tell me this is an AIX machine. It's only a single line in the flint makefile to fix this.

I assume it is flint 1.6.


---

Comment by embray created at 2019-01-15 18:39:07

I don't believe anyone's been maintaining support for AIX or HP-UX for some time.  Putting in sage-wishlist for now in case there is still a desire for it out there, otherwise these tickets should be closed (most of them are probably no longer relevant in any case but I have no obvious way to check this).


---

Comment by mkoeppe created at 2020-06-23 21:26:55

We should close this ticket as outdated.


---

Comment by mkoeppe created at 2020-06-23 21:26:55

Changing status from new to needs_review.


---

Comment by chapoton created at 2020-06-25 13:34:01

Resolution: invalid
