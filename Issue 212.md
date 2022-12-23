# Issue 212: gsl matrix multiply too slow -- ???

Issue created by migration from https://trac.sagemath.org/ticket/212

Original creator: was

Original creation time: 2007-01-24 02:25:08

Assignee: was


```
sage: m = MatrixSpace(RDF,1000).random_element()
sage: time n=m.numpy('f')
CPU time: 2.97 s,  Wall time: 3.00 s
sage: import numpy
sage: time k=numpy.dot(n,n)
CPU time: 0.20 s,  Wall time: 0.11 s
sage: time z=m*m
CPU time: 3.69 s,  Wall time: 3.79 s
```



---

Comment by mabshoff created at 2007-08-22 20:20:45

The code snippet from above no longer works (maybe because numpy became part of Sage?):

```
sage: m = MatrixSpace(RDF,1000).random_element()
sage: time n=m.numpy('f')
---------------------------------------------------------------------------
<type 'exceptions.TypeError'>             Traceback (most recent call last)

/tmp/Work2/sage-2.8.1/sage-2.8.2.rc3/<ipython console> in <module>()

/tmp/Work2/sage-2.8.1/sage-2.8.2.rc3/local/lib/python2.5/site-packages/IPython/iplib.py in ipmagic(self, arg_s)
    962         else:
    963             magic_args = self.var_expand(magic_args,1)
--> 964             return fn(magic_args)
    965
    966     def ipalias(self,arg_s):

/tmp/Work2/sage-2.8.1/sage-2.8.2.rc3/local/lib/python2.5/site-packages/IPython/Magic.py in magic_time(self, parameter_s)
   1855         else:
   1856             st = clk()
-> 1857             exec code in glob
   1858             end = clk()
   1859             out = None

/tmp/Work2/sage-2.8.1/sage-2.8.2.rc3/<timed exec> in <module>()

<type 'exceptions.TypeError'>: numpy() takes no arguments (1 given)
sage: time z=m*m
CPU times: user 6.69 s, sys: 0.01 s, total: 6.70 s
Wall time: 6.74
```

I would also assume that the bad performance is due to the GSL BLAS. I did submit an ATLAS package to William Stein about a week ago. It builds in about 10 minutes on a current MacBook and about 12 minutes on an Opteron 3000. So could we consider making ATLAS an optional package that forces rebuilds of all packages that depend on BLAS?

Cheers,

Michael


---

Comment by cwitty created at 2007-10-27 22:48:03

See #1013 for the reason the test case no longer works.

Note that in the test case, numpy is using single-precision floating-point and GSL is using double-precision floating-point.

Here's a revised test case, that shows the timings I get on my laptop.  The timings are for numpy single-precision, numpy double-precision, and GSL double-precision, respectively.


```
sage: import numpy
sage: time n = sage.matrix.matrix1.Matrix.numpy(m, 'f')
CPU times: user 0.74 s, sys: 0.02 s, total: 0.76 s
Wall time: 0.76
sage: time k = numpy.dot(n, n)
CPU times: user 6.66 s, sys: 0.00 s, total: 6.66 s
Wall time: 6.66
sage: time n = sage.matrix.matrix1.Matrix.numpy(m, 'd')
CPU times: user 0.76 s, sys: 0.02 s, total: 0.78 s
Wall time: 0.79
sage: time k = numpy.dot(n, n)
CPU times: user 7.98 s, sys: 0.00 s, total: 7.98 s
Wall time: 8.14
sage: time z=m*m
CPU times: user 5.26 s, sys: 0.02 s, total: 5.28 s
Wall time: 5.38
```



---

Comment by was created at 2008-02-23 03:09:55

This is no longer valid, especially in light of carl witty's comments above and us switching to using ATLAS (on sage.math):

```
sage: m = MatrixSpace(RDF,1000).random_element()
sage: n = m.numpy()
sage: import numpy
sage: time k =numpy.dot(n,n)
CPU times: user 0.69 s, sys: 0.05 s, total: 0.74 s
Wall time: 0.79
sage: time z = m*m
CPU times: user 0.68 s, sys: 0.04 s, total: 0.72 s
Wall time: 0.72
```



---

Comment by was created at 2008-02-23 03:09:55

Resolution: fixed
