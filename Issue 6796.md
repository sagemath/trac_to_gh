# Issue 6796: doctest failure in sage/sage/interfaces/psage.py due to upgrade to Maxima 5.19.1

Issue created by migration from https://trac.sagemath.org/ticket/6796

Original creator: drkirkby

Original creation time: 2009-08-21 07:29:44

Assignee: was

Keywords: maxima

On Solaris (SPARC), the following tests failed. Both ECL and Maxima were updated - ECL version 9.8.4 (see trac #6564); Maxima version 5.19.1 (see trac #6699). Updated spkgs can be found here. 

http://sage.math.washington.edu/home/kirkby/Solaris-fixes/ecl-9.8.4/ecl-9.8.4.spkg

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
sage -t  "devel/sage/sage/interfaces/psage.py"
**********************************************************************
File "/export/home/drkirkby/sage/sage-4.1.1/devel/sage/sage/interfaces/psage.py", line 23:
    sage: w = [x('factor(2^%s-1)'% randint(250,310)) for x in v]
Exception raised:
    Traceback (most recent call last):
      File "/export/home/drkirkby/sage/sage-4.1.1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/export/home/drkirkby/sage/sage-4.1.1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/export/home/drkirkby/sage/sage-4.1.1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[3]>", line 1, in <module>
        w = [x('factor(2^%s-1)'% randint(Integer(250),Integer(310))) for x in v]###line 23:
    sage: w = [x('factor(2^%s-1)'% randint(250,310)) for x in v]
      File "/export/home/drkirkby/sage/sage-4.1.1/local/lib/python/site-packages/sage/interfaces/sage0.py", line 263, in __call__
        return SageElement(self, x)
      File "/export/home/drkirkby/sage/sage-4.1.1/local/lib/python/site-packages/sage/interfaces/expect.py", line 1433, in __init__
        raise TypeError, x
    TypeError: Unable to start sage
**********************************************************************
File "/export/home/drkirkby/sage/sage-4.1.1/devel/sage/sage/interfaces/psage.py", line 26:
    sage: print "ignore this";  w       # random output (depends on timing)
Exception raised:
    Traceback (most recent call last):
      File "/export/home/drkirkby/sage/sage-4.1.1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/export/home/drkirkby/sage/sage-4.1.1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/export/home/drkirkby/sage/sage-4.1.1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[4]>", line 1, in <module>
        print "ignore this";  w       # random output (depends on timing)###line 26:
    sage: print "ignore this";  w       # random output (depends on timing)
    NameError: name 'w' is not defined
**********************************************************************
File "/export/home/drkirkby/sage/sage-4.1.1/devel/sage/sage/interfaces/psage.py", line 35:
    sage: print "ignore this";  w       # random output
Exception raised:
    Traceback (most recent call last):
      File "/export/home/drkirkby/sage/sage-4.1.1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/export/home/drkirkby/sage/sage-4.1.1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/export/home/drkirkby/sage/sage-4.1.1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[5]>", line 1, in <module>
        print "ignore this";  w       # random output###line 35:
    sage: print "ignore this";  w       # random output
    NameError: name 'w' is not defined
**********************************************************************
1 items had failures:
   3 of   6 in __main__.example_0
***Test Failed*** 3 failures.
For whitespace errors, see the file /export/home/drkirkby/sage/sage-4.1.1/tmp/.doctest_psage.py
         [87.0 s]
```



---

Comment by burcin created at 2009-12-17 20:15:10

Resolution: worksforme


---

Comment by burcin created at 2009-12-17 20:15:10

I am closing this as `worksforme`. We've gone several releases with maxima-5.19.1, who knows what the problem that prevented Sage from starting as in the description was.
