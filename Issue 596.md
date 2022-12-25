# Issue 596: sage wiki() doesn't close with ctl-C

archive/issues_000596.json:
```json
{
    "body": "Assignee: @williamstein\n\nWhen I execute\n\n```\nsage: wiki()\n```\n\n\nI get ...\n\n```\n* Open your web browser to http://localhost:9000\n...\n```\n\nand it works fine.  Then how do I close it cleanly?\n\nI've tried ctrl-C in the sage window, which gives the following...\nIt closes that web window but then restarts the wiki.\n\n\n```\n2007/09/05 13:47 -0700 [-] Received SIGINT, shutting down.\n2007/09/05 13:47 -0700 [-] (Port 9000 Closed)\n2007/09/05 13:47 -0700 [-] Stopping factory\n<MoinMoin.server.twistedmoin.MoinSite instance at 0x4060ebec>\n2007/09/05 13:47 -0700 [-] Main loop terminated.\n2007/09/05 13:47 -0700 [-] Server Shut Down.\nPort 9000 is already in use.  Trying next port...\n**************************************************\n*                                                *\n* Open your web browser to http://localhost:9001 *\n*                                                *\n**************************************************\n2007/09/05 13:47 -0700 [-] Log opened.\n```\n\netc.\n\nClosing the webpage first doesn't help and SAGE doesn't accept any\ncommands\nother than ctrl-C, including ctrl-D.\n\nApparently Ctl-C Ctl-C (twice in rapid succession) closes it.\n\nReported by rjleveque`@`gmail.com (Randy Leveque)\n\nIssue created by migration from https://trac.sagemath.org/ticket/596\n\n",
    "created_at": "2007-09-05T22:18:22Z",
    "labels": [
        "component: algebraic geometry",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.2",
    "title": "sage wiki() doesn't close with ctl-C",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/596",
    "user": "https://github.com/wdjoyner"
}
```
Assignee: @williamstein

When I execute

```
sage: wiki()
```


I get ...

```
* Open your web browser to http://localhost:9000
...
```

and it works fine.  Then how do I close it cleanly?

I've tried ctrl-C in the sage window, which gives the following...
It closes that web window but then restarts the wiki.


```
2007/09/05 13:47 -0700 [-] Received SIGINT, shutting down.
2007/09/05 13:47 -0700 [-] (Port 9000 Closed)
2007/09/05 13:47 -0700 [-] Stopping factory
<MoinMoin.server.twistedmoin.MoinSite instance at 0x4060ebec>
2007/09/05 13:47 -0700 [-] Main loop terminated.
2007/09/05 13:47 -0700 [-] Server Shut Down.
Port 9000 is already in use.  Trying next port...
**************************************************
*                                                *
* Open your web browser to http://localhost:9001 *
*                                                *
**************************************************
2007/09/05 13:47 -0700 [-] Log opened.
```

etc.

Closing the webpage first doesn't help and SAGE doesn't accept any
commands
other than ctrl-C, including ctrl-D.

Apparently Ctl-C Ctl-C (twice in rapid succession) closes it.

Reported by rjleveque`@`gmail.com (Randy Leveque)

Issue created by migration from https://trac.sagemath.org/ticket/596





---

archive/issue_comments_003062.json:
```json
{
    "body": "Changing component from algebraic geometry to website/wiki.",
    "created_at": "2007-09-05T22:53:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/596",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/596#issuecomment-3062",
    "user": "https://github.com/williamstein"
}
```

Changing component from algebraic geometry to website/wiki.



---

archive/issue_comments_003063.json:
```json
{
    "body": "I can't replicate this:\n\n```\nsage: wiki()\n**************************************************\n*                                                *\n* Open your web browser to http://localhost:9000 *\n*                                                *\n**************************************************\n2007/09/05 15:49 -0700 [-] Log opened.\n2007/09/05 15:49 -0700 [-] twistd 2.5.0 (/home/was/s/local/bin/python 2.5.1) starting up\n2007/09/05 15:49 -0700 [-] reactor class: <class 'twisted.internet.selectreactor.SelectReactor'>\n2007/09/05 15:49 -0700 [-] Loading twistedconf.py...\n2007/09/05 15:49 -0700 [-] Loaded.\n2007/09/05 15:49 -0700 [-] MoinMoin.server.twistedmoin.MoinSite starting on 9000\n2007/09/05 15:49 -0700 [-] Starting factory <MoinMoin.server.twistedmoin.MoinSite instance at 0xb9e998>\n2007/09/05 15:49 -0700 [-] set uid/gid 1000/1000\n2007/09/05 15:49 -0700 [-] Received SIGINT, shutting down.\n2007/09/05 15:49 -0700 [-] (Port 9000 Closed)\n2007/09/05 15:49 -0700 [-] Stopping factory <MoinMoin.server.twistedmoin.MoinSite instance at 0xb9e998>\n2007/09/05 15:49 -0700 [-] Main loop terminated.\n2007/09/05 15:49 -0700 [-] Server Shut Down.\nTrue\nsage:       \n```\n",
    "created_at": "2007-09-05T22:53:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/596",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/596#issuecomment-3063",
    "user": "https://github.com/williamstein"
}
```

I can't replicate this:

```
sage: wiki()
**************************************************
*                                                *
* Open your web browser to http://localhost:9000 *
*                                                *
**************************************************
2007/09/05 15:49 -0700 [-] Log opened.
2007/09/05 15:49 -0700 [-] twistd 2.5.0 (/home/was/s/local/bin/python 2.5.1) starting up
2007/09/05 15:49 -0700 [-] reactor class: <class 'twisted.internet.selectreactor.SelectReactor'>
2007/09/05 15:49 -0700 [-] Loading twistedconf.py...
2007/09/05 15:49 -0700 [-] Loaded.
2007/09/05 15:49 -0700 [-] MoinMoin.server.twistedmoin.MoinSite starting on 9000
2007/09/05 15:49 -0700 [-] Starting factory <MoinMoin.server.twistedmoin.MoinSite instance at 0xb9e998>
2007/09/05 15:49 -0700 [-] set uid/gid 1000/1000
2007/09/05 15:49 -0700 [-] Received SIGINT, shutting down.
2007/09/05 15:49 -0700 [-] (Port 9000 Closed)
2007/09/05 15:49 -0700 [-] Stopping factory <MoinMoin.server.twistedmoin.MoinSite instance at 0xb9e998>
2007/09/05 15:49 -0700 [-] Main loop terminated.
2007/09/05 15:49 -0700 [-] Server Shut Down.
True
sage:       
```




---

archive/issue_comments_003064.json:
```json
{
    "body": "This might have been fixed by the sig off/on fix.\n\nRetagged for 2.8.6 - if it isn't fixed yet it might get retagged again.\n\nCheers,\n\nMichael",
    "created_at": "2007-09-30T22:11:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/596",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/596#issuecomment-3064",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This might have been fixed by the sig off/on fix.

Retagged for 2.8.6 - if it isn't fixed yet it might get retagged again.

Cheers,

Michael



---

archive/issue_comments_003065.json:
```json
{
    "body": "Can anybody replicate this?",
    "created_at": "2007-10-12T06:03:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/596",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/596#issuecomment-3065",
    "user": "https://github.com/williamstein"
}
```

Can anybody replicate this?



---

archive/issue_events_000652.json:
```json
{
    "actor": "@williamstein",
    "created_at": "2007-10-13T07:36:16Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/596",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/596#event-652"
}
```



---

archive/issue_comments_003066.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2007-10-13T07:36:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/596",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/596#issuecomment-3066",
    "user": "https://github.com/williamstein"
}
```

Resolution: wontfix



---

archive/issue_comments_003067.json:
```json
{
    "body": "I now see this on OS X 10.5 and it is easy to replicate, so I am re-opening this. \n\nThe problem somehow probably involves the codes that indicate a port is in use. \n\n -- William",
    "created_at": "2007-11-02T18:30:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/596",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/596#issuecomment-3067",
    "user": "https://github.com/williamstein"
}
```

I now see this on OS X 10.5 and it is easy to replicate, so I am re-opening this. 

The problem somehow probably involves the codes that indicate a port is in use. 

 -- William



---

archive/issue_comments_003068.json:
```json
{
    "body": "Resolution changed from wontfix to ",
    "created_at": "2007-11-02T18:30:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/596",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/596#issuecomment-3068",
    "user": "https://github.com/williamstein"
}
```

Resolution changed from wontfix to 



---

archive/issue_comments_003069.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2007-11-02T18:30:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/596",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/596#issuecomment-3069",
    "user": "https://github.com/williamstein"
}
```

Changing status from closed to reopened.



---

archive/issue_events_000653.json:
```json
{
    "actor": "@williamstein",
    "created_at": "2007-11-02T18:30:24Z",
    "event": "reopened",
    "issue": "https://github.com/sagemath/sagetest/issues/596",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/596#event-653"
}
```



---

archive/issue_events_000654.json:
```json
{
    "actor": "@rlmill",
    "created_at": "2008-02-10T03:16:36Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/596",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/596#event-654"
}
```



---

archive/issue_comments_003070.json:
```json
{
    "body": "This is duplicated in #1871.",
    "created_at": "2008-02-10T03:16:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/596",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/596#issuecomment-3070",
    "user": "https://github.com/rlmill"
}
```

This is duplicated in #1871.



---

archive/issue_comments_003071.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2008-02-10T03:16:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/596",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/596#issuecomment-3071",
    "user": "https://github.com/rlmill"
}
```

Resolution: duplicate
