# Issue 3266: Sage 3.0.2.alpha1: doctest failure in sage/server/simple/twist.py

Issue created by migration from https://trac.sagemath.org/ticket/3266

Original creator: mabshoff

Original creation time: 2008-05-21 13:54:36

Assignee: failure


```
sage -t -long devel/sage/sage/server/simple/twist.py        
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.0.2.rc0/tmp/twist.py", line 81:
    sage: nb.dispose()
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/release-cycle/sage-3.0.2.rc0/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[20]>", line 1, in <module>
        nb.dispose()###line 81:
    sage: nb.dispose()
      File "/scratch/mabshoff/release-cycle/sage-3.0.2.rc0/local/lib/python2.5/site-packages/sage/server/notebook/notebook_object.py", line 195, in dispose
        p.expect("Press control-C again to exit")
      File "/scratch/mabshoff/release-cycle/sage-3.0.2.rc0/local/lib/python2.5/site-packages/pexpect.py", line 912, in expect
        return self.expect_list(compiled_pattern_list, timeout, searchwindowsize)
      File "/scratch/mabshoff/release-cycle/sage-3.0.2.rc0/local/lib/python2.5/site-packages/pexpect.py", line 978, in expect_list
        raise EOF (str(e) + '\n' + str(self))
    EOF: End of File (EOF) in read_nonblocking(). Very pokey platform.
    <pexpect.spawn instance at 0x2b73dba18518>
    version: 2.0 ($Revision: 1.151 $)
    command: /scratch/mabshoff/release-cycle/sage-3.0.2.rc0/sage
    args: ['/scratch/mabshoff/release-cycle/sage-3.0.2.rc0/sage', '-twistd', '--pidfile=tmpR1esq-/twistd.pid', '-ny', 'tmpR1esq-/twistedconf.tac']
    patterns:
        Press control-C again to exit
    buffer (last 100 chars):
    before (last 100 chars): 2008-05-21 06:53:03-0700 [-] Main loop terminated.
    2008-05-21 06:53:03-0700 [-] Server Shut Down.

    after: <class 'pexpect.EOF'>
    match: None
    match_index: None
    exitstatus: 0
    flag_eof: 1
    pid: 724
    child_fd: 3
    timeout: 30
    delimiter: <class 'pexpect.EOF'>
    logfile: None
    maxread: 2000
    searchwindowsize: None
    delaybeforesend: 0.1
**********************************************************************
1 items had failures:
   1 of  21 in __main__.example_0
***Test Failed*** 1 failures.
For whitespace errors, see the file /scratch/mabshoff/release-cycle/sage-3.0.2.rc0/tmp/.doctest_twist.py
         [38.7 s]
exit code: 1024
```



---

Attachment


---

Comment by mabshoff created at 2008-05-23 07:08:23

The patch fixes the issue. Positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-05-23 07:09:14

Resolution: fixed


---

Comment by mabshoff created at 2008-05-23 07:09:14

Merged in Sage 3.0.2.rc0
