# Issue 4426: Do not hard code RTLD_GLOBAL as 256 for libSingular

archive/issues_004426.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  malb\n\nWe currently hard code RTLD_GLOBAL as 256 when we dlopen libSingular. This is not true on AIX and Cygwin for example, so we should pull the value in from the system's dlfcn.h.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/4426\n\n",
    "created_at": "2008-11-02T19:20:12Z",
    "labels": [
        "porting",
        "critical",
        "bug"
    ],
    "title": "Do not hard code RTLD_GLOBAL as 256 for libSingular",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4426",
    "user": "mabshoff"
}
```
Assignee: mabshoff

CC:  malb

We currently hard code RTLD_GLOBAL as 256 when we dlopen libSingular. This is not true on AIX and Cygwin for example, so we should pull the value in from the system's dlfcn.h.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/4426





---

archive/issue_comments_032541.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2008-11-02T19:25:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4426",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4426#issuecomment-32541",
    "user": "mabshoff"
}
```

Resolution: duplicate



---

archive/issue_comments_032542.json:
```json
{
    "body": "Ha, malb and I opened a ticket for the same issue, but since #4427 has a patch close this as a dupe.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-02T19:25:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4426",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4426#issuecomment-32542",
    "user": "mabshoff"
}
```

Ha, malb and I opened a ticket for the same issue, but since #4427 has a patch close this as a dupe.

Cheers,

Michael
