# Issue 9986: Shared readline library uses a .so extension on AIX when it should be .a

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2010-09-23 21:20:05

Assignee: drkirkby

Using the following system: 

 * IBM [RS/6000 7025 F50](http://publib.boulder.ibm.com/infocenter/pseries/v5r3/index.jsp?topic=/com.ibm.pseries.doc/hardware_docs/rs6000_7025f50series.htm)
 * 4 x 332 MHz 32-bit PowerPC CPUs
 * 3 GB RAM
 * A fair wide mixture of disks sizes (3 x 9 GB, 1 x 18 GB, 2 x 36 GB and 1 x 73 GB)
 * DDS-4 tape drive 
 * AIX 5.3 (A POSIX certified operating system)
 * gcc 4.2.4 downloaded from [pware](http://pware.hvcc.edu/)
 * sage-4.6.alpha1

Readline builds, but then if we look at the libraries, one has the wrong extension. 


```
-bash-4.1$ ls -l local/lib/libreadline*
-rwxr-xr-x   1 drkirkby staff       1739661 23 Sep 15:43 local/lib/libreadline.a
lrwxrwxrwx   1 drkirkby staff            16 23 Sep 15:43 local/lib/libreadline.so -> libreadline.so.6
-rwxr-xr-x   1 drkirkby staff       1145940 23 Sep 15:43 local/lib/libreadline.so.6
-bash-4.1$ 
-bash-4.1$ 
-bash-4.1$ file local/lib/libreadline.a     local/lib/libreadline.so    local/lib/libreadline.so.6
local/lib/libreadline.a: archive (big format)
local/lib/libreadline.so: executable (RISC System/6000) or object module not stripped
local/lib/libreadline.so.6: executable (RISC System/6000) or object module not stripped

```


I don't know AIX well, but I suspect the .a is a static library here, and the .so is a shared library. But AIX uses .a for shared libraries. (I don't know what it uses for static libraries - it might be .o). 

This is probably a mis-configuration in Sage. 

Dave 


---

Comment by drkirkby created at 2011-03-22 17:37:19

It appears AIX uses .a for both shared and static libs. But it understands .so too, so this can be closed as invalid.


---

Comment by chapoton created at 2014-10-21 14:49:41

Can this be closed ?


---

Comment by chapoton created at 2014-10-21 14:49:41

Changing status from new to needs_review.


---

Comment by vbraun created at 2014-10-25 21:45:58

Resolution: invalid


---

Comment by fbissey created at 2014-10-26 05:49:04

While this is now closed I should add a couple of comments. AIX doesn't use elf format but xcoff (google it). The .a from aix can contain both static and dynamic libraries. They also can contain both 32 and 64bit objects all at the same type. The linker works out what it needs at linking time.
".so" linux style shared libraries are allowed with recent linkers of AIX (I don't know if it extends as far back as AIX 5.3 it is definitely in 6.1) but you need to know the extra linking flags to use them "-G" and "-brtl" depending on the case. It is all pretty dangerous and it is best to leave the task of making the libraries to libtool if possible.
