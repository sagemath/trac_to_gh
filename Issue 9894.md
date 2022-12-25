# Issue 9894: Doctest error raised by os.fork in sage/parallel/decorate.py

archive/issues_009894.json:
```json
{
    "body": "Assignee: drkirkby\n\nCC:  @dimpase\n\nDavid Kirkby [comment:ticket:9449:7 reported this previously] at #9449:\n\n```python\nsage -t  -long devel/sage/sage/parallel/decorate.py\n**********************************************************************\nFile \"/tmp/kirkby/sage-4.5.alpha4/devel/sage-testing/sage/parallel/decorate.py\", line 152:\n    sage: v = list(f([1,2,4])); v.sort(); v\nException raised:\n    Traceback (most recent call last):\n      File \"/tmp/kirkby/sage-4.5.alpha4/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/tmp/kirkby/sage-4.5.alpha4/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/tmp/kirkby/sage-4.5.alpha4/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_4[9]>\", line 1, in <module>\n        v = list(f([Integer(1),Integer(2),Integer(4)])); v.sort(); v###line 152:\n    sage: v = list(f([1,2,4])); v.sort(); v\n      File \"/tmp/kirkby/sage-4.5.alpha4/local/lib/python/site-packages/sage/parallel/multiprocessing_sage.py\", line 64, in parallel_iter\n        p = Pool(processes)\n      File \"/tmp/kirkby/sage-4.5.alpha4/local/lib/python2.6/multiprocessing/__init__.py\", line 227, in Pool\n        return Pool(processes, initializer, initargs)\n      File \"/tmp/kirkby/sage-4.5.alpha4/local/lib/python2.6/multiprocessing/pool.py\", line 104, in __init__\n        w.start()\n      File \"/tmp/kirkby/sage-4.5.alpha4/local/lib/python2.6/multiprocessing/process.py\", line 104, in start\n        self._popen = Popen(self)\n      File \"/tmp/kirkby/sage-4.5.alpha4/local/lib/python2.6/multiprocessing/forking.py\", line 94, in __init__\n        self.pid = os.fork()\n    OSError: [Errno 12] Not enough space\n```\n\nAccording to [this page](https://defect.opensolaris.org/bz/show_bug.cgi?id=2297), insufficient free memory is the problem.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9895\n\n",
    "created_at": "2010-09-11T00:38:52Z",
    "labels": [
        "component: porting: solaris",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Doctest error raised by os.fork in sage/parallel/decorate.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9894",
    "user": "https://github.com/qed777"
}
```
Assignee: drkirkby

CC:  @dimpase

David Kirkby [comment:ticket:9449:7 reported this previously] at #9449:

```python
sage -t  -long devel/sage/sage/parallel/decorate.py
**********************************************************************
File "/tmp/kirkby/sage-4.5.alpha4/devel/sage-testing/sage/parallel/decorate.py", line 152:
    sage: v = list(f([1,2,4])); v.sort(); v
Exception raised:
    Traceback (most recent call last):
      File "/tmp/kirkby/sage-4.5.alpha4/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/tmp/kirkby/sage-4.5.alpha4/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/tmp/kirkby/sage-4.5.alpha4/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_4[9]>", line 1, in <module>
        v = list(f([Integer(1),Integer(2),Integer(4)])); v.sort(); v###line 152:
    sage: v = list(f([1,2,4])); v.sort(); v
      File "/tmp/kirkby/sage-4.5.alpha4/local/lib/python/site-packages/sage/parallel/multiprocessing_sage.py", line 64, in parallel_iter
        p = Pool(processes)
      File "/tmp/kirkby/sage-4.5.alpha4/local/lib/python2.6/multiprocessing/__init__.py", line 227, in Pool
        return Pool(processes, initializer, initargs)
      File "/tmp/kirkby/sage-4.5.alpha4/local/lib/python2.6/multiprocessing/pool.py", line 104, in __init__
        w.start()
      File "/tmp/kirkby/sage-4.5.alpha4/local/lib/python2.6/multiprocessing/process.py", line 104, in start
        self._popen = Popen(self)
      File "/tmp/kirkby/sage-4.5.alpha4/local/lib/python2.6/multiprocessing/forking.py", line 94, in __init__
        self.pid = os.fork()
    OSError: [Errno 12] Not enough space
```

According to [this page](https://defect.opensolaris.org/bz/show_bug.cgi?id=2297), insufficient free memory is the problem.

Issue created by migration from https://trac.sagemath.org/ticket/9895





---

archive/issue_comments_098010.json:
```json
{
    "body": "Will adding swap space help?",
    "created_at": "2010-09-11T00:39:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9894",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9894#issuecomment-98010",
    "user": "https://github.com/qed777"
}
```

Will adding swap space help?



---

archive/issue_comments_098011.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2020-07-08T16:51:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9894",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9894#issuecomment-98011",
    "user": "https://github.com/mkoeppe"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_098012.json:
```json
{
    "body": "Outdated, should be closed",
    "created_at": "2020-07-08T16:51:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9894",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9894#issuecomment-98012",
    "user": "https://github.com/mkoeppe"
}
```

Outdated, should be closed



---

archive/issue_comments_098013.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2020-08-13T20:24:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9894",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9894#issuecomment-98013",
    "user": "https://github.com/mwageringel"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_098014.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2020-08-17T18:38:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9894",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9894#issuecomment-98014",
    "user": "https://github.com/fchapoton"
}
```

Resolution: invalid
