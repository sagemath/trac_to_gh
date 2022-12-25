# Issue 7108: Sage 4.1.2.rc0 doctest failures on 32-bit Fedora 9

archive/issues_007108.json:
```json
{
    "body": "Assignee: tbd\n\nAs the subject says. This was reported to [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/c8b23afa63990d0f).\n\nIssue created by migration from https://trac.sagemath.org/ticket/7108\n\n",
    "created_at": "2009-10-04T06:17:06Z",
    "labels": [
        "component: doctest coverage",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Sage 4.1.2.rc0 doctest failures on 32-bit Fedora 9",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7108",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```
Assignee: tbd

As the subject says. This was reported to [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/c8b23afa63990d0f).

Issue created by migration from https://trac.sagemath.org/ticket/7108





---

archive/issue_comments_058738.json:
```json
{
    "body": "I just tried a clean build of sage-4.1.2.rc0 + a bit and get *only* one failure in twist.py:\n\n\n```\n----------------------------------------------------------------------\nThe following tests failed:\n\n\n        sage -t -long \"devel/sage/sage/server/simple/twist.py\"\n```\n\n\nThe failure is:\n\n```\nsage -t -long \"devel/sage/sage/server/simple/twist.py\"      \n**********************************************************************\nFile \"/home/wstein/screen/cicero/build/sage-4.1.2.rc1.alpha1/devel/sage/sage/server/simple/twist.py\", line 51:\n    sage: print get_url('http://localhost:%s/simple/compute?session=%s&code=2*2' % (port, session))\nExpected:\n    {\n    \"status\": \"done\",\n    \"files\": [],\n    \"cell_id\": 1\n    }\n    ___S_A_G_E___\n    4\nGot:\n    {\n    \"status\": \"computing\",\n    \"files\": [],\n    \"cell_id\": 1\n    }\n    ___S_A_G_E___\n    <BLANKLINE>\n**********************************************************************\n1 items had failures:\n   1 of  24 in __main__.example_0\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file /home/wstein/.sage//tmp/.doctest_twist.py\n         [17.8 s]\n```\n\n\nThis is somwhat expected since cicero is slow and the difference between the above two is that one didn't finish and the other did.  Hmm.",
    "created_at": "2009-10-04T17:24:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7108",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7108#issuecomment-58738",
    "user": "https://github.com/williamstein"
}
```

I just tried a clean build of sage-4.1.2.rc0 + a bit and get *only* one failure in twist.py:


```
----------------------------------------------------------------------
The following tests failed:


        sage -t -long "devel/sage/sage/server/simple/twist.py"
```


The failure is:

```
sage -t -long "devel/sage/sage/server/simple/twist.py"      
**********************************************************************
File "/home/wstein/screen/cicero/build/sage-4.1.2.rc1.alpha1/devel/sage/sage/server/simple/twist.py", line 51:
    sage: print get_url('http://localhost:%s/simple/compute?session=%s&code=2*2' % (port, session))
Expected:
    {
    "status": "done",
    "files": [],
    "cell_id": 1
    }
    ___S_A_G_E___
    4
Got:
    {
    "status": "computing",
    "files": [],
    "cell_id": 1
    }
    ___S_A_G_E___
    <BLANKLINE>
**********************************************************************
1 items had failures:
   1 of  24 in __main__.example_0
***Test Failed*** 1 failures.
For whitespace errors, see the file /home/wstein/.sage//tmp/.doctest_twist.py
         [17.8 s]
```


This is somwhat expected since cicero is slow and the difference between the above two is that one didn't finish and the other did.  Hmm.



---

archive/issue_comments_058739.json:
```json
{
    "body": "I also see exactly the same twist.py failure on opensuse 64-bit.  I think this is likely just a poorly written doctest. \n\nYes, in fact, looking at the doctest it is:\n\n```\nRun a command::\n\n    sage: sleep(0.5)\n    sage: print get_url('http://localhost:%s/simple/compute?session=%s&code=2*2' % (port, session))\n    {\n    \"status\": \"done\",\n    \"files\": [],\n    \"cell_id\": 1\n    }\n    ___S_A_G_E___\n    4\n```\n\n\nTo be frank, it is utterly ridiculous to think that a doctest like this is going to work all the time.  Often computers get heavily loaded during testing, or are slow because of DNS configuration, virtualization, etc.   The above test needs to be rewritten.  Two options:\n    \n* try repeatedly until status is done.\n\n* put some ...'s in the output.",
    "created_at": "2009-10-04T17:47:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7108",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7108#issuecomment-58739",
    "user": "https://github.com/williamstein"
}
```

I also see exactly the same twist.py failure on opensuse 64-bit.  I think this is likely just a poorly written doctest. 

Yes, in fact, looking at the doctest it is:

```
Run a command::

    sage: sleep(0.5)
    sage: print get_url('http://localhost:%s/simple/compute?session=%s&code=2*2' % (port, session))
    {
    "status": "done",
    "files": [],
    "cell_id": 1
    }
    ___S_A_G_E___
    4
```


To be frank, it is utterly ridiculous to think that a doctest like this is going to work all the time.  Often computers get heavily loaded during testing, or are slow because of DNS configuration, virtualization, etc.   The above test needs to be rewritten.  Two options:
    
* try repeatedly until status is done.

* put some ...'s in the output.



---

archive/issue_comments_058740.json:
```json
{
    "body": "I had figured that 2*2 would be nearly instantaneous to compute, even on a heavily loaded machine, but here we're also waiting for the sage session to start up. \n\nWe should add a \"timeout=-1\" to that url so it waits for the computation to finish no matter what (and then can delete the \"sleep(0.5).\"",
    "created_at": "2009-10-05T16:46:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7108",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7108#issuecomment-58740",
    "user": "https://github.com/robertwb"
}
```

I had figured that 2*2 would be nearly instantaneous to compute, even on a heavily loaded machine, but here we're also waiting for the sage session to start up. 

We should add a "timeout=-1" to that url so it waits for the computation to finish no matter what (and then can delete the "sleep(0.5)."



---

archive/issue_events_016806.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2009-10-07T12:47:15Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7108",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7108#event-16806"
}
```



---

archive/issue_comments_058741.json:
```json
{
    "body": "The same testing issue comes up with OS X 10.5 and is fixed there in #7112.  I'm thus closing this as a dupe.",
    "created_at": "2009-10-07T12:47:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7108",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7108#issuecomment-58741",
    "user": "https://github.com/williamstein"
}
```

The same testing issue comes up with OS X 10.5 and is fixed there in #7112.  I'm thus closing this as a dupe.



---

archive/issue_comments_058742.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2009-10-07T12:47:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7108",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7108#issuecomment-58742",
    "user": "https://github.com/williamstein"
}
```

Resolution: duplicate



---

archive/issue_events_016807.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2009-10-14T17:12:11Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7108",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7108#event-16807"
}
```
