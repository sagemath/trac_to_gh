# Issue 6795: doctest failure in sage/sage/interfaces/expect.py due to upgrade to Maxima 5.19.1

Issue created by migration from https://trac.sagemath.org/ticket/6795

Original creator: drkirkby

Original creation time: 2009-08-21 07:22:07

Assignee: was

Keywords: maxima

On Solaris (SPARC), the following tests failed. Both ECL and Maxima were updated - ECL version 9.8.4 (see trac #6564); Maxima version 5.19.1 (see trac #6699). Updated spkgs can be found here. 

http://sage.math.washington.edu/home/kirkby/Solaris-fixes/ecl-9.8.4/

http://sage.math.washington.edu/home/kirkby/Solaris-fixes/maxima-5.19.1/


```

----------------------------------------------------------------------
----------------------------------------------------------------------
Thu Aug 20 20:02:37 BST 2009
dsage-trial tmp directory doesn't exist - creating ...
This script will run the unit tests for DSage
```

| Sage Version 4.1.1, Release Date: 2009-08-14                       |
| Type notebook() for the GUI, and license() for information.        |
<SNIP>

```
sage -t  "devel/sage/sage/interfaces/expect.py"
**********************************************************************
File "/export/home/drkirkby/sage/sage-4.1.1/devel/sage/sage/interfaces/expect.py", line 805:
    sage: print sage0.eval("alarm(1); singular._expect_expr('1')")
Exception raised:
    Traceback (most recent call last):
      File "/export/home/drkirkby/sage/sage-4.1.1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/export/home/drkirkby/sage/sage-4.1.1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/export/home/drkirkby/sage/sage-4.1.1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_15[9]>", line 1, in <module>
        print sage0.eval("alarm(1); singular._expect_expr('1')")###line 805:
    sage: print sage0.eval("alarm(1); singular._expect_expr('1')")
      File "/export/home/drkirkby/sage/sage-4.1.1/local/lib/python/site-packages/sage/interfaces/sage0.py", line 325, in eval
        return Expect.eval(self, line, **kwds).strip()
      File "/export/home/drkirkby/sage/sage-4.1.1/local/lib/python/site-packages/sage/interfaces/expect.py", line 980, in eval
        return '\n'.join([self._eval_line(L, **kwds) for L in code.split('\n') if L != ''])
      File "/export/home/drkirkby/sage/sage-4.1.1/local/lib/python/site-packages/sage/interfaces/expect.py", line 634, in _eval_line
        self._start()
      File "/export/home/drkirkby/sage/sage-4.1.1/local/lib/python/site-packages/sage/interfaces/expect.py", line 469, in _start
        raise RuntimeError, "Unable to start %s"%self.__name
    RuntimeError: Unable to start sage
**********************************************************************
1 items had failures:
   1 of  10 in __main__.example_15
***Test Failed*** 1 failures.
For whitespace errors, see the file /export/home/drkirkby/sage/sage-4.1.1/tmp/.doctest_expect.py
         [153.2 s]

```



---

Comment by burcin created at 2009-12-17 20:14:24

Resolution: worksforme


---

Comment by burcin created at 2009-12-17 20:14:24

I am closing this as `worksforme`. We've gone several releases with maxima-5.19.1, who knows what the problem that prevented Sage from starting as in the description was.
