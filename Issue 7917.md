# Issue 7917: [with patch, needs review] make gauss_sum() work for dirichlet characters when the base ring is CC

Issue created by migration from https://trac.sagemath.org/ticket/7917

Original creator: bober

Original creation time: 2010-01-13 06:22:56

Assignee: was

CC:  rishi

Keywords: dirichlet character gauss sum

This is a pretty small change. We add three lines to gauss_sum_numerical() to make it work when the base ring is a complex field, and change gauss_sum() to call gauss_sum_numerical() when the base ring is a complex field.

Note that it is actually much faster to compute the (approximate) gauss sum when the base ring is CC, as compared to when the base ring is a cyclotomic field.



```
sage: G = DirichletGroup(2981)
sage: chi = G.0
sage: timeit('chi.gauss_sum_numerical()')
5 loops, best of 3: 1.82 s per loop
sage: G = DirichletGroup(2981, ComplexField(200))
sage: chi = G.0                                  
sage: timeit('chi.gauss_sum_numerical()')        
25 loops, best of 3: 23.5 ms per loop
```




---

Attachment


---

Comment by roed created at 2012-09-17 05:37:22

Should this be marked as needs review?


---

Comment by pbruin created at 2015-08-19 14:28:16

This is superseded by #7191; I propose to close this as a duplicate.  There is only one small problem, namely that in the lines

```python
if rings.is_ComplexField(K):
    return self.gauss_sum_numerical(a=a)
```

the argument `a` was omitted in #7191.  This will be fixed in #19056.


---

Comment by pbruin created at 2015-08-19 14:28:16

Changing status from new to needs_review.


---

Comment by pbruin created at 2015-09-07 11:55:30

Now that #19056 is closed, I see no reason to keep this ticket open.


---

Comment by pbruin created at 2015-09-07 11:55:30

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2015-09-12 13:58:21

Resolution: invalid
