# Issue 2935: notebook: internal server error sage-3.0.alpha5

archive/issues_002935.json:
```json
{
    "body": "Assignee: boothby\n\nTrying to delete some old worksheets, this happened:\n\n\n```\n[jaap@paix sage-3.0.alpha5]$ ./sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n| SAGE Version 3.0.alpha5, Release Date: 2008-04-15                  |\n| Type notebook() for the GUI, and license() for information.        |\n\nsage: notebook()\nThe notebook files are stored in: /home/jaap/.sage//sage_notebook\nPort 8000 is already in use.\nTrying next port...\n****************************************************\n*                                                  *\n* Open your web browser to https://localhost:8001  *\n*                                                  *\n****************************************************\nThere is an admin account.  If you do not remember the password,\nquit the notebook and type notebook(reset=True).\nRemoving stale pidfile /home/jaap/.sage/sage_notebook/twistd.pd\n2008-04-15 19:54:17+0200 [-] Log opened.\n2008-04-15 19:54:17+0200 [-] twistd 8.0.1 (/home/jaap/downloads/sage-3.0.alpha5/local/bin/python 2.5.1) starting up\n2008-04-15 19:54:17+0200 [-] reactor class: <class 'twisted.internet.selectreactor.SelectReactor'>\n2008-04-15 19:54:17+0200 [-] twisted.web2.channel.http.HTTPFactory starting on 8001\n2008-04-15 19:54:17+0200 [-] Starting factory <twisted.web2.channel.http.HTTPFactory instance at 0xa6cdc4c>\n2008-04-15 19:55:24+0200 [HTTPChannel,3,127.0.0.1] /home/jaap/downloads/sage-3.0.alpha5/local/lib/python2.5/site-packages/twisted/internet/defer.py:262: exceptions.DeprecationWarning: Don't pass strings (like 'Bad token') to failure.Failure (replacing with a DefaultException).\n2008-04-15 19:55:24+0200 [HTTPChannel,3,127.0.0.1] Exception rendering:\n2008-04-15 19:55:24+0200 [HTTPChannel,3,127.0.0.1] Unhandled Error\n        Traceback (most recent call last):\n        Failure: twisted.python.failure.DefaultException: Bad token\n\n\n}}\n\nJaap\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2935\n\n",
    "created_at": "2008-04-15T18:11:04Z",
    "labels": [
        "notebook",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.2",
    "title": "notebook: internal server error sage-3.0.alpha5",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2935",
    "user": "@jaapspies"
}
```
Assignee: boothby

Trying to delete some old worksheets, this happened:


```
[jaap@paix sage-3.0.alpha5]$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 3.0.alpha5, Release Date: 2008-04-15                  |
| Type notebook() for the GUI, and license() for information.        |

sage: notebook()
The notebook files are stored in: /home/jaap/.sage//sage_notebook
Port 8000 is already in use.
Trying next port...
****************************************************
*                                                  *
* Open your web browser to https://localhost:8001  *
*                                                  *
****************************************************
There is an admin account.  If you do not remember the password,
quit the notebook and type notebook(reset=True).
Removing stale pidfile /home/jaap/.sage/sage_notebook/twistd.pd
2008-04-15 19:54:17+0200 [-] Log opened.
2008-04-15 19:54:17+0200 [-] twistd 8.0.1 (/home/jaap/downloads/sage-3.0.alpha5/local/bin/python 2.5.1) starting up
2008-04-15 19:54:17+0200 [-] reactor class: <class 'twisted.internet.selectreactor.SelectReactor'>
2008-04-15 19:54:17+0200 [-] twisted.web2.channel.http.HTTPFactory starting on 8001
2008-04-15 19:54:17+0200 [-] Starting factory <twisted.web2.channel.http.HTTPFactory instance at 0xa6cdc4c>
2008-04-15 19:55:24+0200 [HTTPChannel,3,127.0.0.1] /home/jaap/downloads/sage-3.0.alpha5/local/lib/python2.5/site-packages/twisted/internet/defer.py:262: exceptions.DeprecationWarning: Don't pass strings (like 'Bad token') to failure.Failure (replacing with a DefaultException).
2008-04-15 19:55:24+0200 [HTTPChannel,3,127.0.0.1] Exception rendering:
2008-04-15 19:55:24+0200 [HTTPChannel,3,127.0.0.1] Unhandled Error
        Traceback (most recent call last):
        Failure: twisted.python.failure.DefaultException: Bad token


}}

Jaap



Issue created by migration from https://trac.sagemath.org/ticket/2935





---

