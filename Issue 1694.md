# Issue 1694: Update FLINT to 1.04 release

Issue created by migration from https://trac.sagemath.org/ticket/1694

Original creator: mabshoff

Original creation time: 2008-01-05 20:47:42

Assignee: mabshoff

To quote Bill Hart:

```
Hi Michael,

I see you are the release manager for the next release of SAGE and
that updating spkg's is a priority.

There are a handful of bug fixes in FLINT 1.0.4 which should probably
make their way into SAGE. Some of the fixes repair bugs which affected
test code on some 32 bit machines, though the bugs are actually in the
test code itself.

The other bug fixes are in code that doesn't affect SAGE at all, since
it is not used by SAGE. So this is not an urgent update, but something
which should be done eventually I guess.

Bill
```


Cheers,

Michael


---

Comment by mabshoff created at 2008-01-06 20:25:34

Oops,

```
Hi Michael,

Sorry to do this to you, but David Harvey and I just fixed some build
issues for machines running Darwin and certain versions of gcc. The
new release is FLINT 1.0.5

http://www.flintlib.org/

It might save you some troubles down the track as some of these issues
would also be a problem for building within SAGE.

Bill.
```


Cheers,

Michael


---

Comment by mabshoff created at 2008-01-08 01:28:04

The udpated spkg is at 

http://sage.math.washington.edu/home/mabshoff/release-cycles-2.10/alpha0/flint-1.05.spkg

I have turned the mandatory check on for now.

Cheers,

Michael


---

Comment by mabshoff created at 2008-01-08 01:28:19

Resolution: fixed
