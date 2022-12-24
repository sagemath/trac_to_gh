# Issue 629: Fix DSage on PPC Linux

archive/issues_000629.json:
```json
{
    "body": "Assignee: Yi\n\nKeywords: DSage, PPC\n\nDSage needs certain bits implemented for each platform. This is missing for PPC Linux. The DSage doc test is the only failing on for Sage on PPC Linux 32 bit as of 2.8.4+pari fix.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/629\n\n",
    "created_at": "2007-09-09T18:12:38Z",
    "labels": [
        "packages: standard",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.5",
    "title": "Fix DSage on PPC Linux",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/629",
    "user": "mabshoff"
}
```
Assignee: Yi

Keywords: DSage, PPC

DSage needs certain bits implemented for each platform. This is missing for PPC Linux. The DSage doc test is the only failing on for Sage on PPC Linux 32 bit as of 2.8.4+pari fix.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/629





---

archive/issue_comments_003236.json:
```json
{
    "body": "Here is the output from /proc/cpuinfo and /proc/meminfo:\n\n```\ncat /proc/cpuinfo\n\nprocessor\t: 0\ncpu\t\t: 7447A, altivec supported\nclock\t\t: 666.666000MHz\nrevision\t: 0.5 (pvr 8003 0105)\nbogomips\t: 36.73\ntimebase\t: 18432000\nplatform\t: PowerMac\nmachine\t\t: PowerBook6,7\nmotherboard\t: PowerBook6,7 MacRISC3 Power Macintosh \ndetected as\t: 287 (iBook G4)\npmac flags\t: 0000001b\nL2 cache\t: 512K unified\npmac-generation\t: NewWorld\n\n\ncat /proc/meminfo\n\nMemTotal:       514288 kB\nMemFree:        247792 kB\nBuffers:         15264 kB\nCached:         163780 kB\nSwapCached:          0 kB\nActive:         113572 kB\nInactive:       119844 kB\nHighTotal:           0 kB\nHighFree:            0 kB\nLowTotal:       514288 kB\nLowFree:        247792 kB\nSwapTotal:     1048568 kB\nSwapFree:      1048568 kB\nDirty:               4 kB\nWriteback:           0 kB\nAnonPages:       54388 kB\nMapped:          49668 kB\nSlab:            14412 kB\nSReclaimable:     8820 kB\nSUnreclaim:       5592 kB\nPageTables:       2768 kB\nNFS_Unstable:        0 kB\nBounce:              0 kB\nCommitLimit:   1305712 kB\nCommitted_AS:   196360 kB\nVmallocTotal:   448936 kB\nVmallocUsed:     29308 kB\nVmallocChunk:   418724 kB\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2007-09-17T00:21:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/629",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/629#issuecomment-3236",
    "user": "mabshoff"
}
```

Here is the output from /proc/cpuinfo and /proc/meminfo:

```
cat /proc/cpuinfo

processor	: 0
cpu		: 7447A, altivec supported
clock		: 666.666000MHz
revision	: 0.5 (pvr 8003 0105)
bogomips	: 36.73
timebase	: 18432000
platform	: PowerMac
machine		: PowerBook6,7
motherboard	: PowerBook6,7 MacRISC3 Power Macintosh 
detected as	: 287 (iBook G4)
pmac flags	: 0000001b
L2 cache	: 512K unified
pmac-generation	: NewWorld


cat /proc/meminfo

