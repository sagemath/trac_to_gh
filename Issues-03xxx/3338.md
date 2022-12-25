# Issue 3338: gfan tarball is not clean upstream

archive/issues_003338.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  alexghitza mhampton\n\nThe gfan sources in SAGE are not quite the upstream sources:\n\n[tabbott`@`debuild export$] diff -ur tmp/gfan0.3 tmp/gfan-0.3/ | diffstat\n gfan-0.3//.DS_Store         |only\n gfan-0.3//Makefile.orig03   |only\n gfan-0.3//Makefile2.2       |only\n gfan-0.3//Makefile2.2anders |only\n gfan-0.3//SAGE.txt          |only\n gfan-0.3//debian            |only\n gfan-0.3//oldsageMakefile   |only\n gfan-0.3/Makefile           |   55 ++++++++++++++------------------------------\n gfan0.3/doc                 |only\n gfan0.3/examples            |only\n gfan0.3/homepage            |only\n 11 files changed, 18 insertions(+), 37 deletions(-)\n\nI actually think that the SAGE changes may be mostly unecessary; the changes to the install target don't seem to be used, and the other changes aside from the removal of app_construction.o seem like they could be implemented via\n\nmake ADDTIONALINCLUDEOPTIONS=-I$(SAGE_LOCAL)/include ADDITIONALLINKOPTIONS=-lcddgmp -lgmp\n\nIf we can figure out how to fig the compilation problems related to app_construction.o (I don't see this problem on Debian with gfan 0.3), then we can stop modifying gfan at all.  But having a makefile patch isn't a big deal either.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3338\n\n",
    "closed_at": "2010-01-25T14:15:40Z",
    "created_at": "2008-05-30T17:32:39Z",
    "labels": [
        "component: packages: standard",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.2",
    "title": "gfan tarball is not clean upstream",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3338",
    "user": "https://github.com/timabbott"
}
```
Assignee: mabshoff

CC:  alexghitza mhampton

The gfan sources in SAGE are not quite the upstream sources:

[tabbott`@`debuild export$] diff -ur tmp/gfan0.3 tmp/gfan-0.3/ | diffstat
 gfan-0.3//.DS_Store         |only
 gfan-0.3//Makefile.orig03   |only
 gfan-0.3//Makefile2.2       |only
 gfan-0.3//Makefile2.2anders |only
 gfan-0.3//SAGE.txt          |only
 gfan-0.3//debian            |only
 gfan-0.3//oldsageMakefile   |only
 gfan-0.3/Makefile           |   55 ++++++++++++++------------------------------
 gfan0.3/doc                 |only
 gfan0.3/examples            |only
 gfan0.3/homepage            |only
 11 files changed, 18 insertions(+), 37 deletions(-)

I actually think that the SAGE changes may be mostly unecessary; the changes to the install target don't seem to be used, and the other changes aside from the removal of app_construction.o seem like they could be implemented via

make ADDTIONALINCLUDEOPTIONS=-I$(SAGE_LOCAL)/include ADDITIONALLINKOPTIONS=-lcddgmp -lgmp

If we can figure out how to fig the compilation problems related to app_construction.o (I don't see this problem on Debian with gfan 0.3), then we can stop modifying gfan at all.  But having a makefile patch isn't a big deal either.

Issue created by migration from https://trac.sagemath.org/ticket/3338





---

archive/issue_comments_023139.json:
```json
{
    "body": "Note #7820 is aimed at updating gfan to the latest release, called \"0.4plus\".",
    "created_at": "2010-01-05T11:24:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3338",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3338#issuecomment-23139",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Note #7820 is aimed at updating gfan to the latest release, called "0.4plus".



---

archive/issue_comments_023140.json:
```json
{
    "body": "Close as fixed by #7820.",
    "created_at": "2010-01-25T14:15:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3338",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3338#issuecomment-23140",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Close as fixed by #7820.



---

archive/issue_comments_023141.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-25T14:15:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3338",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3338#issuecomment-23141",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_events_007480.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2010-01-25T14:15:40Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3338",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3338#event-7480"
}
```