archive/issue_comments_020215.json:
```json
{
    "body": "Well, there already seems to be a notebook running on port 8000, so could that have something to do with that? Can you check and report back?\n\nDo we support more than one notebook running from the same Sage instance?\n\nCheers,\n\nMichael",
    "created_at": "2008-04-15T19:12:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2935",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2935#issuecomment-20215",
    "user": "mabshoff"
}
```

Well, there already seems to be a notebook running on port 8000, so could that have something to do with that? Can you check and report back?

Do we support more than one notebook running from the same Sage instance?

Cheers,

Michael



---

archive/issue_comments_020216.json:
```json
{
    "body": "Replying to [comment:1 mabshoff]:\n> Well, there already seems to be a notebook running on port 8000, so could that have something to do with that? Can you check and report back?\n>\n\nNo, this is not the case. No notebook on port 8000.\n\n \n> Do we support more than one notebook running from the same Sage instance?\n> \n\nI don't think so. I would love to have the possibility to run\nmore notebooks from different versions of sage!\n\n\n\nJaap\n\n\n> Cheers,\n> \n> Michael",
    "created_at": "2008-04-15T20:03:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2935",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2935#issuecomment-20216",
    "user": "@jaapspies"
}
```

Replying to [comment:1 mabshoff]:
> Well, there already seems to be a notebook running on port 8000, so could that have something to do with that? Can you check and report back?
>

No, this is not the case. No notebook on port 8000.

 
> Do we support more than one notebook running from the same Sage instance?
> 

I don't think so. I would love to have the possibility to run
more notebooks from different versions of sage!



Jaap


> Cheers,
> 
> Michael



---

archive/issue_comments_020217.json:
```json
{
    "body": "Neither tom nor I can replicate this.\n\nCould you try with a fresh NOTEBOOK directory?  E.g.,\n\n  sage: notebook(directory = 'foo')\n\nwilliam",
    "created_at": "2008-04-16T21:44:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2935",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2935#issuecomment-20217",
    "user": "@williamstein"
}
```

Neither tom nor I can replicate this.

Could you try with a fresh NOTEBOOK directory?  E.g.,

  sage: notebook(directory = 'foo')

william



---

archive/issue_comments_020218.json:
```json
{
    "body": "Let me tell what I did a few minutes ago.\n\nI created a worksheet 'test' with sage-2.11, saved it and quit.\n\nStarted the notebook under sage-3.0.alpha5, selected 'test' and clicked on delete.\n\nWith the error mentioned above :(\n\nWorksheets created with earlier versions and with alpha5 don't give this error!\n\nJaap",
    "created_at": "2008-04-16T22:43:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2935",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2935#issuecomment-20218",
    "user": "@jaapspies"
}
```

Let me tell what I did a few minutes ago.

I created a worksheet 'test' with sage-2.11, saved it and quit.

Started the notebook under sage-3.0.alpha5, selected 'test' and clicked on delete.

