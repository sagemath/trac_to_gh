# Issue 4812: [with patch, needs review] matrix_plot is broken for matrices with "complicated" base rings

Issue created by migration from https://trac.sagemath.org/ticket/4812

Original creator: mhansen

Original creation time: 2008-12-16 11:51:31

Assignee: was


```
Hello all,

I'm trying to run the following code:

s     = 7
s2    = 2^s
P.<x> = GF(2)[]
M     = matrix(parent(x),s2)
for i in range(s2):
  p  = (1+x)^i
  pc = p.coeffs()
  a  = pc.count(1)
  for j in range(a):
    idx        = pc.index(1)
    M[i,idx+j] = pc.pop(idx)
matrixprogram = matrix_plot(M,cmap='Greys')

...but with 3.2.1, it complains:

---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)

/home/drake/.sage/temp/klee/11408/_tmp_foo_sage_2.py in <module>()
    16        M[i,idx+j] = pc.pop(idx)
    17
---> 18 matrixprogram = matrix_plot(M,cmap='Greys')     19
    20

/opt/sage-3.2.1/local/lib/python2.5/site-packages/sage/plot/misc.pyc in wrapper(*args, **kwds)
   279                 options['__original_opts'] = kwds
   280             options.update(kwds)
--> 281             return func(*args, **options)
   282
   283

/opt/sage-3.2.1/local/lib/python2.5/site-packages/sage/plot/matrix_plot.pyc in matrix_plot(mat, **options)
   123         xrange = (0, len(mat[0]))
   124         yrange = (0, len(mat))
--> 125     xy_data_array = [array(r, dtype=float) for r in mat]
   126
   127     g = Graphics()

/opt/sage-3.2.1/local/lib/python2.5/site-packages/numpy/oldnumeric/functions.pyc in array(sequence, typecode, copy, savespace, dtype)
    77 def array(sequence, typecode=None, copy=1, savespace=0, dtype=None):
    78     dtype = convtypecode2(typecode, dtype)
---> 79     return mu.array(sequence, dtype, copy=copy)
    80
    81 def sarray(a, typecode=None, copy=False, dtype=None):

ValueError: setting an array element with a sequence.


I know this used to work, because the example distributed with SageTeX
has it! See example.{tex,pdf} from
http://tug.ctan.org/tex-archive/macros/latex/contrib/sagetex/. Is the
above code still considered correct, or is there now a problem with
matrix_plot? The matrix M above has all 1's and 0's despite its parent
being GF(2)[x], so perhaps this is a coercion thing?
```



---

Comment by ddrake created at 2008-12-16 13:25:59

Code looks good, the SageTeX example file now works...positive review.


---

Comment by mabshoff created at 2008-12-17 14:35:25

This patch needs some fixing:

```
sage -t -long "devel/sage/sage/plot/matrix_plot.py"
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.2.2.rc1/devel/sage/sage/plot/matrix_plot.py", line 129:
    sage: matrix_plot(random_matrix(P, 3, 3))
Expected:
    Traceback (most recent call last):
    ...
    ValueError: can not convert array entries to floating point numbers
Got:
    Traceback (most recent call last):
      File "/scratch/mabshoff/release-cycle/sage-3.2.2.rc1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mabshoff/release-cycle/sage-3.2.2.rc1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mabshoff/release-cycle/sage-3.2.2.rc1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_3[15]>", line 1, in <module>
        matrix_plot(random_matrix(P, Integer(3), Integer(3)))###line 129:
    sage: matrix_plot(random_matrix(P, 3, 3))
      File "/scratch/mabshoff/release-cycle/sage-3.2.2.rc1/local/lib/python2.5/site-packages/sage/plot/misc.py", line 285, in wrapper
        return func(*args, **options)
      File "/scratch/mabshoff/release-cycle/sage-3.2.2.rc1/local/lib/python2.5/site-packages/sage/plot/matrix_plot.py", line 150, in matrix_plot
        mat = mat.change_ring(RDF).numpy()
      File "matrix0.pyx", line 888, in sage.matrix.matrix0.Matrix.change_ring (sage/matrix/matrix0.c:5304)
      File "/scratch/mabshoff/release-cycle/sage-3.2.2.rc1/local/lib/python2.5/site-packages/sage/matrix/matrix_space.py", line 354, in __call__
        return self.matrix(entries, copy=copy, coerce=coerce, rows=rows)
      File "/scratch/mabshoff/release-cycle/sage-3.2.2.rc1/local/lib/python2.5/site-packages/sage/matrix/matrix_space.py", line 979, in matrix
        return self.__matrix_class(self, entries=x, copy=copy, coerce=coerce)
      File "matrix_double_dense.pyx", line 222, in sage.matrix.matrix_double_dense.Matrix_double_dense.__init__ (sage/matrix/matrix_double_dense.c:2203)
      File "polynomial_element.pyx", line 649, in sage.rings.polynomial.polynomial_element.Polynomial.__float__ (sage/rings/polynomial/polynomial_element.c:7124)
    TypeError: cannot coerce nonconstant polynomial to float
**********************************************************************
1 items had failures:
   1 of  18 in __main__.example_3
***Test Failed*** 1 failures.
For whitespace errors, see the file /scratch/mabshoff/release-cycle/sage-3.2.2.rc1/tmp/.doctest_matrix_plot.py
         [5.1 s]
exit code: 1024
```

Dan: Please don't give positive reviews without at least doctesting all changed files ;)

The fix here seems obvious since only the traceback message has changed.

Cheers,

Michael


---

Attachment


---

Comment by mhansen created at 2008-12-22 16:37:56

Changing status from new to assigned.


---

Comment by mhansen created at 2008-12-22 16:37:56

I put up a new patch which fixes the issue above.


---

Comment by mhansen created at 2008-12-22 16:37:56

Changing assignee from was to mhansen.


---

Comment by mabshoff created at 2008-12-22 22:14:25

Merged in Sage 3.2.3.alpha0


---

Comment by mabshoff created at 2008-12-22 22:14:25

Resolution: fixed