MemTotal:       514288 kB
MemFree:        247792 kB
Buffers:         15264 kB
Cached:         163780 kB
SwapCached:          0 kB
Active:         113572 kB
Inactive:       119844 kB
HighTotal:           0 kB
HighFree:            0 kB
LowTotal:       514288 kB
LowFree:        247792 kB
SwapTotal:     1048568 kB
SwapFree:      1048568 kB
Dirty:               4 kB
Writeback:           0 kB
AnonPages:       54388 kB
Mapped:          49668 kB
Slab:            14412 kB
SReclaimable:     8820 kB
SUnreclaim:       5592 kB
PageTables:       2768 kB
NFS_Unstable:        0 kB
Bounce:              0 kB
CommitLimit:   1305712 kB
Committed_AS:   196360 kB
VmallocTotal:   448936 kB
VmallocUsed:     29308 kB
VmallocChunk:   418724 kB
```


Cheers,

Michael



---

archive/issue_comments_003237.json:
```json
{
    "body": "oops, second try:\n\nHere is the output from /proc/cpuinfo and /proc/meminfo:\n\n```\ncat /proc/cpuinfo\n\nprocessor\t: 0\ncpu\t\t: 7447A, altivec supported\nclock\t\t: 666.666000MHz\nrevision\t: 0.5 (pvr 8003 0105)\nbogomips\t: 36.73\ntimebase\t: 18432000\nplatform\t: PowerMac\nmachine\t\t: PowerBook6,7\nmotherboard\t: PowerBook6,7 MacRISC3 Power Macintosh \ndetected as\t: 287 (iBook G4)\npmac flags\t: 0000001b\nL2 cache\t: 512K unified\npmac-generation\t: NewWorld\n\n\ncat /proc/meminfo\n\nMemTotal:       514288 kB\nMemFree:        247792 kB\nBuffers:         15264 kB\nCached:         163780 kB\nSwapCached:          0 kB\nActive:         113572 kB\nInactive:       119844 kB\nHighTotal:           0 kB\nHighFree:            0 kB\nLowTotal:       514288 kB\nLowFree:        247792 kB\nSwapTotal:     1048568 kB\nSwapFree:      1048568 kB\nDirty:               4 kB\nWriteback:           0 kB\nAnonPages:       54388 kB\nMapped:          49668 kB\nSlab:            14412 kB\nSReclaimable:     8820 kB\nSUnreclaim:       5592 kB\nPageTables:       2768 kB\nNFS_Unstable:        0 kB\nBounce:              0 kB\nCommitLimit:   1305712 kB\nCommitted_AS:   196360 kB\nVmallocTotal:   448936 kB\nVmallocUsed:     29308 kB\nVmallocChunk:   418724 kB\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2007-09-17T00:24:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/629",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/629#issuecomment-3237",
    "user": "mabshoff"
}
```

oops, second try:

Here is the output from /proc/cpuinfo and /proc/meminfo:

```
cat /proc/cpuinfo

processor	: 0
cpu		: 7447A, altivec supported
clock		: 666.666000MHz
revision	: 0.5 (pvr 8003 0105)
bogomips	: 36.73
timebase	: 18432000
platform	: PowerMac
machine		: PowerBook6,7
motherboard	: PowerBook6,7 MacRISC3 Power Macintosh 
detected as	: 287 (iBook G4)
pmac flags	: 0000001b
L2 cache	: 512K unified
pmac-generation	: NewWorld


cat /proc/meminfo

