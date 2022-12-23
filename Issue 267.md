# Issue 267: implement "sage -bt"

Issue created by migration from https://trac.sagemath.org/ticket/267

Original creator: dmharvey

Original creation time: 2007-02-17 20:59:16

Assignee: was

`sage -bt filename` could run a `sage -b` and then run doctests on the indicated file



---

Attachment


---

Comment by ncalexan created at 2007-02-25 02:48:25

Resolution: fixed


---

Comment by ncalexan created at 2007-02-25 02:48:25

Adds options "-bt" and "-btnew" for "build current and test/test new".

Adds option "-r clone" for "switch to and run clone".

Changes cloning so that "-clone existing" switches to "existing" clone.
