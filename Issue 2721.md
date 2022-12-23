# Issue 2721: parallel doctest not robust against filesystem issues

archive/issues_002721.json:
```json
{
    "body": "Assignee: failure\n\nI ran a parallel doctest while I was editing a file in Emacs.  Evidently Emacs creates strange symlinks that point to nowhere as a file locking mechanism:\n\n```\nlrwxrwxrwx 1 cwitty cwitty     46 2008-03-29 09:11 .#randstate.pyx -> cwitty@magnetar.newtonlabs.com.3701:1202495200\n```\n\n\nThe doctest runner tried to doctest \".#randstate.pyx\" and got this error message:\n\n```\nException in thread Thread-3:\nTraceback (most recent call last):\n  File \"/home/cwitty/sage/local/lib/python2.5/threading.py\", line 460, in __bootstrap\n    self.run()\n  File \"/home/cwitty/sage/local/bin/sage-ptest\", line 70, in run\n    e = test(F, 'doctest '+opts)\n  File \"/home/cwitty/sage/local/bin/sage-ptest\", line 140, in test\n    if not skip(F):\n  File \"/home/cwitty/sage/local/bin/sage-ptest\", line 116, in skip\n    G = abspath(F)\n  File \"/home/cwitty/sage/local/bin/sage-ptest\", line 86, in abspath\n    return strip_automount_prefix(os.path.abspath(x))\n  File \"/home/cwitty/sage/local/bin/sage-ptest\", line 103, in strip_automount_prefix\n    inode1 = os.stat(filename)[1]\nOSError: [Errno 2] No such file or directory: '/home/cwitty/sage/devel/sage-mq/sage/misc/.#randstate.pyx'\n```\n\n\nThere are a couple of problems here.\n\n1) I'm guessing that this crashed this doctest-running thread, so that I was running with one fewer thread than I wanted for the rest of the test run.\n\n2) The problem did not show up in the report at the end of the run.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2721\n\n",
    "created_at": "2008-03-29T17:23:13Z",
    "labels": [
        "doctest coverage",
        "major",
        "bug"
    ],
    "title": "parallel doctest not robust against filesystem issues",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2721",
    "user": "cwitty"
}
```
Assignee: failure

I ran a parallel doctest while I was editing a file in Emacs.  Evidently Emacs creates strange symlinks that point to nowhere as a file locking mechanism:

```
lrwxrwxrwx 1 cwitty cwitty     46 2008-03-29 09:11 .#randstate.pyx -> cwitty@magnetar.newtonlabs.com.3701:1202495200
```


The doctest runner tried to doctest ".#randstate.pyx" and got this error message:

```
Exception in thread Thread-3:
Traceback (most recent call last):
  File "/home/cwitty/sage/local/lib/python2.5/threading.py", line 460, in __bootstrap
    self.run()
  File "/home/cwitty/sage/local/bin/sage-ptest", line 70, in run
    e = test(F, 'doctest '+opts)
  File "/home/cwitty/sage/local/bin/sage-ptest", line 140, in test
    if not skip(F):
  File "/home/cwitty/sage/local/bin/sage-ptest", line 116, in skip
    G = abspath(F)
  File "/home/cwitty/sage/local/bin/sage-ptest", line 86, in abspath
    return strip_automount_prefix(os.path.abspath(x))
  File "/home/cwitty/sage/local/bin/sage-ptest", line 103, in strip_automount_prefix
    inode1 = os.stat(filename)[1]
OSError: [Errno 2] No such file or directory: '/home/cwitty/sage/devel/sage-mq/sage/misc/.#randstate.pyx'
```


There are a couple of problems here.

1) I'm guessing that this crashed this doctest-running thread, so that I was running with one fewer thread than I wanted for the rest of the test run.

2) The problem did not show up in the report at the end of the run.


Issue created by migration from https://trac.sagemath.org/ticket/2721





---

archive/issue_comments_018759.json:
```json
{
    "body": "Attachment\n\nLooks good; I tested a couple of things (including my original problem case) and couldn't make it fail.",
    "created_at": "2008-03-29T21:32:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2721",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2721#issuecomment-18759",
    "user": "cwitty"
}
```

Attachment

Looks good; I tested a couple of things (including my original problem case) and couldn't make it fail.



---

archive/issue_comments_018760.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-29T21:34:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2721",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2721#issuecomment-18760",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_018761.json:
```json
{
    "body": "Merged in Sage 2.11.rc0",
    "created_at": "2008-03-29T21:34:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2721",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2721#issuecomment-18761",
    "user": "mabshoff"
}
```

Merged in Sage 2.11.rc0
