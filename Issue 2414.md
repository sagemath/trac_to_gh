# Issue 2414: there should be a conversion from X.fraction_field() to X (esp. for multivariate polynomials)

Issue created by migration from https://trac.sagemath.org/ticket/2414

Original creator: cwitty

Original creation time: 2008-03-07 02:29:19

Assignee: somebody


```
sage: R.<x,y> = QQ[]
sage: R(x/y*y)
```

goes boom; it should return x.


---

Comment by jbmohler created at 2008-03-19 12:26:26

I cannot reproduce this in 2.10.4.  Has it really just been fixed in the last two weeks?


---

Comment by cwitty created at 2008-03-21 06:20:03

Resolution: fixed


---

Comment by cwitty created at 2008-03-21 06:20:03

Yes, this example was fixed in 2.10.3 by #1186, and I can't find any other examples with problems, so I'm declaring this bug fixed.
