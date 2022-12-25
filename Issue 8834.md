# Issue 8834: make R png graphics doctests optional

archive/issues_008834.json:
```json
{
    "body": "Assignee: jason, was\n\n```\nHi,\n\nContinuing this thread, I think that building Sage shouldn't require X11.  E.g., on t2, the new R png tests fail:\n\nFile \"/scratch/wstein/build/sage-4.4.1.alpha2/devel/sage/sage/interfaces/r.py\", line 993:\n    sage: r.png(filename='\"%s\"'%filename) # filename not needed in notebook, used for doctesting\nException raised:\n...\n    sage: r.png(filename='\"%s\"'%filename) # filename not needed in notebook, used for doctesting\n      File \"/scratch/wstein/build/sage-4.4.1.alpha2/local/lib/python/site-packages/sage/interfaces/r.py\n\", line 356, in png\n        raise RuntimeError, \"R was not compiled with PNG support\"\n    RuntimeError: R was not compiled with PNG support\n*******************************************************************\n\n---\n\nUnfortunately, this really means that those tests should all be changed to be \n\n   # optional -- x11\n\nThey won't get tested by \"make test\".  However, doing \n\n  ./sage -t -only_optional=x11 devel/sage/sage/\n\nwill test them.  The release manager checklist will suggest to do this check. \n\nI've opened a ticket for this:\n\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/8834\n\n",
    "created_at": "2010-05-01T06:14:29Z",
    "labels": [
        "component: graphics",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.1",
    "title": "make R png graphics doctests optional",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8834",
    "user": "https://github.com/williamstein"
}
```
Assignee: jason, was

```
Hi,

Continuing this thread, I think that building Sage shouldn't require X11.  E.g., on t2, the new R png tests fail:

File "/scratch/wstein/build/sage-4.4.1.alpha2/devel/sage/sage/interfaces/r.py", line 993:
    sage: r.png(filename='"%s"'%filename) # filename not needed in notebook, used for doctesting
Exception raised:
...
    sage: r.png(filename='"%s"'%filename) # filename not needed in notebook, used for doctesting
      File "/scratch/wstein/build/sage-4.4.1.alpha2/local/lib/python/site-packages/sage/interfaces/r.py
", line 356, in png
        raise RuntimeError, "R was not compiled with PNG support"
    RuntimeError: R was not compiled with PNG support
*******************************************************************

---

Unfortunately, this really means that those tests should all be changed to be 

   # optional -- x11

They won't get tested by "make test".  However, doing 

  ./sage -t -only_optional=x11 devel/sage/sage/

will test them.  The release manager checklist will suggest to do this check. 

I've opened a ticket for this:

