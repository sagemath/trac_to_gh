# Issue 667: Fix DSage on Solaris 10

archive/issues_000667.json:
```json
{
    "body": "Assignee: Yi\n\nKeywords: DSage, Solaris\n\nHello,\n\non my Solaris 10 box I have the following failure during the DSage test:\n\n```\nsage.dsage.twisted.tests.test_remote\n  ClientRemoteCallsTest\n    testremoteSubmitBadJob ...                                             [OK]\n    testremoteSubmitJob ...                                                [OK]\n  MonitorRemoteCallsTest\n    testget_killed_jobs_list ...                                        [ERROR]\n                                       [ERROR]\n    testremote_get_job ...                                              [ERROR]\n                                             [ERROR]\n    testremote_job_done ...                                             [ERROR]\n                                            [ERROR]\n    testremote_job_failed ...                                           [ERROR]\n                                          [ERROR]\n\n===============================================================================\n[ERROR]: sage.dsage.twisted.tests.test_remote.MonitorRemoteCallsTest.testget_killed_jobs_list\n\nTraceback from remote host -- Traceback unavailable\n===============================================================================\n[ERROR]: sage.dsage.twisted.tests.test_remote.MonitorRemoteCallsTest.testget_killed_jobs_list\n\nTraceback (most recent call last):\n  File \"/export/home/mabshoff/sage-2.8.4.2/local/lib/python2.5/site-packages/sage/dsage/twisted/pb.py\", line 412, in requestAvatar\n    avatar.attached(avatar, mind)\n  File \"/export/home/mabshoff/sage-2.8.4.2/local/lib/python2.5/site-packages/sage/dsage/twisted/pb.py\", line 258, in attached\n    self.DSageServer.monitordb.add_monitor(self.host_info)\n  File \"/export/home/mabshoff/sage-2.8.4.2/local/lib/python2.5/site-packages/sage/dsage/database/monitordb.py\", line 113, in add_monitor\n    hostname = host_info['hostname']\nexceptions.KeyError: 'hostname'\n===============================================================================\n[ERROR]: sage.dsage.twisted.tests.test_remote.MonitorRemoteCallsTest.testremote_get_job\n\nTraceback from remote host -- Traceback unavailable\n===============================================================================\n[ERROR]: sage.dsage.twisted.tests.test_remote.MonitorRemoteCallsTest.testremote_get_job\n\nTraceback (most recent call last):\n  File \"/export/home/mabshoff/sage-2.8.4.2/local/lib/python2.5/site-packages/sage/dsage/twisted/pb.py\", line 412, in requestAvatar\n    avatar.attached(avatar, mind)\n  File \"/export/home/mabshoff/sage-2.8.4.2/local/lib/python2.5/site-packages/sage/dsage/twisted/pb.py\", line 258, in attached\n    self.DSageServer.monitordb.add_monitor(self.host_info)\n  File \"/export/home/mabshoff/sage-2.8.4.2/local/lib/python2.5/site-packages/sage/dsage/database/monitordb.py\", line 113, in add_monitor\n    hostname = host_info['hostname']\nexceptions.KeyError: 'hostname'\n===============================================================================\n[ERROR]: sage.dsage.twisted.tests.test_remote.MonitorRemoteCallsTest.testremote_job_done\n\nTraceback from remote host -- Traceback unavailable\n===============================================================================\n[ERROR]: sage.dsage.twisted.tests.test_remote.MonitorRemoteCallsTest.testremote_job_done\n\nTraceback (most recent call last):\n  File \"/export/home/mabshoff/sage-2.8.4.2/local/lib/python2.5/site-packages/sage/dsage/twisted/pb.py\", line 412, in requestAvatar\n    avatar.attached(avatar, mind)\n  File \"/export/home/mabshoff/sage-2.8.4.2/local/lib/python2.5/site-packages/sage/dsage/twisted/pb.py\", line 258, in attached\n    self.DSageServer.monitordb.add_monitor(self.host_info)\n  File \"/export/home/mabshoff/sage-2.8.4.2/local/lib/python2.5/site-packages/sage/dsage/database/monitordb.py\", line 113, in add_monitor\n    hostname = host_info['hostname']\nexceptions.KeyError: 'hostname'\n===============================================================================\n[ERROR]: sage.dsage.twisted.tests.test_remote.MonitorRemoteCallsTest.testremote_job_failed\n\nTraceback from remote host -- Traceback unavailable\n===============================================================================\n[ERROR]: sage.dsage.twisted.tests.test_remote.MonitorRemoteCallsTest.testremote_job_failed\n\nTraceback (most recent call last):\n  File \"/export/home/mabshoff/sage-2.8.4.2/local/lib/python2.5/site-packages/sage/dsage/twisted/pb.py\", line 412, in requestAvatar\n    avatar.attached(avatar, mind)\n  File \"/export/home/mabshoff/sage-2.8.4.2/local/lib/python2.5/site-packages/sage/dsage/twisted/pb.py\", line 258, in attached\n    self.DSageServer.monitordb.add_monitor(self.host_info)\n  File \"/export/home/mabshoff/sage-2.8.4.2/local/lib/python2.5/site-packages/sage/dsage/database/monitordb.py\", line 113, in add_monitor\n    hostname = host_info['hostname']\nexceptions.KeyError: 'hostname'\n-------------------------------------------------------------------------------\nRan 50 tests in 8.508s\n```\n\n\nInterestingly enough that doctest works perfectly fine on Solaris 9\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/667\n\n",
    "created_at": "2007-09-17T00:26:09Z",
    "labels": [
        "component: packages",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1",
    "title": "Fix DSage on Solaris 10",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/667",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
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

Issue created by migration from https://trac.sagemath.org/ticket/667





---

archive/issue_comments_003443.json:
```json
{
    "body": "Changing component from packages to doctest.",
    "created_at": "2007-09-17T01:22:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/667",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/667#issuecomment-3443",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing component from packages to doctest.



---

archive/issue_comments_003444.json:
```json
{
    "body": "\n```\n-bash-3.00$ python\nPython 2.5.1 (r251:54863, Sep 17 2007, 01:21:26)\n[GCC 4.2.1] on sunos5\nType \"help\", \"copyright\", \"credits\" or \"license\" for more information.\n>>> import sys\n>>> print sys.platform\nsunos5\n```\n",
    "created_at": "2007-09-17T05:19:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/667",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/667#issuecomment-3444",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```


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

archive/issue_comments_003445.json:
```json
{
    "body": "I'm changing the priority of this bug since the Solaris port is not even ready yet.",
    "created_at": "2007-09-21T18:49:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/667",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/667#issuecomment-3445",
    "user": "https://github.com/yqiang"
}
```

I'm changing the priority of this bug since the Solaris port is not even ready yet.



---

archive/issue_comments_003446.json:
```json
{
    "body": "Changing priority from major to minor.",
    "created_at": "2007-09-21T18:49:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/667",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/667#issuecomment-3446",
    "user": "https://github.com/yqiang"
}
```

Changing priority from major to minor.



---

archive/issue_comments_003447.json:
```json
{
    "body": "The DSage unit tests now work on Solaris 10:\n\n```\n-bash-3.00$ uname -a\nSunOS fulvia 5.10 Generic_127128-11 i86pc i386 i86pc\n-bash-3.00$ \\sage-dsage-trial\ndsage-trial tmp directory doesn't exist - creating ...\nThis script will run the unit tests for DSage\nsage.dsage.database.tests.test_client\n  ClientTestCase\n    testGetPublicKey ...                                                   [OK]\n    testGetUsername ...                                                    [OK]\n    testInitClient ...                                                     [OK]\n    testSetConnected ...                                                   [OK]\n    testSetEnabled ...                                                     [OK]\nsage.dsage.database.tests.test_clientdb\n  ClientDatabaseSQLiteTestCase\n    testadd_client ...                                                     [OK]\n    testdel_client ...                                                     [OK]\n    testset_enabled ...                                                    [OK]\n    testupdate_login_time ...                                              [OK]\nsage.dsage.database.tests.test_job\n  JobTestCase\n    testcreate_job ...                                                     [OK]\n    testjobCreationTime ...                                                [OK]\n    testjobFailures ...                                                    [OK]\n    testjobFile ...                                                        [OK]\n    testjobFinishTime ...                                                  [OK]\n    testjobKilled ...                                                      [OK]\n    testjobResult ...                                                      [OK]\n    testjobStatus ...                                                      [OK]\n    testjobUpdateTime ...                                                  [OK]\n    testjob_id ...                                                         [OK]\nsage.dsage.database.tests.test_jobdb\n  JobDatabaseSATestCase\n    testget_job ...                                                        [OK]\n    teststore_jdict ...                                                    [OK]\n  JobDatabaseSQLiteTestCase\n    testcreate_jdict ...                                                   [OK]\n    testget_job ...                                                        [OK]\n    testget_job_by_id ...                                                  [OK]\n    testget_killed_jobs_list ...                                           [OK]\n    testhas_job ...                                                        [OK]\n    teststore_jdict ...                                                    [OK]\nsage.dsage.database.tests.test_workerdb\n  WorkerDatabaseSATestCase\n    testget_worker ...                                                     [OK]\n    testget_worker_count ...                                               [OK]\n    testinitial_sate ...                                                   [OK]\n    testset_connected ...                                                  [OK]\nsage.dsage.server.tests.test_server\n  DSageServerTestCase\n    testget_active_clients_list ...                                        [OK]\n    testget_active_jobs ...                                                [OK]\n    testget_all_jobs ...                                                   [OK]\n    testget_job ...                                                        [OK]\n    testget_job_by_id ...                                                  [OK]\n    testget_job_result_by_id ...                                           [OK]\n    testget_jobs_by_username ...                                           [OK]\n    testget_killed_jobs_list ...                                           [OK]\n    testjob_done ...                                                       [OK]\n    testjob_failed ...                                                     [OK]\n    testkill_job ...                                                       [OK]\n    testsubmit_job ...                                                     [OK]\nsage.dsage.twisted.tests.test_pubkeyauth\n  PublicKeyCredentialsCheckerTest\n    testanonymous_login ...                                                [OK]\n    testget_pubkey_string ...                                              [OK]\n    testrequestAvatarId ...                                                [OK]\nsage.dsage.twisted.tests.test_remote\n  ClientRemoteCallsTest\n    testremoteSubmitBadJob ...                                             [OK]\n    testremoteSubmitJob ...                                                [OK]\n  WorkerRemoteCallsTest\n    testget_killed_jobs_list ...                                           [OK]\n    testremote_get_job ...                                                 [OK]\n    testremote_job_done ...                                                [OK]\n    testremote_job_failed ...                                              [OK]\n\n-------------------------------------------------------------------------------\nRan 52 tests in 15.493s\n\nPASSED (successes=52)\n```\n",
    "created_at": "2008-07-31T03:28:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/667",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/667#issuecomment-3447",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

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

archive/issue_comments_003448.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-07-31T03:28:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/667",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/667#issuecomment-3448",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
