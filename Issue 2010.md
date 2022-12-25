# Issue 2010: crap -- libpng contains lots and lots of weird (OS X?) temp or meta files

archive/issues_002010.json:
```json
{
    "body": "Assignee: mabshoff\n\n```\nsage-2.10.1.rc3/spkg/standard/libpng-1.2.22.p3/src/._Y2KINFO\nsage-2.10.1.rc3/spkg/standard/libpng-1.2.22.p3/src/._TODO\nsage-2.10.1.rc3/spkg/standard/libpng-1.2.22.p3/src/._test-pngtest.sh\nsage-2.10.1.rc3/spkg/standard/libpng-1.2.22.p3/src/scripts/._smakefile.ppc\nsage-2.10.1.rc3/spkg/standard/libpng-1.2.22.p3/src/scripts/._SCOPTIONS.ppc\nsage-2.10.1.rc3/spkg/standard/libpng-1.2.22.p3/src/scripts/._pngw32.rc\nsage-2.10.1.rc3/spkg/standard/libpng-1.2.22.p3/src/scripts/._pngw32.def\nsage-2.10.1.rc3/spkg/standard/libpng-1.2.22.p3/src/scripts/._pngos2.def\nsage-2.10.1.rc3/spkg/standard/libpng-1.2.22.p3/src/scripts/._makevms.com\nsage-2.10.1.rc3/spkg/standard/libpng-1.2.22.p3/src/scripts/._makefile.watcom\nsage-2.10.1.rc3/spkg/standard/libpng-1.2.22.p3/src/scripts/._makefile.vcwin32\nsage-2.10.1.rc3/spkg/standard/libpng-1.2.22.p3/src/scripts/._makefile.vcawin32\n...\nAND MANY MORE\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/2010\n\n",
    "created_at": "2008-01-31T23:21:33Z",
    "labels": [
        "component: packages: standard",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.1",
    "title": "crap -- libpng contains lots and lots of weird (OS X?) temp or meta files",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2010",
    "user": "https://github.com/williamstein"
}
```
Assignee: mabshoff

```
sage-2.10.1.rc3/spkg/standard/libpng-1.2.22.p3/src/._Y2KINFO
sage-2.10.1.rc3/spkg/standard/libpng-1.2.22.p3/src/._TODO
sage-2.10.1.rc3/spkg/standard/libpng-1.2.22.p3/src/._test-pngtest.sh
sage-2.10.1.rc3/spkg/standard/libpng-1.2.22.p3/src/scripts/._smakefile.ppc
sage-2.10.1.rc3/spkg/standard/libpng-1.2.22.p3/src/scripts/._SCOPTIONS.ppc
sage-2.10.1.rc3/spkg/standard/libpng-1.2.22.p3/src/scripts/._pngw32.rc
sage-2.10.1.rc3/spkg/standard/libpng-1.2.22.p3/src/scripts/._pngw32.def
sage-2.10.1.rc3/spkg/standard/libpng-1.2.22.p3/src/scripts/._pngos2.def
sage-2.10.1.rc3/spkg/standard/libpng-1.2.22.p3/src/scripts/._makevms.com
sage-2.10.1.rc3/spkg/standard/libpng-1.2.22.p3/src/scripts/._makefile.watcom
sage-2.10.1.rc3/spkg/standard/libpng-1.2.22.p3/src/scripts/._makefile.vcwin32
sage-2.10.1.rc3/spkg/standard/libpng-1.2.22.p3/src/scripts/._makefile.vcawin32
...
AND MANY MORE
```

Issue created by migration from https://trac.sagemath.org/ticket/2010





---

archive/issue_comments_012964.json:
```json
{
    "body": "The updated spkg at\n\nhttp://sage.math.washington.edu/home/mabshoff/release-cycles-2.10.1/rc4/libpng-1.2.22.p4.spkg\n\nremoves the offending files.\n\nCheers,\n\nMichael",
    "created_at": "2008-01-31T23:49:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2010",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2010#issuecomment-12964",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The updated spkg at

http://sage.math.washington.edu/home/mabshoff/release-cycles-2.10.1/rc4/libpng-1.2.22.p4.spkg

removes the offending files.

Cheers,

Michael



---

archive/issue_comments_012965.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-01-31T23:51:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2010",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2010#issuecomment-12965",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_events_004844.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-02-01T02:01:14Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2010",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2010#event-4844"
}
```



---

archive/issue_comments_012966.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-01T02:01:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2010",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2010#issuecomment-12966",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_012967.json:
```json
{
    "body": "Merged in Sage 2.10.1.rc4",
    "created_at": "2008-02-01T02:01:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2010",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2010#issuecomment-12967",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.1.rc4
