# Issue 2606: command line option to kill a background notebook

archive/issues_002606.json:
```json
{
    "body": "Assignee: boothby\n\nSince running sage -notebook now checks if another instance is already running, it would be fairly straightforward to create an option that kills that notebook process as well.\n\nThe rationale is that it is probably much easier for a user to recreate the circumstances under which the notebook was started, and hence enable sage to find the relevant PID file, than to figure out where that PID file is stored.\n\nGiven the code in sage.server.notebook.run_notebook it can be rather involved to track down where twistd.pid gets stored (and it might change in the future too), being able to get a hold of the pidfile in a general way would make startup scripts much more robust (the location of twistd.pid has already changed once)\n\nAs an example, daemon-like services such as vncserver and dhclient have \"-kill\" and \"-r\" options to kill previously started instances in a way that takes the burden from the user to figure out which PID to kill.\n\nOne should probably first address\n\nhttp://trac.sagemath.org/sage_trac/ticket/2359\n\nIssue created by migration from https://trac.sagemath.org/ticket/2606\n\n",
    "created_at": "2008-03-19T22:06:09Z",
    "labels": [
        "component: notebook",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "command line option to kill a background notebook",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2606",
    "user": "https://github.com/nbruin"
}
```
Assignee: boothby

Since running sage -notebook now checks if another instance is already running, it would be fairly straightforward to create an option that kills that notebook process as well.

The rationale is that it is probably much easier for a user to recreate the circumstances under which the notebook was started, and hence enable sage to find the relevant PID file, than to figure out where that PID file is stored.

Given the code in sage.server.notebook.run_notebook it can be rather involved to track down where twistd.pid gets stored (and it might change in the future too), being able to get a hold of the pidfile in a general way would make startup scripts much more robust (the location of twistd.pid has already changed once)

As an example, daemon-like services such as vncserver and dhclient have "-kill" and "-r" options to kill previously started instances in a way that takes the burden from the user to figure out which PID to kill.

One should probably first address

http://trac.sagemath.org/sage_trac/ticket/2359

Issue created by migration from https://trac.sagemath.org/ticket/2606





---

archive/issue_comments_017777.json:
```json
{
    "body": "Can you suggest a very specific design?  E.g.,\n\n```\nsage: notebook.killall()\n... kills all running notebook servers\nsage: notebook.pids()\n... shows pids' of all running notebook servers\nsage: notebook.urls()\n... shows urls...\n```\n\n\nWhat do you think?",
    "created_at": "2008-03-19T22:49:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2606",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2606#issuecomment-17777",
    "user": "https://github.com/williamstein"
}
```

Can you suggest a very specific design?  E.g.,

```
sage: notebook.killall()
... kills all running notebook servers
sage: notebook.pids()
... shows pids' of all running notebook servers
sage: notebook.urls()
... shows urls...
```


What do you think?



---

archive/issue_comments_017778.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2020-03-29T02:12:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2606",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2606#issuecomment-17778",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Resolution: invalid



---

archive/issue_comments_017779.json:
```json
{
    "body": "Closing deprecated notebook tickets",
    "created_at": "2020-03-29T02:12:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2606",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2606#issuecomment-17779",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Closing deprecated notebook tickets
