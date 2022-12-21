# Issue 4930: [with spkg, needs review] 3.2.3.final: Fix bug in ATLAS' spkg-install that breaks the install target for dynamic libs

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2009-01-03 03:19:47

Assignee: mabshoff

Unfortunately the spkg at #3785 contained a buglet: the patches Make.top isn't copied into the right directory, so "make install" doesn't copy over libatlas.so, libcblas.so and libf77blas.so. Due to that on some machines rpy won't load due to a missing libatlas.so.

An spkg with that fixed is coming up.

Cheers,

Michael


---

Comment by mabshoff created at 2009-01-03 03:36:45

The spkg at

http://sage.math.washington.edu/home/mabshoff/spkgs/atlas-3.8.2.p0.spkg

fixes the issue. The only "real" difference is this:

```
--- a/spkg-install      Thu Jan 01 21:06:49 2009 -0800
+++ b/spkg-install      Fri Jan 02 19:29:51 2009 -0800
`@``@` -73,7 +73,7 `@``@`
 cp patches/probe_comp.c src/CONFIG/src/probe_comp.c
 # add dynamic libs make install targets
 echo Updating Make.top
-cp patches/Make.top src/ATLAS/
+cp patches/Make.top src
 # add K7, Pentium M and non-AltiVec G4 profiles
 cp patches/*tgz src/CONFIG/ARCHS
```


The location of the ATLAS src was adjusted from src/ATLAS to src, so the improvements to Make.top were not copied correctly. This caused libatlas.so, libcblas.so and libf77blas.so not to be copied over for "make install".

Cheers,

Michael


---

Comment by mabshoff created at 2009-01-03 03:36:45

Changing status from new to assigned.


---

Comment by mabshoff created at 2009-01-03 05:58:40

Resolution: fixed


---

Comment by mabshoff created at 2009-01-03 05:58:40

Merged in Sage 3.2.3.final
