# Issue 667: Fix DSage on Solaris 10

Issue created by migration from https://trac.sagemath.org/ticket/667

Original creator: mabshoff

Original creation time: 2007-09-17 00:26:09

Assignee: Yi

Keywords: DSage, Solaris

Hello,

on my Solaris 10 box I have the following failure during the DSage test:

```
sage.dsage.twisted.tests.test_remote
  ClientRemoteCallsTest
    testremoteSubmitBadJob ...                                             [OK]
    testremoteSubmitJob ...                                                [OK]
  MonitorRemoteCallsTest
    testget_killed_jobs_list ...                                        [ERROR]
                                       [ERROR]
    testremote_get_job ...                                              [ERROR]
                                             [ERROR]
    testremote_job_done ...                                             [ERROR]
                                            [ERROR]
    testremote_job_failed ...                                           [ERROR]
                                          [ERROR]

===============================================================================
[ERROR]: sage.dsage.twisted.tests.test_remote.MonitorRemoteCallsTest.testget_killed_jobs_list

Traceback from remote host -- Traceback unavailable
===============================================================================
[ERROR]: sage.dsage.twisted.tests.test_remote.MonitorRemoteCallsTest.testget_killed_jobs_list

Traceback (most recent call last):
  File "/export/home/mabshoff/sage-2.8.4.2/local/lib/python2.5/site-packages/sage/dsage/twisted/pb.py", line 412, in requestAvatar
    avatar.attached(avatar, mind)
  File "/export/home/mabshoff/sage-2.8.4.2/local/lib/python2.5/site-packages/sage/dsage/twisted/pb.py", line 258, in attached
    self.DSageServer.monitordb.add_monitor(self.host_info)
  File "/export/home/mabshoff/sage-2.8.4.2/local/lib/python2.5/site-packages/sage/dsage/database/monitordb.py", line 113, in add_monitor
    hostname = host_info['hostname']
exceptions.KeyError: 'hostname'
===============================================================================
[ERROR]: sage.dsage.twisted.tests.test_remote.MonitorRemoteCallsTest.testremote_get_job

Traceback from remote host -- Traceback unavailable
===============================================================================
[ERROR]: sage.dsage.twisted.tests.test_remote.MonitorRemoteCallsTest.testremote_get_job

Traceback (most recent call last):
  File "/export/home/mabshoff/sage-2.8.4.2/local/lib/python2.5/site-packages/sage/dsage/twisted/pb.py", line 412, in requestAvatar
    avatar.attached(avatar, mind)
  File "/export/home/mabshoff/sage-2.8.4.2/local/lib/python2.5/site-packages/sage/dsage/twisted/pb.py", line 258, in attached
    self.DSageServer.monitordb.add_monitor(self.host_info)
  File "/export/home/mabshoff/sage-2.8.4.2/local/lib/python2.5/site-packages/sage/dsage/database/monitordb.py", line 113, in add_monitor
    hostname = host_info['hostname']
exceptions.KeyError: 'hostname'
===============================================================================
[ERROR]: sage.dsage.twisted.tests.test_remote.MonitorRemoteCallsTest.testremote_job_done

Traceback from remote host -- Traceback unavailable
===============================================================================
[ERROR]: sage.dsage.twisted.tests.test_remote.MonitorRemoteCallsTest.testremote_job_done

Traceback (most recent call last):
  File "/export/home/mabshoff/sage-2.8.4.2/local/lib/python2.5/site-packages/sage/dsage/twisted/pb.py", line 412, in requestAvatar
    avatar.attached(avatar, mind)
  File "/export/home/mabshoff/sage-2.8.4.2/local/lib/python2.5/site-packages/sage/dsage/twisted/pb.py", line 258, in attached
    self.DSageServer.monitordb.add_monitor(self.host_info)
  File "/export/home/mabshoff/sage-2.8.4.2/local/lib/python2.5/site-packages/sage/dsage/database/monitordb.py", line 113, in add_monitor
    hostname = host_info['hostname']
exceptions.KeyError: 'hostname'
===============================================================================
[ERROR]: sage.dsage.twisted.tests.test_remote.MonitorRemoteCallsTest.testremote_job_failed

Traceback from remote host -- Traceback unavailable
===============================================================================
[ERROR]: sage.dsage.twisted.tests.test_remote.MonitorRemoteCallsTest.testremote_job_failed

Traceback (most recent call last):
  File "/export/home/mabshoff/sage-2.8.4.2/local/lib/python2.5/site-packages/sage/dsage/twisted/pb.py", line 412, in requestAvatar
    avatar.attached(avatar, mind)
  File "/export/home/mabshoff/sage-2.8.4.2/local/lib/python2.5/site-packages/sage/dsage/twisted/pb.py", line 258, in attached
    self.DSageServer.monitordb.add_monitor(self.host_info)
  File "/export/home/mabshoff/sage-2.8.4.2/local/lib/python2.5/site-packages/sage/dsage/database/monitordb.py", line 113, in add_monitor
    hostname = host_info['hostname']
exceptions.KeyError: 'hostname'
-------------------------------------------------------------------------------
Ran 50 tests in 8.508s
```


