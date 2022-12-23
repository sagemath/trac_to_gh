# Issue 680: Solaris 9: fix partition import problem

Issue created by migration from https://trac.sagemath.org/ticket/680

Original creator: mabshoff

Original creation time: 2007-09-17 09:09:12

Assignee: mabshoff

As a workaround on Solaris 9 we define:

```
#if defined(__sun)
extern long double fabsl (long double);
extern long double sinl (long double);
extern long double cosl (long double);
extern long double sqrtl (long double);
extern long double coshl (long double);
extern long double sinhl (long double);
#endif
```

Problem is that this file is C++, so those externs need to be defined as extern "C". Otherwise the linker mangles the function names and consequently Sage doesn't start complaining about missing symbols.

Cheers,

Michael


---

Comment by mabshoff created at 2007-09-17 09:09:20

Changing status from new to assigned.


---

Comment by mabshoff created at 2007-09-18 20:18:30

A patch for this problem can be found at 

http://fsmath.mathematik.uni-dortmund.de/~mabshoff/patches/Sage-2.8.4-fix-partition.so-load-problem-on-Solaris9.patch

Cheers,

Michael


---

Comment by was created at 2007-09-21 00:10:41

Resolution: fixed
