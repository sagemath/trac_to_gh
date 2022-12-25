# Issue 4620: setup.py: if the cythonization fails then next "sage -b" starts to build extensions

archive/issues_004620.json:
```json
{
    "body": "Assignee: @craigcitro\n\nThis is with 3.2.1.alpha1-current. To reproduce do a \"sage -ba\" and have a Cython process fail. Then the next \"sage -b\" will not pick up with the Cythonization again, but start building extensions.\n\nDeleting .cython_deps does not fix the problem.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/4620\n\n",
    "created_at": "2008-11-25T23:19:49Z",
    "labels": [
        "component: build",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.1",
    "title": "setup.py: if the cythonization fails then next \"sage -b\" starts to build extensions",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4620",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: @craigcitro

This is with 3.2.1.alpha1-current. To reproduce do a "sage -ba" and have a Cython process fail. Then the next "sage -b" will not pick up with the Cythonization again, but start building extensions.

Deleting .cython_deps does not fix the problem.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/4620





---

archive/issue_comments_034666.json:
```json
{
    "body": "Attachment [trac-4620.patch](tarball://root/attachments/some-uuid/ticket4620/trac-4620.patch) by @craigcitro created at 2008-11-26 08:45:22",
    "created_at": "2008-11-26T08:45:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4620",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4620#issuecomment-34666",
    "user": "https://github.com/craigcitro"
}
```

Attachment [trac-4620.patch](tarball://root/attachments/some-uuid/ticket4620/trac-4620.patch) by @craigcitro created at 2008-11-26 08:45:22



---

archive/issue_comments_034667.json:
```json
{
    "body": "The attached patch fixes the issue. The problem was that we were copying the files at one point in the code, and then running Cython later. Of course, if Cython failed, the code was still copied, which meant it would pass a timestamp comparison on later builds. The patch fixes this by only copying once the file is successfully built. \n\nIn addition, it slightly expands the capabilities of William's parallel build code: now, in addition to accepting strings, it accepts pairs of the form `[f, v]`, and calls `f(v)`. The previous code did this with `f` always being `run_command`.",
    "created_at": "2008-11-26T08:49:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4620",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4620#issuecomment-34667",
    "user": "https://github.com/craigcitro"
}
```

The attached patch fixes the issue. The problem was that we were copying the files at one point in the code, and then running Cython later. Of course, if Cython failed, the code was still copied, which meant it would pass a timestamp comparison on later builds. The patch fixes this by only copying once the file is successfully built. 

In addition, it slightly expands the capabilities of William's parallel build code: now, in addition to accepting strings, it accepts pairs of the form `[f, v]`, and calls `f(v)`. The previous code did this with `f` always being `run_command`.



---

archive/issue_comments_034668.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-11-26T08:49:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4620",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4620#issuecomment-34668",
    "user": "https://github.com/craigcitro"
}
```

Changing status from new to assigned.



---

archive/issue_comments_034669.json:
```json
{
    "body": "Nice work. Thanks for fixing this quickly.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-26T09:35:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4620",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4620#issuecomment-34669",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Nice work. Thanks for fixing this quickly.

Cheers,

Michael



---

archive/issue_comments_034670.json:
```json
{
    "body": "Merged in Sage 3.2.1.alpha1",
    "created_at": "2008-11-26T09:35:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4620",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4620#issuecomment-34670",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.2.1.alpha1



---

archive/issue_comments_034671.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-11-26T09:35:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4620",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4620#issuecomment-34671",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
