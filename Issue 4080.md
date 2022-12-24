# Issue 4080: [with patch, needs review] Symbol clash between global M4RI and PolyBoRi's M4RI

archive/issues_004080.json:
```json
{
    "body": "Assignee: @malb\n\nCC:  polybori\n\nKeywords: sigsegv\n\nPolyBoRi uses its own M4RI instance which is older than the version of M4RI which is going to be in Sage 3.1.2. Since M4RI is written in C there are no namespaces and thus the symbols clash, even though both versions are binary incompatible. A workaround for now -- until PolyBoRi is updated -- is to delay the import of `sage.rings.pbring` after the import of `sage.matrix.matrix_mod2_dense`. Since PolyBoRi is statically linked for now anyway, this shouldn't mess up things. However **this is a dirty workaround**\n\nIssue created by migration from https://trac.sagemath.org/ticket/4080\n\n",
    "created_at": "2008-09-08T23:03:27Z",
    "labels": [
        "misc",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.2",
    "title": "[with patch, needs review] Symbol clash between global M4RI and PolyBoRi's M4RI",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4080",
    "user": "@malb"
}
```
Assignee: @malb

CC:  polybori

Keywords: sigsegv

PolyBoRi uses its own M4RI instance which is older than the version of M4RI which is going to be in Sage 3.1.2. Since M4RI is written in C there are no namespaces and thus the symbols clash, even though both versions are binary incompatible. A workaround for now -- until PolyBoRi is updated -- is to delay the import of `sage.rings.pbring` after the import of `sage.matrix.matrix_mod2_dense`. Since PolyBoRi is statically linked for now anyway, this shouldn't mess up things. However **this is a dirty workaround**

Issue created by migration from https://trac.sagemath.org/ticket/4080





---

archive/issue_comments_029440.json:
```json
{
    "body": "Attachment [pbimport.patch](tarball://root/attachments/some-uuid/ticket4080/pbimport.patch) by @malb created at 2008-09-08 23:03:56",
    "created_at": "2008-09-08T23:03:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4080",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4080#issuecomment-29440",
    "user": "@malb"
}
```

Attachment [pbimport.patch](tarball://root/attachments/some-uuid/ticket4080/pbimport.patch) by @malb created at 2008-09-08 23:03:56



---

archive/issue_comments_029441.json:
```json
{
    "body": "btw. this patch can remain applied and does not need to be reverted once the issue at hand is fixed. This is, because it is a good idea to late import more stuff anyway.",
    "created_at": "2008-09-08T23:05:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4080",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4080#issuecomment-29441",
    "user": "@malb"
}
```

btw. this patch can remain applied and does not need to be reverted once the issue at hand is fixed. This is, because it is a good idea to late import more stuff anyway.



---

archive/issue_comments_029442.json:
```json
{
    "body": "The patch is good, it fixes the issue on OSX and does pass doctests on Linux. Positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-08T23:15:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4080",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4080#issuecomment-29442",
    "user": "mabshoff"
}
```

The patch is good, it fixes the issue on OSX and does pass doctests on Linux. Positive review.

Cheers,

Michael



---

archive/issue_comments_029443.json:
```json
{
    "body": "Merged in Sage 3.1.2.rc1",
    "created_at": "2008-09-08T23:57:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4080",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4080#issuecomment-29443",
    "user": "mabshoff"
}
```

Merged in Sage 3.1.2.rc1



---

archive/issue_comments_029444.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-08T23:57:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4080",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4080#issuecomment-29444",
    "user": "mabshoff"
}
```

Resolution: fixed
