# Issue 7991: Generic matrix testing -- left and right kernel

archive/issues_007991.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @rbeezer\n\nThis patch implements generic testing for left and right kernels.  It exposes lots of bugs.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7991\n\n",
    "created_at": "2010-01-19T03:39:28Z",
    "labels": [
        "linear algebra",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-7.4",
    "title": "Generic matrix testing -- left and right kernel",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7991",
    "user": "@jasongrout"
}
```
Assignee: @williamstein

CC:  @rbeezer

This patch implements generic testing for left and right kernels.  It exposes lots of bugs.

Issue created by migration from https://trac.sagemath.org/ticket/7991





---

archive/issue_comments_069796.json:
```json
{
    "body": "Attachment [trac-7991-generic-kernel-testing.patch](tarball://root/attachments/some-uuid/ticket7991/trac-7991-generic-kernel-testing.patch) by @jasongrout created at 2010-01-19 03:42:33",
    "created_at": "2010-01-19T03:42:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7991",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7991#issuecomment-69796",
    "user": "@jasongrout"
}
```

Attachment [trac-7991-generic-kernel-testing.patch](tarball://root/attachments/some-uuid/ticket7991/trac-7991-generic-kernel-testing.patch) by @jasongrout created at 2010-01-19 03:42:33



---

archive/issue_comments_069797.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2010-01-19T03:44:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7991",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7991#issuecomment-69797",
    "user": "@jasongrout"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_069798.json:
```json
{
    "body": "Just out of curiosity I have refreshed this patch.\n----\nNew commits:",
    "created_at": "2016-08-15T18:47:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7991",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7991#issuecomment-69798",
    "user": "@mkoeppe"
}
```

Just out of curiosity I have refreshed this patch.
----
New commits:



---

archive/issue_comments_069799.json:
```json
{
    "body": "\n```\nsage -t src/sage/matrix/\n[...]\nsage -t src/sage/matrix/matrix2.pyx\n**********************************************************************\nFile \"src/sage/matrix/matrix2.pyx\", line 18, in sage.matrix.matrix2\nFailed example:\n    TestSuite(m).run()\nExpected nothing\nGot:\n    Failure in _test_left_kernel:\n    Traceback (most recent call last):\n      File \"/Users/mkoeppe/cvs/sage/local/lib/python2.7/site-packages/sage/misc/sage_unittest.py\", line 283, in run\n        test_method(tester = tester)\n      File \"sage/matrix/matrix2.pyx\", line 4397, in sage.matrix.matrix2.Matrix._test_left_kernel (build/cythonized/sage/matrix/matrix2.c:30535)\n        tester.assert_((V.basis_matrix()*self).is_zero())\n      File \"sage/structure/parent.pyx\", line 855, in sage.structure.parent.Parent.__getattr__ (build/cythonized/sage/structure/parent.c:8322)\n        attr = getattr_from_other_class(self, self._category.parent_class, name)\n      File \"sage/structure/misc.pyx\", line 253, in sage.structure.misc.getattr_from_other_class (build/cythonized/sage/structure/misc.c:1772)\n        raise dummy_attribute_error\n    AttributeError: 'SubmoduleWithBasis_with_category' object has no attribute 'basis_matrix'\n    ------------------------------------------------------------\n    Failure in _test_right_kernel:\n    Traceback (most recent call last):\n      File \"/Users/mkoeppe/cvs/sage/local/lib/python2.7/site-packages/sage/misc/sage_unittest.py\", line 283, in run\n        test_method(tester = tester)\n      File \"sage/matrix/matrix2.pyx\", line 4226, in sage.matrix.matrix2.Matrix._test_right_kernel (build/cythonized/sage/matrix/matrix2.c:29805)\n        tester.assert_((self*V.basis_matrix().transpose()).is_zero())\n      File \"sage/structure/parent.pyx\", line 855, in sage.structure.parent.Parent.__getattr__ (build/cythonized/sage/structure/parent.c:8322)\n        attr = getattr_from_other_class(self, self._category.parent_class, name)\n      File \"sage/structure/misc.pyx\", line 253, in sage.structure.misc.getattr_from_other_class (build/cythonized/sage/structure/misc.c:1772)\n        raise dummy_attribute_error\n    AttributeError: 'SubmoduleWithBasis_with_category' object has no attribute 'basis_matrix'\n    ------------------------------------------------------------\n    The following tests failed: _test_left_kernel, _test_right_kernel\n**********************************************************************\n1 item had failures:\n   1 of   3 in sage.matrix.matrix2\n    [2223 tests, 1 failure, 13.93 s]\n[...]\nsage -t src/sage/matrix/matrix_dense.pyx\n**********************************************************************\nFile \"src/sage/matrix/matrix_dense.pyx\", line 8, in sage.matrix.matrix_dense\nFailed example:\n    TestSuite(m).run()\nExpected nothing\nGot:\n    Failure in _test_left_kernel:\n    Traceback (most recent call last):\n      File \"/Users/mkoeppe/cvs/sage/local/lib/python2.7/site-packages/sage/misc/sage_unittest.py\", line 283, in run\n        test_method(tester = tester)\n      File \"sage/matrix/matrix2.pyx\", line 4395, in sage.matrix.matrix2.Matrix._test_left_kernel (build/cythonized/sage/matrix/matrix2.c:30415)\n        V=self.left_kernel()\n      File \"sage/matrix/matrix2.pyx\", line 4375, in sage.matrix.matrix2.Matrix.left_kernel (build/cythonized/sage/matrix/matrix2.c:30201)\n        K = self.transpose().right_kernel(*args, **kwds)\n      File \"sage/matrix/matrix2.pyx\", line 4200, in sage.matrix.matrix2.Matrix.right_kernel (build/cythonized/sage/matrix/matrix2.c:29315)\n        M = self.right_kernel_matrix(*args, **kwds)\n      File \"sage/matrix/matrix2.pyx\", line 3816, in sage.matrix.matrix2.Matrix.right_kernel_matrix (build/cythonized/sage/matrix/matrix2.c:28309)\n        format, M = self._right_kernel_matrix_over_domain()\n      File \"sage/matrix/matrix2.pyx\", line 3212, in sage.matrix.matrix2.Matrix._right_kernel_matrix_over_domain (build/cythonized/sage/matrix/matrix2.c:25970)\n        d, u, v = self.smith_form()\n      File \"sage/matrix/matrix2.pyx\", line 13304, in sage.matrix.matrix2.Matrix.smith_form (build/cythonized/sage/matrix/matrix2.c:90592)\n        u,t,v = _smith_onestep(self)\n      File \"sage/matrix/matrix2.pyx\", line 14790, in sage.matrix.matrix2._smith_onestep (build/cythonized/sage/matrix/matrix2.c:104299)\n        s,t,u = _smith_onestep(a.transpose())\n      File \"sage/matrix/matrix2.pyx\", line 14779, in sage.matrix.matrix2._smith_onestep (build/cythonized/sage/matrix/matrix2.c:104011)\n        left_mat, a = _generic_clear_column(a)\n      File \"sage/matrix/matrix2.pyx\", line 14692, in sage.matrix.matrix2._generic_clear_column (build/cythonized/sage/matrix/matrix2.c:102379)\n        raise ArithmeticError(\"Ideal %s not principal\" % R.ideal(a[0,0], a[k,0]))\n    ArithmeticError: Ideal Ideal (a, b^2) of Multivariate Polynomial Ring in a, b over Rational Field not principal\n    ------------------------------------------------------------\n    Failure in _test_right_kernel:\n    Traceback (most recent call last):\n      File \"/Users/mkoeppe/cvs/sage/local/lib/python2.7/site-packages/sage/misc/sage_unittest.py\", line 283, in run\n        test_method(tester = tester)\n      File \"sage/matrix/matrix2.pyx\", line 4224, in sage.matrix.matrix2.Matrix._test_right_kernel (build/cythonized/sage/matrix/matrix2.c:29685)\n        V=self.right_kernel()\n      File \"sage/matrix/matrix2.pyx\", line 4200, in sage.matrix.matrix2.Matrix.right_kernel (build/cythonized/sage/matrix/matrix2.c:29315)\n        M = self.right_kernel_matrix(*args, **kwds)\n      File \"sage/matrix/matrix2.pyx\", line 3816, in sage.matrix.matrix2.Matrix.right_kernel_matrix (build/cythonized/sage/matrix/matrix2.c:28309)\n        format, M = self._right_kernel_matrix_over_domain()\n      File \"sage/matrix/matrix2.pyx\", line 3212, in sage.matrix.matrix2.Matrix._right_kernel_matrix_over_domain (build/cythonized/sage/matrix/matrix2.c:25970)\n        d, u, v = self.smith_form()\n      File \"sage/matrix/matrix2.pyx\", line 13314, in sage.matrix.matrix2.Matrix.smith_form (build/cythonized/sage/matrix/matrix2.c:91076)\n        dp, up, vp = _smith_diag(d)\n      File \"sage/matrix/matrix2.pyx\", line 14604, in sage.matrix.matrix2._smith_diag (build/cythonized/sage/matrix/matrix2.c:100470)\n        if len(t) > 1: raise ArithmeticError\n    ArithmeticError\n    ------------------------------------------------------------\n    The following tests failed: _test_left_kernel, _test_right_kernel\n**********************************************************************\n1 item had failures:\n   1 of   4 in sage.matrix.matrix_dense\n    [39 tests, 1 failure, 0.50 s]\n[...]\nsage -t src/sage/matrix/matrix_generic_dense.pyx\n**********************************************************************\nFile \"src/sage/matrix/matrix_generic_dense.pyx\", line 31, in sage.matrix.matrix_generic_dense.Matrix_generic_dense\nFailed example:\n    TestSuite(A).run()\nExpected nothing\nGot:\n    Failure in _test_left_kernel:\n    Traceback (most recent call last):\n      File \"/Users/mkoeppe/cvs/sage/local/lib/python2.7/site-packages/sage/misc/sage_unittest.py\", line 283, in run\n        test_method(tester = tester)\n      File \"sage/matrix/matrix2.pyx\", line 4395, in sage.matrix.matrix2.Matrix._test_left_kernel (build/cythonized/sage/matrix/matrix2.c:30415)\n        V=self.left_kernel()\n      File \"sage/matrix/matrix2.pyx\", line 4375, in sage.matrix.matrix2.Matrix.left_kernel (build/cythonized/sage/matrix/matrix2.c:30201)\n        K = self.transpose().right_kernel(*args, **kwds)\n      File \"sage/matrix/matrix2.pyx\", line 4200, in sage.matrix.matrix2.Matrix.right_kernel (build/cythonized/sage/matrix/matrix2.c:29315)\n        M = self.right_kernel_matrix(*args, **kwds)\n      File \"sage/matrix/matrix2.pyx\", line 3819, in sage.matrix.matrix2.Matrix.right_kernel_matrix (build/cythonized/sage/matrix/matrix2.c:28407)\n        raise NotImplementedError(\"Cannot compute a matrix kernel over %s\" % R)\n    NotImplementedError: Cannot compute a matrix kernel over Univariate Polynomial Ring in x over Ring of integers modulo 25\n    ------------------------------------------------------------\n    Failure in _test_right_kernel:\n    Traceback (most recent call last):\n      File \"/Users/mkoeppe/cvs/sage/local/lib/python2.7/site-packages/sage/misc/sage_unittest.py\", line 283, in run\n        test_method(tester = tester)\n      File \"sage/matrix/matrix2.pyx\", line 4224, in sage.matrix.matrix2.Matrix._test_right_kernel (build/cythonized/sage/matrix/matrix2.c:29685)\n        V=self.right_kernel()\n      File \"sage/matrix/matrix2.pyx\", line 4200, in sage.matrix.matrix2.Matrix.right_kernel (build/cythonized/sage/matrix/matrix2.c:29315)\n        M = self.right_kernel_matrix(*args, **kwds)\n      File \"sage/matrix/matrix2.pyx\", line 3819, in sage.matrix.matrix2.Matrix.right_kernel_matrix (build/cythonized/sage/matrix/matrix2.c:28407)\n        raise NotImplementedError(\"Cannot compute a matrix kernel over %s\" % R)\n    NotImplementedError: Cannot compute a matrix kernel over Univariate Polynomial Ring in x over Ring of integers modulo 25\n    ------------------------------------------------------------\n    The following tests failed: _test_left_kernel, _test_right_kernel\n```\n",
    "created_at": "2016-08-15T18:50:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7991",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7991#issuecomment-69799",
    "user": "@mkoeppe"
}
```


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

