# Issue 431: dsage server hangs

archive/issues_000431.json:
```json
{
    "body": "Assignee: @rlmill\n\nApparently, a large number of jobs in a small time can cause the dsage server to hang, while there are waiting jobs and workers. \n\nIssue created by migration from https://trac.sagemath.org/ticket/431\n\n",
    "created_at": "2007-08-16T03:12:35Z",
    "labels": [
        "component: interfaces",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.11",
    "title": "dsage server hangs",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/431",
    "user": "https://github.com/rlmill"
}
```
Assignee: @rlmill

Apparently, a large number of jobs in a small time can cause the dsage server to hang, while there are waiting jobs and workers. 

Issue created by migration from https://trac.sagemath.org/ticket/431





---

archive/issue_comments_002149.json:
```json
{
    "body": "Changing assignee from @rlmill to @yqiang.",
    "created_at": "2007-08-16T17:25:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/431",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/431#issuecomment-2149",
    "user": "https://github.com/yqiang"
}
```

Changing assignee from @rlmill to @yqiang.



---

archive/issue_comments_002150.json:
```json
{
    "body": "Please include as much information as you can on this bug, including repro steps.",
    "created_at": "2007-08-16T17:25:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/431",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/431#issuecomment-2150",
    "user": "https://github.com/yqiang"
}
```

Please include as much information as you can on this bug, including repro steps.



---

archive/issue_comments_002151.json:
```json
{
    "body": "Problem seems to be a race condition between the task that downloads new jobs and the task that checks for results.  A temporary fix is to introduce a 1 second delay to all jobs to make sure this race condition doesn't happen.",
    "created_at": "2007-08-19T17:03:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/431",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/431#issuecomment-2151",
    "user": "https://github.com/yqiang"
}
```

Problem seems to be a race condition between the task that downloads new jobs and the task that checks for results.  A temporary fix is to introduce a 1 second delay to all jobs to make sure this race condition doesn't happen.



---

archive/issue_comments_002152.json:
```json
{
    "body": "\n```\nReproduction steps ( takes about 6 hours ... )\n\nrlmill@sage:~/sage-2.8.4.1$ ./sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n| SAGE Version 2.8.4.2.1, Release Date: 2007-09-20                   |\n| Type notebook() for the GUI, and license() for information.        |\nsage: d = dsage.start_all()\nSpawned dsage_server.py -d /home/rlmill/.sage/dsage/db/dsage.db -p 8081 -l 0 -f /home/rlmill/.sage/dsage/server.log -c /home/rlmill/.sage/dsage/pubcert.pem -k /home/rlmill/.sage/dsage/cacert.pem --statsfile=/home/rlmill/.sage/dsage/dsage.xml --ssl --noblock (pid = 25908)\n\nSpawned dsage_worker.py -s localhost -p 8081 -u rlmill -w 2 --poll 1.0 -l 0 -f /home/rlmill/.sage/dsage/worker.log --privkey=/home/rlmill/.sage/dsage/dsage_key --pubkey=/home/rlmill/.sage/dsage/dsage_key.pub --priority=20  --ssl --noblock (pid = 25911)\n\nsage: import sage.graphs.bruhat_sn\nsage: from sage.graphs.bruhat_sn import DistributedBruhatIntervals, BruhatDatabase\nsage: db = BruhatDatabase('/home/rlmill/database.db')\nsage: dbi = DistributedBruhatIntervals(d, db)\nsage: dbi.start()\n```\n",
    "created_at": "2007-09-20T23:42:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/431",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/431#issuecomment-2152",
    "user": "https://github.com/rlmill"
}
```


```
Reproduction steps ( takes about 6 hours ... )

rlmill@sage:~/sage-2.8.4.1$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 2.8.4.2.1, Release Date: 2007-09-20                   |
| Type notebook() for the GUI, and license() for information.        |
sage: d = dsage.start_all()
Spawned dsage_server.py -d /home/rlmill/.sage/dsage/db/dsage.db -p 8081 -l 0 -f /home/rlmill/.sage/dsage/server.log -c /home/rlmill/.sage/dsage/pubcert.pem -k /home/rlmill/.sage/dsage/cacert.pem --statsfile=/home/rlmill/.sage/dsage/dsage.xml --ssl --noblock (pid = 25908)

Spawned dsage_worker.py -s localhost -p 8081 -u rlmill -w 2 --poll 1.0 -l 0 -f /home/rlmill/.sage/dsage/worker.log --privkey=/home/rlmill/.sage/dsage/dsage_key --pubkey=/home/rlmill/.sage/dsage/dsage_key.pub --priority=20  --ssl --noblock (pid = 25911)

sage: import sage.graphs.bruhat_sn
sage: from sage.graphs.bruhat_sn import DistributedBruhatIntervals, BruhatDatabase
sage: db = BruhatDatabase('/home/rlmill/database.db')
sage: dbi = DistributedBruhatIntervals(d, db)
sage: dbi.start()
```




---

archive/issue_comments_002153.json:
```json
{
    "body": "This seems to have been fixed by one of Yi's patches.",
    "created_at": "2007-11-01T21:56:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/431",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/431#issuecomment-2153",
    "user": "https://github.com/rlmill"
}
```

This seems to have been fixed by one of Yi's patches.



---

archive/issue_comments_002154.json:
```json
{
    "body": "Fixed by an earlier patch of Yi according to the original reporter.",
    "created_at": "2007-11-01T22:21:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/431",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/431#issuecomment-2154",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Fixed by an earlier patch of Yi according to the original reporter.



---

archive/issue_events_000458.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-11-01T22:21:00Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/431",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/431#event-458"
}
```



---

archive/issue_comments_002155.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-11-01T22:21:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/431",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/431#issuecomment-2155",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
