# Issue 4753: make sparse * sparse = dense mod p like 50 frickin' times faster.

Issue created by migration from https://trac.sagemath.org/ticket/4753

Original creator: was

Original creation time: 2008-12-11 02:36:08

Assignee: was

CC:  craigcitro

title says it all


---

Attachment


---

Comment by mhansen created at 2008-12-11 08:41:11

One issue is that in the patch, it should actually be 


```
            sage: type(c)
            <type 'sage.matrix.matrix_modn_dense.Matrix_modn_dense'>
```


Also, I'm curious as to where the big speedup comes from?  For example,


```
sage: %time a*a
CPU times: user 3.13 s, sys: 0.00 s, total: 3.13 s
Wall time: 3.25 s
100 x 100 sparse matrix over Finite Field of size 10007
sage: %time a._matrix_times_matrix_dense(a)
CPU times: user 0.16 s, sys: 0.00 s, total: 0.16 s
Wall time: 0.17 s
100 x 100 dense matrix over Finite Field of size 10007
```


Is it because you have a faster, more specialized underlying data structure?  Wouldn't it make more sense to add an optimized _mul_ method to matrix_modn_sparse and then have it do a normal (naive) conversion?


---

Comment by craigcitro created at 2008-12-11 09:09:20

This code wasn't ready for review yet -- William posted an initial patch after quickly writing some code in his office, and I'm going to clean it up and implement a few more things and post a patch tomorrow ...


---

Comment by mabshoff created at 2008-12-11 09:23:44

Replying to [comment:5 craigcitro]:
> This code wasn't ready for review yet -- William posted an initial patch after quickly writing some code in his office, and I'm going to clean it up and implement a few more things and post a patch tomorrow ...

I saw the patch, changed the subject, but did ping William about whether this code was supposed to be reviewed yet and didn't get an answer, so my bad :(

Cheers,

Michael


---

Comment by was created at 2008-12-12 00:06:59

> Is it because you have a faster, more specialized underlying data structure? 
> Wouldn't  it make more sense to add an optimized _mul_ method to
> matrix_modn_sparse and then have it do a normal (naive) conversion?

Definitely *not*.  Much of the time would likely be spent with setting and inserting entries in the sparse output, which is an insanely expensive datastructure compared to the super-fast dense data structure. 

That said, obviously a fast sparse*sparse = sparse should also be implemented, which would just be an easy cut and paste from Matrix_rational_sparse.

 -- william


---

Comment by craigcitro created at 2009-01-10 12:03:43

I'm adding a second patch, which does two things: 

 * cleans up the doctests for `_matrix_times_matrix_dense`
 * provides a fast `_matrix_times_matrix_`, so that `a*b` is now fast for a sparse mod N matrix `a`.

Now it's ready for review.


---

Attachment


---

Comment by craigcitro created at 2009-01-10 12:31:57

As Michael pointed out, it wouldn't hurt to have some comparison code.

BEFORE:

```
sage: m = random_matrix(GF(10007), 100, 100, sparse=True)

sage: %time m*m
CPU times: user 3.36 s, sys: 0.03 s, total: 3.39 s
Wall time: 3.42 s
100 x 100 sparse matrix over Finite Field of size 10007
```


AFTER:

```
sage: m = random_matrix(GF(10007), 100, 100, sparse=True)

sage: %time m*m
CPU times: user 0.09 s, sys: 0.00 s, total: 0.09 s
Wall time: 0.09 s
100 x 100 sparse matrix over Finite Field of size 10007
```



---

Comment by mabshoff created at 2009-01-10 13:13:48

Changing priority from major to critical.


---

Comment by mabshoff created at 2009-01-10 13:13:48

This patch set causes one doctest failure:

```
sage -t  "devel/sage/sage/modular/modsym/ambient.py"        
**********************************************************************
File "/scratch/mabshoff/sage-3.2.4.alpha0/devel/sage/sage/modular/modsym/ambient.py", line 20:
    sage: M.T(2).matrix().fcp('x')
Exception raised:
    Traceback (most recent call last):
      File "/home/mabshoff/build/sage-3.2.4-cycle/sage-3.2.4.alpha0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/mabshoff/build/sage-3.2.4-cycle/sage-3.2.4.alpha0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/mabshoff/build/sage-3.2.4-cycle/sage-3.2.4.alpha0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[6]>", line 1, in <module>
        M.T(Integer(2)).matrix().fcp('x')###line 20:
    sage: M.T(2).matrix().fcp('x')
      File "/scratch/mabshoff/sage-3.2.4.alpha0/local/lib/python2.5/site-packages/sage/modular/hecke/hecke_operator.py", line 459, in matrix
        self.__matrix = self.parent().hecke_matrix(self.__n)
      File "/scratch/mabshoff/sage-3.2.4.alpha0/local/lib/python2.5/site-packages/sage/modular/hecke/algebra.py", line 201, in hecke_matrix
        return self.__M.hecke_matrix(n)
      File "/scratch/mabshoff/sage-3.2.4.alpha0/local/lib/python2.5/site-packages/sage/modular/hecke/module.py", line 917, in hecke_matrix
        T = self._compute_hecke_matrix(n)
      File "/scratch/mabshoff/sage-3.2.4.alpha0/local/lib/python2.5/site-packages/sage/modular/hecke/module.py", line 117, in _compute_hecke_matrix
        return self._compute_hecke_matrix_prime(n)
      File "/scratch/mabshoff/sage-3.2.4.alpha0/local/lib/python2.5/site-packages/sage/modular/modsym/ambient.py", line 653, in _compute_hecke_matrix_prime
        Tp = W._matrix_times_matrix_dense(R)
      File "matrix_modn_sparse.pyx", line 370, in sage.matrix.matrix_modn_sparse.Matrix_modn_sparse._matrix_times_matrix_dense (sage/matrix/matrix_modn_sparse.c:6236)
    TypeError: Cannot convert sage.matrix.matrix_mod2_dense.Matrix_mod2_dense to sage.matrix.matrix_modn_dense.Matrix_modn_dense
**********************************************************************
```


Cheers,

Michael


---

Attachment


---

Comment by craigcitro created at 2009-01-11 09:00:10

Ok, new patch should fix that. The problem was fairly straightforward: we didn't think to test in the case of `GF(2)`, and in that case, the actual type for the result (`matrix_mod2_dense`) wasn't a subclass of `matrix_modn_dense`, so we were rightfully getting a type error.


---

Comment by was created at 2009-01-11 20:40:55

i applied all three patches to a clean sage-3.2.3 on sage.math and doctested matrix and got:

```
The following tests failed:

        sage -t  devel/sage/sage/matrix/matrix_modn_sparse.pyx # 2 doctests failed
        sage -t  devel/sage/sage/matrix/matrix2.pyx # 3 doctests failed
----------------------------------------------------------------------
Total time for all tests: 111.4 seconds
```



---

Comment by craigcitro created at 2009-01-12 04:49:55

Ok, problem solved. The issue is that `set_unsafe` take different input types for `matrix_modn_dense` and `matrix_mod2_dense` -- I only looked at the latter, mistakenly assuming they would be the same. 

I wised up, and tested `sage/matrix/` and `sage/modular/modsym` before posting -- no failures.


---

Attachment


---

Comment by mabshoff created at 2009-01-18 13:54:41

Resolution: fixed


---

Comment by mabshoff created at 2009-01-18 13:54:41

Merged all four patches in Sage 3.3.alpha0

Cheers,

Michael
