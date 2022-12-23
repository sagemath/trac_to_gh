# Issue 4039: choose one name for  partial fraction decompositions

Issue created by migration from https://trac.sagemath.org/ticket/4039

Original creator: jason

Original creation time: 2008-09-02 15:41:20

Assignee: tbd

Two different ways to do partial fractions should have the same function name:


```
sage: x=polygen(QQ)
sage: f=(x - 3)/((x +1)*(x-1))
sage: f.partial_fraction_decomposition()
(0, [-1/(x - 1), 2/(x + 1)])
sage: x=var('x')
sage: f=(x - 3)/((x +1)*(x-1))
sage: f.partial_fraction()
2/(x + 1) - 1/(x - 1)
```


An added bonus would be if they gave similar output (currently one gives a list, the other gives an expression).


---

Comment by robertwb created at 2010-09-18 23:38:28

Note that there's no way to "symbolically" unevaluated sums of fraction field elements in Frac(QQ[x])


---

Comment by chapoton created at 2020-06-25 18:45:46

Changing status from new to needs_review.


---

Comment by chapoton created at 2020-06-25 18:45:46

New commits:


---

Comment by mkoeppe created at 2020-06-25 18:52:37

Returning the result as a `FormalSum` could also be nice


---

Comment by mkoeppe created at 2020-07-09 01:31:44

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2020-07-10 19:34:19

Resolution: fixed
