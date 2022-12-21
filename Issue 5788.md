# Issue 5788: Fix MPIR build problem on OSX 10.4 exposed by linbox

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2009-04-15 00:52:01

Assignee: mabshoff

On OSX 10.4 a problem in libgmpxx.la leads to linbox linking gmpxx, mpir *and* gmp at the same time resulting in duplicate symbol errors. The latest upstream release (MPIR 1.0) fixes that.

Spkg coming up.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-18 07:32:50

Changing status from new to assigned.


---

Comment by mabshoff created at 2009-04-18 07:32:50

The spkg at 

 http://sage.math.washington.edu/home/mabshoff/release-cycles-3.4.1/rc4/gmp-mpir-1.1.spkg

fixes this problem, a couple other test failures reported in IRC and face-to-face and updates to the latest upstream release.

Cheers,

Michael


---

Comment by GeorgSWeber created at 2009-04-18 13:46:10

Extracting the Sage 3.4.rc3 tarball, replacing the gmp-mpir spkg with this "rc4" one (and as only other change replacing the atlas spkg also with the "rc4" version from #5219), Sage builds fine (!) and for "make test" all tests pass.

Tested on my MacIntel OS X 10.4.11 / Xcode 2.5 box / "daily work" installation (but TeX being in the path should be of no concern here).

Cheers, gsw


---

Comment by mabshoff created at 2009-04-18 23:13:48

Merged in Sage 3.4.1.rc4.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-18 23:13:48

Resolution: fixed
