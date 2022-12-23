# Issue 6454: improve sbox linear and differences matrices computation

Issue created by migration from https://trac.sagemath.org/ticket/6454

Original creator: ylchapuy

Original creation time: 2009-07-01 09:29:14

Assignee: somebody

CC:  malb

In particular, use walsh transform for linear_approximation_matrix.


---

Attachment


---

Comment by malb created at 2009-07-01 11:06:32

Hi there, it is embarrassing how bad my naive original code was. Here's a comparison (for the release tour)

**Old***


```
sage: S = mq.SR(1,4,4,8).sbox()
sage: %time _ = S.difference_distribution_matrix()
CPU times: user 82.14 s, sys: 0.01 s, total: 82.15 s
Wall time: 82.15 s

sage: %time _ = S.linear_approximation_matrix()
CPU times: user 145.10 s, sys: 0.02 s, total: 145.12 s
Wall time: 145.12 s
```


***New***


```
sage: S = mq.SR(1,4,4,8).sbox()
sage: %time _ = S.difference_distribution_matrix()
CPU times: user 0.32 s, sys: 0.00 s, total: 0.32 s
Wall time: 0.32 s
sage: %time _ = S.linear_approximation_matrix()
CPU times: user 1.10 s, sys: 0.00 s, total: 1.10 s
Wall time: 1.10 s
```


The code looks good, doctests pass.

The only issue: the `sage -coverage` script will pick up `_walsh_transform` and complain that it isn't documented and doctested. 

Of course it is impossible to doctest this inner function directly, but the keyword `# indirect doctest` will do the trick.

This is a positive review except for the missing documentation.


---

Attachment

Both patches should be applied.

I added an indirect doctest. I give myself a positive review, feel free to correct me if you disagree.


---

Comment by malb created at 2009-07-01 12:36:49

All good, definitively a positive review.


---

Comment by mvngu created at 2009-07-16 10:23:25

Just to let people know, this has been merged in sage-4.1.1-alpha0. I can't close this ticket because I don't have the privilege to do so. Sorry, folks :-(


---

Comment by mvngu created at 2009-07-16 21:31:06

Resolution: fixed
