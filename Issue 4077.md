# Issue 4077: notebook - ReactorNotRunning error consistently seen in sage-3.1.2.rc0

archive/issues_004077.json:
```json
{
    "body": "Assignee: boothby\n\nTraceback when I hit CLTRL-C to stop the notebook. \n\nThis is happening in sage-3.1.2.rc0 with and without the spkg at #4074.\n\n\n```\n2008-09-08 05:45:38-0700 [-] Log opened.\n2008-09-08 05:45:38-0700 [-] twistd 8.1.0 (/home/tclemans/sage-3.1.2.rc0/local/bin/python 2.5.2) starting up\n2008-09-08 05:45:38-0700 [-] reactor class: <class 'twisted.internet.selectreactor.SelectReactor'>\n2008-09-08 05:45:38-0700 [-] twisted.web2.channel.http.HTTPFactory starting on 8999\n2008-09-08 05:45:38-0700 [-] Starting factory <twisted.web2.channel.http.HTTPFactory instance at 0x2b779155d9e0>\n2008-09-08 05:45:49-0700 [-] Saving notebook...\n2008-09-08 05:45:49-0700 [-] Notebook cleanly saved.\n2008-09-08 05:45:49-0700 [-] Saving notebook...\n2008-09-08 05:45:49-0700 [-] Unhandled Error\n        Traceback (most recent call last):\n          File \"/home/tclemans/sage-3.1.2.rc0/local/lib/python2.5/site-packages/Twisted-8.1.0-py2.5-linux-x86_64.egg/twisted/internet/base.py\", line 1048, in run\n            self.mainLoop()\n          File \"/home/tclemans/sage-3.1.2.rc0/local/lib/python2.5/site-packages/Twisted-8.1.0-py2.5-linux-x86_64.egg/twisted/internet/base.py\", line 1057, in mainLoop\n            self.runUntilCurrent()\n          File \"/home/tclemans/sage-3.1.2.rc0/local/lib/python2.5/site-packages/Twisted-8.1.0-py2.5-linux-x86_64.egg/twisted/internet/base.py\", line 705, in runUntilCurrent\n            call.func(*call.args, **call.kw)\n          File \"/home/tclemans/sage-3.1.2.rc0/local/lib/python2.5/site-packages/Twisted-8.1.0-py2.5-linux-x86_64.egg/twisted/internet/base.py\", line 545, in fireSystemEvent\n            event.fireEvent()\n        --- <exception caught here> ---\n          File \"/home/tclemans/sage-3.1.2.rc0/local/lib/python2.5/site-packages/Twisted-8.1.0-py2.5-linux-x86_64.egg/twisted/internet/base.py\", line 368, in fireEvent\n            result = callable(*args, **kwargs)\n          File \"notebooktesting/twistedconf.tac\", line 25, in save_notebook\n            reactor.stop()\n          File \"/home/tclemans/sage-3.1.2.rc0/local/lib/python2.5/site-packages/Twisted-8.1.0-py2.5-linux-x86_64.egg/twisted/internet/base.py\", line 495, in stop\n            \"Can't stop reactor that isn't running.\")\n        twisted.internet.error.ReactorNotRunning: Can't stop reactor that isn't running.\n\n2008-09-08 05:45:49-0700 [-] (Port 8999 Closed)\n2008-09-08 05:45:49-0700 [-] Stopping factory <twisted.web2.channel.http.HTTPFactory instance at 0x2b779155d9e0>\n2008-09-08 05:45:49-0700 [-] Main loop terminated.\n2008-09-08 05:45:49-0700 [-] Server Shut Down.\nTrue\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4077\n\n",
    "created_at": "2008-09-08T12:52:39Z",
    "labels": [
        "notebook",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.2",
    "title": "notebook - ReactorNotRunning error consistently seen in sage-3.1.2.rc0",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4077",
    "user": "TimothyClemans"
}
```
Assignee: boothby

Traceback when I hit CLTRL-C to stop the notebook. 

This is happening in sage-3.1.2.rc0 with and without the spkg at #4074.


```
2008-09-08 05:45:38-0700 [-] Log opened.
2008-09-08 05:45:38-0700 [-] twistd 8.1.0 (/home/tclemans/sage-3.1.2.rc0/local/bin/python 2.5.2) starting up
2008-09-08 05:45:38-0700 [-] reactor class: <class 'twisted.internet.selectreactor.SelectReactor'>
2008-09-08 05:45:38-0700 [-] twisted.web2.channel.http.HTTPFactory starting on 8999
2008-09-08 05:45:38-0700 [-] Starting factory <twisted.web2.channel.http.HTTPFactory instance at 0x2b779155d9e0>
2008-09-08 05:45:49-0700 [-] Saving notebook...
2008-09-08 05:45:49-0700 [-] Notebook cleanly saved.
2008-09-08 05:45:49-0700 [-] Saving notebook...
2008-09-08 05:45:49-0700 [-] Unhandled Error
        Traceback (most recent call last):
          File "/home/tclemans/sage-3.1.2.rc0/local/lib/python2.5/site-packages/Twisted-8.1.0-py2.5-linux-x86_64.egg/twisted/internet/base.py", line 1048, in run
            self.mainLoop()
          File "/home/tclemans/sage-3.1.2.rc0/local/lib/python2.5/site-packages/Twisted-8.1.0-py2.5-linux-x86_64.egg/twisted/internet/base.py", line 1057, in mainLoop
            self.runUntilCurrent()
          File "/home/tclemans/sage-3.1.2.rc0/local/lib/python2.5/site-packages/Twisted-8.1.0-py2.5-linux-x86_64.egg/twisted/internet/base.py", line 705, in runUntilCurrent
            call.func(*call.args, **call.kw)
          File "/home/tclemans/sage-3.1.2.rc0/local/lib/python2.5/site-packages/Twisted-8.1.0-py2.5-linux-x86_64.egg/twisted/internet/base.py", line 545, in fireSystemEvent
            event.fireEvent()
        --- <exception caught here> ---
          File "/home/tclemans/sage-3.1.2.rc0/local/lib/python2.5/site-packages/Twisted-8.1.0-py2.5-linux-x86_64.egg/twisted/internet/base.py", line 368, in fireEvent
            result = callable(*args, **kwargs)
          File "notebooktesting/twistedconf.tac", line 25, in save_notebook
            reactor.stop()
          File "/home/tclemans/sage-3.1.2.rc0/local/lib/python2.5/site-packages/Twisted-8.1.0-py2.5-linux-x86_64.egg/twisted/internet/base.py", line 495, in stop
            "Can't stop reactor that isn't running.")
        twisted.internet.error.ReactorNotRunning: Can't stop reactor that isn't running.

