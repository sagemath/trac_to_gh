# Issue 7315: Can only forget one GenericDeclaration at a time for some reason

Issue created by migration from Trac.

Original creator: kcrisman

Original creation time: 2009-10-26 19:56:08

Assignee: burcin

From [ this thread]: 

```
sage: var('m')
m
sage: var('n')
n
sage: assume(n, 'integer'); assume(m, 'integer')
sage: sin(n*pi).simplify()
0
sage: sin(m*pi).simplify()
0
sage: forget()
sage: sin(m*pi).simplify()
0
sage: sin(n*pi).simplify()
sin(pi*n)
```

The problem seems to lie in the last few lines of _forget_all in sage.symbolic.assumptions.py, where for some reason the loop isn't doing what it should.


---

Comment by kcrisman created at 2009-10-26 20:04:10

Unfortunately, #1163 doesn't fix this either.


---

Comment by kcrisman created at 2009-10-26 20:29:19

The problem is actually because list removal is called in GenericDeclaration.forget(), so this is about behavior of list iteration in Python when you remove elements:

```
>>> L=[1,2,3,4]
>>> for x in L:
...     L.remove(x)
...     x
...     L
... 
1
[2, 3, 4]
3
[2, 4]
```

So this piece of code is apparently using the wrong/un-Pythonic way of removing items from a list.


---

Attachment

Based on 4.2


---

Comment by kcrisman created at 2009-10-27 13:43:08

Changing status from new to needs_review.


---

Comment by kcrisman created at 2009-10-27 13:43:08

This patch should fix the issue.  In fact, it's only because #7084 finally allows more than one such declaration that this bug ever showed up!


---

Comment by jason created at 2009-10-29 19:36:44

Great catch.  Doctests and documentation passes.  Good work.


---

Comment by jason created at 2009-10-29 19:36:44

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2009-10-31 16:46:14

Resolution: fixed