Interestingly enough that doctest works perfectly fine on Solaris 9

Cheers,

Michael


---

Comment by mabshoff created at 2007-09-17 01:22:58

Changing component from packages to doctest.


---

Comment by mabshoff created at 2007-09-17 05:19:29


```
-bash-3.00$ python
Python 2.5.1 (r251:54863, Sep 17 2007, 01:21:26)
[GCC 4.2.1] on sunos5
Type "help", "copyright", "credits" or "license" for more information.
>>> import sys
>>> print sys.platform
sunos5
```



---

Comment by yi created at 2007-09-21 18:49:54

I'm changing the priority of this bug since the Solaris port is not even ready yet.


---

Comment by yi created at 2007-09-21 18:49:54

Changing priority from major to minor.


---

Comment by mabshoff created at 2008-07-31 03:28:57

The DSage unit tests now work on Solaris 10:

```
-bash-3.00$ uname -a
SunOS fulvia 5.10 Generic_127128-11 i86pc i386 i86pc
-bash-3.00$ \sage-dsage-trial
dsage-trial tmp directory doesn't exist - creating ...
This script will run the unit tests for DSage
sage.dsage.database.tests.test_client
  ClientTestCase
    testGetPublicKey ...                                                   [OK]
    testGetUsername ...                                                    [OK]
    testInitClient ...                                                     [OK]
    testSetConnected ...                                                   [OK]
    testSetEnabled ...                                                     [OK]
sage.dsage.database.tests.test_clientdb
  ClientDatabaseSQLiteTestCase
    testadd_client ...                                                     [OK]
    testdel_client ...                                                     [OK]
    testset_enabled ...                                                    [OK]
    testupdate_login_time ...                                              [OK]
sage.dsage.database.tests.test_job
  JobTestCase
    testcreate_job ...                                                     [OK]
    testjobCreationTime ...                                                [OK]
    testjobFailures ...                                                    [OK]
    testjobFile ...                                                        [OK]
    testjobFinishTime ...                                                  [OK]
    testjobKilled ...                                                      [OK]
    testjobResult ...                                                      [OK]
    testjobStatus ...                                                      [OK]
    testjobUpdateTime ...                                                  [OK]
    testjob_id ...                                                         [OK]
sage.dsage.database.tests.test_jobdb
  JobDatabaseSATestCase
    testget_job ...                                                        [OK]
    teststore_jdict ...                                                    [OK]
  JobDatabaseSQLiteTestCase
    testcreate_jdict ...                                                   [OK]
    testget_job ...                                                        [OK]
    testget_job_by_id ...                                                  [OK]
    testget_killed_jobs_list ...                                           [OK]
    testhas_job ...                                                        [OK]
    teststore_jdict ...                                                    [OK]
sage.dsage.database.tests.test_workerdb
  WorkerDatabaseSATestCase
    testget_worker ...                                                     [OK]
    testget_worker_count ...                                               [OK]
    testinitial_sate ...                                                   [OK]
    testset_connected ...                                                  [OK]
sage.dsage.server.tests.test_server
  DSageServerTestCase
    testget_active_clients_list ...                                        [OK]
    testget_active_jobs ...                                                [OK]
    testget_all_jobs ...                                                   [OK]
    testget_job ...                                                        [OK]
    testget_job_by_id ...                                                  [OK]
    testget_job_result_by_id ...                                           [OK]
    testget_jobs_by_username ...                                           [OK]
    testget_killed_jobs_list ...                                           [OK]
    testjob_done ...                                                       [OK]
    testjob_failed ...                                                     [OK]
    testkill_job ...                                                       [OK]
    testsubmit_job ...                                                     [OK]
sage.dsage.twisted.tests.test_pubkeyauth
  PublicKeyCredentialsCheckerTest
    testanonymous_login ...                                                [OK]
    testget_pubkey_string ...                                              [OK]
    testrequestAvatarId ...                                                [OK]
sage.dsage.twisted.tests.test_remote
  ClientRemoteCallsTest
    testremoteSubmitBadJob ...                                             [OK]
    testremoteSubmitJob ...                                                [OK]
  WorkerRemoteCallsTest
    testget_killed_jobs_list ...                                           [OK]
    testremote_get_job ...                                                 [OK]
    testremote_job_done ...                                                [OK]
    testremote_job_failed ...                                              [OK]

-------------------------------------------------------------------------------
Ran 52 tests in 15.493s

PASSED (successes=52)
```



---

Comment by mabshoff created at 2008-07-31 03:28:57

Resolution: fixed
