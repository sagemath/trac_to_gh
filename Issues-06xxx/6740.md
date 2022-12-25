# Issue 6740: [with spkg, positive review] upgrade mpmath to 0.13

archive/issues_006740.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  @fredrik-johansson\n\nThe latest version of mpmath is now 0.13. Upgrade Sage to use that latest version.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6740\n\n",
    "closed_at": "2009-09-02T09:44:53Z",
    "created_at": "2009-08-13T19:24:19Z",
    "labels": [
        "component: packages: standard"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.2",
    "title": "[with spkg, positive review] upgrade mpmath to 0.13",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6740",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```
Assignee: mabshoff

CC:  @fredrik-johansson

The latest version of mpmath is now 0.13. Upgrade Sage to use that latest version.

Issue created by migration from https://trac.sagemath.org/ticket/6740





---

archive/issue_comments_055123.json:
```json
{
    "body": "Attachment [mpmath-0.13.spkg](tarball://root/attachments/some-uuid/ticket6740/mpmath-0.13.spkg) by @fredrik-johansson created at 2009-08-14 00:35:36",
    "created_at": "2009-08-14T00:35:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6740",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6740#issuecomment-55123",
    "user": "https://github.com/fredrik-johansson"
}
```

Attachment [mpmath-0.13.spkg](tarball://root/attachments/some-uuid/ticket6740/mpmath-0.13.spkg) by @fredrik-johansson created at 2009-08-14 00:35:36



---

archive/issue_comments_055124.json:
```json
{
    "body": "I took the 0.12 spkg and updated the files in it. Let's see if this works!",
    "created_at": "2009-08-14T00:36:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6740",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6740#issuecomment-55124",
    "user": "https://github.com/fredrik-johansson"
}
```

I took the 0.12 spkg and updated the files in it. Let's see if this works!



---

archive/issue_comments_055125.json:
```json
{
    "body": "I just removed a temporary file from the spkg and checked in Fredrik's update to SPKG.txt into the hg repo.  Other than that, looks good.\n\nUse the spkg at http://sage.math.washington.edu/home/mhansen/mpmath-0.13.spkg",
    "created_at": "2009-09-01T23:11:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6740",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6740#issuecomment-55125",
    "user": "https://github.com/mwhansen"
}
```

I just removed a temporary file from the spkg and checked in Fredrik's update to SPKG.txt into the hg repo.  Other than that, looks good.

Use the spkg at http://sage.math.washington.edu/home/mhansen/mpmath-0.13.spkg



---

archive/issue_comments_055126.json:
```json
{
    "body": "Merged `mpmath-0.13.spkg` in the standard packages repository. Running the test suite results in the following failures:\n\n```\nsage -t -long devel/sage-main/sage/server/simple/twist.py\n**********************************************************************\nFile \"/scratch/mvngu/release/sage-4.1.1/devel/sage-main/sage/server/simple/twist.py\", line 51:\n    sage: print get_url('http://localhost:%s/simple/compute?session=%s&code=2*2' % (port, session))\nExpected:\n    {\n    \"status\": \"done\",\n    \"files\": [],\n    \"cell_id\": 1\n    }\n    ___S_A_G_E___\n    4\nGot:\n    {\n    \"status\": \"computing\",\n    \"files\": [],\n    \"cell_id\": 1\n    }\n    ___S_A_G_E___\n    <BLANKLINE>\n**********************************************************************\nFile \"/scratch/mvngu/release/sage-4.1.1/devel/sage-main/sage/server/simple/twist.py\", line 95:\n    sage: print get_url('http://localhost:%s/simple/compute?session=%s&code=%s' % (port, session, urllib.quote(code)))\nExpected:\n    {\n    \"status\": \"done\",\n    \"files\": [\"a.txt\"],\n    \"cell_id\": 3\n    }\n    ___S_A_G_E___\nGot:\n    {\n    \"status\": \"done\",\n    \"files\": [],\n    \"cell_id\": 3\n    }\n    ___S_A_G_E___\n    <BLANKLINE>\n    Traceback (most recent call last):    h = open('a.txt', 'w'); h.write('test'); h.close()\n    NameError: name 'os' is not defined\n    THERE WAS AN ERROR LOADING THE SAGE LIBRARIES.  Try starting Sage from the command line to see what the error is.\n**********************************************************************\nFile \"/scratch/mvngu/release/sage-4.1.1/devel/sage-main/sage/server/simple/twist.py\", line 103:\n    sage: print get_url('http://localhost:%s/simple/file?session=%s&cell=3&file=a.txt' % (port, session))\nExpected:\n    test\nGot:\n    No such file a.txt in cell 3.\n**********************************************************************\n1 items had failures:\n   3 of  24 in __main__.example_0\n***Test Failed*** 3 failures.\nFor whitespace errors, see the file /scratch/mvngu/release/sage-4.1.1/tmp/.doctest_twist.py\n\t [23.3 s]\n```\nThese have nothing to do to with the updated mpmath spkg. They are known failures and have been reported in Sage 4.1.1.",
    "created_at": "2009-09-02T09:44:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6740",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6740#issuecomment-55126",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Merged `mpmath-0.13.spkg` in the standard packages repository. Running the test suite results in the following failures:

```
sage -t -long devel/sage-main/sage/server/simple/twist.py
**********************************************************************
File "/scratch/mvngu/release/sage-4.1.1/devel/sage-main/sage/server/simple/twist.py", line 51:
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
File "/scratch/mvngu/release/sage-4.1.1/devel/sage-main/sage/server/simple/twist.py", line 95:
    sage: print get_url('http://localhost:%s/simple/compute?session=%s&code=%s' % (port, session, urllib.quote(code)))
Expected:
    {
    "status": "done",
    "files": ["a.txt"],
    "cell_id": 3
    }
    ___S_A_G_E___
Got:
    {
    "status": "done",
    "files": [],
    "cell_id": 3
    }
    ___S_A_G_E___
    <BLANKLINE>
    Traceback (most recent call last):    h = open('a.txt', 'w'); h.write('test'); h.close()
    NameError: name 'os' is not defined
    THERE WAS AN ERROR LOADING THE SAGE LIBRARIES.  Try starting Sage from the command line to see what the error is.
**********************************************************************
File "/scratch/mvngu/release/sage-4.1.1/devel/sage-main/sage/server/simple/twist.py", line 103:
    sage: print get_url('http://localhost:%s/simple/file?session=%s&cell=3&file=a.txt' % (port, session))
Expected:
    test
Got:
    No such file a.txt in cell 3.
**********************************************************************
1 items had failures:
   3 of  24 in __main__.example_0
***Test Failed*** 3 failures.
For whitespace errors, see the file /scratch/mvngu/release/sage-4.1.1/tmp/.doctest_twist.py
	 [23.3 s]
```
These have nothing to do to with the updated mpmath spkg. They are known failures and have been reported in Sage 4.1.1.



---

archive/issue_comments_055127.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-09-02T09:44:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6740",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6740#issuecomment-55127",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_events_015897.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2009-09-02T09:44:53Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6740",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6740#event-15897"
}
```
