# Issue 6794: doctest failure in sage/sage/interfaces/rubik.py due to upgrade to Maxima 5.19.1

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2009-08-21 07:12:24

Assignee: tbd

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
sage -t  "devel/sage/sage/interfaces/rubik.py"
**********************************************************************
File "/export/home/drkirkby/sage/sage-4.1.1/devel/sage/sage/interfaces/rubik.py", line 136:
    sage: solver.solve(C.facets())
Exception raised:
    Traceback (most recent call last):
      File "/export/home/drkirkby/sage/sage-4.1.1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/export/home/drkirkby/sage/sage-4.1.1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/export/home/drkirkby/sage/sage-4.1.1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_3[5]>", line 1, in <module>
        solver.solve(C.facets())###line 136:
    sage: solver.solve(C.facets())
      File "/export/home/drkirkby/sage/sage-4.1.1/local/lib/python/site-packages/sage/interfaces/rubik.py", line 254, in solve
        child.expect('Initialization done!')
      File "/export/home/drkirkby/sage/sage-4.1.1/local/lib/python/site-packages/pexpect.py", line 912, in expect
        return self.expect_list(compiled_pattern_list, timeout, searchwindowsize)
      File "/export/home/drkirkby/sage/sage-4.1.1/local/lib/python/site-packages/pexpect.py", line 989, in expect_list
        raise TIMEOUT (str(e) + '\n' + str(self))
    TIMEOUT: Timeout exceeded in read_nonblocking().
    <pexpect.spawn instance at 0x37b15a8>
    version: 2.0 ($Revision: 1.151 $)
    command: /export/home/drkirkby/sage/sage-4.1.1/local/bin/dikcube
    args: ['/export/home/drkirkby/sage/sage-4.1.1/local/bin/dikcube', '-p']
    patterns:
        Initialization done!
    buffer (last 100 chars):
    before (last 100 chars): ialized = 24
            Maxpath = 4
        Done!
        Initializing mixed...
            Maxpath(c+s) = 14

    after: <class 'pexpect.TIMEOUT'>
    match: None
    match_index: None
    exitstatus: None
    flag_eof: 0
    pid: 19689
    child_fd: 4
    timeout: 30
    delimiter: <class 'pexpect.EOF'>
    logfile: None
    maxread: 2000
    searchwindowsize: None
    delaybeforesend: 0.1
**********************************************************************
File "/export/home/drkirkby/sage/sage-4.1.1/devel/sage/sage/interfaces/rubik.py", line 139:
    sage: solver.solve(C.facets())
Exception raised:
    Traceback (most recent call last):
      File "/export/home/drkirkby/sage/sage-4.1.1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/export/home/drkirkby/sage/sage-4.1.1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/export/home/drkirkby/sage/sage-4.1.1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_3[7]>", line 1, in <module>
        solver.solve(C.facets())###line 139:
    sage: solver.solve(C.facets())
      File "/export/home/drkirkby/sage/sage-4.1.1/local/lib/python/site-packages/sage/interfaces/rubik.py", line 254, in solve
        child.expect('Initialization done!')
      File "/export/home/drkirkby/sage/sage-4.1.1/local/lib/python/site-packages/pexpect.py", line 912, in expect
        return self.expect_list(compiled_pattern_list, timeout, searchwindowsize)
      File "/export/home/drkirkby/sage/sage-4.1.1/local/lib/python/site-packages/pexpect.py", line 989, in expect_list
        raise TIMEOUT (str(e) + '\n' + str(self))
    TIMEOUT: Timeout exceeded in read_nonblocking().
    <pexpect.spawn instance at 0x37b17b0>
    version: 2.0 ($Revision: 1.151 $)
    command: /export/home/drkirkby/sage/sage-4.1.1/local/bin/dikcube
    args: ['/export/home/drkirkby/sage/sage-4.1.1/local/bin/dikcube', '-p']
    patterns:
        Initialization done!
    buffer (last 100 chars):
    before (last 100 chars): ialized = 24
            Maxpath = 4
        Done!
        Initializing mixed...
            Maxpath(c+s) = 14

    after: <class 'pexpect.TIMEOUT'>
    match: None
    match_index: None
    exitstatus: None
    flag_eof: 0
    pid: 26746
    child_fd: 5
    timeout: 30
    delimiter: <class 'pexpect.EOF'>
    logfile: None
    maxread: 2000
    searchwindowsize: None
    delaybeforesend: 0.1
**********************************************************************
File "/export/home/drkirkby/sage/sage-4.1.1/devel/sage/sage/interfaces/rubik.py", line 142:
    sage: solver.solve(C.facets())
