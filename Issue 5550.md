# Issue 5550: .../doc/output/html/en/index.html should include "/index.html" in links

Issue created by migration from https://trac.sagemath.org/ticket/5550

Original creator: cwitty

Original creation time: 2009-03-17 15:04:43

Assignee: tba

The web page produced for "all the documentation" at .../doc/output/html/en/index.html doesn't work when browsing the documentation locally with `file:///` URLs, because the ".../" -> ".../index.html" redirect is done by the web server, and there's no web server involved for `file:///`.  So clicking on "Reference Manual" brings you to a directory listing for the reference manual, not to the index.html that lets you actually read the reference manual.


---

Comment by davidloeffler created at 2009-07-13 16:42:06

Ticket #6485 seems to be a duplicate of this one. I suggest we close this one and keep #6485, since there is already a patch there.


---

Comment by mvngu created at 2009-07-18 20:15:37

Resolution: duplicate
