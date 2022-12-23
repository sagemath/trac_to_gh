# Issue 9061: Fix broken inequalities in add_constraint method

Issue created by migration from https://trac.sagemath.org/ticket/9061

Original creator: ncohen

Original creation time: 2010-05-26 22:38:38

Assignee: jason, jkantor

CC:  mvngu abmasse

Inequalities using <= and >= still do not work properly... :-/

Nathann


---

Comment by jason created at 2010-05-28 00:28:10

Can you try `sage.misc.misc.balanced_sum`?  It seems to get about the same speedup for me as you indicate.


```
p = MixedIntegerLinearProgram()
v = p.new_variable()
%timeit sage.misc.misc.balanced_sum([v[i] for i in xrange(900)])
```



---

Comment by jason created at 2010-05-28 02:36:20

For me, the balanced_sum function gives these timings:


```
sage: p = MixedIntegerLinearProgram()
sage: v = p.new_variable()
sage: sage: %timeit sum([v[i] for i in xrange(900)])
5 loops, best of 3: 1.48 s per loop
sage: p = MixedIntegerLinearProgram()
sage: v = p.new_variable()
sage: %timeit sage.misc.misc.balanced_sum([v[i] for i in xrange(900)])
25 loops, best of 3: 28.2 ms per loop
```


So I guess your function still wins (which isn't much of a surprise).


---

Comment by ncohen created at 2010-06-15 17:00:43

Changing status from new to needs_review.


---

Comment by ncohen created at 2010-06-15 17:00:43

This patch defines the function sage.numerical.mip.Sum and updates the LP functions to have them use it !

Nathann


---

Comment by ncohen created at 2010-07-01 11:20:25

Changing status from needs_review to needs_work.


---

Comment by ncohen created at 2010-07-01 11:20:25

Rebased ! :-)

Nathann


---

Attachment

Hello, Nathann!

Did you rebase it on sage-4.4.3? It seems so because it doesn't apply on sage-4.4.4. Since it touches many parts of the code, I don't know what would be the best strategy to make sure it is correctly based and it does not raise any problem with other patches.

Having looked at the code, it will probably be a fast review, as soon as I have checked for the improved efficiency.


---

Comment by rlm created at 2010-07-06 08:20:38

Changing status from needs_work to positive_review.


---

Comment by rlm created at 2010-07-06 08:20:52

Resolution: fixed
