# Issue 6086: [with patch, needs review] fixed laplacian_matrix in graph.py

archive/issues_006086.json:
```json
{
    "body": "Assignee: dperkinson\n\nCC:  ekirkman\n\nKeywords: kirchhoff laplacian matrix\n\nThe kirchhoff_matrix/laplacian_matrix did not handle graphs with loops correctly.\n\nThe patch fixes the bug and adds a doctest that fails without the patch.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6086\n\n",
    "created_at": "2009-05-19T19:51:13Z",
    "labels": [
        "graph theory",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0",
    "title": "[with patch, needs review] fixed laplacian_matrix in graph.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6086",
    "user": "dperkinson"
}
```
Assignee: dperkinson

CC:  ekirkman

Keywords: kirchhoff laplacian matrix

The kirchhoff_matrix/laplacian_matrix did not handle graphs with loops correctly.

The patch fixes the bug and adds a doctest that fails without the patch.

Issue created by migration from https://trac.sagemath.org/ticket/6086





---

archive/issue_comments_048492.json:
```json
{
    "body": "Attachment [trac_6086_laplacian.patch](tarball://root/attachments/some-uuid/ticket6086/trac_6086_laplacian.patch) by dperkinson created at 2009-05-19 19:53:48",
    "created_at": "2009-05-19T19:53:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6086",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6086#issuecomment-48492",
    "user": "dperkinson"
}
```

Attachment [trac_6086_laplacian.patch](tarball://root/attachments/some-uuid/ticket6086/trac_6086_laplacian.patch) by dperkinson created at 2009-05-19 19:53:48



---

archive/issue_comments_048493.json:
```json
{
    "body": "Passes doctests and fixes bug.  Good job!",
    "created_at": "2009-05-19T20:13:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6086",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6086#issuecomment-48493",
    "user": "ekirkman"
}
```

Passes doctests and fixes bug.  Good job!



---

archive/issue_comments_048494.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-05-19T20:24:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6086",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6086#issuecomment-48494",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_048495.json:
```json
{
    "body": "Merged in Sage 4.0.rc0.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-19T20:24:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6086",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6086#issuecomment-48495",
    "user": "mabshoff"
}
```

Merged in Sage 4.0.rc0.

Cheers,

Michael
