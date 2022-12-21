# Issue 5081: Make numpy play nice with Sage types

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2009-01-24 01:26:02

Assignee: was

We should make numpy understand Sage float and complex types, at least the RDF and CDF types.  See the following thread on the numpy list.

http://thread.gmane.org/gmane.comp.python.numeric.general/25251/focus=25273



---

Comment by jason created at 2009-01-24 01:27:53


```
[17:22] <cwitty> One problem is that Python has no particular C-level support for __complex__(); you actually have to use generic code to call that method.
```



---

Comment by fccoelho created at 2009-04-22 14:07:46

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

Comment by robertwb created at 2009-07-09 08:42:07

Solves the integer and real types. Complex types are still an issue which will need to be resolved by fixing NumPy.


---

Attachment

Brilliant!  I'm upgrading now so I can test this!


---

Comment by jason created at 2009-07-09 09:35:53

Is there a reason that you didn't use the same trick on ZZ that you used on RealField (with regards to not needing to specify whether dtype=object or not)?


---

Comment by jason created at 2009-07-09 09:48:40

What does the '=' in the type descriptor mean?  I couldn't find that documented here: http://docs.scipy.org/doc/numpy/reference/arrays.interface.html


---

Comment by jason created at 2009-07-09 09:56:21

Ah, I found the answer to my last question here: http://docs.scipy.org/doc/numpy/reference/arrays.dtypes.html#specifying-and-constructing-data-types

'=' means hardware-default endian behavior.


---

Comment by jason created at 2009-07-09 10:20:39

Things seem to work fine if I put the logic that the patch has in real_mpfr.pyx also in integer.pyx.  Is there a reason the logic wasn't included dealing with switching from hardware types to object types?


---

Comment by robertwb created at 2009-07-09 10:41:32

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

Comment by was created at 2009-07-09 19:17:47

This looks good, is well documented, and is a long time coming.  I'm giving it a positive review.

Regarding:

> We should maybe have three cases--long (sys.maxint), int64, and object. Of course, the former would only be for 32-bit machines.

Yes, that would be good.  But I don't consider it a show stopper for this patch.  It could easily be added on another ticket later.


---

Comment by mvngu created at 2009-07-16 14:26:43

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

Comment by mvngu created at 2009-07-17 08:53:13

This ticket is related to #6497.


---

Comment by jason created at 2009-07-19 03:55:27

See #6506 for a patch which fixes most of these issues and discusses another.


---

Comment by robertwb created at 2009-07-27 14:13:43

All issues fixed in #6506, review of this patch should happen with review of the other.


---

Comment by jason created at 2009-07-27 16:29:24

Positive review, since #6506 is positive review and fixes all issues listed here.

mvngu: are you a reviewer as well?


---

Comment by mvngu created at 2009-07-28 03:12:12

Replying to [comment:15 jason]:
> mvngu: are you a reviewer as well?
No, not really. I often like to apply patches and doctest them to see them break. Seeing doctests break is more fun than seeing all tests passed :-)


---

Comment by mvngu created at 2009-07-29 13:45:52

Resolution: fixed
