# Issue 887: 2.8.7-alpha0: doctest failure in rings/polynomial/real_roots.pyx

archive/issues_000887.json:
```json
{
    "body": "Assignee: failure\n\nAll three errors are essentially the same; here's one of them:\n\n```\nFile \"real_roots.pyx\", line 797:\n    sage: str(dbp)\nExpected:\n    '<IBP: (-1, 148, 901) + [0 .. 4); level 1; slope_err [-24.000000000000000 .. 24.000000000000000]>'\nGot:\n    '<IBP: (-1, 148, 901) + [0 .. 4); level 1>'\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/887\n\n",
    "created_at": "2007-10-13T20:31:31Z",
    "labels": [
        "doctest coverage",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.7",
    "title": "2.8.7-alpha0: doctest failure in rings/polynomial/real_roots.pyx",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/887",
    "user": "cwitty"
}
```
Assignee: failure

All three errors are essentially the same; here's one of them:

```
File "real_roots.pyx", line 797:
    sage: str(dbp)
Expected:
    '<IBP: (-1, 148, 901) + [0 .. 4); level 1; slope_err [-24.000000000000000 .. 24.000000000000000]>'
Got:
    '<IBP: (-1, 148, 901) + [0 .. 4); level 1>'
```



Issue created by migration from https://trac.sagemath.org/ticket/887





---

archive/issue_comments_005474.json:
```json
{
    "body": "Attachment [6930.patch](tarball://root/attachments/some-uuid/ticket887/6930.patch) by cwitty created at 2007-10-13 22:11:40",
    "created_at": "2007-10-13T22:11:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/887",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/887#issuecomment-5474",
    "user": "cwitty"
}
```

Attachment [6930.patch](tarball://root/attachments/some-uuid/ticket887/6930.patch) by cwitty created at 2007-10-13 22:11:40



---

archive/issue_comments_005475.json:
```json
{
    "body": "This one was all my fault :-)\n\nMy original code was buggy, but the bug was masked by a Cython bug.  But I was the one who reported the Cython bug and triggered the fix, exposing this bug...",
    "created_at": "2007-10-13T22:12:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/887",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/887#issuecomment-5475",
    "user": "cwitty"
}
```

This one was all my fault :-)

My original code was buggy, but the bug was masked by a Cython bug.  But I was the one who reported the Cython bug and triggered the fix, exposing this bug...



---

archive/issue_comments_005476.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-14T22:56:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/887",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/887#issuecomment-5476",
    "user": "@williamstein"
}
```

Resolution: fixed
