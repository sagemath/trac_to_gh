# Issue 42: Calling GAP commands via gap("command") reacts badly sometimes

Issue created by migration from https://trac.sagemath.org/ticket/42

Original creator: was

Original creation time: 2006-09-12 23:32:22

Assignee: somebody

** (KiranKedlaya) Calling GAP commands via gap("command") reacts badly when the command does not return a value, e.g., gap('Read("myfile.txt")').


---

Comment by wdj created at 2006-09-24 19:36:51

Do you mean gap.eval('Read("myfile.txt")') is flaky? If so, can you give an example?


---

Comment by was created at 2007-01-12 22:03:04

Resolution: fixed


---

Comment by was created at 2007-01-12 22:03:04

This is a misunderstanding about using gap(s) versus gap.eval(s).  This is not a bug.
gap(s) is supposed to always create a new gap object.
