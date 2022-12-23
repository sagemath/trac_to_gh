# Issue 7753: Coxeter groups: more Bruhat and weak order features

Issue created by migration from https://trac.sagemath.org/ticket/7753

Original creator: nthiery

Original creation time: 2009-12-23 22:55:34

Assignee: nthiery

CC:  sage-combinat

Keywords: Bruhat order, Weak order

New methods:
 - bruhat_le (code inspired from code by Daniel Bump)
 - weak_le
 - bruhat_poset (finite Coxeter groups)
 - weak_poset   (finite Coxeter groups)

Improved doctests for related methods


---

Comment by nthiery created at 2009-12-23 23:16:20

Changing status from new to needs_review.


---

Comment by bump created at 2010-01-02 22:24:23

Changing status from needs_review to needs_work.


---

Comment by bump created at 2010-01-02 22:24:23

This patch implements the bruhat_order as a cached method and is badly needed.

With Sage 4.3, this raises an exception at the test in coxeter_groups.py, line 1010.

The definition of Q could be rewritten:


```
W = WeylGroup("B3")
sage: fcn = lambda x,y : x.bruhat_le(y)
sage: Q=Poset((W.list(),fcn))
```


Maybe the `?!?` should be removed from the `# long time` directive
a couple of lines later since it is unclear what it means.


---

Comment by nthiery created at 2010-01-04 15:47:51

Changing status from needs_work to needs_review.


---

Comment by nthiery created at 2010-01-04 15:47:51

Replying to [comment:2 bump]:
> This patch implements the bruhat_order as a cached method and is badly needed.
> 
> With Sage 4.3, this raises an exception at the test in coxeter_groups.py, line 1010.

Oops, I forgot that this depended on another patch; now #7842.  As you mention, this dependency is trivial though, so we can also work around it if #7842 is not merged instantly.

> Maybe the `?!?` should be removed from the `# long time` directive
> a couple of lines later since it is unclear what it means.

Fixed, and updated the # long time around that line. I was just surprised by how much time this was taking. We need more Weyl group optimizations!


---

Comment by nthiery created at 2010-01-04 18:10:09

Updated timings w.r.t. #7754 which is already in Sage


---

Attachment

By now this code is tested a lot, at least for finite Weyl groups, and
the previous reviewer comments were addressed. I am changing the
status to positive review.


---

Comment by bump created at 2010-01-07 14:18:37

Changing status from needs_review to positive_review.


---

Comment by rlm created at 2010-01-13 09:45:58

Resolution: fixed