```

Issue created by migration from https://trac.sagemath.org/ticket/8834





---

archive/issue_comments_081097.json:
```json
{
    "body": "PNG libraries do exist on Solaris. Whether they are sufficiently new I don't know.",
    "created_at": "2010-05-01T10:25:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8834",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8834#issuecomment-81097",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

PNG libraries do exist on Solaris. Whether they are sufficiently new I don't know.



---

archive/issue_comments_081098.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-05-01T18:58:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8834",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8834#issuecomment-81098",
    "user": "https://github.com/williamstein"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_081099.json:
```json
{
    "body": "There are *many* platforms -- even the latest OS X -- where our copy of R gets built without any graphics support (png or aqua or whatever). \n\nHaving these tests exist, but get clearly marked #optional, will remind users that they are usually broken, and that we know this, at least until we fix this major issue.",
    "created_at": "2010-05-01T18:58:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8834",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8834#issuecomment-81099",
    "user": "https://github.com/williamstein"
}
```

There are *many* platforms -- even the latest OS X -- where our copy of R gets built without any graphics support (png or aqua or whatever). 

Having these tests exist, but get clearly marked #optional, will remind users that they are usually broken, and that we know this, at least until we fix this major issue.



---

archive/issue_comments_081100.json:
```json
{
    "body": "Attachment [trac_8834.patch](tarball://root/attachments/some-uuid/ticket8834/trac_8834.patch) by @williamstein created at 2010-05-01 18:59:27",
    "created_at": "2010-05-01T18:59:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8834",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8834#issuecomment-81100",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac_8834.patch](tarball://root/attachments/some-uuid/ticket8834/trac_8834.patch) by @williamstein created at 2010-05-01 18:59:27



---

archive/issue_comments_081101.json:
```json
{
    "body": "How to test:\n\n```\nwstein@sage:~/build/release/4.4.1/sage-4.4.1.rc0$ ./sage -t devel/sage/sage/interfaces/r.py \nsage -t  \"devel/sage/sage/interfaces/r.py\"                  \n         [4.2 s]\n \n----------------------------------------------------------------------\nAll tests passed!\nTotal time for all tests: 4.2 seconds\nwstein@sage:~/build/release/4.4.1/sage-4.4.1.rc0$ ./sage -t --only_optional=rgraphics devel/sage/sage/interfaces/r.py \nsage -t --only_optional=rgraphics \"devel/sage/sage/interfaces/r.py\"\n         [3.3 s]\n \n----------------------------------------------------------------------\nAll tests passed!\nTotal time for all tests: 3.3 seconds\nwstein@sage:~/build/release/4.4.1/sage-4.4.1.rc0$ \n```",
    "created_at": "2010-05-01T19:01:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8834",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8834#issuecomment-81101",
    "user": "https://github.com/williamstein"
}
```

How to test:

```
wstein@sage:~/build/release/4.4.1/sage-4.4.1.rc0$ ./sage -t devel/sage/sage/interfaces/r.py 
sage -t  "devel/sage/sage/interfaces/r.py"                  
         [4.2 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 4.2 seconds
wstein@sage:~/build/release/4.4.1/sage-4.4.1.rc0$ ./sage -t --only_optional=rgraphics devel/sage/sage/interfaces/r.py 
sage -t --only_optional=rgraphics "devel/sage/sage/interfaces/r.py"
         [3.3 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 3.3 seconds
wstein@sage:~/build/release/4.4.1/sage-4.4.1.rc0$ 
```



---

archive/issue_comments_081102.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-05-02T23:49:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8834",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8834#issuecomment-81102",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_081103.json:
```json
{
    "body": "Doctests pass on bsd.math (Mac OS X 10.6) with the option:\n\n```\n[mvngu@bsd sage-4.4.1.rc0]$ ./sage -t -long devel/sage-main/sage/interfaces/r.py\n```\nBut doctests would fail with:\n\n```\nsage -t -long --only_optional=rgraphics \"devel/sage-main/sage/interfaces/r.py\"\n**********************************************************************\nFile \"/Users/mvngu/sandbox/sage-4.4.1.rc0/devel/sage-main/sage/interfaces/r.py\", line 338:\n    sage: r.png(filename='\"%s\"'%filename)             # optional -- rgraphics\nException raised:\n    Traceback (most recent call last):\n      File \"/Users/mvngu/sandbox/sage-4.4.1.rc0/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/Users/mvngu/sandbox/sage-4.4.1.rc0/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/Users/mvngu/sandbox/sage-4.4.1.rc0/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_0[3]>\", line 1, in <module>\n        r.png(filename='\"%s\"'%filename)             # optional -- rgraphics###line 338:\n    sage: r.png(filename='\"%s\"'%filename)             # optional -- rgraphics\n      File \"/Users/mvngu/sandbox/sage-4.4.1.rc0/local/lib/python/site-packages/sage/interfaces/r.py\", line 359, in png\n        raise RuntimeError, \"R was not compiled with PNG support\"\n    RuntimeError: R was not compiled with PNG support\n**********************************************************************\nFile \"/Users/mvngu/sandbox/sage-4.4.1.rc0/devel/sage-main/sage/interfaces/r.py\", line 342:\n    sage: r.plot(x,y) # This saves to filename, but is not viewable from command line; optional -- rgraphics\nExpected:\n    null device\n              1\nGot:\n    Error: object 'sage8' not found\n**********************************************************************\nFile \"/Users/mvngu/sandbox/sage-4.4.1.rc0/devel/sage-main/sage/interfaces/r.py\", line 345:\n    sage: import os; os.unlink(filename) # We remove the file for doctesting; optional -- rgraphics\nException raised:\n    Traceback (most recent call last):\n      File \"/Users/mvngu/sandbox/sage-4.4.1.rc0/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/Users/mvngu/sandbox/sage-4.4.1.rc0/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/Users/mvngu/sandbox/sage-4.4.1.rc0/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_0[7]>\", line 1, in <module>\n        import os; os.unlink(filename) # We remove the file for doctesting; optional -- rgraphics###line 345:\n    sage: import os; os.unlink(filename) # We remove the file for doctesting; optional -- rgraphics\n    OSError: [Errno 2] No such file or directory: '/Users/mvngu/.sage//temp/bsd.local/96132//tmp_0.png'\n**********************************************************************\nFile \"/Users/mvngu/sandbox/sage-4.4.1.rc0/devel/sage-main/sage/interfaces/r.py\", line 352:\n    sage: \"TRUE\" in s+t                      # optional -- rgraphics\nExpected:\n    True\nGot:\n    False\n**********************************************************************\nFile \"/Users/mvngu/sandbox/sage-4.4.1.rc0/devel/sage-main/sage/interfaces/r.py\", line 961:\n    sage: r.plot(\"1:10\")                # optional -- rgraphics\nExpected:\n    null device\n              1\nGot:\n    [1] 4\n**********************************************************************\nFile \"/Users/mvngu/sandbox/sage-4.4.1.rc0/devel/sage-main/sage/interfaces/r.py\", line 970:\n    sage: r.png(filename='\"%s\"'%filename) # Note the double quotes in single quotes!; optional -- rgraphics\nException raised:\n    Traceback (most recent call last):\n      File \"/Users/mvngu/sandbox/sage-4.4.1.rc0/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/Users/mvngu/sandbox/sage-4.4.1.rc0/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/Users/mvngu/sandbox/sage-4.4.1.rc0/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_1[5]>\", line 1, in <module>\n        r.png(filename='\"%s\"'%filename) # Note the double quotes in single quotes!; optional -- rgraphics###line 970:\n    sage: r.png(filename='\"%s\"'%filename) # Note the double quotes in single quotes!; optional -- rgraphics\n      File \"/Users/mvngu/sandbox/sage-4.4.1.rc0/local/lib/python/site-packages/sage/interfaces/r.py\", line 359, in png\n        raise RuntimeError, \"R was not compiled with PNG support\"\n    RuntimeError: R was not compiled with PNG support\n**********************************************************************\nFile \"/Users/mvngu/sandbox/sage-4.4.1.rc0/devel/sage-main/sage/interfaces/r.py\", line 974:\n    sage: r.plot(x,y)         # optional -- rgraphics\nExpected:\n    null device\n              1\nGot:\n    Error: object 'sage10' not found\n**********************************************************************\nFile \"/Users/mvngu/sandbox/sage-4.4.1.rc0/devel/sage-main/sage/interfaces/r.py\", line 977:\n    sage: import os; os.unlink(filename) # For doctesting, we remove the file; optional -- rgraphics\nException raised:\n    Traceback (most recent call last):\n      File \"/Users/mvngu/sandbox/sage-4.4.1.rc0/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/Users/mvngu/sandbox/sage-4.4.1.rc0/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/Users/mvngu/sandbox/sage-4.4.1.rc0/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_1[9]>\", line 1, in <module>\n        import os; os.unlink(filename) # For doctesting, we remove the file; optional -- rgraphics###line 977:\n    sage: import os; os.unlink(filename) # For doctesting, we remove the file; optional -- rgraphics\n    OSError: [Errno 2] No such file or directory: '/Users/mvngu/.sage//temp/bsd.local/96132//tmp_1.png'\n**********************************************************************\nFile \"/Users/mvngu/sandbox/sage-4.4.1.rc0/devel/sage-main/sage/interfaces/r.py\", line 997:\n    sage: r.png(filename='\"%s\"'%filename) # filename not needed in notebook, used for doctesting; optional -- rgraphics\nException raised:\n    Traceback (most recent call last):\n      File \"/Users/mvngu/sandbox/sage-4.4.1.rc0/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/Users/mvngu/sandbox/sage-4.4.1.rc0/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/Users/mvngu/sandbox/sage-4.4.1.rc0/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_1[11]>\", line 1, in <module>\n        r.png(filename='\"%s\"'%filename) # filename not needed in notebook, used for doctesting; optional -- rgraphics###line 997:\n    sage: r.png(filename='\"%s\"'%filename) # filename not needed in notebook, used for doctesting; optional -- rgraphics\n      File \"/Users/mvngu/sandbox/sage-4.4.1.rc0/local/lib/python/site-packages/sage/interfaces/r.py\", line 359, in png\n        raise RuntimeError, \"R was not compiled with PNG support\"\n    RuntimeError: R was not compiled with PNG support\n**********************************************************************\nFile \"/Users/mvngu/sandbox/sage-4.4.1.rc0/devel/sage-main/sage/interfaces/r.py\", line 1000:\n    sage: r(\"print(histogram(~wt | cyl, data=mtcars))\") # plot should appear; optional -- rgraphics\nExpected nothing\nGot:\n    [1] 4\n**********************************************************************\nFile \"/Users/mvngu/sandbox/sage-4.4.1.rc0/devel/sage-main/sage/interfaces/r.py\", line 1001:\n    sage: import os; os.unlink(filename) # We remove the file for doctesting, not needed in notebook;  optional -- rgraphics\nException raised:\n    Traceback (most recent call last):\n      File \"/Users/mvngu/sandbox/sage-4.4.1.rc0/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/Users/mvngu/sandbox/sage-4.4.1.rc0/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/Users/mvngu/sandbox/sage-4.4.1.rc0/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_1[14]>\", line 1, in <module>\n        import os; os.unlink(filename) # We remove the file for doctesting, not needed in notebook;  optional -- rgraphics###line 1001:\n    sage: import os; os.unlink(filename) # We remove the file for doctesting, not needed in notebook;  optional -- rgraphics\n    OSError: [Errno 2] No such file or directory: '/Users/mvngu/.sage//temp/bsd.local/96132//tmp_2.png'\n**********************************************************************\n2 items had failures:\n   4 of  11 in __main__.example_0\n   7 of  15 in __main__.example_1\n***Test Failed*** 11 failures.\nFor whitespace errors, see the file /Users/mvngu/.sage//tmp/.doctest_r.py\n\t [3.0 s]\n \n----------------------------------------------------------------------\nThe following tests failed:\n\n\n\tsage -t -long --only_optional=rgraphics \"devel/sage-main/sage/interfaces/r.py\"\nTotal time for all tests: 3.0 seconds\n```\nMaking the specified doctests optional mean we're postponing a fix for the failure for a later time. Note that the above doctest failure is specific to Mac OS X as far as I can tell.",
    "created_at": "2010-05-02T23:49:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8834",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8834#issuecomment-81103",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Doctests pass on bsd.math (Mac OS X 10.6) with the option:

```
[mvngu@bsd sage-4.4.1.rc0]$ ./sage -t -long devel/sage-main/sage/interfaces/r.py
```
But doctests would fail with:

```
sage -t -long --only_optional=rgraphics "devel/sage-main/sage/interfaces/r.py"
**********************************************************************
File "/Users/mvngu/sandbox/sage-4.4.1.rc0/devel/sage-main/sage/interfaces/r.py", line 338:
    sage: r.png(filename='"%s"'%filename)             # optional -- rgraphics
Exception raised:
    Traceback (most recent call last):
      File "/Users/mvngu/sandbox/sage-4.4.1.rc0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/Users/mvngu/sandbox/sage-4.4.1.rc0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/Users/mvngu/sandbox/sage-4.4.1.rc0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[3]>", line 1, in <module>
        r.png(filename='"%s"'%filename)             # optional -- rgraphics###line 338:
    sage: r.png(filename='"%s"'%filename)             # optional -- rgraphics
      File "/Users/mvngu/sandbox/sage-4.4.1.rc0/local/lib/python/site-packages/sage/interfaces/r.py", line 359, in png
        raise RuntimeError, "R was not compiled with PNG support"
    RuntimeError: R was not compiled with PNG support
**********************************************************************
File "/Users/mvngu/sandbox/sage-4.4.1.rc0/devel/sage-main/sage/interfaces/r.py", line 342:
    sage: r.plot(x,y) # This saves to filename, but is not viewable from command line; optional -- rgraphics
Expected:
    null device
              1
Got:
    Error: object 'sage8' not found
**********************************************************************
File "/Users/mvngu/sandbox/sage-4.4.1.rc0/devel/sage-main/sage/interfaces/r.py", line 345:
    sage: import os; os.unlink(filename) # We remove the file for doctesting; optional -- rgraphics
Exception raised:
    Traceback (most recent call last):
      File "/Users/mvngu/sandbox/sage-4.4.1.rc0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/Users/mvngu/sandbox/sage-4.4.1.rc0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/Users/mvngu/sandbox/sage-4.4.1.rc0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[7]>", line 1, in <module>
        import os; os.unlink(filename) # We remove the file for doctesting; optional -- rgraphics###line 345:
    sage: import os; os.unlink(filename) # We remove the file for doctesting; optional -- rgraphics
    OSError: [Errno 2] No such file or directory: '/Users/mvngu/.sage//temp/bsd.local/96132//tmp_0.png'
**********************************************************************
File "/Users/mvngu/sandbox/sage-4.4.1.rc0/devel/sage-main/sage/interfaces/r.py", line 352:
    sage: "TRUE" in s+t                      # optional -- rgraphics
Expected:
    True
Got:
    False
**********************************************************************
File "/Users/mvngu/sandbox/sage-4.4.1.rc0/devel/sage-main/sage/interfaces/r.py", line 961:
    sage: r.plot("1:10")                # optional -- rgraphics
Expected:
    null device
              1
Got:
    [1] 4
**********************************************************************
File "/Users/mvngu/sandbox/sage-4.4.1.rc0/devel/sage-main/sage/interfaces/r.py", line 970:
    sage: r.png(filename='"%s"'%filename) # Note the double quotes in single quotes!; optional -- rgraphics
Exception raised:
    Traceback (most recent call last):
      File "/Users/mvngu/sandbox/sage-4.4.1.rc0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/Users/mvngu/sandbox/sage-4.4.1.rc0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/Users/mvngu/sandbox/sage-4.4.1.rc0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_1[5]>", line 1, in <module>
        r.png(filename='"%s"'%filename) # Note the double quotes in single quotes!; optional -- rgraphics###line 970:
    sage: r.png(filename='"%s"'%filename) # Note the double quotes in single quotes!; optional -- rgraphics
      File "/Users/mvngu/sandbox/sage-4.4.1.rc0/local/lib/python/site-packages/sage/interfaces/r.py", line 359, in png
        raise RuntimeError, "R was not compiled with PNG support"
    RuntimeError: R was not compiled with PNG support
**********************************************************************
File "/Users/mvngu/sandbox/sage-4.4.1.rc0/devel/sage-main/sage/interfaces/r.py", line 974:
    sage: r.plot(x,y)         # optional -- rgraphics
Expected:
    null device
              1
Got:
    Error: object 'sage10' not found
**********************************************************************
File "/Users/mvngu/sandbox/sage-4.4.1.rc0/devel/sage-main/sage/interfaces/r.py", line 977:
    sage: import os; os.unlink(filename) # For doctesting, we remove the file; optional -- rgraphics
Exception raised:
    Traceback (most recent call last):
      File "/Users/mvngu/sandbox/sage-4.4.1.rc0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/Users/mvngu/sandbox/sage-4.4.1.rc0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/Users/mvngu/sandbox/sage-4.4.1.rc0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_1[9]>", line 1, in <module>
        import os; os.unlink(filename) # For doctesting, we remove the file; optional -- rgraphics###line 977:
    sage: import os; os.unlink(filename) # For doctesting, we remove the file; optional -- rgraphics
    OSError: [Errno 2] No such file or directory: '/Users/mvngu/.sage//temp/bsd.local/96132//tmp_1.png'
**********************************************************************
File "/Users/mvngu/sandbox/sage-4.4.1.rc0/devel/sage-main/sage/interfaces/r.py", line 997:
    sage: r.png(filename='"%s"'%filename) # filename not needed in notebook, used for doctesting; optional -- rgraphics
Exception raised:
    Traceback (most recent call last):
      File "/Users/mvngu/sandbox/sage-4.4.1.rc0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/Users/mvngu/sandbox/sage-4.4.1.rc0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/Users/mvngu/sandbox/sage-4.4.1.rc0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_1[11]>", line 1, in <module>
        r.png(filename='"%s"'%filename) # filename not needed in notebook, used for doctesting; optional -- rgraphics###line 997:
    sage: r.png(filename='"%s"'%filename) # filename not needed in notebook, used for doctesting; optional -- rgraphics
      File "/Users/mvngu/sandbox/sage-4.4.1.rc0/local/lib/python/site-packages/sage/interfaces/r.py", line 359, in png
        raise RuntimeError, "R was not compiled with PNG support"
    RuntimeError: R was not compiled with PNG support
**********************************************************************
File "/Users/mvngu/sandbox/sage-4.4.1.rc0/devel/sage-main/sage/interfaces/r.py", line 1000:
    sage: r("print(histogram(~wt | cyl, data=mtcars))") # plot should appear; optional -- rgraphics
Expected nothing
Got:
    [1] 4
**********************************************************************
File "/Users/mvngu/sandbox/sage-4.4.1.rc0/devel/sage-main/sage/interfaces/r.py", line 1001:
    sage: import os; os.unlink(filename) # We remove the file for doctesting, not needed in notebook;  optional -- rgraphics
Exception raised:
    Traceback (most recent call last):
      File "/Users/mvngu/sandbox/sage-4.4.1.rc0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/Users/mvngu/sandbox/sage-4.4.1.rc0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/Users/mvngu/sandbox/sage-4.4.1.rc0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_1[14]>", line 1, in <module>
        import os; os.unlink(filename) # We remove the file for doctesting, not needed in notebook;  optional -- rgraphics###line 1001:
    sage: import os; os.unlink(filename) # We remove the file for doctesting, not needed in notebook;  optional -- rgraphics
    OSError: [Errno 2] No such file or directory: '/Users/mvngu/.sage//temp/bsd.local/96132//tmp_2.png'
**********************************************************************
2 items had failures:
   4 of  11 in __main__.example_0
   7 of  15 in __main__.example_1
***Test Failed*** 11 failures.
For whitespace errors, see the file /Users/mvngu/.sage//tmp/.doctest_r.py
	 [3.0 s]
 
----------------------------------------------------------------------
The following tests failed:


	sage -t -long --only_optional=rgraphics "devel/sage-main/sage/interfaces/r.py"
Total time for all tests: 3.0 seconds
```
Making the specified doctests optional mean we're postponing a fix for the failure for a later time. Note that the above doctest failure is specific to Mac OS X as far as I can tell.



---

archive/issue_events_021565.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2010-05-02T23:49:38Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8834",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8834#event-21565"
}
```



---

archive/issue_events_021566.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2010-05-02T23:49:51Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8834",
    "milestone": "sage-4.4.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8834#event-21566"
}
```



---

archive/issue_comments_081104.json:
```json
{
    "body": "> Making the specified doctests optional mean we're postponing a fix for the failure for a later time. \n\n\nI'm not so sure.  I'm still not convinced R can do any graphics on a system without X11 dev packages, which will not be a dependency for building Sage.   R graphics might always be optional on Linux.   I really hope I'm wrong!\n\n> Note that the above doctest failure is specific to Mac OS X as far as I can tell.\n\n\nThey also happen on some Linux and Solaris boxes.",
    "created_at": "2010-05-03T03:31:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8834",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8834#issuecomment-81104",
    "user": "https://github.com/williamstein"
}
```

> Making the specified doctests optional mean we're postponing a fix for the failure for a later time. 


I'm not so sure.  I'm still not convinced R can do any graphics on a system without X11 dev packages, which will not be a dependency for building Sage.   R graphics might always be optional on Linux.   I really hope I'm wrong!

> Note that the above doctest failure is specific to Mac OS X as far as I can tell.


They also happen on some Linux and Solaris boxes.



---

archive/issue_comments_081105.json:
```json
{
    "body": "Replying to [comment:6 was]:\n> > Making the specified doctests optional mean we're postponing a fix for the failure for a later time. \n\n> \n> I'm not so sure.  I'm still not convinced R can do any graphics on a system without X11 dev packages, which will not be a dependency for building Sage.   R graphics might always be optional on Linux.   I really hope I'm wrong!\n\n\nI am sure you are, having seen some workarounds on the internet.  But how to deal with this is something we need an R build expert for, I think.\n\nThanks to Minh for dealing with this - I was not able to deal with any Sage-devel related material this weekend.\n\n> There are *many* platforms -- even the latest OS X -- where our copy of R gets built without any graphics support (png or aqua or whatever).\n\nYou mean OS X 10.6?  That's odd - that's where I did the main work for testing the new R spkg which should compile with aqua support whenever the system is 'Darwin'.",
    "created_at": "2010-05-03T14:50:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8834",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8834#issuecomment-81105",
    "user": "https://github.com/kcrisman"
}
```

Replying to [comment:6 was]:
> > Making the specified doctests optional mean we're postponing a fix for the failure for a later time. 

> 
> I'm not so sure.  I'm still not convinced R can do any graphics on a system without X11 dev packages, which will not be a dependency for building Sage.   R graphics might always be optional on Linux.   I really hope I'm wrong!


I am sure you are, having seen some workarounds on the internet.  But how to deal with this is something we need an R build expert for, I think.

Thanks to Minh for dealing with this - I was not able to deal with any Sage-devel related material this weekend.

> There are *many* platforms -- even the latest OS X -- where our copy of R gets built without any graphics support (png or aqua or whatever).

You mean OS X 10.6?  That's odd - that's where I did the main work for testing the new R spkg which should compile with aqua support whenever the system is 'Darwin'.



---

archive/issue_comments_081106.json:
```json
{
    "body": "Replying to [comment:7 kcrisman]:\n> Replying to [comment:6 was]:\n> > > Making the specified doctests optional mean we're postponing a fix for the failure for a later time. \n\n> > \n> > I'm not so sure.  I'm still not convinced R can do any graphics on a system without X11 dev packages, which will not be a dependency for building Sage.   R graphics might always be optional on Linux.   I really hope I'm wrong!\n\n> \n> I am sure you are, having seen some workarounds on the internet.  But how to deal with this is something we need an R build expert for, I think.\n\n\nSorry, I mean wrong in the sense that R can do graphics in other ways, apparently.  I don't know whether it will allow capabilities() to return png support True without them, which is what I meant to say.",
    "created_at": "2010-05-03T14:52:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8834",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8834#issuecomment-81106",
    "user": "https://github.com/kcrisman"
}
```

Replying to [comment:7 kcrisman]:
> Replying to [comment:6 was]:
> > > Making the specified doctests optional mean we're postponing a fix for the failure for a later time. 

> > 
> > I'm not so sure.  I'm still not convinced R can do any graphics on a system without X11 dev packages, which will not be a dependency for building Sage.   R graphics might always be optional on Linux.   I really hope I'm wrong!

> 
> I am sure you are, having seen some workarounds on the internet.  But how to deal with this is something we need an R build expert for, I think.


Sorry, I mean wrong in the sense that R can do graphics in other ways, apparently.  I don't know whether it will allow capabilities() to return png support True without them, which is what I meant to say.



---

archive/issue_comments_081107.json:
```json
{
    "body": "Just putting things here because there isn't anywhere else convenient...  R install guide says:\n\n```\nUnless you do not want to view graphs on-screen you need \u2018X11\u2019 installed, including its headers and client libraries. For recent Fedora distributions it means (at least) \u2018libX11\u2019, \u2018libX11-devel\u2019, \u2018libXt\u2019 and \u2018libXt-devel\u2019. On Debian we recommend the meta-package \u2018xorg-dev\u2019. If you really do not want these you will need to explicitly configure R without X11, using --with-x=no.\n```",
    "created_at": "2010-05-03T19:11:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8834",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8834#issuecomment-81107",
    "user": "https://github.com/kcrisman"
}
```

Just putting things here because there isn't anywhere else convenient...  R install guide says:

```
Unless you do not want to view graphs on-screen you need ‘X11’ installed, including its headers and client libraries. For recent Fedora distributions it means (at least) ‘libX11’, ‘libX11-devel’, ‘libXt’ and ‘libXt-devel’. On Debian we recommend the meta-package ‘xorg-dev’. If you really do not want these you will need to explicitly configure R without X11, using --with-x=no.
```



---

archive/issue_comments_081108.json:
```json
{
    "body": "This continues at #8868.",
    "created_at": "2010-05-04T15:21:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8834",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8834#issuecomment-81108",
    "user": "https://github.com/kcrisman"
}
```

This continues at #8868.
