# Issue 1036: optional macaulay2 package does not install

Issue created by migration from Trac.

Original creator: malb

Original creation time: 2007-10-30 17:18:37

Assignee: was

first `bison` is required and after installing that, this happens:


```
In file included from ../comp.hpp:9,
                 from ../comp_gb.hpp:6,
                 from lingb.hpp:8,
                 from lingb.cpp:1:
../comp.hpp:7: error: previous declaration of ‘int gbTrace’ with ‘C++’ linkage
../engine.h:1530: error: conflicts with new declaration with ‘C’ linkage
```


This is with `GCC 4.2.3` on 64-bit Debian/testing.


---

Comment by mabshoff created at 2007-10-30 18:00:25

Hello,

Macaulay2 not building is a known issue and #10 should take care of that. But after initial ativity about a month back the work on a new Macaulay2 release seems to have slowed down.

Cheers,

Michael


---

Comment by wjp created at 2007-11-14 23:58:33

Attached a small patch. The 'extern int gbTrace' in engine.h is in an extern "C" {} block, while 'int gbTrace' is defined in a .cpp file.

Since it doesn't appear to be patched in Macaulay2 svn, attaching a small patch.


---

Comment by wjp created at 2007-11-14 23:59:07

gbTrace C++-linkage patch


---

Attachment


---

Comment by was created at 2007-12-16 00:25:44

Resolution: fixed


---

Comment by was created at 2007-12-16 00:25:44

I've put this into sage.
