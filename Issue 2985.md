# Issue 2985: ITANIUM (RHEL 5) -- bug in rubik.py's OptimalSolver()

Issue created by migration from https://trac.sagemath.org/ticket/2985

Original creator: was

Original creation time: 2008-04-21 04:39:21

Assignee: mabshoff


```
[wstein@cleo sage-3.0.rc0]$ ./sage -t --long devel/sage/sage/interfaces/rubik.py
sage -t --long devel/sage/sage/interfaces/rubik.py          **********************************************************************
File "/home/wstein/sage-3.0.rc0/tmp/rubik.py", line 132:
    sage: solver = OptimalSolver() # long time
Exception raised:
    Traceback (most recent call last):
      File "/home/wstein/sage-3.0.rc0/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_3[3]>", line 1, in <module>
        solver = OptimalSolver() # long time###line 132:
    sage: solver = OptimalSolver() # long time
      File "/home/wstein/sage-3.0.rc0/local/lib/python2.5/site-packages/sage/interfaces/rubik.py", line 98, in __init__
        self.ready()
      File "/home/wstein/sage-3.0.rc0/local/lib/python2.5/site-packages/sage/interfaces/rubik.py", line 117, in ready
        self.child.expect('enter cube')
      File "/home/wstein/sage-3.0.rc0/local/lib/python2.5/site-packages/pexpect.py", line 912, in expect
        return self.expect_list(compiled_pattern_list, timeout, searchwindowsize)
      File "/home/wstein/sage-3.0.rc0/local/lib/python2.5/site-packages/pexpect.py", line 978, in expect_list
        raise EOF (str(e) + '\n' + str(self))
    EOF: End Of File (EOF) in read_nonblocking(). Exception style platform.
    <pexpect.spawn instance at 0x6000000003270950>
    version: 2.0 ($Revision: 1.151 $)
    command: /home/wstein/sage-3.0.rc0/local/bin/optimal
    args: ['/home/wstein/sage-3.0.rc0/local/bin/optimal']
    patterns:
        enter cube
    buffer (last 100 chars): 
    before (last 100 chars): *********
    1 items had failures:
       1 of  10 in __main__.example_3
    ***Test Failed*** 1 failures.

    after: <class 'pexpect.EOF'>
    match: None
    match_index: None
    exitstatus: None
    flag_eof: 1
    pid: 18447
    child_fd: 3
    timeout: None
    delimiter: <class 'pexpect.EOF'>
    logfile: None
    maxread: 2000
    searchwindowsize: None
    delaybeforesend: 0.1
**********************************************************************
1 items had failures:
   1 of  10 in __main__.example_3
***Test Failed*** 1 failures.
For whitespace errors, see the file /home/wstein/sage-3.0.rc0/tmp/.doctest_rubik.py
         [49.0 s]
exit code: 1024
 
----------------------------------------------------------------------
The following tests failed:



```



---

Comment by mabshoff created at 2008-04-25 04:17:10

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-04-25 04:17:10

The issue also happens on Ubuntu 6.06 LTS on AMD64.

Cheers,

Michaek


---

Comment by mabshoff created at 2008-04-25 06:22:04

Arrg, somebody [I know who] didn't remove the i686 optimal and twist binaries in the reid solver. We also did build reid without any optimization. The spkg at

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.0.1/alpha0/rubiks-20070912.p6.spkg

fixes that.

Doctest pass on x86-64, Itanium and OSX.

Cheers,

Michael


---

Comment by gfurnish created at 2008-04-25 06:25:37

works for me


---

Comment by mabshoff created at 2008-04-25 06:34:27

Resolution: fixed


---

Comment by mabshoff created at 2008-04-25 06:34:27

Merged in Sage 3.0.1.alpha0
