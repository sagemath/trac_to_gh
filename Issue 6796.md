# Issue 6796: doctest failure in sage/sage/interfaces/psage.py due to upgrade to Maxima 5.19.1

archive/issues_006796.json:
```json
{
    "body": "Assignee: @williamstein\n\nKeywords: maxima\n\nOn Solaris (SPARC), the following tests failed. Both ECL and Maxima were updated - ECL version 9.8.4 (see trac #6564); Maxima version 5.19.1 (see trac #6699). Updated spkgs can be found here. \n\nhttp://sage.math.washington.edu/home/kirkby/Solaris-fixes/ecl-9.8.4/ecl-9.8.4.spkg\n\nhttp://sage.math.washington.edu/home/kirkby/Solaris-fixes/maxima-5.19.1/\n\n\n```\n\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nThu Aug 20 20:02:37 BST 2009\ndsage-trial tmp directory doesn't exist - creating ...\nThis script will run the unit tests for DSage\n```\n\n| Sage Version 4.1.1, Release Date: 2009-08-14                       |\n| Type notebook() for the GUI, and license() for information.        |\n<SNIP>\n\n```\nsage -t  \"devel/sage/sage/interfaces/psage.py\"\n**********************************************************************\nFile \"/export/home/drkirkby/sage/sage-4.1.1/devel/sage/sage/interfaces/psage.py\", line 23:\n    sage: w = [x('factor(2^%s-1)'% randint(250,310)) for x in v]\nException raised:\n    Traceback (most recent call last):\n      File \"/export/home/drkirkby/sage/sage-4.1.1/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/export/home/drkirkby/sage/sage-4.1.1/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/export/home/drkirkby/sage/sage-4.1.1/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_0[3]>\", line 1, in <module>\n        w = [x('factor(2^%s-1)'% randint(Integer(250),Integer(310))) for x in v]###line 23:\n    sage: w = [x('factor(2^%s-1)'% randint(250,310)) for x in v]\n      File \"/export/home/drkirkby/sage/sage-4.1.1/local/lib/python/site-packages/sage/interfaces/sage0.py\", line 263, in __call__\n        return SageElement(self, x)\n      File \"/export/home/drkirkby/sage/sage-4.1.1/local/lib/python/site-packages/sage/interfaces/expect.py\", line 1433, in __init__\n        raise TypeError, x\n    TypeError: Unable to start sage\n**********************************************************************\nFile \"/export/home/drkirkby/sage/sage-4.1.1/devel/sage/sage/interfaces/psage.py\", line 26:\n    sage: print \"ignore this\";  w       # random output (depends on timing)\nException raised:\n    Traceback (most recent call last):\n      File \"/export/home/drkirkby/sage/sage-4.1.1/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/export/home/drkirkby/sage/sage-4.1.1/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/export/home/drkirkby/sage/sage-4.1.1/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_0[4]>\", line 1, in <module>\n        print \"ignore this\";  w       # random output (depends on timing)###line 26:\n    sage: print \"ignore this\";  w       # random output (depends on timing)\n    NameError: name 'w' is not defined\n**********************************************************************\nFile \"/export/home/drkirkby/sage/sage-4.1.1/devel/sage/sage/interfaces/psage.py\", line 35:\n    sage: print \"ignore this\";  w       # random output\nException raised:\n    Traceback (most recent call last):\n      File \"/export/home/drkirkby/sage/sage-4.1.1/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/export/home/drkirkby/sage/sage-4.1.1/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/export/home/drkirkby/sage/sage-4.1.1/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_0[5]>\", line 1, in <module>\n        print \"ignore this\";  w       # random output###line 35:\n    sage: print \"ignore this\";  w       # random output\n    NameError: name 'w' is not defined\n**********************************************************************\n1 items had failures:\n   3 of   6 in __main__.example_0\n***Test Failed*** 3 failures.\nFor whitespace errors, see the file /export/home/drkirkby/sage/sage-4.1.1/tmp/.doctest_psage.py\n         [87.0 s]\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6796\n\n",
    "created_at": "2009-08-21T07:29:44Z",
    "labels": [
        "component: interfaces",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3",
    "title": "doctest failure in sage/sage/interfaces/psage.py due to upgrade to Maxima 5.19.1",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6796",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```
Assignee: @williamstein

Keywords: maxima

On Solaris (SPARC), the following tests failed. Both ECL and Maxima were updated - ECL version 9.8.4 (see trac #6564); Maxima version 5.19.1 (see trac #6699). Updated spkgs can be found here. 

http://sage.math.washington.edu/home/kirkby/Solaris-fixes/ecl-9.8.4/ecl-9.8.4.spkg

http://sage.math.washington.edu/home/kirkby/Solaris-fixes/maxima-5.19.1/


```

----------------------------------------------------------------------
----------------------------------------------------------------------
Thu Aug 20 20:02:37 BST 2009
dsage-trial tmp directory doesn't exist - creating ...
This script will run the unit tests for DSage
```

| Sage Version 4.1.1, Release Date: 2009-08-14                       |
| Type notebook() for the GUI, and license() for information.        |
<SNIP>

```
sage -t  "devel/sage/sage/interfaces/psage.py"
**********************************************************************
File "/export/home/drkirkby/sage/sage-4.1.1/devel/sage/sage/interfaces/psage.py", line 23:
    sage: w = [x('factor(2^%s-1)'% randint(250,310)) for x in v]
Exception raised:
    Traceback (most recent call last):
      File "/export/home/drkirkby/sage/sage-4.1.1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/export/home/drkirkby/sage/sage-4.1.1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/export/home/drkirkby/sage/sage-4.1.1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[3]>", line 1, in <module>
        w = [x('factor(2^%s-1)'% randint(Integer(250),Integer(310))) for x in v]###line 23:
    sage: w = [x('factor(2^%s-1)'% randint(250,310)) for x in v]
      File "/export/home/drkirkby/sage/sage-4.1.1/local/lib/python/site-packages/sage/interfaces/sage0.py", line 263, in __call__
        return SageElement(self, x)
      File "/export/home/drkirkby/sage/sage-4.1.1/local/lib/python/site-packages/sage/interfaces/expect.py", line 1433, in __init__
        raise TypeError, x
    TypeError: Unable to start sage
**********************************************************************
File "/export/home/drkirkby/sage/sage-4.1.1/devel/sage/sage/interfaces/psage.py", line 26:
    sage: print "ignore this";  w       # random output (depends on timing)
Exception raised:
    Traceback (most recent call last):
      File "/export/home/drkirkby/sage/sage-4.1.1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/export/home/drkirkby/sage/sage-4.1.1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/export/home/drkirkby/sage/sage-4.1.1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[4]>", line 1, in <module>
        print "ignore this";  w       # random output (depends on timing)###line 26:
    sage: print "ignore this";  w       # random output (depends on timing)
    NameError: name 'w' is not defined
**********************************************************************
File "/export/home/drkirkby/sage/sage-4.1.1/devel/sage/sage/interfaces/psage.py", line 35:
    sage: print "ignore this";  w       # random output
Exception raised:
    Traceback (most recent call last):
      File "/export/home/drkirkby/sage/sage-4.1.1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/export/home/drkirkby/sage/sage-4.1.1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/export/home/drkirkby/sage/sage-4.1.1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[5]>", line 1, in <module>
        print "ignore this";  w       # random output###line 35:
    sage: print "ignore this";  w       # random output
    NameError: name 'w' is not defined
**********************************************************************
1 items had failures:
   3 of   6 in __main__.example_0
***Test Failed*** 3 failures.
For whitespace errors, see the file /export/home/drkirkby/sage/sage-4.1.1/tmp/.doctest_psage.py
         [87.0 s]
```


Issue created by migration from https://trac.sagemath.org/ticket/6796





---

archive/issue_comments_055878.json:
```json
{
    "body": "Resolution: worksforme",
    "created_at": "2009-12-17T20:15:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6796",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6796#issuecomment-55878",
    "user": "https://github.com/burcin"
}
```

Resolution: worksforme



---

archive/issue_comments_055879.json:
```json
{
    "body": "I am closing this as `worksforme`. We've gone several releases with maxima-5.19.1, who knows what the problem that prevented Sage from starting as in the description was.",
    "created_at": "2009-12-17T20:15:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6796",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6796#issuecomment-55879",
    "user": "https://github.com/burcin"
}
```

I am closing this as `worksforme`. We've gone several releases with maxima-5.19.1, who knows what the problem that prevented Sage from starting as in the description was.



---

archive/issue_events_007031.json:
```json
{
    "actor": "https://github.com/burcin",
    "created_at": "2009-12-17T20:15:10Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6796",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6796#event-7031"
}
```
