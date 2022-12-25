# Issue 8471: Upgrade or patch pexpect

archive/issues_008471.json:
```json
{
    "body": "Assignee: @williamstein\n\nKeywords: pexpect\n\nSpecifying the full path of a command to `Expect` hits a bug in the `pexpect` module shipped with Sage:\n\n```\nkarkwa: which sage\n/home/saliola/Applications/bin/sage\n\nkarkwa: sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: from sage.interfaces.expect import Expect\nsage: s = Expect('sage', 'sage> ', command='/home/saliola/Applications/bin/sage')\nsage: s.is_running()\nFalse\nsage: s._start()\n---------------------------------------------------------------------------\nUnboundLocalError                         Traceback (most recent call last)\n| Sage Version 4.3.3, Release Date: 2010-02-21                       |\n| Type notebook() for the GUI, and license() for information.        |\n/home/saliola/Applications/sage-4.3.3/data/extcode/sage/<ipython console> in <module>()\n\n/home/saliola/Applications/sage-4.3.3/local/lib/python2.6/site-packages/sage/interfaces/expect.pyc in _start(self, alt_message, block_during_init)\n    447                 c = 'sage-native-execute  ssh %s \"nohup sage -cleaner\"  &'%self._server\n    448                 os.system(c)\n--> 449             self._expect = pexpect.spawn(cmd, logfile=self.__logfile)\n    450             if self._do_cleaner():\n    451                 cleaner.cleaner(self._expect.pid, cmd)\n\n/home/saliola/Applications/sage-4.3.3/local/lib/python2.6/site-packages/pexpect.pyc in __init__(self, command, args, timeout, maxread, searchwindowsize, logfile)\n    324             self.command = command\n    325\n--> 326         command_with_path = which(self.command)\n    327         if command_with_path == None:\n    328             raise ExceptionPexpect ('The command was not found or was not executable: %s.' % self.command)\n\n/home/saliola/Applications/sage-4.3.3/local/lib/python2.6/site-packages/pexpect.pyc in which(filename)\n   1131     # Special case where filename already contains a path.\n\n   1132     if os.path.dirname(filename) != '':\n-> 1133         if os.access (filename, os.X_OK) and not os.path.isdir(f):\n   1134             return filename\n   1135\n\nUnboundLocalError: local variable 'f' referenced before assignment\nsage: \n```\n\nNote that this is a bug in the `pexpect` Python module shipped with Sage.\n\n```\nsage: import pexpect\nsage: pexpect.__version__\n'2.0'\n```\n\nIt appears to be fixed in the newest version of `pexpect` (version 2.3).\n\nShould we patch `pexpect` or upgrade?\n\nIssue created by migration from https://trac.sagemath.org/ticket/8471\n\n",
    "created_at": "2010-03-07T02:47:33Z",
    "labels": [
        "component: interfaces",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Upgrade or patch pexpect",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8471",
    "user": "https://github.com/saliola"
}
```
Assignee: @williamstein

Keywords: pexpect

Specifying the full path of a command to `Expect` hits a bug in the `pexpect` module shipped with Sage:

```
karkwa: which sage
/home/saliola/Applications/bin/sage

karkwa: sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: from sage.interfaces.expect import Expect
sage: s = Expect('sage', 'sage> ', command='/home/saliola/Applications/bin/sage')
sage: s.is_running()
False
sage: s._start()
---------------------------------------------------------------------------
UnboundLocalError                         Traceback (most recent call last)
| Sage Version 4.3.3, Release Date: 2010-02-21                       |
| Type notebook() for the GUI, and license() for information.        |
/home/saliola/Applications/sage-4.3.3/data/extcode/sage/<ipython console> in <module>()

/home/saliola/Applications/sage-4.3.3/local/lib/python2.6/site-packages/sage/interfaces/expect.pyc in _start(self, alt_message, block_during_init)
    447                 c = 'sage-native-execute  ssh %s "nohup sage -cleaner"  &'%self._server
    448                 os.system(c)
--> 449             self._expect = pexpect.spawn(cmd, logfile=self.__logfile)
    450             if self._do_cleaner():
    451                 cleaner.cleaner(self._expect.pid, cmd)

/home/saliola/Applications/sage-4.3.3/local/lib/python2.6/site-packages/pexpect.pyc in __init__(self, command, args, timeout, maxread, searchwindowsize, logfile)
    324             self.command = command
    325
--> 326         command_with_path = which(self.command)
    327         if command_with_path == None:
    328             raise ExceptionPexpect ('The command was not found or was not executable: %s.' % self.command)

