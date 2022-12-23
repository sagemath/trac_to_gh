# Issue 1944: subsections not honored in ref manual

Issue created by migration from https://trac.sagemath.org/ticket/1944

Original creator: jason

Original creation time: 2008-01-26 23:43:16

Assignee: tba

In what should be a very small subsection of the reference manual, the Visualizing Graphs section contains the documentation for *every* function in graph.py.

See
http://sagemath.org/doc/html/ref/node48.html currently to see this.

A consequence of this is that it is very hard to find the documentation for a graph function when browsing the source because the table of contents does not indicate that all these are hidden under a sub section.



---

Comment by jason created at 2008-02-18 16:34:32

Changing priority from minor to major.


---

Comment by jason created at 2008-02-18 16:34:32

Changing to major priority since it seems very confusing for a new user and looks very unprofessional.


---

Comment by mhansen created at 2008-12-25 07:53:25

Changing assignee from tba to mhansen.


---

Comment by mhansen created at 2008-12-25 07:53:25

Changing status from new to assigned.


---

Comment by mhansen created at 2008-12-25 07:53:25

This will be fixed in the Sphinx reference manual.


---

Comment by mhansen created at 2009-02-28 04:20:37

This was fixed in #5330.


---

Comment by mhansen created at 2009-02-28 04:20:37

Resolution: fixed
