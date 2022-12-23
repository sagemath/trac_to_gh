# Issue 2774: [with patch, needs review] conversion from PolyBoRi to Singular

Issue created by migration from https://trac.sagemath.org/ticket/2774

Original creator: malb

Original creation time: 2008-04-02 16:09:06

Assignee: malb

CC:  burcin

Keywords: polybori


```
sage: B.<x,y> = BooleanPolynomialRing(2)
sage: B._singular_()
//   characteristic : 2
//   number of vars : 2
//        block   1 : ordering lp
//                  : names    x y
//        block   2 : ordering C
// quotient ring from ideal
_[1]=x2+x
_[2]=y2+y
```



---

Attachment

Looks good to me.


---

Comment by mabshoff created at 2008-04-04 22:15:05

Merged in Sage 3.0.alpha1


---

Comment by mabshoff created at 2008-04-04 22:15:05

Resolution: fixed
