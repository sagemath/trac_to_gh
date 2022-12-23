# Issue 666: add spacing in latex output of matrices for increasing readbility

Issue created by migration from https://trac.sagemath.org/ticket/666

Original creator: pdenapo

Original creation time: 2007-09-16 18:43:39

Assignee: was

Currently, printing of matrices in Latex form is difficult to read. I'm submitting a (trivial) patch
that adds more spacing to increase readibility.

Example: 

```
sage: M=MatrixSpace(QQ,2,2)
sage: A=M([[2,3],[4,5]])
sage: latex(A)
```

currently gives:

```
\left(\begin{array}{rr}
2&3\\
4&5
\end{array}\right)
```

My patch changes this to 

```
\left(\begin{array}{rr}
2 & 3 \\
4 & 5
\end{array}\right)
```







---

Attachment


---

Comment by was created at 2007-09-21 02:40:03

Resolution: fixed
