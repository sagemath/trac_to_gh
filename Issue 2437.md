# Issue 2437: update eclib.spkg to eclib-20080304.spkg

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-03-09 06:45:02

Assignee: mabshoff

This spkg is required for #2394 to wrap newforms


---

Comment by mabshoff created at 2008-03-09 06:50:35

I fail to see any difference to eclib-20080127.p0 in the hg log, so can somebody enlighten me what is different?

Cheers,

Michael


---

Comment by boothby created at 2008-03-13 06:20:25

http://sage.math.washington.edu/home/boothby/SPKG/2.10.4/eclib-20080310.spkg


---

Comment by mhansen created at 2008-03-15 21:39:00

I tried installing this with 'sage -i' and got the following error:


```
eclib-20080127.p1/src/g0n/nfd.cc
eclib-20080127.p1/src/g0n/nflist.cc
eclib-20080127.p1/src/g0n/nftest.out
eclib-20080127.p1/src/g0n/nftest.in
eclib-20080127.p1/src/g0n/documentation.txt
eclib-20080127.p1/src/Makefile.dynamic
eclib-20080127.p1/src/lib/
Finished extraction
sage: After decompressing the directory eclib-20080310 does not exist
This means that the corresponding .spkg needs to be downloaded
again.
http://www.sagemath.org//packages/optional/eclib-20080310.spkg --> eclib-20080310.spkg
[.]
http://www.sagemath.org//packages/standard/eclib-20080310.spkg --> eclib-20080310.spkg
[.]
http://www.sagemath.org//packages/experimental/eclib-20080310.spkg --> eclib-20080310.spkg
[.]
http://www.sagemath.org//packages/archive/eclib-20080310.spkg --> eclib-20080310.spkg
[.]
Unable to download eclib-20080310
Please see http://www.sagemath.org//packages for a list of valid packages
/home/mhansen/sage-2.10.4.alpha0-sage.math-only-x86_64-Linux/spkg/build
bunzip2: Can't open input file eclib-20080310.spkg: No such file or directory.
tar: eclib-20080310.spkg: Cannot open: No such file or directory
tar: Error is not recoverable: exiting now
Second download resulted in a corrupted package.
```



---

Comment by mabshoff created at 2008-03-19 10:37:26

Hi Tom,

the spkg at

http://sage.math.washington.edu/home/mabshoff/SPKG/eclib-20080310.p0.spkg

fixes the problem Mike had and another thing I found:

 * the name of the spkg must match the directory name, i.e. eclib-20080310.p0.spkg unpacks into eclib-20080310.p0
 * you forgot to update SPKG.txt

The new spkg builds fine, but I am doing some more testing before giving it a positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-03-19 11:01:28

I also fixed some permission issues since John seems to have a rather tight umask. In total I give this spkg a positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-03-19 11:35:24

Resolution: fixed


---

Comment by mabshoff created at 2008-03-19 11:35:24

Merged in Sage 2.11.alpha0
