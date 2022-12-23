# Issue 9826: Intermittent doctest failure in sage/interfaces/psage.py

Issue created by migration from https://trac.sagemath.org/ticket/9827

Original creator: mpatel

Original creation time: 2010-08-28 00:15:05

Assignee: mvngu

Reported by Justin C. Walker on [sage-release](http://groups.google.com/group/sage-release/browse_thread/thread/b2827cba9319bfed/4327cb6c3f565890#4327cb6c3f565890) (scroll down the thread for replies):

```
Upgraded from 4.5.3.a1, w/o problems.  Ran 'ptestlong', and one test failed.  Failure noted below.  I reran the test by hand and it passed.  Mac OS X, 10.5.8, Dual Quad Xeon.
```



```python
sage -t  -long devel/sage/sage/interfaces/psage.py
**********************************************************************
File "/Users/Sage/sage-4.5.3.alpha1/devel/sage-main/sage/interfaces/psage.py", line 35:
     sage: print "ignore this";  w       # random output
Exception raised:
     Traceback (most recent call last):
       File "/Users/Sage/sage-4.5.3.alpha1/local/bin/ncadoctest.py", line 1231, in run_one_test
         self.run_one_example(test, example, filename, compileflags)
       File "/Users/Sage/sage-4.5.3.alpha1/local/bin/sagedoctest.py", line 38, in run_one_example
         OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
       File "/Users/Sage/sage-4.5.3.alpha1/local/bin/ncadoctest.py", line 1172, in run_one_example
         compileflags, 1) in test.globs
       File "<doctest __main__.example_0[5]>", line 1, in <module>
         print "ignore this";  w       # random output###line 35:
     sage: print "ignore this";  w       # random output
       File "/Users/Sage/sage-4.5.3.alpha1/local/lib/python/site-packages/sage/misc/displayhook.py", line 174, in displayhook
         print_obj(sys.stdout, obj)
       File "/Users/Sage/sage-4.5.3.alpha1/local/lib/python/site-packages/sage/misc/displayhook.py", line 142, in print_obj
         print >>out_stream, `obj`
       File "/Users/Sage/sage-4.5.3.alpha1/local/lib/python/site-packages/sage/interfaces/expect.py", line 1670, in __repr__
         s =  s.replace(self._name, self.__dict__['__custom_name'])
     KeyError: '__custom_name' 
```


See [this reply](http://groups.google.com/group/sage-release/browse_thread/thread/b2827cba9319bfed/14beffeda6842d4b#14beffeda6842d4b) (and possible follow-ups) for batch-testing results for `psage.py`.  The problem may be in `SAGE_LOCAL/bin/sage-test` and/or `sage-doctest`.

Distantly related: #1991.


---

Comment by mpatel created at 2010-08-28 00:15:58

Near the top of `sage/interfaces/psage.py` is a possibly relevant note:

```
BUG -- currently non-idle PSage subprocesses do not stop when
\sage exits.  I would very much like to fix this but don't know how.
```



---

Comment by roed created at 2013-03-14 21:49:16

Is this still relevant after #12415?


---

Comment by roed created at 2013-03-28 22:16:14

Changing assignee from mvngu to was.


---

Comment by roed created at 2013-03-28 22:16:14

I don't think this has to do with doctesting...


---

Comment by roed created at 2013-03-28 22:16:14

Changing component from doctest to interfaces.


---

Attachment


---

Comment by jdemeyer created at 2013-04-05 13:27:25

Changing status from new to needs_review.


---

Comment by ppurka created at 2014-07-20 03:48:56

I too ran into intermittent doctest failures in #12061


---

Comment by chapoton created at 2014-10-21 15:22:45

New commits:


---

Comment by git created at 2014-10-21 15:25:25

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by chapoton created at 2014-10-22 08:42:37

Looks good to me.


---

Comment by chapoton created at 2014-10-22 08:42:37

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2014-10-23 11:17:01

Resolution: fixed
