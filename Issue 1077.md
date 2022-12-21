# Issue 1077: DSage restarts two workers after timeout

Issue created by migration from Trac.

Original creator: jvoight

Original creation time: 2007-11-03 17:07:55

Assignee: was

When a job times out, the worker restarts running two jobs.  This slows things down and is not natural.

And when one of those new jobs finishes, it performs a hard reset, killing the second job, which then never gets completed.


---

Comment by yi created at 2007-11-03 17:33:42

Changing assignee from was to yi.


---

Comment by yi created at 2007-11-08 05:38:20

Could you please elaborate?  What do you mean it restarts running two jobs? Currently the job timing out counts as a failure and by default each job has a failure threshold of 3 (i.e. it will fail three times before being removed from the job queue).  Unfortunately there is no easy way to change that until now.  If you launch the server like this:

dsage.server(job_failure_threshold=0), this means that each job will only fail once before it is removed from the queue.  Find the bundle here:

http://sage.math.washington.edu/home/yqiang/dsage.hg

Please report back if this does not fix the problem for you.


---

Comment by jvoight created at 2007-11-08 05:45:18

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

Comment by yi created at 2007-11-12 01:03:58

This is fixed.  Find the bundle here:

http://sage.math.washington.edu/home/yqiang/dsage_latest.hg


---

Comment by yi created at 2007-11-12 01:06:55

Changing status from new to assigned.


---

Comment by mabshoff created at 2007-11-20 14:45:28

Yi, could you please provide a patch or bundle once 2.8.13 is out. If I try the bundle above it complains about unknown parent and it is unclear to me whether to apply the other bundle first.

Cheers,

Michael


---

Comment by yi created at 2007-12-01 04:14:59

I've uploaded

http://sage.math.washington.edu/home/yqiang/dsage_latest.hg

Which is a bundle against 2.8.14.


---

Comment by mabshoff created at 2007-12-15 00:37:34

Resolution: fixed


---

Comment by mabshoff created at 2007-12-15 00:37:34

Merged in 2.9.rc0.
