# Issue 8448: doc/common/builder.py doctests write files in Sage tree

archive/issues_008448.json:
```json
{
    "body": "Assignee: mvngu\n\nCC:  @dimpase\n\nKeywords: builder.py, doctest, system-wide\n\nI am using a system-wide install, so I don't have write access in the Sage tree.  When I run `sage -testall`, I get the following errors.  (More may come; it's only been running a few minutes. :-)\n\n\n```\nsage -t  \"devel/sage/doc/common/builder.py\"                 \n**********************************************************************\nFile \"/share/apps/contrib/sage-4.3.3/devel/sage/doc/common/builder.py\", line 157:\n    sage: b = builder.DocBuilder('tutorial')\nException raised:\n    Traceback (most recent call last):\n      File \"/share/apps/contrib/sage-4.3.3/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/share/apps/contrib/sage-4.3.3/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/share/apps/contrib/sage-4.3.3/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_4[3]>\", line 1, in <module>\n        b = builder.DocBuilder('tutorial')###line 157:\n    sage: b = builder.DocBuilder('tutorial')\n      File \"/share/apps/contrib/sage-4.3.3/devel/sage/doc/common/builder.py\", line 145, in __init__\n        mkdir(os.path.join(self.dir, \"static\"))\n      File \"/share/apps/contrib/sage-4.3.3/devel/sage/doc/common/builder.py\", line 55, in mkdir\n        os.makedirs(path)\n      File \"/share/apps/contrib/sage-4.3.3/local/lib/python2.6/os.py\", line 157, in makedirs\n        mkdir(name, mode)\n    OSError: [Errno 13] Permission denied: '/share/apps/contrib/sage-4.3.3/devel/sage/doc/en/tutorial/static'\n**********************************************************************\nFile \"/share/apps/contrib/sage-4.3.3/devel/sage/doc/common/builder.py\", line 158:\n    sage: b._output_dir('html')\nException raised:\n    Traceback (most recent call last):\n      File \"/share/apps/contrib/sage-4.3.3/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/share/apps/contrib/sage-4.3.3/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/share/apps/contrib/sage-4.3.3/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_4[4]>\", line 1, in <module>\n        b._output_dir('html')###line 158:\n    sage: b._output_dir('html')\n    NameError: name 'b' is not defined\n**********************************************************************\nFile \"/share/apps/contrib/sage-4.3.3/devel/sage/doc/common/builder.py\", line 172:\n    sage: b = builder.DocBuilder('tutorial')\nException raised:\n    Traceback (most recent call last):\n      File \"/share/apps/contrib/sage-4.3.3/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/share/apps/contrib/sage-4.3.3/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/share/apps/contrib/sage-4.3.3/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_5[3]>\", line 1, in <module>\n        b = builder.DocBuilder('tutorial')###line 172:\n    sage: b = builder.DocBuilder('tutorial')\n      File \"/share/apps/contrib/sage-4.3.3/devel/sage/doc/common/builder.py\", line 145, in __init__\n        mkdir(os.path.join(self.dir, \"static\"))\n      File \"/share/apps/contrib/sage-4.3.3/devel/sage/doc/common/builder.py\", line 55, in mkdir\n        os.makedirs(path)\n      File \"/share/apps/contrib/sage-4.3.3/local/lib/python2.6/os.py\", line 157, in makedirs\n        mkdir(name, mode)\n    OSError: [Errno 13] Permission denied: '/share/apps/contrib/sage-4.3.3/devel/sage/doc/en/tutorial/static'\n**********************************************************************\nFile \"/share/apps/contrib/sage-4.3.3/devel/sage/doc/common/builder.py\", line 173:\n    sage: b._doctrees_dir()\nException raised:\n    Traceback (most recent call last):\n      File \"/share/apps/contrib/sage-4.3.3/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/share/apps/contrib/sage-4.3.3/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/share/apps/contrib/sage-4.3.3/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_5[4]>\", line 1, in <module>\n        b._doctrees_dir()###line 173:\n    sage: b._doctrees_dir()\n    NameError: name 'b' is not defined\n**********************************************************************\nFile \"/share/apps/contrib/sage-4.3.3/devel/sage/doc/common/builder.py\", line 185:\n    sage: b = builder.DocBuilder('tutorial')\nException raised:\n    Traceback (most recent call last):\n      File \"/share/apps/contrib/sage-4.3.3/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/share/apps/contrib/sage-4.3.3/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/share/apps/contrib/sage-4.3.3/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_6[3]>\", line 1, in <module>\n        b = builder.DocBuilder('tutorial')###line 185:\n    sage: b = builder.DocBuilder('tutorial')\n      File \"/share/apps/contrib/sage-4.3.3/devel/sage/doc/common/builder.py\", line 145, in __init__\n        mkdir(os.path.join(self.dir, \"static\"))\n      File \"/share/apps/contrib/sage-4.3.3/devel/sage/doc/common/builder.py\", line 55, in mkdir\n        os.makedirs(path)\n      File \"/share/apps/contrib/sage-4.3.3/local/lib/python2.6/os.py\", line 157, in makedirs\n        mkdir(name, mode)\n    OSError: [Errno 13] Permission denied: '/share/apps/contrib/sage-4.3.3/devel/sage/doc/en/tutorial/static'\n**********************************************************************\nFile \"/share/apps/contrib/sage-4.3.3/devel/sage/doc/common/builder.py\", line 186:\n    sage: b._output_formats()\nException raised:\n    Traceback (most recent call last):\n      File \"/share/apps/contrib/sage-4.3.3/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/share/apps/contrib/sage-4.3.3/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/share/apps/contrib/sage-4.3.3/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_6[4]>\", line 1, in <module>\n        b._output_formats()###line 186:\n    sage: b._output_formats()\n    NameError: name 'b' is not defined\n**********************************************************************\nFile \"/share/apps/contrib/sage-4.3.3/devel/sage/doc/common/builder.py\", line 209:\n    sage: b = builder.DocBuilder('tutorial')\nException raised:\n    Traceback (most recent call last):\n      File \"/share/apps/contrib/sage-4.3.3/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/share/apps/contrib/sage-4.3.3/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/share/apps/contrib/sage-4.3.3/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_7[3]>\", line 1, in <module>\n        b = builder.DocBuilder('tutorial')###line 209:\n    sage: b = builder.DocBuilder('tutorial')\n      File \"/share/apps/contrib/sage-4.3.3/devel/sage/doc/common/builder.py\", line 145, in __init__\n        mkdir(os.path.join(self.dir, \"static\"))\n      File \"/share/apps/contrib/sage-4.3.3/devel/sage/doc/common/builder.py\", line 55, in mkdir\n        os.makedirs(path)\n      File \"/share/apps/contrib/sage-4.3.3/local/lib/python2.6/os.py\", line 157, in makedirs\n        mkdir(name, mode)\n    OSError: [Errno 13] Permission denied: '/share/apps/contrib/sage-4.3.3/devel/sage/doc/en/tutorial/static'\n**********************************************************************\n4 items had failures:\n   2 of   5 in __main__.example_4\n   2 of   5 in __main__.example_5\n   2 of   5 in __main__.example_6\n   1 of   4 in __main__.example_7\n***Test Failed*** 7 failures.\nFor whitespace errors, see the file /home/rwh4s/.sage//tmp/.doctest_builder.py\n\t [6.9 s]\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8448\n\n",
    "created_at": "2010-03-05T17:13:21Z",
    "labels": [
        "component: documentation",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "doc/common/builder.py doctests write files in Sage tree",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8448",
    "user": "https://github.com/rhinton"
}
```
Assignee: mvngu

CC:  @dimpase

Keywords: builder.py, doctest, system-wide

I am using a system-wide install, so I don't have write access in the Sage tree.  When I run `sage -testall`, I get the following errors.  (More may come; it's only been running a few minutes. :-)


```
sage -t  "devel/sage/doc/common/builder.py"                 
**********************************************************************
File "/share/apps/contrib/sage-4.3.3/devel/sage/doc/common/builder.py", line 157:
    sage: b = builder.DocBuilder('tutorial')
