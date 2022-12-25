# Issue 3035: calculus/equations.py
segfault with new cython & -ba

archive/issues_003035.json:
```json
{
    "body": "Assignee: @williamstein\n\ncalculus/equations.py segfaults on test with patched cython and -ba.  However it only segfaults most of the time on automated testing, and does not segfault for gdb, valgrind, etc.\n\nThe test in question is \n\n```\n    sage: loads(dumps(eqn)) == eqn \n    True\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3035\n\n",
    "created_at": "2008-04-26T23:48:15Z",
    "labels": [
        "component: calculus",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.1",
    "title": "calculus/equations.py\nsegfault with new cython & -ba",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3035",
    "user": "https://github.com/garyfurnish"
}
```
Assignee: @williamstein

calculus/equations.py segfaults on test with patched cython and -ba.  However it only segfaults most of the time on automated testing, and does not segfault for gdb, valgrind, etc.

The test in question is 

```
    sage: loads(dumps(eqn)) == eqn 
    True
```


Issue created by migration from https://trac.sagemath.org/ticket/3035





---

archive/issue_comments_020843.json:
```json
{
    "body": "This also happens with stefan's cython-dev code.",
    "created_at": "2008-04-27T00:30:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3035",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3035#issuecomment-20843",
    "user": "https://github.com/garyfurnish"
}
```

This also happens with stefan's cython-dev code.



---

archive/issue_comments_020844.json:
```json
{
    "body": "This does not segfault as of sage-3.0.alpha0",
    "created_at": "2008-04-27T00:56:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3035",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3035#issuecomment-20844",
    "user": "https://github.com/garyfurnish"
}
```

This does not segfault as of sage-3.0.alpha0



---

archive/issue_comments_020845.json:
```json
{
    "body": "This problem is introduced after sage-3.0.rc0",
    "created_at": "2008-04-27T02:52:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3035",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3035#issuecomment-20845",
    "user": "https://github.com/garyfurnish"
}
```

This problem is introduced after sage-3.0.rc0



---

archive/issue_comments_020846.json:
```json
{
    "body": "This is caused by #2419, according to gfurnish.",
    "created_at": "2008-04-27T03:16:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3035",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3035#issuecomment-20846",
    "user": "https://github.com/williamstein"
}
```

This is caused by #2419, according to gfurnish.



---

archive/issue_comments_020847.json:
```json
{
    "body": "Specifically this is caused by sage-2419-refactor.patch",
    "created_at": "2008-04-27T03:28:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3035",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3035#issuecomment-20847",
    "user": "https://github.com/garyfurnish"
}
```

Specifically this is caused by sage-2419-refactor.patch



---

archive/issue_comments_020848.json:
```json
{
    "body": "Everything in that patch except the functions\n\n```\n    def _crash_msg(self):\n    def _interrupt(self):\n```\n\ncause segfaults.",
    "created_at": "2008-04-27T03:40:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3035",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3035#issuecomment-20848",
    "user": "https://github.com/garyfurnish"
}
```

Everything in that patch except the functions

```
    def _crash_msg(self):
    def _interrupt(self):
```

cause segfaults.



---

archive/issue_comments_020849.json:
```json
{
    "body": "Correction:\nEverything in that patch that alters expect.py except the functions\n\n```\n    def _crash_msg(self):\n    def _interrupt(self):\n```\n\ncause segfaults",
    "created_at": "2008-04-27T03:43:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3035",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3035#issuecomment-20849",
    "user": "https://github.com/garyfurnish"
}
```

Correction:
Everything in that patch that alters expect.py except the functions

```
    def _crash_msg(self):
    def _interrupt(self):
```

cause segfaults



---

archive/issue_comments_020850.json:
```json
{
    "body": "This does not segfault if you first delete ~/.sage/ or if it does not already exist.  It does segfault after it is run once until the folder is again deleted.",
    "created_at": "2008-04-27T21:27:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3035",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3035#issuecomment-20850",
    "user": "https://github.com/garyfurnish"
}
```

This does not segfault if you first delete ~/.sage/ or if it does not already exist.  It does segfault after it is run once until the folder is again deleted.



---

archive/issue_comments_020851.json:
```json
{
    "body": "This seems to have \"magically\" fixed itself for me after 3.0.1.alpha1.  After consulting with mabshoff we have decided to close this as something likely caused by my local machine.",
    "created_at": "2008-05-01T10:24:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3035",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3035#issuecomment-20851",
    "user": "https://github.com/garyfurnish"
}
```

This seems to have "magically" fixed itself for me after 3.0.1.alpha1.  After consulting with mabshoff we have decided to close this as something likely caused by my local machine.



---

archive/issue_events_006884.json:
```json
{
    "actor": "https://github.com/garyfurnish",
    "created_at": "2008-05-01T10:24:26Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3035",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3035#event-6884"
}
```



---

archive/issue_comments_020852.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-05-01T10:24:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3035",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3035#issuecomment-20852",
    "user": "https://github.com/garyfurnish"
}
```

Resolution: fixed
