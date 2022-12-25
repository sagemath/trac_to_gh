# Issue 139: automatic dependency checking for pyrex files

archive/issues_000139.json:
```json
{
    "body": "Assignee: @williamstein\n\nAdd code to devel/sage/setup.py so that a Pyrex file is pyrexed if it\nchanges *or* if any pxd file that it cimports changes.\n\nIssue created by migration from https://trac.sagemath.org/ticket/139\n\n",
    "created_at": "2006-10-20T01:08:54Z",
    "labels": [
        "component: user interface",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.3",
    "title": "automatic dependency checking for pyrex files",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/139",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

Add code to devel/sage/setup.py so that a Pyrex file is pyrexed if it
changes *or* if any pxd file that it cimports changes.

Issue created by migration from https://trac.sagemath.org/ticket/139





---

archive/issue_comments_000645.json:
```json
{
    "body": "It would also be good to check any .pxi files that are included. Maybe even any .h files that are referenced, because the C file compilation will depend on this too.",
    "created_at": "2006-10-20T01:20:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/139",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/139#issuecomment-645",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```

It would also be good to check any .pxi files that are included. Maybe even any .h files that are referenced, because the C file compilation will depend on this too.



---

archive/issue_comments_000646.json:
```json
{
    "body": "I've made a change so when you do a \"sage -upgrade\" all .pyx files get rebuilt.  This is obviously slower, but will avoid a lot of stupid confusion for now.",
    "created_at": "2006-10-21T01:26:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/139",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/139#issuecomment-646",
    "user": "https://github.com/williamstein"
}
```

I've made a change so when you do a "sage -upgrade" all .pyx files get rebuilt.  This is obviously slower, but will avoid a lot of stupid confusion for now.



---

archive/issue_comments_000647.json:
```json
{
    "body": "* Checking for dependencies on .h files doesn't work at all.\n\n* Recursive dependencies don't work, i.e., if a depends on b and b on c, and\nc changes, then a isn't rebuilt.",
    "created_at": "2006-10-26T04:36:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/139",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/139#issuecomment-647",
    "user": "https://github.com/williamstein"
}
```

* Checking for dependencies on .h files doesn't work at all.

* Recursive dependencies don't work, i.e., if a depends on b and b on c, and
c changes, then a isn't rebuilt.



---

archive/issue_comments_000648.json:
```json
{
    "body": "Is this still a valid ticket? We do check dependencies now, right?",
    "created_at": "2008-02-26T23:57:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/139",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/139#issuecomment-648",
    "user": "https://github.com/malb"
}
```

Is this still a valid ticket? We do check dependencies now, right?



---

archive/issue_comments_000649.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-27T12:21:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/139",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/139#issuecomment-649",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_comments_000650.json:
```json
{
    "body": "I implemented this and forgot to close the ticket.",
    "created_at": "2008-02-27T12:21:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/139",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/139#issuecomment-650",
    "user": "https://github.com/williamstein"
}
```

I implemented this and forgot to close the ticket.
