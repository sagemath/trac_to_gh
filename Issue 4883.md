# Issue 4883: possible memory leak in sage.matrix.matrix_integer_dense

archive/issues_004883.json:
```json
{
    "body": "Assignee: mabshoff\n\n\n```\n    def __dealloc__(self):\n        \"\"\"\n        Frees all the memory allocated for this matrix. \n        EXAMPLE:\n            sage: a = Matrix(ZZ,2,[1,2,3,4])\n            sage: del a        \n        \"\"\"\n        cdef Py_ssize_t i\n        if self._initialized:\n            for i from 0 <= i < (self._nrows * self._ncols):\n                mpz_clear(self._entries[i])\n            sage_free(self._entries)\n            sage_free(self._matrix)\n```\n\n\nIt is possible that `_initialized` is not set but `_matrix` and `_entries` are allocated.\n\nError paths in `__new__` and `__init__` should also be revised, since if one raises an error in these functions python still calls `__dealloc__` for the cleanup. \n\nFrom the `__init__` function:\n\n```\n        elif isinstance(entries, (int,long)) or is_Element(entries):\n            try:\n                x = ZZ(entries)\n            except TypeError:\n                self._initialized = False\n                raise TypeError, \"unable to coerce entry to an integer\"\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4883\n\n",
    "created_at": "2008-12-27T00:52:38Z",
    "labels": [
        "memleak",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "possible memory leak in sage.matrix.matrix_integer_dense",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4883",
    "user": "@burcin"
}
```
Assignee: mabshoff


```
    def __dealloc__(self):
        """
        Frees all the memory allocated for this matrix. 
        EXAMPLE:
            sage: a = Matrix(ZZ,2,[1,2,3,4])
            sage: del a        
        """
        cdef Py_ssize_t i
        if self._initialized:
            for i from 0 <= i < (self._nrows * self._ncols):
                mpz_clear(self._entries[i])
            sage_free(self._entries)
            sage_free(self._matrix)
```


It is possible that `_initialized` is not set but `_matrix` and `_entries` are allocated.

Error paths in `__new__` and `__init__` should also be revised, since if one raises an error in these functions python still calls `__dealloc__` for the cleanup. 

From the `__init__` function:

```
        elif isinstance(entries, (int,long)) or is_Element(entries):
            try:
                x = ZZ(entries)
            except TypeError:
                self._initialized = False
                raise TypeError, "unable to coerce entry to an integer"
```


Issue created by migration from https://trac.sagemath.org/ticket/4883





---

archive/issue_comments_037007.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-01-25T19:01:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4883",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4883#issuecomment-37007",
    "user": "@malb"
}
```

Changing status from new to assigned.



---

archive/issue_comments_037008.json:
```json
{
    "body": "Changing assignee from mabshoff to @malb.",
    "created_at": "2009-01-25T19:01:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4883",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4883#issuecomment-37008",
    "user": "@malb"
}
```

Changing assignee from mabshoff to @malb.
