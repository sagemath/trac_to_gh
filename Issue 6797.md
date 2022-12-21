# Issue 6797: doctest failure in sage/sage/groups/perm_gps/cubegroup.py due to upgrade to Maxima 5.19.1

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2009-08-21 08:02:41

Assignee: tbd

Keywords: maxima

On Solaris 10 update 7 (SPARC), the following tests failed. Both ECL and Maxima were updated - ECL version 9.8.4 (see trac #6564); Maxima version 5.19.1 (see trac #6699). Updated spkgs can be found here. 

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
sage -t  "devel/sage/sage/groups/perm_gps/cubegroup.py"
**********************************************************************
File "/export/home/drkirkby/sage/sage-4.1.1/devel/sage/sage/groups/perm_gps/cubegroup.py", line 892:
    sage: rubik.solve(state)
Exception raised:
    Traceback (most recent call last):
      File "/export/home/drkirkby/sage/sage-4.1.1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/export/home/drkirkby/sage/sage-4.1.1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/export/home/drkirkby/sage/sage-4.1.1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_16[4]>", line 1, in <module>
        rubik.solve(state)###line 892:
    sage: rubik.solve(state)
      File "/export/home/drkirkby/sage/sage-4.1.1/local/lib/python/site-packages/sage/groups/perm_gps/cubegroup.py", line 913, in solve
        return C.solve(algorithm)
      File "/export/home/drkirkby/sage/sage-4.1.1/local/lib/python/site-packages/sage/groups/perm_gps/cubegroup.py", line 1106, in solve
        return solver.solve(self.facets(), timeout=timeout)
      File "/export/home/drkirkby/sage/sage-4.1.1/local/lib/python/site-packages/sage/interfaces/rubik.py", line 254, in solve
        child.expect('Initialization done!')
      File "/export/home/drkirkby/sage/sage-4.1.1/local/lib/python/site-packages/pexpect.py", line 912, in expect
        return self.expect_list(compiled_pattern_list, timeout, searchwindowsize)
      File "/export/home/drkirkby/sage/sage-4.1.1/local/lib/python/site-packages/pexpect.py", line 989, in expect_list
        raise TIMEOUT (str(e) + '\n' + str(self))
    TIMEOUT: Timeout exceeded in read_nonblocking().
    <pexpect.spawn instance at 0x3958c10>
    version: 2.0 ($Revision: 1.151 $)
    command: /export/home/drkirkby/sage/sage-4.1.1/local/bin/dikcube
    args: ['/export/home/drkirkby/sage/sage-4.1.1/local/bin/dikcube', '-p']
    patterns:
        Initialization done!
    buffer (last 100 chars):
    before (last 100 chars): ice orders...
            Initialized = 24
            Maxpath = 4
        Done!
        Initializing mixed...

    after: <class 'pexpect.TIMEOUT'>
    match: None
    match_index: None
    exitstatus: None
    flag_eof: 0
    pid: 17118
    child_fd: 4
    timeout: 30
    delimiter: <class 'pexpect.EOF'>
    logfile: None
    maxread: 2000
    searchwindowsize: None
    delaybeforesend: 0.1
**********************************************************************
1 items had failures:
   1 of   6 in __main__.example_16
***Test Failed*** 1 failures.
For whitespace errors, see the file /export/home/drkirkby/sage/sage-4.1.1/tmp/.doctest_cubegroup.py
         [173.9 s]

```



---

Comment by wdj created at 2009-08-21 11:05:38

The Rubik's cube solver (I think) calls a C program. Can it be tested if that C program is compiled correctly?

But honestly, I don't know what this failure means. I think Robert Bradshaw needs to look at it.


---

Comment by AlexGhitza created at 2009-11-15 13:04:12

Changing component from algebra to solaris.


---

Comment by jdemeyer created at 2013-12-02 20:51:58

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2013-12-02 20:52:12

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2013-12-05 08:07:43

Resolution: invalid
