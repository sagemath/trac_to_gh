# Issue 2985: ITANIUM (RHEL 5) -- bug in rubik.py's OptimalSolver()

archive/issues_002985.json:
```json
{
    "body": "Assignee: mabshoff\n\n\n```\n[wstein@cleo sage-3.0.rc0]$ ./sage -t --long devel/sage/sage/interfaces/rubik.py\nsage -t --long devel/sage/sage/interfaces/rubik.py          **********************************************************************\nFile \"/home/wstein/sage-3.0.rc0/tmp/rubik.py\", line 132:\n    sage: solver = OptimalSolver() # long time\nException raised:\n    Traceback (most recent call last):\n      File \"/home/wstein/sage-3.0.rc0/local/lib/python2.5/doctest.py\", line 1228, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_3[3]>\", line 1, in <module>\n        solver = OptimalSolver() # long time###line 132:\n    sage: solver = OptimalSolver() # long time\n      File \"/home/wstein/sage-3.0.rc0/local/lib/python2.5/site-packages/sage/interfaces/rubik.py\", line 98, in __init__\n        self.ready()\n      File \"/home/wstein/sage-3.0.rc0/local/lib/python2.5/site-packages/sage/interfaces/rubik.py\", line 117, in ready\n        self.child.expect('enter cube')\n      File \"/home/wstein/sage-3.0.rc0/local/lib/python2.5/site-packages/pexpect.py\", line 912, in expect\n        return self.expect_list(compiled_pattern_list, timeout, searchwindowsize)\n      File \"/home/wstein/sage-3.0.rc0/local/lib/python2.5/site-packages/pexpect.py\", line 978, in expect_list\n        raise EOF (str(e) + '\\n' + str(self))\n    EOF: End Of File (EOF) in read_nonblocking(). Exception style platform.\n    <pexpect.spawn instance at 0x6000000003270950>\n    version: 2.0 ($Revision: 1.151 $)\n    command: /home/wstein/sage-3.0.rc0/local/bin/optimal\n    args: ['/home/wstein/sage-3.0.rc0/local/bin/optimal']\n    patterns:\n        enter cube\n    buffer (last 100 chars): \n    before (last 100 chars): *********\n    1 items had failures:\n       1 of  10 in __main__.example_3\n    ***Test Failed*** 1 failures.\n\n    after: <class 'pexpect.EOF'>\n    match: None\n    match_index: None\n    exitstatus: None\n    flag_eof: 1\n    pid: 18447\n    child_fd: 3\n    timeout: None\n    delimiter: <class 'pexpect.EOF'>\n    logfile: None\n    maxread: 2000\n    searchwindowsize: None\n    delaybeforesend: 0.1\n**********************************************************************\n1 items had failures:\n   1 of  10 in __main__.example_3\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file /home/wstein/sage-3.0.rc0/tmp/.doctest_rubik.py\n         [49.0 s]\nexit code: 1024\n \n----------------------------------------------------------------------\nThe following tests failed:\n\n\n\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2985\n\n",
    "created_at": "2008-04-21T04:39:21Z",
    "labels": [
        "porting",
        "major",
        "bug"
    ],
    "title": "ITANIUM (RHEL 5) -- bug in rubik.py's OptimalSolver()",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2985",
    "user": "was"
}
```
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


Issue created by migration from https://trac.sagemath.org/ticket/2985





---

archive/issue_comments_020553.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-04-25T04:17:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2985",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2985#issuecomment-20553",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_020554.json:
```json
{
    "body": "The issue also happens on Ubuntu 6.06 LTS on AMD64.\n\nCheers,\n\nMichaek",
    "created_at": "2008-04-25T04:17:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2985",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2985#issuecomment-20554",
    "user": "mabshoff"
}
```

The issue also happens on Ubuntu 6.06 LTS on AMD64.

Cheers,

Michaek



---

archive/issue_comments_020555.json:
```json
{
    "body": "Arrg, somebody [I know who] didn't remove the i686 optimal and twist binaries in the reid solver. We also did build reid without any optimization. The spkg at\n\nhttp://sage.math.washington.edu/home/mabshoff/release-cycles-3.0.1/alpha0/rubiks-20070912.p6.spkg\n\nfixes that.\n\nDoctest pass on x86-64, Itanium and OSX.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-25T06:22:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2985",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2985#issuecomment-20555",
    "user": "mabshoff"
}
```

Arrg, somebody [I know who] didn't remove the i686 optimal and twist binaries in the reid solver. We also did build reid without any optimization. The spkg at

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.0.1/alpha0/rubiks-20070912.p6.spkg

fixes that.

Doctest pass on x86-64, Itanium and OSX.

Cheers,

Michael



---

archive/issue_comments_020556.json:
```json
{
    "body": "works for me",
    "created_at": "2008-04-25T06:25:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2985",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2985#issuecomment-20556",
    "user": "gfurnish"
}
```

works for me



---

archive/issue_comments_020557.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-25T06:34:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2985",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2985#issuecomment-20557",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_020558.json:
```json
{
    "body": "Merged in Sage 3.0.1.alpha0",
    "created_at": "2008-04-25T06:34:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2985",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2985#issuecomment-20558",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.1.alpha0
