# Issue 7199: inefficiency of creation of sparse matrices

Issue created by migration from https://trac.sagemath.org/ticket/7199

Original creator: zimmerma

Original creation time: 2009-10-13 13:32:12

Assignee: was

The following was reported to me by David Monniaux.

```
sparseflag=True

def essai1():
    m=identity_matrix(QQ,dimen,sparse=sparseflag)
    compound=m
    for i in xrange(count):
        compound = compound.stack(m)

def essai2():
    m_rows=identity_matrix(QQ,dimen,sparse=sparseflag).rows()
    compound_l=[]
    for i in xrange(count):
        compound_l += m_rows
    m=Matrix(QQ,compound_l,sparse=sparseflag)

def essai3():
    m=identity_matrix(QQ,dimen,sparse=sparseflag)
    compound=Matrix(QQ,m.nrows()*count,m.ncols(),sparse=sparseflag)
    for i in xrange(count):
        compound[m.nrows()*i:m.nrows()*(i+1),:] = m
```

I get with Sage 4.1.1 on a 2.83Ghz Core 2:

```
sage: count=200
sage: dimen=30
sage: timeit('essai1()',number=1)
1 loops, best of 3: 33.1 s per loop
sage: timeit('essai2()',number=1)
1 loops, best of 3: 25.4 s per loop
sage: timeit('essai3()')
5 loops, best of 3: 820 ms per loop
```



---

Comment by zimmerma created at 2009-10-13 17:05:38

Another example (still from David Monniaux):

```
sage: count2=1000
sage: sparseflag=True
sage: def vessai1():
....:         v = vector(QQ,dimen)
....:     v[0]=1
....:     compound = Matrix(QQ, [v for i in xrange(count2)], sparse=sparseflag)
....: 
sage: def vessai2():
....:         v = vector(QQ,dimen)
....:     v[0]=1
....:     compound = Matrix(QQ, count2, dimen, sparse=sparseflag)
....:     for i in xrange(count2):
....:             compound[i,:] = v
sage: dimen=30
sage: timeit('vessai1()')
5 loops, best of 3: 168 ms per loop
sage: timeit('vessai2()')
25 loops, best of 3: 14.8 ms per loop
```



---

Comment by zimmerma created at 2010-02-05 20:34:38

still there in 4.3.1. No progress in 4 months!


---

Comment by robertwb created at 2010-02-05 21:50:33

Been busy with other stuff: http://trac.sagemath.org/sage_trac/query?status=closed&status=positive_review&order=priority&milestone=sage-4.3.2&milestone=sage-4.3.1&milestone=sage-4.3&milestone=sage-4.2.1&milestone=sage-4.2


---

Attachment


---

Comment by ylchapuy created at 2010-08-15 14:58:30

With the provided patch, `essai1` becomes faster than `essai3`.


---

Comment by ylchapuy created at 2010-08-15 14:58:30

Changing status from new to needs_review.


---

Comment by zimmerma created at 2010-09-01 20:27:49

Changing status from needs_review to positive_review.


---

Comment by zimmerma created at 2010-09-01 20:27:49

Replying to [comment:4 ylchapuy]:
> With the provided patch, `essai1` becomes faster than `essai3`.

I confirm, with Sage 4.4.4, still on a 2.83Ghz Core 2 (note however the regression in the timing for `essai3` between 4.1.1 and 4.4.4, which is independent from this patch):

```
sage: count=200
sage: dimen=30
sage: timeit('essai1()')
5 loops, best of 3: 431 ms per loop
sage: timeit('essai3()')
5 loops, best of 3: 1.18 s per loop
```


Good work,Yann!

Paul


---

Comment by mpatel created at 2010-09-15 09:54:36

Resolution: fixed
