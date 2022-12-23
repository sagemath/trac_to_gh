# Issue 1037: arithmetic with Schubert polynomials includes extra fixed points in the permutations

Issue created by migration from https://trac.sagemath.org/ticket/1037

Original creator: mhansen

Original creation time: 2007-10-30 22:49:41

Assignee: was

CC:  sage-combinat

For example,


```
sage: X([3,2,1])*X([4,3,2,1])
X[6, 4, 2, 1, 3, 5, 7]
```


should be


```
sage: X([3,2,1])*X([4,3,2,1])
X[6, 4, 2, 1, 3, 5]
```



---

Comment by mhansen created at 2007-10-30 23:19:25

Changing priority from major to minor.


---

Comment by mabshoff created at 2007-11-01 09:22:16

Resolution: fixed


---

Attachment

applied to 2.8.11.alpha0


---

Comment by mabshoff created at 2007-11-01 09:22:16

Changing component from algebraic geometry to combinatorics.
