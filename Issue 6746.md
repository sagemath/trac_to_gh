# Issue 6746: cliquer doesn't build under 64-bit mode

Issue created by migration from Trac.

Original creator: mvngu

Original creation time: 2009-08-14 17:22:13

Assignee: mabshoff

CC:  jhpalmieri ncohen

At this [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/9b8016e17cc81128) thread, Kiran Kedlaya reported a problem with building cliquer under a 64-bit platform:

```
On 64-bit Fedora 10, I get a build failure in cliquer. The relevant
snippet from the install log is below.

This looks like a case of 32/64 confusion, which I am no stranger to.
This machine runs on a primarily 32-bit network, and in the past we've
discovered various build problems due to this. For instance, the local
gcc in /usr/bin is 64-bit, but the NFS one in /usr/local/bin is 32-
bit, so I have to configure my path appropriately. In this case, it's
somehow trying to find stubs-32.h instead of stubs-64.h, but I don't
know why.
```

John Palmieri also reported at ticket #6681 a similar problem with 64-bit OS X.


---

Comment by mvngu created at 2009-09-13 09:41:41

See ticket #6681 for an updated cliquer spkg. If that package also builds on 64-bit Fedora 10, then this ticket should be closed as a duplicate of #6681.


---

Comment by kedlaya created at 2009-09-22 19:08:45

Replying to [comment:1 mvngu]:
> See ticket #6681 for an updated cliquer spkg. If that package also builds on 64-bit Fedora 10, then this ticket should be closed as a duplicate of #6681.

It does indeed build on 64-bit Fedora 10, as part of a full build of 4.1.2.alpha2.


---

Comment by mhansen created at 2009-09-25 08:07:36

Duplicate of #6681


---

Comment by mhansen created at 2009-09-25 08:07:36

Resolution: duplicate