Exception raised:
    Traceback (most recent call last):
      File "/share/apps/contrib/sage-4.3.3/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/share/apps/contrib/sage-4.3.3/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/share/apps/contrib/sage-4.3.3/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_4[3]>", line 1, in <module>
        b = builder.DocBuilder('tutorial')###line 157:
    sage: b = builder.DocBuilder('tutorial')
      File "/share/apps/contrib/sage-4.3.3/devel/sage/doc/common/builder.py", line 145, in __init__
        mkdir(os.path.join(self.dir, "static"))
      File "/share/apps/contrib/sage-4.3.3/devel/sage/doc/common/builder.py", line 55, in mkdir
        os.makedirs(path)
      File "/share/apps/contrib/sage-4.3.3/local/lib/python2.6/os.py", line 157, in makedirs
        mkdir(name, mode)
    OSError: [Errno 13] Permission denied: '/share/apps/contrib/sage-4.3.3/devel/sage/doc/en/tutorial/static'
**********************************************************************
File "/share/apps/contrib/sage-4.3.3/devel/sage/doc/common/builder.py", line 158:
    sage: b._output_dir('html')
Exception raised:
    Traceback (most recent call last):
      File "/share/apps/contrib/sage-4.3.3/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/share/apps/contrib/sage-4.3.3/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/share/apps/contrib/sage-4.3.3/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_4[4]>", line 1, in <module>
        b._output_dir('html')###line 158:
    sage: b._output_dir('html')
    NameError: name 'b' is not defined
