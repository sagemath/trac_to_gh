# Issue 1252: 2.8.13: gmp related build problems on OSX 10.4.11, 10.5.1

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2007-11-24 00:23:16

Assignee: mabshoff

Justin Walker reported:

```
I did a full build of 2.8.13 on two systems:

Mac OS X/10.4.11: Dual Quad-Core Xeon
Mac OS X/10.5.1:  Core Duo

Problems on both:
10.5.1: blow-up in Flint
   ld: duplicate symbol ___gmpz_abs in test-support.o and fmpz_poly-
test.o

10.4.11: blow-up in cddlib ("/usr/local" contamination)
   /usr/libexec/gcc/i686-apple-darwin8/4.0.1/ld: Undefined symbols:
   ___gmpq_init
   ...

FWIW, I used "-j6" on the 10.4 system and "-j2" on the 10.5 system.  
Rerunning the builds without the "j factor" gave me the (more or  
less) the same result on 10.4 and 10.5.

The full logs (of the "-j" builds) are in ~justin/logs on  
sage.math.washington.edu (tagged with 10.x).

Justin 
```


See http://groups.google.com/group/sage-devel/t/8e446357a1d15a8a

Cheers,

Michael


---

Comment by mabshoff created at 2007-11-24 01:54:14

A potential solution for the 10.4.11 issue can be found at

http://sage.math.washington.edu/home/mabshoff/cddlib-094b.p0.spkg

Feedback welcome.

Cheers,

Michael


---

Comment by mabshoff created at 2007-11-24 13:12:00

Changing status from new to assigned.


---

Comment by mabshoff created at 2007-11-25 04:07:08

Merged in 2.8.14.rc2. Justin Walker did report that it fixed the issue for him.


---

Comment by mabshoff created at 2007-11-25 04:07:08

Resolution: fixed
