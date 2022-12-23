# Issue 4961: sage/modules/vector_modn_sparse_c.pxi: allocate_c_vector_modint can leak memory in case of failure

archive/issues_004961.json:
```json
{
    "body": "Assignee: craigcitro\n\nLook at\n\n```\ncdef int allocate_c_vector_modint(c_vector_modint* v, Py_ssize_t num_nonzero) except -1:\n    \"\"\"\n    Allocate memory for a c_vector_modint -- most user code won't call this.\n    \"\"\"\n    v.entries = <int*>sage_malloc(num_nonzero*sizeof(int))\n    if v.entries == NULL:\n        raise MemoryError, \"Error allocating memory\"\n    v.positions = <Py_ssize_t*>sage_malloc(num_nonzero*sizeof(Py_ssize_t))\n    if v.positions == NULL:\n        raise MemoryError, \"Error allocating memory\"\n    return 0\n```\n\n\nWhen the allocation for positions fails we will leak entries.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/4961\n\n",
    "created_at": "2009-01-10T09:55:59Z",
    "labels": [
        "memleak",
        "major",
        "bug"
    ],
    "title": "sage/modules/vector_modn_sparse_c.pxi: allocate_c_vector_modint can leak memory in case of failure",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4961",
    "user": "mabshoff"
}
```
Assignee: craigcitro

Look at

```
cdef int allocate_c_vector_modint(c_vector_modint* v, Py_ssize_t num_nonzero) except -1:
    """
    Allocate memory for a c_vector_modint -- most user code won't call this.
    """
    v.entries = <int*>sage_malloc(num_nonzero*sizeof(int))
    if v.entries == NULL:
        raise MemoryError, "Error allocating memory"
    v.positions = <Py_ssize_t*>sage_malloc(num_nonzero*sizeof(Py_ssize_t))
    if v.positions == NULL:
        raise MemoryError, "Error allocating memory"
    return 0
```


When the allocation for positions fails we will leak entries.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/4961





---

archive/issue_comments_037706.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-01-23T15:19:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4961",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4961#issuecomment-37706",
    "user": "rlm"
}
```

Attachment



---

archive/issue_comments_037707.json:
```json
{
    "body": "Positive review.\n\nCheers,\n\nMichael",
    "created_at": "2009-01-23T16:20:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4961",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4961#issuecomment-37707",
    "user": "mabshoff"
}
```

Positive review.

Cheers,

Michael



---

archive/issue_comments_037708.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-24T13:17:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4961",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4961#issuecomment-37708",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_037709.json:
```json
{
    "body": "Merged in Sage 3.3.alpha2",
    "created_at": "2009-01-24T13:17:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4961",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4961#issuecomment-37709",
    "user": "mabshoff"
}
```

Merged in Sage 3.3.alpha2
