# Issue 4862: two trivial-to-fix issues with the macaulay2 spkg

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-12-24 02:16:14

Assignee: mabshoff

CC:  schilly

1. The name of it in experimental is macaulay2-20061014.p1.spkg but it should be macaulay2-20081014.p1.spkg

2. If you do `export MAKE="make -j4"` then the build fails as follows:

```
checking for gmake... make -j20
checking whether make -j20 is GNU make... ./configure: line 1497: make -j20: command not found
configure: make -j20: GNU make is required
```


This could be fixed by not using $MAKE to do anything in parallel, which would be better than just having it break.


---

Comment by was created at 2008-12-24 02:27:34

And, for the record, the spkg doesn't build on the new sage.math (Ubuntu 8.04


---

Comment by mabshoff created at 2008-12-24 02:37:45

The issue is with the website, i.e. all the spkgs are in www-files.

Cheers,

Michael


---

Comment by was created at 2008-12-24 03:49:25

now fixed.  and it does build on sage.math, but not in parallel...


---

Comment by mabshoff created at 2008-12-24 14:34:55

The spkg at

http://sage.math.washington.edu/home/mabshoff/macaulay2-1.1-r7221.p0.spkg

fixes the issue:

```
mabshoff`@`sage:/scratch/release-cycle/junk/sage-3.2.2$ export MAKE="make -j8"
mabshoff`@`sage:/scratch/release-cycle/junk/sage-3.2.2$ ./sage -i macaulay2-1.1-r7221.p0
<SNIP - things do not blow up>
```


Cheers,

Michael


---

Comment by was created at 2008-12-24 21:29:45

Looks good.


---

Comment by mabshoff created at 2008-12-26 17:18:07

Resolution: fixed


---

Comment by mabshoff created at 2008-12-26 17:18:07

Merged in Sage 3.2.3.final and uploaded to the optional spkg repo.

Cheers,

Michael
