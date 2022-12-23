# Issue 5510: [with patch, not ready for review] update M4RI interface

Issue created by migration from https://trac.sagemath.org/ticket/5510

Original creator: malb

Original creation time: 2009-03-13 15:38:21

Assignee: malb

CC:  rhinton

Keywords: m4ri, linear algebra

The attached patch(es) update Sage's interface to work with the HG version of M4RI available at: http://bitbucket.org/malb/m4ri/

Also, a dedicated (faster) `rank()` function was added for dense matrices over GF(2).


---

Attachment

Patch requires SPKG at:

   http://sage.math.washington.edu/home/malb/spkgs/libm4ri-20090512.spkg

This update is a requirement for updating PolyBoRi to 0.6.


---

Comment by jason created at 2009-05-30 06:35:53

The spkg looks great.  Positive review for that.

The patch looks good to me as well.  Here are some timings:

BEFORE:

```
sage: A = random_matrix(GF(2), 1000, 1000) 
sage: timeit('B=A.copy(); B.rank()')
25 loops, best of 3: 8.42 ms per loop
sage: timeit('B=A.copy(); B.rank()')
25 loops, best of 3: 8.39 ms per loop
sage: A = matrix(GF(2),10, 0) 
sage: timeit('B=A.copy(); B.rank()')
625 loops, best of 3: 24.5 µs per loop
sage: timeit('B=A.copy(); B.rank()')
625 loops, best of 3: 24.3 µs per loop
```


AFTER

```
sage: A = random_matrix(GF(2), 1000, 1000) 
sage: timeit('B=A.copy(); B.rank()')
125 loops, best of 3: 6.05 ms per loop
sage: timeit('B=A.copy(); B.rank()')
125 loops, best of 3: 6.09 ms per loop
sage: A = matrix(GF(2),10, 0) 
sage: timeit('B=A.copy(); B.rank()')
625 loops, best of 3: 38.7 µs per loop
sage: timeit('B=A.copy(); B.rank()')
625 loops, best of 3: 40.1 µs per loop
```


Note that the rank of a zero matrix is significantly longer (i.e., twice as long).  Malb, can you comment?

If malb addresses this performance regression sufficiently, then this is a positive review as far as I'm concerned for both the spkg and the patch.


---

Comment by malb created at 2009-05-30 21:25:32

Here is the code that used to be called:


```
    def rank(self):
        x = self.fetch('rank')
        if not x is None: return x
        if self._nrows == 0 or self._ncols == 0:
            return 0
```



And here is the code that is called now:


```
    def rank(self):
        x = self.fetch('rank')
        if not x is None:
            return x
        if self._nrows == 0 or self._ncols == 0:
            return 0
```


i.e. they are identical and thus I have no idea to address this performance regression. Maybe the fetch is more expensive from a subclass or something? In any case, I don't think this should hold back the merge of this ticket.


---

Comment by malb created at 2009-06-07 13:37:49

Jason, can you comment on my reply?


---

Comment by jason created at 2009-06-09 19:04:31

I thought your patch had a new rank function (at the bottom of the patch).  Isn't that what is called now?


---

Comment by jason created at 2009-06-09 19:17:59

I re-ran my timings (on a different computer) in 4.0.  Here are the results:

BEFORE:

```
sage: A = matrix(GF(2),100, 100,0)
sage: timeit('A.rank(); A._clear_cache()')
625 loops, best of 3: 47.9 µs per loop
sage: A = matrix(GF(2),10, 10,0)
sage: timeit('A.rank(); A._clear_cache()')
625 loops, best of 3: 39.9 µs per loop
sage: A = matrix(GF(2),100, 100,0)
sage: timeit('A.rank(); A._clear_cache()')
625 loops, best of 3: 47.7 µs per loop
sage: A = matrix(GF(2),1000, 1000,0)
sage: timeit('A.rank(); A._clear_cache()')
625 loops, best of 3: 222 µs per loop
sage: A = random_matrix(GF(2), 1000)
sage: save(A,'m4ri.sobj')
sage: timeit('A.rank(); A._clear_cache()')
125 loops, best of 3: 6.85 ms per loop
sage: A = random_matrix(GF(2), 100)
sage: save(A,'m4ri2.sobj')
sage: timeit('A.rank(); A._clear_cache()')
625 loops, best of 3: 164 µs per loop
sage: A = random_matrix(GF(2), 10000)
sage: save(A,'m4ri3.sobj')
sage: timeit('A.rank(); A._clear_cache()')
5 loops, best of 3: 4.24 s per loop
```


AFTER

```
sage: A = matrix(GF(2),100, 100,0)
sage: timeit('A.rank(); A._clear_cache()')
625 loops, best of 3: 17.9 µs per loop
sage: A = matrix(GF(2),10, 10,0)
sage: timeit('A.rank(); A._clear_cache()')
625 loops, best of 3: 13.4 µs per loop
sage: A = matrix(GF(2),100, 100,0)
sage: timeit('A.rank(); A._clear_cache()')
625 loops, best of 3: 18.3 µs per loop
sage: A = matrix(GF(2),1000, 1000,0)
sage: timeit('A.rank(); A._clear_cache()')
625 loops, best of 3: 205 µs per loop
sage: A=load('./m4ri.sobj')
sage: timeit('A.rank(); A._clear_cache()')
125 loops, best of 3: 4.72 ms per loop
sage: A=load('./m4ri2.sobj')
sage: timeit('A.rank(); A._clear_cache()')
625 loops, best of 3: 115 µs per loop
sage: A=load('./m4ri3.sobj')
sage: timeit('A.rank(); A._clear_cache()')
5 loops, best of 3: 2.57 s per loop
```


