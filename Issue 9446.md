# Issue 9446: misc/trace.py doctest failure on t2 (solaris)

Issue created by migration from https://trac.sagemath.org/ticket/9446

Original creator: jhpalmieri

Original creation time: 2010-07-07 05:45:50

Assignee: jason

CC:  drkirkby justin mhansen

With Sage 4.5.alpha4 on t2.math.washington.edu (solaris):

```
sage -t  -long devel/sage/sage/misc/trace.py
**********************************************************************
File "/home/palmieri/t2/sage-4.5.alpha4/devel/sage-main/sage/misc/trace.py", line 54:
    sage: _ = s.expect('100')
Exception raised:
    Traceback (most recent call last):
      File "/home/palmieri/t2/sage-4.5.alpha4/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/palmieri/t2/sage-4.5.alpha4/local/bin/sagedoctest.py", line 38, in run_one_examp\
le
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/palmieri/t2/sage-4.5.alpha4/local/bin/ncadoctest.py", line 1172, in run_one_exam\
ple
        compileflags, 1) in test.globs
      File "<doctest __main__.example_1[6]>", line 1, in <module>
        _ = s.expect('100')###line 54:
    sage: _ = s.expect('100')
      File "/home/palmieri/t2/sage-4.5.alpha4/local/lib/python/site-packages/pexpect.py", line 912\
, in expect
        return self.expect_list(compiled_pattern_list, timeout, searchwindowsize)
      File "/home/palmieri/t2/sage-4.5.alpha4/local/lib/python/site-packages/pexpect.py", line 989\
, in expect_list
        raise TIMEOUT (str(e) + '\n' + str(self))
    TIMEOUT: Timeout exceeded in read_nonblocking().
    <pexpect.spawn instance at 0x2c005d0>
    version: 2.0 ($Revision: 1.151 $)
    command: /home/palmieri/t2/sage-4.5.alpha4/sage
    args: ['/home/palmieri/t2/sage-4.5.alpha4/sage']
    patterns:
        100
    buffer (last 100 chars):
    before (last 100 chars):                       *^M
    **********************************************************************^M
    c^M

    after: <class 'pexpect.TIMEOUT'>
    match: None
    match_index: None
    exitstatus: None
    flag_eof: 0
    pid: 22383
    child_fd: 4
    timeout: 30
    delimiter: <class 'pexpect.EOF'>
    logfile: None
    maxread: 2000
    searchwindowsize: None
    delaybeforesend: 0.1
**********************************************************************
File "/home/palmieri/t2/sage-4.5.alpha4/devel/sage-main/sage/misc/trace.py", line 61:
    sage: print s.before[s.before.find('-'):]
Expected:
    ---...
    ipdb> c
    2 * 5
Got:
    ----------------------------------------------------------------------^M
    | Sage Version 4.5.alpha4, Release Date: 2010-07-06                  |^M
    | Type notebook() for the GUI, and license() for information.        |^M
    ----------------------------------------------------------------------^M
    **********************************************************************^M
    *                                                                    *^M
    * Warning: this is a prerelease version, and it may be unstable.     *^M
    *                                                                    *^M
    **********************************************************************^M
    c^M
    <BLANKLINE>
**********************************************************************
```

Is this due to something timing out?


---

Comment by drkirkby created at 2010-07-07 07:10:11

This does not look like a timeout to me - at least not like one I've seen. Have you set something like the following?


```
SAGE_TIMEOUT_LONG=10000
SAGE_TIMEOUT=1000
export SAGE_TIMEOUT_LONG
export SAGE_TIMEOUT
```


I'm just making a build on t2 myself. I'll see if I get this issue.


---

Comment by drkirkby created at 2010-07-07 09:12:13

This is odd:


```
kirkby@t2:[/tmp/kirkby/sage-4.5.alpha4] $ ./sage -t  -long devel/sage/sage/misc/trace.py
sage -t -long "devel/sage/sage/misc/trace.py"               
	 [29.7 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 29.7 seconds
kirkby@t2:[/tmp/kirkby/sage-4.5.alpha4] $ 
```


Can you retry the test John. 

I'm personally quite suspicious about using /home anywhere on *.math.washington.edu, since I'm aware the NFS directories are shared from a server (disk.math) which has the default configuration of the pools modified to increase performance, in a manner which risks data corruption on NFS shares. 

Dave


---

Comment by jhpalmieri created at 2010-07-07 15:49:01

The first three times I ran the test, I had a failure.  Now I've run it without a failure, too, so I'm changing the "blocker" status.

Since it's not even reproducible, should this ticket be closed?


---

Comment by jhpalmieri created at 2010-07-07 15:49:01

Changing priority from blocker to minor.


---

Comment by drkirkby created at 2010-07-07 20:28:35

Replying to [comment:3 jhpalmieri]:
> The first three times I ran the test, I had a failure.  Now I've run it without a failure, too, so I'm changing the "blocker" status.
> 
> Since it's not even reproducible, should this ticket be closed?

I think not yet. There are a lot of doctest failures which seem to not be reproducible. I think something is screwed up with the doctesting framework myself.


---

Comment by mpatel created at 2010-10-02 21:38:34

Changing assignee from jason to mvngu.


---

Comment by mpatel created at 2010-10-02 21:38:34

Changing component from misc to doctest.


---

Comment by mpatel created at 2010-10-02 21:38:34

