# Issue 1336: [with patch] 2.8.14/Linux PPC: rings/polynomial/polynomial_element.pyx doctest failure

archive/issues_001336.json:
```json
{
    "body": "Assignee: mabshoff\n\nOn Linux PPC the following doctest fails due to numerical noise:\n\n```\nFile \"polynomial_element.pyx\", line 2371:\n    sage: f.roots(multiplicities=False)\nExpected:\n    [-1.6772670339941..., 0.199954796285..., 0.200045306115..., 1.5763035161844...]\nGot:\n    [-1.67726703399418, 0.199954796284890, 0.200045306115409, 1.57630351618444]\n```\n\n\nThe attached patch fixes that.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/1336\n\n",
    "created_at": "2007-11-29T09:42:06Z",
    "labels": [
        "doctest coverage",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.15",
    "title": "[with patch] 2.8.14/Linux PPC: rings/polynomial/polynomial_element.pyx doctest failure",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1336",
    "user": "mabshoff"
}
```
Assignee: mabshoff

On Linux PPC the following doctest fails due to numerical noise:

```
File "polynomial_element.pyx", line 2371:
    sage: f.roots(multiplicities=False)
Expected:
    [-1.6772670339941..., 0.199954796285..., 0.200045306115..., 1.5763035161844...]
Got:
    [-1.67726703399418, 0.199954796284890, 0.200045306115409, 1.57630351618444]
```


The attached patch fixes that.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/1336





---

archive/issue_comments_008543.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-11-29T09:42:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1336",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1336#issuecomment-8543",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_008544.json:
```json
{
    "body": "Attachment [Sage-2.8.14-polynomial_element-doctest-fix-PPCLinux.patch](tarball://root/attachments/some-uuid/ticket1336/Sage-2.8.14-polynomial_element-doctest-fix-PPCLinux.patch) by mabshoff created at 2007-11-29 09:42:40",
    "created_at": "2007-11-29T09:42:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1336",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1336#issuecomment-8544",
    "user": "mabshoff"
}
```

Attachment [Sage-2.8.14-polynomial_element-doctest-fix-PPCLinux.patch](tarball://root/attachments/some-uuid/ticket1336/Sage-2.8.14-polynomial_element-doctest-fix-PPCLinux.patch) by mabshoff created at 2007-11-29 09:42:40



---

archive/issue_comments_008545.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2007-12-01T02:26:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1336",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1336#issuecomment-8545",
    "user": "cwitty"
}
```

Looks good to me.



---

archive/issue_comments_008546.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-01T11:23:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1336",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1336#issuecomment-8546",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_008547.json:
```json
{
    "body": "Merged in 2.8.15.alpha0.",
    "created_at": "2007-12-01T11:23:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1336",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1336#issuecomment-8547",
    "user": "mabshoff"
}
```

Merged in 2.8.15.alpha0.
