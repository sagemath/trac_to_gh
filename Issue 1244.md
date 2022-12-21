# Issue 1244: update flint to r1075, add spkg-check

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2007-11-22 21:43:26

Assignee: mabshoff

From Bill:

```
Actually I've got no idea how to create an spkg-check script. But the
things you would type at the command line, supposing you were in the
FLINT source tree in the trunk directory are:

make -Bj test
./mpn_extras-test
./ZmodF-test
./ZmodF_mul-test
./ZmodF_poly-test
./fmpz-test
./fmpz_poly-test
```

Those tests take about 6.5 minutes to run on sage.math, but we should run the tests per default for at least on release cycle (2.8.14) and disable them right before the final release. This will help Bill to shake out the last esoteric bug before the 1.0 release. The current Sage doctests don't even push the envelope. 

Cheers,

Michael


---

Comment by mabshoff created at 2007-11-22 21:43:34

Changing status from new to assigned.


---

Comment by mabshoff created at 2007-11-24 03:52:50

Ok, spkg is at

http://sage.math.washington.edu/home/mabshoff/flint-0.9-r1075.spkg

The forced tests can take 15-30 minutes.

Cheers,

Michael


---

Comment by mabshoff created at 2007-11-24 03:52:50

Changing component from algebraic geometry to packages.


---

Comment by mabshoff created at 2007-11-24 10:14:43

Ok, Bill found a bug that cause memory leakes. Updated spkg is at

http://sage.math.washington.edu/home/mabshoff/flint-0.9-r1075.p0.spkg

Cheers,

Michael


---

Comment by mabshoff created at 2007-11-24 15:36:38

Resolution: fixed


---

Comment by mabshoff created at 2007-11-24 15:36:38

Merged in 2.8.14.rc1. Various people reported that the spkg works.

Cheers,

Michael
