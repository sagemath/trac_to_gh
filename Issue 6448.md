# Issue 6448: darwin_utilities import issues

archive/issues_006448.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  rlm\n\nThe following is on sage.math:\n\n\n```\nsage -t  \"devel/sage-main/sage/misc/darwin_utilities.pyx\"\n**********************************************************************\nFile \"/space/rlm/sage-4.1.alpha2/devel/sage-main/sage/misc/darwin_utilities.pyx\", line 12:\n    sage: from sage.misc.darwin_utilities import darwin_memory_usage\nException raised:\n    Traceback (most recent call last):\n      File \"/space/rlm/sage-4.1.alpha2/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/space/rlm/sage-4.1.alpha2/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/space/rlm/sage-4.1.alpha2/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_0[2]>\", line 1, in <module>\n        from sage.misc.darwin_utilities import darwin_memory_usage###line 12:\n    sage: from sage.misc.darwin_utilities import darwin_memory_usage\n    ImportError: No module named darwin_utilities\n**********************************************************************\nFile \"/space/rlm/sage-4.1.alpha2/devel/sage-main/sage/misc/darwin_utilities.pyx\", line 17:\n    sage: from sage.misc.darwin_utilities import darwin_memory_usage\nException raised:\n    Traceback (most recent call last):\n      File \"/space/rlm/sage-4.1.alpha2/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/space/rlm/sage-4.1.alpha2/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/space/rlm/sage-4.1.alpha2/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_0[4]>\", line 1, in <module>\n        from sage.misc.darwin_utilities import darwin_memory_usage###line 17:\n    sage: from sage.misc.darwin_utilities import darwin_memory_usage\n    ImportError: No module named darwin_utilities\n**********************************************************************\nFile \"/space/rlm/sage-4.1.alpha2/devel/sage-main/sage/misc/darwin_utilities.pyx\", line 18:\n    sage: try:\n        if os.uname()[Integer(0)] != 'Darwin':\n            memory_usage = darwin_memory_usage()\n        else:\n            raise NotImplementedError\n    except NotImplementedError:\n        print \"NotImplementedError\"\nException raised:\n    Traceback (most recent call last):\n      File \"/space/rlm/sage-4.1.alpha2/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/space/rlm/sage-4.1.alpha2/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/space/rlm/sage-4.1.alpha2/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_0[5]>\", line 3, in <module>\n        memory_usage = darwin_memory_usage()\n    NameError: name 'darwin_memory_usage' is not defined\n**********************************************************************\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6448\n\n",
    "created_at": "2009-06-29T20:54:15Z",
    "labels": [
        "distribution",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1",
    "title": "darwin_utilities import issues",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6448",
    "user": "rlm"
}
```
Assignee: tbd

CC:  rlm

The following is on sage.math:


```
sage -t  "devel/sage-main/sage/misc/darwin_utilities.pyx"
**********************************************************************
File "/space/rlm/sage-4.1.alpha2/devel/sage-main/sage/misc/darwin_utilities.pyx", line 12:
    sage: from sage.misc.darwin_utilities import darwin_memory_usage
Exception raised:
    Traceback (most recent call last):
      File "/space/rlm/sage-4.1.alpha2/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/space/rlm/sage-4.1.alpha2/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/space/rlm/sage-4.1.alpha2/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[2]>", line 1, in <module>
        from sage.misc.darwin_utilities import darwin_memory_usage###line 12:
    sage: from sage.misc.darwin_utilities import darwin_memory_usage
    ImportError: No module named darwin_utilities
**********************************************************************
File "/space/rlm/sage-4.1.alpha2/devel/sage-main/sage/misc/darwin_utilities.pyx", line 17:
    sage: from sage.misc.darwin_utilities import darwin_memory_usage
Exception raised:
    Traceback (most recent call last):
      File "/space/rlm/sage-4.1.alpha2/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/space/rlm/sage-4.1.alpha2/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/space/rlm/sage-4.1.alpha2/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[4]>", line 1, in <module>
        from sage.misc.darwin_utilities import darwin_memory_usage###line 17:
    sage: from sage.misc.darwin_utilities import darwin_memory_usage
    ImportError: No module named darwin_utilities
**********************************************************************
File "/space/rlm/sage-4.1.alpha2/devel/sage-main/sage/misc/darwin_utilities.pyx", line 18:
    sage: try:
        if os.uname()[Integer(0)] != 'Darwin':
            memory_usage = darwin_memory_usage()
        else:
            raise NotImplementedError
    except NotImplementedError:
        print "NotImplementedError"
Exception raised:
    Traceback (most recent call last):
      File "/space/rlm/sage-4.1.alpha2/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/space/rlm/sage-4.1.alpha2/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/space/rlm/sage-4.1.alpha2/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[5]>", line 3, in <module>
        memory_usage = darwin_memory_usage()
    NameError: name 'darwin_memory_usage' is not defined
**********************************************************************
```


Issue created by migration from https://trac.sagemath.org/ticket/6448





---

archive/issue_comments_051832.json:
```json
{
    "body": "Attachment [trac_6448-darwin_utilities-doctest.patch](tarball://root/attachments/some-uuid/ticket6448/trac_6448-darwin_utilities-doctest.patch) by GeorgSWeber created at 2009-07-02 22:06:56\n\nI developed and tested this patch on OS X 10.4, and it worked (I had seen before a slightly different doctest failure than noted in the description, but nevertheless).\nFrom this, and the nature of the changes in the patch, I deduce it should work on any platform except possibly OS X 10.5.\nI can't test on the latter one, though.",
    "created_at": "2009-07-02T22:06:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6448",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6448#issuecomment-51832",
    "user": "GeorgSWeber"
}
```

Attachment [trac_6448-darwin_utilities-doctest.patch](tarball://root/attachments/some-uuid/ticket6448/trac_6448-darwin_utilities-doctest.patch) by GeorgSWeber created at 2009-07-02 22:06:56

I developed and tested this patch on OS X 10.4, and it worked (I had seen before a slightly different doctest failure than noted in the description, but nevertheless).
From this, and the nature of the changes in the patch, I deduce it should work on any platform except possibly OS X 10.5.
I can't test on the latter one, though.



---

archive/issue_comments_051833.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-07-03T01:02:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6448",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6448#issuecomment-51833",
    "user": "rlm"
}
```

Resolution: fixed
