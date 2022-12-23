# Issue 9992: Singular fails to build on AIX 5.3

Issue created by migration from https://trac.sagemath.org/ticket/9993

Original creator: drkirkby

Original creation time: 2010-09-24 00:39:19

Assignee: drkirkby

CC:  jdemeyer

Singular is not building properly on the following hardware. If any Singular developer wants access to AIX to debug this, I can provide it. 

 == Hardware and software ==
 * IBM [RS/6000 7025 F50](http://publib.boulder.ibm.com/infocenter/pseries/v5r3/index.jsp?topic=/com.ibm.pseries.doc/hardware_docs/rs6000_7025f50series.htm)
 * 4 x 332 MHz 32-bit PowerPC CPUs
 * 3 GB RAM
 * A fairly wide mixture of disks sizes (3 x 9 GB, 1 x 18 GB, 2 x 36 GB and 1 x 73 GB)
 * DDS-4 tape drive 
 * AIX 5.3 (A POSIX certified operating system)
 * gcc 4.2.4 downloaded from [pware](http://pware.hvcc.edu/)
 * sage-4.6.alpha1 (which has singular-3-1-1-4.p2)

 == The Problem ==
As note, Singular fails to build. I see this _error_ a couple of times, but it does not abort the build. 


```
/opt/pware/lib/gcc/powerpc-ibm-aix5.3.0.0/4.2.4/../../../../include/c++/4.2.4/bits/ios_base.h:187: error: 'SEEK_CUR' was not declared in this scope
```


If eventually ends with:


```
polys-impl.h:177:1: warning: "pPolyAssumeReturn" redefined
polys-impl.h:176:1: warning: this is the location of the previous definition
make[4]: Target `install' not remade because of errors.
make[4]: Leaving directory `/home/users/drkirkby/sage-4.6.alpha1/spkg/build/singular-3-1-1-4.p2/src/kernel'
make[3]: *** [install] Error 1
make[3]: Leaving directory `/home/users/drkirkby/sage-4.6.alpha1/spkg/build/singular-3-1-1-4.p2/src'
make[2]: *** [/home/users/drkirkby/sage-4.6.alpha1/local/bin/Singular-3-1-1] Error 2
make[2]: Leaving directory `/home/users/drkirkby/sage-4.6.alpha1/spkg/build/singular-3-1-1-4.p2/src'
Unable to build Singular.

real    120m55.494s
user    164m57.036s
sys     2m3.365s
sage: An error occurred while installing singular-3-1-1-4.p2
```



---

Comment by jmantysalo created at 2016-09-02 08:05:55

Changing status from new to needs_review.


---

Comment by jmantysalo created at 2016-09-02 08:05:55

Refers to old AIX and old Singular --> close?


---

Comment by jdemeyer created at 2016-09-02 08:35:52

Resolution: invalid
