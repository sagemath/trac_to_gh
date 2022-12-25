# Issue 6610: Compiler environment variables should be consistent

archive/issues_006610.json:
```json
{
    "body": "Assignee: tbd\n\nKeywords: Environment\n\nSage sets the environment variable LIBRARY_PATH which is a gcc variable.  OTOH, it doesn't set CPATH or C_INCLUDE_PATH or CPLUS_INCLUDE_PATH.  This causes inconsistencies, particularly since Sage replicates many Linux libraries potentially leading to version issues.\n\nLD_LIBRARY_PATH is also set (appended / modified), as it would need to be, but that is for the loader (ld).  Sometimes this leads to difficulties when running non-Sage installed executables which use replicated libraries.  One example is Git which doesn't like Sage's zlib.\n\nThis latter problem is more difficult to address and rarely causes difficulty.  In fact, the only manifestation I've seen is git although it seems obvious that there are potential problems lurking.\n\nIn my case, I replace the symlinks for libz.so* to reference the system libraries.  This will work as long as major version's (interfaces) are consistent.\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6610\n\n",
    "created_at": "2009-07-24T04:21:32Z",
    "labels": [
        "component: build",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Compiler environment variables should be consistent",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6610",
    "user": "https://trac.sagemath.org/admin/accounts/users/ghtdak"
}
```
Assignee: tbd

Keywords: Environment

Sage sets the environment variable LIBRARY_PATH which is a gcc variable.  OTOH, it doesn't set CPATH or C_INCLUDE_PATH or CPLUS_INCLUDE_PATH.  This causes inconsistencies, particularly since Sage replicates many Linux libraries potentially leading to version issues.

LD_LIBRARY_PATH is also set (appended / modified), as it would need to be, but that is for the loader (ld).  Sometimes this leads to difficulties when running non-Sage installed executables which use replicated libraries.  One example is Git which doesn't like Sage's zlib.

This latter problem is more difficult to address and rarely causes difficulty.  In fact, the only manifestation I've seen is git although it seems obvious that there are potential problems lurking.

In my case, I replace the symlinks for libz.so* to reference the system libraries.  This will work as long as major version's (interfaces) are consistent.



Issue created by migration from https://trac.sagemath.org/ticket/6610





---

archive/issue_comments_054008.json:
```json
{
    "body": "This is essentially a duplicate of #10572.",
    "created_at": "2013-12-29T23:08:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6610",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6610#issuecomment-54008",
    "user": "https://github.com/jdemeyer"
}
```

This is essentially a duplicate of #10572.



---

archive/issue_comments_054009.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2013-12-29T23:08:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6610",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6610#issuecomment-54009",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_054010.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-12-29T23:08:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6610",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6610#issuecomment-54010",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_054011.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2014-01-04T04:27:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6610",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6610#issuecomment-54011",
    "user": "https://github.com/vbraun"
}
```

Resolution: duplicate