/home/saliola/Applications/sage-4.3.3/local/lib/python2.6/site-packages/pexpect.pyc in which(filename)
   1131     # Special case where filename already contains a path.

   1132     if os.path.dirname(filename) != '':
-> 1133         if os.access (filename, os.X_OK) and not os.path.isdir(f):
   1134             return filename
   1135

UnboundLocalError: local variable 'f' referenced before assignment
sage: 
```

Note that this is a bug in the `pexpect` Python module shipped with Sage.

```
sage: import pexpect
sage: pexpect.__version__
'2.0'
```

It appears to be fixed in the newest version of `pexpect` (version 2.3).

Should we patch `pexpect` or upgrade?

Issue created by migration from https://trac.sagemath.org/ticket/8471





---

archive/issue_comments_076177.json:
```json
{
    "body": "We discussed this a bit on sage-devel:\n[http://groups.google.com/group/sage-devel/browse_thread/thread/8213950ab1abbeb2](http://groups.google.com/group/sage-devel/browse_thread/thread/8213950ab1abbeb2)\n\nSome highlights:\n\n- William Stein pointed out that pexpect was rewritten after 2.0 and has had some performance issues; it is worth trying the latest version of pexpect to see if the situation has improved.\n\n- Robert Bradshaw pointed out that we need to add a blurb to pexpect's SPKG.txt explaining this issue.\n\nSo these should be addressed appropriately by this ticket.",
    "created_at": "2010-03-10T23:49:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8471",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8471#issuecomment-76177",
    "user": "https://github.com/saliola"
}
```

We discussed this a bit on sage-devel:
[http://groups.google.com/group/sage-devel/browse_thread/thread/8213950ab1abbeb2](http://groups.google.com/group/sage-devel/browse_thread/thread/8213950ab1abbeb2)

Some highlights:

- William Stein pointed out that pexpect was rewritten after 2.0 and has had some performance issues; it is worth trying the latest version of pexpect to see if the situation has improved.

- Robert Bradshaw pointed out that we need to add a blurb to pexpect's SPKG.txt explaining this issue.

So these should be addressed appropriately by this ticket.



---

archive/issue_comments_076178.json:
```json
{
    "body": "Changing assignee from @williamstein to @saliola.",
    "created_at": "2010-03-10T23:49:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8471",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8471#issuecomment-76178",
    "user": "https://github.com/saliola"
}
```

Changing assignee from @williamstein to @saliola.



---

archive/issue_comments_076179.json:
```json
{
    "body": "The `gap3.py` file at #8380 contains a reference to this ticket. When this issues is resolved, the comment in that file should be changed appropriately.",
    "created_at": "2010-05-11T21:38:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8471",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8471#issuecomment-76179",
    "user": "https://github.com/saliola"
}
```

The `gap3.py` file at #8380 contains a reference to this ticket. When this issues is resolved, the comment in that file should be changed appropriately.



---

archive/issue_events_020340.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8471",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8471#event-20340"
}
```



---

archive/issue_events_020341.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8471",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8471#event-20341"
}
```



---

archive/issue_events_020342.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8471",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8471#event-20342"
}
```



---

archive/issue_events_020343.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8471",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8471#event-20343"
}
```



---

archive/issue_events_020344.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8471",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8471#event-20344"
}
```



---

archive/issue_events_020345.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8471",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8471#event-20345"
}
```



---

archive/issue_events_020346.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8471",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8471#event-20346"
}
```



---

archive/issue_events_020347.json:
```json
{
    "actor": "https://github.com/nexttime",
    "created_at": "2015-05-07T03:07:43Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8471",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8471#event-20347"
}
```



---

archive/issue_events_020348.json:
```json
{
    "actor": "https://github.com/nexttime",
    "created_at": "2015-05-07T03:07:43Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8471",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8471#event-20348"
}
```



---

archive/issue_comments_076180.json:
```json
{
    "body": "Duplicate of #10295.",
    "created_at": "2015-05-07T03:07:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8471",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8471#issuecomment-76180",
    "user": "https://github.com/nexttime"
}
```

Duplicate of #10295.



---

archive/issue_comments_076181.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2015-05-07T03:07:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8471",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8471#issuecomment-76181",
    "user": "https://github.com/nexttime"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_076182.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2015-05-08T16:31:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8471",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8471#issuecomment-76182",
    "user": "https://github.com/videlec"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_076183.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2015-05-19T06:42:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8471",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8471#issuecomment-76183",
    "user": "https://github.com/vbraun"
}
```

Resolution: duplicate



---

archive/issue_events_020349.json:
```json
{
    "actor": "https://github.com/vbraun",
    "created_at": "2015-05-19T06:42:28Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8471",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8471#event-20349"
}
```
