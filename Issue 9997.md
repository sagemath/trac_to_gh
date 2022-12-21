# Issue 9997: NTL is building the shared library with the wrong extension on AIX

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2010-09-24 02:33:06

Assignee: drkirkby

CC:  chapoton

## Hardware and software
 * IBM [RS/6000 7025 F50](http://publib.boulder.ibm.com/infocenter/pseries/v5r3/index.jsp?topic=/com.ibm.pseries.doc/hardware_docs/rs6000_7025f50series.htm)
 * 4 x 332 MHz 32-bit PowerPC CPUs
 * 3 GB RAM
 * A fairly wide mixture of disks sizes (3 x 9 GB, 1 x 18 GB, 2 x 36 GB and 1 x 73 GB)
 * DDS-4 tape drive 
 * AIX 5.3 (A POSIX certified operating system)
 * gcc 4.2.4 downloaded from [pware](http://pware.hvcc.edu/)
 * sage-4.6.alpha1 (which has ntl-5.4.2.p12)


```
bash-4.1$ ls -l local/lib/libntl*
-rwxr-xr-x   1 drkirkby staff      26740371 23 Sep 18:12 local/lib/libntl-5.4.2.so
-rw-r--r--   1 drkirkby staff      29165744 23 Sep 18:12 local/lib/libntl.a
lrwxrwxrwx   1 drkirkby staff            15 23 Sep 18:12 local/lib/libntl.so -> libntl-5.4.2.so
```



```
-bash-4.1$ file local/lib/libntl*
local/lib/libntl-5.4.2.so: executable (RISC System/6000) or object module not stripped
local/lib/libntl.a: archive (big format)
local/lib/libntl.so: executable (RISC System/6000) or object module not stripped
-bash-4.1$ 
```



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

Comment by chapoton created at 2020-06-25 13:34:28

Resolution: invalid
