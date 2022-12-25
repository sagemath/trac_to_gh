# Issue 5081: Make numpy play nice with Sage types

archive/issues_005081.json:
```json
{
    "body": "Assignee: @williamstein\n\nWe should make numpy understand Sage float and complex types, at least the RDF and CDF types.  See the following thread on the numpy list.\n\nhttp://thread.gmane.org/gmane.comp.python.numeric.general/25251/focus=25273\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5081\n\n",
    "created_at": "2009-01-24T01:26:02Z",
    "labels": [
        "component: linear algebra"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.1",
    "title": "Make numpy play nice with Sage types",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5081",
    "user": "https://github.com/jasongrout"
}
```
Assignee: @williamstein

We should make numpy understand Sage float and complex types, at least the RDF and CDF types.  See the following thread on the numpy list.

http://thread.gmane.org/gmane.comp.python.numeric.general/25251/focus=25273


Issue created by migration from https://trac.sagemath.org/ticket/5081





---

archive/issue_comments_038645.json:
```json
{
    "body": "\n```\n[17:22] <cwitty> One problem is that Python has no particular C-level support for __complex__(); you actually have to use generic code to call that method.\n```\n",
    "created_at": "2009-01-24T01:27:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5081",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5081#issuecomment-38645",
    "user": "https://github.com/jasongrout"
}
```


```
[17:22] <cwitty> One problem is that Python has no particular C-level support for __complex__(); you actually have to use generic code to call that method.
```




---

archive/issue_comments_038646.json:
```json
{
    "body": "an example of failure:\n\n```\nfrom scipy import stats\nstats.uniform(0,15).ppf([0.5,0.7])\n```\n\nTraceback (most recent call last):\n  File \"<stdin>\", line 1, in <module>\n  File \"/home/Users/fcoelho/.sage/sage_notebook/worksheets/admin/0/code/19.py\", line 7, in <module>\n    stats.uniform(_sage_const_0 ,_sage_const_15 ).ppf([_sage_const_0p5 ,_sage_const_0p7 ])\n  File \"/usr/local/sage-3.4/local/lib/python2.5/site-packages/SQLAlchemy-0.4.6-py2.5.egg/\", line 1, in <module>\n    \n  File \"/usr/local/sage-3.4/local/lib/python2.5/site-packages/scipy/stats/distributions.py\", line 112, in ppf\n    return self.dist.ppf(q,*self.args,**self.kwds)\n  File \"/usr/local/sage-3.4/local/lib/python2.5/site-packages/scipy/stats/distributions.py\", line 563, in ppf\n    place(output,cond,self._ppf(*goodargs)*scale + loc)\n  File \"/usr/local/sage-3.4/local/lib/python2.5/site-packages/numpy/lib/function_base.py\", line 1357, in place\n    return _insert(arr, mask, vals)\nTypeError: array cannot be safely cast to required type",
    "created_at": "2009-04-22T14:07:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5081",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5081#issuecomment-38646",
    "user": "https://trac.sagemath.org/admin/accounts/users/fccoelho"
}
```

an example of failure:

```
from scipy import stats
stats.uniform(0,15).ppf([0.5,0.7])
```

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/Users/fcoelho/.sage/sage_notebook/worksheets/admin/0/code/19.py", line 7, in <module>
    stats.uniform(_sage_const_0 ,_sage_const_15 ).ppf([_sage_const_0p5 ,_sage_const_0p7 ])
  File "/usr/local/sage-3.4/local/lib/python2.5/site-packages/SQLAlchemy-0.4.6-py2.5.egg/", line 1, in <module>
    
  File "/usr/local/sage-3.4/local/lib/python2.5/site-packages/scipy/stats/distributions.py", line 112, in ppf
    return self.dist.ppf(q,*self.args,**self.kwds)
  File "/usr/local/sage-3.4/local/lib/python2.5/site-packages/scipy/stats/distributions.py", line 563, in ppf
    place(output,cond,self._ppf(*goodargs)*scale + loc)
  File "/usr/local/sage-3.4/local/lib/python2.5/site-packages/numpy/lib/function_base.py", line 1357, in place
    return _insert(arr, mask, vals)
TypeError: array cannot be safely cast to required type



