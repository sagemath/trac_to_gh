# Issue 4620: setup.py: if the cythonization fails then next "sage -b" starts to build extensions

archive/issues_004620.json:
```json
{
    "body": "Assignee: craigcitro\n\nThis is with 3.2.1.alpha1-current. To reproduce do a \"sage -ba\" and have a Cython process fail. Then the next \"sage -b\" will not pick up with the Cythonization again, but start building extensions.\n\nDeleting .cython_deps does not fix the problem.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/4620\n\n",
    "created_at": "2008-11-25T23:19:49Z",
    "labels": [
        "build",
        "blocker",
        "bug"
    ],
    "title": "setup.py: if the cythonization fails then next \"sage -b\" starts to build extensions",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4620",
    "user": "mabshoff"
}
```
Assignee: craigcitro

This is with 3.2.1.alpha1-current. To reproduce do a "sage -ba" and have a Cython process fail. Then the next "sage -b" will not pick up with the Cythonization again, but start building extensions.

Deleting .cython_deps does not fix the problem.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/4620





---

archive/issue_comments_034733.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-11-26T08:45:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4620",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4620#issuecomment-34733",
    "user": "craigcitro"
}
```

Attachment



---

archive/issue_comments_034734.json:
```json
{
    "body": "The attached patch fixes the issue. The problem was that we were copying the files at one point in the code, and then running Cython later. Of course, if Cython failed, the code was still copied, which meant it would pass a timestamp comparison on later builds. The patch fixes this by only copying once the file is successfully built. \n\nIn addition, it slightly expands the capabilities of William's parallel build code: now, in addition to accepting strings, it accepts pairs of the form `[f, v]`, and calls `f(v)`. The previous code did this with `f` always being `run_command`.",
    "created_at": "2008-11-26T08:49:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4620",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4620#issuecomment-34734",
    "user": "craigcitro"
}
```

The attached patch fixes the issue. The problem was that we were copying the files at one point in the code, and then running Cython later. Of course, if Cython failed, the code was still copied, which meant it would pass a timestamp comparison on later builds. The patch fixes this by only copying once the file is successfully built. 

In addition, it slightly expands the capabilities of William's parallel build code: now, in addition to accepting strings, it accepts pairs of the form `[f, v]`, and calls `f(v)`. The previous code did this with `f` always being `run_command`.



---

archive/issue_comments_034735.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-11-26T08:49:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4620",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4620#issuecomment-34735",
    "user": "craigcitro"
}
```

Changing status from new to assigned.



---

archive/issue_comments_034736.json:
```json
{
    "body": "Nice work. Thanks for fixing this quickly.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-26T09:35:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4620",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4620#issuecomment-34736",
    "user": "mabshoff"
}
```

Nice work. Thanks for fixing this quickly.

Cheers,

Michael



---

archive/issue_comments_034737.json:
```json
{
    "body": "Merged in Sage 3.2.1.alpha1",
    "created_at": "2008-11-26T09:35:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4620",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4620#issuecomment-34737",
    "user": "mabshoff"
}
```

Merged in Sage 3.2.1.alpha1



---

archive/issue_comments_034738.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-11-26T09:35:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4620",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4620#issuecomment-34738",
    "user": "mabshoff"
}
```

Resolution: fixed
