# Issue 6451: Fint uses a non-portable option to 'cp' which fails on Solaris.

archive/issues_006451.json:
```json
{
    "body": "Assignee: tbd\n\nKeywords: solaris GNUism\n\nI noticed a problem when building 'sage-4.1.alpha2.spkg'. It complains\n\n```\nld: fatal: library -lflint: not found\n```\n\n\nBut the flint package indicates it was installed. However, when I tried to build flint again, I see this error message:\n\n\n```\nDeleting old FLINT\nInstalling new library file\ncp: illegal option -- a\nUsage: cp [-f] [-i] [-p] [-@] f1 f2\n        cp [-f] [-i] [-p] [-@] f1 ... fn d1\n        cp -r|-R [-H|-L|-P] [-f] [-i] [-p] [-@] d1 ... dn-1 dn\n```\n\n\nIt's clear flint is making use of some GNU-specific option to 'cp' The fact the copy fails means of course the library does not get installed.\n\nI'll post a fix later - it should be trivial \n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6451\n\n",
    "created_at": "2009-06-30T16:16:14Z",
    "labels": [
        "component: porting: solaris",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.1",
    "title": "Fint uses a non-portable option to 'cp' which fails on Solaris.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6451",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```
Assignee: tbd

Keywords: solaris GNUism

I noticed a problem when building 'sage-4.1.alpha2.spkg'. It complains

```
ld: fatal: library -lflint: not found
```


But the flint package indicates it was installed. However, when I tried to build flint again, I see this error message:


```
Deleting old FLINT
Installing new library file
cp: illegal option -- a
Usage: cp [-f] [-i] [-p] [-@] f1 f2
        cp [-f] [-i] [-p] [-@] f1 ... fn d1
        cp -r|-R [-H|-L|-P] [-f] [-i] [-p] [-@] d1 ... dn-1 dn
```


It's clear flint is making use of some GNU-specific option to 'cp' The fact the copy fails means of course the library does not get installed.

I'll post a fix later - it should be trivial 


Issue created by migration from https://trac.sagemath.org/ticket/6451





---

archive/issue_comments_051792.json:
```json
{
    "body": "One of the easier patches - it just needed one byte changed. In spkg-install:\n\n\n\n\n```\n  $CP -a libflint* \"$SAGE_LOCAL/lib/\"\n```\n\n\nwas changed to\n\n\n```\n  $CP -p libflint* \"$SAGE_LOCAL/lib/\"\n```\n\n\n\nSee http://sage.math.washington.edu/home/kirkby/Solaris-fixes/flint/",
    "created_at": "2009-06-30T17:04:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6451",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6451#issuecomment-51792",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

One of the easier patches - it just needed one byte changed. In spkg-install:




```
  $CP -a libflint* "$SAGE_LOCAL/lib/"
```


was changed to


```
  $CP -p libflint* "$SAGE_LOCAL/lib/"
```



See http://sage.math.washington.edu/home/kirkby/Solaris-fixes/flint/



---

archive/issue_comments_051793.json:
```json
{
    "body": "Changing assignee from tbd to drkirkby.",
    "created_at": "2009-06-30T17:04:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6451",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6451#issuecomment-51793",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing assignee from tbd to drkirkby.



---

archive/issue_comments_051794.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-06-30T17:04:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6451",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6451#issuecomment-51794",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing status from new to assigned.



---

archive/issue_comments_051795.json:
```json
{
    "body": "The patch posted here:\n\nhttp://sage.math.washington.edu/home/kirkby/Solaris-fixes/flint/spkg-install.patch\n\nchanges the -a option to cp to -p. I have checked that -a is exactly equivalent to -dpR. Here R is not relevant as only one file is copied and R is for recursive. The -d is not relevant as it is for symbolic links and is again not relevant for copying a single actual file.\n\nThe -p option is indeed available on Solaris and T2, so the patch is good. The patch is clearly conservative.\n\nNote this is not an issue with FLINT itself, but with the FLINT spkg installer.",
    "created_at": "2009-07-06T21:41:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6451",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6451#issuecomment-51795",
    "user": "https://trac.sagemath.org/admin/accounts/users/wbhart"
}
```

The patch posted here:

http://sage.math.washington.edu/home/kirkby/Solaris-fixes/flint/spkg-install.patch

changes the -a option to cp to -p. I have checked that -a is exactly equivalent to -dpR. Here R is not relevant as only one file is copied and R is for recursive. The -d is not relevant as it is for symbolic links and is again not relevant for copying a single actual file.

The -p option is indeed available on Solaris and T2, so the patch is good. The patch is clearly conservative.

Note this is not an issue with FLINT itself, but with the FLINT spkg installer.



---

archive/issue_comments_051796.json:
```json
{
    "body": "The spkg posted by David Kirkby didn't check in all changes. I've checked in the changes in David's name. The updated spkg is up at\n\nhttp://sage.math.washington.edu/home/mvngu/patch/flint-1.3.0.p2.spkg\n\nJust to let people know, the updated spkg has been merged in sage-4.1.1-alpha0. I can't close this ticket because I don't have the privilege to do so. Sorry, folks :-(",
    "created_at": "2009-07-16T18:53:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6451",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6451#issuecomment-51796",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

The spkg posted by David Kirkby didn't check in all changes. I've checked in the changes in David's name. The updated spkg is up at

http://sage.math.washington.edu/home/mvngu/patch/flint-1.3.0.p2.spkg

Just to let people know, the updated spkg has been merged in sage-4.1.1-alpha0. I can't close this ticket because I don't have the privilege to do so. Sorry, folks :-(



---

archive/issue_events_006692.json:
```json
{
    "actor": "mvngu",
    "created_at": "2009-07-16T21:12:50Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6451",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6451#event-6692"
}
```



---

archive/issue_comments_051797.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-07-16T21:12:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6451",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6451#issuecomment-51797",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed
