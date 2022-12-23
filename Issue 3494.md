# Issue 3494: var --> name

Issue created by migration from https://trac.sagemath.org/ticket/3494

Original creator: craigcitro

Original creation time: 2008-06-23 18:49:35

Assignee: craigcitro

Lots of things that are matrix-related in `sage` use `var`, whereas `name` would often be more appropriate. Someone should fix this.


---

Comment by jason created at 2008-11-14 05:45:48

He's talking about the name of the keyword arguments.


```
[23:39] <jason--> craigcitro: 3494 is awfully vague
[23:39] <craigcitro> hah, true
[23:39] <craigcitro> but it's also sad that it's not uniform
[23:39] <craigcitro> the number of times i have to try three different things to find the right argument is sad
[23:40] <jason--> Can you at least point out one instance?
[23:41] <craigcitro> charpoly, minpoly, eigenspaces
[23:41] <jason--> mabshoff: what is the status on 3435?
[23:41] <craigcitro> whereas, say, PolynomialRing uses name
[23:41] <craigcitro> seems like it should just uniformly be name.
```



---

Comment by mkoeppe created at 2021-11-16 05:55:34

Outdated, too late to change it.


---

Comment by mkoeppe created at 2021-11-16 05:55:34

Changing status from new to needs_review.


---

Comment by klee created at 2021-11-16 08:32:34

Changing status from needs_review to positive_review.


---

Comment by klee created at 2021-11-16 08:32:34

I don't like the "too late" argument. But since we can do

```
sage: m = matrix(2,[1,2,3,4])
sage: var('y')
y
sage: m.charpoly(y)
y^2 - 5*y - 2
```

it is not clear if `name` is preferable than `var`. So let's close this ticket until we have a fresh discussion, which is too late perhaps...


---

Comment by mkoeppe created at 2021-11-20 23:57:15

Resolution: invalid
