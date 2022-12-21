# Issue 475: check for SAGE_DEBUG flag on build to include symbols

Issue created by migration from Trac.

Original creator: burcin

Original creation time: 2007-08-21 14:10:23

Assignee: was

Packages should check for a flag (i.e. SAGE_DEBUG) on build. If this is set, options suitable for debugging should be used. i.e. CFLAGS="-g", no optimizations,  --without-pymalloc in Python (for valgrind)


---

Comment by mabshoff created at 2007-11-20 14:20:34

Changing keywords from "" to "package audit".


---

Comment by robertwb created at 2009-07-28 12:58:05

-g in CFLAGS is, IMHO, a different level than turning off all optimization and Python memory management (the latter actually have a significant speed impact, the former none).
