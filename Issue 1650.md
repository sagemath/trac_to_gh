# Issue 1650: eclib-20071231.p0.spkg: fix tsat test failure on sage.math

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-01-01 00:04:05

Assignee: cremona

When running `make check` for eclib-20071231.p0.spkg on sage.math it fails with exit code 134:

```
./tsat < tsat.in > t 2>/dev/null && diff t tsat.out
/bin/sh: line 1: 13769 Aborted                 ./tsat <tsat.in >t 2>/dev/null
make[1]: *** [check] Error 134
```

In detail:

```
verbose (0/1)?
Input a curve: Curve [0,0,1,-7,36]
enter number of points:
  enter point 1 :
  enter point 2 :
  enter point 3 :
  enter point 4 : 4 points entered.
prime p to saturate at?
Saturating at prime 11
Original generators:
[ [1:-6:1] [-30:21:8] [-3:5:1] [-2:6:1] ]
Finished p-saturation for p =  11, points were saturated
fatal error:
   corrupted memory detected in _ntl_gblock_destroy
exit...
Aborted
```

Valgrind says:

```

[ [1:-6:1] [-30:21:8] [-3:5:1] [-2:6:1] ]
Finished p-saturation for p =  11, points were saturated
==13794== Invalid read of size 8
==13794==    at 0x54A2E0C: NTL::vec_ZZ_p::~vec_ZZ_p() (in /tmp/Work-mabshoff/release-cycle/sage-2.9.1.1/local/lib/libntl.so)
==13794==    by 0x5C22E0B: __cxa_finalize (in /lib/libc-2.3.6.so)
==13794==    by 0x4B35782: (within /tmp/Work-mabshoff/release-cycle/sage-2.9.1.1/local/lib/libcurvesntl.so)
==13794==    by 0x4C05E00: (within /tmp/Work-mabshoff/release-cycle/sage-2.9.1.1/local/lib/libcurvesntl.so)
==13794==    by 0x5C22B8C: exit (in /lib/libc-2.3.6.so)
==13794==    by 0x5C0D4D0: (below main) (in /lib/libc-2.3.6.so)
==13794==  Address 0x66761e0 is 16 bytes inside a block of size 64 free'd
==13794==    at 0x4A1B74A: free (vg_replace_malloc.c:320)
==13794==    by 0x5C22B8C: exit (in /lib/libc-2.3.6.so)
==13794==    by 0x5C0D4D0: (below main) (in /lib/libc-2.3.6.so)
==13794==
==13794== Invalid read of size 8
==13794==    at 0x54A2D91: NTL::BlockDestroy(NTL::ZZ_p*, long) (in /tmp/Work-mabshoff/release-cycle/sage-2.9.1.1/local/lib/libntl.so)
==13794==    by 0x54A2E14: NTL::vec_ZZ_p::~vec_ZZ_p() (in /tmp/Work-mabshoff/release-cycle/sage-2.9.1.1/local/lib/libntl.so)
==13794==    by 0x5C22E0B: __cxa_finalize (in /lib/libc-2.3.6.so)
==13794==    by 0x4B35782: (within /tmp/Work-mabshoff/release-cycle/sage-2.9.1.1/local/lib/libcurvesntl.so)
==13794==    by 0x4C05E00: (within /tmp/Work-mabshoff/release-cycle/sage-2.9.1.1/local/lib/libcurvesntl.so)
==13794==    by 0x5C22B8C: exit (in /lib/libc-2.3.6.so)
==13794==    by 0x5C0D4D0: (below main) (in /lib/libc-2.3.6.so)
==13794==  Address 0x66761f0 is 32 bytes inside a block of size 64 free'd
==13794==    at 0x4A1B74A: free (vg_replace_malloc.c:320)
==13794==    by 0x5C22B8C: exit (in /lib/libc-2.3.6.so)
==13794==    by 0x5C0D4D0: (below main) (in /lib/libc-2.3.6.so)
[SNIP]
```

This points potentially to another issue in template.h. If I have some more time I will investigate later.

Cheers,

Michael


---

Comment by mabshoff created at 2008-01-27 03:20:36

The spkg at #1649 should fix this. But that needs to be verified.


---

Comment by was created at 2008-01-27 18:44:02

New version that builds on OS X:
 http://sage.math.washington.edu/home/was/tmp/eclib-20071231.p2.spkg


---

Comment by was created at 2008-01-27 18:55:34

New version that passes spkg-check on OS X as well:

http://sage.math.washington.edu/home/was/tmp/eclib-20080127.spkg

I upped the release version number, since Cremona and I made changes
inside the src/ directory (which we dutifully checked in).


---

Comment by mabshoff created at 2008-01-27 19:54:09

The spkg fixes the issue and the check target now passes all test on sage.math.

Cheers,

Michael


---

Comment by mabshoff created at 2008-01-27 19:54:24

Resolution: fixed


---

Comment by mabshoff created at 2008-01-27 19:54:24

Merged in Sage 2.10.1.rc2