**********************************************************************
File "/share/apps/contrib/sage-4.3.3/devel/sage/doc/common/builder.py", line 172:
    sage: b = builder.DocBuilder('tutorial')
Exception raised:
    Traceback (most recent call last):
      File "/share/apps/contrib/sage-4.3.3/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/share/apps/contrib/sage-4.3.3/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/share/apps/contrib/sage-4.3.3/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_5[3]>", line 1, in <module>
        b = builder.DocBuilder('tutorial')###line 172:
    sage: b = builder.DocBuilder('tutorial')
      File "/share/apps/contrib/sage-4.3.3/devel/sage/doc/common/builder.py", line 145, in __init__
        mkdir(os.path.join(self.dir, "static"))
      File "/share/apps/contrib/sage-4.3.3/devel/sage/doc/common/builder.py", line 55, in mkdir
        os.makedirs(path)
      File "/share/apps/contrib/sage-4.3.3/local/lib/python2.6/os.py", line 157, in makedirs
        mkdir(name, mode)
    OSError: [Errno 13] Permission denied: '/share/apps/contrib/sage-4.3.3/devel/sage/doc/en/tutorial/static'
**********************************************************************
File "/share/apps/contrib/sage-4.3.3/devel/sage/doc/common/builder.py", line 173:
    sage: b._doctrees_dir()
Exception raised:
    Traceback (most recent call last):
      File "/share/apps/contrib/sage-4.3.3/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/share/apps/contrib/sage-4.3.3/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/share/apps/contrib/sage-4.3.3/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_5[4]>", line 1, in <module>
        b._doctrees_dir()###line 173:
    sage: b._doctrees_dir()
    NameError: name 'b' is not defined
**********************************************************************
File "/share/apps/contrib/sage-4.3.3/devel/sage/doc/common/builder.py", line 185:
    sage: b = builder.DocBuilder('tutorial')
