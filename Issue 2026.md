# Issue 2026: matrix.eigenspaces doctest description is misleading

archive/issues_002026.json:
```json
{
    "body": "Assignee: was\n\nIn matrix2.pyx under eigenspaces():\n\n\n```\n        Next we compute the eigenspaces over the finite field\n        of order 11:\n        \n            sage: # A = ModularSymbols(43, base_ring=GF(11), sign=1).T(2).matrix()\n            sage: A = matrix(QQ, 4, [3, 9, 0, 0, 0, 9, 0, 1, 0, 10, 9, 2, 0, 9, 0, 2])\n```\n\n\nIt seems like the description should be deleted or the doctest should be run and the output included.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2026\n\n",
    "created_at": "2008-02-01T19:18:58Z",
    "labels": [
        "linear algebra",
        "minor",
        "bug"
    ],
    "title": "matrix.eigenspaces doctest description is misleading",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2026",
    "user": "jason"
}
```
Assignee: was

In matrix2.pyx under eigenspaces():


```
        Next we compute the eigenspaces over the finite field
        of order 11:
        
            sage: # A = ModularSymbols(43, base_ring=GF(11), sign=1).T(2).matrix()
            sage: A = matrix(QQ, 4, [3, 9, 0, 0, 0, 9, 0, 1, 0, 10, 9, 2, 0, 9, 0, 2])
```


It seems like the description should be deleted or the doctest should be run and the output included.


Issue created by migration from https://trac.sagemath.org/ticket/2026





---

archive/issue_comments_013105.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-02-01T23:02:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2026",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2026#issuecomment-13105",
    "user": "was"
}
```

Changing status from new to assigned.



---

archive/issue_comments_013106.json:
```json
{
    "body": "Attachment [trac-2026.patch](tarball://root/attachments/some-uuid/ticket2026/trac-2026.patch) by was created at 2008-02-01 23:11:04",
    "created_at": "2008-02-01T23:11:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2026",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2026#issuecomment-13106",
    "user": "was"
}
```

Attachment [trac-2026.patch](tarball://root/attachments/some-uuid/ticket2026/trac-2026.patch) by was created at 2008-02-01 23:11:04



---

archive/issue_comments_013107.json:
```json
{
    "body": "apply on top of first patch.",
    "created_at": "2008-02-01T23:38:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2026",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2026#issuecomment-13107",
    "user": "jason"
}
```

apply on top of first patch.



---

archive/issue_comments_013108.json:
```json
{
    "body": "Attachment [eigenspace-docs.2.patch](tarball://root/attachments/some-uuid/ticket2026/eigenspace-docs.2.patch) by jason created at 2008-02-01 23:39:21\n\nApply instead of first patch (this includes the first patch)",
    "created_at": "2008-02-01T23:39:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2026",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2026#issuecomment-13108",
    "user": "jason"
}
```

Attachment [eigenspace-docs.2.patch](tarball://root/attachments/some-uuid/ticket2026/eigenspace-docs.2.patch) by jason created at 2008-02-01 23:39:21

Apply instead of first patch (this includes the first patch)



---

archive/issue_comments_013109.json:
```json
{
    "body": "okay, now I've messed all the attachments up.  What I mean is that the third patch \"eigenspace-docs.2.patch\" includes the first patch and the second patch, and so is the only patch that needs applying.  William deserves credit for the first patch, though.",
    "created_at": "2008-02-01T23:40:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2026",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2026#issuecomment-13109",
    "user": "jason"
}
```

okay, now I've messed all the attachments up.  What I mean is that the third patch "eigenspace-docs.2.patch" includes the first patch and the second patch, and so is the only patch that needs applying.  William deserves credit for the first patch, though.



---

archive/issue_comments_013110.json:
```json
{
    "body": "Jason positive reviewed my patch, and I positively review his patch on top of my patch.",
    "created_at": "2008-02-01T23:44:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2026",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2026#issuecomment-13110",
    "user": "was"
}
```

Jason positive reviewed my patch, and I positively review his patch on top of my patch.



---

archive/issue_comments_013111.json:
```json
{
    "body": "Merged eigenspace-docs.2.patch in Sage 2.10.1.rc5",
    "created_at": "2008-02-02T03:18:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2026",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2026#issuecomment-13111",
    "user": "mabshoff"
}
```

Merged eigenspace-docs.2.patch in Sage 2.10.1.rc5



---

archive/issue_comments_013112.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-02T03:18:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2026",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2026#issuecomment-13112",
    "user": "mabshoff"
}
```

Resolution: fixed
