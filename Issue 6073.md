# Issue 6073: Developer guide somewhat wrong about cython extensions

Issue created by migration from Trac.

Original creator: mhampton

Original creation time: 2009-05-18 18:09:02

Assignee: tba

In the developer guide, in the "Coding in other languages" section, it says that Cython pyx files should be added to setup.py, but they should really be added to module_list.py.


---

Comment by jhpalmieri created at 2009-06-10 21:50:00

I think the information about module_list.py is in the paragraph before the one you're mentioning.  Here's a patch which tries to clarify things a bit, and adds some new information.


---

Attachment

This patch applies fine and the command "/sage -docbuild developer html" builts the docs without error. The addition clarifies and improves the documentation as advertised.


---

Comment by rlm created at 2009-06-24 10:09:43

Resolution: fixed
