# Issue 431: dsage server hangs

Issue created by migration from https://trac.sagemath.org/ticket/431

Original creator: rlm

Original creation time: 2007-08-16 03:12:35

Assignee: rlm

Apparently, a large number of jobs in a small time can cause the dsage server to hang, while there are waiting jobs and workers. 


---

Comment by yi created at 2007-08-16 17:25:55

Changing assignee from rlm to yi.


---

Comment by yi created at 2007-08-16 17:25:55

Please include as much information as you can on this bug, including repro steps.


---

Comment by yi created at 2007-08-19 17:03:30

Problem seems to be a race condition between the task that downloads new jobs and the task that checks for results.  A temporary fix is to introduce a 1 second delay to all jobs to make sure this race condition doesn't happen.


---

Comment by rlm created at 2007-09-20 23:42:07


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

Comment by rlm created at 2007-11-01 21:56:33

This seems to have been fixed by one of Yi's patches.


---

Comment by mabshoff created at 2007-11-01 22:21:00

Fixed by an earlier patch of Yi according to the original reporter.


---

Comment by mabshoff created at 2007-11-01 22:21:00

Resolution: fixed