Justin Walker has [seen this problem with 4.6.alpha2](http://groups.google.com/group/sage-release/msg/fe720bce3f933171) on two OS X 10.6.4 systems (Dual Quad Xeon, Core i7):

```python
sage -t  -long devel/sage/sage/misc/trace.py
**********************************************************************
File "/Users/Sage/sage-4.6.alpha0/devel/sage-main/sage/misc/trace.py", line 61:
    sage: print s.before[s.before.find('-'):]
Expected:
    ---...
    ipdb> c
    2 * 5
Got:
    -bit mode
    Creating SAGE_LOCAL/lib/sage-64.txt since it does not exist
    Detected SAGE64 flag
    Building Sage on OS X in 64-bit mode
    ----------------------------------------------------------------------
    | Sage Version 4.6.alpha2, Release Date: 2010-09-29                  |
    | Type notebook() for the GUI, and license() for information.        |
    ----------------------------------------------------------------------
    **********************************************************************
    *                                                                    *
    * Warning: this is a prerelease version, and it may be unstable.     *
    *                                                                    *
    **********************************************************************
    trace('print factor(10)'); print 3+97
    s
    c
    sage: trace('print factor(10)'); print 3+97
    > <string>(1)<module>()
    
    ipdb> s
    --Call--
    > /Users/Sage/sage-4.6.alpha0/local/lib/python2.6/site-packages/sage/rings/arith.py(2153)factor()
       2152 
    -> 2153 def factor(n, proof=None, int_=False, algorithm='pari', verbose=0, **kwds):
       2154     """
    
    ipdb> c
    2 * 5
    <BLANKLINE>
```



---

Comment by drkirkby created at 2010-10-03 05:36:06

I'm changing the priority of this to the default "major" since it was only changed to minor when it was thought to be almost a non-issue. 

Dave


---

Comment by drkirkby created at 2010-10-03 05:37:41

Changing priority from minor to major.


---

Comment by mpatel created at 2010-10-10 03:10:47

Maybe the problem is that `pexpect`'s default timeout (30 seconds) is exceeded under load.  For example

```python
sage: import pexpect
sage: s = pexpect.spawn('sage')
sage: _ = s.sendline("trace('print factor(10)'); import time; time.sleep(31); print 3+97")
sage: _ = s.sendline("s"); _ = s.sendline("c");
sage: _ = s.expect('100')
---------------------------------------------------------------------------
TIMEOUT                                   Traceback (most recent call last)
[...]
TIMEOUT: Timeout exceeded in read_nonblocking().
<pexpect.spawn instance at 0x6d9d88>
version: 2.0 ($Revision: 1.151 $)
command: /home/mpatel/apps/sage/sage
args: ['/home/mpatel/apps/sage/sage']
patterns:
    100
buffer (last 100 chars):
before (last 100 chars): , proof=None, int_=False, algorithm='pari', verbose=0, **kwds):
   2154     """

ipdb> c
2 * 5

after: <class 'pexpect.TIMEOUT'>
match: None
match_index: None
exitstatus: None
flag_eof: 0
pid: 29286
child_fd: 3
timeout: 30
delimiter: <class 'pexpect.EOF'>
logfile: None
maxread: 2000
searchwindowsize: None
delaybeforesend: 0.1
sage: 
```



---

Comment by mpatel created at 2010-10-10 03:27:29

With

```python
def example(verbose=False, **kwargs):
    error = False
    try:
        import pexpect
        s = pexpect.spawn('sage')
        _ = s.sendline("trace('print factor(10)'); print 3+97")
        _ = s.sendline("s"); _ = s.sendline("c");
        _ = s.expect('100', timeout=kwargs['timeout'])
        t = s.before[s.before.find('-'):]
        if not t.strip().endswith('ipdb> c\r\n2 * 5'):
            raise Exception('"Got" does not match "Expected"')

    except Exception as exc:
        error = True
        if verbose:
            print exc
    return error

def runner(n=1000, verbose=False, **kwargs):
    fail = 0
    for i in xrange(n):
        fail += example(verbose, **kwargs)
    return fail

runner(100, timeout=1)
```

I get 13 failures on sage.math, at least some of which I may have induced with a simultaneous `sage -tp`.  This 4.6.alpha3 installation is under `/scratch`.


---

Attachment

Increase pexpect timeout for test


---

Comment by mpatel created at 2010-10-10 03:32:15

Changing status from new to needs_review.


---

Comment by mpatel created at 2010-10-10 03:32:15

I've attached a patch that increases the timeout to 90 seconds.


---

Comment by mpatel created at 2010-10-22 06:53:57

Replying to [comment:5 mpatel]:
> Justin Walker has [seen this problem with 4.6.alpha2](http://groups.google.com/group/sage-release/msg/fe720bce3f933171) on two OS X 10.6.4 systems (Dual Quad Xeon, Core i7):

See #10138 for this problem, which is specific to 64-bit builds.


---

Comment by mariah created at 2011-05-26 15:57:40

Changing status from needs_review to positive_review.


---

Comment by mariah created at 2011-05-26 15:57:40

I did 'make NUM_THREADS=10 ptestlong' on a 4.7.rc4 build on skynet/eno and had one test failure, which passed with I ran it individually.  (So I suspect a timeout problem.)  I then applied the patch and did 'make NUM_THREADS=10 ptestlong' again, and this time all the tests passed. 

Positive review.


---

Comment by jdemeyer created at 2011-05-31 17:07:06

Resolution: fixed
