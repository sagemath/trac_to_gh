# Issue 4641: [with patch, needs review] "-notebook" commandline option should take trailing options

Issue created by migration from https://trac.sagemath.org/ticket/4641

Original creator: klee

Original creation time: 2008-11-28 05:24:45

Assignee: klee

Keywords: commandline option

The commandline option "-notebook" is advertised to take trailing options, but does not yet (as of Sage 3.1.2). A patch is included.


---

Attachment


---

Comment by klee created at 2008-11-28 05:38:10

Changing assignee from klee to somebody.


---

Comment by klee created at 2008-11-28 06:18:18

With the patch, the following works:

sage -notebook "address='10.0.1.199'" secure=True open_viewer=False


---

Comment by was created at 2008-11-28 23:41:03

This is *very* nice and a simple solution.  Excellent work!

Mabshoff -- apply the patch to the scripts repo.


---

Comment by mabshoff created at 2008-11-28 23:49:22

Merged in Sage 3.2.1.rc0


---

Comment by mabshoff created at 2008-11-28 23:49:22

Resolution: fixed
