# Issue 8419: cddlib fails to build on OpenSolaris fully.

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2010-03-02 14:04:28

Assignee: drkirkby

CC:  jsp mvngu

As reported by Jaap Spies, one of the reviewers of #8363, the package is not building properly as a 64-bit binary on OpenSolaris. This is despite the fact that CFLAGS includes -m64. It might be the lack of LDFLAGS being exported which is causing this problem. Whatever the cause is, this needs to work for a complete port to OpenSolaris. 


---

Comment by drkirkby created at 2010-06-11 19:20:33

Resolution: fixed


---

Comment by drkirkby created at 2010-06-11 19:20:33

This issue is resolved by #8363, so I am closing it. 

Dave
