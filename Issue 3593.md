# Issue 3593: dsage-interfaces -- error decompressing data

archive/issues_003593.json:
```json
{
    "body": "Assignee: yi\n\nI got this when running the test on a heavily loaded system.   It's probably an issue with reading a file that hasn't been completely written yet.  !\n\n```\nsage -t  devel/sage/sage/dsage/database/sql_functions.py (skipping) -- nodoctest.py file in directory\nsage -t  devel/sage/sage/dsage/interface/sage_interface.py **********************************************************************\nFile \"/home/was/build/sage-3.0.4.alpha2/tmp/dsage_interface.py\", line 466:\n    sage: j = d.block_on_jobs(d.map(f, [25,12,25,32,12]))\nException raised:\n    Traceback (most recent call last):\n      File \"/home/was/build/sage-3.0.4.alpha2/local/lib/python2.5/doctest.py\", line 1228, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_13[10]>\", line 1, in <module>\n        j = d.block_on_jobs(d.map(f, [Integer(25),Integer(12),Integer(25),Integer(32),Integer(12)]))###line 466:\n    sage: j = d.block_on_jobs(d.map(f, [25,12,25,32,12]))\n      File \"/home/was/build/sage-3.0.4.alpha2/local/lib/python2.5/site-packages/sage/dsage/interface/dsage_interface.py\", line 476, in block_on_jobs\n        j.get_job()\n      File \"/home/was/build/sage-3.0.4.alpha2/local/lib/python2.5/site-packages/sage/dsage/interface/dsage_interface.py\", line 1009, in get_job\n        self._update_job(jdict)\n      File \"/home/was/build/sage-3.0.4.alpha2/local/lib/python2.5/site-packages/sage/dsage/interface/dsage_interface.py\", line 820, in _update_job\n        job = expand_job(jdict)\n      File \"/home/was/build/sage-3.0.4.alpha2/local/lib/python2.5/site-packages/sage/dsage/database/job.py\", line 177, in expand_job\n        jdict['result'] = zlib.decompress(jdict['result'])\n    error: Error -5 while decompressing data\n**********************************************************************\nFile \"/home/was/build/sage-3.0.4.alpha2/tmp/dsage_interface.py\", line 467:\n    sage: print \"ignore this\";  j # random\nException raised:\n    Traceback (most recent call last):\n      File \"/home/was/build/sage-3.0.4.alpha2/local/lib/python2.5/doctest.py\", line 1228, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_13[11]>\", line 1, in <module>\n        print \"ignore this\";  j # random###line 467:\n    sage: print \"ignore this\";  j # random\n    NameError: name 'j' is not defined\n**********************************************************************\n1 items had failures:\n   2 of  12 in __main__.example_13\n***Test Failed*** 2 failures.\n[DSage] Closed connection to localhost\n[DSage] Closed connection to localhost\n[DSage] Closed connection to localhost\n[DSage] Closed connection to localhost\nFor whitespace errors, see the file /home/was/build/sage-3.0.4.alpha2/tmp/.doctest_dsage_interface.pyUnhandled exception in thread started by <bound method Thread.__bootstrap of <Thread(PoolThread-twisted.internet.reactor-1, stopped)>>\nTraceback (most recent call last):\n  File \"/home/was/build/sage-3.0.4.alpha\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3593\n\n",
    "created_at": "2008-07-07T22:13:28Z",
    "labels": [
        "dsage",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.4",
    "title": "dsage-interfaces -- error decompressing data",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3593",
    "user": "was"
}
```
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


Issue created by migration from https://trac.sagemath.org/ticket/3593





---

archive/issue_comments_025390.json:
```json
{
    "body": "This bug is also in sage-3.0.4.rc0 on arch linux.",
    "created_at": "2008-07-08T06:21:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3593",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3593#issuecomment-25390",
    "user": "was"
}
```

This bug is also in sage-3.0.4.rc0 on arch linux.



---

archive/issue_comments_025391.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2008-07-08T06:22:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3593",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3593#issuecomment-25391",
    "user": "was"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_025392.json:
```json
{
    "body": "Additional problems:\n\nOn sage.math we have\n\n```\nsage -t  devel/sage/sage/dsage/interface/dsage_interface.py **********************************************************************\nFile \"/home/was/build/sage-3.0.4.rc0/tmp/dsage_interface.py\", line 461:\n    sage: d.is_connected()\nExpected:\n    True\nGot:\n    False\n**********************************************************************\nFile \"/home/was/build/sage-3.0.4.rc0/tmp/dsage_interface.py\", line 466:\n    sage: j = d.block_on_jobs(d.map(f, [25,12,25,32,12]))\nException raised:\n    Traceback (most recent call last):\n      File \"/home/was/build/sage-3.0.4.rc0/local/lib/python2.5/doctest.py\", line 1228, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_13[10]>\", line 1, in <module>\n        j = d.block_on_jobs(d.map(f, [Integer(25),Integer(12),Integer(25),Integer(32),Integer(12)]))###line 466:\n    sage: j = d.block_on_jobs(d.map(f, [25,12,25,32,12]))\n      File \"/home/was/build/sage-3.0.4.rc0/local/lib/python2.5/site-packages/sage/dsage/interface/dsage_interface.py\", line 518, in map\n        for a in izip(*args)]\n      File \"/home/was/build/sage-3.0.4.rc0/local/lib/python2.5/site-packages/sage/dsage/interface/dsage_interface.py\", line 609, in eval_function\n        wrapped_job = BlockingJobWrapper(self._remoteobj, job)\n      File \"/home/was/build/sage-3.0.4.rc0/local/lib/python2.5/site-packages/sage/dsage/interface/dsage_interface.py\", line 982, in __init__\n        self.job_id = blockingCallFromThread(reactor, self._remoteobj.callRemote,\n    AttributeError: 'NoneType' object has no attribute 'callRemote'\n**********************************************************************\nFile \"/home/was/build/sage-3.0.4.rc0/tmp/dsage_interface.py\", line 467:\n    sage: print \"ignore this\";  j # random\nException raised:\n    Traceback (most recent call last):\n      File \"/home/was/build/sage-3.0.4.rc0/local/lib/python2.5/doctest.py\", line 1228, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_13[11]>\", line 1, in <module>\n        print \"ignore this\";  j # random###line 467:\n    sage: print \"ignore this\";  j # random\n    NameError: name 'j' is not defined\n**********************************************************************\nFile \"/home/was/build/sage-3.0.4.rc0/tmp/dsage_interface.py\", line 501:\n    sage: d.is_connected()\nExpected:\n    True\nGot:\n    False\n**********************************************************************\nFile \"/home/was/build/sage-3.0.4.rc0/tmp/dsage_interface.py\", line 506:\n    sage: j = d.map(f, [25,12,25,32,12])\nException raised:\n    Traceback (most recent call last):\n      File \"/home/was/build/sage-3.0.4.rc0/local/lib/python2.5/doctest.py\", line 1228, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_14[10]>\", line 1, in <module>\n        j = d.map(f, [Integer(25),Integer(12),Integer(25),Integer(32),Integer(12)])###line 506:\n    sage: j = d.map(f, [25,12,25,32,12])\n      File \"/home/was/build/sage-3.0.4.rc0/local/lib/python2.5/site-packages/sage/dsage/interface/dsage_interface.py\", line 518, in map\n        for a in izip(*args)]\n      File \"/home/was/build/sage-3.0.4.rc0/local/lib/python2.5/site-packages/sage/dsage/interface/dsage_interface.py\", line 609, in eval_function\n        wrapped_job = BlockingJobWrapper(self._remoteobj, job)\n      File \"/home/was/build/sage-3.0.4.rc0/local/lib/python2.5/site-packages/sage/dsage/interface/dsage_interface.py\", line 982, in __init__\n        self.job_id = blockingCallFromThread(reactor, self._remoteobj.callRemote,\n    AttributeError: 'NoneType' object has no attribute 'callRemote'\n**********************************************************************\n                                                                                                                                                       1329,42       55%\netc.\n```\n",
    "created_at": "2008-07-08T06:22:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3593",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3593#issuecomment-25392",
    "user": "was"
}
```

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

archive/issue_comments_025393.json:
```json
{
    "body": "Attachment [sage-3593.patch](tarball://root/attachments/some-uuid/ticket3593/sage-3593.patch) by was created at 2008-07-08 06:31:39",
    "created_at": "2008-07-08T06:31:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3593",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3593#issuecomment-25393",
    "user": "was"
}
```

Attachment [sage-3593.patch](tarball://root/attachments/some-uuid/ticket3593/sage-3593.patch) by was created at 2008-07-08 06:31:39



---

archive/issue_comments_025394.json:
```json
{
    "body": "I was able to reproduce the problem on sage.math by running 4 doctests simultaneously. The problem is that we weren't using temporary directories for the separate dsage servers so twistd never launched the other servers.  Attached is a patch that fixes this issue.",
    "created_at": "2008-07-08T07:52:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3593",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3593#issuecomment-25394",
    "user": "yi"
}
```

I was able to reproduce the problem on sage.math by running 4 doctests simultaneously. The problem is that we weren't using temporary directories for the separate dsage servers so twistd never launched the other servers.  Attached is a patch that fixes this issue.



---

archive/issue_comments_025395.json:
```json
{
    "body": "Attachment [tmpdir.patch](tarball://root/attachments/some-uuid/ticket3593/tmpdir.patch) by yi created at 2008-07-08 07:52:37",
    "created_at": "2008-07-08T07:52:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3593",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3593#issuecomment-25395",
    "user": "yi"
}
```

Attachment [tmpdir.patch](tarball://root/attachments/some-uuid/ticket3593/tmpdir.patch) by yi created at 2008-07-08 07:52:37



---

archive/issue_comments_025396.json:
```json
{
    "body": "Attachment [find_ports.patch](tarball://root/attachments/some-uuid/ticket3593/find_ports.patch) by yi created at 2008-07-08 17:19:38\n\nThis will bind to port 0 and the OS will return a valid port to listen on",
    "created_at": "2008-07-08T17:19:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3593",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3593#issuecomment-25396",
    "user": "yi"
}
```

Attachment [find_ports.patch](tarball://root/attachments/some-uuid/ticket3593/find_ports.patch) by yi created at 2008-07-08 17:19:38

This will bind to port 0 and the OS will return a valid port to listen on



---

archive/issue_comments_025397.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-07-09T16:20:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3593",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3593#issuecomment-25397",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_025398.json:
```json
{
    "body": "Merged in Sage 3.0.4.rc1",
    "created_at": "2008-07-09T16:20:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3593",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3593#issuecomment-25398",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.4.rc1



---

archive/issue_comments_025399.json:
```json
{
    "body": "Did you merge in William's patch to disable doctesting or my patches to fix doctesting?",
    "created_at": "2008-07-09T16:30:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3593",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3593#issuecomment-25399",
    "user": "yi"
}
```

Did you merge in William's patch to disable doctesting or my patches to fix doctesting?



---

archive/issue_comments_025400.json:
```json
{
    "body": "Replying to [comment:9 yi]:\n> Did you merge in William's patch to disable doctesting or my patches to fix doctesting?\n\nI have not looked in detail, but I believe the patch to disable the doctest was merged for now. Please check rc2 and in case I am right open a new ticket with your patches and a reversal patch for what William did. Sorry for the confusion, William mentioned this ticket ought to be closed, so I did it without checking the details.\n\nCheers,\n\nMichael",
    "created_at": "2008-07-09T16:34:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3593",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3593#issuecomment-25400",
    "user": "mabshoff"
}
```

Replying to [comment:9 yi]:
> Did you merge in William's patch to disable doctesting or my patches to fix doctesting?

I have not looked in detail, but I believe the patch to disable the doctest was merged for now. Please check rc2 and in case I am right open a new ticket with your patches and a reversal patch for what William did. Sorry for the confusion, William mentioned this ticket ought to be closed, so I did it without checking the details.

Cheers,

Michael
