# Issue 9984: Freetype fails to build on AIX - looks as though it does not find Sage's zlib header files.

Issue created by migration from https://trac.sagemath.org/ticket/9985

Original creator: drkirkby

Original creation time: 2010-09-23 20:51:00

Assignee: drkirkby

CC:  chapoton

Using the following system: 

 * IBM [RS/6000 7025 F50](http://publib.boulder.ibm.com/infocenter/pseries/v5r3/index.jsp?topic=/com.ibm.pseries.doc/hardware_docs/rs6000_7025f50series.htm)
 * 4 x 332 MHz 32-bit PowerPC CPUs
 * 3 GB RAM
 * A fair wide mixture of disks sizes (3 x 9 GB, 1 x 18 GB, 2 x 36 GB and 1 x 73 GB)
 * AIX 5.3 (A POSIX certified operating system)
 * gcc 4.2.4 downloaded from [pware](http://pware.hvcc.edu/)
 * DDS-4 tape drive 

FreeType fails to build, but reports:


```
kby/sage-4.6.alpha1/spkg/build/freetype-2.3.5.p2/src/src/lzw/ftlzw.c
In file included from /home/users/drkirkby/sage-4.6.alpha1/spkg/build/freetype-2.3.5.p2/src/src/gzip/ftgzip.c:45:
/opt/pware/include/zlib.h:1585: error: expected '=', ',', ';', 'asm' or '__attribute__' before 'gzseek'
/opt/pware/include/zlib.h:1586: error: expected '=', ',', ';', 'asm' or '__attribute__' before 'gztell'
/opt/pware/include/zlib.h:1587: error: expected '=', ',', ';', 'asm' or '__attribute__' before 'gzoffset'
/opt/pware/include/zlib.h:1588: error: expected declaration specifiers or '...' before 'off_t'
/opt/pware/include/zlib.h:1589: error: expected declaration specifiers or '...' before 'off_t'
```


I can't understand why this is using the header files from `/opt/pware/include/` when it should be using the header file from `$SAGE_LOCAL/local/include/zlib.h`


---

Attachment

Build failure observed on an RS/6000 running AIX 5.3


---

Comment by drkirkby created at 2010-09-23 20:55:14

Changing priority from major to minor.


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

Comment by chapoton created at 2020-06-25 13:33:03

Resolution: invalid
