# Issue 2983: Itanium (RHEL 5) -- singular interface problems in matrix_group.py

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-04-21 03:25:38

Assignee: mabshoff

This may get resolved by fixing #2209.


```
sage -t  devel/sage/sage/groups/matrix_gps/matrix_group.py  **********************************************************************
File "/home/wstein/sage-3.0.rc0/tmp/matrix_group.py", line 689:
    sage: G.invariant_generators()
Exception raised:
    Traceback (most recent call last):
      File "/home/wstein/sage-3.0.rc0/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_26[4]>", line 1, in <module>
        G.invariant_generators()###line 689:
    sage: G.invariant_generators()
      File "/home/wstein/sage-3.0.rc0/local/lib/python2.5/site-packages/sage/groups/matrix_gps/matrix_group.py", line 762, in invariant_generators
        singular.eval('matrix %s = invariant_algebra_reynolds(%s[1])'%(IRName,ReyName))
      File "/home/wstein/sage-3.0.rc0/local/lib/python2.5/site-packages/sage/interfaces/singular.py", line 416, in eval
        s = Expect.eval(self, x)
      File "/home/wstein/sage-3.0.rc0/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 722, in eval
        return '\n'.join([self._eval_line(L, **kwds) for L in code.split('\n') if L != ''])
      File "/home/wstein/sage-3.0.rc0/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 643, in _eval_line
        raise RuntimeError, "%s\n%s crashed executing %s"%(msg,self, line)
    RuntimeError: End Of File (EOF) in read_nonblocking(). Exception style platform.
    <pexpect.spawn instance at 0x6000000003666998>
    version: 2.0 ($Revision: 1.151 $)
    command: /home/wstein/sage-3.0.rc0/local/bin/Singular
    args: ['/home/wstein/sage-3.0.rc0/local/bin/Singular', '-t', '--ticks-per-sec', '1000']
    patterns:
        >
    buffer (last 100 chars):
    before (last 100 chars): me/wstein/sage-3.0.rc0/local/bin/Singular: line 2: 30877 Segmentation fault      Singular-3-0-4 $*^M

    after: <class 'pexpect.EOF'>
    match: None
    match_index: None
    exitstatus: 139
    flag_eof: 1
    pid: 30874
    child_fd: 5
    timeout: None
    delimiter: <class 'pexpect.EOF'>
    logfile: None
    maxread: 1000
    searchwindowsize: None
    delaybeforesend: 0
    Singular crashed executing matrix tsage4 = invariant_algebra_reynolds(tsage3[1]);

```



---

Comment by mabshoff created at 2008-04-21 04:36:27

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-04-21 04:36:27

Changing priority from major to blocker.


---

Comment by mabshoff created at 2008-04-21 04:36:27

This is definitely a problem with Singular segfaulting and not related to GAP AFAIK.

Cheers,

Michael


---

Comment by wdj created at 2008-04-21 10:33:40

My two cents:
(1) I don't see how this can be related to 2209, since it is a Singular crash not a GAP crash. AFAIK, the code for invariant_generators does not call GAP:
http://www.sagemath.org/hg/sage-main/file/cc1e12a492fc/sage/groups/matrix_gps/matrix_group.py
(2) It passes for me on ubuntu 7.10 amd64:


```
wdj`@`wooster:~/wdj/sagefiles/sage-3.0.rc0$ ./sage -t devel/sage/sage/groups/matrix_gps/matrix_group.py
sage -t  0/devel/sage/sage/groups/matrix_gps/matrix_group.py
         [42.7 s]

----------------------------------------------------------------------
All tests passed!
Total time for all tests: 42.7 seconds
```



---

Comment by mabshoff created at 2008-04-23 11:48:20

Yes, as other people have overserved this is a Singular issue unrelated to GAP. I will hopefully track this down for 3.0.1.

Cheers,

Michael


---

Comment by mabshoff created at 2008-05-02 05:17:07

Ahh, this is a gcc 4.1.2 specific issue - it does not segfault with a build from source gcc 4.3 on the same platform.

Cheers,

Michael


---

Comment by mabshoff created at 2008-05-05 17:19:26

Compiling with `-O2` fixes the issue. Patch coming up in a couple hours.

Cheers,

Michael


---

Attachment

The spkg at 

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.0.2/alpha0/singular-3-0-4-2-20080405.p2.spkg

fixes this and also #3158.

Cheers,

Michael


---

Comment by broune created at 2008-05-11 13:07:39

Builds for me on mac 10.5, can do 


```
sage: R=QQ['x,y,z']
sage: R(x^5)
x^5
sage: R(x^5)^2
x^10
```


also sage -t  devel/sage/sage/groups/matrix_gps/matrix_group.py passes with no errors.


---

Comment by mabshoff created at 2008-05-11 13:10:50

Merged in Sage 3.0.2.alpha0


---

Comment by mabshoff created at 2008-05-11 13:10:50

Resolution: fixed
