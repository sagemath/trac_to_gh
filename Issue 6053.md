# Issue 6053: Cython numpy broken in notebook

archive/issues_006053.json:
```json
{
    "body": "Assignee: jkantor\n\nKeywords: numpy, cython, notebook\n\nin a notebook cell with\n\n\n\n```\n%cython\ncimport numpy as np\n```\n\n\nan error is thrown because numpy/arrayobject.h isn't found by gcc.  No directive for the numpy include directories is part of the compiler invocation.\n\nthe header path is:\n\n$SAGE_LOCAL/lib/python2.5/site-packages/numpy/core/include/numpy/arrayobject.h\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6053\n\n",
    "created_at": "2009-05-17T04:44:56Z",
    "labels": [
        "numerical",
        "minor",
        "bug"
    ],
    "title": "Cython numpy broken in notebook",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6053",
    "user": "ghtdak"
}
```
Assignee: jkantor

Keywords: numpy, cython, notebook

in a notebook cell with



```
%cython
cimport numpy as np
```


an error is thrown because numpy/arrayobject.h isn't found by gcc.  No directive for the numpy include directories is part of the compiler invocation.

the header path is:

$SAGE_LOCAL/lib/python2.5/site-packages/numpy/core/include/numpy/arrayobject.h



Issue created by migration from https://trac.sagemath.org/ticket/6053





---

archive/issue_comments_048216.json:
```json
{
    "body": "Attachment [trac-6053-cython-numpy-header.patch](tarball://root/attachments/some-uuid/ticket6053/trac-6053-cython-numpy-header.patch) by jason created at 2009-05-28 07:09:28",
    "created_at": "2009-05-28T07:09:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6053",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6053#issuecomment-48216",
    "user": "jason"
}
```

Attachment [trac-6053-cython-numpy-header.patch](tarball://root/attachments/some-uuid/ticket6053/trac-6053-cython-numpy-header.patch) by jason created at 2009-05-28 07:09:28



---

archive/issue_comments_048217.json:
```json
{
    "body": "Looks good to me.\n\nMerged in 4.0.rc1.",
    "created_at": "2009-05-28T07:17:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6053",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6053#issuecomment-48217",
    "user": "mhansen"
}
```

Looks good to me.

Merged in 4.0.rc1.



---

archive/issue_comments_048218.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-05-28T07:17:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6053",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6053#issuecomment-48218",
    "user": "mhansen"
}
```

Resolution: fixed
