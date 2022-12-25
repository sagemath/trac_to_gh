# Issue 9826: Intermittent doctest failure in sage/interfaces/psage.py

archive/issues_009826.json:
```json
{
    "body": "Assignee: mvngu\n\nReported by Justin C. Walker on [sage-release](http://groups.google.com/group/sage-release/browse_thread/thread/b2827cba9319bfed/4327cb6c3f565890#4327cb6c3f565890) (scroll down the thread for replies):\n\n```\nUpgraded from 4.5.3.a1, w/o problems.  Ran 'ptestlong', and one test failed.  Failure noted below.  I reran the test by hand and it passed.  Mac OS X, 10.5.8, Dual Quad Xeon.\n```\n\n\n\n```python\nsage -t  -long devel/sage/sage/interfaces/psage.py\n**********************************************************************\nFile \"/Users/Sage/sage-4.5.3.alpha1/devel/sage-main/sage/interfaces/psage.py\", line 35:\n     sage: print \"ignore this\";  w       # random output\nException raised:\n     Traceback (most recent call last):\n       File \"/Users/Sage/sage-4.5.3.alpha1/local/bin/ncadoctest.py\", line 1231, in run_one_test\n         self.run_one_example(test, example, filename, compileflags)\n       File \"/Users/Sage/sage-4.5.3.alpha1/local/bin/sagedoctest.py\", line 38, in run_one_example\n         OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n       File \"/Users/Sage/sage-4.5.3.alpha1/local/bin/ncadoctest.py\", line 1172, in run_one_example\n         compileflags, 1) in test.globs\n       File \"<doctest __main__.example_0[5]>\", line 1, in <module>\n         print \"ignore this\";  w       # random output###line 35:\n     sage: print \"ignore this\";  w       # random output\n       File \"/Users/Sage/sage-4.5.3.alpha1/local/lib/python/site-packages/sage/misc/displayhook.py\", line 174, in displayhook\n         print_obj(sys.stdout, obj)\n       File \"/Users/Sage/sage-4.5.3.alpha1/local/lib/python/site-packages/sage/misc/displayhook.py\", line 142, in print_obj\n         print >>out_stream, `obj`\n       File \"/Users/Sage/sage-4.5.3.alpha1/local/lib/python/site-packages/sage/interfaces/expect.py\", line 1670, in __repr__\n         s =  s.replace(self._name, self.__dict__['__custom_name'])\n     KeyError: '__custom_name' \n```\n\n\nSee [this reply](http://groups.google.com/group/sage-release/browse_thread/thread/b2827cba9319bfed/14beffeda6842d4b#14beffeda6842d4b) (and possible follow-ups) for batch-testing results for `psage.py`.  The problem may be in `SAGE_LOCAL/bin/sage-test` and/or `sage-doctest`.\n\nDistantly related: #1991.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9827\n\n",
    "created_at": "2010-08-28T00:15:05Z",
    "labels": [
        "component: doctest",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "Intermittent doctest failure in sage/interfaces/psage.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9826",
    "user": "https://github.com/qed777"
}
```
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

Issue created by migration from https://trac.sagemath.org/ticket/9827





---

archive/issue_comments_096772.json:
```json
{
    "body": "Near the top of `sage/interfaces/psage.py` is a possibly relevant note:\n\n```\nBUG -- currently non-idle PSage subprocesses do not stop when\n\\sage exits.  I would very much like to fix this but don't know how.\n```\n",
    "created_at": "2010-08-28T00:15:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9826",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9826#issuecomment-96772",
    "user": "https://github.com/qed777"
}
```

Near the top of `sage/interfaces/psage.py` is a possibly relevant note:

```
BUG -- currently non-idle PSage subprocesses do not stop when
\sage exits.  I would very much like to fix this but don't know how.
```




---

archive/issue_comments_096773.json:
```json
{
    "body": "Is this still relevant after #12415?",
    "created_at": "2013-03-14T21:49:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9826",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9826#issuecomment-96773",
    "user": "https://github.com/roed314"
}
```

Is this still relevant after #12415?



---

archive/issue_comments_096774.json:
```json
{
    "body": "Changing assignee from mvngu to @williamstein.",
    "created_at": "2013-03-28T22:16:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9826",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9826#issuecomment-96774",
    "user": "https://github.com/roed314"
}
```

Changing assignee from mvngu to @williamstein.



---

archive/issue_comments_096775.json:
```json
{
    "body": "I don't think this has to do with doctesting...",
    "created_at": "2013-03-28T22:16:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9826",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9826#issuecomment-96775",
    "user": "https://github.com/roed314"
}
```

I don't think this has to do with doctesting...



---

archive/issue_comments_096776.json:
```json
{
    "body": "Changing component from doctest to interfaces.",
    "created_at": "2013-03-28T22:16:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9826",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9826#issuecomment-96776",
    "user": "https://github.com/roed314"
}
```

Changing component from doctest to interfaces.



---

archive/issue_comments_096777.json:
```json
{
    "body": "Attachment [9827_custom_name.patch](tarball://root/attachments/some-uuid/ticket9827/9827_custom_name.patch) by @jdemeyer created at 2013-04-05 13:27:11",
    "created_at": "2013-04-05T13:27:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9826",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9826#issuecomment-96777",
    "user": "https://github.com/jdemeyer"
}
```

Attachment [9827_custom_name.patch](tarball://root/attachments/some-uuid/ticket9827/9827_custom_name.patch) by @jdemeyer created at 2013-04-05 13:27:11



---

archive/issue_comments_096778.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2013-04-05T13:27:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9826",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9826#issuecomment-96778",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_096779.json:
```json
{
    "body": "I too ran into intermittent doctest failures in #12061",
    "created_at": "2014-07-20T03:48:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9826",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9826#issuecomment-96779",
    "user": "https://github.com/ppurka"
}
```

I too ran into intermittent doctest failures in #12061



---

archive/issue_comments_096780.json:
```json
{
    "body": "New commits:",
    "created_at": "2014-10-21T15:22:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9826",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9826#issuecomment-96780",
    "user": "https://github.com/fchapoton"
}
```

New commits:



---

archive/issue_comments_096781.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2014-10-21T15:25:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9826",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9826#issuecomment-96781",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_096782.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2014-10-22T08:42:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9826",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9826#issuecomment-96782",
    "user": "https://github.com/fchapoton"
}
```

Looks good to me.



---

archive/issue_comments_096783.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2014-10-22T08:42:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9826",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9826#issuecomment-96783",
    "user": "https://github.com/fchapoton"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_009949.json:
```json
{
    "actor": "https://github.com/vbraun",
    "created_at": "2014-10-23T11:17:01Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9826",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9826#event-9949"
}
```



---

archive/issue_comments_096784.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2014-10-23T11:17:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9826",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9826#issuecomment-96784",
    "user": "https://github.com/vbraun"
}
```

Resolution: fixed
