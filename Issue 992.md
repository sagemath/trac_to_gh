# Issue 992: Need an extra "sage -b" after an upgrade

archive/issues_000992.json:
```json
{
    "body": "Assignee: was\n\nWhen doing sage -ugprade, i.e., running SAGE_ROOT/devel/sage/spkg-install, there should be one extra \"sage -b\"  again at the end to ensure that the new versions of all .pyx files get copied to the build directory.\n\n\nThis is incredibly easy to fix.\n\nIssue created by migration from https://trac.sagemath.org/ticket/992\n\n",
    "created_at": "2007-10-25T02:08:34Z",
    "labels": [
        "packages: standard",
        "major",
        "bug"
    ],
    "title": "Need an extra \"sage -b\" after an upgrade",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/992",
    "user": "was"
}
```
Assignee: was

When doing sage -ugprade, i.e., running SAGE_ROOT/devel/sage/spkg-install, there should be one extra "sage -b"  again at the end to ensure that the new versions of all .pyx files get copied to the build directory.


This is incredibly easy to fix.

Issue created by migration from https://trac.sagemath.org/ticket/992





---

archive/issue_comments_006051.json:
```json
{
    "body": "Attachment\n\nthis probably fixes the problem, though it is hard to test.  time will tell.",
    "created_at": "2007-10-25T02:09:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/992",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/992#issuecomment-6051",
    "user": "was"
}
```

Attachment

this probably fixes the problem, though it is hard to test.  time will tell.



---

archive/issue_comments_006052.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-25T07:56:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/992",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/992#issuecomment-6052",
    "user": "was"
}
```

Resolution: fixed
