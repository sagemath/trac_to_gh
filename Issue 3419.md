# Issue 3419: [with patch, needs review] 100% coverage for sage.coding.binary_code

Issue created by migration from https://trac.sagemath.org/ticket/3419

Original creator: rlm

Original creation time: 2008-06-13 18:41:02

Assignee: rlm


```
$ ./sage -coverage devel/sage/sage/coding/binary_code.pyx
----------------------------------------------------------------------
devel/sage/sage/coding/binary_code.pyx
SCORE devel/sage/sage/coding/binary_code.pyx: 100% (41 of 41)

Possibly wrong (function name doesn't occur in doctests):
	 * int put_in_std_form(self)

----------------------------------------------------------------------
```


There seems to be a little bug in sage-coverage related to cpdef functions: the function name definitely occurs in the doctest. Has #1795 gone stale?!


---

Attachment

The cpdef patch ought to get merged this week, I am not sure what the current merge status is.

Cheers,

Michael


---

Comment by malb created at 2008-06-15 19:03:34

Patch looks good.


---

Comment by rlm created at 2008-06-22 20:54:02

Apply after #3471.


---

Comment by mabshoff created at 2008-06-23 03:02:35

Resolution: fixed


---

Comment by mabshoff created at 2008-06-23 03:02:35

Merged in Sage 3.0.4.alpha0
