# Issue 9473: notebook: execute bit set on pickle's, but shouldn't be (really easy to fix)

archive/issues_009473.json:
```json
{
    "body": "Assignee: jason, was\n\nCC:  chapoton\n\nThe execute bit is set on some pickles in sage_notebook.sagenb for no reason:\n\n```\n\nexecutable bit set?  huh?\n\nsage: !ls -l\ntotal 28\n-rwx------  1 sagenb sagenb   253 2010-07-06 00:52 conf.pickle\ndrwxr-xr-x 39 sagenb sagenb  4096 2010-05-22 08:58 home\n-rw-r--r--  1 sagenb sagenb     4 2010-05-20 12:04 twistd.pid\n-rw-r--r--  1 sagenb sagenb  2560 2010-05-20 12:04 twistedconf.tac\n-rwx------  1 sagenb sagenb 11116 2010-07-06 00:52 users.pickle\n```\n\n\nFix this.   This is probably really easy.   I think the notebook server does a chmod somewhere to make sure other and group don't have access, and this is done incorrectly.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9473\n\n",
    "created_at": "2010-07-11T08:51:04Z",
    "labels": [
        "notebook",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "notebook: execute bit set on pickle's, but shouldn't be (really easy to fix)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9473",
    "user": "was"
}
```
Assignee: jason, was

CC:  chapoton

The execute bit is set on some pickles in sage_notebook.sagenb for no reason:

```

executable bit set?  huh?

sage: !ls -l
total 28
-rwx------  1 sagenb sagenb   253 2010-07-06 00:52 conf.pickle
drwxr-xr-x 39 sagenb sagenb  4096 2010-05-22 08:58 home
-rw-r--r--  1 sagenb sagenb     4 2010-05-20 12:04 twistd.pid
-rw-r--r--  1 sagenb sagenb  2560 2010-05-20 12:04 twistedconf.tac
-rwx------  1 sagenb sagenb 11116 2010-07-06 00:52 users.pickle
```


Fix this.   This is probably really easy.   I think the notebook server does a chmod somewhere to make sure other and group don't have access, and this is done incorrectly.

Issue created by migration from https://trac.sagemath.org/ticket/9473





---

archive/issue_comments_090864.json:
```json
{
    "body": "Proposing to close all sagenb tickets as outdated, so that all remaining open tickets in the notebook component are about the Jupyter notebook.",
    "created_at": "2020-08-18T00:36:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9473",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9473#issuecomment-90864",
    "user": "mkoeppe"
}
```

Proposing to close all sagenb tickets as outdated, so that all remaining open tickets in the notebook component are about the Jupyter notebook.



---

archive/issue_comments_090865.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2020-08-18T00:36:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9473",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9473#issuecomment-90865",
    "user": "mkoeppe"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_090866.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2020-09-08T09:48:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9473",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9473#issuecomment-90866",
    "user": "chapoton"
}
```

Resolution: invalid
