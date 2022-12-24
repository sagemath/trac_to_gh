# Issue 3463: notebook -- create a resource folder and move AnonymousToplevel to it

archive/issues_003463.json:
```json
{
    "body": "Assignee: boothby\n\nThis is a first step in making the Notebook code more modular like Knoboo's. \n\nIssue created by migration from https://trac.sagemath.org/ticket/3463\n\n",
    "created_at": "2008-06-18T19:30:09Z",
    "labels": [
        "notebook",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "notebook -- create a resource folder and move AnonymousToplevel to it",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3463",
    "user": "TimothyClemans"
}
```
Assignee: boothby

This is a first step in making the Notebook code more modular like Knoboo's. 

Issue created by migration from https://trac.sagemath.org/ticket/3463





---

archive/issue_comments_024423.json:
```json
{
    "body": "Changing assignee from boothby to TimothyClemans.",
    "created_at": "2008-06-18T19:32:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3463",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3463#issuecomment-24423",
    "user": "TimothyClemans"
}
```

Changing assignee from boothby to TimothyClemans.



---

archive/issue_comments_024424.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-06-18T19:32:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3463",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3463#issuecomment-24424",
    "user": "TimothyClemans"
}
```

Changing status from new to assigned.



---

archive/issue_comments_024425.json:
```json
{
    "body": "Attachment [3463_1.patch](tarball://root/attachments/some-uuid/ticket3463/3463_1.patch) by TimothyClemans created at 2008-06-18 20:50:47\n\nI'm getting the following import error and haven't been able to figure it out.\n\n\n```\n  File \"/home/tclemans/sage-3.0.3.alpha0/local/lib/python2.5/site-packages/twisted/application/app.py\", line 412, in getApplication\n    application = service.loadApplication(filename, style, passphrase)\n  File \"/home/tclemans/sage-3.0.3.alpha0/local/lib/python2.5/site-packages/twisted/application/service.py\", line 340, in loadApplication\n    application = sob.loadValueFromFile(filename, 'application', passphrase)\n  File \"/home/tclemans/sage-3.0.3.alpha0/local/lib/python2.5/site-packages/twisted/persisted/sob.py\", line 214, in loadValueFromFile\n    exec fileObj in d, d\n  File \"sage_notebook/twistedconf.tac\", line 47, in <module>\n    import sage.server.notebook.avatars as avatars\n  File \"/home/tclemans/sage-3.0.3.alpha0/local/lib/python2.5/site-packages/sage/server/notebook/avatars.py\", line 20, in <module>\n    import resources.toplevels as toplevels\n  File \"/home/tclemans/sage-3.0.3.alpha0/local/lib/python2.5/site-packages/sage/server/notebook/resources/toplevels.py\", line 3, in <module>\n    import sage.server.notebook.avatars as avatars\nexceptions.AttributeError: 'module' object has no attribute 'avatars'\n\nFailed to load application: 'module' object has no attribute 'avatars'\n```\n",
    "created_at": "2008-06-18T20:50:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3463",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3463#issuecomment-24425",
    "user": "TimothyClemans"
}
```

Attachment [3463_1.patch](tarball://root/attachments/some-uuid/ticket3463/3463_1.patch) by TimothyClemans created at 2008-06-18 20:50:47

I'm getting the following import error and haven't been able to figure it out.


```
  File "/home/tclemans/sage-3.0.3.alpha0/local/lib/python2.5/site-packages/twisted/application/app.py", line 412, in getApplication
    application = service.loadApplication(filename, style, passphrase)
  File "/home/tclemans/sage-3.0.3.alpha0/local/lib/python2.5/site-packages/twisted/application/service.py", line 340, in loadApplication
    application = sob.loadValueFromFile(filename, 'application', passphrase)
  File "/home/tclemans/sage-3.0.3.alpha0/local/lib/python2.5/site-packages/twisted/persisted/sob.py", line 214, in loadValueFromFile
    exec fileObj in d, d
  File "sage_notebook/twistedconf.tac", line 47, in <module>
    import sage.server.notebook.avatars as avatars
  File "/home/tclemans/sage-3.0.3.alpha0/local/lib/python2.5/site-packages/sage/server/notebook/avatars.py", line 20, in <module>
    import resources.toplevels as toplevels
  File "/home/tclemans/sage-3.0.3.alpha0/local/lib/python2.5/site-packages/sage/server/notebook/resources/toplevels.py", line 3, in <module>
    import sage.server.notebook.avatars as avatars
exceptions.AttributeError: 'module' object has no attribute 'avatars'

Failed to load application: 'module' object has no attribute 'avatars'
```




---

archive/issue_comments_024426.json:
```json
{
    "body": "Attachment [3463_2.patch](tarball://root/attachments/some-uuid/ticket3463/3463_2.patch) by was created at 2009-11-19 21:46:57\n\nThis was evidently the beginning of an unrealized vision.",
    "created_at": "2009-11-19T21:46:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3463",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3463#issuecomment-24426",
    "user": "was"
}
```

Attachment [3463_2.patch](tarball://root/attachments/some-uuid/ticket3463/3463_2.patch) by was created at 2009-11-19 21:46:57

This was evidently the beginning of an unrealized vision.



---

archive/issue_comments_024427.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2009-11-19T21:46:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3463",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3463#issuecomment-24427",
    "user": "was"
}
```

Resolution: invalid
