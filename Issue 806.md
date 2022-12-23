# Issue 806: matrix_integer_dense.elementary_divisors return a mutable object

Issue created by migration from https://trac.sagemath.org/ticket/806

Original creator: syazdani

Original creation time: 2007-10-03 14:52:20

Assignee: was

The following code causes incorrect output:

```
sage: M=random_matrix(ZZ,3,2)

sage: M.elementary_divisors()
 [1, 1, 0]

sage: edivs=M.elementary_divisors()

sage: edivs.pop()
 0

sage: edivs
 [1, 1]

sage: M.elementary_divisors()
 [1, 1]
```

The problem seems to be elementary_divisors() caches the result, but returns a mutable object.


---

Comment by mhansen created at 2007-10-04 11:50:04

Patch attached.


```
sage: M=random_matrix(ZZ,3,2)
sage: 
sage: M.elementary_divisors()
[1, 1, 0]
sage: edivs = M.elementary_divisors()
sage: edivs.pop()
0
sage: edivs
[1, 1]
sage: M.elementary_divisors()
[1, 1, 0]
```



---

Attachment


---

Comment by was created at 2007-10-04 18:53:43

Resolution: fixed
