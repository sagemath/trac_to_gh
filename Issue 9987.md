# Issue 9987: zlib 1.2.5 installs zlib library with a .so extension on AIX when it should be .a

Issue created by migration from https://trac.sagemath.org/ticket/9988

Original creator: drkirkby

Original creation time: 2010-09-23 21:29:55

Assignee: drkirkby

CC:  madler@alumni.caltech.edu chapoton

I'm cc'ing Mark Adler on this, as he is the maintainer of the zlib package. It would appear that zlib is building the shared library with the wrong extension on AIX. Rather unconventionally, AIX uses .a for shared libraries. 

If Mark needs access to an AIX machine, I can the following:


 * IBM [RS/6000 7025 F50](http://publib.boulder.ibm.com/infocenter/pseries/v5r3/index.jsp?topic=/com.ibm.pseries.doc/hardware_docs/rs6000_7025f50series.htm)
 * 4 x 332 MHz 32-bit PowerPC CPUs
 * 3 GB RAM
 * A fair wide mixture of disks sizes (3 x 9 GB, 1 x 18 GB, 2 x 36 GB and 1 x 73 GB)
 * DDS-4 tape drive 
 * AIX 5.3 (A POSIX certified operating system)
 * gcc 4.2.4 downloaded from [pware](http://pware.hvcc.edu/)
 * sage-4.6.alpha1


```
-bash-4.1$ ls -l local/lib/libz*       
-rw-r--r--   1 drkirkby staff        123336 23 Sep 15:37 local/lib/libz.a
lrwxrwxrwx   1 drkirkby staff            13 23 Sep 15:37 local/lib/libz.so -> libz.so.1.2.5
lrwxrwxrwx   1 drkirkby staff            13 23 Sep 15:37 local/lib/libz.so.1 -> libz.so.1.2.5
-rwxr-xr-x   1 drkirkby staff        393465 23 Sep 15:37 local/lib/libz.so.1.2.5
```




---

Comment by embray created at 2019-01-15 18:39:07

I don't believe anyone's been maintaining support for AIX or HP-UX for some time.  Putting in sage-wishlist for now in case there is still a desire for it out there, otherwise these tickets should be closed (most of them are probably no longer relevant in any case but I have no obvious way to check this).


---

Comment by mkoeppe created at 2020-06-23 21:26:55

Changing status from new to needs_review.


---

Comment by mkoeppe created at 2020-06-23 21:26:55

We should close this ticket as outdated.


---

Comment by chapoton created at 2020-06-25 13:33:35

Resolution: invalid
