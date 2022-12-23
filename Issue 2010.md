# Issue 2010: crap -- libpng contains lots and lots of weird (OS X?) temp or meta files

Issue created by migration from https://trac.sagemath.org/ticket/2010

Original creator: was

Original creation time: 2008-01-31 23:21:33

Assignee: mabshoff


```
sage-2.10.1.rc3/spkg/standard/libpng-1.2.22.p3/src/._Y2KINFO
sage-2.10.1.rc3/spkg/standard/libpng-1.2.22.p3/src/._TODO
sage-2.10.1.rc3/spkg/standard/libpng-1.2.22.p3/src/._test-pngtest.sh
sage-2.10.1.rc3/spkg/standard/libpng-1.2.22.p3/src/scripts/._smakefile.ppc
sage-2.10.1.rc3/spkg/standard/libpng-1.2.22.p3/src/scripts/._SCOPTIONS.ppc
sage-2.10.1.rc3/spkg/standard/libpng-1.2.22.p3/src/scripts/._pngw32.rc
sage-2.10.1.rc3/spkg/standard/libpng-1.2.22.p3/src/scripts/._pngw32.def
sage-2.10.1.rc3/spkg/standard/libpng-1.2.22.p3/src/scripts/._pngos2.def
sage-2.10.1.rc3/spkg/standard/libpng-1.2.22.p3/src/scripts/._makevms.com
sage-2.10.1.rc3/spkg/standard/libpng-1.2.22.p3/src/scripts/._makefile.watcom
sage-2.10.1.rc3/spkg/standard/libpng-1.2.22.p3/src/scripts/._makefile.vcwin32
sage-2.10.1.rc3/spkg/standard/libpng-1.2.22.p3/src/scripts/._makefile.vcawin32
...
AND MANY MORE
```



---

Comment by mabshoff created at 2008-01-31 23:49:41

The updated spkg at

http://sage.math.washington.edu/home/mabshoff/release-cycles-2.10.1/rc4/libpng-1.2.22.p4.spkg

removes the offending files.

Cheers,

Michael


---

Comment by mabshoff created at 2008-01-31 23:51:24

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-02-01 02:01:14

Resolution: fixed


---

Comment by mabshoff created at 2008-02-01 02:01:14

Merged in Sage 2.10.1.rc4
