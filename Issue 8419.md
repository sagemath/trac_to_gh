# Issue 8419: cddlib fails to build on OpenSolaris fully.

archive/issues_008419.json:
```json
{
    "body": "Assignee: drkirkby\n\nCC:  jsp mvngu\n\nAs reported by Jaap Spies, one of the reviewers of #8363, the package is not building properly as a 64-bit binary on OpenSolaris. This is despite the fact that CFLAGS includes -m64. It might be the lack of LDFLAGS being exported which is causing this problem. Whatever the cause is, this needs to work for a complete port to OpenSolaris. \n\nIssue created by migration from https://trac.sagemath.org/ticket/8419\n\n",
    "created_at": "2010-03-02T14:04:28Z",
    "labels": [
        "porting: Solaris",
        "major",
        "bug"
    ],
    "title": "cddlib fails to build on OpenSolaris fully.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8419",
    "user": "drkirkby"
}
```
Assignee: drkirkby

CC:  jsp mvngu

As reported by Jaap Spies, one of the reviewers of #8363, the package is not building properly as a 64-bit binary on OpenSolaris. This is despite the fact that CFLAGS includes -m64. It might be the lack of LDFLAGS being exported which is causing this problem. Whatever the cause is, this needs to work for a complete port to OpenSolaris. 

Issue created by migration from https://trac.sagemath.org/ticket/8419





---

archive/issue_comments_075451.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-11T19:20:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8419",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8419#issuecomment-75451",
    "user": "drkirkby"
}
```

Resolution: fixed



---

archive/issue_comments_075452.json:
```json
{
    "body": "This issue is resolved by #8363, so I am closing it. \n\nDave",
    "created_at": "2010-06-11T19:20:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8419",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8419#issuecomment-75452",
    "user": "drkirkby"
}
```

This issue is resolved by #8363, so I am closing it. 

Dave
