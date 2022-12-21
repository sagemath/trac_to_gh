# Issue 4665: sage/misc/cython.py creates file sage/misc/hello.spyx in tree while doctesting

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-11-30 10:04:17

Assignee: mabshoff

#4660 exposed a bug in sage/misc/cython.py: hello.spyx is created in tree, but that file should be created in the Sage tmp directory.

Cheers,

Michael


---

Attachment


---

Comment by mabshoff created at 2009-01-24 12:25:00

Positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2009-01-24 13:16:50

Resolution: fixed


---

Comment by mabshoff created at 2009-01-24 13:16:50

Merged in Sage 3.3.alpha2
