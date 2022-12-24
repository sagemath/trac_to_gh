# Issue 9163: cygwin: output of a subtle test in expect.py differs slightly on cygwin

archive/issues_009163.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  simonking\n\n\n```\n\nsage -t  \"devel/sage/sage/interfaces/expect.py\"             \n**********************************************************************\nFile \"/home/wstein/sage-4.4.3/devel/sage/sage/interfaces/expect.py\", line 808:\n    sage: print sage0.eval(\"alarm(1); singular._expect_expr('1')\")\nExpected:\n    Control-C pressed.  Interrupting Singular. Please wait a few seconds...\n    ...\n    KeyboardInterrupt: computation timed out because alarm was set for 1 seconds\nGot:\n    ---------------------------------------------------------------------------\n    KeyboardInterrupt                         Traceback (most recent call last)\n    <BLANKLINE>\n    /home/wstein/sage-4.4.3/data/extcode/sage/<ipython console> in <module>()\n    <BLANKLINE>\n    /home/wstein/sage-4.4.3/local/lib/python2.6/site-packages/sage/interfaces/expect.pyc in _expect_expr(self, expr, timeout)\n        815             expr = self._prompt_wait\n        816         if self._expect is None:\n    --> 817             self._start()\n        818         try:\n        819             if timeout:\n    <BLANKLINE>\n    /home/wstein/sage-4.4.3/local/lib/python2.6/site-packages/sage/interfaces/singular.pyc in _start(self, alt_message)\n        373         \"\"\"\n        374         self.__libs = []\n    --> 375         Expect._start(self, alt_message)\n        376         # Load some standard libraries.\n        377         self.lib('general')   # assumed loaded by misc/constants.py\n    <BLANKLINE>\n    /home/wstein/sage-4.4.3/local/lib/python2.6/site-packages/sage/interfaces/expect.pyc in _start(self, alt_message, block_during_init)\n        447                 c = 'sage-native-execute  ssh %s \"nohup sage -cleaner\"  &'%self._server\n        448                 os.system(c)\n    --> 449             self._expect = pexpect.spawn(cmd, logfile=self.__logfile)\n        450             if self._do_cleaner():\n        451                 cleaner.cleaner(self._expect.pid, cmd)\n    <BLANKLINE>\n    /home/wstein/sage-4.4.3/local/lib/python2.6/site-packages/pexpect.pyc in __init__(self, command, args, timeout, maxread, searchwindowsize, logfile)\n        331 \n        332         self.name = '<' + ' '.join (self.args) + '>'\n    --> 333         self.__spawn()\n        334 \n        335     def __del__(self):\n    <BLANKLINE>\n    /home/wstein/sage-4.4.3/local/lib/python2.6/site-packages/pexpect.pyc in __spawn(self)\n        399 \n        400         try:\n    --> 401             self.pid, self.child_fd = pty.fork()\n        402         except OSError, e:\n        403             raise ExceptionPexpect('Pexpect: pty.fork() failed: ' + str(e))\n    <BLANKLINE>\n    /home/wstein/sage-4.4.3/local/lib/python/pty.pyc in fork()\n         93 \n         94     try:\n    ---> 95         pid, fd = os.forkpty()\n         96     except (AttributeError, OSError):\n         97         pass\n    <BLANKLINE>\n    /home/wstein/sage-4.4.3/local/lib/python2.6/site-packages/sage/misc/misc.pyc in __mysig(a, b)\n       1690 __alarm_time=0\n       1691 def __mysig(a,b):\n    -> 1692     raise KeyboardInterrupt, \"computation timed out because alarm was set for %s seconds\"%__alarm_time\n       1693 \n       1694 def alarm(seconds):\n    <BLANKLINE>\n    KeyboardInterrupt: computation timed out because alarm was set for 1 seconds\n**********************************************************************\n1 items had failures:\n   1 of  10 in __main__.example_15\n***Test Failed*** 1 failures.\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9163\n\n",
    "created_at": "2010-06-07T04:00:41Z",
    "labels": [
        "Cygwin",
        "major",
        "bug"
    ],
    "title": "cygwin: output of a subtle test in expect.py differs slightly on cygwin",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9163",
    "user": "was"
}
```
Assignee: tbd

CC:  simonking


