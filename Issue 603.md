# Issue 603: add documentation/tutorial on how to valgrind Sage

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2007-09-06 19:35:54

Assignee: burcin

CC:  mvngu

See http://www.sagemath.org:9001/ValgrindingSage for a working copy of the document. Once it is deemed usable we should use it to html and merge it into the official documentation.

Cheers,

Michael


---

Comment by kcrisman created at 2009-12-30 04:53:23

It's probably better to have this in the documentation in some form than not at all - even a brief intro in the Developer Guide might encourage someone to learn to use it properly.   I'm cc:ing a likely suspect for doing so nicely :)


---

Comment by rws created at 2015-10-12 06:43:40

Just a note to add a note that `sage -t --valgrind` runs the tests with the `--serial` option in order to have them all in one process (and therefore it's not necessary to add it explicitly---which may not work).
