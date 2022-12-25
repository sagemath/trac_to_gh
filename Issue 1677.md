# Issue 1677: trivial-to-fix mistake in the rubiks spkg

archive/issues_001677.json:
```json
{
    "body": "Assignee: mabshoff\n\nThere is a pre-built OS X binary of cube in the rubiks spkg\n\n```\nglobals.c    makefile     prntsol.c   setcube.c  sizekoc1.c  trans\nwas@newserver:~/sage/spkg/standard/rubiks-20070912/src/dik$ ls -lh\ntotal 196K\n-rwxr-xr-x 1 was was  38K 2007-09-12 03:28 cube\n-rw-r--r-- 1 was was  13K 2007-09-12 03:28 cube.c\n-rw-r--r-- 1 was was  14K 2007-09-12 03:28 Description\n-rw-r--r-- 1 was was  254 2007-09-12 03:28 globals.c\n-rw-r--r-- 1 was was  249 2007-09-12 03:28 globals.h\n-rw-r--r-- 1 was was 1.1K 2007-09-12 03:28 license.txt\n-rw-r--r-- 1 was was  148 2007-09-12 03:28 longtype.h\n-rw-r--r-- 1 was was 2.6K 2007-09-12 03:28 makefile\n-rw-r--r-- 1 was was 2.4K 2007-09-12 03:28 permcube.c\n-rw-r--r-- 1 was was 6.2K 2007-09-12 03:28 phase1.c\n-rw-r--r-- 1 was was 4.1K 2007-09-12 03:28 phase2.c\n-rw-r--r-- 1 was was  338 2007-09-12 03:28 prntsol.c\n-rw-r--r-- 1 was was  306 2007-09-12 03:28 rancube.c\n-rw-r--r-- 1 was was 2.8K 2007-09-12 03:28 README\n-rw-r--r-- 1 was was 7.7K 2007-09-12 03:28 RESULTS\n-rw-r--r-- 1 was was 4.2K 2007-09-12 03:28 setcube.c\n-rw-r--r-- 1 was was 3.3K 2007-09-12 03:28 size222.c\n-rw-r--r-- 1 was was 5.6K 2007-09-12 03:28 size333c.c\n-rw-r--r-- 1 was was 8.9K 2007-09-12 03:28 sizedom.c\n-rw-r--r-- 1 was was 4.6K 2007-09-12 03:28 sizekoc1.c\n-rw-r--r-- 1 was was 5.6K 2007-09-12 03:28 sizekoc2.c\n-rw-r--r-- 1 was was 3.0K 2007-09-12 03:28 sizesquare.c\n-rw-r--r-- 1 was was 5.7K 2007-09-12 03:28 TABLE\ndrwxr-xr-x 2 was was 4.0K 2007-09-12 03:28 trans\nwas@newserver:~/sage/spkg/standard/rubiks-20070912/src/dik$ file cube\ncube: Mach-O executable i386\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1677\n\n",
    "created_at": "2008-01-04T02:57:10Z",
    "labels": [
        "component: packages: standard",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.9.2",
    "title": "trivial-to-fix mistake in the rubiks spkg",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1677",
    "user": "https://github.com/williamstein"
}
```
Assignee: mabshoff

There is a pre-built OS X binary of cube in the rubiks spkg

```
globals.c    makefile     prntsol.c   setcube.c  sizekoc1.c  trans
was@newserver:~/sage/spkg/standard/rubiks-20070912/src/dik$ ls -lh
total 196K
-rwxr-xr-x 1 was was  38K 2007-09-12 03:28 cube
-rw-r--r-- 1 was was  13K 2007-09-12 03:28 cube.c
-rw-r--r-- 1 was was  14K 2007-09-12 03:28 Description
-rw-r--r-- 1 was was  254 2007-09-12 03:28 globals.c
-rw-r--r-- 1 was was  249 2007-09-12 03:28 globals.h
-rw-r--r-- 1 was was 1.1K 2007-09-12 03:28 license.txt
-rw-r--r-- 1 was was  148 2007-09-12 03:28 longtype.h
-rw-r--r-- 1 was was 2.6K 2007-09-12 03:28 makefile
-rw-r--r-- 1 was was 2.4K 2007-09-12 03:28 permcube.c
-rw-r--r-- 1 was was 6.2K 2007-09-12 03:28 phase1.c
-rw-r--r-- 1 was was 4.1K 2007-09-12 03:28 phase2.c
-rw-r--r-- 1 was was  338 2007-09-12 03:28 prntsol.c
-rw-r--r-- 1 was was  306 2007-09-12 03:28 rancube.c
-rw-r--r-- 1 was was 2.8K 2007-09-12 03:28 README
-rw-r--r-- 1 was was 7.7K 2007-09-12 03:28 RESULTS
-rw-r--r-- 1 was was 4.2K 2007-09-12 03:28 setcube.c
-rw-r--r-- 1 was was 3.3K 2007-09-12 03:28 size222.c
-rw-r--r-- 1 was was 5.6K 2007-09-12 03:28 size333c.c
-rw-r--r-- 1 was was 8.9K 2007-09-12 03:28 sizedom.c
-rw-r--r-- 1 was was 4.6K 2007-09-12 03:28 sizekoc1.c
-rw-r--r-- 1 was was 5.6K 2007-09-12 03:28 sizekoc2.c
-rw-r--r-- 1 was was 3.0K 2007-09-12 03:28 sizesquare.c
-rw-r--r-- 1 was was 5.7K 2007-09-12 03:28 TABLE
drwxr-xr-x 2 was was 4.0K 2007-09-12 03:28 trans
was@newserver:~/sage/spkg/standard/rubiks-20070912/src/dik$ file cube
cube: Mach-O executable i386
```


Issue created by migration from https://trac.sagemath.org/ticket/1677





---

archive/issue_comments_010608.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-01-04T08:41:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1677",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1677#issuecomment-10608",
    "user": "https://github.com/robertwb"
}
```

