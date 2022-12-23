# Issue 5319: Fix location of source in the Sage's installation manual

Issue created by migration from https://trac.sagemath.org/ticket/5319

Original creator: mabshoff

Original creation time: 2009-02-20 10:53:28

Assignee: schilly

This is in "3.1 Steps to Install from Source"

```
rootard: http://www.sagemath.org/doc/inst/node6.html <-- says to download source from http://www.sagemath.org/dist/src/ but I get a 404.
[02:52am] mabs: oops
[02:52am] mabs: That moved around, I will open a ticket.
```


Cheers,

Michael


---

Comment by schilly created at 2009-02-20 10:58:06

the canonical url for things like this is
`http://www.sagemath.org/download-source.html` (or `*-linux, ...` because there you can choose
the mirror. otherwise it's just the main website.


---

Comment by mhansen created at 2009-02-20 10:58:48

Changing assignee from schilly to mhansen.


---

Comment by mhansen created at 2009-02-20 10:58:48

I've changed the ReST docs to point to that URL.


---

Comment by mhansen created at 2009-02-20 10:58:48

Changing status from new to assigned.


---

Comment by jhpalmieri created at 2009-02-26 18:02:04

It looks like Mike fixed this, so it can be closed.


---

Comment by mhansen created at 2009-02-26 18:03:00

Closed due to #5330.


---

Comment by mhansen created at 2009-02-26 18:03:00

Resolution: fixed