2008-09-08 05:45:49-0700 [-] (Port 8999 Closed)
2008-09-08 05:45:49-0700 [-] Stopping factory <twisted.web2.channel.http.HTTPFactory instance at 0x2b779155d9e0>
2008-09-08 05:45:49-0700 [-] Main loop terminated.
2008-09-08 05:45:49-0700 [-] Server Shut Down.
True
```


Issue created by migration from https://trac.sagemath.org/ticket/4077





---

archive/issue_comments_029426.json:
```json
{
    "body": "Attachment [trac_4077.patch](tarball://root/attachments/some-uuid/ticket4077/trac_4077.patch) by mhansen created at 2008-09-08 23:20:30",
    "created_at": "2008-09-08T23:20:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4077",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4077#issuecomment-29426",
    "user": "mhansen"
}
```

Attachment [trac_4077.patch](tarball://root/attachments/some-uuid/ticket4077/trac_4077.patch) by mhansen created at 2008-09-08 23:20:30



---

archive/issue_comments_029427.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-09-08T23:20:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4077",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4077#issuecomment-29427",
    "user": "mhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_029428.json:
```json
{
    "body": "Changing assignee from boothby to mhansen.",
    "created_at": "2008-09-08T23:20:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4077",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4077#issuecomment-29428",
    "user": "mhansen"
}
```

Changing assignee from boothby to mhansen.



---

archive/issue_comments_029429.json:
```json
{
    "body": "Patch looks good to me.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-09T04:58:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4077",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4077#issuecomment-29429",
    "user": "mabshoff"
}
```

Patch looks good to me.

Cheers,

Michael



---

archive/issue_comments_029430.json:
```json
{
    "body": "Merged in Sage 3.1.2.rc1",
    "created_at": "2008-09-09T04:59:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4077",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4077#issuecomment-29430",
    "user": "mabshoff"
}
```

Merged in Sage 3.1.2.rc1



---

archive/issue_comments_029431.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-09T04:59:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4077",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4077#issuecomment-29431",
    "user": "mabshoff"
}
```

Resolution: fixed
