# Issue 1910: linear algebra -- doctesting for sage/matrix/matrix_field_dense.pyx is off for no good reason, and there are lots of problems when we turn it on.

Issue created by migration from https://trac.sagemath.org/ticket/1910

Original creator: was

Original creation time: 2008-01-24 15:17:11

Assignee: was




---

Comment by dfdeshom created at 2008-03-04 17:07:20

This seems to be the reason: matrix_field_dense.pyx has matrix_pid_dense has its parent, but matrix_pid_dense doesn't even exist (yet)! Same for matrix_field_sparse and its counterpart, matrix_pid_sparse.


---

Comment by mabshoff created at 2008-12-11 16:00:57

The file in question does not exist any more in Sage 3.2.2.alpha2, so I am closing this as wontfix:

```
sage-3.2.2.alpha2/devel/sage$ ls -al sage/matrix/matrix_dense*
-rw-r--r-- 1 mabshoff 1090 264468 2008-12-10 06:41 sage/matrix/matrix_dense.c
-rw-r--r-- 1 mabshoff 1090     66 2008-12-08 02:44 sage/matrix/matrix_dense.pxd
-rw-r--r-- 1 mabshoff 1090  10782 2008-12-10 06:40 sage/matrix/matrix_dense.pyx
```

I also used find to locate the file elsewhere in the tree and it isn't there any more :)

Cheers,

Michael


---

Comment by mabshoff created at 2008-12-11 16:00:57

Resolution: wontfix
