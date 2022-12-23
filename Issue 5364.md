# Issue 5364: unused maxima builtin functions for matrices over SR

Issue created by migration from https://trac.sagemath.org/ticket/5364

Original creator: ylchapuy

Original creation time: 2009-02-24 23:42:26

Assignee: was

some functions are not wraped which makes e.g. identity_matrix or transpose awfully slow for matrices over SR.
(we do not use maxime.ident nor maxima.transpose)




---

Comment by mhansen created at 2009-06-05 01:35:37

Resolution: invalid


---

Comment by mhansen created at 2009-06-05 01:35:37

This was fixed by converting symbolic matrices to use Sage's generic dense matrix backend:


```
sage: m = MatrixSpace(SR, 1000, 1000)
sage: %time a = m.identity_matrix()
CPU times: user 0.04 s, sys: 0.00 s, total: 0.04 s
Wall time: 0.04 s
sage: %time b = a.transpose()
CPU times: user 0.05 s, sys: 0.01 s, total: 0.06 s
Wall time: 0.06 s
```

