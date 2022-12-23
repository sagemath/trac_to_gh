# Issue 1984: make html documentation error

Issue created by migration from https://trac.sagemath.org/ticket/1984

Original creator: pgrinber

Original creation time: 2008-01-30 13:42:31

Assignee: tba

in v2.10, after the build process is complete, change directories to devel/doc and run make html. This gives an emergency stop on \`@`mathbf when processing ref.toc. In order to successfully generate the HTML documentation I  had to first run 

sed -i -e "s/`@`mathbf/mathbf/g" ../doc-main/ref/ref.toc

which simply removed the unnecessary '`@`' sign before mathbf.


---

Comment by cwitty created at 2008-01-30 18:58:06

In my experience, it also suffices to simply remove ref.toc.  Probably we should not be shipping this file at all.


---

Comment by mhansen created at 2009-01-22 08:01:16

This will be irrelevant once the Sphinx docs are in so I'm not going to work it.


---

Comment by jhpalmieri created at 2009-02-26 17:09:29

This can be closed now.


---

Comment by mhansen created at 2009-02-26 17:22:48

Resolution: fixed


---

Comment by mhansen created at 2009-02-26 17:22:48

Good catch.  Closed due to #5330.
