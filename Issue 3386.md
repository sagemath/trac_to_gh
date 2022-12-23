# Issue 3386: zn_poly test code is still being run

Issue created by migration from https://trac.sagemath.org/ticket/3386

Original creator: dmharvey

Original creation time: 2008-06-09 14:17:58

Assignee: mabshoff

The build process is still running the full `zn_poly` test suite. This is probably no longer necessary, and makes the build time somewhat longer than it needs to be.



---

Comment by mabshoff created at 2008-06-09 21:02:01

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-06-09 21:02:01

I know about the test suite still running, but I thought you wouldn't mind the extra coverage. But I agree that we should now disable the testing. The updated spkg that moves the test suite to spkg-check can be found at

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.0.3/alpha2/zn_poly-0.8.p1.spkg

Cheers,

Michael


---

Comment by mabshoff created at 2008-06-09 21:14:59

Merged in Sage 3.0.3.alpha2


---

Comment by mabshoff created at 2008-06-09 21:14:59

Resolution: fixed