MemTotal:       514288 kB
MemFree:        247792 kB
Buffers:         15264 kB
Cached:         163780 kB
SwapCached:          0 kB
Active:         113572 kB
Inactive:       119844 kB
HighTotal:           0 kB
HighFree:            0 kB
LowTotal:       514288 kB
LowFree:        247792 kB
SwapTotal:     1048568 kB
SwapFree:      1048568 kB
Dirty:               4 kB
Writeback:           0 kB
AnonPages:       54388 kB
Mapped:          49668 kB
Slab:            14412 kB
SReclaimable:     8820 kB
SUnreclaim:       5592 kB
PageTables:       2768 kB
NFS_Unstable:        0 kB
Bounce:              0 kB
CommitLimit:   1305712 kB
Committed_AS:   196360 kB
VmallocTotal:   448936 kB
VmallocUsed:     29308 kB
VmallocChunk:   418724 kB
```


Cheers,

Michael



---

archive/issue_comments_003238.json:
```json
{
    "body": "sys.platform output:\n\n```\n[mabshoff@localhost sage-2.8.4.1]$ ./local/bin/python\nPython 2.5.1 (r251:54863, Sep  9 2007, 19:19:35)\n[GCC 4.1.2 20070502 (Red Hat 4.1.2-12)] on linux2\nType \"help\", \"copyright\", \"credits\" or \"license\" for more information.\n>>> import sys\n>>> print sys.platform\nlinux2\n```\n\n\nThe exact failure:\n\n```\nsage.dsage.twisted.tests.test_remote\n  ClientRemoteCallsTest\n    testremoteSubmitBadJob ...                                             [OK]\n    testremoteSubmitJob ...                                                [OK]\n  MonitorRemoteCallsTest\n    testget_killed_jobs_list ...                                        [ERROR]\n                                       [ERROR]\n    testremote_get_job ...                                              [ERROR]\n                                             [ERROR]\n    testremote_job_done ...                                             [ERROR]\n                                            [ERROR]\n    testremote_job_failed ...                                           [ERROR]\n                                          [ERROR]\n\n===============================================================================\n[ERROR]: sage.dsage.twisted.tests.test_remote.MonitorRemoteCallsTest.testget_killed_jobs_list\n\nTraceback from remote host -- Traceback unavailable\n===============================================================================\n[ERROR]: sage.dsage.twisted.tests.test_remote.MonitorRemoteCallsTest.testget_killed_jobs_list\n\nTraceback (most recent call last):\n  File \"/tmp/Work/sage-2.8.4.1/local/lib/python2.5/site-packages/sage/dsage/twisted/pb.py\", line 412, in requestAvatar\n    avatar.attached(avatar, mind)\n  File \"/tmp/Work/sage-2.8.4.1/local/lib/python2.5/site-packages/sage/dsage/twisted/pb.py\", line 258, in attached\n    self.DSageServer.monitordb.add_monitor(self.host_info)\n  File \"/tmp/Work/sage-2.8.4.1/local/lib/python2.5/site-packages/sage/dsage/database/monitordb.py\", line 120, in add_monitor\n    cpu_speed = host_info['cpu_speed']\nexceptions.KeyError: 'cpu_speed'\n===============================================================================\n[ERROR]: sage.dsage.twisted.tests.test_remote.MonitorRemoteCallsTest.testremote_get_job\n\nTraceback from remote host -- Traceback unavailable\n===============================================================================\n[ERROR]: sage.dsage.twisted.tests.test_remote.MonitorRemoteCallsTest.testremote_get_job\n\nTraceback (most recent call last):\n  File \"/tmp/Work/sage-2.8.4.1/local/lib/python2.5/site-packages/sage/dsage/twisted/pb.py\", line 412, in requestAvatar\n    avatar.attached(avatar, mind)\n  File \"/tmp/Work/sage-2.8.4.1/local/lib/python2.5/site-packages/sage/dsage/twisted/pb.py\", line 258, in attached\n    self.DSageServer.monitordb.add_monitor(self.host_info)\n  File \"/tmp/Work/sage-2.8.4.1/local/lib/python2.5/site-packages/sage/dsage/database/monitordb.py\", line 120, in add_monitor\n    cpu_speed = host_info['cpu_speed']\nexceptions.KeyError: 'cpu_speed'\n===============================================================================\n[ERROR]: sage.dsage.twisted.tests.test_remote.MonitorRemoteCallsTest.testremote_job_done\n\nTraceback from remote host -- Traceback unavailable\n===============================================================================\n[ERROR]: sage.dsage.twisted.tests.test_remote.MonitorRemoteCallsTest.testremote_job_done\n\nTraceback (most recent call last):\n  File \"/tmp/Work/sage-2.8.4.1/local/lib/python2.5/site-packages/sage/dsage/twisted/pb.py\", line 412, in requestAvatar\n    avatar.attached(avatar, mind)\n  File \"/tmp/Work/sage-2.8.4.1/local/lib/python2.5/site-packages/sage/dsage/twisted/pb.py\", line 258, in attached\n    self.DSageServer.monitordb.add_monitor(self.host_info)\n  File \"/tmp/Work/sage-2.8.4.1/local/lib/python2.5/site-packages/sage/dsage/database/monitordb.py\", line 120, in add_monitor\n    cpu_speed = host_info['cpu_speed']\nexceptions.KeyError: 'cpu_speed'\n===============================================================================\n[ERROR]: sage.dsage.twisted.tests.test_remote.MonitorRemoteCallsTest.testremote_job_failed\n\nTraceback from remote host -- Traceback unavailable\n===============================================================================\n[ERROR]: sage.dsage.twisted.tests.test_remote.MonitorRemoteCallsTest.testremote_job_failed\n\nTraceback (most recent call last):\n  File \"/tmp/Work/sage-2.8.4.1/local/lib/python2.5/site-packages/sage/dsage/twisted/pb.py\", line 412, in requestAvatar\n    avatar.attached(avatar, mind)\n  File \"/tmp/Work/sage-2.8.4.1/local/lib/python2.5/site-packages/sage/dsage/twisted/pb.py\", line 258, in attached\n    self.DSageServer.monitordb.add_monitor(self.host_info)\n  File \"/tmp/Work/sage-2.8.4.1/local/lib/python2.5/site-packages/sage/dsage/database/monitordb.py\", line 120, in add_monitor\n    cpu_speed = host_info['cpu_speed']\nexceptions.KeyError: 'cpu_speed'\n-------------------------------------------------------------------------------\nRan 50 tests in 10.105s\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2007-09-17T05:55:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/629",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/629#issuecomment-3238",
    "user": "mabshoff"
}
```

sys.platform output:

```
[mabshoff@localhost sage-2.8.4.1]$ ./local/bin/python
Python 2.5.1 (r251:54863, Sep  9 2007, 19:19:35)
[GCC 4.1.2 20070502 (Red Hat 4.1.2-12)] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> import sys
>>> print sys.platform
linux2
```


The exact failure:

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
  File "/tmp/Work/sage-2.8.4.1/local/lib/python2.5/site-packages/sage/dsage/twisted/pb.py", line 412, in requestAvatar
    avatar.attached(avatar, mind)
  File "/tmp/Work/sage-2.8.4.1/local/lib/python2.5/site-packages/sage/dsage/twisted/pb.py", line 258, in attached
    self.DSageServer.monitordb.add_monitor(self.host_info)
  File "/tmp/Work/sage-2.8.4.1/local/lib/python2.5/site-packages/sage/dsage/database/monitordb.py", line 120, in add_monitor
    cpu_speed = host_info['cpu_speed']
exceptions.KeyError: 'cpu_speed'
===============================================================================
[ERROR]: sage.dsage.twisted.tests.test_remote.MonitorRemoteCallsTest.testremote_get_job

Traceback from remote host -- Traceback unavailable
===============================================================================
[ERROR]: sage.dsage.twisted.tests.test_remote.MonitorRemoteCallsTest.testremote_get_job

Traceback (most recent call last):
  File "/tmp/Work/sage-2.8.4.1/local/lib/python2.5/site-packages/sage/dsage/twisted/pb.py", line 412, in requestAvatar
    avatar.attached(avatar, mind)
  File "/tmp/Work/sage-2.8.4.1/local/lib/python2.5/site-packages/sage/dsage/twisted/pb.py", line 258, in attached
    self.DSageServer.monitordb.add_monitor(self.host_info)
  File "/tmp/Work/sage-2.8.4.1/local/lib/python2.5/site-packages/sage/dsage/database/monitordb.py", line 120, in add_monitor
    cpu_speed = host_info['cpu_speed']
exceptions.KeyError: 'cpu_speed'
===============================================================================
[ERROR]: sage.dsage.twisted.tests.test_remote.MonitorRemoteCallsTest.testremote_job_done

Traceback from remote host -- Traceback unavailable
===============================================================================
[ERROR]: sage.dsage.twisted.tests.test_remote.MonitorRemoteCallsTest.testremote_job_done

Traceback (most recent call last):
  File "/tmp/Work/sage-2.8.4.1/local/lib/python2.5/site-packages/sage/dsage/twisted/pb.py", line 412, in requestAvatar
    avatar.attached(avatar, mind)
  File "/tmp/Work/sage-2.8.4.1/local/lib/python2.5/site-packages/sage/dsage/twisted/pb.py", line 258, in attached
    self.DSageServer.monitordb.add_monitor(self.host_info)
  File "/tmp/Work/sage-2.8.4.1/local/lib/python2.5/site-packages/sage/dsage/database/monitordb.py", line 120, in add_monitor
    cpu_speed = host_info['cpu_speed']
exceptions.KeyError: 'cpu_speed'
===============================================================================
[ERROR]: sage.dsage.twisted.tests.test_remote.MonitorRemoteCallsTest.testremote_job_failed

Traceback from remote host -- Traceback unavailable
===============================================================================
[ERROR]: sage.dsage.twisted.tests.test_remote.MonitorRemoteCallsTest.testremote_job_failed

Traceback (most recent call last):
  File "/tmp/Work/sage-2.8.4.1/local/lib/python2.5/site-packages/sage/dsage/twisted/pb.py", line 412, in requestAvatar
    avatar.attached(avatar, mind)
  File "/tmp/Work/sage-2.8.4.1/local/lib/python2.5/site-packages/sage/dsage/twisted/pb.py", line 258, in attached
    self.DSageServer.monitordb.add_monitor(self.host_info)
  File "/tmp/Work/sage-2.8.4.1/local/lib/python2.5/site-packages/sage/dsage/database/monitordb.py", line 120, in add_monitor
    cpu_speed = host_info['cpu_speed']
exceptions.KeyError: 'cpu_speed'
-------------------------------------------------------------------------------
Ran 50 tests in 10.105s
```


