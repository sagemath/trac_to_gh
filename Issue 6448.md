# Issue 6448: darwin_utilities import issues

Issue created by migration from Trac.

Original creator: rlm

Original creation time: 2009-06-29 20:54:15

Assignee: tbd

CC:  rlm

The following is on sage.math:


```
sage -t  "devel/sage-main/sage/misc/darwin_utilities.pyx"
**********************************************************************
File "/space/rlm/sage-4.1.alpha2/devel/sage-main/sage/misc/darwin_utilities.pyx", line 12:
    sage: from sage.misc.darwin_utilities import darwin_memory_usage
Exception raised:
    Traceback (most recent call last):
      File "/space/rlm/sage-4.1.alpha2/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/space/rlm/sage-4.1.alpha2/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/space/rlm/sage-4.1.alpha2/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[2]>", line 1, in <module>
        from sage.misc.darwin_utilities import darwin_memory_usage###line 12:
    sage: from sage.misc.darwin_utilities import darwin_memory_usage
    ImportError: No module named darwin_utilities
**********************************************************************
File "/space/rlm/sage-4.1.alpha2/devel/sage-main/sage/misc/darwin_utilities.pyx", line 17:
    sage: from sage.misc.darwin_utilities import darwin_memory_usage
Exception raised:
    Traceback (most recent call last):
      File "/space/rlm/sage-4.1.alpha2/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/space/rlm/sage-4.1.alpha2/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/space/rlm/sage-4.1.alpha2/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[4]>", line 1, in <module>
        from sage.misc.darwin_utilities import darwin_memory_usage###line 17:
    sage: from sage.misc.darwin_utilities import darwin_memory_usage
    ImportError: No module named darwin_utilities
**********************************************************************
File "/space/rlm/sage-4.1.alpha2/devel/sage-main/sage/misc/darwin_utilities.pyx", line 18:
    sage: try:
        if os.uname()[Integer(0)] != 'Darwin':
            memory_usage = darwin_memory_usage()
        else:
            raise NotImplementedError
    except NotImplementedError:
        print "NotImplementedError"
Exception raised:
    Traceback (most recent call last):
      File "/space/rlm/sage-4.1.alpha2/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/space/rlm/sage-4.1.alpha2/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/space/rlm/sage-4.1.alpha2/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[5]>", line 3, in <module>
        memory_usage = darwin_memory_usage()
    NameError: name 'darwin_memory_usage' is not defined
**********************************************************************
```



---

Attachment

I developed and tested this patch on OS X 10.4, and it worked (I had seen before a slightly different doctest failure than noted in the description, but nevertheless).
From this, and the nature of the changes in the patch, I deduce it should work on any platform except possibly OS X 10.5.
I can't test on the latter one, though.


---

Comment by rlm created at 2009-07-03 01:02:14

Resolution: fixed