Exception raised:
    Traceback (most recent call last):
      File "/export/home/drkirkby/sage/sage-4.1.1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/export/home/drkirkby/sage/sage-4.1.1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/export/home/drkirkby/sage/sage-4.1.1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_3[9]>", line 1, in <module>
        solver.solve(C.facets())###line 142:
    sage: solver.solve(C.facets())
      File "/export/home/drkirkby/sage/sage-4.1.1/local/lib/python/site-packages/sage/interfaces/rubik.py", line 254, in solve
        child.expect('Initialization done!')
      File "/export/home/drkirkby/sage/sage-4.1.1/local/lib/python/site-packages/pexpect.py", line 912, in expect
        return self.expect_list(compiled_pattern_list, timeout, searchwindowsize)
      File "/export/home/drkirkby/sage/sage-4.1.1/local/lib/python/site-packages/pexpect.py", line 989, in expect_list
        raise TIMEOUT (str(e) + '\n' + str(self))
    TIMEOUT: Timeout exceeded in read_nonblocking().
    <pexpect.spawn instance at 0x37b1918>
    version: 2.0 ($Revision: 1.151 $)
    command: /export/home/drkirkby/sage/sage-4.1.1/local/bin/dikcube
    args: ['/export/home/drkirkby/sage/sage-4.1.1/local/bin/dikcube', '-p']
    patterns:
        Initialization done!
    buffer (last 100 chars):
    before (last 100 chars): ialized = 24
            Maxpath = 4
        Done!
        Initializing mixed...
            Maxpath(c+s) = 14

    after: <class 'pexpect.TIMEOUT'>
    match: None
    match_index: None
    exitstatus: None
    flag_eof: 0
    pid: 4188
    child_fd: 4
    timeout: 30
    delimiter: <class 'pexpect.EOF'>
    logfile: None
    maxread: 2000
    searchwindowsize: None
    delaybeforesend: 0.1
**********************************************************************
File "/export/home/drkirkby/sage/sage-4.1.1/devel/sage/sage/interfaces/rubik.py", line 243:
    sage: DikSolver().solve(C.facets())
Exception raised:
    Traceback (most recent call last):
      File "/export/home/drkirkby/sage/sage-4.1.1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/export/home/drkirkby/sage/sage-4.1.1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/export/home/drkirkby/sage/sage-4.1.1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_5[4]>", line 1, in <module>
        DikSolver().solve(C.facets())###line 243:
    sage: DikSolver().solve(C.facets())
      File "/export/home/drkirkby/sage/sage-4.1.1/local/lib/python/site-packages/sage/interfaces/rubik.py", line 254, in solve
        child.expect('Initialization done!')
      File "/export/home/drkirkby/sage/sage-4.1.1/local/lib/python/site-packages/pexpect.py", line 912, in expect
        return self.expect_list(compiled_pattern_list, timeout, searchwindowsize)
      File "/export/home/drkirkby/sage/sage-4.1.1/local/lib/python/site-packages/pexpect.py", line 989, in expect_list
        raise TIMEOUT (str(e) + '\n' + str(self))
    TIMEOUT: Timeout exceeded in read_nonblocking().
    <pexpect.spawn instance at 0x38d2648>
    version: 2.0 ($Revision: 1.151 $)
    command: /export/home/drkirkby/sage/sage-4.1.1/local/bin/dikcube
    args: ['/export/home/drkirkby/sage/sage-4.1.1/local/bin/dikcube', '-p']
    patterns:
        Initialization done!
    buffer (last 100 chars):
    before (last 100 chars): path = 5
        Done!
        Initializing mixed...
            Maxpath(t+f) = 9
            Maxpath(t+c) = 9

    after: <class 'pexpect.TIMEOUT'>
    match: None
    match_index: None
    exitstatus: None
    flag_eof: 0
    pid: 12287
    child_fd: 5
    timeout: 30
    delimiter: <class 'pexpect.EOF'>
    logfile: None
    maxread: 2000
    searchwindowsize: None
    delaybeforesend: 0.1
**********************************************************************
2 items had failures:
   3 of  10 in __main__.example_3
   1 of   9 in __main__.example_5
***Test Failed*** 4 failures.
For whitespace errors, see the file /export/home/drkirkby/sage/sage-4.1.1/tmp/.doctest_rubik.py
         [243.9 s]
```



---

Comment by AlexGhitza created at 2009-11-15 13:03:19

Changing component from algebra to solaris.


---

Comment by drkirkby created at 2011-04-02 12:42:09

This can be closed as fixed. I'm not exactly sure what ticket caused this to be fixed, but it has been fixed a very long fixed ago.


---

Comment by jdemeyer created at 2011-04-05 15:55:24

Resolution: worksforme
