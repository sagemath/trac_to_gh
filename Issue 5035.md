# Issue 5035: get doctest coverage of matrix_generic_dense.pyx up to 100%

Issue created by migration from https://trac.sagemath.org/ticket/5035

Original creator: was

Original creation time: 2009-01-20 07:14:41

Assignee: was




---

Comment by was created at 2009-01-20 07:15:53

this is against sage-3.3.alpha0


---

Attachment


---

Comment by ddrake created at 2009-01-20 07:25:18

The patch applies cleanly, but I get a doctest error:

```
sage -t  "devel/sage-main/sage/matrix/matrix_generic_dense.pyx"
**********************************************************************
File "/var/tmp/sage-3.3.alpha0/devel/sage-main/sage/matrix/matrix_generic_dense.pyx", line 161:
    sage: hash(A)
Expected:
    -623270016
Got:
    139665060168050560
**********************************************************************
1 items had failures:
   1 of   6 in __main__.example_6
***Test Failed*** 1 failures.
For whitespace errors, see the file /var/tmp/sage-3.3.alpha0/tmp/.doctest_matrix_generic_dense.py
	 [1.1 s]
exit code: 1024
```



---

Attachment

With both patches applied, we have 100% coverage, and the examples are nice. Positive review.


---

Comment by mabshoff created at 2009-01-23 09:07:35

Resolution: fixed


---

Comment by mabshoff created at 2009-01-23 09:07:35

Merged both patches in Sage 3.3.alpha1
