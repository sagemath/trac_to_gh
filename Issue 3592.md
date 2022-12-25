# Issue 3592: [with spkg, positive review] update sympy to the 0.6.0 release

archive/issues_003592.json:
```json
{
    "body": "Assignee: ondrej\n\n1) Put there the attached sympy-0.6.0.spkg. \n\n2) Then apply the attached patch to Sage and rebuild Sage with \"sage -b\"\n\n3) make sure the test_sympy.py test works, this should be the outcome:\n\n\n```\n$ ./sage -t devel/sage/sage/calculus/test_sympy.py\nsage -t  3.0.3-debian-opteron64-x86_64-Linux/devel/sage/sage/calculus/test_sympy.py\n [5.2 s]\n \n----------------------------------------------------------------------\nAll tests passed!\nTotal time for all tests: 5.2 seconds\n```\n\n4) make sure all tests work. The result of:\n\n$ ./sage -tp 6 devel/sage/sage &> test.log\n\nis attached.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3592\n\n",
    "closed_at": "2008-07-16T02:46:29Z",
    "created_at": "2008-07-07T22:06:16Z",
    "labels": [
        "component: packages: standard",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.6",
    "title": "[with spkg, positive review] update sympy to the 0.6.0 release",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3592",
    "user": "https://github.com/certik"
}
```
Assignee: ondrej

1) Put there the attached sympy-0.6.0.spkg. 

2) Then apply the attached patch to Sage and rebuild Sage with "sage -b"

3) make sure the test_sympy.py test works, this should be the outcome:


```
$ ./sage -t devel/sage/sage/calculus/test_sympy.py
sage -t  3.0.3-debian-opteron64-x86_64-Linux/devel/sage/sage/calculus/test_sympy.py
 [5.2 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 5.2 seconds
```

4) make sure all tests work. The result of:

$ ./sage -tp 6 devel/sage/sage &> test.log

is attached.

Issue created by migration from https://trac.sagemath.org/ticket/3592





---

archive/issue_comments_025329.json:
```json
{
    "body": "Attachment [sage.patch](tarball://root/attachments/some-uuid/ticket3592/sage.patch) by mabshoff created at 2008-07-07 22:17:06\n\nThe category of this ticket is packages and please also assign a milestone per default.\n\nCheers,\n\nMichael",
    "created_at": "2008-07-07T22:17:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3592",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3592#issuecomment-25329",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [sage.patch](tarball://root/attachments/some-uuid/ticket3592/sage.patch) by mabshoff created at 2008-07-07 22:17:06

The category of this ticket is packages and please also assign a milestone per default.

Cheers,

Michael



---

archive/issue_events_008227.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-07-07T22:17:06Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3592",
    "milestone": "sage-3.0.5",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3592#event-8227"
}
```



---

archive/issue_comments_025330.json:
```json
{
    "body": "Changing assignee from @garyfurnish to ondrej.",
    "created_at": "2008-07-07T22:17:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3592",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3592#issuecomment-25330",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing assignee from @garyfurnish to ondrej.



---

archive/issue_comments_025331.json:
```json
{
    "body": "Changing component from calculus to packages.",
    "created_at": "2008-07-07T22:17:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3592",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3592#issuecomment-25331",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing component from calculus to packages.



---

archive/issue_comments_025332.json:
```json
{
    "body": "And do *not* attach spkgs, link them.\n\nCheers,\n\nMichael",
    "created_at": "2008-07-07T22:17:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3592",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3592#issuecomment-25332",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

And do *not* attach spkgs, link them.

Cheers,

Michael



---

archive/issue_comments_025333.json:
```json
{
    "body": "Test log:\n\nhttp://sage.math.washington.edu/home/ondrej/ext/sage/test.log\n\nas you can see, there is one test failing, but I think it is not related. Should I check if all tests run without the patch for me?\n\nHere is the link to the spkg:\n\nhttp://sage.math.washington.edu/home/ondrej/ext/sage/ondrej/sympy-0.6.0.spkg",
    "created_at": "2008-07-07T22:33:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3592",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3592#issuecomment-25333",
    "user": "https://github.com/certik"
}
```

Test log:

http://sage.math.washington.edu/home/ondrej/ext/sage/test.log

as you can see, there is one test failing, but I think it is not related. Should I check if all tests run without the patch for me?

Here is the link to the spkg:

http://sage.math.washington.edu/home/ondrej/ext/sage/ondrej/sympy-0.6.0.spkg



---

archive/issue_comments_025334.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2008-07-08T00:08:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3592",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3592#issuecomment-25334",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_025335.json:
```json
{
    "body": "I am making this a blocker since it fixes one more important import time patch that is worth >0.1 seconds.\n\nCheers,\n\nMichael",
    "created_at": "2008-07-08T00:08:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3592",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3592#issuecomment-25335",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

I am making this a blocker since it fixes one more important import time patch that is worth >0.1 seconds.

Cheers,

Michael



---

archive/issue_comments_025336.json:
```json
{
    "body": "The test failure seems to be another rpy is moved and hence broken failure. This ought to be put on its own ticket and fixed.\n\nCheers,\n\nMichael",
    "created_at": "2008-07-08T00:09:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3592",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3592#issuecomment-25336",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The test failure seems to be another rpy is moved and hence broken failure. This ought to be put on its own ticket and fixed.

Cheers,

Michael



---

archive/issue_comments_025337.json:
```json
{
    "body": "Positive review. The attached patch is a diff and not a proper mercurial patch.\n\nCheers,\n\nMichael",
    "created_at": "2008-07-16T02:12:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3592",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3592#issuecomment-25337",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Positive review. The attached patch is a diff and not a proper mercurial patch.

Cheers,

Michael



---

archive/issue_events_008228.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-07-16T02:46:29Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3592",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3592#event-8228"
}
```



---

archive/issue_comments_025338.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-07-16T02:46:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3592",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3592#issuecomment-25338",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_025339.json:
```json
{
    "body": "Merged in Sage 3.0.6.alpha0. I committed the patch in Ondrej's name.\n\nCheers,\n\nMichael",
    "created_at": "2008-07-16T02:46:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3592",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3592#issuecomment-25339",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.6.alpha0. I committed the patch in Ondrej's name.

Cheers,

Michael