---

archive/issue_comments_038647.json:
```json
{
    "body": "Solves the integer and real types. Complex types are still an issue which will need to be resolved by fixing NumPy.",
    "created_at": "2009-07-09T08:42:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5081",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5081#issuecomment-38647",
    "user": "https://github.com/robertwb"
}
```

Solves the integer and real types. Complex types are still an issue which will need to be resolved by fixing NumPy.



---

archive/issue_comments_038648.json:
```json
{
    "body": "Attachment [5081-numpy-types.patch](tarball://root/attachments/some-uuid/ticket5081/5081-numpy-types.patch) by @jasongrout created at 2009-07-09 09:24:24\n\nBrilliant!  I'm upgrading now so I can test this!",
    "created_at": "2009-07-09T09:24:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5081",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5081#issuecomment-38648",
    "user": "https://github.com/jasongrout"
}
```

Attachment [5081-numpy-types.patch](tarball://root/attachments/some-uuid/ticket5081/5081-numpy-types.patch) by @jasongrout created at 2009-07-09 09:24:24

Brilliant!  I'm upgrading now so I can test this!



---

archive/issue_comments_038649.json:
```json
{
    "body": "Is there a reason that you didn't use the same trick on ZZ that you used on RealField (with regards to not needing to specify whether dtype=object or not)?",
    "created_at": "2009-07-09T09:35:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5081",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5081#issuecomment-38649",
    "user": "https://github.com/jasongrout"
}
```

Is there a reason that you didn't use the same trick on ZZ that you used on RealField (with regards to not needing to specify whether dtype=object or not)?



---

archive/issue_comments_038650.json:
```json
{
    "body": "What does the '=' in the type descriptor mean?  I couldn't find that documented here: http://docs.scipy.org/doc/numpy/reference/arrays.interface.html",
    "created_at": "2009-07-09T09:48:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5081",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5081#issuecomment-38650",
    "user": "https://github.com/jasongrout"
}
```

What does the '=' in the type descriptor mean?  I couldn't find that documented here: http://docs.scipy.org/doc/numpy/reference/arrays.interface.html



---

archive/issue_comments_038651.json:
```json
{
    "body": "Ah, I found the answer to my last question here: http://docs.scipy.org/doc/numpy/reference/arrays.dtypes.html#specifying-and-constructing-data-types\n\n'=' means hardware-default endian behavior.",
    "created_at": "2009-07-09T09:56:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5081",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5081#issuecomment-38651",
    "user": "https://github.com/jasongrout"
}
```

Ah, I found the answer to my last question here: http://docs.scipy.org/doc/numpy/reference/arrays.dtypes.html#specifying-and-constructing-data-types

'=' means hardware-default endian behavior.



---

archive/issue_comments_038652.json:
```json
{
    "body": "Things seem to work fine if I put the logic that the patch has in real_mpfr.pyx also in integer.pyx.  Is there a reason the logic wasn't included dealing with switching from hardware types to object types?",
    "created_at": "2009-07-09T10:20:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5081",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5081#issuecomment-38652",
    "user": "https://github.com/jasongrout"
}
```

Things seem to work fine if I put the logic that the patch has in real_mpfr.pyx also in integer.pyx.  Is there a reason the logic wasn't included dealing with switching from hardware types to object types?



---

archive/issue_comments_038653.json:
```json
{
    "body": "http://bugs.python.org/issue1675423 may resolve the complex case. \n\nAs for not using the precision trick for ZZ, I was thinking that a single ring should map to a single dtype. A sticky issue is that once you switch from ints to objects, you have different overflow semantics. \n\nI guess numpy folks are already used to this \n\n\n```\n>>> import numpy \n>>> numpy.array(2**20)\narray(1048576)\n>>> numpy.array(2**20)**2\n0\n>>> numpy.array(2**40)   \narray(1099511627776L, dtype=int64)\n>>> numpy.array(2**40)**2\n0\n>>> numpy.array(2**80)\narray(1208925819614629174706176L, dtype=object)\n>>> numpy.array(2**80)**2\n1461501637330902918203684832716283019655932542976L\n```\n\n\nWe should maybe have three cases--long (sys.maxint), int64, and object. Of course, the former would only be for 32-bit machines. \n\n- Robert",
    "created_at": "2009-07-09T10:41:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5081",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5081#issuecomment-38653",
    "user": "https://github.com/robertwb"
}
```

http://bugs.python.org/issue1675423 may resolve the complex case. 

As for not using the precision trick for ZZ, I was thinking that a single ring should map to a single dtype. A sticky issue is that once you switch from ints to objects, you have different overflow semantics. 

I guess numpy folks are already used to this 


```
>>> import numpy 
>>> numpy.array(2**20)
array(1048576)
>>> numpy.array(2**20)**2
0
>>> numpy.array(2**40)   
array(1099511627776L, dtype=int64)
>>> numpy.array(2**40)**2
0
>>> numpy.array(2**80)
array(1208925819614629174706176L, dtype=object)
>>> numpy.array(2**80)**2
1461501637330902918203684832716283019655932542976L
```


We should maybe have three cases--long (sys.maxint), int64, and object. Of course, the former would only be for 32-bit machines. 

- Robert



---

archive/issue_comments_038654.json:
```json
{
    "body": "This looks good, is well documented, and is a long time coming.  I'm giving it a positive review.\n\nRegarding:\n\n> We should maybe have three cases--long (sys.maxint), int64, and object. Of course, the former would only be for 32-bit machines.\n\nYes, that would be good.  But I don't consider it a show stopper for this patch.  It could easily be added on another ticket later.",
    "created_at": "2009-07-09T19:17:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5081",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5081#issuecomment-38654",
    "user": "https://github.com/williamstein"
}
```

This looks good, is well documented, and is a long time coming.  I'm giving it a positive review.

Regarding:

> We should maybe have three cases--long (sys.maxint), int64, and object. Of course, the former would only be for 32-bit machines.

Yes, that would be good.  But I don't consider it a show stopper for this patch.  It could easily be added on another ticket later.



---

archive/issue_comments_038655.json:
```json
{
    "body": "I'm getting the following test failures:\n\n```\nsage -t -long devel/sage-exp/sage/matrix/matrix1.pyx\n**********************************************************************\nFile \"/scratch/mvngu/release/sage-4.1.1/devel/sage-exp/sage/matrix/matrix1.pyx\", line 428:\n    sage: a.numpy()\nExpected:\n    array([[0, 1, 2, 3],\n           [4, 5, 6, 7],\n           [8, 9, 10, 11]], dtype=object)\nGot:\n    array([[ 0,  1,  2,  3],\n           [ 4,  5,  6,  7],\n           [ 8,  9, 10, 11]])\n**********************************************************************\n1 items had failures:\n   1 of   9 in __main__.example_13\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file /scratch/mvngu/release/sage-4.1.1/tmp/.doctest_matrix1.py\n\t [3.5 s]\n\n<SNIP>\n\nsage -t -long devel/sage-exp/sage/rings/number_field/totallyreal_rel.py\n**********************************************************************\nFile \"/scratch/mvngu/release/sage-4.1.1/devel/sage-exp/sage/rings/number_field/totallyreal_rel.py\", line 156:\n    sage: T = sage.rings.number_field.totallyreal_rel.tr_data_rel(F, 2, 2000)\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/mvngu/release/sage-4.1.1/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/scratch/mvngu/release/sage-4.1.1/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/scratch/mvngu/release/sage-4.1.1/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_3[3]>\", line 1, in <module>\n        T = sage.rings.number_field.totallyreal_rel.tr_data_rel(F, Integer(2), Integer(2000))###line 156:\n    sage: T = sage.rings.number_field.totallyreal_rel.tr_data_rel(F, 2, 2000)\n      File \"/scratch/mvngu/release/sage-4.1.1/local/lib/python/site-packages/sage/rings/number_field/totallyreal_rel.py\", line 200, in __init__\n        adj = pari(Q).qflll()[self.d]\n      File \"gen.pyx\", line 9174, in sage.libs.pari.gen._pari_trap (sage/libs/pari/gen.c:44241)\n    PariError: unexpected character (2)\n**********************************************************************\nFile \"/scratch/mvngu/release/sage-4.1.1/devel/sage-exp/sage/rings/number_field/totallyreal_rel.py\", line 569:\n    sage: enumerate_totallyreal_fields_rel(F, 2, 2000)\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/mvngu/release/sage-4.1.1/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/scratch/mvngu/release/sage-4.1.1/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/scratch/mvngu/release/sage-4.1.1/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_5[4]>\", line 1, in <module>\n        enumerate_totallyreal_fields_rel(F, Integer(2), Integer(2000))###line 569:\n    sage: enumerate_totallyreal_fields_rel(F, 2, 2000)\n      File \"/scratch/mvngu/release/sage-4.1.1/local/lib/python/site-packages/sage/rings/number_field/totallyreal_rel.py\", line 647, in enumerate_totallyreal_fields_rel\n        T = tr_data_rel(F,m,B,a)\n      File \"/scratch/mvngu/release/sage-4.1.1/local/lib/python/site-packages/sage/rings/number_field/totallyreal_rel.py\", line 200, in __init__\n        adj = pari(Q).qflll()[self.d]\n      File \"gen.pyx\", line 9174, in sage.libs.pari.gen._pari_trap (sage/libs/pari/gen.c:44241)\n    PariError: unexpected character (2)\n**********************************************************************\nFile \"/scratch/mvngu/release/sage-4.1.1/devel/sage-exp/sage/rings/number_field/totallyreal_rel.py\", line 578:\n    sage: ls = enumerate_totallyreal_fields_rel(F, 2, 10^4)\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/mvngu/release/sage-4.1.1/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/scratch/mvngu/release/sage-4.1.1/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/scratch/mvngu/release/sage-4.1.1/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_5[6]>\", line 1, in <module>\n        ls = enumerate_totallyreal_fields_rel(F, Integer(2), Integer(10)**Integer(4))###line 578:\n    sage: ls = enumerate_totallyreal_fields_rel(F, 2, 10^4)\n      File \"/scratch/mvngu/release/sage-4.1.1/local/lib/python/site-packages/sage/rings/number_field/totallyreal_rel.py\", line 647, in enumerate_totallyreal_fields_rel\n        T = tr_data_rel(F,m,B,a)\n      File \"/scratch/mvngu/release/sage-4.1.1/local/lib/python/site-packages/sage/rings/number_field/totallyreal_rel.py\", line 200, in __init__\n        adj = pari(Q).qflll()[self.d]\n      File \"gen.pyx\", line 9174, in sage.libs.pari.gen._pari_trap (sage/libs/pari/gen.c:44241)\n    PariError: unexpected character (2)\n**********************************************************************\nFile \"/scratch/mvngu/release/sage-4.1.1/devel/sage-exp/sage/rings/number_field/totallyreal_rel.py\", line 579:\n    sage: print \"ignore this\";  ls # random (the second factor is platform-dependent)\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/mvngu/release/sage-4.1.1/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/scratch/mvngu/release/sage-4.1.1/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/scratch/mvngu/release/sage-4.1.1/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_5[7]>\", line 1, in <module>\n        print \"ignore this\";  ls # random (the second factor is platform-dependent)###line 579:\n    sage: print \"ignore this\";  ls # random (the second factor is platform-dependent)\n    NameError: name 'ls' is not defined\n**********************************************************************\nFile \"/scratch/mvngu/release/sage-4.1.1/devel/sage-exp/sage/rings/number_field/totallyreal_rel.py\", line 601:\n    sage: [ f[0] for f in ls ]\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/mvngu/release/sage-4.1.1/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/scratch/mvngu/release/sage-4.1.1/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/scratch/mvngu/release/sage-4.1.1/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_5[8]>\", line 1, in <module>\n        [ f[Integer(0)] for f in ls ]###line 601:\n    sage: [ f[0] for f in ls ]\n    NameError: name 'ls' is not defined\n**********************************************************************\nFile \"/scratch/mvngu/release/sage-4.1.1/devel/sage-exp/sage/rings/number_field/totallyreal_rel.py\", line 604:\n    sage: [NumberField(ZZx(x[1]), 't').is_galois() for x in ls]\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/mvngu/release/sage-4.1.1/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/scratch/mvngu/release/sage-4.1.1/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/scratch/mvngu/release/sage-4.1.1/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_5[9]>\", line 1, in <module>\n        [NumberField(ZZx(x[Integer(1)]), 't').is_galois() for x in ls]###line 604:\n    sage: [NumberField(ZZx(x[1]), 't').is_galois() for x in ls]\n    NameError: name 'ls' is not defined\n**********************************************************************\n2 items had failures:\n   1 of   4 in __main__.example_3\n   5 of  12 in __main__.example_5\n***Test Failed*** 6 failures.\nFor whitespace errors, see the file /scratch/mvngu/release/sage-4.1.1/tmp/.doctest_totallyreal_rel.py\n\t [2.2 s]\n\n<SNIP>\n\nsage -t -long devel/sage-exp/doc/en/numerical_sage/numpy.rst\n**********************************************************************\nFile \"/scratch/mvngu/release/sage-4.1.1/devel/sage-exp/doc/en/numerical_sage/numpy.rst\", line 19:\n    sage: l\nExpected:\n    array([1, 2, 3], dtype=object)\nGot:\n    array([1, 2, 3])\n**********************************************************************\nFile \"/scratch/mvngu/release/sage-4.1.1/devel/sage-exp/doc/en/numerical_sage/numpy.rst\", line 54:\n    sage: l\nExpected:\n    array([1.00000000000000, 2.00000000000000, 3.00000000000000], dtype=object)\nGot:\n    array([ 1.,  2.,  3.])\n**********************************************************************\n1 items had failures:\n   2 of  52 in __main__.example_0\n***Test Failed*** 2 failures.\nFor whitespace errors, see the file /scratch/mvngu/release/sage-4.1.1/tmp/.doctest_numpy.py\n\t [1.8 s]\n\n<SNIP>\n\n----------------------------------------------------------------------\n\nThe following tests failed:\n\n\tsage -t -long devel/sage-exp/sage/matrix/matrix1.pyx # 1 doctests failed\n\tsage -t -long devel/sage-exp/sage/rings/number_field/totallyreal_rel.py # 6 doctests failed\n\tsage -t -long devel/sage-exp/doc/en/numerical_sage/numpy.rst # 2 doctests failed\n----------------------------------------------------------------------\nTotal time for all tests: 525.6 seconds\n```\n",
    "created_at": "2009-07-16T14:26:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5081",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5081#issuecomment-38655",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

I'm getting the following test failures:

```
sage -t -long devel/sage-exp/sage/matrix/matrix1.pyx
**********************************************************************
File "/scratch/mvngu/release/sage-4.1.1/devel/sage-exp/sage/matrix/matrix1.pyx", line 428:
    sage: a.numpy()
Expected:
    array([[0, 1, 2, 3],
           [4, 5, 6, 7],
           [8, 9, 10, 11]], dtype=object)
Got:
    array([[ 0,  1,  2,  3],
           [ 4,  5,  6,  7],
           [ 8,  9, 10, 11]])
**********************************************************************
1 items had failures:
   1 of   9 in __main__.example_13
***Test Failed*** 1 failures.
For whitespace errors, see the file /scratch/mvngu/release/sage-4.1.1/tmp/.doctest_matrix1.py
	 [3.5 s]

<SNIP>

sage -t -long devel/sage-exp/sage/rings/number_field/totallyreal_rel.py
**********************************************************************
File "/scratch/mvngu/release/sage-4.1.1/devel/sage-exp/sage/rings/number_field/totallyreal_rel.py", line 156:
    sage: T = sage.rings.number_field.totallyreal_rel.tr_data_rel(F, 2, 2000)
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mvngu/release/sage-4.1.1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mvngu/release/sage-4.1.1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mvngu/release/sage-4.1.1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_3[3]>", line 1, in <module>
        T = sage.rings.number_field.totallyreal_rel.tr_data_rel(F, Integer(2), Integer(2000))###line 156:
    sage: T = sage.rings.number_field.totallyreal_rel.tr_data_rel(F, 2, 2000)
      File "/scratch/mvngu/release/sage-4.1.1/local/lib/python/site-packages/sage/rings/number_field/totallyreal_rel.py", line 200, in __init__
        adj = pari(Q).qflll()[self.d]
      File "gen.pyx", line 9174, in sage.libs.pari.gen._pari_trap (sage/libs/pari/gen.c:44241)
    PariError: unexpected character (2)
**********************************************************************
File "/scratch/mvngu/release/sage-4.1.1/devel/sage-exp/sage/rings/number_field/totallyreal_rel.py", line 569:
    sage: enumerate_totallyreal_fields_rel(F, 2, 2000)
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mvngu/release/sage-4.1.1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mvngu/release/sage-4.1.1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mvngu/release/sage-4.1.1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_5[4]>", line 1, in <module>
        enumerate_totallyreal_fields_rel(F, Integer(2), Integer(2000))###line 569:
    sage: enumerate_totallyreal_fields_rel(F, 2, 2000)
      File "/scratch/mvngu/release/sage-4.1.1/local/lib/python/site-packages/sage/rings/number_field/totallyreal_rel.py", line 647, in enumerate_totallyreal_fields_rel
        T = tr_data_rel(F,m,B,a)
      File "/scratch/mvngu/release/sage-4.1.1/local/lib/python/site-packages/sage/rings/number_field/totallyreal_rel.py", line 200, in __init__
        adj = pari(Q).qflll()[self.d]
      File "gen.pyx", line 9174, in sage.libs.pari.gen._pari_trap (sage/libs/pari/gen.c:44241)
    PariError: unexpected character (2)
**********************************************************************
File "/scratch/mvngu/release/sage-4.1.1/devel/sage-exp/sage/rings/number_field/totallyreal_rel.py", line 578:
    sage: ls = enumerate_totallyreal_fields_rel(F, 2, 10^4)
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mvngu/release/sage-4.1.1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mvngu/release/sage-4.1.1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mvngu/release/sage-4.1.1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_5[6]>", line 1, in <module>
        ls = enumerate_totallyreal_fields_rel(F, Integer(2), Integer(10)**Integer(4))###line 578:
    sage: ls = enumerate_totallyreal_fields_rel(F, 2, 10^4)
      File "/scratch/mvngu/release/sage-4.1.1/local/lib/python/site-packages/sage/rings/number_field/totallyreal_rel.py", line 647, in enumerate_totallyreal_fields_rel
        T = tr_data_rel(F,m,B,a)
      File "/scratch/mvngu/release/sage-4.1.1/local/lib/python/site-packages/sage/rings/number_field/totallyreal_rel.py", line 200, in __init__
        adj = pari(Q).qflll()[self.d]
      File "gen.pyx", line 9174, in sage.libs.pari.gen._pari_trap (sage/libs/pari/gen.c:44241)
    PariError: unexpected character (2)
**********************************************************************
File "/scratch/mvngu/release/sage-4.1.1/devel/sage-exp/sage/rings/number_field/totallyreal_rel.py", line 579:
    sage: print "ignore this";  ls # random (the second factor is platform-dependent)
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mvngu/release/sage-4.1.1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mvngu/release/sage-4.1.1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mvngu/release/sage-4.1.1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_5[7]>", line 1, in <module>
        print "ignore this";  ls # random (the second factor is platform-dependent)###line 579:
    sage: print "ignore this";  ls # random (the second factor is platform-dependent)
    NameError: name 'ls' is not defined
**********************************************************************
File "/scratch/mvngu/release/sage-4.1.1/devel/sage-exp/sage/rings/number_field/totallyreal_rel.py", line 601:
    sage: [ f[0] for f in ls ]
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mvngu/release/sage-4.1.1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mvngu/release/sage-4.1.1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mvngu/release/sage-4.1.1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_5[8]>", line 1, in <module>
        [ f[Integer(0)] for f in ls ]###line 601:
    sage: [ f[0] for f in ls ]
    NameError: name 'ls' is not defined
**********************************************************************
File "/scratch/mvngu/release/sage-4.1.1/devel/sage-exp/sage/rings/number_field/totallyreal_rel.py", line 604:
    sage: [NumberField(ZZx(x[1]), 't').is_galois() for x in ls]
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mvngu/release/sage-4.1.1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mvngu/release/sage-4.1.1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mvngu/release/sage-4.1.1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_5[9]>", line 1, in <module>
        [NumberField(ZZx(x[Integer(1)]), 't').is_galois() for x in ls]###line 604:
    sage: [NumberField(ZZx(x[1]), 't').is_galois() for x in ls]
    NameError: name 'ls' is not defined
**********************************************************************
2 items had failures:
   1 of   4 in __main__.example_3
   5 of  12 in __main__.example_5
***Test Failed*** 6 failures.
For whitespace errors, see the file /scratch/mvngu/release/sage-4.1.1/tmp/.doctest_totallyreal_rel.py
	 [2.2 s]

<SNIP>

sage -t -long devel/sage-exp/doc/en/numerical_sage/numpy.rst
**********************************************************************
File "/scratch/mvngu/release/sage-4.1.1/devel/sage-exp/doc/en/numerical_sage/numpy.rst", line 19:
    sage: l
Expected:
    array([1, 2, 3], dtype=object)
Got:
    array([1, 2, 3])
**********************************************************************
File "/scratch/mvngu/release/sage-4.1.1/devel/sage-exp/doc/en/numerical_sage/numpy.rst", line 54:
    sage: l
Expected:
    array([1.00000000000000, 2.00000000000000, 3.00000000000000], dtype=object)
Got:
    array([ 1.,  2.,  3.])
**********************************************************************
1 items had failures:
   2 of  52 in __main__.example_0
***Test Failed*** 2 failures.
For whitespace errors, see the file /scratch/mvngu/release/sage-4.1.1/tmp/.doctest_numpy.py
	 [1.8 s]

<SNIP>

----------------------------------------------------------------------

The following tests failed:

	sage -t -long devel/sage-exp/sage/matrix/matrix1.pyx # 1 doctests failed
	sage -t -long devel/sage-exp/sage/rings/number_field/totallyreal_rel.py # 6 doctests failed
	sage -t -long devel/sage-exp/doc/en/numerical_sage/numpy.rst # 2 doctests failed
----------------------------------------------------------------------
Total time for all tests: 525.6 seconds
```




---

archive/issue_comments_038656.json:
```json
{
    "body": "This ticket is related to #6497.",
    "created_at": "2009-07-17T08:53:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5081",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5081#issuecomment-38656",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

This ticket is related to #6497.



---

archive/issue_comments_038657.json:
```json
{
    "body": "See #6506 for a patch which fixes most of these issues and discusses another.",
    "created_at": "2009-07-19T03:55:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5081",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5081#issuecomment-38657",
    "user": "https://github.com/jasongrout"
}
```

See #6506 for a patch which fixes most of these issues and discusses another.



---

archive/issue_comments_038658.json:
```json
{
    "body": "All issues fixed in #6506, review of this patch should happen with review of the other.",
    "created_at": "2009-07-27T14:13:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5081",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5081#issuecomment-38658",
    "user": "https://github.com/robertwb"
}
```

All issues fixed in #6506, review of this patch should happen with review of the other.



---

archive/issue_comments_038659.json:
```json
{
    "body": "Positive review, since #6506 is positive review and fixes all issues listed here.\n\nmvngu: are you a reviewer as well?",
    "created_at": "2009-07-27T16:29:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5081",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5081#issuecomment-38659",
    "user": "https://github.com/jasongrout"
}
```

Positive review, since #6506 is positive review and fixes all issues listed here.

mvngu: are you a reviewer as well?



---

archive/issue_comments_038660.json:
```json
{
    "body": "Replying to [comment:15 jason]:\n> mvngu: are you a reviewer as well?\nNo, not really. I often like to apply patches and doctest them to see them break. Seeing doctests break is more fun than seeing all tests passed :-)",
    "created_at": "2009-07-28T03:12:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5081",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5081#issuecomment-38660",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Replying to [comment:15 jason]:
> mvngu: are you a reviewer as well?
No, not really. I often like to apply patches and doctest them to see them break. Seeing doctests break is more fun than seeing all tests passed :-)



---

archive/issue_comments_038661.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-07-29T13:45:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5081",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5081#issuecomment-38661",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_events_005327.json:
```json
{
    "actor": "mvngu",
    "created_at": "2009-07-29T13:45:52Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5081",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5081#event-5327"
}
```
