# Issue 1593: m4ri -- the documentation of the echelon command only lists 1 algorithm but >= 2 algorithms are supported

archive/issues_001593.json:
```json
{
    "body": "Assignee: tba\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1593\n\n",
    "created_at": "2007-12-24T17:36:31Z",
    "labels": [
        "documentation",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.1",
    "title": "m4ri -- the documentation of the echelon command only lists 1 algorithm but >= 2 algorithms are supported",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1593",
    "user": "@williamstein"
}
```
Assignee: tba



Issue created by migration from https://trac.sagemath.org/ticket/1593





---

archive/issue_comments_010135.json:
```json
{
    "body": "Also, there is a bug in algorithm = \"classical\", since it doesn't\ncheck for mutability and doesn't clear the cache.",
    "created_at": "2007-12-24T17:37:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1593",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1593#issuecomment-10135",
    "user": "@williamstein"
}
```

Also, there is a bug in algorithm = "classical", since it doesn't
check for mutability and doesn't clear the cache.



---

archive/issue_comments_010136.json:
```json
{
    "body": "Changing assignee from tba to @malb.",
    "created_at": "2007-12-24T17:37:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1593",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1593#issuecomment-10136",
    "user": "@williamstein"
}
```

Changing assignee from tba to @malb.



---

archive/issue_comments_010137.json:
```json
{
    "body": "Attachment [trac_1593.patch](tarball://root/attachments/some-uuid/ticket1593/trac_1593.patch) by @malb created at 2007-12-25 16:17:49",
    "created_at": "2007-12-25T16:17:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1593",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1593#issuecomment-10137",
    "user": "@malb"
}
```

Attachment [trac_1593.patch](tarball://root/attachments/some-uuid/ticket1593/trac_1593.patch) by @malb created at 2007-12-25 16:17:49



---

archive/issue_comments_010138.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-12-25T16:19:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1593",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1593#issuecomment-10138",
    "user": "@malb"
}
```

Changing status from new to assigned.



---

archive/issue_comments_010139.json:
```json
{
    "body": "the attached patch adds 'classical' to the docstring of `echelonize`. The remark about `algorithm=\"classical\"` is invalid because the called method `_echelon_in_place_classical` does check for mutability and clears the cache. See `matrix2.pyx` for details.",
    "created_at": "2007-12-25T16:19:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1593",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1593#issuecomment-10139",
    "user": "@malb"
}
```

the attached patch adds 'classical' to the docstring of `echelonize`. The remark about `algorithm="classical"` is invalid because the called method `_echelon_in_place_classical` does check for mutability and clears the cache. See `matrix2.pyx` for details.



---

archive/issue_comments_010140.json:
```json
{
    "body": "Patch looks good to me.\n\nCheers,\n\nMichael",
    "created_at": "2008-01-25T17:34:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1593",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1593#issuecomment-10140",
    "user": "mabshoff"
}
```

Patch looks good to me.

Cheers,

Michael



---

archive/issue_comments_010141.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-25T17:34:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1593",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1593#issuecomment-10141",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_010142.json:
```json
{
    "body": "Merged in Sage 2.10.1.alpha2",
    "created_at": "2008-01-25T17:34:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1593",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1593#issuecomment-10142",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.1.alpha2
