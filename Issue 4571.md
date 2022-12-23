# Issue 4571: merge sage's numpy.pxd with the cython numpy.pxd

Issue created by migration from https://trac.sagemath.org/ticket/4571

Original creator: jason

Original creation time: 2008-11-20 21:56:56

Assignee: mabshoff

CC:  robertwb dagss


```
[15:53] <robertwb> yep, we should merge them
```





---

Comment by robertwb created at 2009-06-28 09:00:20

See http://trac.cython.org/cython_trac/ticket/339


---

Attachment


---

Comment by robertwb created at 2009-06-28 09:02:28

Preliminary patch, need a new Cython spkg for it to work all the way.


---

Attachment

Here are some more fixes. With this, and the latest state of the

http://hg.cython.org/cython

repo, all the relevant tests seem to pass. I do get two failures (due to Cython upgrade? something else?), see test.log in

/home/dagss/sage-4.0.2-sage.math.washington.edu-x86_64-Linux

Once this works let's tag http://hg.cython.org/cython as 0.11.2.1 for #6438?


---

Comment by dagss created at 2009-07-07 15:57:04

Note (re: discussion on Cython ML) that shape in numpy.pxd is still a field, long story (well, it is performance critical), and I shouldn't change it.


---

Comment by dagss created at 2009-07-07 16:09:27

Another quick comment: With this, full Cython/NumPy functionality is available from the notebook and works well.


---

Comment by robertwb created at 2009-07-09 08:50:35

Those errors seem completely unrelated, I'll see if I get them too. Other than that, it looks really good. 

I've used Cython + NumPy from the notebook before, as long as you weren't in sage.ext then "cimport numpy" worked as expected (though there was a point where it didn't).


---

Comment by robertwb created at 2009-07-21 20:52:44

Hmm... I also got 


```
The following tests failed:

        sage -t -long devel/sage-main/sage/rings/polynomial/polynomial_template.pxi # 1 doctests failed
        sage -t -long devel/sage-main/sage/interfaces/sage0.py # 1 doctests failed

```



---

Comment by robertwb created at 2009-07-22 14:19:05

Changing component from build to numerical.


---

Comment by robertwb created at 2009-07-22 14:19:05

Looks good. The single doctest failure was minor, fixed in #6438.


---

Comment by mvngu created at 2009-07-22 16:21:52

Replying to [comment:4 dagss]:
> Here are some more fixes. With this, and the latest state of the
<SNIP>


The patch `4571-more-fixes.patch` doesn't contain a commit message and your username is not on the patch. Your username should follow the format:

```
Full Name <email@somewhere.com>
```

The username makes it easy to identify the patch, when it is committed, as your contribution.


---

Comment by mvngu created at 2009-07-23 02:23:03

With both patches applied in the following order:
 1. `4571-numpy-pxd.patch`
 1. `4571-more-fixes.patch`
I see the following build failure:

```
[mvngu@sage sage-4.1.1.alpha0]$ ./sage -br main

----------------------------------------------------------
sage: Building and installing modified Sage library files.


Installing c_lib
scons: `install' is up to date.
Updating Cython code....
Building modified file sage/finance/time_series.pyx.
Building modified file sage/matrix/change_ring.pyx.
Building modified file sage/matrix/matrix_complex_double_dense.pyx.
Building modified file sage/matrix/matrix_double_dense.pyx.
Building modified file sage/matrix/matrix_real_double_dense.pyx.
Building modified file sage/modules/vector_complex_double_dense.pyx.
Building modified file sage/modules/vector_double_dense.pyx.
Building modified file sage/modules/vector_real_double_dense.pyx.
Building sage/rings/polynomial/real_roots.pyx because it depends on sage/modules/vector_double_dense.pxd.
Building sage/stats/hmm/chmm.pyx because it depends on sage/matrix/matrix_double_dense.pxd.
Building sage/stats/hmm/hmm.pyx because it depends on sage/matrix/matrix_double_dense.pxd.
python `which cython` --embed-positions --incref-local-binop -I/scratch/mvngu/release/sage-4.1.1.alpha0/devel/sage-main -o sage/finance/time_series.c sage/finance/time_series.pyx
warning: /scratch/mvngu/release/sage-4.1.1.alpha0/devel/sage-main/sage/finance/time_series.pyx:1722:24: cdef variable 'j' declared after it is used

Error converting Pyrex file to C:
------------------------------------------------------------
...
            [20.0000, -3.0000, 4.5000, -2.0000]
        """
        cnumpy.import_array() #This must be called before using the numpy C/api or you will get segfault
        cdef cnumpy.npy_intp dims[1]
        dims[0] = self._length
        cdef cnumpy.ndarray n = cnumpy.PyArray_SimpleNewFromData(1, dims, cnumpy.NPY_DOUBLE, self._values)
                                                                       ^
------------------------------------------------------------

/scratch/mvngu/release/sage-4.1.1.alpha0/devel/sage-main/sage/finance/time_series.pyx:1862:72: Cannot convert 'numpy.npy_intp [1]' to Python object

Error converting Pyrex file to C:
------------------------------------------------------------
...
            [20.0000, -3.0000, 4.5000, -2.0000]
        """
        cnumpy.import_array() #This must be called before using the numpy C/api or you will get segfault
        cdef cnumpy.npy_intp dims[1]
        dims[0] = self._length
        cdef cnumpy.ndarray n = cnumpy.PyArray_SimpleNewFromData(1, dims, cnumpy.NPY_DOUBLE, self._values)
                                                                                                ^
------------------------------------------------------------

/scratch/mvngu/release/sage-4.1.1.alpha0/devel/sage-main/sage/finance/time_series.pyx:1862:97: Cannot convert 'double *' to Python object
Error running command, failed with status 256.
sage: There was an error installing modified sage library code.
```



---

Comment by robertwb created at 2009-07-23 08:50:21

Looks like it'll have to be rebased, worked fine on vanilla 4.1. Where's the .tar on sage.math?


---

Comment by mvngu created at 2009-07-23 08:53:59

Replying to [comment:13 robertwb]:
> Looks like it'll have to be rebased, worked fine on vanilla 4.1. Where's the .tar on sage.math? 
Source and binary versions are up at

http://sage.math.washington.edu/home/mvngu/release/sage-4.1.1.alpha0.tar


http://sage.math.washington.edu/home/mvngu/release/sage-4.1.1.alpha0-sage.math.washignton.edu-x86_64-Linux.tar.gz


---

Comment by robertwb created at 2009-07-25 12:07:43

Works fine form me. sage-4.1.1.alpha0-sage.math.washignton.edu-x86_64-Linux.tar.gz + #6438 + #4571. Are you sure applied the latest Cython spkg first? 4.1.1.alpha0 doesn't seem to have it.


---

Comment by mvngu created at 2009-07-25 15:45:02

Resolution: fixed


---

Comment by mvngu created at 2009-07-25 15:45:02

dagss: The patch `4571-more-fixes.patch` doesn't contain your username. I'm committing it in your name. Merged in this order
 1. the SPKG at #6438
 1. `4571-numpy-pxd.patch`
 1. `4571-more-fixes.patch`
