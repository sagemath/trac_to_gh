# Issue 947: Cython reload produces ln errors

Issue created by migration from https://trac.sagemath.org/ticket/947

Original creator: jvoight

Original creation time: 2007-10-20 18:04:06

Assignee: was

If you have a ./foo.spyx Cython file, and you "load foo.spyx" in SAGE, then touch foo.spyx and again "load foo.spyx", it gives messages of the sort:

ln: create symbolic link './d' to '/home/sage/d': File exists

for every directory d in ./

Everything appears to compile correctly, but if you're working in a directory with 100 folders, this can be very annoying!


---

Attachment


---

Comment by was created at 2007-10-20 22:28:57

Resolution: fixed
