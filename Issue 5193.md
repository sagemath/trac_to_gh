# Issue 5193: [with patch, needs review] maximum allowed matrix size is too big

archive/issues_005193.json:
```json
{
    "body": "Assignee: @williamstein\n\nOn a 32-bit computer, `MatrixSpace` will let you create a matrix space with up to 2<sup>32</sup>-1 rows or columns.  But we use Py_ssize_t for matrix indices, which can only hold numbers up to 2<sup>31</sup>-1.\n\nPatch attached; all doctests pass on a 64-bit computer, and .../matrix_space.py doctests pass on a 32-bit computer.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5193\n\n",
    "created_at": "2009-02-06T03:11:31Z",
    "labels": [
        "component: linear algebra",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "[with patch, needs review] maximum allowed matrix size is too big",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5193",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```
Assignee: @williamstein

On a 32-bit computer, `MatrixSpace` will let you create a matrix space with up to 2<sup>32</sup>-1 rows or columns.  But we use Py_ssize_t for matrix indices, which can only hold numbers up to 2<sup>31</sup>-1.

Patch attached; all doctests pass on a 64-bit computer, and .../matrix_space.py doctests pass on a 32-bit computer.

Issue created by migration from https://trac.sagemath.org/ticket/5193





---

archive/issue_comments_039729.json:
```json
{
    "body": "Attachment [fix-max-matrix-size.patch](tarball://root/attachments/some-uuid/ticket5193/fix-max-matrix-size.patch) by @jasongrout created at 2009-02-06 08:20:41\n\nI think the reasoning is that Py_ssize_t is a signed integer to allow for negative indices.",
    "created_at": "2009-02-06T08:20:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5193",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5193#issuecomment-39729",
    "user": "https://github.com/jasongrout"
}
```

Attachment [fix-max-matrix-size.patch](tarball://root/attachments/some-uuid/ticket5193/fix-max-matrix-size.patch) by @jasongrout created at 2009-02-06 08:20:41

I think the reasoning is that Py_ssize_t is a signed integer to allow for negative indices.



---

archive/issue_comments_039730.json:
```json
{
    "body": "Yep, the reasoning is explained in the patch.  Doctests in matrixspace.py pass on my 32 bit computer.  Positive review.",
    "created_at": "2009-02-06T08:23:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5193",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5193#issuecomment-39730",
    "user": "https://github.com/jasongrout"
}
```

Yep, the reasoning is explained in the patch.  Doctests in matrixspace.py pass on my 32 bit computer.  Positive review.



---

archive/issue_events_005447.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-02-06T22:28:39Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5193",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5193#event-5447"
}
```



---

archive/issue_comments_039731.json:
```json
{
    "body": "Merged in Sage 3.3.alpha6.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-06T22:28:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5193",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5193#issuecomment-39731",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.3.alpha6.

Cheers,

Michael



---

archive/issue_comments_039732.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-06T22:28:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5193",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5193#issuecomment-39732",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
