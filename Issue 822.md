# Issue 822: Some matrix multiplications inefficiencies

Issue created by migration from https://trac.sagemath.org/ticket/822

Original creator: jbmohler

Original creation time: 2007-10-04 09:51:37

Assignee: somebody

I've observed an errant base_extend call on matrix multiplies and also some unnecessary calls out to the python parent class.  The attached patch fixes both of these.  An example is below:


```
sage: M=MatrixSpace(ZZ,3,3)
sage: m=M([range(9)])
sage: n=M([range(1,10)])
sage: prun m*n
         20 function calls in 0.000 CPU seconds
   Ordered by: internal time
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        2    0.000    0.000    0.000    0.000 matrix_space.py:105(MatrixSpace)
        1    0.000    0.000    0.000    0.000 matrix_space.py:282(change_ring)
        1    0.000    0.000    0.000    0.000 matrix_space.py:306(base_extend)
        1    0.000    0.000    0.000    0.000 matrix_space.py:648
(matrix_space)
        3    0.000    0.000    0.000    0.000 matrix_space.py:670(ncols)
        3    0.000    0.000    0.000    0.000 matrix_space.py:681(nrows)
...
```



---

Attachment

matrix multiplication optimization


---

Comment by was created at 2007-10-04 17:57:27

Resolution: fixed


---

Comment by was created at 2007-10-04 17:57:27

This looks very good to me!