Cheers,

Michael



---

archive/issue_comments_003239.json:
```json
{
    "body": "Hello, \n\nYi's bundle at\n\nhttp://sage.math.washington.edu/home/yqiang/dsage_ppc.hg\n\nfixes the problem for me.\n\nCheers,\n\nMichael",
    "created_at": "2007-09-19T05:19:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/629",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/629#issuecomment-3239",
    "user": "mabshoff"
}
```

Hello, 

Yi's bundle at

http://sage.math.washington.edu/home/yqiang/dsage_ppc.hg

fixes the problem for me.

Cheers,

Michael



---

archive/issue_comments_003240.json:
```json
{
    "body": "Ok, Yi just send me an email to hold on before applying this patch until he gets some more info about Linux on Itanium.\n\nStay tuned.\n\nMichael",
    "created_at": "2007-09-19T20:45:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/629",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/629#issuecomment-3240",
    "user": "mabshoff"
}
```

Ok, Yi just send me an email to hold on before applying this patch until he gets some more info about Linux on Itanium.

Stay tuned.

Michael



---

archive/issue_comments_003241.json:
```json
{
    "body": "Ok, new bundle at \n\nhttp://sage.math.washington.edu/home/yqiang/dsage_ppc.hg\n\nshould fix it for both PPC and IA64.",
    "created_at": "2007-09-20T04:45:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/629",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/629#issuecomment-3241",
    "user": "@yqiang"
}
```

Ok, new bundle at 

http://sage.math.washington.edu/home/yqiang/dsage_ppc.hg

should fix it for both PPC and IA64.



---

archive/issue_comments_003242.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-09-21T00:09:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/629",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/629#issuecomment-3242",
    "user": "@williamstein"
}
```

Resolution: fixed
