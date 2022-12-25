# Issue 1532: Error out with intelligent message if ATLAS tune failed

archive/issues_001532.json:
```json
{
    "body": "Assignee: jkantor\n\nOn a loaded machine ATLAS tends to report the following\n\n```\nVARIATION EXCEEDS TOLERENCE, RERUN WITH HIGHER REPS.\n```\n\nIt then errors out:\n\n```\nThread model: posix\ngcc version 4.1.2 20061115 (prerelease) (Debian 4.1.1-21)\ngcc -V 2>&1  >> bin/INSTALL_LOG/ERROR.LOG\ngcc: '-V' option must have argument\nmake[6]: [error_report] Error 1 (ignored)\ngcc --version 2>&1  >> bin/INSTALL_LOG/ERROR.LOG\ntar cf error_HAMMER64SSE3.tar Make.inc bin/INSTALL_LOG/*\ngzip --best error_HAMMER64SSE3.tar\nmv error_HAMMER64SSE3.tar.gz error_HAMMER64SSE3.tgz\nmake[6]: Leaving directory `/home/rlmill/sage-2.9.rc2/spkg/build/atlas-3.8.p5/ATLAS-build'\nmake[5]: Leaving directory `/home/rlmill/sage-2.9.rc2/spkg/build/atlas-3.8.p5/ATLAS-build'\nmake[4]: Leaving directory `/home/rlmill/sage-2.9.rc2/spkg/build/atlas-3.8.p5/ATLAS-build/bin'\nError report error_<ARCH>.tgz has been created in your top-level ATLAS\ndirectory.  Be sure to include this file in any help request.\ncat: ../../CONFIG/error.txt: No such file or directory\ncat: ../../CONFIG/error.txt: No such file or directory\n\n\nIN STAGE 1 INSTALL:  SYSTEM PROBE/AUX COMPILE\n```\n\nBut the build of Sage goes on and fails down the road.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/1532\n\n",
    "created_at": "2007-12-16T03:34:00Z",
    "labels": [
        "component: numerical",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.9",
    "title": "Error out with intelligent message if ATLAS tune failed",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1532",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: jkantor

On a loaded machine ATLAS tends to report the following

```
VARIATION EXCEEDS TOLERENCE, RERUN WITH HIGHER REPS.
```

It then errors out:

```
Thread model: posix
gcc version 4.1.2 20061115 (prerelease) (Debian 4.1.1-21)
gcc -V 2>&1  >> bin/INSTALL_LOG/ERROR.LOG
gcc: '-V' option must have argument
make[6]: [error_report] Error 1 (ignored)
gcc --version 2>&1  >> bin/INSTALL_LOG/ERROR.LOG
tar cf error_HAMMER64SSE3.tar Make.inc bin/INSTALL_LOG/*
gzip --best error_HAMMER64SSE3.tar
mv error_HAMMER64SSE3.tar.gz error_HAMMER64SSE3.tgz
make[6]: Leaving directory `/home/rlmill/sage-2.9.rc2/spkg/build/atlas-3.8.p5/ATLAS-build'
make[5]: Leaving directory `/home/rlmill/sage-2.9.rc2/spkg/build/atlas-3.8.p5/ATLAS-build'
make[4]: Leaving directory `/home/rlmill/sage-2.9.rc2/spkg/build/atlas-3.8.p5/ATLAS-build/bin'
Error report error_<ARCH>.tgz has been created in your top-level ATLAS
directory.  Be sure to include this file in any help request.
cat: ../../CONFIG/error.txt: No such file or directory
cat: ../../CONFIG/error.txt: No such file or directory


IN STAGE 1 INSTALL:  SYSTEM PROBE/AUX COMPILE
```

But the build of Sage goes on and fails down the road.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/1532





---

archive/issue_comments_009757.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-16T04:51:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1532",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1532#issuecomment-9757",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_003865.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-12-16T04:51:47Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1532",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1532#event-3865"
}
```



---

archive/issue_comments_009758.json:
```json
{
    "body": "Merged in 2.9.rc3. Updated in atlas-3.8.p6.spkg",
    "created_at": "2007-12-16T04:51:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1532",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1532#issuecomment-9758",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in 2.9.rc3. Updated in atlas-3.8.p6.spkg
