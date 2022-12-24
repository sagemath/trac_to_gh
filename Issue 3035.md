# Issue 3035: calculus/equations.py
segfault with new cython & -ba

archive/issues_003035.json:
```json
{
    "body": "Assignee: @williamstein\n\ncalculus/equations.py segfaults on test with patched cython and -ba.  However it only segfaults most of the time on automated testing, and does not segfault for gdb, valgrind, etc.\n\nThe test in question is \n\n```\n    sage: loads(dumps(eqn)) == eqn \n    True\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3035\n\n",
    "created_at": "2008-04-26T23:48:15Z",
    "labels": [
        "calculus",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.1",
    "title": "calculus/equations.py\nsegfault with new cython & -ba",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3035",
    "user": "@garyfurnish"
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

archive/issue_comments_020886.json:
```json
{
    "body": "This also happens with stefan's cython-dev code.",
    "created_at": "2008-04-27T00:30:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3035",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3035#issuecomment-20886",
    "user": "@garyfurnish"
}
```

This also happens with stefan's cython-dev code.



---

archive/issue_comments_020887.json:
```json
{
    "body": "This does not segfault as of sage-3.0.alpha0",
    "created_at": "2008-04-27T00:56:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3035",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3035#issuecomment-20887",
    "user": "@garyfurnish"
}
```

This does not segfault as of sage-3.0.alpha0



---

archive/issue_comments_020888.json:
```json
{
    "body": "This problem is introduced after sage-3.0.rc0",
    "created_at": "2008-04-27T02:52:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3035",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3035#issuecomment-20888",
    "user": "@garyfurnish"
}
```

This problem is introduced after sage-3.0.rc0



---

archive/issue_comments_020889.json:
```json
{
    "body": "This is caused by #2419, according to gfurnish.",
    "created_at": "2008-04-27T03:16:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3035",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3035#issuecomment-20889",
    "user": "@williamstein"
}
```

This is caused by #2419, according to gfurnish.



---

archive/issue_comments_020890.json:
```json
{
    "body": "Specifically this is caused by sage-2419-refactor.patch",
    "created_at": "2008-04-27T03:28:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3035",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3035#issuecomment-20890",
    "user": "@garyfurnish"
}
```

Specifically this is caused by sage-2419-refactor.patch



---

archive/issue_comments_020891.json:
```json
{
    "body": "Everything in that patch except the functions\n\n```\n    def _crash_msg(self):\n    def _interrupt(self):\n```\n\ncause segfaults.",
    "created_at": "2008-04-27T03:40:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3035",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3035#issuecomment-20891",
    "user": "@garyfurnish"
}
```

Everything in that patch except the functions

```
    def _crash_msg(self):
    def _interrupt(self):
```

cause segfaults.



---

archive/issue_comments_020892.json:
```json
{
    "body": "Correction:\nEverything in that patch that alters expect.py except the functions\n\n```\n    def _crash_msg(self):\n    def _interrupt(self):\n```\n\ncause segfaults",
    "created_at": "2008-04-27T03:43:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3035",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3035#issuecomment-20892",
    "user": "@garyfurnish"
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

archive/issue_comments_020893.json:
```json
{
    "body": "This does not segfault if you first delete ~/.sage/ or if it does not already exist.  It does segfault after it is run once until the folder is again deleted.",
    "created_at": "2008-04-27T21:27:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3035",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3035#issuecomment-20893",
    "user": "@garyfurnish"
}
```

This does not segfault if you first delete ~/.sage/ or if it does not already exist.  It does segfault after it is run once until the folder is again deleted.



---

archive/issue_comments_020894.json:
```json
{
    "body": "This seems to have \"magically\" fixed itself for me after 3.0.1.alpha1.  After consulting with mabshoff we have decided to close this as something likely caused by my local machine.",
    "created_at": "2008-05-01T10:24:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3035",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3035#issuecomment-20894",
    "user": "@garyfurnish"
}
```

This seems to have "magically" fixed itself for me after 3.0.1.alpha1.  After consulting with mabshoff we have decided to close this as something likely caused by my local machine.



---

archive/issue_comments_020895.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-05-01T10:24:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3035",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3035#issuecomment-20895",
    "user": "@garyfurnish"
}
```

Resolution: fixed
