# Issue 9894: Doctest error raised by os.fork in sage/parallel/decorate.py

Issue created by migration from Trac.

Original creator: mpatel

Original creation time: 2010-09-11 00:38:52

Assignee: drkirkby

CC:  dimpase

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


---

Comment by mpatel created at 2010-09-11 00:39:37

Will adding swap space help?


---

Comment by mkoeppe created at 2020-07-08 16:51:35

Changing status from new to needs_review.


---

Comment by mkoeppe created at 2020-07-08 16:51:35

Outdated, should be closed


---

Comment by @mwageringel created at 2020-08-13 20:24:41

Changing status from needs_review to positive_review.


---

Comment by chapoton created at 2020-08-17 18:38:27

Resolution: invalid
