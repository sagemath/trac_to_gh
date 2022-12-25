# Issue 2983: Itanium (RHEL 5) -- singular interface problems in matrix_group.py

archive/issues_002983.json:
```json
{
    "body": "Assignee: mabshoff\n\nThis may get resolved by fixing #2209.\n\n\n```\nsage -t  devel/sage/sage/groups/matrix_gps/matrix_group.py  **********************************************************************\nFile \"/home/wstein/sage-3.0.rc0/tmp/matrix_group.py\", line 689:\n    sage: G.invariant_generators()\nException raised:\n    Traceback (most recent call last):\n      File \"/home/wstein/sage-3.0.rc0/local/lib/python2.5/doctest.py\", line 1228, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_26[4]>\", line 1, in <module>\n        G.invariant_generators()###line 689:\n    sage: G.invariant_generators()\n      File \"/home/wstein/sage-3.0.rc0/local/lib/python2.5/site-packages/sage/groups/matrix_gps/matrix_group.py\", line 762, in invariant_generators\n        singular.eval('matrix %s = invariant_algebra_reynolds(%s[1])'%(IRName,ReyName))\n      File \"/home/wstein/sage-3.0.rc0/local/lib/python2.5/site-packages/sage/interfaces/singular.py\", line 416, in eval\n        s = Expect.eval(self, x)\n      File \"/home/wstein/sage-3.0.rc0/local/lib/python2.5/site-packages/sage/interfaces/expect.py\", line 722, in eval\n        return '\\n'.join([self._eval_line(L, **kwds) for L in code.split('\\n') if L != ''])\n      File \"/home/wstein/sage-3.0.rc0/local/lib/python2.5/site-packages/sage/interfaces/expect.py\", line 643, in _eval_line\n        raise RuntimeError, \"%s\\n%s crashed executing %s\"%(msg,self, line)\n    RuntimeError: End Of File (EOF) in read_nonblocking(). Exception style platform.\n    <pexpect.spawn instance at 0x6000000003666998>\n    version: 2.0 ($Revision: 1.151 $)\n    command: /home/wstein/sage-3.0.rc0/local/bin/Singular\n    args: ['/home/wstein/sage-3.0.rc0/local/bin/Singular', '-t', '--ticks-per-sec', '1000']\n    patterns:\n        >\n    buffer (last 100 chars):\n    before (last 100 chars): me/wstein/sage-3.0.rc0/local/bin/Singular: line 2: 30877 Segmentation fault      Singular-3-0-4 $*^M\n\n    after: <class 'pexpect.EOF'>\n    match: None\n    match_index: None\n    exitstatus: 139\n    flag_eof: 1\n    pid: 30874\n    child_fd: 5\n    timeout: None\n    delimiter: <class 'pexpect.EOF'>\n    logfile: None\n    maxread: 1000\n    searchwindowsize: None\n    delaybeforesend: 0\n    Singular crashed executing matrix tsage4 = invariant_algebra_reynolds(tsage3[1]);\n\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2983\n\n",
    "created_at": "2008-04-21T03:25:38Z",
    "labels": [
        "component: porting",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.2",
    "title": "Itanium (RHEL 5) -- singular interface problems in matrix_group.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2983",
    "user": "https://github.com/williamstein"
}
```
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


Issue created by migration from https://trac.sagemath.org/ticket/2983





---

archive/issue_comments_020492.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-04-21T04:36:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2983",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2983#issuecomment-20492",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_020493.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2008-04-21T04:36:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2983",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2983#issuecomment-20493",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_020494.json:
```json
{
    "body": "This is definitely a problem with Singular segfaulting and not related to GAP AFAIK.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-21T04:36:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2983",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2983#issuecomment-20494",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This is definitely a problem with Singular segfaulting and not related to GAP AFAIK.

Cheers,

Michael



---

archive/issue_comments_020495.json:
```json
{
    "body": "My two cents:\n(1) I don't see how this can be related to 2209, since it is a Singular crash not a GAP crash. AFAIK, the code for invariant_generators does not call GAP:\nhttp://www.sagemath.org/hg/sage-main/file/cc1e12a492fc/sage/groups/matrix_gps/matrix_group.py\n(2) It passes for me on ubuntu 7.10 amd64:\n\n\n```\nwdj@wooster:~/wdj/sagefiles/sage-3.0.rc0$ ./sage -t devel/sage/sage/groups/matrix_gps/matrix_group.py\nsage -t  0/devel/sage/sage/groups/matrix_gps/matrix_group.py\n         [42.7 s]\n\n----------------------------------------------------------------------\nAll tests passed!\nTotal time for all tests: 42.7 seconds\n```\n",
    "created_at": "2008-04-21T10:33:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2983",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2983#issuecomment-20495",
    "user": "https://github.com/wdjoyner"
}
```

My two cents:
(1) I don't see how this can be related to 2209, since it is a Singular crash not a GAP crash. AFAIK, the code for invariant_generators does not call GAP:
http://www.sagemath.org/hg/sage-main/file/cc1e12a492fc/sage/groups/matrix_gps/matrix_group.py
(2) It passes for me on ubuntu 7.10 amd64:


```
wdj@wooster:~/wdj/sagefiles/sage-3.0.rc0$ ./sage -t devel/sage/sage/groups/matrix_gps/matrix_group.py
sage -t  0/devel/sage/sage/groups/matrix_gps/matrix_group.py
         [42.7 s]

----------------------------------------------------------------------
All tests passed!
Total time for all tests: 42.7 seconds
```




---

archive/issue_comments_020496.json:
```json
{
    "body": "Yes, as other people have overserved this is a Singular issue unrelated to GAP. I will hopefully track this down for 3.0.1.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-23T11:48:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2983",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2983#issuecomment-20496",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Yes, as other people have overserved this is a Singular issue unrelated to GAP. I will hopefully track this down for 3.0.1.

Cheers,

Michael



---

archive/issue_comments_020497.json:
```json
{
    "body": "Ahh, this is a gcc 4.1.2 specific issue - it does not segfault with a build from source gcc 4.3 on the same platform.\n\nCheers,\n\nMichael",
    "created_at": "2008-05-02T05:17:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2983",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2983#issuecomment-20497",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Ahh, this is a gcc 4.1.2 specific issue - it does not segfault with a build from source gcc 4.3 on the same platform.

Cheers,

Michael



---

archive/issue_comments_020498.json:
```json
{
    "body": "Compiling with `-O2` fixes the issue. Patch coming up in a couple hours.\n\nCheers,\n\nMichael",
    "created_at": "2008-05-05T17:19:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2983",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2983#issuecomment-20498",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Compiling with `-O2` fixes the issue. Patch coming up in a couple hours.

Cheers,

Michael



---

archive/issue_comments_020499.json:
```json
{
    "body": "Attachment [trac_2983.patch](tarball://root/attachments/some-uuid/ticket2983/trac_2983.patch) by mabshoff created at 2008-05-11 12:47:35\n\nThe spkg at \n\nhttp://sage.math.washington.edu/home/mabshoff/release-cycles-3.0.2/alpha0/singular-3-0-4-2-20080405.p2.spkg\n\nfixes this and also #3158.\n\nCheers,\n\nMichael",
    "created_at": "2008-05-11T12:47:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2983",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2983#issuecomment-20499",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [trac_2983.patch](tarball://root/attachments/some-uuid/ticket2983/trac_2983.patch) by mabshoff created at 2008-05-11 12:47:35

The spkg at 

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.0.2/alpha0/singular-3-0-4-2-20080405.p2.spkg

fixes this and also #3158.

Cheers,

Michael



---

archive/issue_comments_020500.json:
```json
{
    "body": "Builds for me on mac 10.5, can do \n\n\n```\nsage: R=QQ['x,y,z']\nsage: R(x^5)\nx^5\nsage: R(x^5)^2\nx^10\n```\n\n\nalso sage -t  devel/sage/sage/groups/matrix_gps/matrix_group.py passes with no errors.",
    "created_at": "2008-05-11T13:07:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2983",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2983#issuecomment-20500",
    "user": "https://trac.sagemath.org/admin/accounts/users/broune"
}
```

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

archive/issue_events_003188.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-05-11T13:10:50Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2983",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2983#event-3188"
}
```



---

archive/issue_comments_020501.json:
```json
{
    "body": "Merged in Sage 3.0.2.alpha0",
    "created_at": "2008-05-11T13:10:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2983",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2983#issuecomment-20501",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.2.alpha0



---

archive/issue_comments_020502.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-05-11T13:10:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2983",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2983#issuecomment-20502",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
