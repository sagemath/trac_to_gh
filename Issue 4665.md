# Issue 4665: sage/misc/cython.py creates file sage/misc/hello.spyx in tree while doctesting

archive/issues_004665.json:
```json
{
    "body": "Assignee: mabshoff\n\n#4660 exposed a bug in sage/misc/cython.py: hello.spyx is created in tree, but that file should be created in the Sage tmp directory.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/4665\n\n",
    "created_at": "2008-11-30T10:04:17Z",
    "labels": [
        "doctest coverage",
        "critical",
        "bug"
    ],
    "title": "sage/misc/cython.py creates file sage/misc/hello.spyx in tree while doctesting",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4665",
    "user": "mabshoff"
}
```
Assignee: mabshoff

#4660 exposed a bug in sage/misc/cython.py: hello.spyx is created in tree, but that file should be created in the Sage tmp directory.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/4665





---

archive/issue_comments_035116.json:
```json
{
    "body": "Attachment [trac_4665.patch](tarball://root/attachments/some-uuid/ticket4665/trac_4665.patch) by was created at 2009-01-24 06:51:38",
    "created_at": "2009-01-24T06:51:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4665",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4665#issuecomment-35116",
    "user": "was"
}
```

Attachment [trac_4665.patch](tarball://root/attachments/some-uuid/ticket4665/trac_4665.patch) by was created at 2009-01-24 06:51:38



---

archive/issue_comments_035117.json:
```json
{
    "body": "Positive review.\n\nCheers,\n\nMichael",
    "created_at": "2009-01-24T12:25:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4665",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4665#issuecomment-35117",
    "user": "mabshoff"
}
```

Positive review.

Cheers,

Michael



---

archive/issue_comments_035118.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-24T13:16:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4665",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4665#issuecomment-35118",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_035119.json:
```json
{
    "body": "Merged in Sage 3.3.alpha2",
    "created_at": "2009-01-24T13:16:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4665",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4665#issuecomment-35119",
    "user": "mabshoff"
}
```

Merged in Sage 3.3.alpha2