The new code is a clear winner.  I don't know what was happening before, but it seems great now.  Positive review.


---

Comment by jason created at 2009-06-09 19:19:37

Ah, I think I know what was happening before.  I was creating a 10x0 matrix.  The copy was probably swamping the rank function.


---

Comment by jason created at 2009-06-09 19:22:13

So, for the tour: calculating the rank of a random 10,000x10,000 GF(2) matrix takes approximately half the time it used to.  Nice!


---

Comment by ncalexan created at 2009-06-13 22:07:03

The dependencies are definitely not correct.  Even after 'touch sage/matrix/*' I can't compile it.


```
sage/rings/polynomial/polynomial_gf2x.cpp: In function â��PyObject* __pyx_pf_4sage_5rings_10polynomial_15polynomial_gf2x_15Polynomial_GF2X_modular_compos                                                                                                                                                    sition(PyObject*, PyObject*, PyObject*)â��:
sage/rings/polynomial/polynomial_gf2x.cpp:10871: error: â��struct __pyx_obj_4sage_6matrix_17matrix_mod2_dense_Matrix_mod2_denseâ�� has no member named â��_en                                                                                                                                                ntriesâ��
sage/rings/polynomial/polynomial_gf2x.cpp:10941: error: â��struct __pyx_obj_4sage_6matrix_17matrix_mod2_dense_Matrix_mod2_denseâ�� has no member named â��_en                                                                                                                                                ntriesâ��
sage/rings/polynomial/polynomial_gf2x.cpp:11042: error: â��struct __pyx_obj_4sage_6matrix_17matrix_mod2_dense_Matrix_mod2_denseâ�� has no member named â��_en                                                                                                                                                ntriesâ��
sage/rings/polynomial/polynomial_gf2x.cpp:11227: error: â��struct __pyx_obj_4sage_6matrix_17matrix_mod2_dense_Matrix_mod2_denseâ�� has no member named â��_en                                                                                                                                                ntriesâ��
sage/rings/polynomial/polynomial_gf2x.cpp:11250: error: â��struct __pyx_obj_4sage_6matrix_17matrix_mod2_dense_Matrix_mod2_denseâ�� has no member named â��_en                                                                                                                                                ntriesâ��
sage/rings/polynomial/polynomial_gf2x.cpp:11475: error: â��struct __pyx_obj_4sage_6matrix_17matrix_mod2_dense_Matrix_mod2_denseâ�� has no member named â��_en                                                                                                                                                ntriesâ��
gcc -fno-strict-aliasing -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -fPIC -I/scratch/ncalexan/sage-4.0.2.alpha1/local/lib/python2.5/site-packages/numpy/core/include -I/scratch/ncalexan/sage-4.0.2.alpha1/local//include -I/scratch/ncalexan/sage-4.0.2.alpha1/local//include/csage -I/scratch/ncalexan/sage-4.0.2.alpha1/devel//sage/sage/ext -I/scratch/ncalexan/sage-4.0.2.alpha1/local/include/python2.5 -c sage/stats/hmm/chmm.c -o build/temp.linux-x86_64-2.5/sage/stats/hmm/chmm.o -w
gcc -pthread -shared build/temp.linux-x86_64-2.5/sage/matrix/matrix2.o -L/scratch/ncalexan/sage-4.0.2.alpha1/local//lib -lcsage -lstdc++ -lntl -o build/lib.linux-x86_64-2.5/sage/matrix/matrix2.so
gcc -fno-strict-aliasing -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -fPIC -I/scratch/ncalexan/sage-4.0.2.alpha1/local/lib/python2.5/site-packages/numpy/core/include -I/scratch/ncalexan/sage-4.0.2.alpha1/local//include -I/scratch/ncalexan/sage-4.0.2.alpha1/local//include/csage -I/scratch/ncalexan/sage-4.0.2.alpha1/devel//sage/sage/ext -I/scratch/ncalexan/sage-4.0.2.alpha1/local/include/python2.5 -c sage/stats/hmm/hmm.c -o build/temp.linux-x86_64-2.5/sage/stats/hmm/hmm.o -w
gcc -pthread -shared build/temp.linux-x86_64-2.5/sage/matrix/matrix_integer_dense.o -L/scratch/ncalexan/sage-4.0.2.alpha1/local//lib -lcsage -liml -lgmp -lm -lcblas -latlas -lstdc++ -lntl -o build/lib.linux-x86_64-2.5/sage/matrix/matrix_integer_dense.so
error: command 'gcc' failed with exit status 1
sage: There was an error installing modified sage library code.
```


After 'touch sage/polynomial/*' and a few retries, this still fails.  (I didn't try sage -ba.)  So I'm going to say needs work, to fix the dependencies.


---

Comment by jason created at 2009-06-13 22:42:18

You need to also install the spkg listed in the comments above.


---

Comment by ncalexan created at 2009-06-13 23:25:29

With the spkg, works perfectly.  Sorry for the confusion.


---

Comment by ncalexan created at 2009-06-13 23:25:29

Resolution: fixed
