# Issue 2359: notebook -- make it so when you send a kill signal to the notebook server it saves state

archive/issues_002359.json:
```json
{
    "body": "Assignee: boothby\n\nKill signal does this\n\n```\n2008/03/01 01:10 -0500 [-] Received SIGTERM, shutting down.\n2008/03/01 01:10 -0500 [-] (Port 8000 Closed)\n2008/03/01 01:10 -0500 [-] Stopping factory <twisted.web2.channel.http.HTTPFactory instance at 0x2a41530>\n2008/03/01 01:10 -0500 [-] Main loop terminated.\n2008/03/01 01:10 -0500 [-] Server Shut Down.\n```\n\n\nControl C does this\n\n```\n2008/03/01 01:12 -0500 [-] (Notebook cleanly saved. Press control-C again to exit.)\n```\n\n\nWe should change the notebook so it catches the kill and saves the notebook cleanly.   I have no idea how to do this.  Maybe some sort of \"hook\" into Twisted.  If anybody knows twisted or reads the docs and figures this out, post here!\n\nIssue created by migration from https://trac.sagemath.org/ticket/2359\n\n",
    "created_at": "2008-03-01T06:18:26Z",
    "labels": [
        "notebook",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.2",
    "title": "notebook -- make it so when you send a kill signal to the notebook server it saves state",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2359",
    "user": "@williamstein"
}
```
Assignee: boothby

Kill signal does this

```
2008/03/01 01:10 -0500 [-] Received SIGTERM, shutting down.
2008/03/01 01:10 -0500 [-] (Port 8000 Closed)
2008/03/01 01:10 -0500 [-] Stopping factory <twisted.web2.channel.http.HTTPFactory instance at 0x2a41530>
2008/03/01 01:10 -0500 [-] Main loop terminated.
2008/03/01 01:10 -0500 [-] Server Shut Down.
```


Control C does this

```
2008/03/01 01:12 -0500 [-] (Notebook cleanly saved. Press control-C again to exit.)
```


We should change the notebook so it catches the kill and saves the notebook cleanly.   I have no idea how to do this.  Maybe some sort of "hook" into Twisted.  If anybody knows twisted or reads the docs and figures this out, post here!

Issue created by migration from https://trac.sagemath.org/ticket/2359





---

archive/issue_comments_015902.json:
```json
{
    "body": "The python atexit module might help here:\n\nhttp://docs.python.org/lib/module-atexit.html",
    "created_at": "2008-03-01T20:27:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2359",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2359#issuecomment-15902",
    "user": "@jasongrout"
}
```

The python atexit module might help here:

http://docs.python.org/lib/module-atexit.html



---

archive/issue_comments_015903.json:
```json
{
    "body": "If you want to do things the twisted way, here is something that should work:\n\nreactor.addSystemEventTrigger('before', 'shutdown', f)\n\nf is a function you want to be called BEFORE the reactor shuts down.  Here is some more documentation about how to properly use this feature:\n\nhttp://twistedmatrix.com/documents/current/api/twisted.internet.interfaces.IReactorCore.html#addSystemEventTrigger\n\nCheers,\nYi\n\nhttp://yiqiang.org",
    "created_at": "2008-03-03T21:40:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2359",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2359#issuecomment-15903",
    "user": "@yqiang"
}
```

If you want to do things the twisted way, here is something that should work:

reactor.addSystemEventTrigger('before', 'shutdown', f)

f is a function you want to be called BEFORE the reactor shuts down.  Here is some more documentation about how to properly use this feature:

http://twistedmatrix.com/documents/current/api/twisted.internet.interfaces.IReactorCore.html#addSystemEventTrigger

Cheers,
Yi

http://yiqiang.org



---

archive/issue_comments_015904.json:
```json
{
    "body": "The attached patch fixes the issues:\n\n\n``` \n   1. I followed Yi's suggestion which worked like a charm.\n   2. As a bonus I also fixed the \"have to hit control-c twice to stop the notebook server\" crap. Now\n      it stops just fine with one single control-c.\n   3. I changed twistd.pd to twistd.pid  -- it's a typo since it's supposed to be a pin id.\n```\n",
    "created_at": "2008-05-11T07:12:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2359",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2359#issuecomment-15904",
    "user": "@williamstein"
}
```

The attached patch fixes the issues:


``` 
   1. I followed Yi's suggestion which worked like a charm.
   2. As a bonus I also fixed the "have to hit control-c twice to stop the notebook server" crap. Now
      it stops just fine with one single control-c.
   3. I changed twistd.pd to twistd.pid  -- it's a typo since it's supposed to be a pin id.
```




---

archive/issue_comments_015905.json:
```json
{
    "body": "A couple of comments:\n\n1) As far as I can tell the last bit of the patch (involving polynomials) has nothing to do with this issue. Could you explain what that does?\n\n2) Is save_notebook() only used on shutdown? Isn't it possible that in the future, someone would want to call save_notebook while the notebook is running? If that's true, you probably do not want to call reactor.stop() in save_notebook unless you're _certain_ that save_notebook() is the last thing you want to do. \n\nBesides that this patch looks great!",
    "created_at": "2008-05-11T17:12:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2359",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2359#issuecomment-15905",
    "user": "@yqiang"
}
```

A couple of comments:

1) As far as I can tell the last bit of the patch (involving polynomials) has nothing to do with this issue. Could you explain what that does?

2) Is save_notebook() only used on shutdown? Isn't it possible that in the future, someone would want to call save_notebook while the notebook is running? If that's true, you probably do not want to call reactor.stop() in save_notebook unless you're _certain_ that save_notebook() is the last thing you want to do. 

Besides that this patch looks great!



---

archive/issue_comments_015906.json:
```json
{
    "body": "Removed polynomial garbage",
    "created_at": "2008-05-12T05:40:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2359",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2359#issuecomment-15906",
    "user": "boothby"
}
```

Removed polynomial garbage



---

archive/issue_comments_015907.json:
```json
{
    "body": "Attachment [sage-2359.patch](tarball://root/attachments/some-uuid/ticket2359/sage-2359.patch) by boothby created at 2008-05-12 05:41:35\n\nworks for me -- I uploaded a cleaned up patch.",
    "created_at": "2008-05-12T05:41:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2359",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2359#issuecomment-15907",
    "user": "boothby"
}
```

Attachment [sage-2359.patch](tarball://root/attachments/some-uuid/ticket2359/sage-2359.patch) by boothby created at 2008-05-12 05:41:35

works for me -- I uploaded a cleaned up patch.



---

archive/issue_comments_015908.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-05-12T11:11:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2359",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2359#issuecomment-15908",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_015909.json:
```json
{
    "body": "Merged in Sage 3.0.2.alpha1",
    "created_at": "2008-05-12T11:11:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2359",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2359#issuecomment-15909",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.2.alpha1
