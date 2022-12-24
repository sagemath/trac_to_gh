# Issue 3414: sage-3.0.3.alpha2 -- massive dsage "testdoc.py" failures on osx ppc

archive/issues_003414.json:
```json
{
    "body": "Assignee: yi\n\nOn fermat.math.harvard.edu an osx ppc box, testdoc.py fails all over the place:\n\n```\nsage -t  devel/sage/sage/dsage/tests/testdoc.py             **********************************************************************\nFile \"/Users/was/build/sage-3.0.3.alpha2/tmp/testdoc.py\", line 12:\n    sage: a = d('2 + 3')\nException raised:\n    Traceback (most recent call last):\n      File \"/Users/was/build/sage-3.0.3.alpha2/local/lib/python2.5/doctest.py\", line 1228, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_0[8]>\", line 1, in <module>\n        a = d('2 + 3')###line 12:\n    sage: a = d('2 + 3')\n      File \"/Users/was/build/sage-3.0.3.alpha2/local/lib/python2.5/site-packages/sage/dsage/interface/dsage_interface.py\", line 128, in __call__\n        job_name=job_name)\n      File \"/Users/was/build/sage-3.0.3.alpha2/local/lib/python2.5/site-packages/sage/dsage/interface/dsage_interface.py\", line 446, in eval\n        wrapped_job = BlockingJobWrapper(self._remoteobj, job)\n      File \"/Users/was/build/sage-3.0.3.alpha2/local/lib/python2.5/site-packages/sage/dsage/interface/dsage_interface.py\", line 776, in __init__\n        self.job_id = blockingCallFromThread(reactor, self._remoteobj.callRemote,\n    AttributeError: 'NoneType' object has no attribute 'callRemote'\n**********************************************************************\nFile \"/Users/was/build/sage-3.0.3.alpha2/tmp/testdoc.py\", line 13:\n    sage: a.wait(timeout=30)\nException raised:\n    Traceback (most recent call last):\n      File \"/Users/was/build/sage-3.0.3.alpha2/local/lib/python2.5/doctest.py\", line 1228, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_0[9]>\", line 1, in <module>\n        a.wait(timeout=Integer(30))###line 13:\n    sage: a.wait(timeout=30)\n    NameError: name 'a' is not defined\n**********************************************************************\nFile \"/Users/was/build/sage-3.0.3.alpha2/tmp/testdoc.py\", line 14:\n    sage: a\nException raised:\n    Traceback (most recent call last):\n      File \"/Users/was/build/sage-3.0.3.alpha2/local/lib/python2.5/doctest.py\", line 1228, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_0[10]>\", line 1, in <module>\n        a###line 14:\n    sage: a\n    NameError: name 'a' is not defined\n**********************************************************************\nFile \"/Users/was/build/sage-3.0.3.alpha2/tmp/testdoc.py\", line 19:\n    sage: job_id = a.kill()\nException raised:\n    Traceback (most recent call last):\n      File \"/Users/was/build/sage-3.0.3.alpha2/local/lib/python2.5/doctest.py\", line 1228, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_0[11]>\", line 1, in <module>\n        job_id = a.kill()###line 19:\n    sage: job_id = a.kill()\n    NameError: name 'a' is not defined\n**********************************************************************\nFile \"/Users/was/build/sage-3.0.3.alpha2/tmp/testdoc.py\", line 20:\n    sage: v = [d('%s^2'%i) for i in range(100,103)]\nException raised:\n    Traceback (most recent call last):\n      File \"/Users/was/build/sage-3.0.3.alpha2/local/lib/python2.5/doctest.py\", line 1228, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_0[12]>\", line 1, in <module>\n        v = [d('%s^2'%i) for i in range(Integer(100),Integer(103))]###line 20:\n    sage: v = [d('%s^2'%i) for i in range(100,103)]\n      File \"/Users/was/build/sage-3.0.3.alpha2/local/lib/python2.5/site-packages/sage/dsage/interface/dsage_interface.py\", line 128, in __call__\n        job_name=job_name)\n      File \"/Users/was/build/sage-3.0.3.alpha2/local/lib/python2.5/site-packages/sage/dsage/interface/dsage_interface.py\", line 446, in eval\n        wrapped_job = BlockingJobWrapper(self._remoteobj, job)\n      File \"/Users/was/build/sage-3.0.3.alpha2/local/lib/python2.5/site-packages/sage/dsage/interface/dsage_interface.py\", line 776, in __init__\n        self.job_id = blockingCallFromThread(reactor, self._remoteobj.callRemote,\n    AttributeError: 'NoneType' object has no attribute 'callRemote'\n**********************************************************************\nFile \"/Users/was/build/sage-3.0.3.alpha2/tmp/testdoc.py\", line 28:\n    sage: _ = [x.kill() for x in v]\nException raised:\n    Traceback (most recent call last):\n      File \"/Users/was/build/sage-3.0.3.alpha2/local/lib/python2.5/doctest.py\", line 1228, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_0[13]>\", line 1, in <module>\n        _ = [x.kill() for x in v]###line 28:\n    sage: _ = [x.kill() for x in v]\n    NameError: name 'v' is not defined\n*********************************************************************\nFile \"/Users/was/build/sage-3.0.3.alpha2/tmp/testdoc.py\", line 31:\n    sage: j = d('a+b', user_vars={'a': a, 'b': b})\nException raised:\n    Traceback (most recent call last):\n      File \"/Users/was/build/sage-3.0.3.alpha2/local/lib/python2.5/doctest.py\", line 1228, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_0[16]>\", line 1, in <module>\n        j = d('a+b', user_vars={'a': a, 'b': b})###line 31:\n    sage: j = d('a+b', user_vars={'a': a, 'b': b})\n      File \"/Users/was/build/sage-3.0.3.alpha2/local/lib/python2.5/site-packages/sage/dsage/interface/dsage_interface.py\", line 128, in __call__\n        job_name=job_name)\n      File \"/Users/was/build/sage-3.0.3.alpha2/local/lib/python2.5/site-packages/sage/dsage/interface/dsage_interface.py\", line 446, in eval\n        wrapped_job = BlockingJobWrapper(self._remoteobj, job)\n      File \"/Users/was/build/sage-3.0.3.alpha2/local/lib/python2.5/site-packages/sage/dsage/interface/dsage_interface.py\", line 776, in __init__\n        self.job_id = blockingCallFromThread(reactor, self._remoteobj.callRemote,\n    AttributeError: 'NoneType' object has no attribute 'callRemote'\n**********************************************************************\nFile \"/Users/was/build/sage-3.0.3.alpha2/tmp/testdoc.py\", line 32:\n    sage: j.wait()\nException raised:\n    Traceback (most recent call last):\n      File \"/Users/was/build/sage-3.0.3.alpha2/local/lib/python2.5/doctest.py\", line 1228, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_0[17]>\", line 1, in <module>\n        j.wait()###line 32:\n    sage: j.wait()\n    NameError: name 'j' is not defined\n**********************************************************************\nFile \"/Users/was/build/sage-3.0.3.alpha2/tmp/testdoc.py\", line 33:\n    sage: j\nException raised:\n    Traceback (most recent call last):\n      File \"/Users/was/build/sage-3.0.3.alpha2/local/lib/python2.5/doctest.py\", line 1228, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_0[18]>\", line 1, in <module>\n        j###line 33:\n    sage: j\n    NameError: name 'j' is not defined\n**********************************************************************\nFile \"/Users/was/build/sage-3.0.3.alpha2/tmp/testdoc.py\", line 46:\n    sage: reactor.callFromThread(reactor.stop); sleep(1)\nExpected:\n    [DSage] Closed connection to localhost\nGot nothing\n**********************************************************************\n1 items had failures:\n  10 of  23 in __main__.example_0\n***Test Failed*** 10 failures.\nFor whitespace errors, see the file /Users/was/build/sage-3.0.3.alpha2/tmp/.doctest_testdoc.py\n         [12.2 s]\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3414\n\n",
    "created_at": "2008-06-13T14:25:18Z",
    "labels": [
        "dsage",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "sage-3.0.3.alpha2 -- massive dsage \"testdoc.py\" failures on osx ppc",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3414",
    "user": "was"
}
```
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


Issue created by migration from https://trac.sagemath.org/ticket/3414





---

archive/issue_comments_023942.json:
```json
{
    "body": "The network on this machine is foobar'd.",
    "created_at": "2008-06-13T22:33:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3414",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3414#issuecomment-23942",
    "user": "was"
}
```

The network on this machine is foobar'd.



---

archive/issue_comments_023943.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2008-06-13T22:33:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3414",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3414#issuecomment-23943",
    "user": "was"
}
```

Resolution: invalid
