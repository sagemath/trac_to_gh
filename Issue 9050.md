# Issue 9050: libntl.dll should be libntl.dll.a on Cygwin

archive/issues_009050.json:
```json
{
    "body": "Assignee: tbd\n\nThis is so that Cygwin will find the shared library before it finds the static library; otherwise, there are lots of segfaults in Sage under Cygwin\n\nIssue created by migration from https://trac.sagemath.org/ticket/9050\n\n",
    "created_at": "2010-05-25T22:54:28Z",
    "labels": [
        "porting: Cygwin",
        "major",
        "bug"
    ],
    "title": "libntl.dll should be libntl.dll.a on Cygwin",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9050",
    "user": "mhansen"
}
```
Assignee: tbd

This is so that Cygwin will find the shared library before it finds the static library; otherwise, there are lots of segfaults in Sage under Cygwin

Issue created by migration from https://trac.sagemath.org/ticket/9050





---

archive/issue_comments_083797.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-05-25T22:57:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9050",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9050#issuecomment-83797",
    "user": "mhansen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_083798.json:
```json
{
    "body": "There is an spkg for this at http://sage.math.washington.edu/home/mhansen/ntl-5.4.2.p12.spkg",
    "created_at": "2010-05-25T22:57:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9050",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9050#issuecomment-83798",
    "user": "mhansen"
}
```

There is an spkg for this at http://sage.math.washington.edu/home/mhansen/ntl-5.4.2.p12.spkg



---

archive/issue_comments_083799.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-05-26T01:08:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9050",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9050#issuecomment-83799",
    "user": "was"
}
```

Resolution: fixed
