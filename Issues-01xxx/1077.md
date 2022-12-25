# Issue 1077: [with patch, with positive review] DSage restarts two workers after timeout

archive/issues_001077.json:
```json
{
    "body": "Assignee: @yqiang\n\nWhen a job times out, the worker restarts running two jobs.  This slows things down and is not natural.\n\nAnd when one of those new jobs finishes, it performs a hard reset, killing the second job, which then never gets completed.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1077\n\n",
    "closed_at": "2007-12-15T00:37:34Z",
    "created_at": "2007-11-03T17:07:55Z",
    "labels": [
        "component: packages: standard",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.9",
    "title": "[with patch, with positive review] DSage restarts two workers after timeout",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1077",
    "user": "https://github.com/jvoight"
}
```
Assignee: @yqiang

When a job times out, the worker restarts running two jobs.  This slows things down and is not natural.

And when one of those new jobs finishes, it performs a hard reset, killing the second job, which then never gets completed.

Issue created by migration from https://trac.sagemath.org/ticket/1077





---

archive/issue_comments_006495.json:
```json
{
    "body": "Changing assignee from @williamstein to @yqiang.",
    "created_at": "2007-11-03T17:33:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1077",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1077#issuecomment-6495",
    "user": "https://github.com/yqiang"
}
```

Changing assignee from @williamstein to @yqiang.



---

archive/issue_events_002914.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-11-03T23:49:46Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1077",
    "milestone": "sage-2.9",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1077#event-2914"
}
```



---

archive/issue_comments_006496.json:
```json
{
    "body": "Could you please elaborate?  What do you mean it restarts running two jobs? Currently the job timing out counts as a failure and by default each job has a failure threshold of 3 (i.e. it will fail three times before being removed from the job queue).  Unfortunately there is no easy way to change that until now.  If you launch the server like this:\n\ndsage.server(job_failure_threshold=0), this means that each job will only fail once before it is removed from the queue.  Find the bundle here:\n\nhttp://sage.math.washington.edu/home/yqiang/dsage.hg\n\nPlease report back if this does not fix the problem for you.",
    "created_at": "2007-11-08T05:38:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1077",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1077#issuecomment-6496",
    "user": "https://github.com/yqiang"
}
```

Could you please elaborate?  What do you mean it restarts running two jobs? Currently the job timing out counts as a failure and by default each job has a failure threshold of 3 (i.e. it will fail three times before being removed from the job queue).  Unfortunately there is no easy way to change that until now.  If you launch the server like this:

dsage.server(job_failure_threshold=0), this means that each job will only fail once before it is removed from the queue.  Find the bundle here:

http://sage.math.washington.edu/home/yqiang/dsage.hg

Please report back if this does not fix the problem for you.



---

archive/issue_comments_006497.json:
```json
{
    "body": "Here's an example output.  How can worker 0 be working on two jobs at once?  \n\n2007/11/07 22:28 -0700 [-] [Worker 0] Job COZkyk31Am failed!\n2007/11/07 22:28 -0700 [-] Traceback:\n        Traceback (most recent call last):\n          File \"<stdin>\", line 1, in <module>\n          File \"/home/jvoight/.sage/dsage/tmp_worker_files/COZkyk31Am/default_job.py\", line 8, in <module>\n            DSAGE_RESULT=enumerate_totallyreal_fields(Integer(9),Integer(28334269485),[Integer(70), Integer(1), -Integer(15), Integer(0), Integer(1)],return_seqs=True)\n          File \"/home/jvoight/sage/local/lib/python2.5/site-packages/sage/rings/number_field/totallyreal.py\", line 225, in enumerate_totallyreal_fields\n            [zk,d] = nf.nfbasis_d()\n          File \"/home/jvoight/sage/local/lib/python2.5/site-packages/sage/misc/misc.py\", line 1300, in __mysig\n            raise KeyboardInterrupt, \"computation timed out because alarm was set for %s seconds\"%__alarm_time\n        KeyboardInterrupt: computation timed out because alarm was set for 1800 seconds\n\n2007/11/07 22:28 -0700 [-] [Worker 0] Performing hard reset.\n2007/11/07 22:28 -0700 [-] [Worker: 0] Restarting...\n2007/11/07 22:28 -0700 [Broker,client] [Worker 0] Starting job kLm2hihd1N\n2007/11/07 22:28 -0700 [Broker,client] [Worker 0] Starting job jUtQDMnlOG",
    "created_at": "2007-11-08T05:45:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1077",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1077#issuecomment-6497",
    "user": "https://github.com/jvoight"
}
```

Here's an example output.  How can worker 0 be working on two jobs at once?  

2007/11/07 22:28 -0700 [-] [Worker 0] Job COZkyk31Am failed!
2007/11/07 22:28 -0700 [-] Traceback:
        Traceback (most recent call last):
          File "<stdin>", line 1, in <module>
          File "/home/jvoight/.sage/dsage/tmp_worker_files/COZkyk31Am/default_job.py", line 8, in <module>
            DSAGE_RESULT=enumerate_totallyreal_fields(Integer(9),Integer(28334269485),[Integer(70), Integer(1), -Integer(15), Integer(0), Integer(1)],return_seqs=True)
          File "/home/jvoight/sage/local/lib/python2.5/site-packages/sage/rings/number_field/totallyreal.py", line 225, in enumerate_totallyreal_fields
            [zk,d] = nf.nfbasis_d()
          File "/home/jvoight/sage/local/lib/python2.5/site-packages/sage/misc/misc.py", line 1300, in __mysig
            raise KeyboardInterrupt, "computation timed out because alarm was set for %s seconds"%__alarm_time
        KeyboardInterrupt: computation timed out because alarm was set for 1800 seconds

2007/11/07 22:28 -0700 [-] [Worker 0] Performing hard reset.
2007/11/07 22:28 -0700 [-] [Worker: 0] Restarting...
2007/11/07 22:28 -0700 [Broker,client] [Worker 0] Starting job kLm2hihd1N
2007/11/07 22:28 -0700 [Broker,client] [Worker 0] Starting job jUtQDMnlOG



---

archive/issue_events_002915.json:
```json
{
    "actor": "https://github.com/yqiang",
    "created_at": "2007-11-12T01:03:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1077",
    "milestone": "sage-2.9",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1077#event-2915"
}
```



---

archive/issue_events_002916.json:
```json
{
    "actor": "https://github.com/yqiang",
    "created_at": "2007-11-12T01:03:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1077",
    "milestone": "sage-2.8.13",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1077#event-2916"
}
```



---

archive/issue_comments_006498.json:
```json
{
    "body": "This is fixed.  Find the bundle here:\n\nhttp://sage.math.washington.edu/home/yqiang/dsage_latest.hg",
    "created_at": "2007-11-12T01:03:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1077",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1077#issuecomment-6498",
    "user": "https://github.com/yqiang"
}
```

This is fixed.  Find the bundle here:

http://sage.math.washington.edu/home/yqiang/dsage_latest.hg



---

archive/issue_comments_006499.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-11-12T01:06:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1077",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1077#issuecomment-6499",
    "user": "https://github.com/yqiang"
}
```

