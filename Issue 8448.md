# Issue 8448: doc/common/builder.py doctests write files in Sage tree

Issue created by migration from https://trac.sagemath.org/ticket/8448

Original creator: rhinton

Original creation time: 2010-03-05 17:13:21

Assignee: mvngu

CC:  dimpase

Keywords: builder.py, doctest, system-wide

I am using a system-wide install, so I don't have write access in the Sage tree.  When I run `sage -testall`, I get the following errors.  (More may come; it's only been running a few minutes. :-)


```
sage -t  "devel/sage/doc/common/builder.py"                 
**********************************************************************
File "/share/apps/contrib/sage-4.3.3/devel/sage/doc/common/builder.py", line 157:
    sage: b = builder.DocBuilder('tutorial')
Exception raised:
    Traceback (most recent call last):
      File "/share/apps/contrib/sage-4.3.3/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/share/apps/contrib/sage-4.3.3/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/share/apps/contrib/sage-4.3.3/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_4[3]>", line 1, in <module>
        b = builder.DocBuilder('tutorial')###line 157:
    sage: b = builder.DocBuilder('tutorial')
      File "/share/apps/contrib/sage-4.3.3/devel/sage/doc/common/builder.py", line 145, in __init__
        mkdir(os.path.join(self.dir, "static"))
      File "/share/apps/contrib/sage-4.3.3/devel/sage/doc/common/builder.py", line 55, in mkdir
        os.makedirs(path)
      File "/share/apps/contrib/sage-4.3.3/local/lib/python2.6/os.py", line 157, in makedirs
        mkdir(name, mode)
    OSError: [Errno 13] Permission denied: '/share/apps/contrib/sage-4.3.3/devel/sage/doc/en/tutorial/static'
**********************************************************************
File "/share/apps/contrib/sage-4.3.3/devel/sage/doc/common/builder.py", line 158:
    sage: b._output_dir('html')
Exception raised:
    Traceback (most recent call last):
      File "/share/apps/contrib/sage-4.3.3/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/share/apps/contrib/sage-4.3.3/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/share/apps/contrib/sage-4.3.3/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_4[4]>", line 1, in <module>
        b._output_dir('html')###line 158:
    sage: b._output_dir('html')
    NameError: name 'b' is not defined
**********************************************************************
File "/share/apps/contrib/sage-4.3.3/devel/sage/doc/common/builder.py", line 172:
    sage: b = builder.DocBuilder('tutorial')
Exception raised:
    Traceback (most recent call last):
      File "/share/apps/contrib/sage-4.3.3/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/share/apps/contrib/sage-4.3.3/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/share/apps/contrib/sage-4.3.3/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_5[3]>", line 1, in <module>
        b = builder.DocBuilder('tutorial')###line 172:
    sage: b = builder.DocBuilder('tutorial')
      File "/share/apps/contrib/sage-4.3.3/devel/sage/doc/common/builder.py", line 145, in __init__
        mkdir(os.path.join(self.dir, "static"))
      File "/share/apps/contrib/sage-4.3.3/devel/sage/doc/common/builder.py", line 55, in mkdir
        os.makedirs(path)
      File "/share/apps/contrib/sage-4.3.3/local/lib/python2.6/os.py", line 157, in makedirs
        mkdir(name, mode)
    OSError: [Errno 13] Permission denied: '/share/apps/contrib/sage-4.3.3/devel/sage/doc/en/tutorial/static'
**********************************************************************
File "/share/apps/contrib/sage-4.3.3/devel/sage/doc/common/builder.py", line 173:
    sage: b._doctrees_dir()
Exception raised:
    Traceback (most recent call last):
      File "/share/apps/contrib/sage-4.3.3/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/share/apps/contrib/sage-4.3.3/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/share/apps/contrib/sage-4.3.3/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_5[4]>", line 1, in <module>
        b._doctrees_dir()###line 173:
    sage: b._doctrees_dir()
    NameError: name 'b' is not defined
**********************************************************************
File "/share/apps/contrib/sage-4.3.3/devel/sage/doc/common/builder.py", line 185:
    sage: b = builder.DocBuilder('tutorial')
Exception raised:
    Traceback (most recent call last):
      File "/share/apps/contrib/sage-4.3.3/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/share/apps/contrib/sage-4.3.3/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/share/apps/contrib/sage-4.3.3/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_6[3]>", line 1, in <module>
        b = builder.DocBuilder('tutorial')###line 185:
    sage: b = builder.DocBuilder('tutorial')
      File "/share/apps/contrib/sage-4.3.3/devel/sage/doc/common/builder.py", line 145, in __init__
        mkdir(os.path.join(self.dir, "static"))
      File "/share/apps/contrib/sage-4.3.3/devel/sage/doc/common/builder.py", line 55, in mkdir
        os.makedirs(path)
      File "/share/apps/contrib/sage-4.3.3/local/lib/python2.6/os.py", line 157, in makedirs
        mkdir(name, mode)
    OSError: [Errno 13] Permission denied: '/share/apps/contrib/sage-4.3.3/devel/sage/doc/en/tutorial/static'
**********************************************************************
File "/share/apps/contrib/sage-4.3.3/devel/sage/doc/common/builder.py", line 186:
    sage: b._output_formats()
Exception raised:
    Traceback (most recent call last):
      File "/share/apps/contrib/sage-4.3.3/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/share/apps/contrib/sage-4.3.3/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/share/apps/contrib/sage-4.3.3/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_6[4]>", line 1, in <module>
        b._output_formats()###line 186:
    sage: b._output_formats()
    NameError: name 'b' is not defined
**********************************************************************
File "/share/apps/contrib/sage-4.3.3/devel/sage/doc/common/builder.py", line 209:
    sage: b = builder.DocBuilder('tutorial')
Exception raised:
    Traceback (most recent call last):
      File "/share/apps/contrib/sage-4.3.3/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/share/apps/contrib/sage-4.3.3/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/share/apps/contrib/sage-4.3.3/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_7[3]>", line 1, in <module>
        b = builder.DocBuilder('tutorial')###line 209:
    sage: b = builder.DocBuilder('tutorial')
      File "/share/apps/contrib/sage-4.3.3/devel/sage/doc/common/builder.py", line 145, in __init__
        mkdir(os.path.join(self.dir, "static"))
      File "/share/apps/contrib/sage-4.3.3/devel/sage/doc/common/builder.py", line 55, in mkdir
        os.makedirs(path)
      File "/share/apps/contrib/sage-4.3.3/local/lib/python2.6/os.py", line 157, in makedirs
        mkdir(name, mode)
    OSError: [Errno 13] Permission denied: '/share/apps/contrib/sage-4.3.3/devel/sage/doc/en/tutorial/static'
**********************************************************************
4 items had failures:
   2 of   5 in __main__.example_4
   2 of   5 in __main__.example_5
   2 of   5 in __main__.example_6
   1 of   4 in __main__.example_7
***Test Failed*** 7 failures.
For whitespace errors, see the file /home/rwh4s/.sage//tmp/.doctest_builder.py
	 [6.9 s]
```



---

Comment by mkoeppe created at 2020-08-17 16:38:58

Changing status from new to needs_review.


---

Comment by mkoeppe created at 2020-08-17 16:38:58

Outdated spkg or build system ticket, should be closed


---

Comment by mmezzarobba created at 2020-10-31 07:26:44

Changing status from needs_review to positive_review.


---

Comment by chapoton created at 2020-10-31 07:34:19

Resolution: invalid
