# Issue 3373: ZZ division gives wrong sym_parent [new symbolics]

Issue created by migration from https://trac.sagemath.org/ticket/3373

Original creator: cwitty

Original creation time: 2008-06-05 20:07:17

Assignee: gfurnish

For x a ZZ variable, 1/x claims to be an integer:

```
sage: var('x', ZZ)
x
sage: (1/x).sym_parent()
Integer Ring
```


But in Sage, integer division always gives a rational:

```
sage: parent(1/1)
Rational Field
```



---

Comment by gfurnish created at 2008-07-18 09:06:48

Fixed in sage-symbolics rev #10235


---

Comment by gfurnish created at 2008-07-18 09:06:48

Resolution: fixed


---

Comment by was created at 2008-08-23 08:14:14

Milestone sage-symbolics deleted
