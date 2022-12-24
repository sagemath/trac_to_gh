# Issue 7723: Sparse matrices for double fields

archive/issues_007723.json:
```json
{
    "body": "Assignee: jkantor\n\nHere's the beginnings of my work on sparse double matrices.\n\nThis is based on 4.3.rc0. Note that I have *not* run the entire Sage test suite,\nonly tests in the matrix package. I'm happy to run the entire suite once I know\nthe final revision this will be rebased to, but 4.3.rc0 produces a few test\nfailures in itself (=noise I'm not bothering with for the moment).\n\nThere are three patches, which should be applied and reviewed in this order:\n\n- generic_multiply lets one override matrix multiplication with\n  different parents.  This is in a seperate patch because it changes\n  structure/element.pxd, causing a big recompile.\n\n- double_sparse is the main new classes\n\n- coo_format changes the matrix constructor to accept \"coo=...\" (see docstring\n  in patch)\n\nMore comments:\n\n- I will not introduce seperate classes for real and complex -- there\n  will be other subclasses (Hermitian, strictly-diagonal etc.) and I\n  don't want to double the size of the hierarchy. There are other\n  (and better) ways to get efficient getitem/setitem without a speed\n  penalty (such as introducing a seperate ItemAccessor protocol/class\n  -- though for sparse matrices an if-test won't matter either).\n\n- Once this is accepted (and I have a general feel for what I do\n  right and wrong) I hope to continue with solvers etc. (as I scratch my itches).\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7723\n\n",
    "created_at": "2009-12-17T13:47:31Z",
    "labels": [
        "numerical",
        "major",
        "enhancement"
    ],
    "title": "Sparse matrices for double fields",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7723",
    "user": "dagss"
}
```
Assignee: jkantor

Here's the beginnings of my work on sparse double matrices.

