# Issue 992: Need an extra "sage -b" after an upgrade

archive/issues_000992.json:
```json
{
    "body": "Assignee: @williamstein\n\nWhen doing sage -ugprade, i.e., running SAGE_ROOT/devel/sage/spkg-install, there should be one extra \"sage -b\"  again at the end to ensure that the new versions of all .pyx files get copied to the build directory.\n\n\nThis is incredibly easy to fix.\n\nIssue created by migration from https://trac.sagemath.org/ticket/992\n\n",
    "created_at": "2007-10-25T02:08:34Z",
    "labels": [
        "component: packages: standard",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.9",
    "title": "Need an extra \"sage -b\" after an upgrade",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/992",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

When doing sage -ugprade, i.e., running SAGE_ROOT/devel/sage/spkg-install, there should be one extra "sage -b"  again at the end to ensure that the new versions of all .pyx files get copied to the build directory.


This is incredibly easy to fix.

Issue created by migration from https://trac.sagemath.org/ticket/992





---

archive/issue_comments_006031.json:
```json
{
    "body": "Attachment [992.patch](tarball://root/attachments/some-uuid/ticket992/992.patch) by @williamstein created at 2007-10-25 02:09:23\n\nthis probably fixes the problem, though it is hard to test.  time will tell.",
    "created_at": "2007-10-25T02:09:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/992",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/992#issuecomment-6031",
    "user": "https://github.com/williamstein"
}
```

Attachment [992.patch](tarball://root/attachments/some-uuid/ticket992/992.patch) by @williamstein created at 2007-10-25 02:09:23

this probably fixes the problem, though it is hard to test.  time will tell.



---

archive/issue_comments_006032.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-25T07:56:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/992",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/992#issuecomment-6032",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed
