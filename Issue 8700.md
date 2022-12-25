# Issue 8700: the libpng-1.2.35.p0 in sage-4.4.alpha0 contains an extra copy of libpng-1.2.35!

archive/issues_008700.json:
```json
{
    "body": "Assignee: tbd\n\n\n```\nwstein@boxen:~/build/sage-4.4.alpha0/spkg/standard/libpng-1.2.35.p0$ ls\nlibpng-1.2.35  spkg-install  SPKG.txt  src\nwstein@boxen:~/build/sage-4.4.alpha0/spkg/standard/libpng-1.2.35.p0$ ls libpng-1.2.35/\nspkg-install  SPKG.txt  src\n```\n\n\nBasically there is an accidental complete copy of the extracted spkg in the spkg!\n\nIssue created by migration from https://trac.sagemath.org/ticket/8700\n\n",
    "created_at": "2010-04-17T06:35:02Z",
    "labels": [
        "component: packages: standard",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.4",
    "title": "the libpng-1.2.35.p0 in sage-4.4.alpha0 contains an extra copy of libpng-1.2.35!",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8700",
    "user": "https://github.com/williamstein"
}
```
Assignee: tbd


```
wstein@boxen:~/build/sage-4.4.alpha0/spkg/standard/libpng-1.2.35.p0$ ls
libpng-1.2.35  spkg-install  SPKG.txt  src
wstein@boxen:~/build/sage-4.4.alpha0/spkg/standard/libpng-1.2.35.p0$ ls libpng-1.2.35/
spkg-install  SPKG.txt  src
```


Basically there is an accidental complete copy of the extracted spkg in the spkg!

Issue created by migration from https://trac.sagemath.org/ticket/8700





---

archive/issue_comments_079138.json:
```json
{
    "body": "Looking in the changelog, the last person to work on the spkg left this message:\n\n```\n### libpng-1.2.35.p0 (Jaap Spies, Feb 1th, 2010)\n *\n```\n\n\nWhat was done?  It doesn't say.    The log shows this though:\n\n```\nchangeset:   13:ae01944f408c\ntag:         tip\nuser:        Jaap Spies <jaapspies@gmail.com>\ndate:        Thu Feb 04 19:32:51 2010 +0100\nsummary:     Corrected stupid typo I thought I had corrected earlier.\n\nchangeset:   12:329a8eb6dd2e\nuser:        Jaap Spies <jaapspies@gmail.com>\ndate:        Wed Feb 03 19:09:41 2010 +0100\nsummary:     Let SAGE64=yes work not only on OSX, but also on Open Solaris and possibly on other platform\n```\n\n\nAnyway, somebody was sloppy refereeing this, etc.",
    "created_at": "2010-04-17T06:36:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8700",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8700#issuecomment-79138",
    "user": "https://github.com/williamstein"
}
```

Looking in the changelog, the last person to work on the spkg left this message:

```
### libpng-1.2.35.p0 (Jaap Spies, Feb 1th, 2010)
 *
```


What was done?  It doesn't say.    The log shows this though:

```
changeset:   13:ae01944f408c
tag:         tip
user:        Jaap Spies <jaapspies@gmail.com>
date:        Thu Feb 04 19:32:51 2010 +0100
summary:     Corrected stupid typo I thought I had corrected earlier.

changeset:   12:329a8eb6dd2e
user:        Jaap Spies <jaapspies@gmail.com>
date:        Wed Feb 03 19:09:41 2010 +0100
summary:     Let SAGE64=yes work not only on OSX, but also on Open Solaris and possibly on other platform
```


Anyway, somebody was sloppy refereeing this, etc.



---

archive/issue_comments_079139.json:
```json
{
    "body": "Here's a fixed spkg:\n\n    http://boxen.math.washington.edu/home/wstein/patches/libpng-1.2.35.p1.spkg",
    "created_at": "2010-04-17T06:40:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8700",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8700#issuecomment-79139",
    "user": "https://github.com/williamstein"
}
```

Here's a fixed spkg:

    http://boxen.math.washington.edu/home/wstein/patches/libpng-1.2.35.p1.spkg



---

archive/issue_comments_079140.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-04-17T06:40:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8700",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8700#issuecomment-79140",
    "user": "https://github.com/williamstein"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_079141.json:
```json
{
    "body": "I'm downgrading this from a blocker to critical: the current spkg makes the Sage source distribution a little bigger, but causes no bugs or test failures.",
    "created_at": "2010-04-23T04:40:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8700",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8700#issuecomment-79141",
    "user": "https://github.com/jhpalmieri"
}
```

I'm downgrading this from a blocker to critical: the current spkg makes the Sage source distribution a little bigger, but causes no bugs or test failures.



---

archive/issue_comments_079142.json:
```json
{
    "body": "Changing priority from blocker to critical.",
    "created_at": "2010-04-23T04:40:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8700",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8700#issuecomment-79142",
    "user": "https://github.com/jhpalmieri"
}
```

Changing priority from blocker to critical.



---

archive/issue_comments_079143.json:
```json
{
    "body": "Close as fixed:\n\n\n```\n[mvngu@sage libpng-1.2.35.p2]$ pwd\n/dev/shm/mvngu/sage-4.4.4.alpha0/spkg/standard/libpng-1.2.35.p2\n[mvngu@sage libpng-1.2.35.p2]$ ls\nspkg-install  SPKG.txt  src\n```\n",
    "created_at": "2010-06-16T01:59:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8700",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8700#issuecomment-79143",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Close as fixed:


```
[mvngu@sage libpng-1.2.35.p2]$ pwd
/dev/shm/mvngu/sage-4.4.4.alpha0/spkg/standard/libpng-1.2.35.p2
[mvngu@sage libpng-1.2.35.p2]$ ls
spkg-install  SPKG.txt  src
```




---

archive/issue_events_008871.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2010-06-16T01:59:49Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8700",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8700#event-8871"
}
```



---

archive/issue_comments_079144.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-16T01:59:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8700",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8700#issuecomment-79144",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed
