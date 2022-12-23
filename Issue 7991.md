# Issue 7991: Generic matrix testing -- left and right kernel

Issue created by migration from https://trac.sagemath.org/ticket/7991

Original creator: jason

Original creation time: 2010-01-19 03:39:28

Assignee: was

CC:  rbeezer

This patch implements generic testing for left and right kernels.  It exposes lots of bugs.


---

Attachment


---

Comment by jason created at 2010-01-19 03:44:39

Changing status from new to needs_work.


---

Comment by mkoeppe created at 2016-08-15 18:47:58

Just out of curiosity I have refreshed this patch.
----
New commits:


---

Comment by mkoeppe created at 2016-08-15 18:50:17


```
sage -t src/sage/matrix/
[...]
sage -t src/sage/matrix/matrix2.pyx
**********************************************************************
File "src/sage/matrix/matrix2.pyx", line 18, in sage.matrix.matrix2
Failed example:
    TestSuite(m).run()
Expected nothing
Got:
    Failure in _test_left_kernel:
    Traceback (most recent call last):
      File "/Users/mkoeppe/cvs/sage/local/lib/python2.7/site-packages/sage/misc/sage_unittest.py", line 283, in run
        test_method(tester = tester)
      File "sage/matrix/matrix2.pyx", line 4397, in sage.matrix.matrix2.Matrix._test_left_kernel (build/cythonized/sage/matrix/matrix2.c:30535)
        tester.assert_((V.basis_matrix()*self).is_zero())
      File "sage/structure/parent.pyx", line 855, in sage.structure.parent.Parent.__getattr__ (build/cythonized/sage/structure/parent.c:8322)
        attr = getattr_from_other_class(self, self._category.parent_class, name)
      File "sage/structure/misc.pyx", line 253, in sage.structure.misc.getattr_from_other_class (build/cythonized/sage/structure/misc.c:1772)
        raise dummy_attribute_error
    AttributeError: 'SubmoduleWithBasis_with_category' object has no attribute 'basis_matrix'
    ------------------------------------------------------------
    Failure in _test_right_kernel:
    Traceback (most recent call last):
      File "/Users/mkoeppe/cvs/sage/local/lib/python2.7/site-packages/sage/misc/sage_unittest.py", line 283, in run
        test_method(tester = tester)
      File "sage/matrix/matrix2.pyx", line 4226, in sage.matrix.matrix2.Matrix._test_right_kernel (build/cythonized/sage/matrix/matrix2.c:29805)
        tester.assert_((self*V.basis_matrix().transpose()).is_zero())
      File "sage/structure/parent.pyx", line 855, in sage.structure.parent.Parent.__getattr__ (build/cythonized/sage/structure/parent.c:8322)
        attr = getattr_from_other_class(self, self._category.parent_class, name)
      File "sage/structure/misc.pyx", line 253, in sage.structure.misc.getattr_from_other_class (build/cythonized/sage/structure/misc.c:1772)
        raise dummy_attribute_error
    AttributeError: 'SubmoduleWithBasis_with_category' object has no attribute 'basis_matrix'
    ------------------------------------------------------------
    The following tests failed: _test_left_kernel, _test_right_kernel
**********************************************************************
1 item had failures:
   1 of   3 in sage.matrix.matrix2
    [2223 tests, 1 failure, 13.93 s]
[...]
sage -t src/sage/matrix/matrix_dense.pyx
**********************************************************************
File "src/sage/matrix/matrix_dense.pyx", line 8, in sage.matrix.matrix_dense
Failed example:
    TestSuite(m).run()
Expected nothing
Got:
    Failure in _test_left_kernel:
    Traceback (most recent call last):
      File "/Users/mkoeppe/cvs/sage/local/lib/python2.7/site-packages/sage/misc/sage_unittest.py", line 283, in run
        test_method(tester = tester)
      File "sage/matrix/matrix2.pyx", line 4395, in sage.matrix.matrix2.Matrix._test_left_kernel (build/cythonized/sage/matrix/matrix2.c:30415)
        V=self.left_kernel()
      File "sage/matrix/matrix2.pyx", line 4375, in sage.matrix.matrix2.Matrix.left_kernel (build/cythonized/sage/matrix/matrix2.c:30201)
        K = self.transpose().right_kernel(*args, **kwds)
      File "sage/matrix/matrix2.pyx", line 4200, in sage.matrix.matrix2.Matrix.right_kernel (build/cythonized/sage/matrix/matrix2.c:29315)
        M = self.right_kernel_matrix(*args, **kwds)
      File "sage/matrix/matrix2.pyx", line 3816, in sage.matrix.matrix2.Matrix.right_kernel_matrix (build/cythonized/sage/matrix/matrix2.c:28309)
        format, M = self._right_kernel_matrix_over_domain()
      File "sage/matrix/matrix2.pyx", line 3212, in sage.matrix.matrix2.Matrix._right_kernel_matrix_over_domain (build/cythonized/sage/matrix/matrix2.c:25970)
        d, u, v = self.smith_form()
      File "sage/matrix/matrix2.pyx", line 13304, in sage.matrix.matrix2.Matrix.smith_form (build/cythonized/sage/matrix/matrix2.c:90592)
        u,t,v = _smith_onestep(self)
      File "sage/matrix/matrix2.pyx", line 14790, in sage.matrix.matrix2._smith_onestep (build/cythonized/sage/matrix/matrix2.c:104299)
        s,t,u = _smith_onestep(a.transpose())
      File "sage/matrix/matrix2.pyx", line 14779, in sage.matrix.matrix2._smith_onestep (build/cythonized/sage/matrix/matrix2.c:104011)
        left_mat, a = _generic_clear_column(a)
      File "sage/matrix/matrix2.pyx", line 14692, in sage.matrix.matrix2._generic_clear_column (build/cythonized/sage/matrix/matrix2.c:102379)
        raise ArithmeticError("Ideal %s not principal" % R.ideal(a[0,0], a[k,0]))
    ArithmeticError: Ideal Ideal (a, b^2) of Multivariate Polynomial Ring in a, b over Rational Field not principal
    ------------------------------------------------------------
    Failure in _test_right_kernel:
    Traceback (most recent call last):
      File "/Users/mkoeppe/cvs/sage/local/lib/python2.7/site-packages/sage/misc/sage_unittest.py", line 283, in run
        test_method(tester = tester)
      File "sage/matrix/matrix2.pyx", line 4224, in sage.matrix.matrix2.Matrix._test_right_kernel (build/cythonized/sage/matrix/matrix2.c:29685)
        V=self.right_kernel()
      File "sage/matrix/matrix2.pyx", line 4200, in sage.matrix.matrix2.Matrix.right_kernel (build/cythonized/sage/matrix/matrix2.c:29315)
        M = self.right_kernel_matrix(*args, **kwds)
      File "sage/matrix/matrix2.pyx", line 3816, in sage.matrix.matrix2.Matrix.right_kernel_matrix (build/cythonized/sage/matrix/matrix2.c:28309)
        format, M = self._right_kernel_matrix_over_domain()
      File "sage/matrix/matrix2.pyx", line 3212, in sage.matrix.matrix2.Matrix._right_kernel_matrix_over_domain (build/cythonized/sage/matrix/matrix2.c:25970)
        d, u, v = self.smith_form()
      File "sage/matrix/matrix2.pyx", line 13314, in sage.matrix.matrix2.Matrix.smith_form (build/cythonized/sage/matrix/matrix2.c:91076)
        dp, up, vp = _smith_diag(d)
      File "sage/matrix/matrix2.pyx", line 14604, in sage.matrix.matrix2._smith_diag (build/cythonized/sage/matrix/matrix2.c:100470)
        if len(t) > 1: raise ArithmeticError
    ArithmeticError
    ------------------------------------------------------------
    The following tests failed: _test_left_kernel, _test_right_kernel
**********************************************************************
1 item had failures:
   1 of   4 in sage.matrix.matrix_dense
    [39 tests, 1 failure, 0.50 s]
[...]
sage -t src/sage/matrix/matrix_generic_dense.pyx
**********************************************************************
File "src/sage/matrix/matrix_generic_dense.pyx", line 31, in sage.matrix.matrix_generic_dense.Matrix_generic_dense
Failed example:
    TestSuite(A).run()
Expected nothing
Got:
    Failure in _test_left_kernel:
    Traceback (most recent call last):
      File "/Users/mkoeppe/cvs/sage/local/lib/python2.7/site-packages/sage/misc/sage_unittest.py", line 283, in run
        test_method(tester = tester)
      File "sage/matrix/matrix2.pyx", line 4395, in sage.matrix.matrix2.Matrix._test_left_kernel (build/cythonized/sage/matrix/matrix2.c:30415)
        V=self.left_kernel()
      File "sage/matrix/matrix2.pyx", line 4375, in sage.matrix.matrix2.Matrix.left_kernel (build/cythonized/sage/matrix/matrix2.c:30201)
        K = self.transpose().right_kernel(*args, **kwds)
      File "sage/matrix/matrix2.pyx", line 4200, in sage.matrix.matrix2.Matrix.right_kernel (build/cythonized/sage/matrix/matrix2.c:29315)
        M = self.right_kernel_matrix(*args, **kwds)
      File "sage/matrix/matrix2.pyx", line 3819, in sage.matrix.matrix2.Matrix.right_kernel_matrix (build/cythonized/sage/matrix/matrix2.c:28407)
        raise NotImplementedError("Cannot compute a matrix kernel over %s" % R)
    NotImplementedError: Cannot compute a matrix kernel over Univariate Polynomial Ring in x over Ring of integers modulo 25
    ------------------------------------------------------------
    Failure in _test_right_kernel:
    Traceback (most recent call last):
      File "/Users/mkoeppe/cvs/sage/local/lib/python2.7/site-packages/sage/misc/sage_unittest.py", line 283, in run
        test_method(tester = tester)
      File "sage/matrix/matrix2.pyx", line 4224, in sage.matrix.matrix2.Matrix._test_right_kernel (build/cythonized/sage/matrix/matrix2.c:29685)
        V=self.right_kernel()
      File "sage/matrix/matrix2.pyx", line 4200, in sage.matrix.matrix2.Matrix.right_kernel (build/cythonized/sage/matrix/matrix2.c:29315)
        M = self.right_kernel_matrix(*args, **kwds)
      File "sage/matrix/matrix2.pyx", line 3819, in sage.matrix.matrix2.Matrix.right_kernel_matrix (build/cythonized/sage/matrix/matrix2.c:28407)
        raise NotImplementedError("Cannot compute a matrix kernel over %s" % R)
    NotImplementedError: Cannot compute a matrix kernel over Univariate Polynomial Ring in x over Ring of integers modulo 25
    ------------------------------------------------------------
    The following tests failed: _test_left_kernel, _test_right_kernel
```

