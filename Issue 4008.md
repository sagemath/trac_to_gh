# Issue 4008: [with spkg, needs review] OSX 10.4/5: build python without the OSX specific extensions

Issue created by migration from https://trac.sagemath.org/ticket/4008

Original creator: mabshoff

Original creation time: 2008-08-30 23:42:57

Assignee: mabshoff

This is a followup to #4407: When we build Python on OSX we per default build extensions that depend on OSX specific frameworks. Those frameworks (especially the IO one) end up pulling in Apple's libpng.dylib which is incompatible with the one we build. Consequently extension linking our libpng.dylib blows up at import time. This is an issue with #3324. Since we are not building the extensions in 64 bit OSX mode this and we have to chose between a working libpng and extension I prefer a working libpng. The spkg at

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.1.2/alpha3/python-2.5.2.p5.spkg

disables the OSX specific python extensions. Builds fine on OSX 10.4 and 10.5 and passes doctests. After applying #3324 the matrix_mod2_dense doctest now also passes.

Cheers,

Michael


---

Comment by mabshoff created at 2008-08-30 23:43:31

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-08-30 23:52:07

Resolution: fixed


---

Comment by mabshoff created at 2008-08-30 23:52:07

Merged in Sage 3.1.2.alpha3
