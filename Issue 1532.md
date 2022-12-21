# Issue 1532: Error out with intelligent message if ATLAS tune failed

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2007-12-16 03:34:00

Assignee: jkantor

On a loaded machine ATLAS tends to report the following

```
VARIATION EXCEEDS TOLERENCE, RERUN WITH HIGHER REPS.
```

It then errors out:

```
Thread model: posix
gcc version 4.1.2 20061115 (prerelease) (Debian 4.1.1-21)
gcc -V 2>&1  >> bin/INSTALL_LOG/ERROR.LOG
gcc: '-V' option must have argument
make[6]: [error_report] Error 1 (ignored)
gcc --version 2>&1  >> bin/INSTALL_LOG/ERROR.LOG
tar cf error_HAMMER64SSE3.tar Make.inc bin/INSTALL_LOG/*
gzip --best error_HAMMER64SSE3.tar
mv error_HAMMER64SSE3.tar.gz error_HAMMER64SSE3.tgz
make[6]: Leaving directory `/home/rlmill/sage-2.9.rc2/spkg/build/atlas-3.8.p5/ATLAS-build'
make[5]: Leaving directory `/home/rlmill/sage-2.9.rc2/spkg/build/atlas-3.8.p5/ATLAS-build'
make[4]: Leaving directory `/home/rlmill/sage-2.9.rc2/spkg/build/atlas-3.8.p5/ATLAS-build/bin'
Error report error_<ARCH>.tgz has been created in your top-level ATLAS
directory.  Be sure to include this file in any help request.
cat: ../../CONFIG/error.txt: No such file or directory
cat: ../../CONFIG/error.txt: No such file or directory


IN STAGE 1 INSTALL:  SYSTEM PROBE/AUX COMPILE
```

But the build of Sage goes on and fails down the road.

Cheers,

Michael


---

Comment by mabshoff created at 2007-12-16 04:51:47

Resolution: fixed


---

Comment by mabshoff created at 2007-12-16 04:51:47

Merged in 2.9.rc3. Updated in atlas-3.8.p6.spkg
