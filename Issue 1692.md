# Issue 1692: Make doc target force to use local sage instead of sage in $PATH

Issue created by migration from https://trac.sagemath.org/ticket/1692

Original creator: mabshoff

Original creation time: 2008-01-05 14:16:25

Assignee: was




---

Comment by mabshoff created at 2008-04-25 16:59:12

This has been fixed by wstein in $SAGE_ROOT/devel/doc/ref/update. It now sets up the end properly when SAGE_ROOT is empty.


---

Comment by mabshoff created at 2008-04-25 16:59:12

Resolution: fixed


---

Comment by mabshoff created at 2008-04-25 16:59:38

Oops: end->env 

Cheers,

Michael
