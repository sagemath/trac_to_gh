# Issue 6611: [with spkg, needs review] rename networkx-0.99.p1-fake_really-0.36.p0.spkg to networkx-0.36.p0.spkg

Issue created by migration from https://trac.sagemath.org/ticket/6611

Original creator: mvngu

Original creation time: 2009-07-24 07:22:33

Assignee: mabshoff

CC:  rlm

As of Sage 4.1, the NetworkX SPKG is named `networkx-0.99.p1-fake_really-0.36.p0.spkg`, which was the result of #4860 and #5934. Let's now rename that SPKG as `networkx-0.36.p0.spkg`. The updated SPKG is up at 

http://sage.math.washington.edu/home/mvngu/patch/networkx-0.36.p0.spkg

There is no substantial difference between that SPKG and the one in Sage 4.1. I merely took the one from Sage 4.1 and renamed it as `networkx-0.36.p0.spkg`.


---

Comment by rlm created at 2009-07-27 16:16:19

I don't think this is a good idea-- there are scripts which determine the newest version of an SPKG, and if you change the name to `networkx-0.36*`, then the newest version will remain `networkx-0.99.p1-fake_really-0.36.p0.spkg`


---

Comment by mvngu created at 2009-07-28 03:13:54

Good catch! So can this ticket be closed as invalid?


---

Comment by jason created at 2009-07-30 09:46:24

+1 to closing it as invalid.

(+1 also for someone actually updating networkx :)


---

Comment by mvngu created at 2009-07-30 09:49:43

Resolution: invalid
