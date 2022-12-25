# Issue 9050: libntl.dll should be libntl.dll.a on Cygwin

archive/issues_009050.json:
```json
{
    "body": "Assignee: tbd\n\nThis is so that Cygwin will find the shared library before it finds the static library; otherwise, there are lots of segfaults in Sage under Cygwin\n\nIssue created by migration from https://trac.sagemath.org/ticket/9050\n\n",
    "created_at": "2010-05-25T22:54:28Z",
    "labels": [
        "component: porting: cygwin",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.3",
    "title": "libntl.dll should be libntl.dll.a on Cygwin",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9050",
    "user": "https://github.com/mwhansen"
}
```
Assignee: tbd

This is so that Cygwin will find the shared library before it finds the static library; otherwise, there are lots of segfaults in Sage under Cygwin

Issue created by migration from https://trac.sagemath.org/ticket/9050





---

archive/issue_comments_083661.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-05-25T22:57:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9050",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9050#issuecomment-83661",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_083662.json:
```json
{
    "body": "There is an spkg for this at http://sage.math.washington.edu/home/mhansen/ntl-5.4.2.p12.spkg",
    "created_at": "2010-05-25T22:57:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9050",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9050#issuecomment-83662",
    "user": "https://github.com/mwhansen"
}
```

There is an spkg for this at http://sage.math.washington.edu/home/mhansen/ntl-5.4.2.p12.spkg



---

archive/issue_events_009201.json:
```json
{
    "actor": "@williamstein",
    "created_at": "2010-05-26T01:08:21Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9050",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9050#event-9201"
}
```



---

archive/issue_comments_083663.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-05-26T01:08:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9050",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9050#issuecomment-83663",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed
