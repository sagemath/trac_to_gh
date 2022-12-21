# Issue 629: Fix DSage on PPC Linux

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2007-09-09 18:12:38

Assignee: Yi

Keywords: DSage, PPC

DSage needs certain bits implemented for each platform. This is missing for PPC Linux. The DSage doc test is the only failing on for Sage on PPC Linux 32 bit as of 2.8.4+pari fix.

Cheers,

Michael


---

Comment by mabshoff created at 2007-09-17 00:21:28

Here is the output from /proc/cpuinfo and /proc/meminfo:
{{{cat /proc/cpuinfo

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
}}}

Cheers,

Michael


---

Comment by mabshoff created at 2007-09-17 00:24:03

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

Comment by mabshoff created at 2007-09-17 05:55:08

sys.platform output:

```
[mabshoff`@`localhost sage-2.8.4.1]$ ./local/bin/python
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

Comment by mabshoff created at 2007-09-19 05:19:11

Hello, 

Yi's bundle at

http://sage.math.washington.edu/home/yqiang/dsage_ppc.hg

fixes the problem for me.

Cheers,

Michael


---

Comment by mabshoff created at 2007-09-19 20:45:12

Ok, Yi just send me an email to hold on before applying this patch until he gets some more info about Linux on Itanium.

Stay tuned.

Michael


---

Comment by yi created at 2007-09-20 04:45:04

Ok, new bundle at 

http://sage.math.washington.edu/home/yqiang/dsage_ppc.hg

should fix it for both PPC and IA64.


---

Comment by was created at 2007-09-21 00:09:46

Resolution: fixed
