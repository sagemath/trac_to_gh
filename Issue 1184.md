# Issue 1184: OSX: moving sage breaks recompile of libcsage (--rpath issue)

Issue created by migration from https://trac.sagemath.org/ticket/1184

Original creator: mabshoff

Original creation time: 2007-11-16 03:39:13

Assignee: cwitty

This is likely one the first issue to be reported and involves the use of --rpath linker option. On OSX that leads to trouble when moving a Sage installation and recompiling the Sage library. Symptoms are the linker complaining that it cannot find a libgmp.dylib, specifically that gmp symbols with triple underscores are missing.

Cheers,

Michael


---

Comment by mabshoff created at 2007-11-27 00:28:17

Changing status from new to assigned.


---

Comment by mabshoff created at 2007-11-27 00:28:17

Changing assignee from cwitty to mabshoff.


---

Attachment

The updated spkg is at 

http://sage.math.washington.edu/home/mabshoff/ntl-5.4.1.p7.spkg

You need to apply both the patch and add the ntl.spkg.

Cheers,

Michael


---

Comment by mabshoff created at 2007-12-02 04:13:49

Resolution: fixed


---

Comment by mabshoff created at 2007-12-02 04:13:49

Merged in 2.8.15.alpha2.
