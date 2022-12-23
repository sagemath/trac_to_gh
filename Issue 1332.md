# Issue 1332: sage -b is really slow

Issue created by migration from https://trac.sagemath.org/ticket/1332

Original creator: moretti

Original creation time: 2007-11-29 06:32:34

Assignee: cwitty

Running sage -b takes a long time. This is because it has to scan through every cython file, building a dependency tree.


---

Comment by was created at 2007-12-02 06:18:58

Resolution: duplicate