```

sage -t  "devel/sage/sage/interfaces/expect.py"             
**********************************************************************
File "/home/wstein/sage-4.4.3/devel/sage/sage/interfaces/expect.py", line 808:
    sage: print sage0.eval("alarm(1); singular._expect_expr('1')")
Expected:
    Control-C pressed.  Interrupting Singular. Please wait a few seconds...
    ...
    KeyboardInterrupt: computation timed out because alarm was set for 1 seconds
Got:
    ---------------------------------------------------------------------------
    KeyboardInterrupt                         Traceback (most recent call last)
    <BLANKLINE>
    /home/wstein/sage-4.4.3/data/extcode/sage/<ipython console> in <module>()
    <BLANKLINE>
    /home/wstein/sage-4.4.3/local/lib/python2.6/site-packages/sage/interfaces/expect.pyc in _expect_expr(self, expr, timeout)
        815             expr = self._prompt_wait
        816         if self._expect is None:
    --> 817             self._start()
        818         try:
        819             if timeout:
    <BLANKLINE>
    /home/wstein/sage-4.4.3/local/lib/python2.6/site-packages/sage/interfaces/singular.pyc in _start(self, alt_message)
        373         """
        374         self.__libs = []
    --> 375         Expect._start(self, alt_message)
        376         # Load some standard libraries.
        377         self.lib('general')   # assumed loaded by misc/constants.py
    <BLANKLINE>
    /home/wstein/sage-4.4.3/local/lib/python2.6/site-packages/sage/interfaces/expect.pyc in _start(self, alt_message, block_during_init)
        447                 c = 'sage-native-execute  ssh %s "nohup sage -cleaner"  &'%self._server
        448                 os.system(c)
    --> 449             self._expect = pexpect.spawn(cmd, logfile=self.__logfile)
        450             if self._do_cleaner():
        451                 cleaner.cleaner(self._expect.pid, cmd)
    <BLANKLINE>
    /home/wstein/sage-4.4.3/local/lib/python2.6/site-packages/pexpect.pyc in __init__(self, command, args, timeout, maxread, searchwindowsize, logfile)
        331 
        332         self.name = '<' + ' '.join (self.args) + '>'
    --> 333         self.__spawn()
        334 
        335     def __del__(self):
    <BLANKLINE>
    /home/wstein/sage-4.4.3/local/lib/python2.6/site-packages/pexpect.pyc in __spawn(self)
        399 
        400         try:
    --> 401             self.pid, self.child_fd = pty.fork()
        402         except OSError, e:
        403             raise ExceptionPexpect('Pexpect: pty.fork() failed: ' + str(e))
    <BLANKLINE>
    /home/wstein/sage-4.4.3/local/lib/python/pty.pyc in fork()
         93 
         94     try:
    ---> 95         pid, fd = os.forkpty()
         96     except (AttributeError, OSError):
         97         pass
    <BLANKLINE>
    /home/wstein/sage-4.4.3/local/lib/python2.6/site-packages/sage/misc/misc.pyc in __mysig(a, b)
       1690 __alarm_time=0
       1691 def __mysig(a,b):
    -> 1692     raise KeyboardInterrupt, "computation timed out because alarm was set for %s seconds"%__alarm_time
       1693 
       1694 def alarm(seconds):
    <BLANKLINE>
    KeyboardInterrupt: computation timed out because alarm was set for 1 seconds
**********************************************************************
1 items had failures:
   1 of  10 in __main__.example_15
***Test Failed*** 1 failures.
```


Issue created by migration from https://trac.sagemath.org/ticket/9163





---

archive/issue_comments_085541.json:
```json
{
    "body": "Changing component from cygwin to interfaces.",
    "created_at": "2010-11-13T10:19:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9163",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9163#issuecomment-85541",
    "user": "jdemeyer"
}
```

Changing component from cygwin to interfaces.



---

archive/issue_comments_085542.json:
```json
{
    "body": "Changing keywords from \"\" to \"cygwin osx expect doctest\".",
    "created_at": "2010-11-13T10:19:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9163",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9163#issuecomment-85542",
    "user": "jdemeyer"
}
```

Changing keywords from "" to "cygwin osx expect doctest".



---

archive/issue_comments_085543.json:
```json
{
    "body": "Changing assignee from tbd to was.",
    "created_at": "2010-11-13T10:19:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9163",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9163#issuecomment-85543",
    "user": "jdemeyer"
}
```