This is based on 4.3.rc0. Note that I have *not* run the entire Sage test suite,
only tests in the matrix package. I'm happy to run the entire suite once I know
the final revision this will be rebased to, but 4.3.rc0 produces a few test
failures in itself (=noise I'm not bothering with for the moment).

There are three patches, which should be applied and reviewed in this order:

- generic_multiply lets one override matrix multiplication with
  different parents.  This is in a seperate patch because it changes
  structure/element.pxd, causing a big recompile.

- double_sparse is the main new classes

- coo_format changes the matrix constructor to accept "coo=..." (see docstring
  in patch)

More comments:

- I will not introduce seperate classes for real and complex -- there
  will be other subclasses (Hermitian, strictly-diagonal etc.) and I
  don't want to double the size of the hierarchy. There are other
  (and better) ways to get efficient getitem/setitem without a speed
  penalty (such as introducing a seperate ItemAccessor protocol/class
  -- though for sparse matrices an if-test won't matter either).

- Once this is accepted (and I have a general feel for what I do
  right and wrong) I hope to continue with solvers etc. (as I scratch my itches).



Issue created by migration from https://trac.sagemath.org/ticket/7723





---

archive/issue_comments_066337.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-12-17T13:50:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7723",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7723#issuecomment-66337",
    "user": "dagss"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_066338.json:
```json
{
    "body": "Changing component from numerical to linear algebra.",
    "created_at": "2009-12-17T13:50:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7723",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7723#issuecomment-66338",
    "user": "dagss"
}
```

Changing component from numerical to linear algebra.



---

archive/issue_comments_066339.json:
```json
{
    "body": "Attachment [trac_7723-coo_format.patch](tarball://root/attachments/some-uuid/ticket7723/trac_7723-coo_format.patch) by dagss created at 2009-12-17 14:11:49",
    "created_at": "2009-12-17T14:11:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7723",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7723#issuecomment-66339",
    "user": "dagss"
}
```

Attachment [trac_7723-coo_format.patch](tarball://root/attachments/some-uuid/ticket7723/trac_7723-coo_format.patch) by dagss created at 2009-12-17 14:11:49



---

archive/issue_comments_066340.json:
```json
{
    "body": "Attachment [trac_7723-double_sparse.patch](tarball://root/attachments/some-uuid/ticket7723/trac_7723-double_sparse.patch) by dagss created at 2009-12-17 14:12:06",
    "created_at": "2009-12-17T14:12:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7723",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7723#issuecomment-66340",
    "user": "dagss"
}
```

Attachment [trac_7723-double_sparse.patch](tarball://root/attachments/some-uuid/ticket7723/trac_7723-double_sparse.patch) by dagss created at 2009-12-17 14:12:06



---

archive/issue_comments_066341.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2009-12-19T20:32:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7723",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7723#issuecomment-66341",
    "user": "was"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_066342.json:
```json
{
    "body": "Attachment [trac_7723-generic_multiply.patch](tarball://root/attachments/some-uuid/ticket7723/trac_7723-generic_multiply.patch) by was created at 2009-12-19 20:32:38\n\nREFEREE REPORT:\n\n* trac_7723-generic_multiply.patch: \n\nLooks good, except there is a missing word \"have\" in this documentation:\n\n```\n3485\t        The matrices should both the same base ring and either both \n3486\t        should be dense or both sparse. \n```\n\nThis doesn't cause any doctest failures, and factoring this code out is a good idea. \n\n* trac_7723-double_sparse.patch\n\nLooks good.\n\n\n* trac_7723-coo_format.patch \n\nThis causes a bunch of doctest failures:\n\n\n```\nwstein@sage:~/build/referee/sage-4.3.rc0$         sage -t  devel/sage/sage/matrix/matrix_integer_2x2.pyx # 5 doctests failed\nsage -t  \"devel/sage/sage/matrix/matrix_integer_2x2.pyx\"    \n**********************************************************************\nFile \"/scratch/wstein/build/referee/sage-4.3.rc0/devel/sage/sage/matrix/matrix_integer_2x2.pyx\", line 266:\n    sage: m.__iter__()\nExpected:\n    <listiterator object at ...>\nGot:\n    <generator object row_iterator at 0x3ddab90>\n**********************************************************************\nFile \"/scratch/wstein/build/referee/sage-4.3.rc0/devel/sage/sage/matrix/matrix_integer_2x2.pyx\", line 397:\n    sage: m.__invert__unit()\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/wstein/build/referee/sage-4.3.rc0/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/scratch/wstein/build/referee/sage-4.3.rc0/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/scratch/wstein/build/referee/sage-4.3.rc0/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_19[4]>\", line 1, in <module>\n        m.__invert__unit()###line 397:\n    sage: m.__invert__unit()\n    AttributeError: 'sage.matrix.matrix_integer_dense.Matrix_integer_de' object has no attribute '__invert__unit'\n**********************************************************************\nFile \"/scratch/wstein/build/referee/sage-4.3.rc0/devel/sage/sage/matrix/matrix_integer_2x2.pyx\", line 400:\n    sage: type(m.__invert__unit())\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/wstein/build/referee/sage-4.3.rc0/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/scratch/wstein/build/referee/sage-4.3.rc0/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/scratch/wstein/build/referee/sage-4.3.rc0/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_19[5]>\", line 1, in <module>\n        type(m.__invert__unit())###line 400:\n    sage: type(m.__invert__unit())\n    AttributeError: 'sage.matrix.matrix_integer_dense.Matrix_integer_de' object has no attribute '__invert__unit'\n**********************************************************************\nFile \"/scratch/wstein/build/referee/sage-4.3.rc0/devel/sage/sage/matrix/matrix_integer_2x2.pyx\", line 407:\n    sage: m.__invert__unit() == m^-1\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/wstein/build/referee/sage-4.3.rc0/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/scratch/wstein/build/referee/sage-4.3.rc0/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/scratch/wstein/build/referee/sage-4.3.rc0/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_19[8]>\", line 1, in <module>\n        m.__invert__unit() == m**-Integer(1)###line 407:\n    sage: m.__invert__unit() == m^-1\n    AttributeError: 'sage.matrix.matrix_integer_dense.Matrix_integer_de' object has no attribute '__invert__unit'\n**********************************************************************\nFile \"/scratch/wstein/build/referee/sage-4.3.rc0/devel/sage/sage/matrix/matrix_integer_2x2.pyx\", line 409:\n    sage: M([2,0,0,2]).__invert__unit()\nExpected:\n    Traceback (most recent call last):\n    ...\n    ZeroDivisionError: Not a unit!\nGot:\n    Traceback (most recent call last):\n      File \"/scratch/wstein/build/referee/sage-4.3.rc0/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/scratch/wstein/build/referee/sage-4.3.rc0/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/scratch/wstein/build/referee/sage-4.3.rc0/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_19[9]>\", line 1, in <module>\n        M([Integer(2),Integer(0),Integer(0),Integer(2)]).__invert__unit()###line 409:\n    sage: M([2,0,0,2]).__invert__unit()\n    AttributeError: 'sage.matrix.matrix_integer_dense.Matrix_integer_de' object has no attribute '__invert__unit'\n**********************************************************************\n2 items had failures:\n   1 of   5 in __main__.example_13\n   4 of  10 in __main__.example_19\n***Test Failed*** 5 failures.\nFor whitespace errors, see the file /scratch/wstein/sage//tmp/.doctest_matrix_integer_2x2.py\n         [1.5 s]\nexit code: 1024\n \n----------------------------------------------------------------------\nThe following tests failed:\n\n\n        sage -t  \"devel/sage/sage/matrix/matrix_integer_2x2.pyx\"\nTotal time for all tests: 1.5 seconds\n```\n\n\n\nI noticed a *massive* performance regression as a result of your patches:\n\n```\nOLD SAGE:\nsage: s = random_matrix(RDF,100)\nsage: time t =s*s\nCPU times: user 0.01 s, sys: 0.00 s, total: 0.01 s\nWall time: 0.15 s\n\n\nWITH YOUR PATCHES:\nsage: s = random_matrix(RDF,100)\nsage: time t =s*s\nCPU times: user 0.91 s, sys: 0.00 s, total: 0.91 s\nWall time: 0.91 s\n```\n\n\nOuch.  These are both dense matrices.  There must be something that got seriously messed up with re-factoring?\n\n* Why is there a backslash here in `matrix_double_sparse.pyx`:\n\n```\n        either as a single list of length ``nrows\\*ncols``, or as a \n```\n\n\n\n---\n\nOverall I'm very happy and excited about this patch!!  I'm really, really glad you're working on this, and would like to do anything I can to encourage this.  It is critically valuable to the Sage project to get much better numerical sparse matrix support.",
    "created_at": "2009-12-19T20:32:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7723",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7723#issuecomment-66342",
    "user": "was"
}
```

Attachment [trac_7723-generic_multiply.patch](tarball://root/attachments/some-uuid/ticket7723/trac_7723-generic_multiply.patch) by was created at 2009-12-19 20:32:38

REFEREE REPORT:

* trac_7723-generic_multiply.patch: 

Looks good, except there is a missing word "have" in this documentation:

```
3485	        The matrices should both the same base ring and either both 
3486	        should be dense or both sparse. 
```

This doesn't cause any doctest failures, and factoring this code out is a good idea. 

* trac_7723-double_sparse.patch

Looks good.


* trac_7723-coo_format.patch 

This causes a bunch of doctest failures:


```
wstein@sage:~/build/referee/sage-4.3.rc0$         sage -t  devel/sage/sage/matrix/matrix_integer_2x2.pyx # 5 doctests failed
sage -t  "devel/sage/sage/matrix/matrix_integer_2x2.pyx"    
**********************************************************************
File "/scratch/wstein/build/referee/sage-4.3.rc0/devel/sage/sage/matrix/matrix_integer_2x2.pyx", line 266:
    sage: m.__iter__()
Expected:
    <listiterator object at ...>
Got:
    <generator object row_iterator at 0x3ddab90>
**********************************************************************
File "/scratch/wstein/build/referee/sage-4.3.rc0/devel/sage/sage/matrix/matrix_integer_2x2.pyx", line 397:
    sage: m.__invert__unit()
Exception raised:
    Traceback (most recent call last):
      File "/scratch/wstein/build/referee/sage-4.3.rc0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/wstein/build/referee/sage-4.3.rc0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/wstein/build/referee/sage-4.3.rc0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_19[4]>", line 1, in <module>
        m.__invert__unit()###line 397:
    sage: m.__invert__unit()
    AttributeError: 'sage.matrix.matrix_integer_dense.Matrix_integer_de' object has no attribute '__invert__unit'
**********************************************************************
File "/scratch/wstein/build/referee/sage-4.3.rc0/devel/sage/sage/matrix/matrix_integer_2x2.pyx", line 400:
    sage: type(m.__invert__unit())
Exception raised:
    Traceback (most recent call last):
      File "/scratch/wstein/build/referee/sage-4.3.rc0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/wstein/build/referee/sage-4.3.rc0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/wstein/build/referee/sage-4.3.rc0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_19[5]>", line 1, in <module>
        type(m.__invert__unit())###line 400:
    sage: type(m.__invert__unit())
    AttributeError: 'sage.matrix.matrix_integer_dense.Matrix_integer_de' object has no attribute '__invert__unit'
**********************************************************************
File "/scratch/wstein/build/referee/sage-4.3.rc0/devel/sage/sage/matrix/matrix_integer_2x2.pyx", line 407:
    sage: m.__invert__unit() == m^-1
Exception raised:
    Traceback (most recent call last):
      File "/scratch/wstein/build/referee/sage-4.3.rc0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/wstein/build/referee/sage-4.3.rc0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/wstein/build/referee/sage-4.3.rc0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_19[8]>", line 1, in <module>
        m.__invert__unit() == m**-Integer(1)###line 407:
    sage: m.__invert__unit() == m^-1
    AttributeError: 'sage.matrix.matrix_integer_dense.Matrix_integer_de' object has no attribute '__invert__unit'
**********************************************************************
File "/scratch/wstein/build/referee/sage-4.3.rc0/devel/sage/sage/matrix/matrix_integer_2x2.pyx", line 409:
    sage: M([2,0,0,2]).__invert__unit()
Expected:
    Traceback (most recent call last):
    ...
    ZeroDivisionError: Not a unit!
Got:
    Traceback (most recent call last):
      File "/scratch/wstein/build/referee/sage-4.3.rc0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/wstein/build/referee/sage-4.3.rc0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/wstein/build/referee/sage-4.3.rc0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_19[9]>", line 1, in <module>
        M([Integer(2),Integer(0),Integer(0),Integer(2)]).__invert__unit()###line 409:
    sage: M([2,0,0,2]).__invert__unit()
    AttributeError: 'sage.matrix.matrix_integer_dense.Matrix_integer_de' object has no attribute '__invert__unit'
**********************************************************************
2 items had failures:
   1 of   5 in __main__.example_13
   4 of  10 in __main__.example_19
***Test Failed*** 5 failures.
For whitespace errors, see the file /scratch/wstein/sage//tmp/.doctest_matrix_integer_2x2.py
         [1.5 s]
exit code: 1024
 
----------------------------------------------------------------------
The following tests failed:


        sage -t  "devel/sage/sage/matrix/matrix_integer_2x2.pyx"
Total time for all tests: 1.5 seconds
```



I noticed a *massive* performance regression as a result of your patches:

```
OLD SAGE:
sage: s = random_matrix(RDF,100)
sage: time t =s*s
CPU times: user 0.01 s, sys: 0.00 s, total: 0.01 s
Wall time: 0.15 s


WITH YOUR PATCHES:
sage: s = random_matrix(RDF,100)
sage: time t =s*s
CPU times: user 0.91 s, sys: 0.00 s, total: 0.91 s
Wall time: 0.91 s
```


Ouch.  These are both dense matrices.  There must be something that got seriously messed up with re-factoring?

* Why is there a backslash here in `matrix_double_sparse.pyx`:

```
        either as a single list of length ``nrows\*ncols``, or as a 
```



---

Overall I'm very happy and excited about this patch!!  I'm really, really glad you're working on this, and would like to do anything I can to encourage this.  It is critically valuable to the Sage project to get much better numerical sparse matrix support.



---

archive/issue_comments_066343.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-12-21T11:00:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7723",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7723#issuecomment-66343",
    "user": "dagss"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_066344.json:
```json
{
    "body": "The attached patch should address the above issues (I guess this should have been folded into the original patches? But I hope this is OK, I still have some way to go before getting to terms with using Mercurial/MQ in a patch-review process.)",
    "created_at": "2009-12-21T11:00:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7723",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7723#issuecomment-66344",
    "user": "dagss"
}
```

The attached patch should address the above issues (I guess this should have been folded into the original patches? But I hope this is OK, I still have some way to go before getting to terms with using Mercurial/MQ in a patch-review process.)



---

archive/issue_comments_066345.json:
```json
{
    "body": "Attachment [trac_7723-fixround1.patch](tarball://root/attachments/some-uuid/ticket7723/trac_7723-fixround1.patch) by dagss created at 2009-12-21 11:19:11",
    "created_at": "2009-12-21T11:19:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7723",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7723#issuecomment-66345",
    "user": "dagss"
}
```

Attachment [trac_7723-fixround1.patch](tarball://root/attachments/some-uuid/ticket7723/trac_7723-fixround1.patch) by dagss created at 2009-12-21 11:19:11



---

archive/issue_comments_066346.json:
```json
{
    "body": "Replying to [comment:4 dagss]:\n> The attached patch should address the above issues (I guess this should have been folded into the original patches? But I hope this is OK, I still have some way to go before getting to terms with using Mercurial/MQ in a patch-review process.)\n\n\nI'm really glad you *didn't* fold this into the original patch, since it makes it much easier for me to see what you changed.",
    "created_at": "2009-12-21T18:21:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7723",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7723#issuecomment-66346",
    "user": "was"
}
```

Replying to [comment:4 dagss]:
> The attached patch should address the above issues (I guess this should have been folded into the original patches? But I hope this is OK, I still have some way to go before getting to terms with using Mercurial/MQ in a patch-review process.)


I'm really glad you *didn't* fold this into the original patch, since it makes it much easier for me to see what you changed.



---

archive/issue_comments_066347.json:
```json
{
    "body": "Looks great!",
    "created_at": "2009-12-21T18:28:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7723",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7723#issuecomment-66347",
    "user": "was"
}
```

Looks great!



---

archive/issue_comments_066348.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-12-21T18:28:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7723",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7723#issuecomment-66348",
    "user": "was"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_066349.json:
```json
{
    "body": "I get failures applying trac_7723-coo_format.patch",
    "created_at": "2010-01-04T02:10:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7723",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7723#issuecomment-66349",
    "user": "mhansen"
}
```

I get failures applying trac_7723-coo_format.patch



---

archive/issue_comments_066350.json:
```json
{
    "body": "I can't reproduce this, applying on 4.3.1.alpha0.\n\nDid you apply them in the wrong order? Apparently I messed up the order when uploading, sorry. The patches *must* be applied in this order:\n\n\n```\ntrac_7723-generic_multiply.patch\ntrac_7723-double_sparse.patch\ntrac_7723-coo_format.patch\ntrac_7723-fixround1.patch\n```\n",
    "created_at": "2010-01-04T21:42:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7723",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7723#issuecomment-66350",
    "user": "dagss"
}
```

I can't reproduce this, applying on 4.3.1.alpha0.

Did you apply them in the wrong order? Apparently I messed up the order when uploading, sorry. The patches *must* be applied in this order:


```
trac_7723-generic_multiply.patch
trac_7723-double_sparse.patch
trac_7723-coo_format.patch
trac_7723-fixround1.patch
```




---

archive/issue_comments_066351.json:
```json
{
    "body": "Ahh, thanks.  I was doing it in the wrong order.",
    "created_at": "2010-01-04T21:49:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7723",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7723#issuecomment-66351",
    "user": "mhansen"
}
```

Ahh, thanks.  I was doing it in the wrong order.



---

archive/issue_comments_066352.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-01-13T10:47:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7723",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7723#issuecomment-66352",
    "user": "rlm"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_066353.json:
```json
{
    "body": "\n```\nThe following tests failed:\n\n        sage -t -long devel/sage-main/sage/matrix/constructor.py # 1 doctests failed\n        sage -t -long devel/sage-main/sage/categories/action.pyx # Segfault\n```\n",
    "created_at": "2010-01-13T10:47:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7723",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7723#issuecomment-66353",
    "user": "rlm"
}
```


```
The following tests failed:

        sage -t -long devel/sage-main/sage/matrix/constructor.py # 1 doctests failed
        sage -t -long devel/sage-main/sage/categories/action.pyx # Segfault
```




---

archive/issue_comments_066354.json:
```json
{
    "body": "Ouch.\n\nI have not idea when I can get back to this at the moment. Basically what has happened is that I bit the bullet and implemented my own numerical matrix class hierarchy which is usable without Sage (but loosely modeled after it). That ended up giving me the results I needed much faster...\n\nThe long-term goal is to perhaps try to merge this back into Sage, however as there's no real benefit for my own work in doing that I don't really know if or when.\n\n(Anyone who finds this ticket because they need this functionality are welcome to send me an email and check the status.)",
    "created_at": "2010-02-04T08:01:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7723",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7723#issuecomment-66354",
    "user": "dagss"
}
```

Ouch.

I have not idea when I can get back to this at the moment. Basically what has happened is that I bit the bullet and implemented my own numerical matrix class hierarchy which is usable without Sage (but loosely modeled after it). That ended up giving me the results I needed much faster...

The long-term goal is to perhaps try to merge this back into Sage, however as there's no real benefit for my own work in doing that I don't really know if or when.

(Anyone who finds this ticket because they need this functionality are welcome to send me an email and check the status.)
