# Issue 7072: scipy 0.7.p2 has a GNUism, sending GNU flags to the Sun compiler.

archive/issues_007072.json:
```json
{
    "body": "Assignee: tbd\n\nUsing\n\n* Solaris 10 update 7 on SPARC\n* sage-4.1.2.alpha2\n* Sun Studio 12.1\n* An updated configure script to allow the Sun compiler to be used #7021 \n\n\n```\nscipy-0.7.p2/patches/setup.py.integrate\nscipy-0.7.p2/patches/optimize.py\nscipy-0.7.p2/spkg-check\nFinished extraction\n****************************************************\nHost system\nuname -a:\nSunOS swan 5.10 Generic_139555-08 sun4u sparc SUNW,Sun-Blade-1000\n****************************************************\n****************************************************\nCC Version\n/opt/xxxsunstudio12.1/bin/cc -v\nusage: cc [ options] files.  Use 'cc -flags' for details\n****************************************************\nf95: Warning: Option -fPIC passed to ld, if ld is invoked, ignored otherwise\nf95: Warning: Option --version passed to ld, if ld is invoked, ignored otherwise\nUsage: f95 [ options ] files.  Use 'f95 -flags' for details\nf95: Warning: Option -fPIC passed to ld, if ld is invoked, ignored otherwise\nf95: Warning: Option --version passed to ld, if ld is invoked, ignored otherwise\nUsage: f95 [ options ] files.  Use 'f95 -flags' for details\n\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7072\n\n",
    "created_at": "2009-09-29T13:40:09Z",
    "labels": [
        "component: algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "scipy 0.7.p2 has a GNUism, sending GNU flags to the Sun compiler.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7072",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```
Assignee: tbd

Using

* Solaris 10 update 7 on SPARC
* sage-4.1.2.alpha2
* Sun Studio 12.1
* An updated configure script to allow the Sun compiler to be used #7021 


```
scipy-0.7.p2/patches/setup.py.integrate
scipy-0.7.p2/patches/optimize.py
scipy-0.7.p2/spkg-check
Finished extraction
****************************************************
Host system
uname -a:
SunOS swan 5.10 Generic_139555-08 sun4u sparc SUNW,Sun-Blade-1000
****************************************************
****************************************************
CC Version
/opt/xxxsunstudio12.1/bin/cc -v
usage: cc [ options] files.  Use 'cc -flags' for details
****************************************************
f95: Warning: Option -fPIC passed to ld, if ld is invoked, ignored otherwise
f95: Warning: Option --version passed to ld, if ld is invoked, ignored otherwise
Usage: f95 [ options ] files.  Use 'f95 -flags' for details
f95: Warning: Option -fPIC passed to ld, if ld is invoked, ignored otherwise
f95: Warning: Option --version passed to ld, if ld is invoked, ignored otherwise
Usage: f95 [ options ] files.  Use 'f95 -flags' for details

```



Issue created by migration from https://trac.sagemath.org/ticket/7072





---

archive/issue_comments_058388.json:
```json
{
    "body": "Changing component from algebra to solaris.",
    "created_at": "2009-11-09T14:03:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7072",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7072#issuecomment-58388",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing component from algebra to solaris.



---

archive/issue_comments_058389.json:
```json
{
    "body": "This is outdated and should be closed.",
    "created_at": "2019-11-23T16:30:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7072",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7072#issuecomment-58389",
    "user": "https://github.com/mkoeppe"
}
```

This is outdated and should be closed.



---

archive/issue_comments_058390.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2019-11-23T19:37:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7072",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7072#issuecomment-58390",
    "user": "https://github.com/fchapoton"
}
```

Resolution: invalid



---

archive/issue_events_007294.json:
```json
{
    "actor": "@fchapoton",
    "created_at": "2019-11-23T19:37:11Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7072",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7072#event-7294"
}
```
