# Issue 3593: dsage-interfaces -- error decompressing data

Issue created by migration from https://trac.sagemath.org/ticket/3593

Original creator: was

Original creation time: 2008-07-07 22:13:28

Assignee: yi

I got this when running the test on a heavily loaded system.   It's probably an issue with reading a file that hasn't been completely written yet.  !

```
sage -t  devel/sage/sage/dsage/database/sql_functions.py (skipping) -- nodoctest.py file in directory
sage -t  devel/sage/sage/dsage/interface/sage_interface.py **********************************************************************
File "/home/was/build/sage-3.0.4.alpha2/tmp/dsage_interface.py", line 466:
    sage: j = d.block_on_jobs(d.map(f, [25,12,25,32,12]))
Exception raised:
    Traceback (most recent call last):
      File "/home/was/build/sage-3.0.4.alpha2/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_13[10]>", line 1, in <module>
        j = d.block_on_jobs(d.map(f, [Integer(25),Integer(12),Integer(25),Integer(32),Integer(12)]))###line 466:
    sage: j = d.block_on_jobs(d.map(f, [25,12,25,32,12]))
      File "/home/was/build/sage-3.0.4.alpha2/local/lib/python2.5/site-packages/sage/dsage/interface/dsage_interface.py", line 476, in block_on_jobs
        j.get_job()
      File "/home/was/build/sage-3.0.4.alpha2/local/lib/python2.5/site-packages/sage/dsage/interface/dsage_interface.py", line 1009, in get_job
        self._update_job(jdict)
      File "/home/was/build/sage-3.0.4.alpha2/local/lib/python2.5/site-packages/sage/dsage/interface/dsage_interface.py", line 820, in _update_job
        job = expand_job(jdict)
      File "/home/was/build/sage-3.0.4.alpha2/local/lib/python2.5/site-packages/sage/dsage/database/job.py", line 177, in expand_job
        jdict['result'] = zlib.decompress(jdict['result'])
    error: Error -5 while decompressing data
**********************************************************************
File "/home/was/build/sage-3.0.4.alpha2/tmp/dsage_interface.py", line 467:
    sage: print "ignore this";  j # random
Exception raised:
    Traceback (most recent call last):
      File "/home/was/build/sage-3.0.4.alpha2/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_13[11]>", line 1, in <module>
        print "ignore this";  j # random###line 467:
    sage: print "ignore this";  j # random
    NameError: name 'j' is not defined
**********************************************************************
1 items had failures:
   2 of  12 in __main__.example_13
***Test Failed*** 2 failures.
[DSage] Closed connection to localhost
[DSage] Closed connection to localhost
[DSage] Closed connection to localhost
[DSage] Closed connection to localhost
For whitespace errors, see the file /home/was/build/sage-3.0.4.alpha2/tmp/.doctest_dsage_interface.pyUnhandled exception in thread started by <bound method Thread.__bootstrap of <Thread(PoolThread-twisted.internet.reactor-1, stopped)>>
Traceback (most recent call last):
  File "/home/was/build/sage-3.0.4.alpha
```



---

Comment by was created at 2008-07-08 06:21:27

This bug is also in sage-3.0.4.rc0 on arch linux.


---

Comment by was created at 2008-07-08 06:22:31

Changing priority from major to blocker.


---

Comment by was created at 2008-07-08 06:22:31

Additional problems:

On sage.math we have