Changing assignee from tbd to was.



---

archive/issue_comments_085544.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2010-11-19T19:30:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9163",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9163#issuecomment-85544",
    "user": "jdemeyer"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_085545.json:
```json
{
    "body": "Does this happen because the interface might be slow to start up?\n\nShould we move the lines\n\n```python\n        if self._expect is None:\n            self._start()\n```\n\nin `sage.interfaces.expect.Expect._expect_expr` to inside its outermost `try` block?",
    "created_at": "2010-11-24T12:23:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9163",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9163#issuecomment-85545",
    "user": "mpatel"
}
```

Does this happen because the interface might be slow to start up?

Should we move the lines

```python
        if self._expect is None:
            self._start()
```

in `sage.interfaces.expect.Expect._expect_expr` to inside its outermost `try` block?



---

archive/issue_comments_085546.json:
```json
{
    "body": "Or remove \"Control-C pressed.  Interrupting Singular. Please wait a few seconds...\" from the expected output?",
    "created_at": "2010-11-24T12:28:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9163",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9163#issuecomment-85546",
    "user": "mpatel"
}
```

Or remove "Control-C pressed.  Interrupting Singular. Please wait a few seconds..." from the expected output?



---

archive/issue_comments_085547.json:
```json
{
    "body": "Changing assignee from was to jdemeyer.",
    "created_at": "2010-12-14T19:45:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9163",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9163#issuecomment-85547",
    "user": "jdemeyer"
}
```

Changing assignee from was to jdemeyer.



---

archive/issue_comments_085548.json:
```json
{
    "body": "The problem is with the Singular interface, see #10476.",
    "created_at": "2010-12-14T19:45:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9163",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9163#issuecomment-85548",
    "user": "jdemeyer"
}
```

The problem is with the Singular interface, see #10476.



---

archive/issue_comments_085549.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-12-14T19:47:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9163",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9163#issuecomment-85549",
    "user": "jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_085550.json:
```json
{
    "body": "Apart from this, `expect.py` is a **huge mess**...",
    "created_at": "2010-12-14T20:02:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9163",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9163#issuecomment-85550",
    "user": "jdemeyer"
}
```

Apart from this, `expect.py` is a **huge mess**...



---

archive/issue_comments_085551.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-12-15T08:42:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9163",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9163#issuecomment-85551",
    "user": "jdemeyer"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_085552.json:
```json
{
    "body": "Attachment [9163_expect_expr.patch](tarball://root/attachments/some-uuid/ticket9163/9163_expect_expr.patch) by jdemeyer created at 2010-12-16 20:37:07",
    "created_at": "2010-12-16T20:37:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9163",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9163#issuecomment-85552",
    "user": "jdemeyer"
}
```

Attachment [9163_expect_expr.patch](tarball://root/attachments/some-uuid/ticket9163/9163_expect_expr.patch) by jdemeyer created at 2010-12-16 20:37:07



---

archive/issue_comments_085553.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-12-16T20:37:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9163",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9163#issuecomment-85553",
    "user": "jdemeyer"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_085554.json:
```json
{
    "body": "I cannot test this on Cygwin since I don't have a build right now.  I do have one close to completion, but it fails due to #10247.",
    "created_at": "2010-12-17T14:54:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9163",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9163#issuecomment-85554",
    "user": "mhansen"
}
```

I cannot test this on Cygwin since I don't have a build right now.  I do have one close to completion, but it fails due to #10247.



---

archive/issue_comments_085555.json:
```json
{
    "body": "I agree that Singular isn't a good test for the expect interfaces since it is quite finicky with being interrupted/restarting. Improving the Singular interface will be pursued in #10247. In the meantime, positive review for this ticket.",
    "created_at": "2011-01-03T11:43:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9163",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9163#issuecomment-85555",
    "user": "vbraun"
}
```

I agree that Singular isn't a good test for the expect interfaces since it is quite finicky with being interrupted/restarting. Improving the Singular interface will be pursued in #10247. In the meantime, positive review for this ticket.



---

archive/issue_comments_085556.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-01-03T11:43:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9163",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9163#issuecomment-85556",
    "user": "vbraun"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_085557.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-01-07T19:16:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9163",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9163#issuecomment-85557",
    "user": "jdemeyer"
}
```

Resolution: fixed
