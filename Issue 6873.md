# Issue 6873: *huge* bug in multivariate polynomial substitution

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-09-03 06:12:27

Assignee: malb

Observe:

```
sage: R.<x,y> = QQ[]
sage: f = x + 2*y
sage: f.subs(x=y,y=x)
3*y
sage: var('x,y')
sage: f = x + 2*y
sage: f.subs(x=y,y=x)
2*x + y
```


This is really really bad.   Notice in the first and second substitution that the semantics are completely wrong/inconsistent.  The semantics should be as in the second one in both cases.


---

Comment by malb created at 2009-09-03 11:24:01

This is a dupe of #6482.

I think the fix is to not check whether `b` in `a=b` is a monomial but whether it is constant. If it isn't a constant we should just fall back to `fast_map`.


---

Comment by malb created at 2009-09-09 20:13:49

Resolution: duplicate


---

Comment by malb created at 2009-09-09 20:13:49

Dupe of #6482
