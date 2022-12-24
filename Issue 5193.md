# Issue 5193: [with patch, needs review] maximum allowed matrix size is too big

archive/issues_005193.json:
```json
{
    "body": "Assignee: was\n\nOn a 32-bit computer, `MatrixSpace` will let you create a matrix space with up to 2<sup>32</sup>-1 rows or columns.  But we use Py_ssize_t for matrix indices, which can only hold numbers up to 2<sup>31</sup>-1.\n\nPatch attached; all doctests pass on a 64-bit computer, and .../matrix_space.py doctests pass on a 32-bit computer.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5193\n\n",
    "created_at": "2009-02-06T03:11:31Z",
    "labels": [
        "linear algebra",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "[with patch, needs review] maximum allowed matrix size is too big",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5193",
    "user": "cwitty"
}
```
Assignee: was

On a 32-bit computer, `MatrixSpace` will let you create a matrix space with up to 2<sup>32</sup>-1 rows or columns.  But we use Py_ssize_t for matrix indices, which can only hold numbers up to 2<sup>31</sup>-1.

Patch attached; all doctests pass on a 64-bit computer, and .../matrix_space.py doctests pass on a 32-bit computer.

Issue created by migration from https://trac.sagemath.org/ticket/5193





---

archive/issue_comments_039807.json:
```json
{
    "body": "Attachment [fix-max-matrix-size.patch](tarball://root/attachments/some-uuid/ticket5193/fix-max-matrix-size.patch) by jason created at 2009-02-06 08:20:41\n\nI think the reasoning is that Py_ssize_t is a signed integer to allow for negative indices.",
    "created_at": "2009-02-06T08:20:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5193",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5193#issuecomment-39807",
    "user": "jason"
}
```

Attachment [fix-max-matrix-size.patch](tarball://root/attachments/some-uuid/ticket5193/fix-max-matrix-size.patch) by jason created at 2009-02-06 08:20:41

I think the reasoning is that Py_ssize_t is a signed integer to allow for negative indices.



---

archive/issue_comments_039808.json:
```json
{
    "body": "Yep, the reasoning is explained in the patch.  Doctests in matrixspace.py pass on my 32 bit computer.  Positive review.",
    "created_at": "2009-02-06T08:23:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5193",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5193#issuecomment-39808",
    "user": "jason"
}
```

Yep, the reasoning is explained in the patch.  Doctests in matrixspace.py pass on my 32 bit computer.  Positive review.



---

archive/issue_comments_039809.json:
```json
{
    "body": "Merged in Sage 3.3.alpha6.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-06T22:28:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5193",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5193#issuecomment-39809",
    "user": "mabshoff"
}
```

Merged in Sage 3.3.alpha6.

Cheers,

Michael



---

archive/issue_comments_039810.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-06T22:28:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5193",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5193#issuecomment-39810",
    "user": "mabshoff"
}
```

Resolution: fixed
