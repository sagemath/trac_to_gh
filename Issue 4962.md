# Issue 4962: sage/modules/vector_modn_sparse_c.pxi: init_c_vector_modint leaks leak memory in case of OverflowError

archive/issues_004962.json:
```json
{
    "body": "Assignee: craigcitro\n\nLook at:\n\n```\ncdef int init_c_vector_modint(c_vector_modint* v, int p, Py_ssize_t degree,\n                              Py_ssize_t num_nonzero) except -1:\n    \"\"\"\n    Initialize a c_vector_modint.\n    \"\"\"\n    if (allocate_c_vector_modint(v, num_nonzero) == -1):\n        raise MemoryError, \"Error allocating memory for sparse vector.\"\n    if p > 46340:\n        raise OverflowError, \"The prime must be <= 46340.\"\n    v.num_nonzero = num_nonzero\n    v.degree = degree\n    v.p = p\n    return 0\n```\n\nOn OverflowError v is leaked. Switching check and allocation will fix the problem.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/4962\n\n",
    "created_at": "2009-01-10T10:01:20Z",
    "labels": [
        "memleak",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "sage/modules/vector_modn_sparse_c.pxi: init_c_vector_modint leaks leak memory in case of OverflowError",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4962",
    "user": "mabshoff"
}
```
Assignee: craigcitro

Look at:

```
cdef int init_c_vector_modint(c_vector_modint* v, int p, Py_ssize_t degree,
                              Py_ssize_t num_nonzero) except -1:
    """
    Initialize a c_vector_modint.
    """
    if (allocate_c_vector_modint(v, num_nonzero) == -1):
        raise MemoryError, "Error allocating memory for sparse vector."
    if p > 46340:
        raise OverflowError, "The prime must be <= 46340."
    v.num_nonzero = num_nonzero
    v.degree = degree
    v.p = p
    return 0
```

On OverflowError v is leaked. Switching check and allocation will fix the problem.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/4962





---

archive/issue_comments_037710.json:
```json
{
    "body": "Attachment [trac-4962.patch](tarball://root/attachments/some-uuid/ticket4962/trac-4962.patch) by rlm created at 2009-01-23 15:23:18",
    "created_at": "2009-01-23T15:23:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4962",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4962#issuecomment-37710",
    "user": "rlm"
}
```

Attachment [trac-4962.patch](tarball://root/attachments/some-uuid/ticket4962/trac-4962.patch) by rlm created at 2009-01-23 15:23:18



---

archive/issue_comments_037711.json:
```json
{
    "body": "Positive review even though the author did not fix it as I suggested :)\n\nCheers,\n\nMichael",
    "created_at": "2009-01-23T16:19:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4962",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4962#issuecomment-37711",
    "user": "mabshoff"
}
```

Positive review even though the author did not fix it as I suggested :)

Cheers,

Michael



---

archive/issue_comments_037712.json:
```json
{
    "body": "Merged in Sage 3.3.alpha2",
    "created_at": "2009-01-24T13:17:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4962",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4962#issuecomment-37712",
    "user": "mabshoff"
}
```

Merged in Sage 3.3.alpha2



---

archive/issue_comments_037713.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-24T13:17:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4962",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4962#issuecomment-37713",
    "user": "mabshoff"
}
```

Resolution: fixed
