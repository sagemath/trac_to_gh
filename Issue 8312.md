# Issue 8312: speed up random_matrix creation

Issue created by migration from Trac.

Original creator: schilly

Original creation time: 2010-02-20 13:54:06

Assignee: jkantor

`random_matrix` is really slow. This ticket seeks to improve it's performance, probably by using cython, a better vectorized routine, Numpy's `random` function or something else. Notice, that besides Numpy, also Matlab and others are much faster.

Timings of Numpy's `random` with `random_matrix` on an Atom N270 netbook running Sage 4.3.2


```
sage: import numpy 
sage: matrix(numpy.random.normal(size=(1000,1000))) 
1000 x 1000 dense matrix over Real Double Field
sage: a = random_matrix(RDF, 1000, 1000)
sage: import numpy 
sage: %time _ = random_matrix(RDF, 1000, 1000)
CPU times: user 17.51 s, sys: 0.10 s, total: 17.61 s
Wall time: 18.43 s
sage: %time _ = matrix(numpy.random.normal(size=(1000,1000))) 
CPU times: user 0.40 s, sys: 0.04 s, total: 0.44 s
Wall time: 0.45 s
```


Related to that: a `random_element` in `MatrixSpace` 1000x1000 is also faster (but still slower than Numpy)

```
sage: v = MatrixSpace(RDF,1000,1000)
sage: %time _ = v.random_element()
CPU times: user 3.45 s, sys: 0.01 s, total: 3.46 s
Wall time: 3.46 s
```

