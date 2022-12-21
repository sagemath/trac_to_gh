# Issue 473: make the -valgrind target more flexible, add massif support

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2007-08-21 01:13:34

Assignee: mabshoff

At the moment the valgrind tool and flags are hardcoded in various scripts. So add checks for environment flag SAGE_VALGRIND_FLAGS to overwrite default.

To illustrate what you can do with other tools from the valgrind suite have a look at the two attached graphs created by the heap profiler massif.

It might also be nice to add a -valgrind to "sage -testall" to valgrind the whole test suite.

Cheers,

Michael


---

Comment by mabshoff created at 2007-08-21 01:14:12

example of massif heap profiler


---

Attachment

In addition increase the timeout value in sage-doctest to above 180 seconds depending on whether valgrind is used. Otherwise certain tests fail with timeouts:

```
==31586== Using valgrind-3.2.1, a dynamic binary instrumentation framework.
==31586== Copyright (C) 2000-2006, and GNU GPL'd, by Julian Seward et al.
==31586== For more details, rerun with: -v
==31586==
--31586-- DWARF2 CFI reader: unhandled CFI instruction 0:10
--31586-- DWARF2 CFI reader: unhandled CFI instruction 0:10
==31586==
==31586== Total spacetime:   1,269,947,691,109 ms.B
==31586== heap:              84.8%
==31586== heap admin:        14.6%
==31586== stack(s):           0.4%
*** *** Error: TIMED OUT! *** ***
*** *** Error: TIMED OUT! *** ***
         [222.3 s]
```


Cheers,

Michael


---

Comment by mabshoff created at 2007-08-22 19:38:48

Changing status from new to assigned.


---

Comment by mabshoff created at 2007-08-30 00:26:39

The sage -t -valgrind support should have been added to the 2.8.3 release. 

Massif support will come for 2.9.

Cheers,

Michael


---

Comment by mabshoff created at 2007-09-06 18:57:20

http://fsmath.mathematik.uni-dortmund.de/~mabshoff/patches/Sage-2.8.3.6-add-more-valgrind-to-sage-sage.patch
http://fsmath.mathematik.uni-dortmund.de/~mabshoff/patches/Sage-2.8.3.6-add-sage-cachegrind.patch
http://fsmath.mathematik.uni-dortmund.de/~mabshoff/patches/Sage-2.8.3.6-add-sage-massif.patch
http://fsmath.mathematik.uni-dortmund.de/~mabshoff/patches/Sage-2.8.3.6-change-location-of-log-file.patch

Cheers,

Michael


---

Comment by was created at 2007-09-06 19:44:05

Resolution: fixed