Changing status from new to assigned.



---

archive/issue_comments_010609.json:
```json
{
    "body": "Updated spkg at http://sage.math.washington.edu/home/robertwb/spkgs/",
    "created_at": "2008-01-04T08:41:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1677",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1677#issuecomment-10609",
    "user": "https://github.com/robertwb"
}
```

Updated spkg at http://sage.math.washington.edu/home/robertwb/spkgs/



---

archive/issue_comments_010610.json:
```json
{
    "body": "Changing assignee from mabshoff to @robertwb.",
    "created_at": "2008-01-04T08:41:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1677",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1677#issuecomment-10610",
    "user": "https://github.com/robertwb"
}
```

Changing assignee from mabshoff to @robertwb.



---

archive/issue_comments_010611.json:
```json
{
    "body": "I put an updated spkg at \n\n http://sage.math.washington.edu/home/mabshoff/rubiks-20070912.p0.spkg\n\nIt fixes various issues:\n\n* clean up SPKG.txt\n* remove *DS*Store and various prebuild binaries from tree\n* remove global hg repo (that included src!)\n\nCheers,\n\nMichael",
    "created_at": "2008-01-04T08:42:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1677",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1677#issuecomment-10611",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

I put an updated spkg at 

 http://sage.math.washington.edu/home/mabshoff/rubiks-20070912.p0.spkg

It fixes various issues:

* clean up SPKG.txt
* remove *DS*Store and various prebuild binaries from tree
* remove global hg repo (that included src!)

Cheers,

Michael



---

archive/issue_events_001836.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-01-04T10:53:06Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1677",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1677#event-1836"
}
```



---

archive/issue_comments_010612.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-04T10:53:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1677",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1677#issuecomment-10612",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_010613.json:
```json
{
    "body": "I merged my spkg, so I am closing this now. So if Robert's spkg has some other improvements we can reopen this.\n\nCheers,\n\nMichael",
    "created_at": "2008-01-04T10:53:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1677",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1677#issuecomment-10613",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

I merged my spkg, so I am closing this now. So if Robert's spkg has some other improvements we can reopen this.

Cheers,

Michael
