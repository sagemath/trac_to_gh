# Issue 6047: Disable threading for boehm_gc

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2009-05-15 21:21:09

Assignee: mabshoff

Threading causes trouble when building ecl against boehm since we need to link threading libraries into ecl, so just don't enable them in boehm. 

While I am in there also remove all the OSX crap from some finder indexing run.

Cheers,

Michael


---

Comment by mabshoff created at 2009-05-16 00:18:04

This was a red herring - invalid.

Cheers,

Michael


---

Comment by mabshoff created at 2009-05-16 00:18:04

Resolution: invalid
