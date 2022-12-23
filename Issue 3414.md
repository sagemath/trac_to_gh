# Issue 3414: sage-3.0.3.alpha2 -- massive dsage "testdoc.py" failures on osx ppc

Issue created by migration from https://trac.sagemath.org/ticket/3414

Original creator: was

Original creation time: 2008-06-13 14:25:18

Assignee: yi

On fermat.math.harvard.edu an osx ppc box, testdoc.py fails all over the place:

```
sage -t  devel/sage/sage/dsage/tests/testdoc.py             **********************************************************************
File "/Users/was/build/sage-3.0.3.alpha2/tmp/testdoc.py", line 12:
    sage: a = d('2 + 3')
Exception raised:
    Traceback (most recent call last):
      File "/Users/was/build/sage-3.0.3.alpha2/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[8]>", line 1, in <module>
        a = d('2 + 3')###line 12:
    sage: a = d('2 + 3')
      File "/Users/was/build/sage-3.0.3.alpha2/local/lib/python2.5/site-packages/sage/dsage/interface/dsage_interface.py", line 128, in __call__
        job_name=job_name)
      File "/Users/was/build/sage-3.0.3.alpha2/local/lib/python2.5/site-packages/sage/dsage/interface/dsage_interface.py", line 446, in eval
        wrapped_job = BlockingJobWrapper(self._remoteobj, job)
      File "/Users/was/build/sage-3.0.3.alpha2/local/lib/python2.5/site-packages/sage/dsage/interface/dsage_interface.py", line 776, in __init__
        self.job_id = blockingCallFromThread(reactor, self._remoteobj.callRemote,
    AttributeError: 'NoneType' object has no attribute 'callRemote'
**********************************************************************
File "/Users/was/build/sage-3.0.3.alpha2/tmp/testdoc.py", line 13:
    sage: a.wait(timeout=30)
Exception raised:
    Traceback (most recent call last):
      File "/Users/was/build/sage-3.0.3.alpha2/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[9]>", line 1, in <module>
        a.wait(timeout=Integer(30))###line 13:
    sage: a.wait(timeout=30)
    NameError: name 'a' is not defined
**********************************************************************
File "/Users/was/build/sage-3.0.3.alpha2/tmp/testdoc.py", line 14:
    sage: a
Exception raised:
    Traceback (most recent call last):
      File "/Users/was/build/sage-3.0.3.alpha2/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[10]>", line 1, in <module>
        a###line 14:
    sage: a
    NameError: name 'a' is not defined
**********************************************************************
File "/Users/was/build/sage-3.0.3.alpha2/tmp/testdoc.py", line 19:
    sage: job_id = a.kill()
Exception raised:
    Traceback (most recent call last):
      File "/Users/was/build/sage-3.0.3.alpha2/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[11]>", line 1, in <module>
        job_id = a.kill()###line 19:
    sage: job_id = a.kill()
    NameError: name 'a' is not defined
**********************************************************************
File "/Users/was/build/sage-3.0.3.alpha2/tmp/testdoc.py", line 20:
    sage: v = [d('%s^2'%i) for i in range(100,103)]
Exception raised:
    Traceback (most recent call last):
      File "/Users/was/build/sage-3.0.3.alpha2/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[12]>", line 1, in <module>
        v = [d('%s^2'%i) for i in range(Integer(100),Integer(103))]###line 20:
    sage: v = [d('%s^2'%i) for i in range(100,103)]
      File "/Users/was/build/sage-3.0.3.alpha2/local/lib/python2.5/site-packages/sage/dsage/interface/dsage_interface.py", line 128, in __call__
        job_name=job_name)
      File "/Users/was/build/sage-3.0.3.alpha2/local/lib/python2.5/site-packages/sage/dsage/interface/dsage_interface.py", line 446, in eval
        wrapped_job = BlockingJobWrapper(self._remoteobj, job)
      File "/Users/was/build/sage-3.0.3.alpha2/local/lib/python2.5/site-packages/sage/dsage/interface/dsage_interface.py", line 776, in __init__
        self.job_id = blockingCallFromThread(reactor, self._remoteobj.callRemote,
    AttributeError: 'NoneType' object has no attribute 'callRemote'
**********************************************************************
File "/Users/was/build/sage-3.0.3.alpha2/tmp/testdoc.py", line 28:
    sage: _ = [x.kill() for x in v]
Exception raised:
    Traceback (most recent call last):
      File "/Users/was/build/sage-3.0.3.alpha2/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[13]>", line 1, in <module>
        _ = [x.kill() for x in v]###line 28:
    sage: _ = [x.kill() for x in v]
    NameError: name 'v' is not defined
*********************************************************************
File "/Users/was/build/sage-3.0.3.alpha2/tmp/testdoc.py", line 31:
    sage: j = d('a+b', user_vars={'a': a, 'b': b})
Exception raised:
    Traceback (most recent call last):
      File "/Users/was/build/sage-3.0.3.alpha2/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[16]>", line 1, in <module>
        j = d('a+b', user_vars={'a': a, 'b': b})###line 31:
    sage: j = d('a+b', user_vars={'a': a, 'b': b})
      File "/Users/was/build/sage-3.0.3.alpha2/local/lib/python2.5/site-packages/sage/dsage/interface/dsage_interface.py", line 128, in __call__
        job_name=job_name)
      File "/Users/was/build/sage-3.0.3.alpha2/local/lib/python2.5/site-packages/sage/dsage/interface/dsage_interface.py", line 446, in eval
        wrapped_job = BlockingJobWrapper(self._remoteobj, job)
      File "/Users/was/build/sage-3.0.3.alpha2/local/lib/python2.5/site-packages/sage/dsage/interface/dsage_interface.py", line 776, in __init__
        self.job_id = blockingCallFromThread(reactor, self._remoteobj.callRemote,
    AttributeError: 'NoneType' object has no attribute 'callRemote'
**********************************************************************
File "/Users/was/build/sage-3.0.3.alpha2/tmp/testdoc.py", line 32:
    sage: j.wait()
Exception raised:
    Traceback (most recent call last):
      File "/Users/was/build/sage-3.0.3.alpha2/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[17]>", line 1, in <module>
        j.wait()###line 32:
    sage: j.wait()
    NameError: name 'j' is not defined
**********************************************************************
File "/Users/was/build/sage-3.0.3.alpha2/tmp/testdoc.py", line 33:
    sage: j
Exception raised:
    Traceback (most recent call last):
      File "/Users/was/build/sage-3.0.3.alpha2/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[18]>", line 1, in <module>
        j###line 33:
    sage: j
    NameError: name 'j' is not defined
**********************************************************************
File "/Users/was/build/sage-3.0.3.alpha2/tmp/testdoc.py", line 46:
    sage: reactor.callFromThread(reactor.stop); sleep(1)
Expected:
    [DSage] Closed connection to localhost
Got nothing
**********************************************************************
1 items had failures:
  10 of  23 in __main__.example_0
***Test Failed*** 10 failures.
For whitespace errors, see the file /Users/was/build/sage-3.0.3.alpha2/tmp/.doctest_testdoc.py
         [12.2 s]
```



---

Comment by was created at 2008-06-13 22:33:10

The network on this machine is foobar'd.


---

Comment by was created at 2008-06-13 22:33:10

Resolution: invalid
