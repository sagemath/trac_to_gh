# Issue 8410: Improve robustness of @parallel

archive/issues_008410.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  wstein\n\nRun the following:\n\n```\n\n@parallel(4)\ndef sleeper(x):\n    sleep(x)\n\nfor _ in sleeper([10]*100):\n    pass\n\n```\n\nand interrupt it with ctrl-c (or esc in the notebook).   We get\n\n```\nKilling any remaining workers...\n[Errno 3] No such process\n---------------------------------------------------------------------------\nKeyboardInterrupt                         Traceback (most recent call last)\n\n/home/boothby/<ipython console> in <module>()\n\n/usr/local/sage/local/lib/python2.6/site-packages/sage/parallel/use_fork.pyc in __call__(self, f, inputs)\n     98                         signal.alarm(int(walltime() - oldest)+1)\n     99                     try:\n--> 100                         pid = os.wait()[0]\n    101                         signal.signal(signal.SIGALRM, signal.SIG_IGN)\n    102                     except RuntimeError:\n\n/usr/local/sage/local/lib/python2.6/site-packages/sage/interfaces/get_sigs.pyc in my_sigint(x, n)\n      7 \n      8 def my_sigint(x, n):\n----> 9     raise KeyboardInterrupt\n     10 \n     11 def my_sigfpe(x, n):\n\nKeyboardInterrupt: \n``` \n\nand then, let's restart the computation:\n\n```\nsage: for _ in sleeper([10]*100):\n    print \"hello\"\n    pass\n....: \n15775\n[Errno 39] Directory not empty: '/home/boothby/.sage/temp/sage.math.washington.edu/15401/dir_0'\nKilling any remaining workers...\n```\n\nAll I can do here is restart Sage.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8410\n\n",
    "created_at": "2010-03-01T17:30:52Z",
    "labels": [
        "component: performance",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5.2",
    "title": "Improve robustness of @parallel",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8410",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```
Assignee: tbd

CC:  wstein

Run the following:

```

@parallel(4)
def sleeper(x):
    sleep(x)

for _ in sleeper([10]*100):
    pass

```

and interrupt it with ctrl-c (or esc in the notebook).   We get

```
Killing any remaining workers...
[Errno 3] No such process
---------------------------------------------------------------------------
KeyboardInterrupt                         Traceback (most recent call last)

/home/boothby/<ipython console> in <module>()

/usr/local/sage/local/lib/python2.6/site-packages/sage/parallel/use_fork.pyc in __call__(self, f, inputs)
     98                         signal.alarm(int(walltime() - oldest)+1)
     99                     try:
--> 100                         pid = os.wait()[0]
    101                         signal.signal(signal.SIGALRM, signal.SIG_IGN)
    102                     except RuntimeError:

/usr/local/sage/local/lib/python2.6/site-packages/sage/interfaces/get_sigs.pyc in my_sigint(x, n)
      7 
      8 def my_sigint(x, n):
----> 9     raise KeyboardInterrupt
     10 
     11 def my_sigfpe(x, n):

KeyboardInterrupt: 
``` 

and then, let's restart the computation:

```
sage: for _ in sleeper([10]*100):
    print "hello"
    pass
....: 
15775
[Errno 39] Directory not empty: '/home/boothby/.sage/temp/sage.math.washington.edu/15401/dir_0'
Killing any remaining workers...
```

All I can do here is restart Sage.


Issue created by migration from https://trac.sagemath.org/ticket/8410





---

archive/issue_comments_075224.json:
```json
{
    "body": "First remark: This fails *exactly* the same on the command line.  Also the error is now:\n\n```\nsage: for _ in sleeper([10]*100):\n....:         pass\n....: \n91260\nKilling any remaining workers...\n```",
    "created_at": "2010-06-24T05:02:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8410",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8410#issuecomment-75224",
    "user": "https://github.com/williamstein"
}
```

First remark: This fails *exactly* the same on the command line.  Also the error is now:

```
sage: for _ in sleeper([10]*100):
....:         pass
....: 
91260
Killing any remaining workers...
```



---

archive/issue_events_020158.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2010-06-24T05:02:31Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8410",
    "milestone": "sage-4.5",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8410#event-20158"
}
```



---

archive/issue_comments_075225.json:
```json
{
    "body": "Attachment [trac_8410.patch](tarball://root/attachments/some-uuid/ticket8410/trac_8410.patch) by @williamstein created at 2010-06-24 05:43:53",
    "created_at": "2010-06-24T05:43:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8410",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8410#issuecomment-75225",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac_8410.patch](tarball://root/attachments/some-uuid/ticket8410/trac_8410.patch) by @williamstein created at 2010-06-24 05:43:53



---

archive/issue_comments_075226.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-06-24T05:43:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8410",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8410#issuecomment-75226",
    "user": "https://github.com/williamstein"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_075227.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-24T05:52:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8410",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8410#issuecomment-75227",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_075228.json:
```json
{
    "body": "works for me",
    "created_at": "2010-06-24T05:52:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8410",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8410#issuecomment-75228",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

works for me



---

archive/issue_comments_075229.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-20T10:02:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8410",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8410#issuecomment-75229",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed



---

archive/issue_events_020159.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-07-20T10:02:01Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8410",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8410#event-20159"
}
```
