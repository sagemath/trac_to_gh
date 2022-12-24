# Issue 1722: Symbolic Matrices should be callable.

archive/issues_001722.json:
```json
{
    "body": "Assignee: was\n\nMatrices of symbolic objects should either be callable, or support substitution, per user request at conference.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1722\n\n",
    "created_at": "2008-01-08T19:11:43Z",
    "labels": [
        "linear algebra",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.3",
    "title": "Symbolic Matrices should be callable.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1722",
    "user": "boothby"
}
```
Assignee: was

Matrices of symbolic objects should either be callable, or support substitution, per user request at conference.

Issue created by migration from https://trac.sagemath.org/ticket/1722





---

archive/issue_comments_010913.json:
```json
{
    "body": "Changing assignee from was to mhansen.",
    "created_at": "2008-01-27T01:17:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1722",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1722#issuecomment-10913",
    "user": "mhansen"
}
```

Changing assignee from was to mhansen.



---

archive/issue_comments_010914.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-01-27T01:17:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1722",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1722#issuecomment-10914",
    "user": "mhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_010915.json:
```json
{
    "body": "Great doctests, good comments, looks good to me.  I say apply.",
    "created_at": "2008-02-15T05:17:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1722",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1722#issuecomment-10915",
    "user": "ncalexan"
}
```

Great doctests, good comments, looks good to me.  I say apply.



---

archive/issue_comments_010916.json:
```json
{
    "body": "Against my 2.10.2.alpha0 I get a reject:\n\n```\npatch -p1 --dry-run < trac_1722.patch\npatching file sage/matrix/matrix_symbolic_dense.pxd\npatching file sage/matrix/matrix_symbolic_dense.pyx\nHunk #1 succeeded at 15 with fuzz 2 (offset 9 lines).\nHunk #2 succeeded at 48 with fuzz 2 (offset 8 lines).\nHunk #3 succeeded at 536 (offset 248 lines).\nHunk #4 FAILED at 617.\nHunk #5 FAILED at 681.\n2 out of 5 hunks FAILED -- saving rejects to file sage/matrix/matrix_symbolic_dense.pyx.rej\n```\n\nThe patch should be rebased against 2.10.2.alpha0 once it is out.\n\nCheers,\n\nMichael",
    "created_at": "2008-02-15T05:20:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1722",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1722#issuecomment-10916",
    "user": "mabshoff"
}
```

Against my 2.10.2.alpha0 I get a reject:

```
patch -p1 --dry-run < trac_1722.patch
patching file sage/matrix/matrix_symbolic_dense.pxd
patching file sage/matrix/matrix_symbolic_dense.pyx
Hunk #1 succeeded at 15 with fuzz 2 (offset 9 lines).
Hunk #2 succeeded at 48 with fuzz 2 (offset 8 lines).
Hunk #3 succeeded at 536 (offset 248 lines).
Hunk #4 FAILED at 617.
Hunk #5 FAILED at 681.
2 out of 5 hunks FAILED -- saving rejects to file sage/matrix/matrix_symbolic_dense.pyx.rej
```

The patch should be rebased against 2.10.2.alpha0 once it is out.

Cheers,

Michael



---

archive/issue_comments_010917.json:
```json
{
    "body": "Attachment [1722.patch](tarball://root/attachments/some-uuid/ticket1722/1722.patch) by mhansen created at 2008-02-27 20:16:25",
    "created_at": "2008-02-27T20:16:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1722",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1722#issuecomment-10917",
    "user": "mhansen"
}
```

Attachment [1722.patch](tarball://root/attachments/some-uuid/ticket1722/1722.patch) by mhansen created at 2008-02-27 20:16:25



---

archive/issue_comments_010918.json:
```json
{
    "body": "New rebased patch attached.",
    "created_at": "2008-02-27T20:16:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1722",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1722#issuecomment-10918",
    "user": "mhansen"
}
```

New rebased patch attached.



---

archive/issue_comments_010919.json:
```json
{
    "body": "Merged in Sage 2.10.3.rc0",
    "created_at": "2008-02-28T00:43:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1722",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1722#issuecomment-10919",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.3.rc0



---

archive/issue_comments_010920.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-28T00:43:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1722",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1722#issuecomment-10920",
    "user": "mabshoff"
}
```

Resolution: fixed
