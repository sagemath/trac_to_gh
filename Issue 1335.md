# Issue 1335: [with patch] 2.8.14/Linux PPC: lcalc doctest failure

archive/issues_001335.json:
```json
{
    "body": "Assignee: mabshoff\n\nOn my Linux PPC 32 bit box I got the following doctest failure due to numerical noise:\n\n```\nFile \"lcalc.py\", line 188:\n    sage: E.Lseries().values_along_line(0.5, 3, 5)\nExpected:\n    lcalc:  1.5 0 WARNING- we don't have enough Dirichlet coefficients.\n    lcalc:  Will use the maximum possible, though the output will not necessarily be accurate.\n    lcalc:  nan nan\n    [(0, 0.209951303),\n     (0.500000000, -2...e-16),\n     (1.00000000, 0.133768433),\n     (2.00000000, 0.552975867)]\nGot:\n    lcalc:  1.5 0 WARNING- we don't have enough Dirichlet coefficients.\n    lcalc:  Will use the maximum possible, though the output will not necessarily be accurate.\n    lcalc:  nan nan\n    [(0, 0.209951303), (0.500000000, -3.16949699e-16), (1.00000000, 0.133768433), (2.00000000, 0.552975867)]\n```\n\n\nThe attached patch fixes that.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/1335\n\n",
    "created_at": "2007-11-29T09:40:03Z",
    "labels": [
        "doctest coverage",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.15",
    "title": "[with patch] 2.8.14/Linux PPC: lcalc doctest failure",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1335",
    "user": "mabshoff"
}
```
Assignee: mabshoff

On my Linux PPC 32 bit box I got the following doctest failure due to numerical noise:

```
File "lcalc.py", line 188:
    sage: E.Lseries().values_along_line(0.5, 3, 5)
Expected:
    lcalc:  1.5 0 WARNING- we don't have enough Dirichlet coefficients.
    lcalc:  Will use the maximum possible, though the output will not necessarily be accurate.
    lcalc:  nan nan
    [(0, 0.209951303),
     (0.500000000, -2...e-16),
     (1.00000000, 0.133768433),
     (2.00000000, 0.552975867)]
Got:
    lcalc:  1.5 0 WARNING- we don't have enough Dirichlet coefficients.
    lcalc:  Will use the maximum possible, though the output will not necessarily be accurate.
    lcalc:  nan nan
    [(0, 0.209951303), (0.500000000, -3.16949699e-16), (1.00000000, 0.133768433), (2.00000000, 0.552975867)]
```


The attached patch fixes that.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/1335





---

archive/issue_comments_008538.json:
```json
{
    "body": "Attachment [Sage-2.8.14-lcalc-doctest-fix-PPCLinux.patch](tarball://root/attachments/some-uuid/ticket1335/Sage-2.8.14-lcalc-doctest-fix-PPCLinux.patch) by mabshoff created at 2007-11-29 09:40:18",
    "created_at": "2007-11-29T09:40:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1335#issuecomment-8538",
    "user": "mabshoff"
}
```

Attachment [Sage-2.8.14-lcalc-doctest-fix-PPCLinux.patch](tarball://root/attachments/some-uuid/ticket1335/Sage-2.8.14-lcalc-doctest-fix-PPCLinux.patch) by mabshoff created at 2007-11-29 09:40:18



---

archive/issue_comments_008539.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-11-29T09:42:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1335#issuecomment-8539",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_008540.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2007-12-01T02:23:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1335#issuecomment-8540",
    "user": "cwitty"
}
```

Looks good to me.



---

archive/issue_comments_008541.json:
```json
{
    "body": "Merged in 2.8.15.alpha0.",
    "created_at": "2007-12-01T11:25:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1335#issuecomment-8541",
    "user": "mabshoff"
}
```

Merged in 2.8.15.alpha0.



---

archive/issue_comments_008542.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-01T11:25:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1335#issuecomment-8542",
    "user": "mabshoff"
}
```

Resolution: fixed
