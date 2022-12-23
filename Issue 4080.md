# Issue 4080: [with patch, needs review] Symbol clash between global M4RI and PolyBoRi's M4RI

Issue created by migration from https://trac.sagemath.org/ticket/4080

Original creator: malb

Original creation time: 2008-09-08 23:03:27

Assignee: malb

CC:  polybori

Keywords: sigsegv

PolyBoRi uses its own M4RI instance which is older than the version of M4RI which is going to be in Sage 3.1.2. Since M4RI is written in C there are no namespaces and thus the symbols clash, even though both versions are binary incompatible. A workaround for now -- until PolyBoRi is updated -- is to delay the import of `sage.rings.pbring` after the import of `sage.matrix.matrix_mod2_dense`. Since PolyBoRi is statically linked for now anyway, this shouldn't mess up things. However *this is a dirty workaround*


---

Attachment


---

Comment by malb created at 2008-09-08 23:05:02

btw. this patch can remain applied and does not need to be reverted once the issue at hand is fixed. This is, because it is a good idea to late import more stuff anyway.


---

Comment by mabshoff created at 2008-09-08 23:15:13

The patch is good, it fixes the issue on OSX and does pass doctests on Linux. Positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-08 23:57:47

Merged in Sage 3.1.2.rc1


---

Comment by mabshoff created at 2008-09-08 23:57:47

Resolution: fixed