Changing status from new to assigned.



---

archive/issue_comments_006500.json:
```json
{
    "body": "Yi, could you please provide a patch or bundle once 2.8.13 is out. If I try the bundle above it complains about unknown parent and it is unclear to me whether to apply the other bundle first.\n\nCheers,\n\nMichael",
    "created_at": "2007-11-20T14:45:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1077",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1077#issuecomment-6500",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Yi, could you please provide a patch or bundle once 2.8.13 is out. If I try the bundle above it complains about unknown parent and it is unclear to me whether to apply the other bundle first.

Cheers,

Michael



---

archive/issue_comments_006501.json:
```json
{
    "body": "I've uploaded\n\nhttp://sage.math.washington.edu/home/yqiang/dsage_latest.hg\n\nWhich is a bundle against 2.8.14.",
    "created_at": "2007-12-01T04:14:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1077",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1077#issuecomment-6501",
    "user": "https://github.com/yqiang"
}
```

I've uploaded

http://sage.math.washington.edu/home/yqiang/dsage_latest.hg

Which is a bundle against 2.8.14.



---

archive/issue_comments_006502.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-15T00:37:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1077",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1077#issuecomment-6502",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_002917.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-12-15T00:37:34Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1077",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1077#event-2917"
}
```



---

archive/issue_comments_006503.json:
```json
{
    "body": "Merged in 2.9.rc0.",
    "created_at": "2007-12-15T00:37:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1077",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1077#issuecomment-6503",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in 2.9.rc0.
