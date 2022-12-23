# Issue 4207: implement an is_close function for matrices and vectors

Issue created by migration from https://trac.sagemath.org/ticket/4207

Original creator: jason

Original creation time: 2008-09-27 10:23:19

Assignee: was

CC:  mjo vbraun ebray


```
[05:16] <mabshoff> One thing we should definitely do is to have some infrastructure to give a vector or matrix and check if all values are without $foo in some norm to a given vector or matrix
[05:16] <jason-> like numpy.allclose?
[05:17] <jason-> but that doesn't use norms
[05:17] <jason-> it just compares entry-wise
[05:17] <mabshoff> Well, we can do entry by entry or some vector/matrix norm.
[05:17] <jason-> well, you can't choose the norm.
[05:17] <mabshoff> the numpy.allclose would work in most cases, but we are mathematicians :)
[05:17] <mabshoff> So using a norm is natural IMHO
[05:18] <jason-> so matrix.is_close(other_matrix, norm='blah')
```



---

Comment by mjo created at 2019-07-21 19:53:48

We pretty much have this for both matrices and vectors:


```
sage: v1 = random_vector(RR,3)
sage: v2 = random_vector(RR,3)
sage: (v1 - v2).norm() < 10e-6
False
```



```
sage: M1 = random_matrix(RR,3,3)
sage: M2 = random_matrix(RR,3,3)
sage: (M1 - M2).norm() < 10e-6
False
```


Both support p-norms, and matrices additionally support the Frobenius norm. The examples above are how this stuff appears in the literature, so I don't think we gain much by giving it a dedicated method name.

Closable?
