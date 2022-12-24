# Issue 326: rebuild system doesn't recognise changed pyrex files on OS X

archive/issues_000326.json:
```json
{
    "body": "Assignee: @williamstein\n\nWhen I change a pyrex file (specifically rings/integer.pyx), sage -b doesn't seem to notice. I have to manually delete the corresponding .c file to get a rebuild happening. This is mac OS 10.4.9, powerpc G5, sage 2.3.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/326\n\n",
    "created_at": "2007-03-21T04:25:32Z",
    "labels": [
        "packages: standard",
        "major",
        "bug"
    ],
    "title": "rebuild system doesn't recognise changed pyrex files on OS X",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/326",
    "user": "dmharvey"
}
```
Assignee: @williamstein

When I change a pyrex file (specifically rings/integer.pyx), sage -b doesn't seem to notice. I have to manually delete the corresponding .c file to get a rebuild happening. This is mac OS 10.4.9, powerpc G5, sage 2.3.


Issue created by migration from https://trac.sagemath.org/ticket/326





---

archive/issue_comments_001541.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2007-03-21T22:35:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/326#issuecomment-1541",
    "user": "@williamstein"
}
```

Resolution: invalid



---

archive/issue_comments_001542.json:
```json
{
    "body": "Depedency checking works fine on OS X Intel.  In fact I wrote it under OS X intel.  I\ntried exactly your example and it works. \n\nI also just tested on a G5 intel machine and dependency testing works fine under sage-2.3.\n\nI have no idea how your install is messed up, but the problem isn't something general.",
    "created_at": "2007-03-21T22:35:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/326#issuecomment-1542",
    "user": "@williamstein"
}
```

Depedency checking works fine on OS X Intel.  In fact I wrote it under OS X intel.  I
tried exactly your example and it works. 

I also just tested on a G5 intel machine and dependency testing works fine under sage-2.3.

I have no idea how your install is messed up, but the problem isn't something general.



---

archive/issue_comments_001543.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2007-03-22T02:21:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/326#issuecomment-1543",
    "user": "@williamstein"
}
```

Changing status from closed to reopened.



---

archive/issue_comments_001544.json:
```json
{
    "body": "Resolution changed from invalid to ",
    "created_at": "2007-03-22T02:21:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/326#issuecomment-1544",
    "user": "@williamstein"
}
```

Resolution changed from invalid to 



---

archive/issue_comments_001545.json:
```json
{
    "body": "We changed some getctimes to getmtimes and all is well now for David.",
    "created_at": "2007-03-22T02:21:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/326#issuecomment-1545",
    "user": "@williamstein"
}
```

We changed some getctimes to getmtimes and all is well now for David.



---

archive/issue_comments_001546.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-03-22T02:21:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/326#issuecomment-1546",
    "user": "@williamstein"
}
```

Resolution: fixed