```
sage -t  devel/sage/sage/dsage/interface/dsage_interface.py **********************************************************************
File "/home/was/build/sage-3.0.4.rc0/tmp/dsage_interface.py", line 461:
    sage: d.is_connected()
Expected:
    True
Got:
    False
**********************************************************************
File "/home/was/build/sage-3.0.4.rc0/tmp/dsage_interface.py", line 466:
    sage: j = d.block_on_jobs(d.map(f, [25,12,25,32,12]))
Exception raised:
    Traceback (most recent call last):
      File "/home/was/build/sage-3.0.4.rc0/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_13[10]>", line 1, in <module>
        j = d.block_on_jobs(d.map(f, [Integer(25),Integer(12),Integer(25),Integer(32),Integer(12)]))###line 466:
    sage: j = d.block_on_jobs(d.map(f, [25,12,25,32,12]))
      File "/home/was/build/sage-3.0.4.rc0/local/lib/python2.5/site-packages/sage/dsage/interface/dsage_interface.py", line 518, in map
        for a in izip(*args)]
      File "/home/was/build/sage-3.0.4.rc0/local/lib/python2.5/site-packages/sage/dsage/interface/dsage_interface.py", line 609, in eval_function
        wrapped_job = BlockingJobWrapper(self._remoteobj, job)
      File "/home/was/build/sage-3.0.4.rc0/local/lib/python2.5/site-packages/sage/dsage/interface/dsage_interface.py", line 982, in __init__
        self.job_id = blockingCallFromThread(reactor, self._remoteobj.callRemote,
    AttributeError: 'NoneType' object has no attribute 'callRemote'
**********************************************************************
File "/home/was/build/sage-3.0.4.rc0/tmp/dsage_interface.py", line 467:
    sage: print "ignore this";  j # random
Exception raised:
    Traceback (most recent call last):
      File "/home/was/build/sage-3.0.4.rc0/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_13[11]>", line 1, in <module>
        print "ignore this";  j # random###line 467:
    sage: print "ignore this";  j # random
    NameError: name 'j' is not defined
**********************************************************************
File "/home/was/build/sage-3.0.4.rc0/tmp/dsage_interface.py", line 501:
    sage: d.is_connected()
Expected:
    True
Got:
    False
**********************************************************************
File "/home/was/build/sage-3.0.4.rc0/tmp/dsage_interface.py", line 506:
    sage: j = d.map(f, [25,12,25,32,12])
Exception raised:
    Traceback (most recent call last):
      File "/home/was/build/sage-3.0.4.rc0/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_14[10]>", line 1, in <module>
        j = d.map(f, [Integer(25),Integer(12),Integer(25),Integer(32),Integer(12)])###line 506:
    sage: j = d.map(f, [25,12,25,32,12])
      File "/home/was/build/sage-3.0.4.rc0/local/lib/python2.5/site-packages/sage/dsage/interface/dsage_interface.py", line 518, in map
        for a in izip(*args)]
      File "/home/was/build/sage-3.0.4.rc0/local/lib/python2.5/site-packages/sage/dsage/interface/dsage_interface.py", line 609, in eval_function
        wrapped_job = BlockingJobWrapper(self._remoteobj, job)
      File "/home/was/build/sage-3.0.4.rc0/local/lib/python2.5/site-packages/sage/dsage/interface/dsage_interface.py", line 982, in __init__
        self.job_id = blockingCallFromThread(reactor, self._remoteobj.callRemote,
    AttributeError: 'NoneType' object has no attribute 'callRemote'
**********************************************************************
                                                                                                                                                       1329,42       55%
etc.
```



---

Attachment


---

Comment by yi created at 2008-07-08 07:52:17

I was able to reproduce the problem on sage.math by running 4 doctests simultaneously. The problem is that we weren't using temporary directories for the separate dsage servers so twistd never launched the other servers.  Attached is a patch that fixes this issue.


---

Attachment


---

Attachment

This will bind to port 0 and the OS will return a valid port to listen on


---

Comment by mabshoff created at 2008-07-09 16:20:41

Resolution: fixed


---

Comment by mabshoff created at 2008-07-09 16:20:41

Merged in Sage 3.0.4.rc1


---

Comment by yi created at 2008-07-09 16:30:28

Did you merge in William's patch to disable doctesting or my patches to fix doctesting?


---

Comment by mabshoff created at 2008-07-09 16:34:18

Replying to [comment:9 yi]:
> Did you merge in William's patch to disable doctesting or my patches to fix doctesting?

I have not looked in detail, but I believe the patch to disable the doctest was merged for now. Please check rc2 and in case I am right open a new ticket with your patches and a reversal patch for what William did. Sorry for the confusion, William mentioned this ticket ought to be closed, so I did it without checking the details.

Cheers,

Michael
