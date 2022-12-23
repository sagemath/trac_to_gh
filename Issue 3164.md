# Issue 3164: Problems with echelon_form over ComplexField

Issue created by migration from https://trac.sagemath.org/ticket/3164

Original creator: dunfield

Original creation time: 2008-05-12 00:47:57

Assignee: was

For certain well-conditioned floating-point matrices with entries in ComplexField, echelon_form can return matrices which are not in (approximate) echelon_form.   This breaks methods like rank(), right_solve() and inverse().  I've attached a sample matrix which illustrates this 

```
sage: A = load("./prob-sol.sobj")
sage: A.parent()
Full MatrixSpace of 5 by 5 dense matrices over Complex Field with 1010 bits of precision
sage: matrix(CDF, A.echelon_form())

[                              1.0                                 0                            -3.5*I                                 0                    -20.0 + 12.0*I]
[                                0                               1.0                               1.0                                 0                      -4.0 + 1.0*I]
[                                0                                 0        1.0 + 4.55695126222e-305*I                                 0 -2.33592727654 + 0.497614402099*I]
[                                0                                 0                              -4.0                               1.0                              -2.0]
[                                0                                 0                              -2.0                                 0                                 0]
sage: CC(A.det())
76.1312551138321 - 5.28799080668534*I
sage: A.rank()
4
```



This bug is probably related to #2256 and #1132 but there the problem with echelon_form is more subtle (1 entries on the diagonal which aren't quite 1), which is why I opened this new ticket.  


---

Comment by dunfield created at 2008-05-12 00:53:39

Resolution: duplicate
