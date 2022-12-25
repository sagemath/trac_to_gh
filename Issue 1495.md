# Issue 1495: Terminate ATLAS build on Linux when power management is enabled

archive/issues_001495.json:
```json
{
    "body": "Assignee: mabshoff\n\nAccording to INSTALL.txt: CPU-Throttling, you have to do\n\n```\n/usr/bin/cpufreq-selector -g performance\n```\nBut with two cores you have to force the cpu1 to run at its peak frequency:\n\n```\nAs root:\ncp /sys/devices/system/cpu/cp0/cpufreq/scaling_governor \\\n    /sys/devices/system/cpu/cp1/cpufreq/scaling_governor\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1495\n\n",
    "closed_at": "2008-04-11T22:38:35Z",
    "created_at": "2007-12-13T23:16:08Z",
    "labels": [
        "component: distribution",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "Terminate ATLAS build on Linux when power management is enabled",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1495",
    "user": "https://github.com/jaapspies"
}
```
Assignee: mabshoff

According to INSTALL.txt: CPU-Throttling, you have to do

```
/usr/bin/cpufreq-selector -g performance
```
But with two cores you have to force the cpu1 to run at its peak frequency:

```
As root:
cp /sys/devices/system/cpu/cp0/cpufreq/scaling_governor \
    /sys/devices/system/cpu/cp1/cpufreq/scaling_governor
```


Issue created by migration from https://trac.sagemath.org/ticket/1495





---

archive/issue_comments_009580.json:
```json
{
    "body": "We need to detect if power management is enabled and set some non-performance mode. Otherwise print a warning and ask for confirmation to continue.\n\nCheers,\n\nMichael",
    "created_at": "2007-12-18T23:04:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1495#issuecomment-9580",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

We need to detect if power management is enabled and set some non-performance mode. Otherwise print a warning and ask for confirmation to continue.

Cheers,

Michael



---

archive/issue_comments_009581.json:
```json
{
    "body": "```\njkantor: 1495 we can't fix and 1547  I don't know how to do\n[12:31pm] william_stein: #1495 -- should go in the docs somewhere\n[12:31pm] william_stein: Also, maybe we can check if the cpu throttling is on and immediately terminate the build with a help message.\n```",
    "created_at": "2008-01-19T20:34:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1495#issuecomment-9581",
    "user": "https://github.com/williamstein"
}
```

```
jkantor: 1495 we can't fix and 1547  I don't know how to do
[12:31pm] william_stein: #1495 -- should go in the docs somewhere
[12:31pm] william_stein: Also, maybe we can check if the cpu throttling is on and immediately terminate the build with a help message.
```



---

archive/issue_comments_009582.json:
```json
{
    "body": "After thinking about this for a long time and some feedback I got from IRC during the ATLAS 3.8.1 upgrade when I did terminate the build I considered that it will cause more trouble than it is worth it. Fixing the power management setting requires root priviledges and since power management is enabled on pretty much any current kernel this would prevent quite a number of users from building Sage. Consequently: won't fix.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-11T22:38:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1495#issuecomment-9582",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

After thinking about this for a long time and some feedback I got from IRC during the ATLAS 3.8.1 upgrade when I did terminate the build I considered that it will cause more trouble than it is worth it. Fixing the power management setting requires root priviledges and since power management is enabled on pretty much any current kernel this would prevent quite a number of users from building Sage. Consequently: won't fix.

Cheers,

Michael



---

archive/issue_comments_009583.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2008-04-11T22:38:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1495#issuecomment-9583",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: wontfix



---

archive/issue_events_003801.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-04-11T22:38:35Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1495",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1495#event-3801"
}
```
