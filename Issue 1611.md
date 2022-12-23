# Issue 1611: polybori should use the m4ri library from libm4ri spkg

Issue created by migration from https://trac.sagemath.org/ticket/1611

Original creator: burcin

Original creation time: 2007-12-27 10:54:50

Assignee: burcin

CC:  polybori

PolyBoRi comes with its own copy of m4ri libraries. After #1505, Sage provides these libraries through a package.

The PolyBoRi build process should be changed to use the library and headers provided by libm4ri-*.spkg.


---

Comment by malb created at 2007-12-27 12:24:54

Michael Brickenstein wrote:

> If you can wait until the end of my holidays, which will begin  
> tomorrow and end at 6th of January, I will do the switch myself.


---

Comment by burcin created at 2008-01-03 15:07:54

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-02-15 23:23:43

The issue might be resolved during the update to PolyBoRi 0.2.rcX during Bug Day 10.

Cheers,

Michael


---

Comment by mabshoff created at 2008-02-17 19:57:01

This should be done while updating PolyBori - see #2060.

Cheers,

Michael


---

Comment by burcin created at 2008-03-08 13:37:53

`PolyBoRi` requires some changes in the m4ri libraries. They are waiting for changes upstream (in m4ri) to switch over, so newer versions of `PolyBoRi` don't support this.


---

Comment by malb created at 2008-03-09 15:27:38

I guess I am upstream so I should diff their m4ri against ours (upstream).


---

Comment by mabshoff created at 2008-05-12 00:12:36

Fixing this bug is planned for the PolyBoRi 0.5 release.

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-07 00:41:58

#3264 does not fix the problem yet. Are there any options to make this happen with PolyBoRi 0.5?

Cheers,

Michael


---

Comment by malb created at 2008-09-07 00:59:07

There is some movement w.r.t. this issue in PolyBoRi, but I wouldn't suspect it to be available in 0.5.


---

Comment by PolyBoRi created at 2008-09-08 06:23:24

it will be available in 0.5. However, you should make sure, that
malloc work also for allocating zero bytes in M4RI, else it will crash
(doesn't work with mm_malloc on Mac OS X 10.5).


---

Comment by malb created at 2009-09-29 08:08:56

This is fixed with #6177


---

Comment by malb created at 2009-09-29 08:08:56

Resolution: fixed