With the error mentioned above :(

Worksheets created with earlier versions and with alpha5 don't give this error!

Jaap



---

archive/issue_comments_020219.json:
```json
{
    "body": "Follow up: selecting an old ws and clicking on 'Archive' cased the same error here.",
    "created_at": "2008-04-16T22:57:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2935",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2935#issuecomment-20219",
    "user": "@jaapspies"
}
```

Follow up: selecting an old ws and clicking on 'Archive' cased the same error here.



---

archive/issue_comments_020220.json:
```json
{
    "body": "I reproduced this failure on a different machine Fedora 8, 32 bits with a ws\nmade under sage-2.11. using Firefox-2.0.0.13.\n\nNarrowing(?) this down: I get the same failure under sage-2.11 :(\n\nStarting the notebook and selecting nothing(!) clicking on Archive or Delete gives the internal server error. Both on Fedora 7 and 8.\n\n\n\nJaap",
    "created_at": "2008-04-17T19:55:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2935",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2935#issuecomment-20220",
    "user": "@jaapspies"
}
```

I reproduced this failure on a different machine Fedora 8, 32 bits with a ws
made under sage-2.11. using Firefox-2.0.0.13.

Narrowing(?) this down: I get the same failure under sage-2.11 :(

Starting the notebook and selecting nothing(!) clicking on Archive or Delete gives the internal server error. Both on Fedora 7 and 8.



Jaap



---

archive/issue_comments_020221.json:
```json
{
    "body": "Replying to [comment:6 jsp]:\n> I reproduced this failure on a different machine Fedora 8, 32 bits with a ws\n> made under sage-2.11. using Firefox-2.0.0.13.\n> \n> Narrowing(?) this down: I get the same failure under sage-2.11 :(\n> \n> Starting the notebook and selecting nothing(!) clicking on Archive or Delete gives the internal server error. Both on Fedora 7 and 8.\n> \n> \n> \n> Jaap\n\n\nEven with sage-2.10.4, just clicking in the overview on Delete:\n\n\n```\n[jaap@paix sage-2.10.4]$ ./sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n| SAGE Version 2.10.4, Release Date: 2008-03-16                      |\n| Type notebook() for the GUI, and license() for information.        |\n\nsage: notebook()\nThe notebook files are stored in: /home/jaap/.sage//sage_notebook\nPort 8000 is already in use.\nTrying next port...\n****************************************************\n*                                                  *\n* Open your web browser to https://localhost:8001  *\n*                                                  *\n****************************************************\nThere is an admin account.  If you do not remember the password,\nquit the notebook and type notebook(reset=True).\nRemoving stale pidfile /home/jaap/.sage/sage_notebook/twistd.pd\n2008/04/17 23:11 +0200 [-] Log opened.\n2008/04/17 23:11 +0200 [-] twistd 2.5.0 (/home/jaap/downloads/sage-2.10.4/local/bin/python 2.5.1) starting up\n2008/04/17 23:11 +0200 [-] reactor class: <class 'twisted.internet.selectreactor.SelectReactor'>\n2008/04/17 23:11 +0200 [-] Loading sage_notebook/twistedconf.tac...\n2008/04/17 23:12 +0200 [-] Loaded.\n2008/04/17 23:12 +0200 [-] twisted.web2.channel.http.HTTPFactory starting on 8001\n2008/04/17 23:12 +0200 [-] Starting factory <twisted.web2.channel.http.HTTPFactory instance at 0x8b9082c>\n2008/04/17 23:12 +0200 [HTTPChannel,1,127.0.0.1] /home/jaap/downloads/sage-2.10.4/local/lib/python2.5/site-packages/twisted/internet/defer.py:259: exceptions.DeprecationWarning: Don't pass strings (like 'Bad token') to failure.Failure (replacing with a DefaultException).\n2008/04/17 23:12 +0200 [HTTPChannel,1,127.0.0.1] Exception rendering:\n2008/04/17 23:12 +0200 [HTTPChannel,1,127.0.0.1] Unhandled Error\n        Traceback (most recent call last):\n        Failure: twisted.python.failure.DefaultException: Bad token\n\n\n\n\n```\n\n\n\nSo I'm flabbergasted\n\nJaap",
    "created_at": "2008-04-17T21:50:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2935",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2935#issuecomment-20221",
    "user": "@jaapspies"
}
```

Replying to [comment:6 jsp]:
> I reproduced this failure on a different machine Fedora 8, 32 bits with a ws
> made under sage-2.11. using Firefox-2.0.0.13.
> 
> Narrowing(?) this down: I get the same failure under sage-2.11 :(
> 
> Starting the notebook and selecting nothing(!) clicking on Archive or Delete gives the internal server error. Both on Fedora 7 and 8.
> 
> 
> 
> Jaap


Even with sage-2.10.4, just clicking in the overview on Delete:


```
[jaap@paix sage-2.10.4]$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 2.10.4, Release Date: 2008-03-16                      |
| Type notebook() for the GUI, and license() for information.        |

sage: notebook()
The notebook files are stored in: /home/jaap/.sage//sage_notebook
Port 8000 is already in use.
Trying next port...
****************************************************
*                                                  *
* Open your web browser to https://localhost:8001  *
*                                                  *
****************************************************
There is an admin account.  If you do not remember the password,
quit the notebook and type notebook(reset=True).
Removing stale pidfile /home/jaap/.sage/sage_notebook/twistd.pd
2008/04/17 23:11 +0200 [-] Log opened.
2008/04/17 23:11 +0200 [-] twistd 2.5.0 (/home/jaap/downloads/sage-2.10.4/local/bin/python 2.5.1) starting up
2008/04/17 23:11 +0200 [-] reactor class: <class 'twisted.internet.selectreactor.SelectReactor'>
2008/04/17 23:11 +0200 [-] Loading sage_notebook/twistedconf.tac...
2008/04/17 23:12 +0200 [-] Loaded.
2008/04/17 23:12 +0200 [-] twisted.web2.channel.http.HTTPFactory starting on 8001
2008/04/17 23:12 +0200 [-] Starting factory <twisted.web2.channel.http.HTTPFactory instance at 0x8b9082c>
2008/04/17 23:12 +0200 [HTTPChannel,1,127.0.0.1] /home/jaap/downloads/sage-2.10.4/local/lib/python2.5/site-packages/twisted/internet/defer.py:259: exceptions.DeprecationWarning: Don't pass strings (like 'Bad token') to failure.Failure (replacing with a DefaultException).
2008/04/17 23:12 +0200 [HTTPChannel,1,127.0.0.1] Exception rendering:
2008/04/17 23:12 +0200 [HTTPChannel,1,127.0.0.1] Unhandled Error
        Traceback (most recent call last):
        Failure: twisted.python.failure.DefaultException: Bad token




```



So I'm flabbergasted

Jaap



---

archive/issue_comments_020222.json:
```json
{
    "body": "This issue seems to be introduced with sage-2.10.1.\n\nIn sage-2.9 clicking on the Archive button gives a warning.\n\nI put up some screen shots here: http://sage.math.washington.edu/home/jsp/screenshots/s1/\n\nJaap",
    "created_at": "2008-04-18T13:48:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2935",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2935#issuecomment-20222",
    "user": "@jaapspies"
}
```

This issue seems to be introduced with sage-2.10.1.

In sage-2.9 clicking on the Archive button gives a warning.

I put up some screen shots here: http://sage.math.washington.edu/home/jsp/screenshots/s1/

Jaap



---

archive/issue_comments_020223.json:
```json
{
    "body": "Could this have something to do with encoding? Jaap: what is the locale you use?\n\nCheers,\n\nMichael",
    "created_at": "2008-04-18T20:33:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2935",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2935#issuecomment-20223",
    "user": "mabshoff"
}
```

Could this have something to do with encoding? Jaap: what is the locale you use?

Cheers,

Michael



---

archive/issue_comments_020224.json:
```json
{
    "body": "Replying to [comment:9 mabshoff]:\n> Could this have something to do with encoding? Jaap: what is the locale you use?\n> \n> Cheers,\n> \n> Michael\n\n\nDon't think so. My Fedora install is just English (American). I do not use\nany localization.\n\nJaap",
    "created_at": "2008-04-18T20:44:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2935",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2935#issuecomment-20224",
    "user": "@jaapspies"
}
```

Replying to [comment:9 mabshoff]:
> Could this have something to do with encoding? Jaap: what is the locale you use?
> 
> Cheers,
> 
> Michael


Don't think so. My Fedora install is just English (American). I do not use
any localization.

Jaap



---

archive/issue_comments_020225.json:
```json
{
    "body": "Can anybody but Jaap replicate this problem?",
    "created_at": "2008-04-20T17:23:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2935",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2935#issuecomment-20225",
    "user": "@williamstein"
}
```

Can anybody but Jaap replicate this problem?



---

archive/issue_comments_020226.json:
```json
{
    "body": "How about this:\n\n```\nWilliam Stein wrote:\n>\n> \n> Please do\n>    sage: hg_sage.pull()\n> \n> then\n> \n>    sage -br\n> \n> and try that test again\n\nSomething strange was going on with the notebook(), but\nafter hg_sage.pull() and ./sage -br the notebook\nstarts in Firefox with still the problem I have reported in trac #2935.\n\nBut when I start firefox by hand:  https://localhost:8001/\neverything seems to work!\n\nJaap\n\n\n```\n",
    "created_at": "2008-04-22T15:55:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2935",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2935#issuecomment-20226",
    "user": "@jaapspies"
}
```

How about this:

```
William Stein wrote:
>
> 
> Please do
>    sage: hg_sage.pull()
> 
> then
> 
>    sage -br
> 
> and try that test again

Something strange was going on with the notebook(), but
after hg_sage.pull() and ./sage -br the notebook
starts in Firefox with still the problem I have reported in trac #2935.

But when I start firefox by hand:  https://localhost:8001/
everything seems to work!

Jaap


```




---

archive/issue_comments_020227.json:
```json
{
    "body": "Once again this is what I do now to avoid the error:\n\nStart the notebook in sage-3.0.\n\nClose the notebook tab in firefox.\n\nConnect to https://localhost:8001/\n\nNow I have a notebook running in which I can Archive en Delete worksheets.\n\nJaap",
    "created_at": "2008-04-22T16:45:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2935",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2935#issuecomment-20227",
    "user": "@jaapspies"
}
```

Once again this is what I do now to avoid the error:

Start the notebook in sage-3.0.

Close the notebook tab in firefox.

Connect to https://localhost:8001/

Now I have a notebook running in which I can Archive en Delete worksheets.

Jaap



---

archive/issue_comments_020228.json:
```json
{
    "body": "Since nobody else can replicate this, and it could just be some weird cookie corruption on Jaap's computer (or a weird firefox bug), I'm closing this as invalid.",
    "created_at": "2008-05-10T23:17:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2935",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2935#issuecomment-20228",
    "user": "@williamstein"
}
```

Since nobody else can replicate this, and it could just be some weird cookie corruption on Jaap's computer (or a weird firefox bug), I'm closing this as invalid.



---

archive/issue_comments_020229.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2008-05-10T23:17:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2935",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2935#issuecomment-20229",
    "user": "@williamstein"
}
```

Resolution: invalid