Exception raised:
    Traceback (most recent call last):
      File "/share/apps/contrib/sage-4.3.3/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/share/apps/contrib/sage-4.3.3/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/share/apps/contrib/sage-4.3.3/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_6[3]>", line 1, in <module>
        b = builder.DocBuilder('tutorial')###line 185:
    sage: b = builder.DocBuilder('tutorial')
      File "/share/apps/contrib/sage-4.3.3/devel/sage/doc/common/builder.py", line 145, in __init__
        mkdir(os.path.join(self.dir, "static"))
      File "/share/apps/contrib/sage-4.3.3/devel/sage/doc/common/builder.py", line 55, in mkdir
        os.makedirs(path)
      File "/share/apps/contrib/sage-4.3.3/local/lib/python2.6/os.py", line 157, in makedirs
        mkdir(name, mode)
    OSError: [Errno 13] Permission denied: '/share/apps/contrib/sage-4.3.3/devel/sage/doc/en/tutorial/static'
**********************************************************************
File "/share/apps/contrib/sage-4.3.3/devel/sage/doc/common/builder.py", line 186:
    sage: b._output_formats()
Exception raised:
    Traceback (most recent call last):
      File "/share/apps/contrib/sage-4.3.3/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/share/apps/contrib/sage-4.3.3/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/share/apps/contrib/sage-4.3.3/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_6[4]>", line 1, in <module>
        b._output_formats()###line 186:
    sage: b._output_formats()
    NameError: name 'b' is not defined
**********************************************************************
File "/share/apps/contrib/sage-4.3.3/devel/sage/doc/common/builder.py", line 209:
    sage: b = builder.DocBuilder('tutorial')
Exception raised:
    Traceback (most recent call last):
      File "/share/apps/contrib/sage-4.3.3/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/share/apps/contrib/sage-4.3.3/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/share/apps/contrib/sage-4.3.3/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_7[3]>", line 1, in <module>
        b = builder.DocBuilder('tutorial')###line 209:
    sage: b = builder.DocBuilder('tutorial')
      File "/share/apps/contrib/sage-4.3.3/devel/sage/doc/common/builder.py", line 145, in __init__
        mkdir(os.path.join(self.dir, "static"))
      File "/share/apps/contrib/sage-4.3.3/devel/sage/doc/common/builder.py", line 55, in mkdir
        os.makedirs(path)
      File "/share/apps/contrib/sage-4.3.3/local/lib/python2.6/os.py", line 157, in makedirs
        mkdir(name, mode)
    OSError: [Errno 13] Permission denied: '/share/apps/contrib/sage-4.3.3/devel/sage/doc/en/tutorial/static'
**********************************************************************
4 items had failures:
   2 of   5 in __main__.example_4
   2 of   5 in __main__.example_5
   2 of   5 in __main__.example_6
   1 of   4 in __main__.example_7
***Test Failed*** 7 failures.
For whitespace errors, see the file /home/rwh4s/.sage//tmp/.doctest_builder.py
	 [6.9 s]
```


Issue created by migration from https://trac.sagemath.org/ticket/8448





---

archive/issue_comments_075825.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2020-08-17T16:38:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8448",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8448#issuecomment-75825",
    "user": "https://github.com/mkoeppe"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_075826.json:
```json
{
    "body": "Outdated spkg or build system ticket, should be closed",
    "created_at": "2020-08-17T16:38:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8448",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8448#issuecomment-75826",
    "user": "https://github.com/mkoeppe"
}
```

Outdated spkg or build system ticket, should be closed



---

archive/issue_comments_075827.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2020-10-31T07:26:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8448",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8448#issuecomment-75827",
    "user": "https://github.com/mezzarobba"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_008632.json:
```json
{
    "actor": "https://github.com/fchapoton",
    "created_at": "2020-10-31T07:34:19Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8448",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8448#event-8632"
}
```



---

archive/issue_comments_075828.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2020-10-31T07:34:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8448",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8448#issuecomment-75828",
    "user": "https://github.com/fchapoton"
}
```

Resolution: invalid
